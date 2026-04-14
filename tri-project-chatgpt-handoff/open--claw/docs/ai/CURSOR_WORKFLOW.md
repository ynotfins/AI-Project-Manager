# Cursor Workflow Overview — Open Claw

This document is the human-readable guide to the Cursor workflow used in the Open Claw project.

## Authority Hierarchy

`open--claw` is the **strict enforcement center** of the tri-workspace. The product charter lives here.

| Priority | Document | Status |
| --- | --- | --- |
| 1 | `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` | **Supreme product charter** — no agent, rule, doc, or prompt in any repo overrides it |
| 2 | Tony's explicit permission to change that file | Only way to amend the charter |
| 3 | `AUTHORITATIVE_STANDARD.md` and `TEAM_ROSTER.md` | Subordinate translations of the charter |
| 4 | Repo-local rules and workflow docs (this file, `.cursor/rules/*`) | Valid only when they do not conflict with the above |
| 5 | `docs/ai/STATE.md`, `docs/ai/HANDOFF.md` | **Operational evidence only** — never product law |

**Workspace layer model:**

| Workspace | Role |
| --- | --- |
| `AI-Project-Manager` | Workflow and process layer — tab discipline, execution contracts, state tracking, tool policy, cross-repo orchestration. Does not issue product law. |
| `open--claw` | **Strict enforcement center** — product charter, AI employee knowledgebase, Sparky's mandate, quality standards |
| `droidrun` | Actuator layer — phone automation, MCP phone tools, Portal/APK runtime bridge |

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
- Prefer lowest-cost safe model; default non-thinking for straightforward execution.

## Where Rules Live

Authoritative (repo-tracked):

- `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — **supreme product charter**
- `.cursor/rules/00-global-core.md` — non-negotiable behaviors
- `.cursor/rules/01-charter-enforcement.md` — charter enforcement kernel
- `.cursor/rules/02-non-routable-exclusions.md` — quarantine and out-of-scope exclusions
- `.cursor/rules/05-global-mcp-usage.md` — MCP tool usage policy
- `.cursor/rules/10-project-workflow.md` — tab contracts (Open Claw specific)
- `.cursor/rules/15-model-routing.md` — model selection and escalation policy
- `.cursor/rules/20-project-quality.md` — engineering standards (Open Claw specific)
- `.cursor/rules/25-ai-employee-standard.mdc` — curated employee packet standard
- `AGENTS.md` — agent operating contract (repo root)

Developer-local (optional):

- Cursor User Rules for personal preferences (formatting, tone)
- Never put project invariants solely in user-local rules

## State and Planning

- `docs/ai/STATE.md` — **operational evidence log**; PLAN reads this to understand current state, blockers, and cross-repo effects. **This is evidence, not product law.**
- `docs/ai/HANDOFF.md` — concise operator snapshot; AGENT keeps this accurate after meaningful state changes. **Operational evidence only.**
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/ARCHIVE.md` — compressed decisions and knowledge from past sessions
- `docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md` — runtime mission, priorities, and anti-drift constraints
- `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` — context budget and file-size guardrails
- `AI-Project-Manager/docs/ai/operations/POLICY_DRIFT_CHECKER.md` — canonical parity checker for mirrored rules

## Excluded directories

- `docs/ai/context/` — non-canonical artifact storage: transcript-derived files, bulk session dumps, ephemeral context. Informative only; never authoritative.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` — **non-canonical** verbatim execution record: exact prompt + exact AGENT response + files changed + verdict, per completed prompt block. AGENT must append after every block. PLAN/DEBUG must NOT load by default — consult only when canonical sources are insufficient, and only the specific needed block(s) **one block at a time**. Archive to `docs/ai/context/archive/` when active ledger exceeds 5 entries or ~300 lines.
- `docs/ai/archive/` — superseded docs. **Never consulted** by PLAN. Historical reference only.
- `open-claw/AI_Employee_knowledgebase/AI_employees/_zips/` — portable packaging artifacts only. Do not use zip bundles as current operational truth when folder-based packets or repo docs exist.

## Context source priority

When PLAN or DEBUG needs to understand current state, consult sources in this order:

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
2. `docs/ai/STATE.md` — operational evidence
3. `docs/ai/memory/DECISIONS.md` — key decisions
4. `docs/ai/memory/PATTERNS.md` — reusable patterns
5. `docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md` — long-term goals and constraints
6. `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` — context budget guardrails
7. `docs/ai/context/` — session artifacts and dumps
8. `@Past Chats` — **last resort only**; use only if all above sources are insufficient

## Memory

- `docs/ai/memory/MEMORY_CONTRACT.md` — policy for what gets persisted
- `docs/ai/memory/DECISIONS.md` — log of key decisions with rationale
- `docs/ai/memory/PATTERNS.md` — reusable patterns discovered during development

Memory MCP tools supplement these docs for cross-session and cross-project recall. All stored memory is subordinate to the product charter.

## Open Claw Project Docs

- `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
- `open-claw/AI_Employee_knowledgebase/AUTHORITATIVE_STANDARD.md` — curated house standard
- `open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md` — AI employee team structure
- `open-claw/docs/VISION.md` — project vision and goals
- `open-claw/docs/REQUIREMENTS.md` — initial requirements
- `open-claw/docs/MODULES.md` — module boundaries
- `open-claw/docs/INTEGRATIONS.md` — target integrations
