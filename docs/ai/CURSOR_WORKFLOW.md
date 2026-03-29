# Cursor Workflow Overview

This document is the human-readable guide to the Cursor workflow used in this project.

## Five-Tab Model

We use exactly five Cursor chat tabs, each with a distinct role:

| Tab     | Role                     | Edits files? | Runs commands? |
| ------- | ------------------------ | ------------ | -------------- |
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

See `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` for the first prompt to paste into each tab.

PLAN output requirement:

- Every PLAN response must end with exactly one copy-pastable AGENT execution prompt.
- The AGENT prompt must start with:
  - `You are AGENT (Executioner)`
  - `Model: <model> — <thinking|non-thinking>`
  - `Rationale: <one-line reason for this model and mode>`
- Model selection is explicit and intentional — PLAN must not silently default to any option. Allowed choices: Composer2, Sonnet 4.6, Opus 4.6 — always with `thinking` or `non-thinking` specified. See `10-project-workflow.md § PLAN output contract` for the full selection matrix.

## Where Rules Live

Authoritative (repo-tracked):

- `.cursor/rules/00-global-core.md` — non-negotiable behaviors
- `.cursor/rules/05-global-mcp-usage.md` — MCP tool usage policy
- `.cursor/rules/10-project-workflow.md` — tab contracts and execution protocol
- `.cursor/rules/20-project-quality.md` — engineering standards
- `AGENTS.md` — agent operating contract (repo root)

Developer-local (optional):

- Cursor User Rules for personal preferences (formatting, tone)
- Never put project invariants solely in user-local rules

## State and Planning

- `docs/ai/STATE.md` — **primary operational source of truth**; PLAN reads this first before reasoning about blockers, next actions, and cross-repo effects. Every AGENT block must append an entry using the enforced template in `.cursor/rules/10-project-workflow.md`.
- `docs/ai/HANDOFF.md` — concise operator snapshot; AGENT keeps this accurate after meaningful state changes
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/ARCHIVE.md` — compressed decisions and knowledge from past sessions
- `docs/ai/operations/AUTONOMOUS_PLAN_SYSTEM.md` — autonomous control loop and escalation policy
- `docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md` — long-term project intent and anti-drift constraints
- `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` — context budget and file-size guardrails
- `docs/ai/operations/POLICY_DRIFT_CHECKER.md` — canonical-vs-mirror rule parity audit runbook
- `docs/ai/context/` — non-canonical artifact storage: transcript-derived files, bulk session dumps, ephemeral context. Informative only; never authoritative.
- `docs/ai/archive/` — superseded docs. **Never consulted** by PLAN. Historical reference only.

## Context source priority

When PLAN or DEBUG needs to understand current state, consult sources in this order:

1. `docs/ai/STATE.md` — primary operational source of truth
2. `docs/ai/memory/DECISIONS.md` — key decisions with rationale
3. `docs/ai/memory/PATTERNS.md` — reusable patterns
4. `docs/ai/HANDOFF.md` — session handoff context
5. `docs/ai/context/` — transcript-derived artifacts and session dumps
6. Chat history / `@Past Chats` — **last resort only**; use only if the above sources are insufficient

Supporting planning references (consult as needed; not part of the authoritative priority order):

- `docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md` — long-term goals and anti-drift constraints
- `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` — context budget and file-size guardrails

## Memory

- `docs/ai/memory/MEMORY_CONTRACT.md` — policy for what gets persisted
- `docs/ai/memory/DECISIONS.md` — log of key decisions with rationale
- `docs/ai/memory/PATTERNS.md` — reusable patterns discovered during development

Memory MCP tools supplement these docs for cross-session and cross-project recall.
