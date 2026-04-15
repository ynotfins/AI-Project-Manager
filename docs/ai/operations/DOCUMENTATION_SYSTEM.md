# Documentation System

This document defines the minimum documentation structure all agents must keep accurate.

The goal is complete operational traceability without uncontrolled doc sprawl.

## Canonical Layers

| Layer | Path | Purpose | Update trigger |
|---|---|---|---|
| Product law | `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` | Supreme product authority | Tony only |
| Governance architecture | `docs/ai/architecture/*` | System design, authority, autonomy, no-loss memory | When structure changes |
| Recovery order | `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` | Single authoritative numbered no-loss recovery order | When recovery flow changes |
| Operations runbooks | `docs/ai/operations/*` | How to run, launch, verify, bootstrap, audit | When workflow changes |
| Recovery bundle | `docs/ai/recovery/*` | Generated non-canonical speed layer for restart recovery | After meaningful verified work or when recovery state changes |
| Active operational truth | `docs/ai/STATE.md` | Current execution evidence and latest outcomes | After every meaningful change |
| Session handoff | `docs/ai/HANDOFF.md` | Optional operator snapshot for unresolved runtime state | Only when the next session would otherwise miss critical operator context |
| Durable memory summaries | `docs/ai/memory/*` | Decisions, patterns, memory contract | When a durable fact is learned |
| Tooling truth | `docs/tooling/*` | MCP config, health, tool usage, infrastructure | When tool behavior changes |
| Non-canonical context | `docs/ai/context/*` | Ledgers, extracts, temporary artifacts | Informational only |

## Required Update Order

After any meaningful code, config, workflow, or tooling change:

1. Update the changed canonical doc for the affected area.
2. Append a full execution block to `docs/ai/STATE.md`.
3. Update `docs/ai/HANDOFF.md` only if the next session would otherwise miss critical unresolved operator/runtime context.
4. Promote durable facts into `docs/ai/memory/DECISIONS.md` or `PATTERNS.md`.
5. If tooling changed, update `docs/tooling/PRIORITY_TOOL_USAGE.md` and relevant tooling docs.

## Anti-Sprawl Rules

- Do not create a new doc if an existing canonical doc already owns the topic.
- Do not store the same fact in multiple canonical docs unless one is a short pointer.
- Keep the full numbered no-loss recovery order only in `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`; every other active doc should point there instead of duplicating the chain.
- Use `docs/ai/context/*` for verbose artifacts, transcripts, or temporary exports.
- Use OpenMemory for durable retrieval support, not as a replacement for canonical repo docs.
- Keep `docs/ai/HANDOFF.md` optional and non-blocking for recovery.
- Keep `docs/ai/recovery/*` generated and non-canonical.

## Ownership Model

| Owner | Responsibility |
|---|---|
| AI-PM | Governance docs, workflow docs, tooling docs, memory discipline |
| Sparky | Delivery evidence, implementation docs, employee-facing execution artifacts |
| ARCHIVE | Archive passes, compaction, promotion of durable facts |

## File Creation Test

Before creating a new markdown file, ask:

1. Is this product law?
2. Is this architecture?
3. Is this an operations runbook?
4. Is this durable memory?
5. Is this tooling state?
6. Is this only context or evidence?

If none fit clearly, do not create the file yet.
