# MCP Canonical Configuration

This document is the single owner of the live installed-tool matrix for the tri-workspace.

## Scope

- Owns the session-visible installed MCP server inventory.
- Owns the global configuration model (`C:/Users/ynotf/.cursor/mcp.json` is the single active config file).
- Does not own the numbered no-loss bootstrap order.
- Does not authorize secret-bearing config; repo docs must stay secret-free.

## Canonical owners

- `docs/tooling/MCP_CANONICAL_CONFIG.md` owns installed-tool inventory.
- `.cursor/rules/05-global-mcp-usage.md` owns tool triggers and degraded-tool policy.
- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` owns recovery order.

## Global config model

- The tri-workspace uses one machine-global MCP config: `C:/Users/ynotf/.cursor/mcp.json`.
- Workspace-local `.cursor/mcp.json` splits are not canonical in this setup.
- Enabled in config is not the same thing as default bootstrap context.
- Repo docs must describe the live session/tool surface, not stale aspirational servers.

## Live installed-tool matrix

Verified against the current session-visible MCP server list and local descriptor cache during the 2026-04-15 governance pass.

| Server | Role | Evidence in this phase |
| --- | --- | --- |
| `thinking-patterns` | structured reasoning | live tool call PASS |
| `openmemory` | durable recall/store | live tool call PASS |
| `Context7` | external library/framework docs | session-visible server |
| `filesystem` | local recovery-bundle and allowed file access | session-visible server |
| `serena` | exact-path code intelligence | session-visible server |
| `droidrun` | phone/device automation | session-visible server |
| `Exa Search` | web search / fetch | session-visible server |
| `playwright` | browser automation | session-visible server |
| `Magic MCP` | UI/design scaffolding | session-visible server |
| `Artiforge` | post-canonical synthesis/scaffold help | session-visible server |
| `obsidian-vault` | sidecar notes / operator research | session-visible server |

Current installed surface count: 11 servers.

## Active contract corrections

- Do not document `github`, `firecrawl-mcp`, or `context-matic` as installed unless they are re-proven in the active session surface and added back here.
- `thinking-patterns.sequential_thinking` is valid; the old standalone `sequential-thinking` server is not the canonical path.
- OpenMemory should be treated as a flat runtime for normal use:
  - `search-memories(query)`
  - `list-memories()`
  - `add-memory(content)`
- Do not rely on `project_id`, `namespace`, `user_preference`, or metadata-filter semantics unless the live runtime proves them.

## Fresh-chat bootstrap discipline

Installed does not mean preloaded. Default recovery/bootstrap still follows:

1. charter
2. repo authority contract
3. targeted OpenMemory
4. recovery bundle
5. `STATE.md` summary/current state
6. exactly one selective deep read if needed
7. execution ledger one block at a time only as a fallback

That numbered order is owned by `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`.

## Tooling hygiene

- Never commit secrets, tokens, or service-account material to repo docs.
- Do not paste stale `mcp.json` excerpts into governance docs when the live session surface has changed.
- If the live session, descriptor cache, and repo docs disagree, update this file and record the evidence in `docs/ai/STATE.md`.

## Re-validation rule

When a future task needs to claim a tool is installed or removed:

1. verify the live session-visible server surface
2. verify the relevant descriptor folder or tool schema
3. update this file first
4. let other docs point here instead of maintaining their own competing inventories
