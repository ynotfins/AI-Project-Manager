# MCP Canonical Configuration

**Last verified:** 2026-04-12 — single global config remains canonical; fresh-chat preload remains separate from enabled-server availability; current live sanity in this session is `thinking-patterns` PASS, `openmemory` FAIL (not registered), `obsidian-vault` FAIL (not registered)

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

### Bitwarden accounts (three separate machine accounts)

| Account | Token env var | Used by | Secrets |
|---|---|---|---|
| OpenClaw machine account | `BWS_ACCESS_TOKEN` (injected via `bws run`) | OpenClaw gateway, MCP servers | ANTHROPIC, OPENAI, OPENROUTER, FIRECRAWL, GITHUB, OPENMEMORY API keys |
| droidrun-windows machine account | `BWS_DROIDRUN_TOKEN` (fetched from `bw get item`) | DroidRun MCP server | `DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY` |
| R3lentle$$-Grind-Global-Memory | runtime-injected `BWS_ACCESS_TOKEN` | No-Loss memory system, autonomous secret management | `CURSOR_LOSSLESS_OPENMEMORY_API_KEY` |

Organization ID: `8098135b-9af5-41d7-9bcc-b3fa001d7cea`

DroidRun secret IDs (in Bitwarden Secrets Manager, droidrun project):

| Secret | ID |
|---|---|
| `DROIDRUN_DEEPSEEK_KEY` | `14d69c11-99ba-428f-a656-b40e014e72ae` |
| `DROIDRUN_OPENROUTER_KEY` | `f9ed80a7-fc35-4add-96d6-b40e0163b041` |

### Merged startup flow (`start-cursor-with-secrets.ps1`)

```
bws run (OpenClaw machine account)
  → Env vars: ANTHROPIC, OPENAI, OPENROUTER, FIRECRAWL, GITHUB, OPENMEMORY keys
  → patch-mcp.ps1 (enforce local durable OpenMemory config)
  → Cursor launches openmemory as: python D:\github\AI-Project-Manager\scripts\openmemory_cursor_server.py
  → DroidRun block (try/catch — non-blocking):
      → bw get item BWS_DROIDRUN_TOKEN (separate vault account)
      → bws secret get (droidrun machine account) → DROIDRUN_DEEPSEEK_KEY, DROIDRUN_OPENROUTER_KEY
      → adb smart reconnect: check → connect → adb_find_port.ps1 (post-reboot)
  → Start-Process Cursor (openclaw.code-workspace — 3 folders)
  → WSL gateway: write transient .gateway-env → systemd restart → delete .gateway-env
  → Windows node host: 
      → extract gateway token from WSL openclaw.json (canonical source)
      → regenerate node.cmd with current token + loopback host (127.0.0.1)
      → restart pwsh watchdog (hidden, durable across restarts)
```

**Startup warning classification (2026-04-10):**

Real local issues (must fix):
- Missing BWS_ACCESS_TOKEN or BWS_DROIDRUN_TOKEN
- Missing required env vars (GITHUB_PERSONAL_ACCESS_TOKEN, FIRECRAWL_API_KEY)
- OpenClaw gateway token extraction failure from WSL openclaw.json
- Gateway systemd restart failure in WSL
- Node host launch failure on Windows

Tolerated upstream/no-action noise:
- Bitwarden CLI informational messages about POSIX compliance (no action needed if secrets work)
- OpenMemory upstream /health 504 Gateway Time-out (local stdio server is canonical)
- Cursor MCP server connection retries during startup (transient)
- WSL network/DNS warnings during gateway health check (tolerate if gateway responds)
- Node.js deprecation warnings from npx/MCP server startup (upstream package maintenance)

### Cursor rules synchronization

Rules files are canonical in AI-Project-Manager and must be mirrored to sibling repos whenever they change:

| File | AI-PM (canonical) | droidrun (copy) | open--claw |
|---|---|---|---|
| `00-global-core.md` | ✓ canonical | ✓ synced | separate |
| `01-charter-enforcement.md` | ✓ canonical | ✓ synced | separate |
| `02-non-routable-exclusions.md` | ✓ canonical | ✓ synced | separate |
| `05-global-mcp-usage.md` | ✓ canonical | ✓ synced | separate |
| `10-project-workflow.md` | ✓ canonical | ✓ synced | separate |
| `20-project-quality.md` | ✓ canonical | ✓ synced | separate |
| `openmemory.mdc` | ✓ canonical | ✓ synced | n/a |

---

## How global MCP config works in Cursor

- **File:** `%USERPROFILE%\.cursor\mcp.json`  (Windows) / `~/.cursor/mcp.json` (Mac/Linux)
- Applies to **all** Cursor projects on the machine.
- Workspace-local `.cursor/mcp.json` files are not used in this setup.
- Cursor has **no working `disabled` flag** — remove an entry to disable it.
- Each server spawns a subprocess; multiple toggles create stale processes. If servers stop
  responding, kill stale processes and toggle once cleanly.
- Individual tool usage is governed by repo rules and PLAN's `Required Tools` / `Safe to disable` lines, not by per-repo MCP config splits.

---

## Enabled servers vs fresh-chat preload

- Enabled in `mcp.json` means the server is available to call on this machine.
- Enabled does **not** mean its docs, outputs, or tool surface become default fresh-chat context.
- Enabled also does **not** guarantee the current Cursor session has registered the server yet; after config churn or degraded sessions, restart Cursor via the launcher and re-probe required tools.
- Default PLAN preload stays lean:
  1. lightweight always-apply rules auto-load
  2. for non-trivial work, use `thinking-patterns`
  3. search active-project OpenMemory first
  4. search governance memory only if cross-repo, containment, routing, or policy concerns are in scope
  5. read `docs/ai/STATE.md`
  6. read exactly one of `DECISIONS.md`, `PATTERNS.md`, or `HANDOFF.md` only if needed
  7. use `obsidian-vault` only for operator notes or personal research already known to live there
  8. read the execution ledger only as a last resort, one block at a time
- This distinction is how the tri-workspace keeps tool availability broad while keeping fresh PLAN chats low-bloat.

---

## Context budget: why tools are disabled

The current strategy is a stable core plus optional on-demand servers, then context control with:

- OpenMemory-first retrieval
- exact-path Serena activation
- gated ledger reads
- selective file attachment

Core default-on:

- `openmemory`
- `Context7`
- `thinking-patterns`

On-demand tiers:

- `serena`, `github`
- `Exa Search`, `firecrawl-mcp`, `context-matic`
- `playwright`, `Magic MCP`
- `droidrun`, `obsidian-vault`, `filesystem`

---

## Configured servers on this machine (current canonical config)

### Active servers in the canonical `~/.cursor/mcp.json`

| Key | Type | Active tools | No-Loss role |
|---|---|---|---|
| `thinking-patterns` | stdio | multi-tool reasoning set (`mental_model`, `debugging_approach`, `decision_framework`, etc.) | Reasoning → stored as decisions |
| `Context7` | HTTP | `resolve-library-id`, `query-docs` (2) | External docs (NOT stored) |
| `openmemory` | stdio | 4 memory tools via local compatibility server | Persistence backbone |
| `Exa Search` | HTTP | web search | Research → stored as patterns |
| `serena` | stdio | ~25 code intelligence | Architecture → stored as components |
| `github` | stdio | ~10 (trimmed) | Repo ops (no memory artifacts) |
| `firecrawl-mcp` | stdio | `scrape`, `map`, `search` (3) | Web extraction → stored as patterns |
| `playwright` | stdio | browser automation | UI verification → stored as debug |
| `Magic MCP` | stdio | UI generation | Scaffolds → stored as components |
| `droidrun` | stdio | `phone_do`, `phone_ping`, `phone_apps` (3) | Phone ops (no memory artifacts) |
| `context-matic` | HTTP | API-integration workflow tools | Vendor API integration acceleration |
| `filesystem` | stdio | local file/vault access tools | On-demand local-knowledge bridge |
| `obsidian-vault` | stdio | task-oriented Obsidian note tools via Local REST API | Fast-access scoped note memory (NOT agent state) |

---

## Live sanity in this session

| Server | Check | Result | Notes |
|---|---|---|---|
| `thinking-patterns` | `CallMcpTool(user-thinking-patterns.sequential_thinking)` | PASS | Returned a valid minimal change and verification plan |
| `openmemory` | `CallMcpTool(user-openmemory.search-memories)` and `CallMcpTool(openmemory.search-memories)` | FAIL | Current Cursor session reports `MCP server does not exist`; `scripts/check_openmemory_stack.ps1` passed, so the local stack looks healthy and the session likely needs reload |
| `obsidian-vault` | `CallMcpTool(user-obsidian-vault.obsidian_global_search)` and `CallMcpTool(obsidian-vault.obsidian_global_search)` | FAIL | Current Cursor session reports `MCP server does not exist`; reload is required before targeted-search reachability can be re-proven |

---

## Removed servers

These are permanently removed from the toolchain:

| Key | Reason |
|---|---|
| `sequential-thinking` | Removed as a standalone server; use `thinking-patterns.sequential_thinking` |
| `shell-mcp` | Removed; use built-in Shell |
| `extension-GitKraken` | Extension uninstalled; MCP cache deleted (2026-04-07 and 2026-04-10 full cleanup) |
| `googlesheets-tvi8pq-94` | Removed |
| `firestore-mcp` | Removed |
| `filesystem_scoped` | Redundant with serena + Shell |

## Formerly disabled, now always enabled

`Exa Search`, `playwright`, and `Magic MCP` are now always enabled in the global config. Tool descriptor cost is small (~500-1000 tokens each). The real context savings come from the No-Loss memory system, not from toggling tools.
| `cloudflare-docs` | Cloudflare documentation | Cloudflare-specific doc lookup |
| `cloudflare-observability` | Cloudflare logs/metrics | Cloudflare observability |

---

## Canonical `mcp.json` excerpt

Keep `%USERPROFILE%\.cursor\mcp.json` as the single authoritative MCP config for this machine. Do not split active servers into workspace-local `.cursor/mcp.json` files.

Secrets are **not** stored in this file — they are injected at runtime via `bws run`.

### Enabled servers block

```json
{
  "mcpServers": {
    "thinking-patterns": {
      "command": "thinking-patterns"
    },
    "Context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {}
    },
    "openmemory": {
      "command": "python",
      "args": ["D:\\github\\AI-Project-Manager\\scripts\\openmemory_cursor_server.py"],
      "env": {
        "CLIENT_NAME": "cursor",
        "OPENMEMORY_STORE_PATH": "C:\\Users\\ynotf\\.openclaw\\data\\openmemory-cursor.sqlite3"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {}
    },
    "obsidian-vault": {
      "command": "npx",
      "args": ["-y", "obsidian-mcp-server"],
      "env": {
        "OBSIDIAN_BASE_URL": "http://127.0.0.1:27123",
        "OBSIDIAN_VERIFY_SSL": "false"
      }
    }
  }
}
```

Runtime note:

- The local durable OpenMemory compatibility server is the canonical Cursor memory runtime on this machine.
- Zero-trust checks on 2026-04-10 confirmed the local Obsidian REST API is live on `http://127.0.0.1:27123`.
- `https://127.0.0.1:27123` is incorrect for the current local plugin state.
- HTTPS is defined by the local OpenAPI spec on port `27124`, not `27123`.
- The Obsidian API key is inherited at launch time as `OBSIDIAN_API_KEY`; it is not written into `mcp.json`.

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
3. Launches Cursor — all child processes (MCP servers) inherit the injected env vars
4. Cursor starts the local OpenMemory compatibility server and points it at the durable local SQLite store
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
| `OPENMEMORY_API_KEY` | Historical hosted OpenMemory path only; no longer required by the local Cursor memory runtime |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | `github` MCP server |
| `FIRECRAWL_API_KEY` | `firecrawl-mcp` server |
| `ANTHROPIC_API_KEY` | OpenClaw model routing + WSL gateway |
| `OPENAI_API_KEY` | OpenClaw model routing + WSL gateway |
| `OPENROUTER_API_KEY` | OpenClaw model routing + WSL gateway |
| `BWS_ACCESS_TOKEN` | `bws` CLI auth (stored outside Bitwarden) |

### OpenMemory local stdio architecture

```
Cursor ──stdio──▶ python D:\github\AI-Project-Manager\scripts\openmemory_cursor_server.py
                     │
                     │ uses CLIENT_NAME=cursor + OPENMEMORY_STORE_PATH
                     ▼
             C:\Users\ynotf\.openclaw\data\openmemory-cursor.sqlite3
```

Local scripts (not in git, under `~/.openclaw/`):

| Script | Purpose |
|---|---|
| `patch-mcp.ps1` | Ensures `mcp.json` uses the local durable OpenMemory compatibility server |
| `start-cursor-with-secrets.ps1` | Patches MCP config, launches Cursor, starts WSL gateway + Windows node (with runtime token injection from WSL openclaw.json) |
| `verify-openmemory.ps1` | Validates `mcp.json` hygiene + local compatibility server startup |
| `validate-launcher-hardening.ps1` | Tests token injection, OpenMemory messaging, and startup warning classification (2026-04-10) |

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
| OpenMemory shows green but add/search/list fail | Broken hosted wrapper path or stale config | Re-run `start-cursor-with-secrets.ps1` so `mcp.json` is rewritten to the local compatibility server, then run `scripts/check_openmemory_stack.ps1` |
| OpenMemory local store roundtrip fails | Local compatibility server degraded or stale process | Run `scripts/check_openmemory_stack.ps1`; if `local store roundtrip` fails, inspect `scripts/openmemory_cursor_server.py` and restart Cursor |
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
