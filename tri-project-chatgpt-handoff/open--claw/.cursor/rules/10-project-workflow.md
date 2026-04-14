---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** for the open--claw repo. Routine delivery work does not require user approval — Sparky is the internal approval authority. Tony approval is required only for Tony-gate actions defined in `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md`.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Choose lowest-cost model that safely fits task complexity; default non-thinking for straightforward execution
  - PLAN may escalate to a stronger model internally without waiting for user confirmation — see `15-model-routing.md`
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified.
- Refresh the non-canonical recovery bundle after meaningful verified work, or record why it was deferred
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict — route to Sparky for internal resolution, not to the user
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the phase instructions explicitly require it or the user requests it. If commit or push is skipped, record why in `docs/ai/STATE.md`.
- May escalate to a stronger model or route a problem to Sparky without waiting for user confirmation — see `15-model-routing.md`

## Sparky review — mandatory on every file change

After any employee makes a file change, Sparky must review the changed files and determine:

- Whether the change followed best practices
- Whether architectural integrity was preserved
- Whether the change moves the project closer to the finished product in `FINAL_OUTPUT_PRODUCT.md`
- Whether refactoring is required before the work is accepted

Sparky's review does not require user involvement. It is an internal quality gate.

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory first for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. If present and current, read the machine-local recovery bundle before broad repo logs
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and recovery bundle, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/memory/MEMORY_CONTRACT.md`
3. `docs/ai/STATE.md` summary/current state section
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md`
5. `docs/ai/context/`
6. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The recovery bundle is a non-canonical filesystem speed layer.

- Use it after the authority contract and OpenMemory, not before them.
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If it is stale or missing, record that and continue with canonical sources.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
