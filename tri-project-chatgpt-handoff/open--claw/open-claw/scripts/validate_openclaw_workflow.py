from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OPEN_CLAW_ROOT = REPO_ROOT / "open-claw"
KB_ROOT = OPEN_CLAW_ROOT / "AI_Employee_knowledgebase"
EMPLOYEE_ROOT = KB_ROOT / "AI_employees"
DEPLOYED_CURATED_ROOT = OPEN_CLAW_ROOT / "employees" / "deployed-curated"
SUMMARY_PATH = KB_ROOT / "RUNTIME_VALIDATION_SUMMARY.md"
DOC_FILES = [
    "README.md",
    "PROVENANCE.md",
    "IDENTITY.md",
    "SOUL.md",
    "AGENTS.md",
    "TOOLS.md",
    "SKILLS.md",
    "WORKFLOWS.md",
    "MEMORY.md",
    "USER.md",
    "BOOTSTRAP.md",
    "HEARTBEAT.md",
    "SCHEDULE.md",
    "CHECKLIST.md",
    "AUDIT.md",
]
RUNTIME_FILES = [
    ".env.example",
    "Dockerfile",
    "docker-compose.yml",
    "entrypoint.sh",
    "setup.sh",
    "package.json",
    "openclaw-runner.js",
    "bot-telegram.js",
    "bot-discord.js",
    "bot-slack.js",
    "bot-whatsapp.js",
    "heartbeat.sh",
]
JS_FILES = [
    "openclaw-runner.js",
    "bot-telegram.js",
    "bot-discord.js",
    "bot-slack.js",
    "bot-whatsapp.js",
]


@dataclass(frozen=True)
class EmployeePacket:
    slug: str
    skills: list[str]



def parse_employees() -> list[EmployeePacket]:
    employees: list[EmployeePacket] = []
    for employee_dir in sorted(path for path in EMPLOYEE_ROOT.iterdir() if path.is_dir() and path.name != "_zips"):
        skills_doc = (employee_dir / "SKILLS.md").read_text(encoding="utf-8")
        skills = [
            match.group(1).strip()
            for match in re.finditer(r"^\s*-\s*`([^`]+)`\s*$", skills_doc, re.MULTILINE)
        ]
        employees.append(EmployeePacket(slug=employee_dir.name, skills=skills))
    return employees



def has_required_files(employee: EmployeePacket) -> bool:
    employee_dir = EMPLOYEE_ROOT / employee.slug
    required = DOC_FILES + RUNTIME_FILES
    return all((employee_dir / name).exists() for name in required)



def has_copied_skills(employee: EmployeePacket) -> bool:
    employee_dir = EMPLOYEE_ROOT / employee.slug
    return all((employee_dir / "skills" / skill / "SKILL.md").exists() for skill in employee.skills)



def checklist_is_fully_checked(employee: EmployeePacket) -> bool:
    text = (EMPLOYEE_ROOT / employee.slug / "CHECKLIST.md").read_text(encoding="utf-8")
    return "- [ ] `" not in text



def node_syntax_ok(employee: EmployeePacket) -> bool:
    employee_dir = EMPLOYEE_ROOT / employee.slug
    for filename in JS_FILES:
        completed = subprocess.run(
            ["node", "--check", str(employee_dir / filename)],
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            return False
    return True



def compose_config_ok(employees: list[EmployeePacket]) -> bool:
    env = os.environ.copy()
    env.setdefault("ANTHROPIC_API_KEY", "test-anthropic")
    env.setdefault("OPENCLAW_GATEWAY_URL", "ws://host.docker.internal:18789")
    env.setdefault("OPENCLAW_GATEWAY_TOKEN", "test-gateway-token")
    for employee in employees:
        env.setdefault(employee.slug.replace("-", "_").upper() + "_TOKEN", "test-token")
    completed = subprocess.run(
        ["docker", "compose", "config"],
        cwd=DEPLOYED_CURATED_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )
    return completed.returncode == 0



def powershell_start_script_ok() -> bool:
    script_path = DEPLOYED_CURATED_ROOT / "start-employees.ps1"
    command = (
        "$errors = @(); "
        f"[void][System.Management.Automation.Language.Parser]::ParseFile('{script_path}', [ref]$null, [ref]$errors); "
        "if ($errors.Count -gt 0) { $errors | ForEach-Object { Write-Output $_.Message }; exit 1 }"
    )
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
    )
    return completed.returncode == 0



def deployed_curated_complete(employees: list[EmployeePacket]) -> bool:
    if not (DEPLOYED_CURATED_ROOT / "docker-compose.yml").exists():
        return False
    if not (DEPLOYED_CURATED_ROOT / "start-employees.ps1").exists():
        return False
    return all((DEPLOYED_CURATED_ROOT / employee.slug).exists() for employee in employees)



def render_summary(results: dict[str, bool], employees: list[EmployeePacket]) -> str:
    lines = "\n".join(f"- **{'PASS' if passed else 'FAIL'}** — {name}" for name, passed in results.items())
    return f"""
# Runtime Validation Summary

## Result Matrix
{lines}

## Employee Count
- Curated employees checked: **{len(employees)}**

## Notes
- Validation covers packet completeness, skill copies, checklist status, generated runtime folders, Docker Compose config parsing, PowerShell startup-script parsing, and Node syntax checks for generated bot files.
- Live channel delivery still depends on real credentials and gateway pairing.
"""



def main() -> None:
    employees = parse_employees()
    results = {
        "curated employee count is 15": len(employees) == 15,
        "every employee has required docs and runtime files": all(has_required_files(employee) for employee in employees),
        "every employee has copied assigned skills": all(has_copied_skills(employee) for employee in employees),
        "every employee checklist has only checked file boxes": all(checklist_is_fully_checked(employee) for employee in employees),
        "generated bot javascript passes node --check": all(node_syntax_ok(employee) for employee in employees),
        "deployed-curated runtime exists for every employee": deployed_curated_complete(employees),
        "deployed-curated docker compose parses": compose_config_ok(employees),
        "generated PowerShell startup script parses": powershell_start_script_ok(),
    }
    SUMMARY_PATH.write_text(render_summary(results, employees).strip() + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))
    if not all(results.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
