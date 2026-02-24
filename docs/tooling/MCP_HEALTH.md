# MCP Health Log

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

### Recovery Steps (if restart fails)

1. Close all Cursor windows completely
2. Reopen Cursor
3. Verify MCP server `user-serena` is enabled in Settings → MCP
4. If still stale: check `C:\Users\ynotf\.serena\serena_config.yml` is correctly written (use `Get-Content` to verify)
5. If config is wrong, restore from backup: `Copy-Item <backupPath> $cfgPath -Force` and re-apply edits
