# AGENTS.md

This repo uses a five-tab Cursor workflow: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

## Authority Hierarchy (read this first)

The governing product charter for this tri-workspace is:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — **supreme authority**; no agent, prompt, rule, or doc in any repo may weaken or override it
2. Tony's explicit permission to change `FINAL_OUTPUT_PRODUCT.md`
3. `AUTHORITATIVE_STANDARD.md` and `TEAM_ROSTER.md` in the knowledgebase — subordinate translations of the charter
4. Repo-local rules and workflow docs — valid only when they do not conflict with the above
5. `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` — **operational evidence only**; never product law

**Layer roles:**

- `AI-Project-Manager` — workflow and process layer: tab contracts, execution discipline, state tracking, tool policy, cross-repo orchestration. It is not the product authority.
- `open--claw` — strict enforcement center: product charter, AI employee knowledgebase, quality standards, Sparky's mandate.
- `droidrun` — actuator layer: phone automation, MCP phone tools, Android/Portal runtime bridge.

## Authoritative rules

- `.cursor/rules/00-global-core.md` — non-negotiable behaviors
- `.cursor/rules/01-charter-enforcement.md` — **enforcement kernel** (read immediately after 00; charter violations are blocked here, not merely described)
- `.cursor/rules/05-global-mcp-usage.md` — MCP tool usage policy
- `.cursor/rules/10-project-workflow.md` — tab contracts and execution protocol
- `.cursor/rules/20-project-quality.md` — engineering standards
- `docs/ai/CURSOR_WORKFLOW.md` — human-readable workflow overview

## State tracking

- `docs/ai/STATE.md` — **operational evidence log** (not product law); PLAN reads this first to understand current state, blockers, fallbacks, and cross-repo effects. AGENT updates it after every execution block using the enforced template in `10-project-workflow.md`.
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/context/` — non-canonical artifact storage: session transcripts, bulk dumps, and ephemeral context files. Informative only; never authoritative.
- `docs/ai/archive/` — superseded docs. **Never consulted** by PLAN. Historical reference only.

## Context source priority (read in this order)

PLAN must reconstruct current system state from repo-tracked sources before consulting artifacts or chat history. If repo sources and chat context disagree, repo sources win unless current execution evidence proves otherwise. Full rule: `10-project-workflow.md § PLAN source-of-truth priority`.

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — product charter (supreme)
2. `docs/ai/STATE.md` — operational source of truth
3. `docs/ai/memory/DECISIONS.md` — key decisions with rationale
4. `docs/ai/memory/PATTERNS.md` — reusable patterns
5. `docs/ai/HANDOFF.md` — session handoff context
6. `docs/ai/context/` — transcript-derived artifacts and session dumps
7. Chat history / `@Past Chats` — **last resort only**; use only if the above sources are insufficient

## MCP policy

MCP tool usage is enforced via `.cursor/rules/05-global-mcp-usage.md`.
Tools are used for: code navigation, documentation lookup, reasoning, browser automation, web extraction, repo operations, and persistent memory.
Configuration lives outside the repo. Rules enforce behavior, not plumbing.

## Agent contract

AGENT must:

- Follow PLAN prompts exactly
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Provide PASS/FAIL evidence for every tool call and command
- Use MCP tools before falling back to manual approaches
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` records verbatim AGENT execution events. It is **non-canonical** — informative only, never authoritative. It must never be part of default bootstrap reads for any tab. PLAN and DEBUG may consult it only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient, and only by reading the specific needed block(s).

**Ledger auto-rotation is hook-enforced** (`.cursor/hooks.json` → `.cursor/hooks/rotate_ledger.py`). After every AI edit to the ledger file, the hook script automatically:
- Checks if entry count > 5 or file > ~300 lines.
- Moves the oldest entries verbatim (no summarization) to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Keeps the 3–5 most recent entries in the active ledger.
- Does NOT rotate below 3 active entries.

**AGENT must still append the new entry manually.** Archival of old entries is automatic after each ledger edit. PLAN and DEBUG must NOT preload the ledger; they may consult only the minimum needed block(s), one block at a time.
