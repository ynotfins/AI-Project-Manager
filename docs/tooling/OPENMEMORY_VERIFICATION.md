# OpenMemory Verification

Goal: prove the live Cursor OpenMemory surface that the governance docs are allowed to claim, without relying on stale proxy-era transport assumptions.

## Proven Runtime Contract

The current documented contract is only:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Do not treat `project_id`, `namespace`, `user_preference`, `memory_types`, proxy health endpoints, or UI-only tool lists as part of the canonical proof unless the active runtime re-proves them.

## Deterministic Verification Path

### 1. Descriptor proof

Read the live tool descriptors from `user-openmemory/tools/` and confirm the current session exposes:

- `search-memories`
- `list-memories`
- `add-memory`

PASS:

- The descriptor cache contains exactly the flat tools above for the current proof scope.

### 2. Retrieval proof

Run a targeted `search-memories(query)` call for the active recovery/governance topic.

PASS:

- The search returns relevant compact memories that match current repo policy closely enough to aid recovery.

### 3. Storage proof

After durable verified work, write one compact self-identifying memory with `add-memory(content)`.

Recommended format:

```text
[repo=ai-pm][kind=policy][status=active][source=docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md + docs/tooling/MCP_CANONICAL_CONFIG.md] <durable conclusion>
```

PASS:

- `add-memory(content)` succeeds without inventing unsupported metadata fields.

### 4. Recovery pairing proof

Refresh the AI-PM recovery bundle and confirm the same pass produced:

- one OpenMemory write
- one recovery-bundle refresh
- one `STATE.md` evidence block

PASS:

- OpenMemory and the recovery bundle now describe the same current phase/goal/blocker reality.

## Not Canonical By Default

These checks may still be useful operationally, but they are not the canonical proof path for this repo:

- direct `mcp.json` transport details
- local proxy health endpoints
- green/red Cursor UI indicators
- historical tool names such as `search-memory`
- rich-schema examples using `project_id` or `namespace`

## Failure Behavior

If OpenMemory retrieval or storage fails during a task that requires it:

1. Announce FAIL immediately.
2. Name the exact failed step.
3. Fall back to repo docs plus the AI-PM recovery bundle only if the task is still safe.
4. Record the evidence gap and memory reseed debt in `docs/ai/STATE.md`.

