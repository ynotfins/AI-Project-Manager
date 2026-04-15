# Autonomous PLAN System

This file describes the planning loop. It is a summary, not the owner of the bootstrap order.

## Canonical pointers

- `AGENTS.md` defines the repo authority contract.
- `.cursor/rules/10-project-workflow.md` defines the PLAN and AGENT execution contract.
- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` defines the only authoritative numbered no-loss bootstrap order.
- `docs/ai/operations/DOCUMENTATION_SYSTEM.md` defines doc-maintenance ownership and update order.

## PLAN objective

PLAN should produce the smallest safe next execution block while preserving:

- repo-truth-first behavior
- explicit model selection
- explicit tool requirements
- reversible, evidence-backed execution

## Control loop

1. Reconstruct context using the canonical no-loss order.
2. Use `thinking-patterns` for non-trivial planning before finalizing the next block.
3. Select the smallest deterministic AGENT step with clear exit criteria.
4. Emit exactly one AGENT prompt with model rationale and required tools.
5. Require AGENT to verify, record PASS/FAIL evidence, and update `docs/ai/STATE.md`.
6. Re-evaluate blockers and decide whether to continue, narrow scope, or return to PLAN.

## Planning discipline

- Prefer minimum-diff execution blocks over broad speculative cleanup.
- Do not let this file redefine source priority or tool inventory ownership.
- Treat `docs/ai/STATE.md` as operational evidence reached through the canonical recovery path, not as the first planning read by default.
- Stop and surface contradictions instead of silently smoothing them over.

## Escalation triggers

Return to a deeper planning pass when:

- required tools are degraded and fallback is risky
- live evidence contradicts repo governance
- the task expands outside the approved phase
- security or secret-handling posture would need to change
