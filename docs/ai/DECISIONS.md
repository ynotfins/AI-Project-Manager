
---

## Decision: CrewClaw employees deployed with Bitwarden secret injection -- no .env files (2026-03-18)

**Context:** 10 pre-configured CrewClaw employees need deployment. Employees are treated as potentially hostile until proven in a controlled environment. Network calls to crewclaw.com (heartbeat) disabled.

**Security model:**
- NO .env files -- secrets never touch the filesystem as plaintext
- `bws secret get` injects tokens at startup via process environment (shell scope)
- Each container gets ONLY its own Telegram token + shared ANTHROPIC_API_KEY
- BWS_ACCESS_TOKEN never enters any container
- Volume mount D:\github:/workspace:rw for project file access
- Memory limited to 512M per container (5 containers = 2.5GB max total)
- CrewClaw heartbeat/monitoring disabled (phones home to crewclaw.com)

**Deployed (5/10):**
- api-integration-specialist -- Claude Sonnet 4.5, research/summarization/analysis/web-search
- code-reviewer -- Claude Sonnet 4.5, research/summarization/analysis/web-search
- financial-analyst -- Claude Sonnet 4.5, research/summarization/analysis/web-search
- frontend-developer -- Claude Sonnet 4.5, research/summarization/analysis/web-search
- overnight-coder -- Claude Sonnet 4.5, research/summarization/analysis/web-search

**Pending (5/10) -- need Telegram bots created + Bitwarden entries:**
- personal-crm, script-builder, seo-specialist, software-engineer, ux-designer

**Gitignore decisions:**
- `docs/ai/protected/` added to AI-Project-Manager .gitignore (contains Bitwarden secret IDs)
- `open-claw/employees/deployed/` added to open--claw .gitignore (contains unzipped employee code)
- `.openclaw/` added to AI-Project-Manager .gitignore (local gateway config)

**Runtime note:** Containers have `restart: unless-stopped` but tokens are NOT stored in any Docker config. start-employees.ps1 must be run after each system restart to re-inject secrets. Consider Windows Task Scheduler if unattended restart is needed.
