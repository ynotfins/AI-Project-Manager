# OpenMemory Guide — AI-Project-Manager

## Overview

AI-Project-Manager is the tri-workspace workflow and governance hub.

OpenMemory is used here as the primary durable structured recall layer, but canonical truth still lives in repo-tracked docs.

## Live Cursor surface

The current live Cursor-side tool surface is:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

This guide intentionally does **not** assume rich metadata filters such as `project_id`, `namespace`, or `memory_types` are available through the current Cursor runtime.

## What this repo stores in OpenMemory

Only validated durable knowledge:

- workflow and governance decisions
- no-loss recovery rules
- reusable process patterns
- stable debug findings about the tooling stack

Do not store:

- secrets
- raw transcripts
- broad copies of repo docs
- speculative notes

## Text convention

Because the current surface is flat, each durable memory entry must self-identify in plain text.

Recommended forms:

- `[repo=ai-pm][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
- `[repo=ai-pm][kind=pattern][stability=durable][source=docs/ai/memory/PATTERNS.md] ...`
- `[repo=tri-workspace][kind=policy][status=active][source=docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md] ...`

Keep entries short and retrieval-friendly.

## Retrieval policy

For this repo:

1. Read `FINAL_OUTPUT_PRODUCT.md`
2. Read the repo authority contract
3. Search OpenMemory with a targeted task query
4. Use the recovery bundle only after those steps
5. Then read `STATE.md` summary/current state and one optional deeper doc

Use OpenMemory to reduce rereads, not to replace canonical docs.

## Recovery relationship

OpenMemory works alongside other no-loss layers:

- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` — recovery order and tool triggers
- `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md` — machine-local non-canonical recovery bundle
- `docs/ai/memory/MEMORY_CONTRACT.md` — storage discipline and conflict rules
- `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` — operational evidence
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` — forensic fallback only

## Runtime notes

- Treat the currently exposed tool surface as the source of truth for capabilities.
- If `add-memory` succeeds but later retrieval cannot find the result, treat OpenMemory as degraded and record reseed debt.
- If OpenMemory is unavailable for a required recovery step, fail loudly and use the documented repo fallback path only if the task remains safely satisfiable.

## Local patterns

- Keep `openmemory.md` aligned with the live runtime, not with aspirational mem0-style schemas.
- Update canonical repo docs before storing durable memory.
- Refresh the recovery bundle after meaningful verified work so future recovery can stay compact.
