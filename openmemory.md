# OpenMemory Guide — AI-Project-Manager

**project_id:** `ynotfins/AI-Project-Manager`
**client:** cursor
**server:** openmemory (hosted at api.openmemory.dev)

## Overview

AI-Project-Manager is a Cursor workspace that serves as the control plane for the OpenClaw mobile project and related tooling. It contains:
- MCP server configuration (global `~/.cursor/mcp.json`)
- Cursor workflow rules (`.cursor/rules/`)
- AI state and planning docs (`docs/ai/`)
- Tooling health logs (`docs/tooling/`)

The repo is a documentation and configuration hub, not an application codebase. Primary language artifacts are markdown docs and JSON configs.

## Architecture

```
AI-Project-Manager/
├── .cursor/rules/          # Cursor agent behavior rules (always-apply)
├── docs/
│   ├── ai/                 # STATE.md, PLAN.md, CURSOR_WORKFLOW.md, tabs/
│   └── tooling/            # MCP_HEALTH.md, MCP_CANONICAL_CONFIG.md
├── AGENTS.md               # Authoritative rule entrypoint
└── openmemory.md           # This file
```

## User Defined Namespaces

- `AI-Project-Manager` — project facts, implementations, configs
- `global` — user preferences applicable across all projects

## Components

| Component | Location | Purpose |
|---|---|---|
| Global MCP Config | `~/.cursor/mcp.json` | Defines all 14 MCP servers for Cursor globally |
| Cursor Rules | `.cursor/rules/` | Always-apply agent behavior rules |
| STATE.md | `docs/ai/STATE.md` | Execution log updated after every task block |
| PLAN.md | `docs/ai/PLAN.md` | Active plan with phases and exit criteria |
| MCP_HEALTH.md | `docs/tooling/MCP_HEALTH.md` | MCP server health history and fixes |
| MCP_CANONICAL_CONFIG.md | `docs/tooling/MCP_CANONICAL_CONFIG.md` | Reference MCP config for reproducing setup |

## Active MCP Servers (14 total)

| Server | Type | Status |
|---|---|---|
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

- **Secret management**: No secrets in source or git. `functions/.env.local` is truth; `bws run` injection planned for github/firecrawl/magic.
- **MCP health**: After any mcp.json edit, validate with `ConvertFrom-Json` before saving.
- **State tracking**: Every task block updates `docs/ai/STATE.md` with PASS/FAIL evidence.
- **Serena**: Uses `--project-from-cwd`; must open the target project folder to activate.

## Key Decisions

- `Memory Tool` (Smithery mem0) removed in favour of `openmemory` (official hosted OpenMemory) — avoids two competing memory servers.
- `filesystem_scoped` covers Windows paths; WSL paths via shell-mcp bash shell.
- `shell-mcp` uses absolute `.exe` path to avoid `uv` shim resolution issues in Cursor.
