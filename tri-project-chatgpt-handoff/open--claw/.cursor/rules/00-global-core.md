---
description: "Global core non-negotiables"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

`open--claw` is the **strict enforcement center** of the tri-workspace. The supreme governing document for this entire project is `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No rule, prompt, plan, workflow doc, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It does not issue product law.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Read **one block at a time**; stop as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
