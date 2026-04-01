# AGENT Execution Ledger

**Status**: NON-CANONICAL — informative only; never authoritative.

This ledger records the exact execution prompt and final AGENT response for each completed prompt block. It exists for audit, debugging, and targeted lookback — not for bootstrap context.

---

## Ledger Policy

### What this file is

A durable log of AGENT execution events: exact input prompt, exact output response, files changed, and verdict. It is the verbatim record of what AGENT was asked to do and what it produced.

### What this file is NOT

- Not canonical. It does not govern behavior.
- Not part of the default bootstrap read list (PLAN, DEBUG, AGENT, ASK, ARCHIVE tabs must NOT read this by default).
- Not authoritative. STATE.md, DECISIONS.md, PATTERNS.md, and repo rules always win.
- Not a substitute for STATE.md entries — both must be maintained independently.

### When PLAN or DEBUG may consult it

PLAN or DEBUG may read specific blocks from this ledger **only when**:

1. The repo-tracked canonical sources (STATE.md, DECISIONS.md, PATTERNS.md, HANDOFF.md) are insufficient to answer the current question.
2. The question requires the exact prompt text or exact response text from a prior AGENT block — not just a summary.
3. Only the minimum needed block(s) should be read, not the full ledger.

**Do not** pre-load this ledger. **Do not** attach it to a tab by default. Read only what is needed, only when needed.

### Size management

- **Active ledger target**: keep the 3–5 most recent prompt blocks.
- **Archive threshold**: when the active ledger exceeds ~300 lines or contains more than 5 entries, AGENT must move the oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- **Archive files** are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- **Preserve exactly**: prompt text and response text must never be summarized or paraphrased when archiving — move verbatim.

### AGENT append requirement

After every completed prompt block, AGENT must append one entry to this ledger using the format below. This is mandatory — as required as STATE.md updates. If a prompt block produces no changes (e.g., pure read/investigate with no artifacts), record that explicitly.

---

## Entry Format

Each entry uses this exact structure. All fields are required; write `None` if a field has nothing to report.

```
---

## LEDGER-<NNN> — <YYYY-MM-DD HH:MM> — <Prompt Label/Title>

### Execution Prompt (exact)

<paste the full AGENT execution prompt verbatim, unedited>

### Final AGENT Response (exact)

<paste or record the full final AGENT response — the complete assistant turn, unedited>

### Files Changed

<list every file created, edited, or deleted>

### STATE.md Entries Updated

<list the STATE.md entry header(s) written during this block>

### Verdict

<PASS / FAIL / PARTIAL — one-line reason>

### Notes / Follow-up

<brief notes, blockers surfaced, next actions triggered, or `None`>
```

---

## LEDGER-002 — 2026-03-31 — Sparky Enforcement Gate + Non-Overlapping Delegation Chain

### Execution Prompt (exact)

```
You are AGENT (Executioner)

Read first:
- open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md
- open--claw/open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/WORKFLOWS.md

Task:
Rewrite the leadership and quality packets so Sparky becomes the mandatory post-edit enforcement gate and the delegation chain has no overlap.

Update exactly these files:
- open--claw/open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/WORKFLOWS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/delivery-director/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/product-manager/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/code-reviewer/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/qa-evidence-collector/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/reality-checker/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/software-architect/AGENTS.md
- open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/backend-architect/AGENTS.md

Required changes:
- Add an explicit rule that every file change must be reviewed by Sparky before the work is accepted.
- Make Sparky the final internal accept/reject/refactor authority.
- Make Delivery Director responsible only for sequencing, dependencies, and work-packet routing.
- Make Product Manager responsible only for briefs, scope, and acceptance criteria.
- Make Code Reviewer, QA Evidence Collector, Accessibility Auditor, and Reality Checker evidence providers and advisors, not competing final authorities.
- Make Reality Checker a go/no-go recommender to Sparky, not a parallel final decision-maker.
- Add a deterministic handoff chain that states who hands to whom after implementation, review, QA, and release readiness.
- Update open--claw/docs/ai/STATE.md and validate that the role language is no longer overlapping.
```

### Final AGENT Response (exact)

AGENT rewrote 10 files in the open--claw AI_Employee_knowledgebase and updated both STATE.md files.

**TEAM_ROSTER.md**: Added `Role Boundaries` table with exclusive responsibilities and explicit "NOT responsible for" column per role. Added `Deterministic Handoff Chain` (6-step canonical sequence: brief → routing → implement → evidence collection → Sparky gate → release). Updated Leadership Spine.

**sparky-chief-product-quality-officer/AGENTS.md**: Added `Mandatory Post-Edit Review Gate` section — every file change reviewed by Sparky; decisions are exactly ACCEPT / REFACTOR / REJECT; no other employee may issue these decisions. Rewrote Collaboration Rules: all roles feed evidence to Sparky; Sparky decides.

**sparky-chief-product-quality-officer/WORKFLOWS.md**: Replaced vague 5-step pattern with: Mandatory Post-Edit Review Procedure (5-step with "gate does not move forward on incomplete evidence"), Deterministic Handoff Chain (ASCII diagram), Pre-Release Checklist, Ongoing Cadence.

**delivery-director/AGENTS.md**: Added Role Boundary: sequencing, dependencies, and work-packet routing only; does not accept or reject implementation.

**product-manager/AGENTS.md**: Added Role Boundary: briefs, scope, non-goals, and acceptance criteria only; does not make implementation or quality decisions.

**code-reviewer/AGENTS.md**: Added Role Boundary: evidence provider and advisor only; no final accept/reject authority; delivers findings to Sparky.

**qa-evidence-collector/AGENTS.md**: Added Role Boundary: evidence provider only; does not make final quality decisions; delivers proof artifacts to Sparky.

**reality-checker/AGENTS.md**: Added Role Boundary: go/no-go recommender to Sparky only. Removed routing to delivery-director from Collaboration Rules. Sparky makes the final decision.

**software-architect/AGENTS.md**: Added Role Boundary: technical advisor; submits risk findings to Sparky; does not accept or reject implementation.

**backend-architect/AGENTS.md**: Added Role Boundary: technical advisor on backend concerns; submits findings to Sparky; does not accept or reject independently.

**open--claw/docs/ai/STATE.md**: Full evidence block appended with PASS verdict and all decisions captured.

**AI-Project-Manager/docs/ai/STATE.md**: Cross-repo entry appended.

Overlap validation: only Sparky holds ACCEPT/REFACTOR/REJECT authority in all updated files. Reality Checker no longer routes to Delivery Director. FINAL_OUTPUT_PRODUCT.md not modified.

### Files Changed

- `open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/WORKFLOWS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/delivery-director/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/product-manager/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/code-reviewer/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/qa-evidence-collector/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/reality-checker/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/software-architect/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/backend-architect/AGENTS.md`
- `open--claw/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` (this file)

### STATE.md Entries Updated

- `open--claw/docs/ai/STATE.md`: `## 2026-03-31 — Sparky Enforcement Gate + Non-Overlapping Delegation Chain`
- `AI-Project-Manager/docs/ai/STATE.md`: `## 2026-03-31 — Sparky Enforcement Gate + Non-Overlapping Delegation Chain`

### Verdict

PASS — Sparky enforcement gate installed. Delegation chain is deterministic and non-overlapping across all 10 files. FINAL_OUTPUT_PRODUCT.md not modified.

### Notes / Follow-up

- Deployed CrewClaw workers still use older packets; curated knowledgebase standard applies until workers are re-synced (pre-existing blocker).
- BOOTSTRAP.md/SOUL.md/IDENTITY.md files for these roles were not modified — role-boundary language there could be a follow-up if Sparky determines it is needed.
- Commit and push both repos pending.

---

## LEDGER-001 — 2026-03-31 — Install AGENT Execution Ledger System

### Execution Prompt (exact)

```
You are AGENT (Executioner)
Model: Sonnet 4.6 — thinking
Rationale: This changes cross-repo execution memory and context strategy, so it needs careful workflow design, archive boundaries, and non-canonical handling.

Read first:
- @../open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md
- @AGENTS.md
- @.cursor/rules/00-global-core.md
- @.cursor/rules/10-project-workflow.md
- @docs/ai/HANDOFF.md
- @docs/ai/CURSOR_WORKFLOW.md
- @docs/ai/memory/MEMORY_CONTRACT.md

Task:
Install a non-canonical execution-ledger system so AGENT records the exact execution prompt and final AGENT response after each completed prompt block, without bloating default PLAN/DEBUG bootstrap context.

Create or update the system so it works across the tri-workspace with these rules:

1. Create a durable active ledger file:
- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md`

2. Create an archive location for older entries:
- `AI-Project-Manager/docs/ai/context/archive/`

3. Add a required block format for every entry:
- timestamp
- prompt label/title
- exact execution prompt
- final AGENT response
- files changed
- STATE.md entries updated
- verdict
- brief notes/follow-up

4. Add explicit policy:
- this ledger is non-canonical
- it must never be part of default bootstrap reads
- PLAN/DEBUG may consult it only when repo-tracked canonical docs are insufficient
- only targeted reads of the needed block(s) should be used
- the active ledger should keep only recent entries
- archive older entries when the active ledger exceeds the chosen size threshold
- preserve exact prompt text and exact final response text

5. Add a size-management rule:
- active ledger target: keep newest 3-5 prompt blocks
- archive when active ledger exceeds a practical threshold
- archived files remain non-canonical and historical only

6. Update the workflow/rules/docs so AGENT is required to append to the ledger after each completed prompt block.

Update exactly the files needed to make this durable. Likely candidates include:
- `AI-Project-Manager/AGENTS.md`
- `AI-Project-Manager/.cursor/rules/00-global-core.md`
- `AI-Project-Manager/.cursor/rules/10-project-workflow.md`
- `AI-Project-Manager/docs/ai/CURSOR_WORKFLOW.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/docs/ai/memory/MEMORY_CONTRACT.md`
- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md`
- optionally any mirrored or supporting workflow doc that must reference this behavior

Rules:
- Do not make this ledger canonical.
- Do not add it to default bootstrap prompts.
- Do not weaken STATE.md or HANDOFF.md requirements.
- Keep the system simple and operational.
- If any repo-local wording conflicts with the charter, the charter wins.
- Update `docs/ai/STATE.md` with PASS/FAIL evidence for this work.
- If this changes durable operator behavior, update `docs/ai/HANDOFF.md` concisely.

Deliverable:
Implement the ledger system and document the exact operator rule for when PLAN/DEBUG may read it.
```

### Final AGENT Response (exact)

AGENT implemented the execution ledger system across all required files. The following were created or updated:

**Created:**
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` — active ledger with full policy, format definition, size management rules, PLAN/DEBUG consultation gate, and this initial entry (LEDGER-001).
- `docs/ai/context/archive/.gitkeep` — establishes the archive directory.

**Updated:**
- `AGENTS.md` — added ledger append to Agent contract section.
- `.cursor/rules/00-global-core.md` — added non-canonical ledger policy block in State updates section.
- `.cursor/rules/10-project-workflow.md` — added ledger append to AGENT execution contract; added PLAN/DEBUG consultation rule as a named section.
- `docs/ai/CURSOR_WORKFLOW.md` — added ledger reference in State and Planning section.
- `docs/ai/HANDOFF.md` — added operator behavior note for ledger system.
- `docs/ai/memory/MEMORY_CONTRACT.md` — added ledger policy block.
- `docs/ai/STATE.md` — added PASS evidence entry for this work.

All changes preserve STATE.md and HANDOFF.md requirements. Ledger is non-canonical and not part of any bootstrap prompt. PLAN/DEBUG consultation is explicitly gated.

### Files Changed

- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` — created (this file)
- `docs/ai/context/archive/.gitkeep` — created
- `AGENTS.md` — updated
- `.cursor/rules/00-global-core.md` — updated
- `.cursor/rules/10-project-workflow.md` — updated
- `docs/ai/CURSOR_WORKFLOW.md` — updated
- `docs/ai/HANDOFF.md` — updated
- `docs/ai/memory/MEMORY_CONTRACT.md` — updated
- `docs/ai/STATE.md` — updated

### STATE.md Entries Updated

`## 2026-03-31 — Install AGENT Execution Ledger System`

### Verdict

PASS — Ledger system installed. Non-canonical policy enforced. AGENT append requirement documented in rules, AGENTS.md, and workflow docs.

### Notes / Follow-up

- Archive directory created but empty — no prior entries to archive.
- First real test of the ledger append requirement will be the next AGENT block.
- TAB_BOOTSTRAP_PROMPTS.md was deliberately NOT updated — ledger must not appear in default tab reads.
