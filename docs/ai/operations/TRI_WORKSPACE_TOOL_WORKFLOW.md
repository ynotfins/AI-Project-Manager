# Tri-Workspace Tool Workflow

This document explains how tools are routed across the tri-workspace. It is not the owner of the installed-tool matrix and it does not own the numbered recovery order.

## Canonical owners

- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` owns the only authoritative numbered no-loss bootstrap order.
- `docs/tooling/MCP_CANONICAL_CONFIG.md` owns the live installed-tool matrix and global MCP configuration model.
- `.cursor/rules/05-global-mcp-usage.md` owns mandatory triggers, degraded-tool policy, and fallback rules.

## Repo responsibilities

| Repo | Role | Tooling implication |
| --- | --- | --- |
| `AI-Project-Manager` | workflow/process layer | owns cross-repo tool policy, installed-tool inventory, and recovery discipline |
| `open--claw` | enforcement/runtime layer | may add repo-local constraints, but must not redefine installed-tool ownership or the shared bootstrap order |
| `droidrun` | actuator layer | may add device/runtime specifics, but must mirror the shared workflow contract |

## Routing model

### `thinking-patterns`

Primary reasoning tool for non-trivial planning, debugging, critique, and cross-repo reasoning.

### `openmemory`

Primary durable recall layer after charter and repo authority reads.

Live usage assumptions:

- use flat queries such as `search-memories(query)`
- store compact self-identifying summaries
- do not assume hidden filters or metadata semantics

### `filesystem`

Used for the recovery bundle and other explicitly allowed local-file operations. The bundle remains generated and non-canonical.

### `serena`

Required for code/symbol intelligence and exact-path project work. Optional for docs-only governance passes.

### `Context7`

External docs only. Never project truth.

### `obsidian-vault`

Sidecar-only and never part of default bootstrap.

### `droidrun`

Device interaction only.

### `Exa Search`, `playwright`, `Magic MCP`, `Artiforge`

Task-specific tools. Use only when the actual task requires web research, browser verification, UI scaffolding, or post-canonical synthesis.

## Configuration model

- Active MCP configuration lives in the single global file `C:/Users/ynotf/.cursor/mcp.json`.
- Workspace docs must describe the session-visible installed surface, not stale aspirational servers.
- Repo-local docs must not claim a tool is installed unless `docs/tooling/MCP_CANONICAL_CONFIG.md` says so.

## Missing-tool behavior

If a required tool is unavailable:

1. Announce FAIL immediately.
2. Name the exact tool and failed step.
3. State the safe fallback if one exists.
4. Record the evidence gap or reseed debt in `docs/ai/STATE.md`.
5. Stop instead of silently degrading when no safe fallback exists.
