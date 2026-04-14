from __future__ import annotations

import json
import re
import shutil
import textwrap
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OPEN_CLAW_ROOT = REPO_ROOT / "open-claw"
KB_ROOT = OPEN_CLAW_ROOT / "AI_Employee_knowledgebase"
AGENCY_ROOT = KB_ROOT / "source_repos" / "agency-agents" / "agency-agents-main"
OUTPUT_ROOT = KB_ROOT / "candidate_employees" / "agency-agents"
SUMMARY_PATH = KB_ROOT / "AGENCY_IMPORT_SUMMARY.md"
MANIFEST_PATH = KB_ROOT / "agency-import-manifest.json"
TODAY = "2026-03-30"
GRADE_RANK = {"A": 5, "A-": 4, "B+": 3, "B": 2, "C+": 1, "C": 0}

EXCLUDED_PREFIXES = {".github", "examples"}
INCLUDED_PREFIXES = {
    "academic",
    "design",
    "engineering",
    "game-development",
    "marketing",
    "paid-media",
    "product",
    "project-management",
    "sales",
    "spatial-computing",
    "specialized",
    "support",
    "testing",
}
REQUIRED_DOCS = [
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
    "UPSTREAM_ROLE.md",
]
RUNTIME_FILES = [
    "Dockerfile",
    "docker-compose.yml",
    "entrypoint.sh",
    "setup.sh",
    ".env.example",
    "package.json",
    "bot-telegram.js",
    "bot-discord.js",
    "bot-slack.js",
    "bot-whatsapp.js",
    "heartbeat.sh",
]


@dataclass(frozen=True)
class AgencyRole:
    slug: str
    title: str
    category: str
    path: Path
    relative_path: str
    description: str
    emoji: str
    vibe: str
    tools: list[str]
    body: str
    headings: list[str]
    skills: list[str]
    grade: str
    summary: str


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    frontmatter_text, body = parts[0][4:], parts[1]
    fields: dict[str, str] = {}
    for line in frontmatter_text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields, body


def slugify(value: str) -> str:
    lowered = value.lower().strip()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-")


def infer_summary(description: str, body: str) -> str:
    if description:
        return description
    first_paragraph = body.strip().split("\n\n", 1)[0].replace("\n", " ").strip()
    return first_paragraph[:220] if first_paragraph else "Imported agency role definition."


def infer_tools(frontmatter_tools: str, title: str, category: str) -> list[str]:
    if frontmatter_tools:
        return [item.strip() for item in frontmatter_tools.split(",") if item.strip()]

    lower = f"{title} {category}".lower()
    tools = ["Context7 docs", "repo search", "artifact review"]
    if any(token in lower for token in ["design", "ux", "ui", "visual"]):
        tools.extend(["browser verification", "screenshot review"])
    if any(token in lower for token in ["engineer", "developer", "architect", "sre", "security"]):
        tools.extend(["git review", "test output", "terminal verification"])
    if any(token in lower for token in ["marketing", "seo", "content", "growth"]):
        tools.extend(["web research", "metadata review"])
    return tools


def infer_skills(path_text: str, title: str, body: str) -> list[str]:
    lower = f"{path_text} {title} {body[:800]}".lower()
    skills: list[str] = []

    def add(skill: str) -> None:
        if skill not in skills:
            skills.append(skill)

    add("handoff-state")

    if any(token in lower for token in ["frontend", "next", "seo", "cms", "landing", "route", "metadata"]):
        add("nextjs-app-router")
    if any(token in lower for token in ["ux", "ui", "design", "brand", "visual", "theme"]):
        add("design-token-theming")
    if any(token in lower for token in ["qa", "evidence", "playwright", "accessibility", "test", "browser"]):
        add("playwright-e2e")
        add("visual-qa-evidence")
    if any(token in lower for token in ["architect", "backend", "system", "schema", "database", "security", "api", "microservice"]):
        add("architecture-adr")
    if any(token in lower for token in ["mcp", "integration", "api", "connector"]):
        add("mcp-integration")
    if any(token in lower for token in ["review", "audit", "quality", "security"]):
        add("code-review-gate")
    if any(token in lower for token in ["release", "deploy", "devops", "sre", "incident"]):
        add("release-readiness")
    if any(token in lower for token in ["product", "marketing", "seo", "brand", "content", "landing", "startup"]):
        add("repo-clone-rebrand")

    return skills


def grade_role(fields: dict[str, str], body: str, headings: list[str]) -> str:
    lines = len(body.splitlines())
    score = 0
    if fields.get("name"):
        score += 1
    if fields.get("description"):
        score += 1
    if fields.get("color"):
        score += 1
    if lines >= 120:
        score += 3
    elif lines >= 70:
        score += 2
    elif lines >= 35:
        score += 1
    if len(headings) >= 8:
        score += 2
    elif len(headings) >= 4:
        score += 1
    if "```" in body:
        score += 2
    if any(token in body.lower() for token in ["deliverable", "acceptance criteria", "migration", "rollback", "schema", "prd"]):
        score += 1

    if score >= 9:
        return "A"
    if score >= 7:
        return "A-"
    if score >= 5:
        return "B+"
    if score >= 4:
        return "B"
    if score >= 3:
        return "C+"
    return "C"


def collect_roles() -> list[AgencyRole]:
    roles: list[AgencyRole] = []
    for path in sorted(AGENCY_ROOT.rglob("*.md")):
        relative = path.relative_to(AGENCY_ROOT)
        if relative.parts[0] in EXCLUDED_PREFIXES or len(relative.parts) == 1:
            continue
        if relative.parts[0] not in INCLUDED_PREFIXES and relative.as_posix() != "integrations/mcp-memory/backend-architect-with-memory.md":
            continue
        raw = path.read_text(encoding="utf-8")
        fields, body = parse_frontmatter(raw)
        title = fields.get("name") or path.stem.replace("-", " ").title()
        category = relative.parts[0]
        relative_path = relative.as_posix()
        slug = slugify(relative.with_suffix("").as_posix().replace("/", "-"))
        headings = re.findall(r"^##+\s+(.+)$", body, re.MULTILINE)
        description = fields.get("description", "")
        vibe = fields.get("vibe", "")
        summary = infer_summary(description, body)
        tools = infer_tools(fields.get("tools", ""), title, category)
        skills = infer_skills(relative_path, title, body)
        grade = grade_role(fields, body, headings)
        roles.append(
            AgencyRole(
                slug=slug,
                title=title,
                category=category,
                path=path,
                relative_path=relative_path,
                description=description,
                emoji=fields.get("emoji", ""),
                vibe=vibe,
                tools=tools,
                body=body,
                headings=headings,
                skills=skills,
                grade=grade,
                summary=summary,
            )
        )
    return roles


def render_checklist(role: AgencyRole) -> str:
    doc_lines = "\n".join(f"- [x] `{name}`" for name in REQUIRED_DOCS)
    runtime_lines = "\n".join(f"- [ ] `{name}`" for name in RUNTIME_FILES)
    skill_lines = "\n".join(f"- [x] `{name}`" for name in role.skills)
    return f"""
# {role.title} Checklist

## Grade Target
- Current grade: **{role.grade}**
- Target grade for live-runtime readiness: **A**

## Required Docs
{doc_lines}

## Required Runtime Files
{runtime_lines}

## Assigned Skills
{skill_lines}

## Remaining Gaps
- [ ] Runtime shell not yet created for this imported packet.
- [ ] Tool access not yet validated in live OpenClaw/CrewClaw runtime.
- [ ] Role-specific workflows may still need adaptation to this project's website/app delivery focus.
"""


def render_audit(role: AgencyRole) -> str:
    heading_lines = "\n".join(f"- {heading}" for heading in role.headings[:8]) or "- No major headings detected"
    skill_lines = "\n".join(f"- `{skill}`" for skill in role.skills)
    tool_lines = "\n".join(f"- {tool}" for tool in role.tools)
    return f"""
# {role.title} Audit

## Grade
- **Current grade:** {role.grade}

## Why This Role Was Kept
- Strong imported source from `agency-agents`.
- Summary: {role.summary}
- Category: `{role.category}`

## Visible Upstream Strengths
{heading_lines}

## Assigned Skills
{skill_lines}

## Tool Expectations
{tool_lines}

## Missing Before Runtime Readiness
- No runtime shell files exist yet for this imported packet.
- Skills are inferred and still need role-by-role verification.
- Packet is imported and standardized, but not yet proven in a live project flow.

## Verdict
Keep this role as part of the broader employee library. Use it as a high-quality source definition, then adapt or harden it before live deployment.
"""


def render_packet(role: AgencyRole) -> dict[str, str]:
    skill_lines = "\n".join(f"- `{skill}`" for skill in role.skills)
    tool_lines = "\n".join(f"- {tool}" for tool in role.tools)
    headings = "\n".join(f"- {heading}" for heading in role.headings[:10]) or "- Role-specific headings live in `UPSTREAM_ROLE.md`."
    vibe_line = f"- **Vibe:** {role.vibe}" if role.vibe else "- **Vibe:** Specialist imported from agency-agents"
    return {
        "README.md": f"""
# {role.title}

## Role
- **Category:** `{role.category}`
- **Grade:** {role.grade}
- **Summary:** {role.summary}

## Source
- Imported from `agency-agents` via `{role.relative_path}`
- Standardized to the house employee packet format used by this project

## Assigned Skills
{skill_lines}
""",
        "PROVENANCE.md": f"""
# Provenance

## Upstream Source
- `open-claw/AI_Employee_knowledgebase/source_repos/agency-agents/agency-agents-main/{role.relative_path}`

## Import Notes
- Original role file preserved in `UPSTREAM_ROLE.md`
- Standardized using `AI-EMPLOYEE-STANDARD.md`
- Imported on {TODAY}
""",
        "IDENTITY.md": f"""
# Identity

- **Name:** {role.title}
- **Category:** {role.category}
{vibe_line}
- **Operating Date:** {TODAY}
""",
        "SOUL.md": f"""
# {role.title}

## Identity
You are **{role.title}**, an imported specialist packet adapted for the `open--claw` employee library.

## Core Mission
{role.summary}

## Standards
- Stay role-specific and high signal.
- Prefer evidence, clarity, and reusable deliverables.
- Adapt imported quality to this project's modular, testable standards.

## Upstream Depth
See `UPSTREAM_ROLE.md` for the original full role definition.
""",
        "AGENTS.md": f"""
# Operating Rules

## Every Session
1. Read `SOUL.md`, `CHECKLIST.md`, and `WORKFLOWS.md`.
2. Use `UPSTREAM_ROLE.md` when deeper specialist guidance is needed.
3. Keep work modular and evidence-first.
4. Update `AUDIT.md` when role maturity changes.

## Collaboration
- Hand off through `handoff-state` discipline.
- Do not overstate capability; record missing pieces explicitly.
- Prefer adapting the strongest source material over improvising generic filler.
""",
        "TOOLS.md": f"""
# Tools

## Expected Tools
{tool_lines}

## Notes
- Tool expectations come from source frontmatter and role/category inference.
- Validate real tool availability before using this role in live runtime work.
""",
        "SKILLS.md": f"""
# Skills

{skill_lines}

## Notes
- Skills are inferred from role title, path, and source content.
- Refine this file when the role is promoted into the curated active squad.
""",
        "WORKFLOWS.md": f"""
# Workflows

## Imported Focus Areas
{headings}

## Delivery Pattern
1. Start with `UPSTREAM_ROLE.md` for specialist depth.
2. Translate that depth into the house packet structure.
3. Produce evidence and project-specific artifacts.
4. Record gaps before claiming readiness.
""",
        "MEMORY.md": f"""
# Memory

## Keep Track Of
- Proven ways this role helped in real project work.
- Missing pieces that still block runtime readiness.
- Best upstream fragments worth promoting into the curated core squad.
""",
        "USER.md": """
# User Context

The founder wants Apple-quality software and autonomous employees that are genuinely useful, not just well-labeled.
""",
        "BOOTSTRAP.md": """
# Bootstrap

1. Read `SOUL.md` and `UPSTREAM_ROLE.md`.
2. Read `CHECKLIST.md` and `AUDIT.md`.
3. Confirm what is already strong and what still needs adaptation.
4. Do not treat imported quality as finished runtime quality without verification.
""",
        "HEARTBEAT.md": f"""
# Heartbeat

## What To Check
- Whether this role has been adapted beyond imported source quality.
- Whether `CHECKLIST.md` still reflects reality.
- Whether the role should be promoted into the active curated squad.
""",
        "SCHEDULE.md": """
# Schedule

## Cadence
- On import: preserve upstream quality and record provenance.
- On first use: refine skills, tools, and workflows for the actual project.
- Before activation: verify runtime shell and tool reachability.
""",
        "CHECKLIST.md": render_checklist(role),
        "AUDIT.md": render_audit(role),
        "UPSTREAM_ROLE.md": role.path.read_text(encoding="utf-8"),
    }


def render_summary(roles: list[AgencyRole]) -> str:
    category_counts: dict[str, int] = {}
    grade_counts: dict[str, int] = {}
    for role in roles:
        category_counts[role.category] = category_counts.get(role.category, 0) + 1
        grade_counts[role.grade] = grade_counts.get(role.grade, 0) + 1
    category_lines = "\n".join(f"- `{category}`: {count}" for category, count in sorted(category_counts.items()))
    grade_lines = "\n".join(f"- `{grade}`: {count}" for grade, count in sorted(grade_counts.items(), reverse=True))
    top_roles = sorted(roles, key=lambda role: (GRADE_RANK.get(role.grade, -1), len(role.body)), reverse=True)[:15]
    top_lines = "\n".join(
        f"| `{role.slug}` | {role.title} | `{role.category}` | {role.grade} | `{role.relative_path}` |"
        for role in top_roles
    )
    return f"""
# Agency Import Summary

## Imported Role Count
- Total imported packets: **{len(roles)}**

## Category Coverage
{category_lines}

## Grade Distribution
{grade_lines}

## Top Imported Roles
| Packet | Title | Category | Grade | Source |
|---|---|---|---|---|
{top_lines}

## Notes
- Every imported packet preserves the original agency role file in `UPSTREAM_ROLE.md`.
- Every imported packet includes `CHECKLIST.md` and `AUDIT.md`.
- Imported packets are standardized library assets, not live runtime workers yet.
"""


def main() -> None:
    roles = collect_roles()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    ensure_dir(OUTPUT_ROOT)
    for role in roles:
        role_dir = OUTPUT_ROOT / role.slug
        for filename, content in render_packet(role).items():
            write(role_dir / filename, content)
    write(SUMMARY_PATH, render_summary(roles))
    manifest = {
        "generated_on": TODAY,
        "source": "agency-agents",
        "packet_count": len(roles),
        "output_root": OUTPUT_ROOT.relative_to(OPEN_CLAW_ROOT).as_posix(),
        "packets": [role.slug for role in roles],
    }
    write(MANIFEST_PATH, json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
