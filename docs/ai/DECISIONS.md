
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

---

## Decision: Canonical OpenClaw gateway restart + CLI/build alignment (2026-03-21)

**Context:** Mixed OpenClaw **2026.3.8** CLI (`~/openclaw-build` old tag) vs **2026.3.13** gateway runtime caused `Config was last written by a newer OpenClaw` warnings and `openclaw doctor` entrypoint mismatch noise. Ad-hoc `pnpm openclaw gateway restart` from shells without Bitwarden-injected keys risked empty `.gateway-env`.

**Policy:**
1. **Canonical restart path:** `AI-Project-Manager/scripts/restart-openclaw-gateway.ps1` (uses `openclaw_gateway_required_env.py` to derive required env names from `~/.openclaw/openclaw.json`). **Fail-fast** if required keys missing. Writes `~/.openclaw/.gateway-env` with `chmod 600` only; never logs secret values.
2. **Launcher:** `$HOME/.openclaw/start-cursor-with-secrets.ps1` must call the canonical script (supports `AI_PROJECT_MANAGER_ROOT` override). Avoid recommending raw `pnpm openclaw gateway restart` without injected env.
3. **Version alignment:** `~/openclaw-build` tracks git tag **`v2026.3.13-1`** (or newer stable in same series). **systemd** `ExecStart` uses **`openclaw-build/dist/index.js`** so `openclaw doctor` no longer reports service vs install entrypoint skew.
4. **Doctor WARN acceptable:** nvm-managed Node path remains until distro Node 22+ is installed; do not chase `openclaw-node.service` cleanup without explicit operator approval.

**Local-only artifacts (not in git):** `~/.config/systemd/user/openclaw-gateway.service` (+ `.bak.20260321`), `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`.
