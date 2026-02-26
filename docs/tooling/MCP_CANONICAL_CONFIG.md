# MCP Canonical Config — Global Setup

This document is the authoritative reference for the global Cursor MCP configuration on all machines.
Config lives at: `%USERPROFILE%\.cursor\mcp.json`

---

## Machine baseline requirements

| Tool | Required version | Install command |
|------|-----------------|-----------------|
| Node.js | ≥22 LTS | `winget install OpenJS.NodeJS.LTS` |
| npm/npx | bundled with Node | — |
| uv | ≥0.10 | `winget install astral-sh.uv` |
| uvx | bundled with uv | — |
| shell-mcp-server | 0.1.x | `uv tool install shell-mcp-server` |
| git | any recent | `winget install Git.Git` |

---

## Server list and transport

| Server key | Transport | Secret required (Bitwarden) |
|------------|-----------|----------------------------|
| `GitKraken` | stdio (gk.exe) | none |
| `Clear Thought 1.5` | http | none |
| `Context7` | http | none |
| `Exa Search` | http | none |
| `Memory Tool` | http | none |
| `Stripe` | http | none |
| `playwright` | stdio (npx) | none |
| `github` | stdio (npx) | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| `sequential-thinking` | stdio (npx) | none |
| `firecrawl-mcp` | stdio (npx) | `FIRECRAWL_API_KEY` |
| `firestore-mcp` | stdio (npx via smithery) | none |
| `Magic MCP` | stdio (npx via cmd) | Magic API key (positional arg) |
| `googlesheets-tvi8pq-94` | http (composio) | `customerId` in URL |
| `serena` | stdio (uvx from git) | none |
| `filesystem_scoped` | stdio (npx) | none |
| `shell-mcp` | stdio (shell-mcp-server.exe) | none |

---

## Bitwarden secret lookup

Before first use, fill these placeholders in `mcp.json` locally (never commit):

| Placeholder | Bitwarden item | Field |
|-------------|---------------|-------|
| `FROM_BITWARDEN` in `github.env.GITHUB_PERSONAL_ACCESS_TOKEN` | "GitHub PAT — MCP" | password |
| `FROM_BITWARDEN` in `firecrawl-mcp.env.FIRECRAWL_API_KEY` | "Firecrawl API" | password |
| `API_KEY="FROM_BITWARDEN"` in `Magic MCP.args` | "21st.dev Magic MCP" | password |
| `customerId=FROM_BITWARDEN` in `googlesheets-tvi8pq-94.url` | "Composio Google Sheets" | customerId |

---

## shell-mcp-server setup

```powershell
# Install
uv tool install shell-mcp-server

# Executable location
C:\Users\<USERNAME>\.local\bin\shell-mcp-server.exe

# Verify sync entrypoint (no patch needed in v0.1.0+)
$pythonExe = "$env:APPDATA\uv\tools\shell-mcp-server\Scripts\python.exe"
& $pythonExe -c "import sys; sys.argv=['s','D:\\github']; from shell_mcp_server import main; import inspect; print('sync:', not inspect.iscoroutinefunction(main))"
# Expected: sync: True
```

Note: In shell-mcp-server v0.1.0 the `__init__.py` already wraps `asyncio.run(server.main())` — no patch is needed. The `main()` in `__init__.py` is sync; `server.main()` is async.

---

## Serena setup

```powershell
# Create config dir
New-Item -ItemType Directory -Path "$env:USERPROFILE\.serena" -Force

# Create config file
@"
projects:
  - path: D:\github\open--claw
  - path: D:\github\AI-Project-Manager
"@ | Set-Content "$env:USERPROFILE\.serena\serena_config.yml"
```

Serena is loaded via `uvx --from git+https://github.com/oraios/serena` — no separate install needed beyond uv.

---

## Kill stale MCP processes (fix for "no tools" after restart)

Run this if a server shows connected but lists 0 tools:

```powershell
# Kill all node processes spawned for MCP (npx-based servers)
Get-Process -Name "node" -ErrorAction SilentlyContinue | Stop-Process -Force

# Kill shell-mcp-server if stale
Get-Process -Name "shell-mcp-server" -ErrorAction SilentlyContinue | Stop-Process -Force

# Kill uvx/serena if stale
Get-Process -Name "serena" -ErrorAction SilentlyContinue | Stop-Process -Force
```

Then fully quit and restart Cursor (File → Exit, not just reload window).

---

## Conflict policy

**Global-only**: All MCP servers must be in `%USERPROFILE%\.cursor\mcp.json`.

Per-project `.cursor\mcp.json` or `.vscode\mcp.json` files are **forbidden** (they shadow global config and cause stale-process issues).

Check both repos:
```powershell
Test-Path "D:\github\open--claw\.cursor\mcp.json"      # must be False
Test-Path "D:\github\open--claw\.vscode\mcp.json"      # must be False
Test-Path "D:\Github\AI-Project-Manager\.cursor\mcp.json"   # must be False
Test-Path "D:\Github\AI-Project-Manager\.vscode\mcp.json"   # must be False
```
