# Memory Contract

## Non-negotiable authority

Repo-tracked docs win. Always.

- `FINAL_OUTPUT_PRODUCT.md` is read first.
- The repo authority contract comes before operational evidence.
- OpenMemory is the primary durable structured recall layer, but it does not outrank repo docs.
- `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are operational evidence, not product or policy law.
- `docs/ai/context/` and `docs/ai/context/AGENT_EXECUTION_LEDGER.md` are non-canonical fallback surfaces only.

If memory conflicts with repo-tracked docs, the docs win and the memory must be corrected or superseded.

## Recovery order

Use this bootstrap order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, this file, `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`, and `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
3. Targeted OpenMemory retrieval
4. The recovery bundle in `docs/ai/recovery/` via `filesystem`, if present and current
5. `docs/ai/STATE.md` summary/current state section
6. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` if needed
7. `docs/ai/context/AGENT_EXECUTION_LEDGER.md` one block at a time only

Other `docs/ai/context/` artifacts and chat history are not part of the default recovery order. Use them only for targeted historical/audit follow-up after the selective deep read and ledger fallback are still insufficient.

## Live OpenMemory reality

The current Cursor MCP surface is thin:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Do not assume direct `project_id`, `namespace`, or `memory_types` filters unless a proven wrapper exposes them. Use compact self-identifying memory text instead.

Recommended prefix convention:

- `[repo=ai-pm][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
- `[repo=ai-pm][kind=pattern][stability=durable][source=docs/ai/memory/PATTERNS.md] ...`
- `[repo=tri-workspace][kind=policy][status=active][source=docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md] ...`

## What to store

Store only validated durable knowledge:

- key decisions and rationale
- reusable patterns
- stable debug findings
- workflow and recovery rules that matter across sessions
- short recovery pointers that reduce future rereads

## What must never be stored

- secrets, credentials, token IDs, or service-account JSON
- personal data
- raw transcripts, full ledger blocks, or broad copied docs
- speculative reasoning or unresolved guesses
- anything that pretends unsupported metadata exists

## Required behavior

### Before planning or execution

- Run targeted OpenMemory retrieval for the active task
- Use the recovery bundle only after authority docs and OpenMemory
- Read `STATE.md` as a summary layer, not as the first authority read

### After meaningful verified work

- Update canonical repo docs first
- Store durable conclusions in OpenMemory when the tool is healthy
- Write the recovery bundle via `filesystem` to:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- Record any memory reseed debt if OpenMemory was degraded

### If OpenMemory is degraded

- Announce the failure explicitly
- State the exact fallback path
- Record PASS/FAIL evidence in `docs/ai/STATE.md`
- Use repo docs plus the recovery bundle only if the task remains safely satisfiable

## Context-window hygiene

- Follow `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` guardrails.
- Prefer compact summaries and pointers over broad rereads.
- Keep memory entries atomic, retrieval-friendly, and non-duplicative.
