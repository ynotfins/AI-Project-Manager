# OpenMemory Guide — AI-Project-Manager

**project_id:** `ynotfins/AI-Project-Manager`
**client:** cursor
**server:** `openmemory` (hosted upstream; connected via local proxy for secret-free config)

## Overview

AI-Project-Manager is a Cursor workspace that serves as the control plane for the OpenClaw mobile project and related tooling. It contains:

- MCP server configuration (global `~/.cursor/mcp.json`)
- Cursor workflow rules (`.cursor/rules/`)
- AI state and planning docs (`docs/ai/`)
- Tooling health logs (`docs/tooling/`)

The repo is a documentation and configuration hub, not an application codebase. Primary language artifacts are markdown docs and JSON configs.

## Architecture

```text
AI-Project-Manager/
├── .cursor/rules/          # Cursor agent behavior rules (always-apply)
├── docs/
│   ├── ai/                 # STATE.md, PLAN.md, CURSOR_WORKFLOW.md, tabs/
│   └── tooling/            # MCP_HEALTH.md, MCP_CANONICAL_CONFIG.md
├── AGENTS.md               # Authoritative rule entrypoint
└── openmemory.md           # This file
```

## User Defined Namespaces

- `global` — user preferences applicable across all projects
- `AI-Project-Manager` — project facts, implementations, configs
- `open--claw` — OpenClaw project facts (stored with `project_id="ynotfins/open--claw"`)

## OpenMemory Auth Model (secret-free MCP config)

We do **not** persist auth headers in `%USERPROFILE%\\.cursor\\mcp.json`.

Instead:

- `%USERPROFILE%\\.cursor\\mcp.json` points `openmemory.url` to a **local proxy**: `http://127.0.0.1:8766/mcp-stream?client=cursor`
- `C:\\Users\\ynotf\\.openclaw\\scripts\\openmemory-proxy.mjs` forwards to `https://api.openmemory.dev/...` and injects `Authorization: Token <OPENMEMORY_API_KEY>` from the **process environment**.
- Cursor is launched with secrets injected via `bws run ...`, so both:
  - the proxy process, and
  - any MCP stdio servers (GitHub/Firecrawl/Magic/etc.)
  inherit secrets without writing them to disk.

Local scripts (not in git):

- `C:\\Users\\ynotf\\.openclaw\\patch-mcp.ps1` (enforces secret-free `mcp.json`)
- `C:\\Users\\ynotf\\.openclaw\\start-cursor-with-secrets.ps1` (patches MCP, starts proxy, launches Cursor)
- `C:\\Users\\ynotf\\.openclaw\\scripts\\start-openmemory-proxy.ps1` / `stop-openmemory-proxy.ps1`

## Components

| Component | Location | Purpose |
| --- | --- | --- |
| Global MCP Config | `~/.cursor/mcp.json` | Defines all 14 MCP servers for Cursor globally |
| Cursor Rules | `.cursor/rules/` | Always-apply agent behavior rules |
| STATE.md | `docs/ai/STATE.md` | Execution log updated after every task block |
| PLAN.md | `docs/ai/PLAN.md` | Active plan with phases and exit criteria |
| Tri-Workspace Context Brief | `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` | Fast routing layer for deciding which repo and entry points to inspect first |
| MCP_HEALTH.md | `docs/tooling/MCP_HEALTH.md` | MCP server health history and fixes |
| MCP_CANONICAL_CONFIG.md | `docs/tooling/MCP_CANONICAL_CONFIG.md` | Reference MCP config for reproducing setup |

## Active MCP Servers (14 total)

| Server | Type | Status |
| --- | --- | --- |
| openmemory | HTTP hosted | PASS — authenticated, tools working |
| Context7 | HTTP Smithery | PASS — unauthenticated public |
| Exa Search | HTTP | PASS — unauthenticated |
| Clear Thought 1.5 | HTTP | PASS — unauthenticated |
| serena | stdio uvx | PASS — LSP code nav |
| sequential-thinking | stdio npx | PASS |
| playwright | stdio npx | PASS |
| filesystem_scoped | stdio npx | PASS — covers D:\github, D:\github_2 |
| shell-mcp | stdio .exe | PASS — abs path to shell-mcp-server.exe |
| github | stdio npx | BLOCKED — needs GITHUB_PERSONAL_ACCESS_TOKEN |
| firecrawl-mcp | stdio npx | BLOCKED — needs FIRECRAWL_API_KEY |
| Magic MCP | stdio cmd/npx | BLOCKED — needs @21st-dev API key |
| googlesheets | HTTP Composio | BLOCKED — needs valid Composio session |
| firestore-mcp | stdio Smithery | WARN — verify Firestore project access |

## Patterns

- **Secret management**: No secrets in source, git, or `mcp.json`. Secrets are injected at runtime (Bitwarden Secrets Manager via `bws run`).
- **MCP health**: After any `mcp.json` change, validate with `ConvertFrom-Json` before saving.
- **State tracking**: Every task block updates `docs/ai/STATE.md` with PASS/FAIL evidence.
- **Bootstrap routing**: `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` is the fastest cross-repo orientation doc; use it to route work before dropping into downstream code.
- **Serena**: Uses `--project-from-cwd`; must open the target project folder to activate.
- **Async ingestion**: `add-memory` may not be immediately searchable; retry `search-memory` after a short wait (2–4s).

## Memory Taxonomy (what we store)

We use a fixed set of `memory_types` values (in metadata):

- `component` — stable description of a module/service/tool and its I/O
- `implementation` — durable “how we did it” patterns (not ephemeral logs)
- `debug` — root cause + fix pattern for recurring issues
- `project_info` — governance facts, invariants, build determinism rules
- `user_preference` — durable preferences about workflow, style, risk tolerance

## Scoping Rules (prevent leakage)

Mem0’s filter guidance applies: memories are stored per entity scope; do not mix scopes incorrectly. In particular, if you later use Mem0 Platform filters, note that combining `user_id` and `agent_id` in a single `AND` commonly returns empty results; query one scope at a time or use `OR` (see `v2-memory-filters` docs).

For OpenMemory MCP (Cursor tool calls), we follow:

- **Project facts**: `project_id="<repo>"` only
- **Global preferences**: `user_preference=true` only
- **Project-specific preferences**: `user_preference=true` + `project_id="<repo>"`

## Key Decisions

- `Memory Tool` (Smithery mem0) removed in favour of `openmemory` (official hosted OpenMemory) — avoids two competing memory servers.
- `filesystem_scoped` covers Windows paths; WSL paths via shell-mcp bash shell.
- `shell-mcp` uses absolute `.exe` path to avoid `uv` shim resolution issues in Cursor.
