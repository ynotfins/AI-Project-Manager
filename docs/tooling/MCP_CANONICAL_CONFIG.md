# MCP Canonical Configuration

**Last verified:** 2026-03-16 — tri-workspace expansion (droidrun added); context budget optimized; tool count ~52.

This is the authoritative reference for the global Cursor MCP setup.
Apply this to every machine and every project. Secrets are injected at runtime
via Bitwarden Secrets Manager (`bws run`) — never stored in this file, in git,
or in `mcp.json`.

---

## Tri-workspace architecture

The Cursor workspace (`openclaw.code-workspace`) contains three projects forming a full-stack AI + mobile control system:

| Project | Role | Path |
|---|---|---|
| **AI-Project-Manager** | Orchestration layer — governance, rules, state tracking, agent planning | `D:\github\AI-Project-Manager` |
| **open--claw** | Agent brain — AI processing, OpenClaw gateway, WhatsApp/Telegram channels | `D:\github\open--claw` |
| **droidrun** | Runtime layer — phone control via ADB + DroidRun Portal, MCP server (`phone_do`/`phone_ping`/`phone_apps`) | `D:\github\droidrun` |

### Integration points
- **open--claw → droidrun**: OpenClaw agent (Sparky) calls DroidRun MCP tools to control the Samsung Galaxy S25 Ultra
- **AI-Project-Manager → all**: Governance rules (`.cursor/rules/`) are canonical in AI-PM and synced to droidrun; open--claw has its own mirror
- **Shared MCP config**: All three projects share the same `%USERPROFILE%\.cursor\mcp.json` (global Cursor config)
- **Phone target**: Samsung Galaxy S25 Ultra, Tailscale IP `100.71.228.18`, ADB port `5555`, DroidRun Portal `tcp:8080`

### Bitwarden accounts (two separate machine accounts)

| Account | Token env var | Used by | Secrets |
|---|---|---|---|
| OpenClaw machine account | `BWS_ACCESS_TOKEN` (injected via `bws run`) | OpenClaw gateway, MCP servers | ANTHROPIC, OPENAI, OPENROUTER, FIRECRAWL, GITHUB, OPENMEMORY API keys |
| droidrun-windows machine account | `BWS_DROIDRUN_TOKEN` (fetched from `bw get item`) | DroidRun MCP server | `DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY` |

DroidRun secret IDs (in Bitwarden Secrets Manager, droidrun project):

| Secret | ID |
|---|---|
| `DROIDRUN_DEEPSEEK_KEY` | `14d69c11-99ba-428f-a656-b40e014e72ae` |
| `DROIDRUN_OPENROUTER_KEY` | `f9ed80a7-fc35-4add-96d6-b40e0163b041` |

### Merged startup flow (`start-cursor-with-secrets.ps1`)

```
bws run (OpenClaw machine account)
  → Env vars: ANTHROPIC, OPENAI, OPENROUTER, FIRECRAWL, GITHUB, OPENMEMORY keys
  → patch-mcp.ps1 (enforce clean mcp.json)
  → start-openmemory-proxy.ps1 (OpenMemory local proxy on :8766)
  → DroidRun block (try/catch — non-blocking):
      → bw get item BWS_DROIDRUN_TOKEN (separate vault account)
      → bws secret get (droidrun machine account) → DROIDRUN_DEEPSEEK_KEY, DROIDRUN_OPENROUTER_KEY
      → adb smart reconnect: check → connect → adb_find_port.ps1 (post-reboot)
  → Start-Process Cursor (openclaw.code-workspace — 3 folders)
  → WSL gateway: write transient .gateway-env → systemd restart → delete .gateway-env
  → Windows node host: update node.cmd WSL IP → kill stale → launch hidden
```

### Cursor rules synchronization

Rules files are canonical in AI-Project-Manager and must be synced to droidrun whenever they change:

| File | AI-PM (canonical) | droidrun (copy) | open--claw |
|---|---|---|---|
| `00-global-core.md` | ✓ canonical | ✓ synced | separate |
| `05-global-mcp-usage.md` | ✓ canonical | ✓ synced | separate |
| `10-project-workflow.md` | ✓ canonical | ✓ synced | separate |
| `20-project-quality.md` | ✓ canonical | ✓ synced | separate |

---

## How global MCP config works in Cursor

- **File:** `%USERPROFILE%\.cursor\mcp.json`  (Windows) / `~/.cursor/mcp.json` (Mac/Linux)
- Applies to **all** Cursor projects on the machine.
- Project-level `.cursor/mcp.json` can add servers but **cannot disable** global ones.
- Cursor has **no working `disabled` flag** — remove an entry to disable it.
- Each server spawns a subprocess; multiple toggles create stale processes. If servers stop
  responding, kill stale processes and toggle once cleanly.
- **Individual tool toggles exist within each server** — use these to disable specific tools
  without removing the entire server entry.

---

## Context budget: why tools are disabled

Each enabled MCP tool consumes tokens in every conversation's context window. With ~200 tools
active, ~90% of the context budget was consumed before any conversation started.

**Target:** ~52 active tools across all enabled servers.

---

## Enabled servers (2026-03-16)

### HTTP / remote servers

| Key | URL | Active tools | Purpose |
|---|---|---|---|
| `Clear Thought 1.5` | `https://clear-thought--waldzellai.run.tools` | `clear_thought` (1) | **Primary reasoning tool** |
| `Context7` | `https://server.smithery.ai/@upstash/context7-mcp` | `resolve-library-id`, `query-docs` (2) | Library docs lookup |
| `openmemory` | `http://127.0.0.1:8766/mcp-stream?client=cursor` | 7 memory tools | Cross-session memory (via local proxy) |

### Local stdio servers

| Key | Command | Active tools | Purpose |
|---|---|---|---|
| `serena` | `uvx ... serena start-mcp-server` | ~25 code intelligence tools | Code navigation (LSP) |
| `github` | `npx -y @modelcontextprotocol/server-github` | ~10 (user-trimmed) | GitHub API |
| `sequential-thinking` | `npx -y @modelcontextprotocol/server-sequential-thinking` | `sequentialthinking` (1) | Step-by-step reasoning — **fallback only** |
| `firecrawl-mcp` | `npx -y firecrawl-mcp` | `scrape`, `map`, `search` (3 active, 8 disabled) | Web scraping |
| `droidrun` | (droidrun MCP server) | `phone_do`, `phone_ping`, `phone_apps` (3) | Phone automation (Samsung Galaxy S25 Ultra) |

---

## Disabled servers (context optimization)

These servers are removed from `mcp.json` or toggled off. Re-enable only when specifically needed.
See `.cursor/rules/05-global-mcp-usage.md` for the disabled tool activation policy.

| Key | Was used for | Re-enable if |
|---|---|---|
| `Exa Search` | Web search | Context7 cannot answer + firecrawl insufficient |
| `playwright` | Browser automation | Frontend UI verification is specifically required |
| `Magic MCP` | UI component generation | Generating design-system components from descriptions |
| `filesystem_scoped` | Scoped file read/write | Direct filesystem ops not coverable by serena/Shell |
| `shell-mcp` | Shell command execution | Shell tool is unavailable (shell-mcp has known async bug on Windows) |
| `firestore-mcp` | Firestore database | Firestore operations are needed |
| `googlesheets-tvi8pq-94` | Google Sheets | Sheets integration is required |
| `Stripe` | Stripe API | Stripe operations are needed |
| `extension-GitKraken` | GitKraken extension | GitKraken-specific operations |
| `cloudflare-bindings` | Cloudflare Workers bindings | Cloudflare dev work |
| `cloudflare-builds` | Cloudflare CI/CD | Monitoring Cloudflare builds |
| `cloudflare-docs` | Cloudflare documentation | Cloudflare-specific doc lookup |
| `cloudflare-observability` | Cloudflare logs/metrics | Cloudflare observability |

---

## Full `mcp.json` template

Copy the **enabled** block to `%USERPROFILE%\.cursor\mcp.json`. The disabled block is kept
here for reference — do not add it to `mcp.json` unless re-enabling.

Secrets are **not** stored in this file — they are injected at runtime via `bws run`.

### Enabled servers block

```json
{
  "mcpServers": {
    "Clear Thought 1.5": {
      "type": "http",
      "url": "https://clear-thought--waldzellai.run.tools",
      "headers": {}
    },
    "Context7": {
      "type": "http",
      "url": "https://server.smithery.ai/@upstash/context7-mcp",
      "headers": {}
    },
    "openmemory": {
      "type": "http",
      "url": "http://127.0.0.1:8766/mcp-stream?client=cursor"
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
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {}
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {}
    },
    "droidrun": {
      "command": "...",
      "args": ["..."]
    }
  }
}
```

### Disabled servers (reference only — do not add to mcp.json)

```jsonc
// Exa Search
// { "type": "http", "url": "https://mcp.exa.ai", "headers": {} }

// playwright
// { "command": "npx", "args": ["@playwright/mcp@latest"] }

// Magic MCP
// { "command": "cmd", "args": ["/c", "npx", "-y", "@21st-dev/magic@latest"], "env": {} }

// filesystem_scoped
// { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:\\github", ...] }

// shell-mcp (has async bug on Windows — apply patch before re-enabling, see Troubleshooting)
// { "command": "C:\\Users\\USERNAME\\.local\\bin\\shell-mcp-server.exe", "args": [...] }

// firestore-mcp
// { "command": "npx", "args": ["-y", "@smithery/cli@latest", "run", "@devlimelabs/firestore-mcp"] }

// googlesheets-tvi8pq-94
// { "url": "https://mcp.composio.dev/partner/composio/googlesheets/mcp?customerId=...&agent=cursor" }

// Stripe
// { "type": "http", "url": "https://stripe.run.tools", "headers": {} }
```

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
5. Writes a transient `~/.openclaw/.gateway-env` for the WSL gateway systemd service (deleted after ~8s)

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
| `ANTHROPIC_API_KEY` | OpenClaw model routing + WSL gateway |
| `OPENAI_API_KEY` | OpenClaw model routing + WSL gateway |
| `OPENROUTER_API_KEY` | OpenClaw model routing + WSL gateway |
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
| `start-cursor-with-secrets.ps1` | Patches MCP config, starts proxy, launches Cursor, starts WSL gateway + Windows node |
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
| Git | https://git-scm.com | Required for github MCP |
| bws | https://github.com/bitwarden/sdk-sm/releases | Bitwarden Secrets Manager CLI v2.0.0 |

> **shell-mcp-server:** Disabled. If re-enabling, install with `uv tool install shell-mcp-server` then apply the async patch — see archived Troubleshooting section.

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
| Serena only shows one project | Process loaded old config | Full Cursor restart (not just toggle) |
| WSL UNC `\\wsl$\...` access denied | PowerShell permission restriction | Use `wsl` shell commands as workaround |
| OpenMemory red / no tools | Proxy not running or `OPENMEMORY_API_KEY` missing | Launch via `bws run ... start-cursor-with-secrets.ps1` |
| OpenMemory `Token Token ...` error | Bitwarden secret has `Token ` prefix in value | Store raw key only (`om-...`); proxy adds prefix |
| `github` / `firecrawl-mcp` fail auth | `env: {}` in mcp.json, secrets not injected | Launch Cursor via `bws run` |
| Context window 90% consumed on start | Too many MCP tools enabled | Keep disabled servers out of `mcp.json`; use individual tool toggles within servers |
| Gateway API key unresolved | `ANTHROPIC_API_KEY` not in systemd env | Restart gateway via `start-cursor-with-secrets.ps1` (writes transient `.gateway-env`) |

### Kill stale MCP processes (PowerShell)
```powershell
Get-WmiObject Win32_Process | Where-Object {
    ($_.CommandLine -like '*server-filesystem*' -or
     $_.CommandLine -like '*shell-mcp-server*' -or
     $_.CommandLine -like '*serena*') -and
    $_.Name -ne 'pwsh.exe'
} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
```
