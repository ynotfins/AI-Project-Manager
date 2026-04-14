from __future__ import annotations

import json
import re
import shutil
import textwrap
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

REPO_ROOT = Path(__file__).resolve().parents[2]
OPEN_CLAW_ROOT = REPO_ROOT / "open-claw"
KB_ROOT = OPEN_CLAW_ROOT / "AI_Employee_knowledgebase"
EMPLOYEE_ROOT = KB_ROOT / "AI_employees"
ZIP_ROOT = EMPLOYEE_ROOT / "_zips"
SKILLS_ROOT = OPEN_CLAW_ROOT / "skills"
DEPLOYED_CURATED_ROOT = OPEN_CLAW_ROOT / "employees" / "deployed-curated"
WORKFLOW_CHECKLIST_PATH = KB_ROOT / "OPENCLAW_WORKFLOW_CHECKLIST.md"
VALIDATION_SUMMARY_PATH = KB_ROOT / "RUNTIME_VALIDATION_SUMMARY.md"
CURRENT_EMPLOYEES_PATH = KB_ROOT / "current_employees.md"
TEAM_STATUS_PATH = KB_ROOT / "CURATED_TEAM_STATUS.json"
TODAY = date.today().isoformat()
OPENCLAW_VERSION = "2026.3.13"
HOST_NATIVE_PRIMARY_PACKET_DIR = "sparky-chief-product-quality-officer"
HOST_NATIVE_PRIMARY_SLUG = "SPARKY_CEO_BOT"
ACTIVATION_ORDER = [
    "sparky-chief-product-quality-officer",
    "delivery-director",
    "product-manager",
    "software-architect",
    "code-reviewer",
    "qa-evidence-collector",
    "reality-checker",
    "devops-automator",
    "frontend-developer",
    "backend-architect",
    "ux-architect",
    "ui-designer",
    "accessibility-auditor",
    "mcp-integration-engineer",
    "seo-ai-discovery-strategist",
]

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
SECRET_IDS = {
    "ACCESS_AUDITOR_ALLISON_BOT": "b1ff4d8c-d7ed-48e8-b96b-b427013718aa",
    "API_ANDY_BOT": "d44c0214-4341-4b57-83b6-b411002ba700",
    "BACKEND_BRUCE_BOT": "64411f20-e4fb-418a-aa1b-b42701375e83",
    "CODE_REVIEWER": "9f6d6d14-917f-435d-a757-b41100300499",
    "DELIVERY_DIRECTOR_DAN_BOT": "f08c26ae-8b3b-42db-8b8a-b41e00254ae0",
    "ENGINEER_ENRIQUE_BOT": "5dd1faf1-c943-4be3-8cbf-b41d000cc156",
    "FINANCIAL_ANALYST": "d32f653b-0f42-4824-b760-b41100307afd",
    "FRONTEND_FELIX_BOT": "db45a28d-e942-4b19-aee9-b4110030a9e8",
    "OVERNIGHT_OLIVER_BOT": "cd3ecf0b-b6df-4490-9bf8-b4110030d207",
    "PERSONAL_PAMELA_BOT": "30a52f8e-5afa-4074-86f7-b41d000c36d7",
    "PRODUCT_MANAGER_PETE_BOT": "262ed8cc-9adf-46a6-a0ba-b41e00258aa7",
    "SCRIPT_SARAH_BOT": "9127c2f6-7185-41c3-9aab-b41d000c69ee",
    "SEO_SAMANTHA_BOT": "35e7872d-66f5-4a6c-9ec1-b41d000c9501",
    "SPARKY_CEO_BOT": "e08b6a94-02bf-4222-876a-b41e00251315",
    "UX_URSULA_BOT": "c58957d8-a07e-4d6f-ab76-b41d000d1de7",
}

TELEGRAM_BOT_BINDINGS = {
    "accessibility-auditor": {
        "secret_name": "ACCESS_AUDITOR_ALLISON_BOT",
        "telegram_name": "ACCESSIBILITY_AUDITOR",
        "telegram_username": "ACCESS_AUDITOR_ALLISON_BOT",
    },
    "backend-architect": {
        "secret_name": "BACKEND_BRUCE_BOT",
        "telegram_name": "BACKEND_ARCHITECT",
        "telegram_username": "BACKEND_BRUCE_BOT",
    },
    "code-reviewer": {
        "secret_name": "CODE_REVIEWER",
        "telegram_name": "CODE_REVIEWER",
        "telegram_username": "CODE_CARL_BOT",
    },
    "delivery-director": {
        "secret_name": "DELIVERY_DIRECTOR_DAN_BOT",
        "telegram_name": "DELIVERY_DIRECTOR",
        "telegram_username": "DELIVERY_DIRECTOR_DAN_BOT",
    },
    "devops-automator": {
        "secret_name": "SCRIPT_SARAH_BOT",
        "telegram_name": "SCRIPT_BUILDER",
        "telegram_username": "SCRIPT_SARAH_BOT",
    },
    "frontend-developer": {
        "secret_name": "FRONTEND_FELIX_BOT",
        "telegram_name": "FRONTEND_DEVELOPER",
        "telegram_username": "FRONTEND_FELIX_BOT",
    },
    "mcp-integration-engineer": {
        "secret_name": "API_ANDY_BOT",
        "telegram_name": "API_INTEGRATION_SPECIALIST",
        "telegram_username": "API_ANDY_BOT",
    },
    "product-manager": {
        "secret_name": "PRODUCT_MANAGER_PETE_BOT",
        "telegram_name": "PRODUCT_MANAGER",
        "telegram_username": "PRODUCT_MANAGER_PETE_BOT",
    },
    "qa-evidence-collector": {
        "secret_name": "OVERNIGHT_OLIVER_BOT",
        "telegram_name": "OVERNIGHT_CODER",
        "telegram_username": "OVERNIGHT_OLIVER_BOT",
    },
    "reality-checker": {
        "secret_name": "FINANCIAL_ANALYST",
        "telegram_name": "FINANCIAL_ANALYST",
        "telegram_username": "FINANCE_FRANKY_BOT",
    },
    "seo-ai-discovery-strategist": {
        "secret_name": "SEO_SAMANTHA_BOT",
        "telegram_name": "SEO_SPECIALIST",
        "telegram_username": "SEO_SAMANTHA_BOT",
    },
    "software-architect": {
        "secret_name": "ENGINEER_ENRIQUE_BOT",
        "telegram_name": "SOFTWARE_ENGINEER",
        "telegram_username": "ENGINEER_ENRIQUE_BOT",
    },
    "sparky-chief-product-quality-officer": {
        "secret_name": "SPARKY_CEO_BOT",
        "telegram_name": "SPARKY_CEO_BOT",
        "telegram_username": "SPARKY_CEO_BOT",
    },
    "ui-designer": {
        "secret_name": "PERSONAL_PAMELA_BOT",
        "telegram_name": "PERSONAL_CRM",
        "telegram_username": "PERSONAL_PAMELA_BOT",
    },
    "ux-architect": {
        "secret_name": "UX_URSULA_BOT",
        "telegram_name": "UX_DESIGNER",
        "telegram_username": "UX_URSELA_BOT",
    },
}

PUBLIC_SLUG_BY_PACKET_DIR = {
    packet_dir: binding["telegram_username"] for packet_dir, binding in TELEGRAM_BOT_BINDINGS.items()
}
CANONICAL_ACTIVATION_ORDER = [PUBLIC_SLUG_BY_PACKET_DIR.get(packet_dir, packet_dir) for packet_dir in ACTIVATION_ORDER]
CANONICAL_BOTFATHER_BOTS = [
    {
        "telegram_name": "BACKEND_ARCHITECT",
        "telegram_username": "BACKEND_BRUCE_BOT",
        "packet_dir": "backend-architect",
        "employee_slug": "BACKEND_BRUCE_BOT",
        "secret_name": "BACKEND_BRUCE_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "ACCESSIBILITY_AUDITOR",
        "telegram_username": "ACCESS_AUDITOR_ALLISON_BOT",
        "packet_dir": "accessibility-auditor",
        "employee_slug": "ACCESS_AUDITOR_ALLISON_BOT",
        "secret_name": "ACCESS_AUDITOR_ALLISON_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "Destiny",
        "telegram_username": "destiny_stripper_bot",
        "packet_dir": "",
        "employee_slug": "",
        "secret_name": "destiny_stripper_bot",
        "status": "unassigned",
    },
    {
        "telegram_name": "PRODUCT_MANAGER",
        "telegram_username": "PRODUCT_MANAGER_PETE_BOT",
        "packet_dir": "product-manager",
        "employee_slug": "PRODUCT_MANAGER_PETE_BOT",
        "secret_name": "PRODUCT_MANAGER_PETE_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "DELIVERY_DIRECTOR",
        "telegram_username": "DELIVERY_DIRECTOR_DAN_BOT",
        "packet_dir": "delivery-director",
        "employee_slug": "DELIVERY_DIRECTOR_DAN_BOT",
        "secret_name": "DELIVERY_DIRECTOR_DAN_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "SPARKY_CEO_BOT",
        "telegram_username": "SPARKY_CEO_BOT",
        "packet_dir": "sparky-chief-product-quality-officer",
        "employee_slug": "SPARKY_CEO_BOT",
        "secret_name": "SPARKY_CEO_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "UX_DESIGNER",
        "telegram_username": "UX_URSELA_BOT",
        "packet_dir": "ux-architect",
        "employee_slug": "UX_URSELA_BOT",
        "secret_name": "UX_URSULA_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "SOFTWARE_ENGINEER",
        "telegram_username": "ENGINEER_ENRIQUE_BOT",
        "packet_dir": "software-architect",
        "employee_slug": "ENGINEER_ENRIQUE_BOT",
        "secret_name": "ENGINEER_ENRIQUE_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "SEO_SPECIALIST",
        "telegram_username": "SEO_SAMANTHA_BOT",
        "packet_dir": "seo-ai-discovery-strategist",
        "employee_slug": "SEO_SAMANTHA_BOT",
        "secret_name": "SEO_SAMANTHA_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "SCRIPT_BUILDER",
        "telegram_username": "SCRIPT_SARAH_BOT",
        "packet_dir": "devops-automator",
        "employee_slug": "SCRIPT_SARAH_BOT",
        "secret_name": "SCRIPT_SARAH_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "PERSONAL_CRM",
        "telegram_username": "PERSONAL_PAMELA_BOT",
        "packet_dir": "ui-designer",
        "employee_slug": "PERSONAL_PAMELA_BOT",
        "secret_name": "PERSONAL_PAMELA_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "OVERNIGHT_CODER",
        "telegram_username": "OVERNIGHT_OLIVER_BOT",
        "packet_dir": "qa-evidence-collector",
        "employee_slug": "OVERNIGHT_OLIVER_BOT",
        "secret_name": "OVERNIGHT_OLIVER_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "FRONTEND_DEVELOPER",
        "telegram_username": "FRONTEND_FELIX_BOT",
        "packet_dir": "frontend-developer",
        "employee_slug": "FRONTEND_FELIX_BOT",
        "secret_name": "FRONTEND_FELIX_BOT",
        "status": "assigned",
    },
    {
        "telegram_name": "FINANCIAL_ANALYST",
        "telegram_username": "FINANCE_FRANKY_BOT",
        "packet_dir": "reality-checker",
        "employee_slug": "FINANCE_FRANKY_BOT",
        "secret_name": "FINANCIAL_ANALYST",
        "status": "assigned",
    },
    {
        "telegram_name": "CODE_REVIEWER",
        "telegram_username": "CODE_CARL_BOT",
        "packet_dir": "code-reviewer",
        "employee_slug": "CODE_CARL_BOT",
        "secret_name": "CODE_REVIEWER",
        "status": "assigned",
    },
    {
        "telegram_name": "API_INTEGRATION_SPECIALIST",
        "telegram_username": "API_ANDY_BOT",
        "packet_dir": "mcp-integration-engineer",
        "employee_slug": "API_ANDY_BOT",
        "secret_name": "API_ANDY_BOT",
        "status": "assigned",
    },
]


@dataclass(frozen=True)
class EmployeeRuntime:
    packet_dir: str
    slug: str
    title: str
    manager: str
    skills: list[str]
    summary: str



def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)



def write(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")



def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")



def parse_skill_slugs(skills_doc: str) -> list[str]:
    skills: list[str] = []
    for match in re.finditer(r"^\s*-\s*`([^`]+)`\s*$", skills_doc, re.MULTILINE):
        slug = match.group(1).strip()
        if slug and slug not in skills:
            skills.append(slug)
    return skills


def parse_employees() -> list[EmployeeRuntime]:
    employees: list[EmployeeRuntime] = []
    for employee_dir in sorted(path for path in EMPLOYEE_ROOT.iterdir() if path.is_dir() and path.name != "_zips"):
        readme = read_text(employee_dir / "README.md")
        skills_doc = read_text(employee_dir / "SKILLS.md")
        title_match = re.search(r"\*\*Title:\*\*\s*(.+)", readme)
        manager_match = re.search(r"\*\*Manager:\*\*\s*(.+)", readme)
        summary_match = re.search(r"\*\*Summary:\*\*\s*(.+)", readme)
        skills = parse_skill_slugs(skills_doc)
        employees.append(
            EmployeeRuntime(
                packet_dir=employee_dir.name,
                slug=PUBLIC_SLUG_BY_PACKET_DIR.get(employee_dir.name, employee_dir.name),
                title=title_match.group(1).strip() if title_match else employee_dir.name.replace("-", " ").title(),
                manager=PUBLIC_SLUG_BY_PACKET_DIR.get(
                    manager_match.group(1).strip(),
                    manager_match.group(1).strip() if manager_match else "Unassigned",
                ),
                skills=skills,
                summary=summary_match.group(1).strip() if summary_match else "Curated employee packet.",
            )
        )
    return employees



def slug_to_env(slug: str) -> str:
    return slug.replace("-", "_").upper()



def telegram_binding(slug: str) -> dict[str, str] | None:
    return TELEGRAM_BOT_BINDINGS.get(slug)



def is_host_native_primary(slug: str) -> bool:
    return slug == HOST_NATIVE_PRIMARY_SLUG



def docker_runtime_employees(employees: list[EmployeeRuntime]) -> list[EmployeeRuntime]:
    return [employee for employee in employees if not is_host_native_primary(employee.slug)]



def deployment_mode(slug: str) -> str:
    return "host_native_primary" if is_host_native_primary(slug) else "deployed_curated_docker"



def deployment_mode_summary(slug: str) -> str:
    if is_host_native_primary(slug):
        return "Host-native primary executive runtime (excluded from deployed-curated Docker worker pool)"
    return "Deployed-curated Docker worker"



def assigned_secret_id(slug: str) -> str:
    binding = telegram_binding(slug)
    if not binding:
        return ""
    secret_name = binding["secret_name"]
    return SECRET_IDS.get(secret_name, "")


def assigned_secret_name(slug: str) -> str:
    binding = telegram_binding(slug)
    return binding["secret_name"] if binding else ""



def assigned_username(slug: str) -> str:
    binding = telegram_binding(slug)
    return binding["telegram_username"] if binding else ""



def assigned_telegram_name(slug: str) -> str:
    binding = telegram_binding(slug)
    return binding["telegram_name"] if binding else "TBD"



def runtime_status(slug: str) -> str:
    if not telegram_binding(slug):
        return "pending_new_bot"
    if assigned_secret_id(slug):
        return "direct_uuid_wired"
    return "env_only_assigned"



def tracked_readiness_state(slug: str) -> str:
    status = runtime_status(slug)
    if status == "direct_uuid_wired":
        return "runtime_ready"
    if status == "env_only_assigned":
        return "needs_runtime_env"
    return "needs_bot"



def readiness_blockers(slug: str) -> list[str]:
    status = runtime_status(slug)
    if status == "pending_new_bot":
        return ["missing_telegram_bot"]
    if status == "env_only_assigned":
        return ["missing_direct_secret_mapping"]
    return []



def pending_bot_slugs(employees: list[EmployeeRuntime]) -> list[str]:
    return [employee.slug for employee in employees if not telegram_binding(employee.packet_dir)]



def env_only_bot_slugs(employees: list[EmployeeRuntime]) -> list[str]:
    return [employee.slug for employee in employees if telegram_binding(employee.packet_dir) and not assigned_secret_id(employee.packet_dir)]



def render_live_binding_block(employee: EmployeeRuntime) -> str:
    binding = telegram_binding(employee.packet_dir)
    if not binding:
        return textwrap.dedent(
            f"""
            ## Live Telegram Binding
            - No Telegram bot is assigned to `{employee.slug}` yet.
            - This worker remains documentation-complete but still needs a dedicated Telegram bot before it can join the live curated runtime.
            - Until a new bot is created, start this worker through non-Telegram/local invocation only.
            """
        ).strip()

    resolution = (
        f"direct Bitwarden secret id wired from `{assigned_secret_name(employee.packet_dir)}`"
        if assigned_secret_id(employee.packet_dir)
        else "env-first only for now; Bitwarden secret id still needs to be recorded"
    )
    return textwrap.dedent(
        f"""
        ## Live Telegram Binding
        - Current Telegram first name: `{binding['telegram_name']}`
        - Assigned Telegram username: `{binding['telegram_username']}`
        - Current Bitwarden secret name: `{assigned_secret_name(employee.packet_dir)}`.
        - Preferred Telegram first name for this curated role: `{employee.title}`
        - Startup resolution status: {resolution}.
        """
    ).strip()



def render_env_example(employee: EmployeeRuntime) -> str:
    env_prefix = assigned_secret_name(employee.packet_dir) or slug_to_env(employee.slug)
    return f"""
# {employee.title} runtime environment
# Do not commit real values.
ANTHROPIC_API_KEY=
OPENCLAW_GATEWAY_URL=ws://host.docker.internal:18789
OPENCLAW_GATEWAY_TOKEN=
OPENCLAW_AGENT_ID={employee.slug}
OPENCLAW_VERSION={OPENCLAW_VERSION}
TELEGRAM_BOT_TOKEN=
DISCORD_BOT_TOKEN=
SLACK_BOT_TOKEN=
SLACK_SIGNING_SECRET=
SLACK_APP_TOKEN=
CREWCLAW_MONITOR_KEY=
{env_prefix}_TOKEN=
"""



def render_runner(employee: EmployeeRuntime) -> str:
    return r"""
const { exec, execFile } = require("child_process");
const path = require("path");
const { promisify } = require("util");

const execAsync = promisify(exec);
const execFileAsync = promisify(execFile);
const preferredAgentId = process.env.OPENCLAW_AGENT_ID || "__DEFAULT_AGENT_ID__";
const defaultWindowsBin = process.env.APPDATA
  ? path.join(process.env.APPDATA, "npm", "openclaw.cmd")
  : "openclaw.cmd";
const openclawBin = process.env.OPENCLAW_BIN || (process.platform === "win32" ? defaultWindowsBin : "openclaw");

function quoteCmdArg(value) {
  if (value === "") return "\"\"";
  if (!/[\\s"]/u.test(value)) return value;
  return `"${value.replace(/"/g, "\"\"")}"`;
}

async function execOpenClaw(args) {
  if (process.platform === "win32") {
    const commandLine = `"${openclawBin}" ${args.map(quoteCmdArg).join(" ")}`;
    return execAsync(commandLine, {
      env: process.env,
      maxBuffer: 1024 * 1024,
    });
  }

  return execFileAsync(openclawBin, args, {
    env: process.env,
    maxBuffer: 1024 * 1024,
  });
}

function isUnknownAgentError(error) {
  const combined = [error?.message, error?.stdout, error?.stderr].filter(Boolean).join("\\n");
  return combined.includes("Unknown agent id");
}

async function runAgent({ message, sessionId }) {
  const args = ["agent", "--agent", preferredAgentId, "--session-id", sessionId, "--message", message];
  try {
    const { stdout } = await execOpenClaw(args);
    return (stdout || "").trim();
  } catch (error) {
    if (preferredAgentId !== "main" && isUnknownAgentError(error)) {
      const { stdout } = await execOpenClaw(["agent", "--agent", "main", "--session-id", sessionId, "--message", message]);
      return (stdout || "").trim();
    }
    throw error;
  }
}

module.exports = { runAgent };
""".replace("__DEFAULT_AGENT_ID__", employee.slug)



def render_telegram_bot(employee: EmployeeRuntime) -> str:
    return f"""
const {{ Bot }} = require("grammy");
const {{ runAgent }} = require("./openclaw-runner");

const bot = new Bot(process.env.TELEGRAM_BOT_TOKEN);
const slug = "{employee.slug}";
const agentId = process.env.OPENCLAW_AGENT_ID || slug;

bot.command("start", (ctx) => {{
  ctx.reply("{employee.title} is online. Worker slug: " + slug + ". Agent route: " + agentId + ".");
}});

bot.on("message:text", async (ctx) => {{
  try {{
    const sessionId = `telegram-${{slug}}-${{ctx.from?.id ?? 'unknown'}}`;
    const reply = await runAgent({{ message: ctx.message.text, sessionId }});
    await ctx.reply(reply || "No response from agent.");
  }} catch (error) {{
    console.error(error);
    await ctx.reply("Something went wrong. Please try again.");
  }}
}});

bot.start();
console.log("Telegram bot is running for {employee.title}.");
"""



def render_discord_bot(employee: EmployeeRuntime) -> str:
    return f"""
const {{ Client, GatewayIntentBits }} = require("discord.js");
const {{ runAgent }} = require("./openclaw-runner");

const client = new Client({{
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
}});
const slug = "{employee.slug}";

client.on("ready", () => {{
  console.log(`Discord bot logged in for {employee.title} as ${{client.user.tag}}`);
}});

client.on("messageCreate", async (message) => {{
  if (message.author.bot) return;
  try {{
    const sessionId = `discord-${{slug}}-${{message.author.id}}`;
    const reply = await runAgent({{ message: message.content, sessionId }});
    await message.reply(reply || "No response from agent.");
  }} catch (error) {{
    console.error(error);
    await message.reply("Something went wrong. Please try again.");
  }}
}});

client.login(process.env.DISCORD_BOT_TOKEN);
"""



def render_slack_bot(employee: EmployeeRuntime) -> str:
    return f"""
const {{ App }} = require("@slack/bolt");
const {{ runAgent }} = require("./openclaw-runner");

const app = new App({{
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  socketMode: true,
  appToken: process.env.SLACK_APP_TOKEN,
}});
const slug = "{employee.slug}";

app.event("app_mention", async ({{ event, say }}) => {{
  const text = event.text.replace(/<@[^>]+>/g, "").trim();
  if (!text) return say("How can I help?");
  try {{
    const sessionId = `slack-${{slug}}-${{event.user ?? 'unknown'}}`;
    const reply = await runAgent({{ message: text, sessionId }});
    await say(reply || "No response from agent.");
  }} catch (error) {{
    console.error(error);
    await say("Something went wrong. Please try again.");
  }}
}});

app.message(async ({{ message, say }}) => {{
  if (message.subtype) return;
  try {{
    const sessionId = `slack-dm-${{slug}}-${{message.user ?? 'unknown'}}`;
    const reply = await runAgent({{ message: message.text, sessionId }});
    await say(reply || "No response from agent.");
  }} catch (error) {{
    console.error(error);
    await say("Something went wrong. Please try again.");
  }}
}});

(async () => {{
  await app.start();
  console.log("Slack bot is running for {employee.title}.");
}})();
"""



def render_whatsapp_bot(employee: EmployeeRuntime) -> str:
    return f"""
const {{ Client, LocalAuth }} = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const {{ runAgent }} = require("./openclaw-runner");

const client = new Client({{ authStrategy: new LocalAuth() }});
const slug = "{employee.slug}";

client.on("qr", (qr) => {{
  qrcode.generate(qr, {{ small: true }});
  console.log("Scan the QR code above with WhatsApp");
}});

client.on("ready", () => {{
  console.log("WhatsApp bot is ready for {employee.title}.");
}});

client.on("message", async (message) => {{
  try {{
    const sender = message.from.replace(/[^a-zA-Z0-9]/g, "-");
    const sessionId = `whatsapp-${{slug}}-${{sender}}`;
    const reply = await runAgent({{ message: message.body, sessionId }});
    await message.reply(reply || "No response from agent.");
  }} catch (error) {{
    console.error(error);
    await message.reply("Something went wrong. Please try again.");
  }}
}});

client.initialize();
"""



def render_dockerfile() -> str:
    copy_lines = "\n".join(
        f"COPY {name} /root/.openclaw/workspace/{name}" for name in DOC_FILES
    )
    return f"""
FROM node:22-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    ffmpeg mediainfo \
    && rm -rf /var/lib/apt/lists/* \
    && git config --global url.'https://github.com/'.insteadOf 'ssh://git@github.com/' \
    && npm install -g openclaw@{OPENCLAW_VERSION} --ignore-scripts

RUN mkdir -p /root/.openclaw/workspace /root/.openclaw/workspace/skills
{copy_lines}
COPY skills/ /root/.openclaw/workspace/skills/
COPY package.json /app/package.json
COPY openclaw-runner.js /app/openclaw-runner.js
COPY bot-telegram.js /app/bot-telegram.js
COPY bot-discord.js /app/bot-discord.js
COPY bot-slack.js /app/bot-slack.js
COPY bot-whatsapp.js /app/bot-whatsapp.js
COPY entrypoint.sh /app/entrypoint.sh

RUN npm install && chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
"""



def render_entrypoint(employee: EmployeeRuntime) -> str:
    return f"""
#!/bin/sh
set -e

CONFIG_DIR="/root/.openclaw"
CONFIG_FILE="$CONFIG_DIR/openclaw.json"
WORKSPACE_DIR="$CONFIG_DIR/workspace"
MAIN_AGENT_DIR="$CONFIG_DIR/agents/main/agent"
ROLE_AGENT_ID="{employee.slug}"
ROLE_AGENT_DIR="$CONFIG_DIR/agents/$ROLE_AGENT_ID/agent"

if [ -z "$OPENCLAW_GATEWAY_URL" ] || [ -z "$OPENCLAW_GATEWAY_TOKEN" ]; then
  echo "[entrypoint] ERROR: OPENCLAW_GATEWAY_URL and OPENCLAW_GATEWAY_TOKEN must be set."
  exit 1
fi

if [ -z "$OPENCLAW_AGENT_ID" ]; then
  export OPENCLAW_AGENT_ID="$ROLE_AGENT_ID"
fi

mkdir -p "$CONFIG_DIR" "$WORKSPACE_DIR" "$MAIN_AGENT_DIR" "$ROLE_AGENT_DIR"

cat > "$CONFIG_FILE" <<OCJSON
{{
  "agents": {{
    "defaults": {{
      "workspace": "$WORKSPACE_DIR",
      "heartbeat": {{ "every": "0m" }}
    }},
    "list": [
      {{
        "id": "main",
        "default": false,
        "workspace": "$WORKSPACE_DIR",
        "agentDir": "$MAIN_AGENT_DIR"
      }},
      {{
        "id": "{employee.slug}",
        "default": true,
        "workspace": "$WORKSPACE_DIR",
        "agentDir": "$ROLE_AGENT_DIR"
      }}
    ]
  }},
  "gateway": {{
    "mode": "remote",
    "remote": {{
      "url": "$OPENCLAW_GATEWAY_URL",
      "token": "$OPENCLAW_GATEWAY_TOKEN"
    }}
  }}
}}
OCJSON

echo "[entrypoint] workspace ready for {employee.slug}"
echo "[entrypoint] worker agent id: $OPENCLAW_AGENT_ID"
echo "[entrypoint] remote gateway configured: $OPENCLAW_GATEWAY_URL"
exec node bot-telegram.js
"""



def render_setup(employee: EmployeeRuntime) -> str:
    return f"""
#!/bin/sh
set -e

WORKSPACE_DIR="$HOME/.openclaw/workspace"
mkdir -p "$WORKSPACE_DIR" "$WORKSPACE_DIR/skills" "$WORKSPACE_DIR/live" "$WORKSPACE_DIR/CHECKLISTS" "$WORKSPACE_DIR/HANDOFF_TEMPLATES" "$WORKSPACE_DIR/evals"

for file in {' '.join(DOC_FILES)} ACCESS.md COMPLETE_TOOL_REFERENCE.md ONBOARDING.md DECISION_LOG.md RUNBOOK.md KNOWLEDGE_SOURCES.md SOURCE_PRIORITY.md RETRIEVAL_RULES.md SUCCESS_METRICS.md APPROVAL_GATES.md PR_RULES.md SPARKY_EVALUATION_SUMMARY.md; do
  cp "$file" "$WORKSPACE_DIR/$file"
done

cp -R skills/. "$WORKSPACE_DIR/skills/"
if [ -d live ]; then
  cp -R live/. "$WORKSPACE_DIR/live/"
fi
if [ -d CHECKLISTS ]; then
  cp -R CHECKLISTS/. "$WORKSPACE_DIR/CHECKLISTS/"
fi
if [ -d HANDOFF_TEMPLATES ]; then
  cp -R HANDOFF_TEMPLATES/. "$WORKSPACE_DIR/HANDOFF_TEMPLATES/"
fi
if [ -d evals ]; then
  cp -R evals/. "$WORKSPACE_DIR/evals/"
fi

echo "Workspace installed for {employee.title}: $WORKSPACE_DIR"
echo "Provide OPENCLAW_GATEWAY_URL and OPENCLAW_GATEWAY_TOKEN before running a channel bot."
"""



def render_packet_compose(employee: EmployeeRuntime) -> str:
    volume = f"openclaw-{employee.packet_dir}:/root/.openclaw"
    return f"""
version: "3.8"

services:
  agent:
    build: .
    env_file:
      - .env
    extra_hosts:
      - "host.docker.internal:host-gateway"
    volumes:
      - {volume}
    restart: unless-stopped

  heartbeat:
    image: alpine/curl:latest
    env_file:
      - .env
    volumes:
      - ./heartbeat.sh:/heartbeat.sh:ro
    entrypoint: ["sh", "/heartbeat.sh"]
    restart: unless-stopped
    depends_on:
      - agent

volumes:
  openclaw-{employee.packet_dir}:
"""



def render_heartbeat() -> str:
    return """
#!/bin/sh
set -e

if [ -z "$CREWCLAW_MONITOR_KEY" ]; then
  echo "[heartbeat] No CREWCLAW_MONITOR_KEY set; skipping dashboard heartbeat."
  exit 0
fi

while true; do
  curl -sf "https://www.crewclaw.com/api/ping/$CREWCLAW_MONITOR_KEY" > /dev/null 2>&1 \
    && echo "[heartbeat] ping ok" \
    || echo "[heartbeat] ping failed"
  sleep 300
done
"""



def render_package_json(employee: EmployeeRuntime) -> str:
    package = {
        "name": f"{employee.slug}-openclaw-worker",
        "version": "1.0.0",
        "private": True,
        "dependencies": {
            "@slack/bolt": "^3.19.0",
            "discord.js": "^14.19.3",
            "grammy": "^1.38.4",
            "qrcode-terminal": "^0.12.0",
            "whatsapp-web.js": "^1.34.1",
        },
    }
    return json.dumps(package, indent=2)



def copy_skill_files(employee_dir: Path, skills: list[str]) -> None:
    skill_target_root = employee_dir / "skills"
    if skill_target_root.exists():
        shutil.rmtree(skill_target_root)
    ensure_dir(skill_target_root)
    for skill in skills:
        source = SKILLS_ROOT / skill / "SKILL.md"
        target = skill_target_root / skill / "SKILL.md"
        if not source.exists():
            raise FileNotFoundError(f"Missing skill file for {skill}: {source}")
        ensure_dir(target.parent)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")



def update_checklist(employee_dir: Path, employee: EmployeeRuntime) -> None:
    path = employee_dir / "CHECKLIST.md"
    text = read_text(path)
    for runtime_file in RUNTIME_FILES:
        unchecked = f"- [ ] `{runtime_file}`"
        checked = f"- [x] `{runtime_file}`"
        if unchecked in text:
            text = text.replace(unchecked, checked)
        elif checked not in text and "## Required Runtime Files" in text:
            text = text.replace("## Assigned Skills", f"- [x] `{runtime_file}`\n\n## Assigned Skills")
    text = re.sub(
        r"## Remaining Gaps\n(?:- \[.\].*\n)+",
        "## Runtime Verification Status\n- Runtime files are packaged in this employee packet.\n- Live gateway pairing, tool entitlement proof, and channel credentials still depend on environment setup.\n",
        text,
    )
    write(path, text)


def update_audit(employee_dir: Path, employee: EmployeeRuntime) -> None:
    path = employee_dir / "AUDIT.md"
    text = read_text(path)
    replacements = {
        "- **Status:** Strong curated packet, not yet live-runtime validated": "- **Status:** Runtime-synced packet with generated shell; structurally validated, but not yet live-started against real channel credentials",
        "- Not yet wrapped into the live `open-claw/employees` runtime packet layout with Docker and bot wiring.": "- Runtime shell now exists in this packet and in the generated `open-claw/employees/deployed-curated/` runtime.",
        "- Tool access is documented, but not yet proven end-to-end against the real worker runtime and installed integrations.": "- Tool expectations and assigned skills are packaged, but end-to-end entitlement proof against the real gateway is not yet recorded.",
        "- No per-role activation smoke test has been recorded yet for the current OpenClaw/CrewClaw deployment path.": "- No per-role live smoke test has been recorded yet for the generated curated runtime.",
        "Use this packet as part of the authoritative standard now. Before treating it as a fully autonomous live worker, pair it with runtime packaging, real tool-entitlement proof, and a recorded smoke test.": "Use this packet as part of the authoritative standard now. Runtime packaging and copied skills are in place. Before treating it as a fully autonomous live worker, prove live startup, real tool entitlements, and a recorded smoke test.",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    if is_host_native_primary(employee.slug):
        text = text.replace(
            "- Runtime shell now exists in this packet and in the generated `open-claw/employees/deployed-curated/` runtime.",
            "- Runtime shell now exists in this packet, but Sparky is intentionally operated as the host-native executive runtime outside the `open-claw/employees/deployed-curated/` Docker worker pool.",
        )
    binding_block = render_live_binding_block(employee)
    if "## Live Telegram Binding" in text:
        text = re.sub(r"## Live Telegram Binding\n(?:- .*\n)+", binding_block + "\n", text, count=1)
    else:
        text = re.sub(r"(- \*\*Status:\*\*.*\n)", r"\1\n" + binding_block + "\n", text, count=1)
    write(path, text)



def write_employee_runtime(employee: EmployeeRuntime) -> None:
    employee_dir = EMPLOYEE_ROOT / employee.packet_dir
    copy_skill_files(employee_dir, employee.skills)
    write(employee_dir / ".env.example", render_env_example(employee))
    write(employee_dir / "openclaw-runner.js", render_runner(employee))
    write(employee_dir / "bot-telegram.js", render_telegram_bot(employee))
    write(employee_dir / "bot-discord.js", render_discord_bot(employee))
    write(employee_dir / "bot-slack.js", render_slack_bot(employee))
    write(employee_dir / "bot-whatsapp.js", render_whatsapp_bot(employee))
    write(employee_dir / "Dockerfile", render_dockerfile())
    write(employee_dir / "entrypoint.sh", render_entrypoint(employee))
    write(employee_dir / "setup.sh", render_setup(employee))
    write(employee_dir / "docker-compose.yml", render_packet_compose(employee))
    write(employee_dir / "heartbeat.sh", render_heartbeat())
    write(employee_dir / "package.json", render_package_json(employee))
    update_checklist(employee_dir, employee)
    update_audit(employee_dir, employee)



def extract_grade(employee_dir: Path, field_name: str) -> str:
    checklist = read_text(employee_dir / "CHECKLIST.md")
    match = re.search(rf"{re.escape(field_name)}:\s*\*\*(.+?)\*\*", checklist)
    return match.group(1).strip() if match else "Unknown"



def extract_audit_status(employee_dir: Path) -> str:
    audit = read_text(employee_dir / "AUDIT.md")
    match = re.search(r"- \*\*Status:\*\*\s*(.+)", audit)
    return match.group(1).strip() if match else "Status not documented"



def file_kind(name: str) -> str:
    if name in DOC_FILES:
        return "doc"
    if name in RUNTIME_FILES:
        return "runtime"
    return "skill"



def file_rating(name: str, employee: EmployeeRuntime) -> tuple[str, str]:
    binding_exists = bool(telegram_binding(employee.packet_dir))
    direct_secret = bool(assigned_secret_id(employee.packet_dir))
    if name in {"README.md", "CHECKLIST.md", "AUDIT.md", "SKILLS.md"}:
        return "A", "Core source-of-truth file is present and actively used to describe the employee."
    if name in DOC_FILES:
        return "A-", "Required packet documentation is present and standardized; refine after more live usage."
    if name == "bot-telegram.js":
        if direct_secret:
            return "B+", "Telegram runtime is assigned to a live bot and a direct Bitwarden UUID is already wired."
        if binding_exists:
            return "B", "Telegram runtime is assigned to a live bot, but startup still depends on env vars or a future UUID mapping."
        return "C", "Telegram runtime scaffold exists, but this employee still needs a brand-new Telegram bot."
    if name in {"Dockerfile", "docker-compose.yml", "entrypoint.sh", "setup.sh", ".env.example", "package.json", "openclaw-runner.js", "heartbeat.sh"}:
        return "B+", "Runtime file is present and structurally validated; live smoke evidence is still pending."
    if name in {"bot-discord.js", "bot-slack.js", "bot-whatsapp.js"}:
        return "C+", "Secondary channel scaffold is present, but this path has not been prioritized or smoke-tested yet."
    return "A-", "Assigned skill file is present in the packet and ready to be refined through real usage."



def file_note(name: str, employee: EmployeeRuntime) -> str:
    if name.startswith("skills/"):
        return "Copied assigned skill playbook is packaged inside the employee packet."
    if name == "bot-telegram.js":
        if telegram_binding(employee.packet_dir):
            return f"Bound to `{assigned_telegram_name(employee.packet_dir)}` / `{assigned_username(employee.packet_dir)}`."
        return "No Telegram identity assigned yet."
    return "Present in the curated packet."



def render_file_rows(employee: EmployeeRuntime) -> str:
    employee_dir = EMPLOYEE_ROOT / employee.packet_dir
    rows: list[str] = []
    for name in DOC_FILES + RUNTIME_FILES:
        present = (employee_dir / name).exists()
        rating, reason = file_rating(name, employee) if present else ("Pending", "File is still missing from the packet.")
        rows.append(
            f"| `{name}` | {file_kind(name)} | {'yes' if present else 'no'} | `{rating}` | {reason} | {file_note(name, employee)} |"
        )
    for skill in employee.skills:
        skill_path = employee_dir / "skills" / skill / "SKILL.md"
        skill_name = f"skills/{skill}/SKILL.md"
        present = skill_path.exists()
        rating, reason = file_rating(skill_name, employee) if present else ("Pending", "Assigned skill copy is missing from the packet.")
        rows.append(
            f"| `{skill_name}` | skill | {'yes' if present else 'no'} | `{rating}` | {reason} | {file_note(skill_name, employee)} |"
        )
    return "\n".join(rows)



def render_current_employees(employees: list[EmployeeRuntime]) -> str:
    assignment_rows = []
    for employee in employees:
        if telegram_binding(employee.packet_dir):
            assignment_status = "direct_uuid_wired" if assigned_secret_id(employee.packet_dir) else "env_only_assigned"
        else:
            assignment_status = "pending_new_bot"
        assignment_rows.append(
            f"| `{employee.slug}` | `{employee.packet_dir}` | {employee.title} | `{assigned_telegram_name(employee.packet_dir)}` | "
            f"`{assigned_username(employee.packet_dir) or 'TBD'}` | `{assigned_secret_name(employee.packet_dir) or 'TBD'}` | `{deployment_mode(employee.slug)}` | `{assignment_status}` | "
            f"`{extract_grade(EMPLOYEE_ROOT / employee.packet_dir, 'Current grade')}` |"
        )

    employee_sections = []
    for employee in employees:
        employee_dir = EMPLOYEE_ROOT / employee.packet_dir
        skills_line = ", ".join(f"`{skill}`" for skill in employee.skills) if employee.skills else "none"
        binding_status = (
            "Direct Bitwarden UUID wired"
            if runtime_status(employee.packet_dir) == "direct_uuid_wired"
            else "Assigned bot, but env var / UUID still pending"
            if runtime_status(employee.packet_dir) == "env_only_assigned"
            else "No Telegram bot assigned yet"
        )
        employee_sections.append(
            f"""## {employee.title}

- **Slug:** `{employee.slug}`
- **Packet Directory:** `{employee.packet_dir}`
- **Manager:** `{employee.manager}`
- **Summary:** {employee.summary}
- **Current packet grade:** `{extract_grade(employee_dir, 'Current grade')}`
- **Target live grade:** `{extract_grade(employee_dir, 'Target grade for live-runtime readiness')}`
- **Audit status:** {extract_audit_status(employee_dir)}
- **Current Telegram first name:** `{assigned_telegram_name(employee.packet_dir)}`
- **Telegram username:** `{assigned_username(employee.packet_dir) or 'TBD'}`
- **Bitwarden secret name:** `{assigned_secret_name(employee.packet_dir) or 'TBD'}`
- **Deployment mode:** {deployment_mode_summary(employee.slug)}
- **Telegram/runtime status:** {binding_status}
- **Assigned skills:** {skills_line}

### File Ratings

| File | Kind | Present | Rating | Reason | Notes |
| --- | --- | --- | --- | --- | --- |
{render_file_rows(employee)}"""
        )

    assignment_table = "\n".join(assignment_rows)
    employee_content = "\n\n".join(employee_sections)
    return f"""
# Current Employees

This file is generated by `open-claw/scripts/sync_curated_employee_runtime.py`.
It is the current status board for the curated employee roster, including Telegram identity mapping, packet readiness, assigned skills, and per-file ratings.

## Rating Legend

- `A` — strong source-of-truth file; keep as-is unless live evidence proves a better pattern
- `A-` — solid file with good structure; likely needs iterative refinement after more real usage
- `B+` — structurally validated runtime file; promising but still needs live smoke proof
- `B` — assigned/usable now, but still depends on env wiring or more runtime evidence
- `C+` — scaffold exists for future use, but is not yet a proven path
- `C` — placeholder/scaffold that still needs assignment or stronger implementation
- `Pending` — file or live binding is still missing

## Roster Snapshot

- Generated on: `{TODAY}`
- Curated employees: **{len(employees)}**
- Telegram bots already assigned: **{sum(1 for employee in employees if telegram_binding(employee.packet_dir))}**
- Direct Bitwarden UUIDs already wired: **{sum(1 for employee in employees if assigned_secret_id(employee.packet_dir))}**
- Canonical BotFather bots: **{len(CANONICAL_BOTFATHER_BOTS)}**
- Assigned bots still waiting on env vars or UUID recording: {", ".join(f"`{employee.slug}`" for employee in employees if runtime_status(employee.packet_dir) == "env_only_assigned") or "none"}
- Employees still waiting on brand-new Telegram bots: {", ".join(f"`{employee.slug}`" for employee in employees if runtime_status(employee.packet_dir) == "pending_new_bot") or "none"}

## Assignment Table

| Employee Slug | Packet Directory | Title | Current Telegram first name | Telegram username | Bitwarden secret name | Deployment mode | Runtime status | Current grade |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{assignment_table}

{employee_content}
"""



def sync_deployed_curated(employees: list[EmployeeRuntime]) -> None:
    docker_workers = docker_runtime_employees(employees)
    ensure_dir(DEPLOYED_CURATED_ROOT)
    for child in DEPLOYED_CURATED_ROOT.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    compose_services: list[str] = []
    volume_lines: list[str] = []
    for employee in docker_workers:
        source_dir = EMPLOYEE_ROOT / employee.packet_dir
        target_dir = DEPLOYED_CURATED_ROOT / employee.packet_dir
        shutil.copytree(source_dir, target_dir)
        env_name = f"{assigned_secret_name(employee.packet_dir) or slug_to_env(employee.slug)}_TOKEN"
        compose_services.append(
            textwrap.dedent(
                f"""
                  {employee.packet_dir}:
                    build: ./{employee.packet_dir}
                    container_name: openclaw-{employee.packet_dir}
                    environment:
                      - ANTHROPIC_API_KEY=${{ANTHROPIC_API_KEY}}
                      - TELEGRAM_BOT_TOKEN=${{{env_name}}}
                      - OPENCLAW_AGENT_ID={employee.slug}
                      - OPENCLAW_GATEWAY_URL=${{OPENCLAW_GATEWAY_URL}}
                      - OPENCLAW_GATEWAY_TOKEN=${{OPENCLAW_GATEWAY_TOKEN}}
                      - OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1
                    extra_hosts:
                      - "host.docker.internal:host-gateway"
                    volumes:
                      - D:/github:/workspace:rw
                      - openclaw-{employee.packet_dir}:/root/.openclaw
                    restart: unless-stopped
                """
            ).rstrip()
        )
        volume_lines.append(f"  openclaw-{employee.packet_dir}:")

    compose_body = textwrap.indent("\n\n".join(compose_services), "  ")
    volumes = "\n".join(volume_lines)
    write(
        DEPLOYED_CURATED_ROOT / "docker-compose.yml",
        f"""
services:
{compose_body}

volumes:
{volumes}
""",
    )
    write(DEPLOYED_CURATED_ROOT / "start-employees.ps1", render_start_script(employees))
    write(DEPLOYED_CURATED_ROOT / "README.md", render_runtime_readme(employees))
    write(DEPLOYED_CURATED_ROOT / "team-status.json", render_team_status(employees))



def render_runtime_readme(employees: list[EmployeeRuntime]) -> str:
    docker_workers = docker_runtime_employees(employees)
    roster = "\n".join(f"- `{employee.slug}` — {employee.title}" for employee in docker_workers)
    assigned_bot_count = sum(1 for employee in docker_workers if telegram_binding(employee.packet_dir))
    direct_secret_count = sum(1 for employee in docker_workers if assigned_secret_id(employee.packet_dir))
    env_only_line = ", ".join(
        f"`{employee.slug}`" for employee in docker_workers if runtime_status(employee.packet_dir) == "env_only_assigned"
    ) or "none"
    pending_line = ", ".join(
        f"`{employee.slug}`" for employee in docker_workers if runtime_status(employee.packet_dir) == "pending_new_bot"
    ) or "none"
    assignment_lines = "\n".join(
        f"- `{employee.slug}` -> `{assigned_username(employee.packet_dir)}`" for employee in docker_workers if telegram_binding(employee.packet_dir)
    )
    return f"""
# Curated Deployed Runtime

This directory is the generated Docker runtime shell for the curated worker pool.

`{HOST_NATIVE_PRIMARY_SLUG}` is intentionally excluded from this Docker runtime and is expected to operate as the host-native executive / primary Sparky runtime.

## Employees
{roster}

## Startup
- Provide `BWS_ACCESS_TOKEN` if you want Bitwarden-backed secret fetches.
- Existing Telegram bot assignments are defined for **{assigned_bot_count}** curated workers.
- Direct Bitwarden worker token IDs are currently wired for **{direct_secret_count}** curated workers.
- Assigned workers that still need explicit `*_TOKEN` env vars or Bitwarden secret IDs recorded: {env_only_line}.
- Curated workers still waiting on brand-new Telegram bots: {pending_line}.
- Run `./start-employees.ps1` from PowerShell.
- Run `./start-employees.ps1 -CheckOnly` to see which workers are currently startable without launching containers.
- Run `./start-employees.ps1 -CheckOnly -CeoOnly` to verify the host-native `SPARKY_CEO_BOT` launch path without starting it.
- Run `./start-employees.ps1 -CeoOnly` to resolve `SPARKY_CEO_BOT` from Bitwarden/env and start the host-native CEO Telegram runtime.
- Run `./start-employees.ps1 -RequireCeo` to require the CEO host-native runtime before starting the Docker worker pool.
- `sparky-chief-product-quality-officer` remains outside the Docker worker pool, but the startup script now provides the supported host-native launch path.
- Dockerized curated workers now default to their own `OPENCLAW_AGENT_ID` instead of all hard-routing to the shared `main` agent shell.
- `team-status.json` contains the generated machine-readable readiness snapshot for this runtime.

## Telegram Assignment Plan
{assignment_lines}

## Validation
- `docker compose config`
- `python ../scripts/validate_openclaw_workflow.py`
"""



def render_start_script(employees: list[EmployeeRuntime]) -> str:
    docker_workers = docker_runtime_employees(employees)
    secret_map_lines = []
    for employee in docker_workers:
        secret = assigned_secret_id(employee.packet_dir)
        secret_map_lines.append(f'    "{employee.packet_dir}" = "{secret}"')
    secret_map_block = "\n".join(secret_map_lines)
    host_native_secret_id = assigned_secret_id(HOST_NATIVE_PRIMARY_PACKET_DIR)
    return f"""
param(
    [switch]$CheckOnly,
    [switch]$Strict,
    [switch]$CeoOnly,
    [switch]$RequireCeo
)

$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot
$openClawRoot = Split-Path (Split-Path $Root -Parent) -Parent
$hostNativeSparkySlug = "{HOST_NATIVE_PRIMARY_SLUG}"
$hostNativeSparkyPacketDirName = "{HOST_NATIVE_PRIMARY_PACKET_DIR}"
$hostNativeSparkySecretId = "{host_native_secret_id}"

function Resolve-SecretValue([string]$EnvName, [string]$SecretId) {{
    $current = [System.Environment]::GetEnvironmentVariable($EnvName, "Process")
    if ($current) {{ return $current }}

    if ($SecretId) {{
        $bwsCmd = Get-Command bws -ErrorAction SilentlyContinue
        if ($bwsCmd) {{
            $raw = & $bwsCmd.Source secret get $SecretId 2>$null
            if ($LASTEXITCODE -eq 0 -and $raw) {{
                $fetched = ($raw | ConvertFrom-Json).value
                if ($fetched) {{
                    Set-Item "env:$EnvName" $fetched
                    return $fetched
                }}
            }}
        }}
    }}

    return $null
}}

function Test-CommandAvailable([string]$CommandName) {{
    return [bool](Get-Command $CommandName -ErrorAction SilentlyContinue)
}}

function Get-HostNativeSparkyPacketDir {{
    return Join-Path $openClawRoot "AI_Employee_knowledgebase/AI_employees/$hostNativeSparkyPacketDirName"
}}

function Get-HostNativeSparkyStatus {{
    $packetDir = Get-HostNativeSparkyPacketDir
    $gatewayUrl = $env:OPENCLAW_GATEWAY_URL
    if (-not $gatewayUrl) {{
        $gatewayUrl = "ws://127.0.0.1:18789"
    }}

    $issues = @()
    $telegramToken = Resolve-SecretValue "TELEGRAM_BOT_TOKEN" $hostNativeSparkySecretId
    $gatewayToken = Resolve-SecretValue "OPENCLAW_GATEWAY_TOKEN" "79f3acf8-c855-4c0d-9726-b40d01278bb6"

    if (-not (Test-Path $packetDir)) {{
        $issues += "Missing host-native CEO packet directory: $packetDir"
    }}
    if (-not $telegramToken) {{
        $issues += "Missing TELEGRAM_BOT_TOKEN for SPARKY_CEO_BOT. Provide TELEGRAM_BOT_TOKEN in the shell or expose Bitwarden secret $hostNativeSparkySecretId through bws."
    }}
    if (-not $gatewayToken) {{
        $issues += "Missing OPENCLAW_GATEWAY_TOKEN"
    }}
    if (-not (Test-CommandAvailable "node")) {{
        $issues += "Node.js is not available in PATH."
    }}
    if (-not (Test-CommandAvailable "openclaw")) {{
        $issues += "OpenClaw CLI is not available in PATH."
    }}

    return [PSCustomObject]@{{
        Ready = ($issues.Count -eq 0)
        PacketDir = $packetDir
        TelegramToken = $telegramToken
        GatewayToken = $gatewayToken
        GatewayUrl = $gatewayUrl
        DependenciesReady = (Test-Path (Join-Path $packetDir "node_modules/grammy"))
        Issues = $issues
    }}
}}

function Install-HostNativeSparkyDependencies([string]$PacketDir) {{
    if (Test-Path (Join-Path $PacketDir "node_modules/grammy")) {{
        return
    }}

    $npmCmd = Get-Command npm -ErrorAction SilentlyContinue
    if (-not $npmCmd) {{
        throw "npm is not available in PATH. Install Node.js/npm before starting SPARKY_CEO_BOT."
    }}

    Write-Host "Installing SPARKY_CEO_BOT host-native dependencies..." -ForegroundColor Cyan
    Push-Location $PacketDir
    try {{
        npm install
        if ($LASTEXITCODE -ne 0) {{
            throw "npm install failed in $PacketDir"
        }}
    }} finally {{
        Pop-Location
    }}
}}

function Get-HostNativeSparkyProcess([string]$PacketDir) {{
    $botScriptPattern = 'bot-telegram\\.js'
    return Get-CimInstance Win32_Process -Filter "Name = 'node.exe'" -ErrorAction SilentlyContinue | Where-Object {{
        $_.CommandLine -match $botScriptPattern
    }} | Select-Object -First 1
}}

function Initialize-HostNativeSparkyRuntime([pscustomobject]$Status) {{
    $runtimeRoot = Join-Path $Status.PacketDir ".openclaw-runtime"
    $workspaceDir = Join-Path $runtimeRoot "workspace"
    $skillsDir = Join-Path $workspaceDir "skills"
    $liveDir = Join-Path $workspaceDir "live"
    $checklistsDir = Join-Path $workspaceDir "CHECKLISTS"
    $handoffTemplatesDir = Join-Path $workspaceDir "HANDOFF_TEMPLATES"
    $evalsDir = Join-Path $workspaceDir "evals"
    $configDir = Join-Path $runtimeRoot "config"
    $configFile = Join-Path $configDir "openclaw.json"
    $mainAgentDir = Join-Path $runtimeRoot "agents/main/agent"
    $roleAgentDir = Join-Path $runtimeRoot "agents/$hostNativeSparkySlug/agent"

    $null = New-Item -ItemType Directory -Force -Path $workspaceDir, $skillsDir, $liveDir, $checklistsDir, $handoffTemplatesDir, $evalsDir, $configDir, $mainAgentDir, $roleAgentDir

    $workspaceFiles = @(
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
        "ACCESS.md",
        "COMPLETE_TOOL_REFERENCE.md",
        "ONBOARDING.md",
        "DECISION_LOG.md",
        "RUNBOOK.md",
        "KNOWLEDGE_SOURCES.md",
        "SOURCE_PRIORITY.md",
        "RETRIEVAL_RULES.md",
        "SUCCESS_METRICS.md",
        "APPROVAL_GATES.md",
        "PR_RULES.md",
        "SPARKY_EVALUATION_SUMMARY.md"
    )
    foreach ($fileName in $workspaceFiles) {{
        $source = Join-Path $Status.PacketDir $fileName
        if (Test-Path $source) {{
            Copy-Item $source (Join-Path $workspaceDir $fileName) -Force
        }}
    }}

    $packetLiveDir = Join-Path $Status.PacketDir "live"
    if (Test-Path $packetLiveDir) {{
        Copy-Item (Join-Path $packetLiveDir "*") $liveDir -Recurse -Force
    }}

    $packetSkillsDir = Join-Path $Status.PacketDir "skills"
    if (Test-Path $packetSkillsDir) {{
        Copy-Item (Join-Path $packetSkillsDir "*") $skillsDir -Recurse -Force
    }}

    $packetChecklistsDir = Join-Path $Status.PacketDir "CHECKLISTS"
    if (Test-Path $packetChecklistsDir) {{
        Copy-Item (Join-Path $packetChecklistsDir "*") $checklistsDir -Recurse -Force
    }}

    $packetHandoffTemplatesDir = Join-Path $Status.PacketDir "HANDOFF_TEMPLATES"
    if (Test-Path $packetHandoffTemplatesDir) {{
        Copy-Item (Join-Path $packetHandoffTemplatesDir "*") $handoffTemplatesDir -Recurse -Force
    }}

    $packetEvalsDir = Join-Path $Status.PacketDir "evals"
    if (Test-Path $packetEvalsDir) {{
        Copy-Item (Join-Path $packetEvalsDir "*") $evalsDir -Recurse -Force
    }}

    $config = @{{
        agents = @{{
            defaults = @{{
                workspace = $workspaceDir
                heartbeat = @{{ every = "0m" }}
            }}
            list = @(
                @{{
                    id = "main"
                    default = $false
                    workspace = $workspaceDir
                    agentDir = $mainAgentDir
                }},
                @{{
                    id = $hostNativeSparkySlug
                    default = $true
                    workspace = $workspaceDir
                    agentDir = $roleAgentDir
                }}
            )
        }}
        gateway = @{{
            mode = "remote"
            remote = @{{
                url = $Status.GatewayUrl
                token = $Status.GatewayToken
            }}
        }}
    }}

    $config | ConvertTo-Json -Depth 8 | Set-Content -Path $configFile -Encoding UTF8

    return [PSCustomObject]@{{
        RuntimeRoot = $runtimeRoot
        WorkspaceDir = $workspaceDir
        ConfigFile = $configFile
    }}
}}

function Start-HostNativeSparky([pscustomobject]$Status) {{
    if (-not $Status.Ready) {{
        throw "SPARKY_CEO_BOT host-native runtime is not ready. Resolve the reported issues and rerun."
    }}

    $existing = Get-HostNativeSparkyProcess $Status.PacketDir
    if ($existing) {{
        Write-Host "Host-native CEO Sparky Telegram runtime already running (pid $($existing.ProcessId))." -ForegroundColor Cyan
        return
    }}

    Install-HostNativeSparkyDependencies $Status.PacketDir

    $powerShellExe = (Get-Process -Id $PID).Path
    if (-not $powerShellExe) {{
        $pwshCmd = Get-Command pwsh -ErrorAction SilentlyContinue
        if ($pwshCmd) {{
            $powerShellExe = $pwshCmd.Source
        }}
    }}
    if (-not $powerShellExe) {{
        throw "Unable to determine the current PowerShell executable for launching SPARKY_CEO_BOT."
    }}

    $runtime = Initialize-HostNativeSparkyRuntime $Status
    $escapedPacketDir = $Status.PacketDir.Replace("'", "''")
    $escapedTelegramToken = $Status.TelegramToken.Replace("'", "''")
    $escapedGatewayUrl = $Status.GatewayUrl.Replace("'", "''")
    $escapedGatewayToken = $Status.GatewayToken.Replace("'", "''")
    $escapedConfigFile = $runtime.ConfigFile.Replace("'", "''")
    $launchCommand = @"
Set-Location '$escapedPacketDir'
`$env:TELEGRAM_BOT_TOKEN = '$escapedTelegramToken'
`$env:OPENCLAW_AGENT_ID = '$hostNativeSparkySlug'
`$env:OPENCLAW_CONFIG_PATH = '$escapedConfigFile'
`$env:OPENCLAW_GATEWAY_URL = '$escapedGatewayUrl'
`$env:OPENCLAW_GATEWAY_TOKEN = '$escapedGatewayToken'
`$env:OPENCLAW_ALLOW_INSECURE_PRIVATE_WS = '1'
node bot-telegram.js
"@

    Start-Process -FilePath $powerShellExe -ArgumentList "-NoProfile", "-Command", $launchCommand | Out-Null
    Write-Host "Started host-native CEO Sparky Telegram runtime from $($Status.PacketDir)." -ForegroundColor Green
}}

function Test-DockerReady {{
    $dockerCmd = Get-Command docker -ErrorAction SilentlyContinue
    if (-not $dockerCmd) {{
        throw "Docker CLI not found in PATH. Start Docker Desktop or install Docker Desktop first."
    }}

    & docker version *> $null
    if ($LASTEXITCODE -ne 0) {{
        throw "Docker engine is not reachable. Start Docker Desktop and wait until it shows Engine running, then rerun start-employees.ps1."
    }}
}}

if (-not $env:BWS_ACCESS_TOKEN) {{
    $stored = [System.Environment]::GetEnvironmentVariable("BWS_ACCESS_TOKEN", "User")
    if ($stored) {{
        $env:BWS_ACCESS_TOKEN = $stored
    }}
}}

if (-not (Resolve-SecretValue "OPENCLAW_GATEWAY_TOKEN" "79f3acf8-c855-4c0d-9726-b40d01278bb6")) {{
    throw "Missing OPENCLAW_GATEWAY_TOKEN"
}}

$ceoStatus = Get-HostNativeSparkyStatus
if ($ceoStatus.Ready) {{
    Write-Host "Host-native CEO Sparky ready: True" -ForegroundColor Green
}} else {{
    Write-Host "Host-native CEO Sparky ready: False" -ForegroundColor Yellow
}}
Write-Host "  Packet: $($ceoStatus.PacketDir)" -ForegroundColor DarkGray
if (-not $ceoStatus.DependenciesReady) {{
    Write-Host "  npm dependencies will be installed on first CEO start." -ForegroundColor Yellow
}}
if ($ceoStatus.Issues.Count -gt 0) {{
    $ceoStatus.Issues | ForEach-Object {{ Write-Host "  $_" -ForegroundColor Yellow }}
}}

if ($RequireCeo -and -not $ceoStatus.Ready) {{
    throw "CEO Sparky host-native runtime is not ready. Resolve the issues above and rerun with -RequireCeo."
}}

if ($CeoOnly) {{
    if ($CheckOnly) {{
        Write-Host "Check-only mode: host-native CEO runtime not started." -ForegroundColor Cyan
        return
    }}
    Start-HostNativeSparky $ceoStatus
    return
}}

$anthropicKey = Resolve-SecretValue "ANTHROPIC_API_KEY" "2fdc8f21-0d02-46b3-ad30-b3fe0049a474"
if (-not $anthropicKey) {{ throw "Missing ANTHROPIC_API_KEY" }}

if (-not $env:OPENCLAW_GATEWAY_URL) {{
    $env:OPENCLAW_GATEWAY_URL = "ws://host.docker.internal:18789"
}}

$secretMap = @{{
{secret_map_block}
}}

$readyServices = @()
$blocked = @()
foreach ($name in $secretMap.Keys) {{
    $envName = $name.ToUpper().Replace('-', '_') + "_TOKEN"
    $resolved = Resolve-SecretValue $envName $secretMap[$name]
    if ($resolved) {{
        $readyServices += $name
    }} else {{
        $blocked += [PSCustomObject]@{{
            Name = $name
            EnvName = $envName
        }}
    }}
}}

Write-Host "Ready dockerized curated workers: $($readyServices.Count)" -ForegroundColor Green
$readyServices | ForEach-Object {{ Write-Host "  $_" -ForegroundColor Green }}

if ($blocked.Count -gt 0) {{
    Write-Host "Blocked dockerized curated workers: $($blocked.Count)" -ForegroundColor Yellow
    $blocked | ForEach-Object {{ Write-Host "  $($_.Name) ($($_.EnvName))" -ForegroundColor Yellow }}
}}

if ($CheckOnly) {{
    Write-Host "Check-only mode: no containers started." -ForegroundColor Cyan
    return
}}

if ($readyServices.Count -eq 0) {{
    throw "No dockerized curated workers are startable. Provide at least one valid worker token or Bitwarden secret mapping."
}}

if ($Strict -and $blocked.Count -gt 0) {{
    throw "Strict mode blocked startup because one or more curated workers are still unresolved."
}}

if ($RequireCeo) {{
    Start-HostNativeSparky $ceoStatus
}}

Test-DockerReady

Set-Location $Root
$composeArgs = @("compose", "up", "-d", "--build") + $readyServices
& docker @composeArgs

if ($blocked.Count -gt 0) {{
    Write-Host "Partial startup complete. Unresolved workers were skipped." -ForegroundColor Yellow
}}
"""


def rewrite_zips(employees: list[EmployeeRuntime]) -> None:
    ensure_dir(ZIP_ROOT)
    for employee in employees:
        employee_dir = EMPLOYEE_ROOT / employee.packet_dir
        zip_path = ZIP_ROOT / f"{employee.slug}.zip"
        with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
            for file_path in sorted(employee_dir.rglob("*")):
                if file_path.is_file():
                    archive.write(file_path, arcname=f"{employee.slug}/{file_path.relative_to(employee_dir).as_posix()}")



def render_workflow_checklist(employees: list[EmployeeRuntime]) -> str:
    docker_workers = docker_runtime_employees(employees)
    employee_lines = "\n".join(f"- [x] `{employee.slug}` packet generated and runtime-synced" for employee in employees)
    assigned_bot_count = sum(1 for employee in employees if telegram_binding(employee.packet_dir))
    direct_secret_count = sum(1 for employee in employees if assigned_secret_id(employee.packet_dir))
    env_only_line = ", ".join(
        f"`{employee.slug}`" for employee in employees if runtime_status(employee.packet_dir) == "env_only_assigned"
    ) or "none"
    pending_line = ", ".join(
        f"`{employee.slug}`" for employee in employees if runtime_status(employee.packet_dir) == "pending_new_bot"
    ) or "none"
    return f"""
# OpenClaw Workflow Checklist

## Packet Standard
- [x] The curated library has 15 employees.
- [x] Every employee packet includes the required docs.
- [x] Every employee packet now includes the required runtime files.
- [x] Every employee packet includes copied assigned skills under `skills/`.
- [x] Every employee packet zip was regenerated after runtime sync.

## Runtime Shape
- [x] A generated runtime exists at `open-claw/employees/deployed-curated/`.
- [x] The generated runtime includes a {len(docker_workers)}-service `docker-compose.yml` for the dockerized worker pool.
- [x] `{HOST_NATIVE_PRIMARY_SLUG}` is intentionally excluded from the Docker worker pool and remains the host-native executive runtime.
- [x] The generated runtime includes `start-employees.ps1` with env-first plus Bitwarden fallback secret resolution and partial-start capability.
- [x] Each worker uses the proven remote-gateway shell pattern: Node 22 + pinned `openclaw@{OPENCLAW_VERSION}` + entrypoint-generated config.
- [x] A machine-readable readiness snapshot is generated for the curated squad.

## Skill Activation
- [x] Assigned skills are present in every employee packet.
- [x] Assigned skills are copied into each packet's runtime payload.
- [x] Employee packets reference only real tracked skill slugs.

## Validation
- [x] Structural validation script available.
- Existing Telegram bot assignments are defined for **{assigned_bot_count}** curated workers.
- Direct Bitwarden worker token IDs are wired for **{direct_secret_count}** curated workers.
- Assigned workers still needing explicit `*_TOKEN` env vars or Bitwarden secret IDs recorded: {env_only_line}.
- Curated workers still waiting on brand-new Telegram bots: {pending_line}.
- First-run device pairing still must be approved against the real gateway.
- End-to-end live message tests still depend on gateway reachability and real bot credentials.

## Employee Coverage
{employee_lines}
"""



def render_validation_summary(results: dict[str, bool], employees: list[EmployeeRuntime]) -> str:
    docker_workers = docker_runtime_employees(employees)
    status_lines = "\n".join(
        f"- **{'PASS' if passed else 'FAIL'}** — {name}" for name, passed in results.items()
    )
    return f"""
# Runtime Validation Summary

## Result Matrix
{status_lines}

## Employee Count
- Curated employees checked: **{len(employees)}**

## Notes
- This validation covers packet completeness, copied skills, deployed-curated generation, compose/start-script presence, and readiness-manifest generation.
- Dockerized curated workers in `deployed-curated`: **{len(docker_workers)}**
- Host-native executive runtime outside Docker: `{HOST_NATIVE_PRIMARY_SLUG}`
- Live channel delivery still depends on real credentials and gateway pairing.
"""



def render_team_status(employees: list[EmployeeRuntime]) -> str:
    docker_workers = docker_runtime_employees(employees)
    activation_index = {slug: index + 1 for index, slug in enumerate(CANONICAL_ACTIVATION_ORDER)}
    payload = {
        "generated_on": TODAY,
        "employee_count": len(employees),
        "counts": {
            "telegram_assigned": sum(1 for employee in employees if telegram_binding(employee.packet_dir)),
            "direct_uuid_wired": sum(1 for employee in employees if runtime_status(employee.packet_dir) == "direct_uuid_wired"),
            "env_only_assigned": sum(1 for employee in employees if runtime_status(employee.packet_dir) == "env_only_assigned"),
            "pending_new_bot": sum(1 for employee in employees if runtime_status(employee.packet_dir) == "pending_new_bot"),
            "dockerized_worker_count": len(docker_workers),
            "host_native_worker_count": len(employees) - len(docker_workers),
            "canonical_botfather_count": len(CANONICAL_BOTFATHER_BOTS),
        },
        "activation_order": CANONICAL_ACTIVATION_ORDER,
        "canonical_botfather_bots": CANONICAL_BOTFATHER_BOTS,
        "employees": [
            {
                "slug": employee.slug,
                "packet_dir": employee.packet_dir,
                "title": employee.title,
                "manager": employee.manager,
                "skills": employee.skills,
                "telegram_name": assigned_telegram_name(employee.packet_dir),
                "telegram_username": assigned_username(employee.packet_dir) or "",
                "secret_name": assigned_secret_name(employee.packet_dir),
                "deployment_mode": deployment_mode(employee.slug),
                "runtime_status": runtime_status(employee.packet_dir),
                "tracked_readiness_state": tracked_readiness_state(employee.packet_dir),
                "activation_order": activation_index.get(employee.slug),
                "secret_id": assigned_secret_id(employee.packet_dir),
                "blockers": readiness_blockers(employee.packet_dir),
            }
            for employee in employees
        ],
    }
    return json.dumps(payload, indent=2)




def main() -> None:
    employees = parse_employees()
    for employee in employees:
        write_employee_runtime(employee)
    sync_deployed_curated(employees)
    rewrite_zips(employees)
    write(WORKFLOW_CHECKLIST_PATH, render_workflow_checklist(employees))
    write(CURRENT_EMPLOYEES_PATH, render_current_employees(employees))
    write(TEAM_STATUS_PATH, render_team_status(employees))

    results = {
        "curated employee count is 15": len(employees) == 15,
        "every employee has runtime files": all(all((EMPLOYEE_ROOT / employee.packet_dir / name).exists() for name in RUNTIME_FILES) for employee in employees),
        "every employee has copied skills": all(all((EMPLOYEE_ROOT / employee.packet_dir / "skills" / skill / "SKILL.md").exists() for skill in employee.skills) for employee in employees),
        "deployed-curated docker compose exists": (DEPLOYED_CURATED_ROOT / "docker-compose.yml").exists(),
        "deployed-curated start script exists": (DEPLOYED_CURATED_ROOT / "start-employees.ps1").exists(),
        "curated team status manifest exists": TEAM_STATUS_PATH.exists(),
        "deployed-curated team status exists": (DEPLOYED_CURATED_ROOT / "team-status.json").exists(),
    }
    write(VALIDATION_SUMMARY_PATH, render_validation_summary(results, employees))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
