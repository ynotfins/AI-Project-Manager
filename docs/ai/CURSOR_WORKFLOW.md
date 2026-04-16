# Cursor Workflow Overview

This file is a human-readable map of the tri-workspace workflow. It is intentionally pointer-heavy so it cannot override the canonical contracts.

## Authority Summary

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` is the supreme product charter.
2. `AI-Project-Manager` owns workflow, recovery order, and tool-policy governance.
3. `open--claw` owns product enforcement and runtime behavior.
4. `droidrun` owns actuator behavior and phone automation.
5. `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are operational evidence only.

## Five-Tab Model

| Tab | Role | Edits files? | Runs commands? |
| --- | --- | --- | --- |
| PLAN | Architect / Strategist | No | No |
| AGENT | Executor / Implementer | Yes | Yes |
| DEBUG | Investigator / Forensics | No | No |
| ASK | Scratchpad / Exploration | No | No |
| ARCHIVE | Compressor / Handoff | Docs only | No |

See `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` for tab-start prompts.

## Canonical Owners

- `AGENTS.md` owns the repo authority contract and agent obligations.
- `.cursor/rules/10-project-workflow.md` owns PLAN / AGENT / DEBUG execution rules.
- `.cursor/rules/05-global-mcp-usage.md` owns tool triggers, degraded-tool handling, and fallback policy.
- `.cursor/rules/openmemory.mdc` owns the live OpenMemory usage contract for the flat runtime.
- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` owns the only authoritative numbered no-loss bootstrap order.
- `docs/ai/operations/DOCUMENTATION_SYSTEM.md` owns documentation-layer responsibilities and update order.
- `docs/tooling/MCP_CANONICAL_CONFIG.md` owns the installed-tool matrix for the live tri-workspace session surface.

## Recovery Guidance

- Do not invent a local bootstrap order from this overview.
- Follow `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` when reconstructing context.
- Do not duplicate the installed-tool inventory here; use `docs/tooling/MCP_CANONICAL_CONFIG.md`.
- Treat `docs/ai/context/` and the execution ledger as non-canonical last-resort evidence only.
- Treat `docs/ai/STATE.md` as operational evidence reached after authority, targeted OpenMemory, and the recovery bundle.

Default bootstrap excludes `docs/ai/context/**`, archived docs, Obsidian sidecar notes, Artiforge briefs, and full-ledger reads unless the canonical recovery path still leaves a targeted question unanswered.

## Tooling Guidance

- Use the active tool inventory from `docs/tooling/MCP_CANONICAL_CONFIG.md`.
- Use `Context7` for external docs, not project truth.
- Use `serena` only when code/symbol intelligence is actually needed.
- Keep `obsidian-vault` sidecar-only and non-blocking.

## Serena Project Map

When Serena is needed, activate it by exact path:

- `D:/github/AI-Project-Manager`
- `D:/github/open--claw/open-claw`
- `D:/github/droidrun`

For docs-only governance work, Serena may be not applicable.
