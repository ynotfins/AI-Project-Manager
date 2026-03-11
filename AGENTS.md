# AGENTS.md

This repo uses a five-tab Cursor workflow: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

## Authoritative rules

- `.cursor/rules/00-global-core.md` — non-negotiable behaviors
- `.cursor/rules/05-global-mcp-usage.md` — MCP tool usage policy
- `.cursor/rules/10-project-workflow.md` — tab contracts and execution protocol
- `.cursor/rules/20-project-quality.md` — engineering standards
- `docs/ai/CURSOR_WORKFLOW.md` — human-readable workflow overview

## State tracking

- `docs/ai/STATE.md` — **primary operational log**; PLAN reads this first to understand current state, blockers, fallbacks, and cross-repo effects. AGENT updates it after every execution block using the enforced template in `10-project-workflow.md`.
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/context/` — non-canonical artifact storage: session transcripts, bulk dumps, and ephemeral context files. Informative only; never authoritative.
- `docs/ai/archive/` — superseded docs. **Never consulted** by PLAN. Historical reference only.

## Context source priority (read in this order)

PLAN must reconstruct current system state from repo-tracked sources before consulting artifacts or chat history. If repo sources and chat context disagree, repo sources win unless current execution evidence proves otherwise. Full rule: `10-project-workflow.md § PLAN source-of-truth priority`.

1. `docs/ai/STATE.md` — primary operational source of truth
2. `docs/ai/memory/DECISIONS.md` — key decisions with rationale
3. `docs/ai/memory/PATTERNS.md` — reusable patterns
4. `docs/ai/HANDOFF.md` — session handoff context
5. `docs/ai/context/` — transcript-derived artifacts and session dumps
6. Chat history / `@Past Chats` — **last resort only**; use only if the above sources are insufficient

## MCP policy

MCP tool usage is enforced via `.cursor/rules/05-global-mcp-usage.md`.
Tools are used for: code navigation, documentation lookup, reasoning, browser automation, web extraction, repo operations, and persistent memory.
Configuration lives outside the repo. Rules enforce behavior, not plumbing.

## Agent contract

AGENT must:
- Follow PLAN prompts exactly
- Update `docs/ai/STATE.md` after each execution block
- Provide PASS/FAIL evidence for every tool call and command
- Use MCP tools before falling back to manual approaches
