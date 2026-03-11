# Cursor Workflow Overview

This document is the human-readable guide to the Cursor workflow used in this project.

## Five-Tab Model

We use exactly five Cursor chat tabs, each with a distinct role:

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

See `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` for the first prompt to paste into each tab.

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
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/ARCHIVE.md` — compressed decisions and knowledge from past sessions
- `docs/ai/context/` — non-canonical artifact storage: transcript-derived files, bulk session dumps, ephemeral context. Informative only; never authoritative.
- `docs/ai/archive/` — superseded docs. **Never consulted** by PLAN. Historical reference only.

## Context source priority

When PLAN or DEBUG needs to understand current state, consult sources in this order:

1. `docs/ai/STATE.md` — primary
2. `docs/ai/memory/DECISIONS.md` — key decisions
3. `docs/ai/memory/PATTERNS.md` — reusable patterns
4. `docs/ai/context/` — session artifacts and dumps
5. `@Past Chats` — **last resort only**; use only if all above sources are insufficient

## Memory

- `docs/ai/memory/MEMORY_CONTRACT.md` — policy for what gets persisted
- `docs/ai/memory/DECISIONS.md` — log of key decisions with rationale
- `docs/ai/memory/PATTERNS.md` — reusable patterns discovered during development

Memory MCP tools supplement these docs for cross-session and cross-project recall.
