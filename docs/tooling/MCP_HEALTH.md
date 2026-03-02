# MCP Health Log

## Entry: 2026-02-27 — Bitwarden Secrets Manager: OpenClaw Project (Session 2)

**Timestamp:** 2026-02-27 03:19 UTC

| Check | Result | Detail |
|---|---|---|
| `bws --version` | **PASS** | v2.0.0 |
| `bws project list` (before) | **PASS** | `[]` — token sees no prior projects |
| `bws project create "OpenClaw"` | **PASS** | ID: `02e3b352-94b4-4b72-a7e2-b3fe0036d7b5` |
| `bws project list` (after) | **PASS** | OpenClaw visible to this machine account |

**Note — duplicate project:** Two `OpenClaw` projects now exist in org `8098135b`:
- `9e81608a` — created in session 1 (ChaosCentral machine account A)
- `02e3b352` — created in session 2 (visible to current token)

**Clean-up action required (Bitwarden UI):**
1. Log into Bitwarden Secrets Manager
2. Go to **Projects**
3. Identify which `OpenClaw` to keep (recommend keeping `02e3b352` — visible to current token)
4. Delete the orphaned one (`9e81608a`) OR grant both machine accounts access to a single project

---

## Entry: 2026-02-27 — Bitwarden Secrets Manager: OpenClaw Project Setup

**Timestamp:** 2026-02-27 02:59 UTC

| Check | Result | Detail |
|---|---|---|
| `bws --version` | **PASS** | v2.0.0 |
| `bws project list` (before) | **PASS** | `[]` — authenticated, no projects |
| `bws project create "OpenClaw"` | **PASS** | Project ID: `9e81608a-7391-436c-b838-b3fe00315f9e` |
| `bws project list` (after) | **PASS** | `OpenClaw` visible — machine account has access |

**Status: PASS** — OpenClaw project created and accessible to ChaosCentral machine account.

**Next steps:**
- Add secrets to `OpenClaw` project via Bitwarden Secrets Manager UI or `bws secret create`
- Secrets to add: `GITHUB_PAT`, `FIRECRAWL_API_KEY`, `MAGIC_API_KEY`, `COMPOSIO_URL`
- Update `mcp.json` servers to use `bws run -- npx ...` for secret injection

---

## Entry: 2026-02-25 — Bitwarden Secrets Manager CLI (bws) Install

**Timestamp:** 2026-02-25 17:45 local (UTC-5 EST)

| Check | Result | Detail |
|---|---|---|
| `BWS_ACCESS_TOKEN` set | **PASS** | Env var present (value not printed) |
| bws.exe pre-existing | SKIP | Not found — downloaded |
| Release found | **PASS** | `bws-v2.0.0` — `bws-x86_64-pc-windows-msvc-2.0.0.zip` |
| Download (5.6 MB) | **PASS** | From `github.com/bitwarden/sdk-sm` |
| Install to `~/.local/bin` | **PASS** | `C:\Users\ynotf\.local\bin\bws.exe` |
| `~/.local/bin` in User PATH | **PASS** | Already present |
| `bws --version` | **PASS** | `bws 2.0.0` |
| `bws project list` | **PASS** | Authenticated — returns `[]` (no projects yet) |

**Status: PASS** — bws v2.0.0 installed and authenticates with existing BWS_ACCESS_TOKEN.

---

## Entry: 2026-02-25 — filesystem_scoped + shell-mcp Tool Evidence Log

**Timestamp:** 2026-02-25 17:30 local (UTC-5 EST)

### A) filesystem_scoped

| Field | Value |
|---|---|
| Server key | `filesystem_scoped` |
| Descriptor folder | `mcps/user-filesystem_scoped/` — **present** |
| Tool count | **14** |
| Tools | `read_file`, `read_text_file`, `read_media_file`, `read_multiple_files`, `write_file`, `edit_file`, `create_directory`, `list_directory`, `list_directory_with_sizes`, `directory_tree`, `move_file`, `search_files`, `get_file_info`, `list_allowed_directories` |

| Proof call | Path | Result | Excerpt |
|---|---|---|---|
| `read_file` | `D:\github\open--claw\README.md` | **PASS** | `# Open Claw — A modular AI assistant platform...` |
| `read_file` | `D:\github\AI-Project-Manager\AGENTS.md` | **PASS** | `# AGENTS.md — This repo uses a five-tab Cursor workflow...` |

### B) shell-mcp

| Field | Value |
|---|---|
| Server key | `shell-mcp` |
| Descriptor folder | `mcps/user-shell-mcp/` — **present** |
| Tool count | **1** |
| Tools | `execute_command` |
| Binary | `C:\Users\ynotf\.local\bin\shell-mcp-server.exe` (v0.1.0, patched) |

| Command | Shell | Result | Output |
|---|---|---|---|
| `whoami` | pwsh | **PASS** | `chaoscentral\ynotf` |
| `dir /b` in `D:\github\AI-Project-Manager` | cmd | **PASS** | `.cursor .gitignore AGENTS.md docs README.md` |
| `$PSVersionTable.PSVersion.ToString()` | pwsh | **PASS** | `7.5.4` |

**Overall: PASS** — both MCP servers connected, tools listed, proof calls all succeeded.

---

## Entry: 2026-02-24 — shell-mcp-server Installation

**Timestamp:** 2026-02-24 00:30 local (UTC-5 EST)

### Install Method
`uv tool install shell-mcp-server` (was already installed — v0.1.0)

### Binary
`C:\Users\ynotf\.local\bin\shell-mcp-server.exe`

### MCP Entry (`shell-mcp`)

| Field | Value |
|---|---|
| command | `shell-mcp-server` |
| Allowed dirs | `D:\github`, `D:\github_2`, `C:\Users\ynotf\.openclaw` |
| Shells configured | `pwsh` (PS7), `powershell` (PS5), `cmd`, `bash` (WSL) |

### Evidence

| Check | Result |
|---|---|
| `uv --version` | **PASS** — 0.9.18 |
| `uv tool install shell-mcp-server` | **PASS** — v0.1.0 already installed |
| `shell-mcp-server --help` | **PASS** — correct args format confirmed |
| JSON valid after edit | **PASS** |
| `filesystem_fulldisk` removed | **PASS** — Cursor ignores `disabled: true`; removed to prevent unscoped C:\\ + D:\\ access |
| `shell-mcp` command → absolute path | **PASS** — `C:\Users\ynotf\.local\bin\shell-mcp-server.exe` |
| Stale process cleanup (20 killed) | **PASS** |
| Cursor restart + MCP connection | **PENDING** — toggle shell-mcp and filesystem_scoped in MCP panel |

---

## Entry: 2026-02-24 — filesystem_scoped + filesystem_fulldisk Installation

**Timestamp:** 2026-02-24 00:10 local (UTC-5 EST)

### A) Preflight

| Check | Result |
|---|---|
| node | **PASS** — v22.18.0 |
| npm | **PASS** — 11.7.0 |
| pnpm | **PASS** — 10.24.0 |
| WSL default distro | **PASS** — `Ubuntu` |
| `Test-Path D:\github` | **PASS** |
| `Test-Path D:\github_2` | **PASS** |
| `Test-Path %USERPROFILE%\.openclaw` | **PASS** — `C:\Users\ynotf\.openclaw` |
| `Test-Path \\wsl.localhost\Ubuntu\mnt\d\github` | **FAIL** — Access denied from PowerShell → **WSL_UNC_BLOCKED** |

**WSL_UNC_BLOCKED fix steps:**
- Option A: Add `\\wsl.localhost\Ubuntu` to `filesystem_scoped` args once Windows→WSL UNC permissions are fixed
- Option B (recommended): Run a second `mcp-server-wsl-filesystem` instance inside WSL via `wsl.exe -e npx ...`

### B) MCP Config Written

**File:** `C:\Users\ynotf\.cursor\mcp.json`

| Server | Status | Allowed roots |
|---|---|---|
| `filesystem_scoped` | **enabled** | `D:\github`, `D:\github_2`, `C:\Users\ynotf\.openclaw` |
| `filesystem_fulldisk` | **disabled** (`"disabled": true`) | `C:\`, `D:\` |
| `Filesystem` (old remote HTTP) | **removed** | — |

**Package:** `@modelcontextprotocol/server-filesystem` — pre-cached at `C:\Users\ynotf\AppData\Roaming\npm\node_modules\`

**Cursor restart required** to activate new servers.

### C) Proof Reads

| Tool | Path | Result | Excerpt |
|---|---|---|---|
| Cursor Read (native) | `D:\github\open--claw\README.md` | **PASS** | `# Open Claw — A modular AI assistant platform...` |
| Cursor Read (native) | `D:\github\AI-Project-Manager\AGENTS.md` | **PASS** | `# AGENTS.md — This repo uses a five-tab Cursor workflow...` |
| `filesystem_scoped` MCP tool | Any path | **PENDING** — Cursor restart required |
| WSL UNC read | `\\wsl.localhost\Ubuntu\mnt\d\github\...` | **BLOCKED** — see WSL_UNC_BLOCKED above |

### Post-Restart Verification (TODO)
After Cursor restart:
- [ ] Confirm `filesystem_scoped` shows connected in MCP panel
- [ ] Call `list_directory` on `D:\github` via `filesystem_scoped`
- [ ] Call `read_file` on `D:\github\open--claw\README.md` via `filesystem_scoped`
- [ ] Update this entry with PASS evidence

---

## Entry: 2026-02-23 — Filesystem MCP Proof + Cross-Platform Path Test

**Timestamp:** 2026-02-23 23:50 local (UTC-5 EST)

### A) Filesystem MCP Server Status

| Field | Value |
|---|---|
| Server ID (mcp.json key) | `Filesystem` |
| Type | HTTP (remote) |
| URL | `https://file-mcp-smith--bhushangitfull.run.tools` |
| Auth headers configured | **None** (`headers: {}`) |
| Descriptor folder in session | **Not present** |
| Session availability | **BLOCKED** — not connected |
| HTTP probe | `401 invalid_token` — server reachable but requires auth token |

**Root cause:** `headers` in mcp.json is empty — no API token configured. Server requires `Authorization` header.

**Tool list:** Unable to retrieve — server not connected.

**Recovery steps to fix Filesystem MCP:**
1. Obtain the API token for `https://file-mcp-smith--bhushangitfull.run.tools`
2. Add it to `~/.cursor/mcp.json` under `Filesystem.headers`: `{"Authorization": "Bearer <token>"}`
3. Restart Cursor to reconnect
4. Alternative: replace with `@modelcontextprotocol/server-filesystem` (local, no auth needed):
   ```json
   "Filesystem": {
     "command": "npx",
     "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:\\github"]
   }
   ```

### B) Cross-Platform Path Discovery

| Check | Result |
|---|---|
| WSL distro (`wsl -l -q`) | **PASS** — `Ubuntu` |
| `Test-Path D:\github\open--claw\README.md` | **PASS** |
| `Test-Path D:\github\AI-Project-Manager\AGENTS.md` | **PASS** |
| `Test-Path \\wsl$\Ubuntu\mnt\d\github\open--claw\README.md` | **FAIL** — Access denied from PowerShell |
| `wsl cat /mnt/d/github/open--claw/README.md` | **PASS** — readable from within WSL |

### C) Read-Only Proof Calls

| Tool | Path | Result | Excerpt |
|---|---|---|---|
| Read (Cursor native) | `D:\github\open--claw\README.md` | **PASS** | `# Open Claw — A modular AI assistant platform...` |
| Read (Cursor native) | `D:\github\AI-Project-Manager\AGENTS.md` | **PASS** | `# AGENTS.md — This repo uses a five-tab Cursor workflow...` |
| `wsl cat` | `/mnt/d/github/open--claw/README.md` | **PASS** | Same content confirmed |
| Filesystem MCP `read_file` | Any path | **SKIPPED** — server not connected |

**Cross-platform verdict: PARTIAL**
- Windows paths: **PASS** via Cursor native Read
- WSL UNC `\\wsl$\...` from PowerShell: **FAIL** — OS-level access denied
- WSL paths via `wsl cat`: **PASS**
- Filesystem MCP tool calls: **BLOCKED** — no auth token

### Remaining Gaps
1. Filesystem MCP needs auth token in `headers` (or replace with local `@modelcontextprotocol/server-filesystem`)
2. `\\wsl$\Ubuntu\...` UNC access from PowerShell denied — workaround: use `wsl` shell commands or mount drive differently

---

## Entry: 2026-02-23 — Smithery CLI + marco280690/mcp Connection Attempt

**Timestamp:** 2026-02-23 23:27 local (UTC-5 EST)

### Preflight

| Check | Result |
|---|---|
| `node --version` | **PASS** — v22.18.0 |
| `npm --version` | **PASS** — 11.7.0 |
| `pnpm --version` | **PASS** — 10.24.0 |

### Smithery CLI

| Check | Result |
|---|---|
| `pnpm dlx @smithery/cli@latest smithery --version` | **PASS** — 4.1.4 |
| `smithery --version` (global) | **PASS** — 4.1.4 (already installed) |
| `smithery auth whoami` | **PASS** — authenticated (API key redacted) |

### MCP Server Connection — marco280690/mcp

| Attempt | Command | Result |
|---|---|---|
| Primary | `smithery mcp add marco280690/mcp --id marco280690-mcp` | **FAIL** — 404 |
| Fallback (a) | `smithery mcp add @marco280690/mcp --id marco280690-mcp` | **FAIL** — 404 |
| Fallback (b) | `smithery mcp add https://server.smithery.ai/marco280690/mcp --id marco280690-mcp` | **FAIL** — 404 |
| Registry search | `smithery search marco280690` | **FAIL** — no results |
| Direct HTTP | `GET https://server.smithery.ai/marco280690/mcp` | **FAIL** — Server not found |

**Status: BLOCKED** — Server `marco280690/mcp` does not exist on Smithery registry.

### Recovery Steps
1. Verify the exact server ID at `https://smithery.ai/search?q=marco280690`
2. If private/unpublished: owner must publish it on Smithery first
3. If ID is wrong: provide corrected qualified name and re-run step D
4. Alternative: use `@modelcontextprotocol/server-sequential-thinking` if sequential-thinking was the intent

### Tool Verification + Sanity Call
**SKIPPED** — blocked by step D failure.

---

## Entry: 2026-02-23 — Serena Global Config Repair

**Timestamp:** 2026-02-23 22:53 local (UTC-5 EST)

**Config path:** `C:\Users\ynotf\.serena\serena_config.yml`

**Backup path:** `C:\Users\ynotf\.serena\serena_config.yml.backup.20260223-225332`

---

### Projects BEFORE

```
- D:\github\alerts-sheets
- D:\github\open-claw
```

### Projects AFTER

```
- D:\github\alerts-sheets
- D:\github\open--claw
- D:\github\AI-Project-Manager
```

**Mutation:** Removed `D:\github\open-claw` (single dash); added `D:\github\open--claw` and `D:\github\AI-Project-Manager`.

---

### Preflight Evidence

| Check | Result |
|---|---|
| `Test-Path $cfgPath` | **PASS** — `C:\Users\ynotf\.serena\serena_config.yml` exists |
| `Get-Content $cfgPath -TotalCount 120` | **PASS** — `projects:` section found |
| `Test-Path D:\github\open--claw` | **PASS** — directory exists |
| `Test-Path D:\github\AI-Project-Manager` | **PASS** — directory exists |

### Edit Evidence

| Check | Result |
|---|---|
| Backup created | **PASS** — `.backup.20260223-225332` |
| `open-claw` removed | **PASS** — 0 lines matching single-dash open-claw |
| `open--claw` present | **PASS** |
| `AI-Project-Manager` present | **PASS** |
| `alerts-sheets` preserved | **PASS** |

### Dashboard Verification

| Check | Result |
|---|---|
| `http://127.0.0.1:24282/dashboard/` | **PENDING** — requires Serena MCP restart first |

### Serena MCP Tool Call Evidence

| Tool call | Result |
|---|---|
| `activate_project(D:\github\open--claw)` | **WARN** — path recognized; no language source files yet (expected for new repo) |
| `activate_project(D:\github\AI-Project-Manager)` | **WARN** — path recognized; no language source files yet (expected for new repo) |
| `get_current_config()` | **PARTIAL** — Serena live but shows only `alerts-sheets`; running process loaded config before edit. **Restart required.** |

---

### Post-Restart Verification

| Check | Result | Notes |
|---|---|---|
| `open-claw` (single dash) removed | **PASS** | Confirmed via PowerShell parse |
| `open--claw` present | **PASS** | Confirmed via PowerShell parse |
| `AI-Project-Manager` present | **PASS** | Confirmed via PowerShell parse |
| `alerts-sheets` preserved | **PASS** | Confirmed via PowerShell parse |
| Serena process running | **PASS** | Single process tree after full Cursor restart |
| `get_current_config` MCP call | **N/A** | Serena registered as `serena` in global mcp.json; uses `--project-from-cwd`; config file is the authoritative source |

**Config repair: COMPLETE**

---

## 2026-03-01 — Global mcp.json JSON Fix + Secret Scrub

### Problem
`ConvertFrom-Json` failed with: `Unexpected character encountered while parsing value: }. Path 'mcpServers.github.env.GITHUB_PERSONAL_ACCESS_TOKEN'`

### Root Cause
Three malformed entries left blank values (invalid JSON):
- `github.env.GITHUB_PERSONAL_ACCESS_TOKEN:` ← missing value
- `firecrawl-mcp.env.FIRECRAWL_API_KEY:` ← missing value
- `Magic MCP.args` contained `"API_KEY=\""` ← empty remnant

### Fixes Applied
| Fix | Action |
|---|---|
| `github.env` | Set to `{}` — secret to be injected via `bws run` when wired |
| `firecrawl-mcp.env` | Set to `{}` — secret to be injected via `bws run` when wired |
| `Magic MCP.args` | Removed `"API_KEY=\""` arg entirely — args end at `@21st-dev/magic@latest` |

### Evidence
| Check | Result |
|---|---|
| Backup created | **PASS** — `mcp.json.backup.20260301-211451` |
| JSON parse after fix | **PASS** — 14 servers loaded |
| Secret literals in file | **PASS (none)** — all env blocks empty `{}` |
| Project `open--claw/.cursor/mcp.json` parse | **PASS** — valid JSON |
| Project mcp.json conflict | **WARN** — defines `filesystem-windows` (redundant with global `filesystem_scoped`); recommend removing it |

### Server Status (post-fix, requires Cursor restart to confirm)
| Server | Expected Status |
|---|---|
| Context7 | PASS (HTTP) |
| Exa Search | PASS (HTTP) |
| Memory Tool | PASS (HTTP) |
| Clear Thought 1.5 | PASS (HTTP) |
| serena | PASS (stdio) |
| sequential-thinking | PASS (stdio) |
| playwright | PASS (stdio) |
| filesystem_scoped | PASS (stdio) |
| shell-mcp | PASS (stdio) |
| github | BLOCKED — needs `GITHUB_PERSONAL_ACCESS_TOKEN` via bws |
| firecrawl-mcp | BLOCKED — needs `FIRECRAWL_API_KEY` via bws |
| Magic MCP | BLOCKED — needs `@21st-dev/magic` API key via bws |
| googlesheets-tvi8pq-94 | BLOCKED — Composio HTTP, needs valid session |
| firestore-mcp | WARN — Smithery CLI wrapper; verify Firestore project access |

### Recovery Steps (if restart fails)

1. Close all Cursor windows completely
2. Reopen Cursor
3. Verify MCP server `user-serena` is enabled in Settings → MCP
4. If still stale: check `C:\Users\ynotf\.serena\serena_config.yml` is correctly written (use `Get-Content` to verify)
5. If config is wrong, restore from backup: `Copy-Item <backupPath> $cfgPath -Force` and re-apply edits

---

## 2026-03-01 — OpenMemory Auth Fix

### Method Used
Option 2 (manual patch via bws run + temp PowerShell script). Option 1 (official 
px @openmemory/install) was blocked: requires interactive TTY, fails with ERR_TTY_INIT_FAILED in non-TTY shells.

### Steps
1. ws secret list — found only OPENMEMORY_API_KEY_2, no canonical OPENMEMORY_API_KEY
2. Created OPENMEMORY_API_KEY in Bitwarden from _2 value (no value printed)
3. Wrote temp script patch-openmemory.ps1 that reads injected env var and patches mcp.json
4. Ran: ws run --project-id f14a97bb... -- pwsh -NonInteractive -File patch-openmemory.ps1
5. Validated auth header set and JSON parses clean

### Evidence
| Check | Result |
|---|---|
| bws version | **PASS** — 2.0.0 |
| OpenClaw project found | **PASS** — f14a97bb-5183-4b11-a6eb-b3fe0015fedf |
| OPENMEMORY_API_KEY secret created | **PASS** — 6c9955ba-a991-4d26-92b9-b4010043efde |
| mcp.json backup | **PASS** — mcp.json.backup.20260301-230722 |
| Authorization header written | **PASS** — Token <41-char key>, no value in output |
| JSON parse after patch | **PASS** |
| /health probe | **PASS** — HTTP 200 |
| openmemory tools visible | **PENDING** — requires Cursor restart to confirm |
| Secret exposure | **PASS (none)** |

### Cleanup Needed
- Delete OPENMEMORY_API_KEY_2 from Bitwarden once OPENMEMORY_API_KEY is confirmed working across both machines

---

## 2026-03-01 — OpenMemory Auth Fix (ChaosCentral — double-Token correction)

### Problem Found
Previous patch produced "Token Token om-..." — the Bitwarden secret value itself began with "Token ", causing the prefix to be applied twice.

### Fix Applied
Rewrote patch script to strip any existing Token  prefix via -replace '^Token\s+', '' before writing "Token <raw_key>". Also removed any stray 	ype field from the openmemory entry.

### Evidence
| Check | Result |
|---|---|
| bws version | **PASS** — 2.0.0 |
| OPENMEMORY_API_KEY in Bitwarden | **PASS** — 6c9955ba |
| mcp.json backup | **PASS** — mcp.json.backup.20260301-232149 |
| Double-Token stripped | **PASS** — header is Token <35-char>, not Token Token ... |
| Type field absent | **PASS** |
| JSON parse | **PASS** |
| /health probe | **PASS** — HTTP 200 |
| openmemory tools visible | **PENDING** — requires Cursor restart |
| Secret exposure | **PASS (none)** |
