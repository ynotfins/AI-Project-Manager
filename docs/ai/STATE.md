# Execution State

Bootstrapped; nothing executed yet.

---

## State Log

<!-- AGENT appends entries below this line after each execution block. -->

## 2026-02-26 — Global MCP Setup (Laptop → ChaosCentral parity)

### Summary
Installed Node.js 24.14.0, uv 0.10.6, shell-mcp-server 0.1.0. Wrote 16-server global `mcp.json` at `C:\Users\ynotf\.cursor\mcp.json`. Created `~/.serena/serena_config.yml`. Created `docs/tooling/MCP_CANONICAL_CONFIG.md`.

### Evidence

| Check | Status | Detail |
|-------|--------|--------|
| Node.js install | **PASS** | v24.14.0 via `winget install OpenJS.NodeJS.LTS` |
| uv/uvx install | **PASS** | v0.10.6 via `winget install astral-sh.uv` |
| shell-mcp-server install | **PASS** | v0.1.0 via `uv tool install shell-mcp-server`; exe at `C:\Users\ynotf\.local\bin\shell-mcp-server.exe` |
| shell-mcp-server sync main() | **PASS** | No patch needed — `__init__.py` already wraps `asyncio.run()` |
| Conflict check (both repos) | **PASS** | No per-project `.cursor\mcp.json` or `.vscode\mcp.json` found |
| mcp.json written | **PASS** | 16 servers, JSON valid, backed up first |
| `~/.serena/serena_config.yml` | **PASS** | Created with `D:\github\open--claw` + `D:\github\AI-Project-Manager` |
| `MCP_CANONICAL_CONFIG.md` | **PASS** | Kept ChaosCentral version (theirs, more complete) |
| 4 secret-dependent servers | **BLOCKED** | `github`, `firecrawl-mcp`, `Magic MCP`, `googlesheets-tvi8pq-94` — user must fill from Bitwarden |
| Cursor restart + verification | **PENDING** | User action required |

### What's next
1. Fill 4 secrets from Bitwarden into `C:\Users\ynotf\.cursor\mcp.json`
2. Fully restart Cursor
3. Verify all 16 servers in Settings → Tools & MCP
4. Update `open--claw/docs/tooling/MCP_HEALTH.md` Section F with per-server PASS/FAIL

---

## 2026-02-26 — Update PLAN bootstrap prompt

### Changes
- Updated `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` PLAN-tab prompt to enforce: tab separation, required reads, MCP-first + fallback, PASS/FAIL evidence expectations, and a deterministic 3-item output contract.

### Evidence
- **Doc edit (Cursor)**: **PASS** — updated prompt block under "PLAN tab — first prompt"
- **Commands run**: **SKIPPED** — PLAN-mode doc edit only

### What's next
- Use the updated PLAN-tab prompt in new sessions; Phase planning should now consistently produce a single AGENT execution prompt with explicit exit criteria and evidence requirements.

---

## 2026-02-27 — Bitwarden Secrets Manager: OpenClaw Project Setup

### Changes
- Created `OpenClaw` project in Bitwarden Secrets Manager

### Evidence
- **bws --version**: **PASS** — v2.0.0
- **bws project list (before)**: **PASS** — `[]` authenticated
- **bws project create "OpenClaw"**: **PASS** — ID `9e81608a-7391-436c-b838-b3fe00315f9e`
- **bws project list (after)**: **PASS** — OpenClaw visible, machine account has access

### What's next
- Add secrets (`GITHUB_PAT`, `FIRECRAWL_API_KEY`, `MAGIC_API_KEY`, `COMPOSIO_URL`) to OpenClaw project
- Wire `mcp.json` to use `bws run` for secret injection instead of hardcoded values

---

## 2026-02-25 — Bitwarden Secrets Manager CLI (bws) Install

### Changes
- Downloaded `bws-x86_64-pc-windows-msvc-2.0.0.zip` from `github.com/bitwarden/sdk-sm`
- Installed `bws.exe` v2.0.0 to `C:\Users\ynotf\.local\bin\bws.exe`

### Evidence
- **BWS_ACCESS_TOKEN**: **PASS** — set in environment
- **Download**: **PASS** — bws-v2.0.0, 5.6 MB
- **Install**: **PASS** — `C:\Users\ynotf\.local\bin\bws.exe`
- **PATH**: **PASS** — `~\.local\bin` already in User PATH
- **bws --version**: **PASS** — `bws 2.0.0`
- **bws project list**: **PASS** — authenticated, returns `[]`

### What's next
- Create Bitwarden projects + secrets to replace hardcoded keys in `mcp.json`
- Integrate `bws run` into MCP server launch scripts for secret injection

---

## 2026-02-25 — filesystem_scoped + shell-mcp Tool Evidence Log

### What was tested
- filesystem_scoped: 14 tools confirmed, file reads on two repos
- shell-mcp: execute_command confirmed across pwsh + cmd shells

### Evidence
- **filesystem_scoped descriptor**: **PASS** — 14 tools listed
- **read_file D:\github\open--claw\README.md**: **PASS**
- **read_file D:\github\AI-Project-Manager\AGENTS.md**: **PASS**
- **shell-mcp descriptor**: **PASS** — 1 tool (execute_command)
- **whoami (pwsh)**: **PASS** — `chaoscentral\ynotf`
- **dir /b AI-Project-Manager (cmd)**: **PASS** — 5 entries listed
- **PSVersion (pwsh)**: **PASS** — 7.5.4

### What's next
- Resolve open--claw → open-claw GitHub rename before running cleanup plan
- Add wsl-filesystem MCP server for WSL path access

---

## 2026-02-24 — shell-mcp-server Installation

### Changes
- `uv tool install shell-mcp-server` — v0.1.0 already present
- `~/.cursor/mcp.json`: added `shell-mcp` entry with 4 shells (pwsh, powershell, cmd, bash) and 3 allowed dirs

### Evidence
- **uv 0.9.18**: **PASS**
- **shell-mcp-server v0.1.0**: **PASS** — `C:\Users\ynotf\.local\bin\shell-mcp-server.exe`
- **shell-mcp-server --help**: **PASS**
- **mcp.json JSON valid**: **PASS**
- **Cursor restart + MCP connection**: **PENDING**

### What's next
- Restart Cursor to activate `shell-mcp`
- Verify `execute_command` tool is listed and callable

---

## 2026-02-24 — filesystem_scoped MCP Installation

### Changes
- `~/.cursor/mcp.json`: replaced broken remote `Filesystem` HTTP entry with:
  - `filesystem_scoped` (enabled) — roots: `D:\github`, `D:\github_2`, `C:\Users\ynotf\.openclaw`
  - `filesystem_fulldisk` (disabled) — roots: `C:\`, `D:\`
- `@modelcontextprotocol/server-filesystem` pre-cached via npx

### Evidence
- **node/npm/pnpm**: **PASS** — v22.18.0 / 11.7.0 / 10.24.0
- **WSL distro**: **PASS** — Ubuntu
- **D:\github + D:\github_2 + .openclaw paths**: **PASS**
- **WSL UNC \\wsl.localhost\Ubuntu\...**: **BLOCKED** — access denied from PowerShell
- **mcp.json written**: **PASS** — verified via ConvertFrom-Json
- **Package pre-cached**: **PASS**
- **filesystem_scoped MCP tool calls**: **PENDING** — Cursor restart required
- **Windows file reads (Cursor native)**: **PASS** — README.md + AGENTS.md confirmed readable

### What's next
- Restart Cursor → confirm `filesystem_scoped` connects
- Run post-restart MCP tool call verification
- Consider `mcp-server-wsl-filesystem` for WSL path access

---

## 2026-02-24 — Publish AI-Project-Manager to GitHub

### Changes
- `git init -b main` — initialized repo at `D:\github\AI-Project-Manager`
- `.gitignore` — appended `**/.env` and `*.p12` (were missing from required entries)
- Secret scan — PASS (no tokens/keys found)
- Created GitHub repo `ynotfins/AI-Project-Manager` (private) via `gh repo create`
- Remote `origin` set and initial push completed
- Clone URL: `https://github.com/ynotfins/AI-Project-Manager.git`

### Evidence
- **Test-Path D:\github\AI-Project-Manager**: **PASS**
- **git is-inside-work-tree (before)**: not a git repo — clean slate
- **.gitignore exists**: **PASS** — updated with `**/.env`, `*.p12`
- **Secret scan (Select-String)**: **PASS** — no secrets found
- **git init -b main**: **PASS**
- **git add -A (16 files)**: **PASS**
- **No .env staged**: **PASS**
- **gh CLI found**: **PASS** — v2.83.2 at `C:\Program Files\GitHub CLI\gh.exe`
- **gh auth status**: **PASS** — `ynotfins`, token has `repo` scope
- **gh repo create ynotfins/AI-Project-Manager --private**: **PASS**
- **git remote -v**: **PASS** — `origin https://github.com/ynotfins/AI-Project-Manager.git`
- **git ls-remote --heads origin**: **PASS** — `refs/heads/main` at `c2bce21`

### What's next
- Clone on laptop: `git clone https://github.com/ynotfins/AI-Project-Manager.git D:\github\AI-Project-Manager`
- Set up MCP filesystem servers (filesystem-windows + filesystem-wsl) per plan

---

## 2026-02-23 — Filesystem MCP Proof + Cross-Platform Path Test

### What was tested
- Filesystem MCP server identification and connection status
- WSL distro discovery and cross-platform path existence
- Read-only proof calls on Windows and WSL paths

### Evidence
- **Filesystem MCP server**: **BLOCKED** — registered as remote HTTP (`https://file-mcp-smith--bhushangitfull.run.tools`), no auth token in `headers`, returns 401, not available in session
- **WSL distro**: **PASS** — `Ubuntu`
- **Test-Path open--claw\README.md**: **PASS**
- **Test-Path AI-Project-Manager\AGENTS.md**: **PASS**
- **Test-Path WSL UNC \\wsl$\Ubuntu\...**: **FAIL** — PowerShell access denied
- **Read open--claw\README.md** (Cursor native): **PASS** — `# Open Claw — A modular AI assistant platform...`
- **Read AI-Project-Manager\AGENTS.md** (Cursor native): **PASS** — `# AGENTS.md — This repo uses a five-tab Cursor workflow...`
- **wsl cat /mnt/d/github/open--claw/README.md**: **PASS** — same content
- **Filesystem MCP tool calls**: **SKIPPED** — server not connected

### Remaining gaps
1. **Filesystem MCP** needs auth token OR replacement with local `@modelcontextprotocol/server-filesystem`
2. **WSL UNC** `\\wsl$\Ubuntu\...` access denied from PowerShell — use `wsl` shell as workaround
3. See `docs/tooling/MCP_HEALTH.md` for full recovery steps

---

## 2026-02-23 — Smithery CLI + marco280690/mcp Connection Attempt

### Changes
- Verified Smithery CLI 4.1.4 (already globally installed)
- Confirmed auth active via `smithery auth whoami`
- Attempted to connect `marco280690/mcp` — all three variants returned 404

### Evidence
- **node v22.18.0**: **PASS**
- **npm 11.7.0**: **PASS**
- **pnpm 10.24.0**: **PASS**
- **smithery --version**: **PASS** — 4.1.4
- **smithery auth whoami**: **PASS** — authenticated
- **smithery mcp add marco280690/mcp**: **FAIL** — 404
- **smithery mcp add @marco280690/mcp**: **FAIL** — 404
- **smithery mcp add https://server.smithery.ai/marco280690/mcp**: **FAIL** — 404
- **smithery search marco280690**: **FAIL** — no results found
- **Tool verification + sanity call**: **SKIPPED** — blocked by D

### What's next
- **BLOCKED**: Provide correct Smithery server ID for marco280690/mcp
- Check `https://smithery.ai/search?q=marco280690` in browser to find real qualified name
- Re-run step D once correct ID is known

---

## 2026-02-23 — Phase 0: Serena Global Config Repair

### Changes
- Removed `D:\github\open-claw` (single dash) from `~/.serena/serena_config.yml` projects list
- Added `D:\github\open--claw` and `D:\github\AI-Project-Manager` to projects list
- `D:\github\alerts-sheets` preserved
- Backup created: `serena_config.yml.backup.20260223-225332`
- Created `docs/tooling/MCP_HEALTH.md`

### Evidence
- **Test-Path cfgPath**: **PASS** — config file exists at `C:\Users\ynotf\.serena\serena_config.yml`
- **Get-Content (120 lines)**: **PASS** — projects section found and readable
- **Test-Path open--claw**: **PASS** — `D:\github\open--claw` directory exists
- **Test-Path AI-Project-Manager**: **PASS** — `D:\github\AI-Project-Manager` directory exists
- **Backup**: **PASS** — `serena_config.yml.backup.20260223-225332` created
- **Config edit**: **PASS** — verified via Select-String; correct 3-entry projects list, no stale entry
- **activate_project(open--claw)**: **WARN** — path recognized by Serena; no source language files yet (new repo, expected)
- **activate_project(AI-Project-Manager)**: **WARN** — same as above
- **get_current_config**: **PARTIAL** — Serena process running but loaded old config; shows only `alerts-sheets`. Restart required.

### Post-Restart Evidence
- **open-claw removed**: **PASS**
- **open--claw present**: **PASS**
- **AI-Project-Manager present**: **PASS**
- **alerts-sheets preserved**: **PASS**
- **Serena process**: **PASS** — single healthy process tree after full Cursor restart
- **MCP_HEALTH.md**: updated with PASS

### What's next
- [ ] Define Phase 1 in `docs/ai/PLAN.md`
- [ ] Note: Serena uses `--project-from-cwd`; to use it for a specific project, open that project folder in Cursor

<!--
Format:

## <Date> — <Phase/Task>

### Changes
- ...

### Evidence
- **<tool/command>**: **PASS/FAIL** — <detail>

### What's next
- ...
-->
