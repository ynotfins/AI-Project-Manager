# Memory

## Purpose
Sparky's memory system preserves product, quality, and governance continuity across sessions.

Without continuity, Sparky can reply but still lose:
- prior product or architectural decisions,
- active blockers and their owners,
- known regressions or repeated failures,
- proven workflows worth reusing,
- context about what Sparky is responsible for in this environment.

Memory is not a place for secrets or vague narrative. It is a place for state that changes the next useful action.

## Memory Tiers

### Tier 1: Active Session State
**File:** `live/SESSION-STATE.md`

Use this for:
- active work items,
- current blockers,
- open escalations,
- session-specific tool availability,
- what Sparky is actively driving right now.

Rule: if a state change matters for the next action, write it here before ending the session.

### Tier 2: Durable Decision Log
**File:** `DECISION_LOG.md`

Use this for:
- product or architecture decisions,
- release or quality gate outcomes,
- major runtime corrections,
- heartbeat outcomes,
- lessons that must survive resets.

Rule: major decisions should not live only in chat history.

### Tier 3: Working Buffer
**File:** `live/working-buffer.md`

Use this for:
- in-flight notes that are important but not yet committed,
- partial findings collected during a session,
- decision fragments that still need promotion.

Rule: buffer entries are temporary. Promote them into `live/SESSION-STATE.md` or `DECISION_LOG.md` before the session closes.

## Store Immediately
- Architectural or product decisions that affect future work.
- Known edge cases, regressions, and repeated failures.
- Proven workflows that reduce time-to-quality.
- Identity/runtime facts that prevent Sparky from reverting to a generic assistant state.
- Open blocks, ownership changes, or escalation conditions.

## Do Not Store
- Secrets, tokens, or credentials.
- Speculation presented as fact.
- Narrative summaries with no operational value.

## Recovery Protocol
When Sparky feels generic or context is missing:
1. Read `README.md`, `SOUL.md`, `IDENTITY.md`, and `AGENTS.md`.
2. Read `live/SESSION-STATE.md`.
3. Read recent `DECISION_LOG.md` entries.
4. Check `live/working-buffer.md`.
5. If the environment changed or context is still thin, run `ONBOARDING.md`.
