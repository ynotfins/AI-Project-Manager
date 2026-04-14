# Recovery Session Summary

Phase 1 no-loss governance normalization is complete for the active AI-PM rule stack.

obsidian_sync: pending
obsidian_target: `AI-PM/Recovery Sidecar/No-Loss Recovery Catch-Up.md`

What changed:
- Normalized the default recovery path to: charter -> repo authority -> targeted OpenMemory -> filesystem recovery bundle -> `STATE.md` summary/current state -> exactly one selective deep read (`DECISIONS.md`, `PATTERNS.md`, or `HANDOFF.md`) -> ledger one-block fallback only.
- Rewrote `.cursor/rules/openmemory.mdc` to match the verified flat runtime only: `search-memories(query)`, `list-memories()`, `add-memory(content)`.
- Updated `docs/ai/operations/TRI_WORKSPACE_TOOL_WORKFLOW.md` so the tool inventory and role boundaries match the 9 installed MCP descriptors.
- Made Obsidian explicitly sidecar-only and non-blocking in the active repo docs, then narrowed the conflicting machine-global Obsidian/governance overlays so they cannot silently outrank repo policy.

Fresh recovery expectation:
Read the charter, repo authority contract, targeted OpenMemory result, and the four files in `docs/ai/recovery/` before touching `STATE.md`. Use the ledger only if the bundle plus one selective deep read are still insufficient.

Phase 2 still needed:
- Sweep broader untouched docs for stale tool inventory or older no-loss wording.
- Decide whether any stale older OpenMemory bootstrap entries should be superseded again.

## Pending Obsidian Sidecar Summary

This is a non-canonical fallback payload to flush into Obsidian once `obsidian-vault` is available again.

- Phase 1 governance normalization now makes the flat OpenMemory surface, the lean bootstrap order, and sidecar-only Obsidian behavior explicit across the active AI-PM rule stack.
- Machine-global Obsidian and governance overlays were narrowed so they cannot silently broaden bootstrap or outrank repo-tracked AI-PM policy.
- Remaining drift is intentionally deferred to Phase 2: broader stale docs, historical logs, and any supersession of older low-relevance OpenMemory bootstrap memories.

Flush rule:
- On next successful `obsidian-vault` availability, copy this sidecar summary into Obsidian and clear `obsidian_sync: pending`.
