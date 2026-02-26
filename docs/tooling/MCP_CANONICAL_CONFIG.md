# MCP Canonical Configuration

**Last verified:** 2026-02-25 — all servers showing tools and connected.

This is the authoritative reference for the global Cursor MCP setup.
Apply this to every machine and every project. Secrets live in the machine's
keyring / `.env.local` — never in this file or git.

---

## How global MCP config works in Cursor

- **File:** `%USERPROFILE%\.cursor\mcp.json`  (Windows) / `~/.cursor/mcp.json` (Mac/Linux)
- Applies to **all** Cursor projects on the machine.
- Project-level `.cursor/mcp.json` can add servers but **cannot disable** global ones.
- Cursor has **no working `disabled` flag** — remove an entry to disable it.
- Each server spawns a subprocess; multiple toggles create stale processes. If servers stop
  responding, kill stale processes and toggle once cleanly.

---

## Working server list (2026-02-25)

### HTTP / remote servers (no local process)

| Key | URL | Purpose |
|---|---|---|
| `Context7` | `https://server.smithery.ai/@upstash/context7-mcp` | Library docs lookup |
| `Exa Search` | `https://mcp.exa.ai` | Web search |
| `Memory Tool` | `https://server.smithery.ai/@mem0ai/mem0-memory-mcp` | Cross-session memory |
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

Copy this to `%USERPROFILE%\.cursor\mcp.json`. Fill in `YOUR_*` placeholders from
your secrets store (1Password / keyring). Never commit secrets.

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
    "Memory Tool": {
      "type": "http",
      "url": "https://server.smithery.ai/@mem0ai/mem0-memory-mcp",
      "headers": {}
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
      "url": "https://mcp.composio.dev/partner/composio/googlesheets/mcp?customerId=YOUR_COMPOSIO_CUSTOMER_ID&agent=cursor"
    },
    "filesystem_scoped": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "D:\\github",
        "D:\\github_2",
        "C:\\Users\\YOUR_USERNAME\\.openclaw"
      ]
    },
    "shell-mcp": {
      "command": "C:\\Users\\YOUR_USERNAME\\.local\\bin\\shell-mcp-server.exe",
      "args": [
        "D:\\github",
        "D:\\github_2",
        "C:\\Users\\YOUR_USERNAME\\.openclaw",
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
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PAT"
      }
    },
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_KEY"
      }
    },
    "firestore-mcp": {
      "command": "npx",
      "args": ["-y", "@smithery/cli@latest", "run", "@devlimelabs/firestore-mcp"]
    },
    "Magic MCP": {
      "command": "cmd",
      "args": [
        "/c", "npx", "-y", "@21st-dev/magic@latest",
        "API_KEY=\"YOUR_MAGIC_API_KEY\""
      ],
      "env": {}
    }
  }
}
```

---

## Prerequisites (must be installed before applying config)

| Tool | Install command | Notes |
|---|---|---|
| Node.js ≥ 18 | https://nodejs.org | Required for all `npx` servers |
| pnpm | `npm i -g pnpm` | Optional but faster |
| uv | https://docs.astral.sh/uv/getting-started/installation/ | Required for Serena |
| uvx | ships with uv | Required for Serena |
| shell-mcp-server | `uv tool install shell-mcp-server` | Then patch — see below |
| Git | https://git-scm.com | Required for github MCP |

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

### Kill stale MCP processes (PowerShell)
```powershell
Get-WmiObject Win32_Process | Where-Object {
    ($_.CommandLine -like '*server-filesystem*' -or
     $_.CommandLine -like '*shell-mcp-server*' -or
     $_.CommandLine -like '*serena*') -and
    $_.Name -ne 'pwsh.exe'
} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
```
