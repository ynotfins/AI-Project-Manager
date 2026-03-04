# AI Project Manager

Governance hub for all Cursor-managed projects under `D:\github` and `D:\github_2`.

This repo does **not** contain application code. It holds:
- Cursor workflow rules and agent contracts
- Execution state and planning docs
- MCP server configuration references
- Tooling health logs and memory policies

## Managed Projects

| Project | Repo | Branch | Status |
|---|---|---|---|
| open--claw | [ynotfins/open--claw](https://github.com/ynotfins/open--claw) | `master` | Phase 6 (build completion) — see `docs/ai/PLAN.md` |

**open--claw** is an [OpenClaw](https://openclaw.ai/) personal AI assistant being set up for full autonomous operation across two machines:
- **ChaosCentral** (primary): i9-14900KF, 128GB DDR5, RTX 4070 Super
- **Laptop** (warm-standby): Samsung Galaxy Book4 Pro 360, Ultra 7 155H, 16GB

## Five-Tab Workflow

Every Cursor project uses exactly five chat tabs:

| Tab | Role | Edits files? |
|---|---|---|
| PLAN | Architect / Strategist | No |
| AGENT | Executor / Implementer | Yes |
| DEBUG | Investigator / Forensics | No |
| ASK | Scratchpad / Exploration | No |
| ARCHIVE | Compressor / Handoff | Docs only |

See `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` for the first prompt to paste into each tab.

## Quick Start (new session)

1. Open this folder in Cursor.
2. Create five chat tabs: PLAN / AGENT / DEBUG / ASK / ARCHIVE.
3. Paste bootstrap prompts from `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`.
4. PLAN produces the next phase; AGENT executes it.

## Rules Structure

- **Global rules** (`00-*`, `05-*`): Broad, reusable across projects.
- **Project rules** (`10-*`, `20-*`): Project-specific, reference global rules.

All rules live in `.cursor/rules/`. See `AGENTS.md` for the authoritative entry point.

## State and Planning

- `docs/ai/STATE.md` — execution log (AGENT updates after every block)
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/ARCHIVE.md` — compressed decisions from past sessions

## Memory

See `docs/ai/memory/MEMORY_CONTRACT.md` for the persistence policy.
OpenMemory MCP tools supplement repo docs for cross-session recall — see `openmemory.md`.

## MCP and Secrets

- `docs/tooling/MCP_CANONICAL_CONFIG.md` — reference config for all MCP servers
- Secrets are managed via Bitwarden Secrets Manager (`bws run`) — never stored in git
