# No-Loss Recovery Loop

This document is the canonical operating guide for context recovery after restart, crash, or power loss.

## Purpose

Recover the smallest trustworthy context slice possible without broad rereads or silent tool fallbacks.

## Hard invariants

- Preserve the five-tab workflow exactly: PLAN / AGENT / DEBUG / ASK / ARCHIVE
- Read `FINAL_OUTPUT_PRODUCT.md` first
- Read repo authority docs before operational evidence
- Use OpenMemory as the primary durable structured recall layer
- Keep the recovery bundle non-canonical
- Keep Obsidian sidecar-only
- Keep Artiforge non-authoritative
- Do not preload `docs/ai/context/AGENT_EXECUTION_LEDGER.md`

## Bootstrap order

Use this order unless a stricter repo rule applies:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. Repo authority contract:
   - `AGENTS.md`
   - `.cursor/rules/01-charter-enforcement.md`
   - `.cursor/rules/05-global-mcp-usage.md`
   - `.cursor/rules/10-project-workflow.md`
   - `docs/ai/memory/MEMORY_CONTRACT.md`
   - `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
3. Targeted OpenMemory search
4. Recovery bundle via `filesystem`, if present and current:
   - `docs/ai/recovery/current-state.json`
   - `docs/ai/recovery/session-summary.md`
   - `docs/ai/recovery/active-blockers.json`
   - `docs/ai/recovery/memory-delta.json`
5. `docs/ai/STATE.md` summary/current state section
6. Exactly one of:
   - `docs/ai/memory/DECISIONS.md`
   - `docs/ai/memory/PATTERNS.md`
   - `docs/ai/HANDOFF.md`
7. `docs/ai/context/AGENT_EXECUTION_LEDGER.md` one block at a time only if required

`docs/ai/context/` artifacts and chat history are excluded from the default bootstrap path. Use them only for targeted historical follow-up after the selective deep read and ledger fallback still do not answer the task.

## By tab

### PLAN

- No edits
- No commands
- Use `thinking-patterns` for non-trivial planning
- Keep recovery reads minimal and deliberate

### AGENT

- Execute the PLAN prompt exactly
- Update `STATE.md`, `HANDOFF.md`, and the execution ledger honestly
- After every meaningful execution, write all four recovery bundle files via `filesystem`
- Store durable conclusions in OpenMemory when healthy

### DEBUG

- Use `thinking-patterns.debugging_approach`
- Read recovery bundle before broad evidence files
- Use the ledger only when exact prior prompt/response text matters

### ASK

- Explore without creating binding workflow changes
- Use OpenMemory and repo docs before chat history

### ARCHIVE

- Promote durable knowledge into canonical docs and OpenMemory
- Refresh the recovery bundle after promotion work

## Tool triggers

### OpenMemory

Use before non-trivial recovery work and after validated durable changes.

Current live surface:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Because the surface is flat, stored text must self-identify repo, kind, stability, and source.

### filesystem

Use for recovery bundle reads/writes at:

- `docs/ai/recovery/current-state.json`
- `docs/ai/recovery/session-summary.md`
- `docs/ai/recovery/active-blockers.json`
- `docs/ai/recovery/memory-delta.json`

### obsidian-vault

Use only when known operator notes or research are relevant.

It is a sidecar-only tool, not a default recovery source and not a replacement for repo-tracked state or memory docs.

If `obsidian-vault` is unavailable during sidecar sync:

- do not retry aggressively
- do not block execution
- place the pending sidecar summary in `docs/ai/recovery/session-summary.md`
- mark `obsidian_sync: pending`
- flush the pending summary into Obsidian on the next successful availability

### Artiforge

Use only after canonical inputs are read, and only for synthesis/scaffold help.

### thinking-patterns

Required for non-trivial plan, architecture, critique, and debug work.

### serena

Optional for docs-only governance passes.
Required when code/symbol understanding is needed.

## Degraded-tool behavior

If a required recovery step is degraded:

1. Announce FAIL immediately
2. Name the exact tool and failed step
3. State the fallback
4. State what confidence/evidence was lost
5. Record the incident in `STATE.md`

If OpenMemory retrieval or storage was skipped, add a reseed note so future sessions know durable memory must be repaired.

`obsidian-vault` sidecar sync is a special non-canonical case: on failure, keep execution moving and store the pending sidecar payload in `docs/ai/recovery/session-summary.md` instead of blocking the task.

## Durable memory text convention

Use compact self-identifying text such as:

- `[repo=ai-pm][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
- `[repo=ai-pm][kind=policy][status=active][source=docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md] ...`
- `[repo=openclaw][kind=pattern][scope=worker-memory][source=MEMORY_PROMOTION_TEMPLATE.md] ...`

Do not claim unsupported metadata fields as if they are enforced by the runtime.

## Recovery simulation

If the system restarts:

1. Search OpenMemory for the active repo/task
2. Read only the four files in `docs/ai/recovery/` via `filesystem`
3. Use those results to recover phase, goal, last action, active blockers, and last decisions/patterns
4. Only then read `STATE.md` summary or one deeper doc if the bundle plus OpenMemory are insufficient
