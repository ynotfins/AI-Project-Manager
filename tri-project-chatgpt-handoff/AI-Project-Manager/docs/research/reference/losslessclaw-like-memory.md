# LosslessClaw-Like Memory Reference

Imported from: `C:\Users\ynotf\OneDrive\Desktop\Temp\losslesclaw-like-memory.md`

Status: non-canonical research reference

## Key Ideas Captured

- Store the raw log, not only summaries.
- Maintain an index/retrieval layer so past details can be found without loading the entire history.
- Use a compression layer that periodically summarizes chunks while keeping the raw source available for drill-down.
- Keep long-horizon storage separate from active-context assembly.

## Relevance To This Repo

- Confirms the current No-Loss direction: raw evidence in repo docs and ledgers, durable recall in OpenMemory, and a compact active-context slice assembled at task time.
- Reinforces the rule that default preload should be small and drill-down should be selective.

## How It Was Applied

- PLAN recovery was tightened toward `OpenMemory -> STATE.md -> on-demand docs`.
- Execution ledger remains gated fallback only.
- Archive/history surfaces remain non-canonical.
