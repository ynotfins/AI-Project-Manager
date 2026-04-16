# AGENTS.md

This repo uses a five-tab Cursor workflow: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

## Authority Hierarchy (read this first)

The tri-workspace authority order is:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product authority
2. Tony's explicit permission to change `FINAL_OUTPUT_PRODUCT.md`
3. `AUTHORITATIVE_STANDARD.md` and `TEAM_ROSTER.md` in the knowledgebase — subordinate translations of the charter
4. Repo-tracked workflow and governance docs — valid only when they do not conflict with the above
5. `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` — operational evidence only, never product law

Machine-global overlays may inform behavior, but they never outrank the charter or repo-tracked governance in this repo.

**Layer roles:**

- `AI-Project-Manager` — workflow and process layer: tab contracts, execution discipline, state tracking, tool policy, and cross-repo orchestration
- `open--claw` — strict enforcement center: product charter, AI employee knowledgebase, quality standards, and Sparky's mandate
- `droidrun` — actuator layer: phone automation, MCP phone tools, and Android/Portal runtime bridge

## Repo Authority Contract

For workflow and memory recovery, read this repo contract before operational evidence:

- `.cursor/rules/00-global-core.md`
- `.cursor/rules/01-charter-enforcement.md`
- `.cursor/rules/02-non-routable-exclusions.md`
- `.cursor/rules/05-global-mcp-usage.md`
- `.cursor/rules/10-project-workflow.md`
- `.cursor/rules/20-project-quality.md`
- `.cursor/rules/openmemory.mdc`
- `docs/ai/memory/MEMORY_CONTRACT.md`
- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`
- `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`

These repo-tracked files define live workflow policy. Historical snapshots such as `docs/global-rules.md` are informative only.

## Canonical Owners

Secondary docs in this repo must point back to these owners instead of restating competing versions:

- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` owns the numbered no-loss bootstrap order
- `docs/tooling/MCP_CANONICAL_CONFIG.md` owns the live installed-tool matrix
- `.cursor/rules/05-global-mcp-usage.md` owns tool triggers and degraded-tool behavior
- `docs/ai/memory/MEMORY_CONTRACT.md` owns the flat-runtime OpenMemory storage/retrieval contract

## State Tracking

- `docs/ai/STATE.md` — operational evidence log, not product law; use the summary/current state section first during recovery, then deeper blocks only as needed
- `docs/ai/HANDOFF.md` — concise unresolved operator snapshot and current cross-session turbulence
- `docs/ai/recovery/` — non-canonical recovery bundle written for crash recovery via `filesystem`:
  - `current-state.json`
  - `session-summary.md`
  - `active-blockers.json`
  - `memory-delta.json`
- `docs/ai/PLAN.md` — active plan with phases and exit criteria
- `docs/ai/context/` — non-canonical artifact storage: session transcripts, bulk dumps, and ephemeral context files
- `docs/ai/archive/` — superseded docs; never part of active bootstrap

## Context Source Priority (read in this order)

PLAN and DEBUG must reconstruct state from the smallest authoritative slice that answers the task. If repo sources and chat context disagree, repo sources win unless current execution evidence proves otherwise.

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. The repo authority contract listed above
3. Targeted `openmemory` retrieval relevant to the active repo/task
4. The recovery bundle files in `docs/ai/recovery/`, if present and current
5. `docs/ai/STATE.md` summary/current state section
6. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` if needed
7. `docs/ai/context/AGENT_EXECUTION_LEDGER.md` only as a one-block-at-a-time fallback

Do not preload the execution ledger by default.

Other `docs/ai/context/` artifacts and chat history are not part of the default recovery path. Use them only for targeted historical/audit follow-up after the selective deep read and ledger fallback are still insufficient.

## MCP Policy

MCP tool usage is enforced via `.cursor/rules/05-global-mcp-usage.md`.
Tools are used for code navigation, documentation lookup, reasoning, repo operations, persistent memory, filesystem recovery reads, and optional sidecar knowledge.
Configuration lives outside the repo. Rules enforce behavior, not plumbing.

### Serena Project Map

When Serena is needed, activate it by exact path for the codebase actually in scope:

- `D:/github/AI-Project-Manager`
- `D:/github/open--claw/open-claw`
- `D:/github/droidrun`

Do not rely on dashboard names when switching projects. `D:/github/open--claw` repo root is docs/governance heavy and is not the default Serena code project. If the task is docs-only or the current root has no valid Serena project, record Serena as not applicable and use targeted search/read tools instead.

## Agent Contract

AGENT must:

- Follow PLAN prompts exactly
- Update `docs/ai/STATE.md` after each execution block
- Update `docs/ai/HANDOFF.md` when unresolved turbulence or project-state changes remain relevant
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block
- Provide PASS/FAIL evidence for every tool call and command
- Use MCP tools before falling back to manual approaches
- After every meaningful execution, write the recovery bundle via `filesystem` to:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- After every meaningful execution, write at least one compact durable OpenMemory update via `openmemory`
- Record degraded-tool incidents honestly, including fallback path and any memory reseed debt

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` records verbatim AGENT execution events. It is non-canonical and must never be part of default bootstrap reads for any tab. PLAN and DEBUG may consult it only when `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, and `HANDOFF.md` are insufficient, and only by reading the specific needed block(s).

**Ledger rotation is hook-configured** (`.cursor/hooks.json` → `.cursor/hooks/rotate_ledger.py`). Repo-local rotation logic is proven when the script is run directly, but live Cursor `afterFileEdit` execution remains unproven. After every AI edit to the ledger file, the intended rotation behavior is:

- Checks if entry count > 5 or file > ~300 lines
- Moves the oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`
- Keeps the 3–5 most recent entries in the active ledger
- Does not rotate below 3 active entries

AGENT must still append the new entry manually. Until live hook firing is re-proven, if a ledger append leaves the file above the compaction threshold, run `python .cursor/hooks/rotate_ledger.py --force` as the current canonical fallback. This is a Cursor-hook proof gap, not a repo-memory architecture gap. PLAN and DEBUG must not preload the ledger; they may consult only the minimum needed block(s), one block at a time.
