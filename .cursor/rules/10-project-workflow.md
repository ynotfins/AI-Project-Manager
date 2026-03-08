# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)

## PLAN output contract

PLAN must produce:
- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- If the phase has >5 connected steps, use a reasoning MCP tool before finalizing

## AGENT execution contract

AGENT must:
- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run tests and commands required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- After meaningful verified work, commit focused changes and push the current repo to origin unless explicitly blocked, unsafe, or awaiting approval. In a shared multi-root workspace, apply this per repo. If commit or push is skipped, record why in docs/ai/STATE.md.

## DEBUG output contract

DEBUG must produce:
- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
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

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
