# Autonomous PLAN System

This document defines how PLAN operates with high autonomy while preserving safety, context fidelity, and long-term project awareness.

## Objective

Enable PLAN and AGENT to work in a Devin-like autonomous loop while remaining evidence-first, repo-truth-first, and reversible.

## Hard invariants

- Repository docs are the source of truth.
- `docs/ai/STATE.md` is always read before planning.
- No secrets in docs, code, logs, or commits.
- PLAN does not execute or edit; AGENT executes and records evidence.
- Every meaningful change updates `docs/ai/STATE.md`.

## Autonomous control loop

1. Reconstruct context from canonical docs.
2. Select smallest safe execution block with clear exit criteria.
3. Generate one deterministic AGENT prompt.
4. Execute, verify, and collect PASS/FAIL evidence.
5. Update `STATE.md`, `DECISIONS.md`, and `PATTERNS.md` as needed.
6. Re-evaluate blockers and next best block.

## Canonical context stack

PLAN and AGENT should read in this order:

1. `docs/ai/STATE.md`
2. `docs/ai/PLAN.md`
3. `docs/ai/memory/DECISIONS.md`
4. `docs/ai/memory/PATTERNS.md`
5. `docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md`
6. `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`
7. `docs/ai/context/` and archive docs (historical only)

## Decision discipline

- Prefer incremental changes over broad refactors.
- Require evidence for each claimed success.
- Stop and surface ambiguity instead of silently proceeding.
- Explicitly document fallbacks when preferred tools are unavailable.

## Context-loss prevention model

- Keep canonical docs concise and current.
- Move superseded details to archive files.
- Maintain a short, high-signal handoff.
- Track context-size health using the monitoring policy in `CONTEXT_WINDOW_MONITORING.md`.

## Escalation rules

Escalate back to PLAN when:

- Required tools are unavailable and fallback is risky.
- Evidence contradicts assumptions.
- A change crosses repo boundaries unexpectedly.
- Security, credentials, or deployment posture changes.
