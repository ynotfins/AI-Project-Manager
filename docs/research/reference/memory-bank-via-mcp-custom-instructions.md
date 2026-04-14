# Memory Bank Via MCP Reference

Imported from: `C:\Users\ynotf\OneDrive\Desktop\Temp\custom-inatructions.md`

Status: non-canonical research reference

## What This Captures

- A memory-bank workflow built around mandatory pre-flight reads, project memory files, and routine updates.
- A structured file hierarchy for project brief, product context, system patterns, active context, and progress.
- A strong bias toward reading the entire memory bank before acting.

## Keep vs Reject

Keep:

- explicit lifecycle thinking
- separation between foundation docs, active context, and progress tracking
- treating memory upkeep as part of execution quality

Reject:

- mandatory full rereads before every task
- large static memory-bank preload as the primary recovery mechanism
- any pattern that would bloat PLAN's default context

## Adapted Rule In This System

We keep the lifecycle discipline, but replace full memory-bank rereads with:

1. OpenMemory retrieval
2. `STATE.md`
3. on-demand `DECISIONS.md`, `PATTERNS.md`, `HANDOFF.md`
4. gated ledger or archive access only if needed
