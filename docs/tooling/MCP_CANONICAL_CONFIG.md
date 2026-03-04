# MCP Canonical Configuration

**Last verified:** 2026-03-04 — all non-secret-dependent servers showing tools and connected.

This is the authoritative reference for the global Cursor MCP setup.
Apply this to every machine and every project. Secrets are injected at runtime
via Bitwarden Secrets Manager (`bws run`) — never stored in this file, in git,
or in `mcp.json`.

---

## How global MCP config works in Cursor

- **File:** `%USERPROFILE%\.cursor\mcp.json`  (Windows) / `~/.cursor/mcp.json` (Mac/Linux)
- Applies to **all** Cursor projects on the machine.
- Project-level `.cursor/mcp.json` can add servers but **cannot disable** global ones.
- Cursor has **no working `disabled` flag** — remove an entry to disable it.
- Each server spawns a subprocess; multiple toggles create stale processes. If servers stop
  responding, kill stale processes and toggle once cleanly.

---

## Working server list (2026-03-04)

### HTTP / remote servers (no local process)

| Key | URL | Purpose |
|---|---|---|
| `Context7` | `https://server.smithery.ai/@upstash/context7-mcp` | Library docs lookup |
| `Exa Search` | `https://mcp.exa.ai` | Web search |
| `openmemory` | `http://127.0.0.1:8766/mcp-stream?client=cursor` | Cross-session memory (via local proxy) |
| `Clear Thought 1.5` | `https://clear-thought--waldzellai.run.tools` | Reasoning/thinking |
| `Stripe` | `https://stripe.run.tools` | Stripe API |
| `googlesheets-tvi8pq-94` | `https://mcp.composio.dev/...` | Google Sheets |

### Local stdio servers (spawn a process)

| Key | Command | Purpose |
|---|---|---|
| `filesystem_scoped` | `npx -y @modelcontextprotocol/server-filesystem` | File read/write scoped to `D:\github`, `D:\github_2`, `.openclaw` |
| `shell-mcp` | `shell-mcp-server` (absolute path on Windows) | Shell command execution |
| `serena` | `uvx ... serena start-mcp-server` | Code navigation (LSP) |
| `sequential-thinking` | `npx -y @modelcontextprotocol/server-sequential-thinking` | Step-by-step reasoning |
| `playwright` | `npx @playwright/mcp@latest` | Browser automation |
| `github` | `npx -y @modelcontextprotocol/server-github` | GitHub API |
| `firecrawl-mcp` | `npx -y firecrawl-mcp` | Web scraping |
| `firestore-mcp` | `npx -y @smithery/cli@latest run @devlimelabs/firestore-mcp` | Firestore |
| `Magic MCP` | `cmd /c npx -y @21st-dev/magic@latest` | UI component generation |

---

## Full `mcp.json` template

Copy this to `%USERPROFILE%\.cursor\mcp.json`. Secrets are **not** stored in this
file — they are injected at runtime via `bws run` (see "Secret injection" section below).

```json
{
  "mcpServers": {
    "Context7": {
      "type": "http",
      "url": "https://server.smithery.ai/@upstash/context7-mcp",
      "headers": {}
    },
    "Exa Search": {
      "type": "http",
      "url": "https://mcp.exa.ai",
      "headers": {}
    },
    "openmemory": {
      "type": "http",
      "url": "http://127.0.0.1:8766/mcp-stream?client=cursor"
    },
    "Clear Thought 1.5": {
      "type": "http",
      "url": "https://clear-thought--waldzellai.run.tools",
      "headers": {}
    },
    "Stripe": {
      "type": "http",
      "url": "https://stripe.run.tools",
      "headers": {}
    },
    "googlesheets-tvi8pq-94": {
      "url": "https://mcp.composio.dev/partner/composio/googlesheets/mcp?customerId=COMPOSIO_CUSTOMER_ID&agent=cursor"
    },
    "filesystem_scoped": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "D:\\github",
        "D:\\github_2",
        "C:\\Users\\USERNAME\\.openclaw"
      ]
    },
    "shell-mcp": {
      "command": "C:\\Users\\USERNAME\\.local\\bin\\shell-mcp-server.exe",
      "args": [
        "D:\\github",
        "D:\\github_2",
        "C:\\Users\\USERNAME\\.openclaw",
        "--shell", "pwsh",       "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
        "--shell", "powershell", "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
        "--shell", "cmd",        "C:\\WINDOWS\\System32\\cmd.exe",
        "--shell", "bash",       "C:\\WINDOWS\\system32\\bash.exe"
      ]
    },
    "serena": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/oraios/serena",
        "serena",
        "start-mcp-server",
        "--project-from-cwd",
        "--transport",
        "stdio"
      ]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {}
    },
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {}
    },
    "firestore-mcp": {
      "command": "npx",
      "args": ["-y", "@smithery/cli@latest", "run", "@devlimelabs/firestore-mcp"]
    },
    "Magic MCP": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@21st-dev/magic@latest"],
      "env": {}
    }
  }
}
```

> **Note:** `github.env`, `firecrawl-mcp.env`, and `Magic MCP.env` are empty `{}`.
> These servers require `GITHUB_PERSONAL_ACCESS_TOKEN`, `FIRECRAWL_API_KEY`, and
> `TWENTY_FIRST_API_KEY` respectively. Secrets are injected via `bws run` at Cursor
> launch time (see below). Without secrets, these servers will start but fail auth on first call.

---

## Secret injection via Bitwarden (`bws run`)

Secrets **never** appear in `mcp.json` or in git. They are injected at runtime:

```
bws run --project-id <OPENCLAW_PROJECT_ID> -- pwsh -NoProfile -File ~\.openclaw\start-cursor-with-secrets.ps1
```

This command:
1. Exports all secrets from the Bitwarden `OpenClaw` project as environment variables
2. Runs `patch-mcp.ps1` to enforce secret-free `mcp.json` state
3. Starts the OpenMemory local proxy (`openmemory-proxy.mjs`) which reads `OPENMEMORY_API_KEY` from env
4. Launches Cursor — all child processes (MCP servers) inherit the injected env vars

### Bitwarden project

| Field | Value |
|---|---|
| Project name | `OpenClaw` |
| Project ID | `f14a97bb-5183-4b11-a6eb-b3fe0015fedf` |
| CLI | `bws` v2.0.0 at `~/.local/bin/bws.exe` |
| Auth | `BWS_ACCESS_TOKEN` set in machine environment (not in git) |

### Secrets stored (names only — values never printed)

| Secret name | Used by |
|---|---|
| `OPENMEMORY_API_KEY` | OpenMemory proxy (`openmemory-proxy.mjs`) |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | `github` MCP server |
| `FIRECRAWL_API_KEY` | `firecrawl-mcp` server |
| `TWENTY_FIRST_API_KEY` | Magic MCP (`@21st-dev/magic`) |
| `ANTHROPIC_API_KEY` | OpenClaw model routing (optional) |
| `OPENAI_API_KEY` | OpenClaw model routing (optional) |
| `BWS_ACCESS_TOKEN` | `bws` CLI auth (stored outside Bitwarden) |

### OpenMemory proxy architecture

```
Cursor ──HTTP──▶ 127.0.0.1:8766 (openmemory-proxy.mjs)
                      │
                      │ injects Authorization: Token $OPENMEMORY_API_KEY
                      ▼
              https://api.openmemory.dev
```

Local scripts (not in git, under `~/.openclaw/`):

| Script | Purpose |
|---|---|
| `patch-mcp.ps1` | Ensures `mcp.json` has no persisted auth headers; normalizes env blocks to `{}` |
| `start-cursor-with-secrets.ps1` | Patches MCP config, starts proxy, launches Cursor |
| `verify-openmemory.ps1` | Validates `mcp.json` hygiene + proxy health (HTTP 200) |
| `scripts/openmemory-proxy.mjs` | Node.js proxy that injects `Authorization` header from env |
| `scripts/start-openmemory-proxy.ps1` | Starts proxy in hidden window, writes PID file |
| `scripts/stop-openmemory-proxy.ps1` | Stops proxy via PID file |

---

## Prerequisites (must be installed before applying config)

| Tool | Install command | Notes |
|---|---|---|
| Node.js >= 18 | https://nodejs.org | Required for all `npx` servers and openmemory proxy |
| pnpm | `npm i -g pnpm` | Optional but faster |
| uv | https://docs.astral.sh/uv/getting-started/installation/ | Required for Serena |
| uvx | ships with uv | Required for Serena |
| shell-mcp-server | `uv tool install shell-mcp-server` | Then patch — see below |
| Git | https://git-scm.com | Required for github MCP |
| bws | https://github.com/bitwarden/sdk-sm/releases | Bitwarden Secrets Manager CLI v2.0.0 |

### shell-mcp-server patch (required — v0.1.0 has async bug)

After `uv tool install shell-mcp-server`, patch the installed `server.py`:

**File:** `%APPDATA%\uv\tools\shell-mcp-server\Lib\site-packages\shell_mcp_server\server.py`

Change the bottom of the file from:
```python
async def main():
    """Main entry point for the shell MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        ...
```

To:
```python
async def _main_async():
    """Async implementation of the shell MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        ...

def main():
    """Sync entry point called by the compiled .exe console script."""
    import asyncio
    asyncio.run(_main_async())
```

This fixes `coroutine 'main' was never awaited` on Windows.

---

## Serena project registration

Serena uses `--project-from-cwd` — it activates based on the folder Cursor opens.
Registered projects live in `%USERPROFILE%\.serena\serena_config.yml` under `projects:`.

Current registered projects:
```yaml
projects:
- D:\github\alerts-sheets
- D:\github\open--claw
- D:\github\AI-Project-Manager
```

To add a new project: append its path to the `projects:` list in that file,
then restart Serena (toggle in MCP panel or restart Cursor).

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Server shows no tools | Stale process from previous toggle | Kill stale processes + toggle once |
| `coroutine was never awaited` | shell-mcp-server v0.1.0 async bug | Apply patch above |
| Serena only shows one project | Process loaded old config | Full Cursor restart (not just toggle) |
| `filesystem_fulldisk` running unscoped | Cursor ignores `disabled: true` | Remove the entry entirely |
| WSL UNC `\\wsl$\...` access denied | PowerShell permission restriction | Use `wsl` shell commands as workaround |
| OpenMemory red / no tools | Proxy not running or `OPENMEMORY_API_KEY` missing | Launch via `bws run ... start-cursor-with-secrets.ps1` |
| OpenMemory `Token Token ...` error | Bitwarden secret has `Token ` prefix in value | Store raw key only (`om-...`); proxy adds prefix |
| `github` / `firecrawl-mcp` / `Magic MCP` fail auth | `env: {}` in mcp.json, secrets not injected | Launch Cursor via `bws run` (Phase 5 wiring) |

### Kill stale MCP processes (PowerShell)
```powershell
Get-WmiObject Win32_Process | Where-Object {
    ($_.CommandLine -like '*server-filesystem*' -or
     $_.CommandLine -like '*shell-mcp-server*' -or
     $_.CommandLine -like '*serena*') -and
    $_.Name -ne 'pwsh.exe'
} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
```
