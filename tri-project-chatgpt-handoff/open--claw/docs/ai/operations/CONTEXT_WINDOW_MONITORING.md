# Context Window Monitoring — Open Claw

Canonical governance policy lives in:

- `AI-Project-Manager/docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`

This local file defines runtime-repo expectations.

## Purpose

Prevent state/log files from consuming PLAN or AGENT context budget before useful execution starts.

## Local guardrails

- `docs/ai/STATE.md`
  - target: <= 160 KB
  - archive advised: > 180 KB
- `docs/ai/HANDOFF.md`
  - target: <= 16 KB
- `docs/ai/PLAN.md`
  - target: <= 36 KB

## Required behavior

- Before large updates to state docs, check size and estimate token load.
- If `STATE.md` is too large, archive completed historical blocks and keep active summary + recent operational entries.
- Mirror major archive actions in `AI-Project-Manager/docs/ai/STATE.md`.
