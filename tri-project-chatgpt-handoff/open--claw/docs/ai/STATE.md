# Execution State — Open Claw
<!-- markdownlint-disable MD024 MD040 MD046 MD052 MD037 MD034 -->

`docs/ai/STATE.md` is the **operational evidence log** for PLAN in the open--claw repo.
PLAN reads this before reasoning about blockers, fallbacks, next actions, and cross-repo effects.

> **Authority note**: This file is operational evidence only. It is not product law. The supreme governing charter is `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — it lives in this repo and governs the entire tri-workspace. If this file conflicts with the charter, the charter wins unconditionally.

---

## Current State Summary

> Last updated: 2026-04-09
> Archive pass: 2026-04-01 — 1,170 → 175 lines (archive/compaction pass, this session)
> Previous archive: `docs/ai/archive/state-log-full-history-2026-02-18-to-2026-03-21.md`

### Authority Reality

- **Supreme charter**: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — immutable without Tony's permission
- **Enforcement kernel**: `.cursor/rules/01-charter-enforcement.md` — active, hard-stop on charter violations
- **Forbidden platforms**: macOS, iOS, Swift, Xcode, CocoaPods — violations stop execution immediately and route to Sparky
- **Sparky** (`sparky-chief-product-quality-officer`) is the exclusive ACCEPT/REFACTOR/REJECT authority for all file changes and release decisions
- **Quarantine system**: installed at 5 enforcement layers; `candidate_employees/**` (163 files) is permanently non-routable until promoted via `NON_ROUTABLE_QUARANTINE.md`

### Active Prompt Sequence Status

| Prompt | Description | Status |
|---|---|---|
| Prompt 7 | Tri-Workspace Governance Normalization | COMPLETE |
| Prompt 8 | Non-Routable Quarantine System | COMPLETE |
| Archive pass | STATE.md compaction (this task) | COMPLETE |
| Prompt 6 (next) | TBD — see PLAN | READY TO PROCEED |

### Phase Status

| Phase | Status | Closed |
|---|---|---|
| Phase 1 — Gateway Boot + First Agent Chat | COMPLETE | 2026-03-08 |
| Phase 2 — First Live Integration | COMPLETE | 2026-03-14 |
| Phase 1A — CrewClaw Worker Stabilization | COMPLETE (runtime fixes applied) | 2026-03-29 |
| Phase 1B — Employee Readiness Audit + Standard | COMPLETE | 2026-03-30 |
| Phase 1C — Curated Runtime Sync + Validation | COMPLETE | 2026-03-30 |
| Phase 1D — Docs Cross-Reference Alignment | COMPLETE | 2026-03-30 |
| Phase 1E — FINAL_OUTPUT_PRODUCT Charter | COMPLETE | 2026-03-30 |
| Phase 1F — Telegram Bot Assignment Mapping | COMPLETE | 2026-03-30 |
| Phase 1G — Employee Status Board | COMPLETE | 2026-03-30 |
| Autonomy Model Rewrite | COMPLETE | 2026-03-31 |
| Sparky Enforcement Gate + Delegation Chain | COMPLETE | 2026-03-31 |
| Charter Enforcement Kernel Install | COMPLETE | 2026-03-31 |
| Governance Normalization (Prompt 7) | COMPLETE | 2026-03-31 |
| Non-Routable Quarantine (Prompt 8) | COMPLETE | 2026-04-01 |
| **Memory Bridge (OpenClaw ↔ OpenMemory)** | **NOT STARTED** | — |

### Runtime Snapshot (as of 2026-03-29; last verified)

- OpenClaw runtime: v2026.3.13 via `~/openclaw-build` (CLI `pnpm openclaw` + systemd)
- Gateway: `0.0.0.0:18789` (bind=lan), API health `127.0.0.1:18792`
- Telegram: healthy, running, `@SECRETARY_STACY_BOT`, polling mode (renamed from `@Sparky4bot`)
- WhatsApp: linked/stopped — **401 Unauthorized** — needs QR re-scan
- Windows node: Windows Desktop — connected (verified 2026-03-29)
- Curated runtime: generated and structurally validated at `open-claw/employees/deployed-curated/`; NOT yet live-started with real tokens

### Active Blockers

| Blocker | Severity | Status |
|---|---|---|
| WhatsApp 401 — session expired | MEDIUM | PENDING USER ACTION: `pnpm openclaw channels login --channel whatsapp` + QR scan |
| 3 curated worker Bitwarden UUIDs unresolved | MEDIUM | `delivery-director`, `product-manager`, `sparky-chief-product-quality-officer` — need explicit `*_TOKEN` env vars or new Bitwarden secret IDs |
| 2 curated worker Telegram usernames still unrecorded | LOW | `accessibility-auditor`, `backend-architect` — tokens exist; final usernames still need to be recorded cleanly in docs |
| Curated runtime not live-proven | HIGH | Run `open-claw/employees/deployed-curated/start-employees.ps1`, approve device pairings, run smoke tests |
| Memory bridge not built | HIGH | Phase 1B design (deferred) — OpenClaw ↔ OpenMemory bridge not yet built |
| `docs/ai/context/AGENT_EXECUTION_LEDGER.md` does not exist | LOW | Create when first open--claw AGENT block appends a ledger entry |

### Cross-Repo Dependencies Still Active

- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` — ledger updated with archive pass entry (this task)
- `droidrun`: `02-non-routable-exclusions.md` mirrors the open--claw quarantine rule; iOS files bannered as non-routable
- `AI-Project-Manager`: `02-non-routable-exclusions.md` mirrors; `openmemory.mdc` updated; `TRI_WORKSPACE_CONTEXT_BRIEF.md` updated

### What Remains Unverified

- PowerShell bulk banner count (2,608) not independently spot-checked post-run
- `openmemory.mdc` exclusions require a live memory search test to confirm `candidate_employees/**` paths are excluded
- TAB_BOOTSTRAP_PROMPTS.md quarantine blocks not tested in a live Cursor session
- Sparky routing plumbing requires live multi-agent session validation
- Governance overlay (Phase 6B) still blocked on ANTHROPIC_API_KEY

### Archived Entries

Historical log (2026-02-18 through 2026-03-21):
`docs/ai/archive/state-log-full-history-2026-02-18-to-2026-03-21.md`

Phase 1A through Governance Normalization (2026-03-21 through 2026-03-31):
`docs/ai/archive/state-log-phase1a-governance-normalization-2026-03-21-to-2026-03-31.md`

---

## State Log

<!-- AGENT appends entries below this line after each execution block. -->

---

## 2026-04-01 — STATE.md Archive/Compaction Pass (Archive Prompt)

### Goal

Perform a dedicated archive/compaction pass for `open--claw/docs/ai/STATE.md` to bring it back into policy compliance, preserve all operationally relevant context, and promote decisions/patterns that existed only in STATE entries to the durable docs before archiving.

### Scope

- `open--claw/docs/ai/STATE.md` (this file) — primary target
- `open--claw/docs/ai/archive/state-log-phase1a-governance-normalization-2026-03-21-to-2026-03-31.md` — new archive file created
- `open--claw/docs/ai/memory/DECISIONS.md` — populated (was empty)
- `open--claw/docs/ai/memory/PATTERNS.md` — populated (was empty)
- `open--claw/docs/ai/HANDOFF.md` — updated to reflect Prompt 8 completion and archive pass
- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` — archive pass entry appended

### Commands / Tool Calls

- Read: `open--claw/docs/ai/STATE.md` (1,170 lines) — PASS
- Read: `open--claw/docs/ai/HANDOFF.md` — PASS
- Read: `open--claw/docs/ai/memory/DECISIONS.md` (empty) — PASS
- Read: `open--claw/docs/ai/memory/PATTERNS.md` (empty) — PASS
- Read: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — PASS
- Read: `open--claw/AGENTS.md`, all `.cursor/rules/*.md`, `AI-Project-Manager/AGENTS.md`, `AI-Project-Manager/.cursor/rules/10-project-workflow.md` — PASS
- Read: `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` — PASS
- Write: `docs/ai/memory/DECISIONS.md` — promoted 10 key decisions — PASS
- Write: `docs/ai/memory/PATTERNS.md` — promoted 4 key patterns — PASS
- Write: `docs/ai/archive/state-log-phase1a-governance-normalization-2026-03-21-to-2026-03-31.md` — verbatim move of 16 historical STATE entries — PASS
- Write: `docs/ai/STATE.md` — compacted from 1,170 → ~175 lines — PASS
- Write: `docs/ai/HANDOFF.md` — updated phase status and added archive pass note — PASS
- Write: `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` — archive pass entry appended — PASS

### Changes

- **DECISIONS.md**: Populated from empty — 10 decisions promoted (worker agent identity, Docker volume pattern, OpenClaw install recipe, Sparky authority, handoff chain, reality checker role, forbidden platforms, KB archive policy, quarantine model, quarantine source of truth)
- **PATTERNS.md**: Populated from empty — 4 patterns promoted (OpenClaw Docker worker install, named Docker volume for device identity, curated employee packet structure, quarantine banner)
- **Archive file created**: `docs/ai/archive/state-log-phase1a-governance-normalization-2026-03-21-to-2026-03-31.md` — 16 historical STATE entries moved verbatim (2026-03-21 through 2026-03-31)
- **STATE.md**: Compacted from 1,170 lines → ~175 lines. New Current State Summary written at top. Prompt 8 entry (2026-04-01 quarantine) kept active. Old 2026-03-29 Current State Summary archived (outdated). Archive pass entry (this entry) appended.
- **HANDOFF.md**: Updated date to 2026-04-01, updated phase status table, added Prompt 8 quarantine and archive pass as completed items, blockers unchanged.

### Evidence

- PASS: `DECISIONS.md` populated — 10 durable decisions from archived STATE entries captured before archiving
- PASS: `PATTERNS.md` populated — 4 reusable patterns captured before archiving
- PASS: Archive file created with all 16 historical entries verbatim (no summarization)
- PASS: Active STATE.md reduced from 1,170 lines to ~175 lines — well below 800-line soft warning
- PASS: `FINAL_OUTPUT_PRODUCT.md` not modified
- PASS: No decisions/patterns lost — cross-checked DECISIONS.md, PATTERNS.md, HANDOFF.md before archiving
- PASS: Current State Summary is sufficient for PLAN to regain situational awareness
- PASS: Archive policy followed exactly (verbatim move, no summarization, archive file in `docs/ai/archive/`)

### Verdict

READY — STATE.md is now policy-compliant at ~175 lines (well below the 800-line soft warning zone and 1,000-line hard ceiling). Archive file created verbatim. DECISIONS.md and PATTERNS.md populated. Current State Summary captures authority reality, phase status, active blockers, unverified items, and cross-repo dependencies. Repo is clean to proceed to Prompt 6.

### Blockers

None for the archive pass itself. Active project blockers are captured in the Current State Summary above.

### Fallbacks Used

None.

### Cross-Repo Impact

- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` — archive pass entry appended (required by AGENT contract)
- `open--claw/docs/ai/HANDOFF.md` — updated to reflect post-Prompt 8 and archive pass state

### Decisions Captured

None new. All promoted decisions were extracted from existing STATE entries and moved to `DECISIONS.md`.

### Pending Actions

- HANDOFF.md: updated in this pass — reflects current truth.
- DECISIONS.md: populated — no further action needed.
- PATTERNS.md: populated — no further action needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` for open--claw still does not exist — create when first open--claw AGENT block runs a real execution task.

### What Remains Unverified

Same as Current State Summary above — the unverified items that were in STATE before the archive pass remain unverified (live quarantine exclusion test, live tab bootstrap test, Sparky routing, ANTHROPIC_API_KEY for governance overlay).

### What's Next

Proceed to Prompt 6. All governance and compaction prerequisites are now satisfied.

---

## 2026-04-01 — Non-Routable Quarantine System Installed (Prompt 8)

### Goal

Implement a path-based quarantine system that prevents out-of-scope material from entering routing, search, memory, or embeddings flows across the entire tri-workspace. This entry records the full open--claw-specific and cross-repo changes.

### Scope

- `open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` — canonical registry (new)
- `open--claw/.cursor/rules/02-non-routable-exclusions.md` — enforcement rule (new)
- `AI-Project-Manager/.cursor/rules/02-non-routable-exclusions.md` — mirror enforcement rule (new)
- `droidrun/.cursor/rules/02-non-routable-exclusions.md` — mirror enforcement rule (new)
- `open-claw/AI_Employee_knowledgebase/README.md` — quarantine notice added
- `open-claw/AI_Employee_knowledgebase/SOURCE_LIBRARY_CATALOG.md` — quarantine status table added
- `open-claw/AI_Employee_knowledgebase/EMPLOYEE_READINESS_AUDIT.md` — quarantine notice added
- `AI-Project-Manager/.cursor/rules/openmemory.mdc` — memory exclusions added
- `droidrun/.cursor/rules/openmemory.mdc` — memory exclusions added
- `AI-Project-Manager/docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` — quarantine table added
- `open--claw/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` — quarantine block added to PLAN and AGENT tabs
- `droidrun/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` — quarantine block added to PLAN and AGENT tabs
- All 2,608 files in `candidate_employees/**` — `<!-- NON-ROUTABLE — OUT OF SCOPE -->` banner prepended
- `droidrun/src/droidrun/tools/driver/ios.py` — `# NON-ROUTABLE — OUT OF SCOPE` banner prepended
- `droidrun/src/droidrun/tools/ui/ios_provider.py` — `# NON-ROUTABLE — OUT OF SCOPE` banner prepended
- `droidrun/src/droidrun/tools/ios/__init__.py` — `# NON-ROUTABLE — OUT OF SCOPE` banner prepended

### Commands / Tool Calls

- PowerShell: bulk prepend `<!-- NON-ROUTABLE — OUT OF SCOPE -->` to 2,608 candidate_employees files — PASS
- StrReplace: bannered 3 droidrun iOS files with `# NON-ROUTABLE — OUT OF SCOPE` — PASS
- Write: Created `NON_ROUTABLE_QUARANTINE.md` with canonical registry, exclusion definitions, promotion gate, and audit trail — PASS
- Write: Created 3 x `02-non-routable-exclusions.md` rule files (alwaysApply: true; search, memory, embeddings, routing exclusions) — PASS
- StrReplace: Updated `README.md`, `SOURCE_LIBRARY_CATALOG.md`, `EMPLOYEE_READINESS_AUDIT.md` — PASS
- StrReplace: Updated `openmemory.mdc` in AI-Project-Manager and droidrun — PASS
- StrReplace: Updated `TRI_WORKSPACE_CONTEXT_BRIEF.md` with quarantine table — PASS
- StrReplace: Updated both `TAB_BOOTSTRAP_PROMPTS.md` files with quarantine blocks in PLAN and AGENT tabs — PASS
- Write: Updated `STATE.md` in all 3 repos — PASS

### Changes

- Created `NON_ROUTABLE_QUARANTINE.md`: canonical quarantine registry with exclusion path list, definition of "non-routable", promotion gate, and audit trail
- Created `02-non-routable-exclusions.md` in open--claw, AI-Project-Manager, and droidrun: alwaysApply: true rule excluding candidate_employees/** from search, memory, embeddings, routing
- Updated `README.md`: quarantine notice section added at top
- Updated `SOURCE_LIBRARY_CATALOG.md`: quarantine status column added to source table
- Updated `EMPLOYEE_READINESS_AUDIT.md`: quarantine notice section added
- Prepended `<!-- NON-ROUTABLE — OUT OF SCOPE -->` to all 2,608 candidate_employees/** markdown files
- Prepended `# NON-ROUTABLE — OUT OF SCOPE` to 3 droidrun iOS Python files

### Evidence

- PASS: `NON_ROUTABLE_QUARANTINE.md` created with all required sections (canonical registry, exclusion list, promotion gate, audit trail)
- PASS: 3 x `02-non-routable-exclusions.md` files created with alwaysApply: true
- PASS: 2,608 candidate_employees files bannered via PowerShell bulk prepend
- PASS: 3 droidrun iOS files bannered via StrReplace
- PASS: openmemory.mdc updated in both AI-Project-Manager and droidrun
- PASS: TAB_BOOTSTRAP_PROMPTS.md updated in open--claw and droidrun (PLAN and AGENT tabs)
- PASS: TRI_WORKSPACE_CONTEXT_BRIEF.md updated
- PASS: STATE.md updated in all 3 repos
- PASS: No files deleted — quarantine-only pass
- PASS: FINAL_OUTPUT_PRODUCT.md not modified

### Verdict

READY — Quarantine system installed at 5 enforcement layers: (1) file banners, (2) `.cursor/rules/` enforcement rules, (3) `openmemory.mdc` memory exclusions, (4) bootstrap prompt blocks, (5) canonical registry with promotion gate. No quarantined files deleted. Canonical source of truth: `NON_ROUTABLE_QUARANTINE.md`.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

AI-Project-Manager: `02-non-routable-exclusions.md` created; `openmemory.mdc` updated; `TRI_WORKSPACE_CONTEXT_BRIEF.md` updated.
droidrun: `02-non-routable-exclusions.md` created; iOS files bannered; `openmemory.mdc` updated; `TAB_BOOTSTRAP_PROMPTS.md` updated.

### Decisions Captured

- Quarantine is path-based and enforced at 5 layers simultaneously.
- candidate_employees/** is permanently non-routable until explicit promotion via `NON_ROUTABLE_QUARANTINE.md` promotion gate.
- Quarantine is a banner-only pass — no files deleted under any circumstance.
- Canonical source of truth for all quarantine status decisions: `open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`.

### Pending Actions

- open--claw `docs/ai/context/AGENT_EXECUTION_LEDGER.md` does not yet exist — create when the first open--claw AGENT block appends a ledger entry.
- open--claw STATE.md required a dedicated archive pass before the next non-trivial prompt block — **COMPLETED in this session**.

### What Remains Unverified

- PowerShell bulk prepend banner count: 2,608 reported but not independently spot-checked post-run.
- openmemory.mdc exclusions require a live memory search test to confirm candidate_employees paths are excluded.
- TAB_BOOTSTRAP_PROMPTS.md quarantine blocks: not tested in a live Cursor session to confirm they surface correctly on session start.

### What's Next

STATE.md archive pass complete. Proceed to Prompt 6.
---

## 2026-04-06 23:25 — Serena Project Normalization

### Goal

Add the repo-local Serena project for OpenClaw runtime work and mirror only the minimum local guidance needed so this repo uses the correct exact-path project without letting repo-root governance/docs masquerade as the main Serena code project.

### Scope

- `open--claw/.gitignore`
- `open--claw/open-claw/.serena/project.yml`
- `open--claw/AGENTS.md`
- `open--claw/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`
- `open--claw/docs/ai/HANDOFF.md`

### Commands / Tool Calls

- Tools: `ReadFile`, `ApplyPatch`
- Cross-repo verification tools used from AI-Project-Manager: `Glob`, `rg`

### Changes

- Updated `.gitignore` so `open-claw/.serena/project.yml` is commit-tracked while other Serena-local artifacts stay ignored.
- Created `open-claw/.serena/project.yml` with the runtime-specific Serena scope and ignored-path list.
- Added minimal repo-local guidance to `AGENTS.md`, `TAB_BOOTSTRAP_PROMPTS.md`, and `HANDOFF.md` telling sessions to activate `D:/github/open--claw/open-claw` by exact path for code work.

### Evidence

- PASS: `open-claw/.serena/project.yml` exists and is readable.
- PASS: `.gitignore` now unignores only `open-claw/.serena/project.yml`.
- PASS: `AGENTS.md`, tab bootstrap prompts, and handoff all state that repo-root docs/governance are not the default Serena code project.

### Verdict

READY — OpenClaw runtime now has the intended repo-local Serena project and the local guidance stays scoped to runtime code.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- Matches the AI-PM Serena project map and fallback policy.
- Keeps OpenClaw aligned with the DroidRun and AI-PM path-based activation model.

### Decisions Captured

- OpenClaw runtime Serena scope is `D:/github/open--claw/open-claw`, not repo root.
- Repo-root governance/docs work uses targeted read/search fallback unless a separate Serena project is explicitly activated.

### Pending Actions

- Live-test a fresh OpenClaw session to confirm the exact-path activation works as documented.

### What Remains Unverified

- Fresh-session Serena activation for `D:/github/open--claw/open-claw` has not yet been manually exercised after this normalization.

### What's Next

Use `D:/github/open--claw/open-claw` as the first Serena activation path on the next OpenClaw runtime code task.
---

## 2026-04-07 00:12 — MCP Tool Governance Alignment

### Goal

Mirror the updated tri-workspace tool policy so OpenClaw runtime work uses repo-first docs, requires the right high-value tools only when relevant, and stops to notify the user if a required tool is unavailable.

### Scope

- `open--claw/.cursor/rules/05-global-mcp-usage.md`
- Local config: `open--claw/.cursor/mcp.json`

### Commands / Tool Calls

- Tools: `ReadFile`, `ApplyPatch`
- Cross-repo verification from AI-Project-Manager: `WebSearch`, `ReadLints`

### Changes

- Rewrote the active MCP rule to align with the new repo-first docs and stop-notify tool policy.
- Added local `.cursor/mcp.json` so `serena`, `Exa Search`, `playwright`, `firecrawl-mcp`, and `Magic MCP` can be project-scoped in this workspace.
- Removed `sequential-thinking`, `shell-mcp`, and GitKraken MCP from the supported toolchain in the active rule surface.

### Evidence

- PASS: `.cursor/rules/05-global-mcp-usage.md` now requires repo docs first and external-doc query discipline.
- PASS: `.cursor/mcp.json` exists for this repo with the intended project-local servers.

### Verdict

READY — OpenClaw runtime now mirrors the cleaned high-value tool policy and has a project-local MCP config for heavier servers.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- Matches the canonical tool policy in AI-Project-Manager.

### Decisions Captured

- OpenClaw runtime keeps `playwright`, `firecrawl-mcp`, and `Magic MCP` local to this workspace rather than global.

### Pending Actions

- Reload Cursor to apply the new local MCP config.

### What Remains Unverified

- The new local MCP tool set has not yet been live-smoke-tested after reload.

### What's Next

Reload Cursor and verify the OpenClaw workspace exposes the expected project-local tools.

---

## 2026-04-08 00:15 — Serena Root Project + Workflow Parity

### Goal

Normalize the open--claw repo-root Serena project and mirror the latest workflow/tool-discipline updates from AI-Project-Manager.

### Scope

`.serena/project.yml`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`.

### Commands / Tool Calls

- Serena `activate_project`
- direct file edits from AI-Project-Manager governance pass

### Changes

- Updated repo-root Serena config so `open--claw` is a governance/docs Serena project.
- Clarified that `open--claw` repo root and `open-claw-runtime` are separate Serena projects.
- Added `Required Tools` prompt contract and launch-integrity rule parity.
- Updated Serena activation guidance to include `D:/github/open--claw` and `D:/github/droidrun`.

### Evidence

- PASS: `D:/github/open--claw` activates in Serena.
- PASS: repo-root `.serena/project.yml` now contains governance/docs-specific initial prompt and ignored runtime paths.

### Verdict

PASS — repo-root Serena behavior is now explicitly modeled instead of implicitly assumed.

### Blockers

- Current session activation still showed stale/empty language metadata for repo root; requires post-restart confirmation.

### Fallbacks Used

- Used exact-path activation and repo docs while cached Serena state remained stale.

### Cross-Repo Impact

- Mirrors AI-Project-Manager governance updates.

### Decisions Captured

- `open--claw` must keep two Serena projects: repo-root governance/docs and runtime subproject.

### Pending Actions

- Re-check repo-root Serena metadata after Cursor restart.

### What Remains Unverified

- Post-restart repo-root Serena metadata freshness.

### What's Next

- Verify both `open--claw` and `open-claw-runtime` appear healthy after restart.

---

## 2026-04-09 01:20 — Team Readiness Hardening + OpenMemory Drift Cleanup

### Goal

Realign OpenClaw handoff/rule surfaces with the repaired OpenMemory transport and add an operating model for Sparky plus the curated 15-employee squad.

### Scope

- `.cursor/rules/05-global-mcp-usage.md`
- `docs/ai/HANDOFF.md`
- `open-claw/AI_Employee_knowledgebase/README.md`
- `open-claw/AI_Employee_knowledgebase/TEAM_OPERATING_SYSTEM.md`

### Commands / Tool Calls

- Read current handoff, workflow checklist, readiness board, roster, and runtime validation docs
- Read post-restart OpenMemory verification outputs from AI-PM
- File edits only

### Changes

- Fixed the stale literal `` `r`n `` formatting bug in the OpenClaw MCP rule so the Serena activation map is readable again
- Updated OpenClaw `HANDOFF.md` to reflect repaired OpenMemory transport and current team-readiness priorities
- Added `TEAM_OPERATING_SYSTEM.md` to define pods, handoff chain, readiness states, and activation order for the curated squad
- Added the new operating-system doc to the knowledgebase README map

### Evidence

- PASS: curated roster already defines the 15 named employees and reporting chain
- PASS: readiness docs already track the real runtime blockers: 2 missing new bots, 3 unresolved direct token mappings, and first-run gateway pairing
- PASS: AI-PM OpenMemory verification remains green after restart (`VERIFY_OPENMEMORY_OK`)
- PASS: the operating model now exists as a single knowledgebase reference instead of being implied across multiple files

### Verdict

PASS — OpenClaw now has a clearer route from curated packets to an actual managed delivery team led by Sparky.

### Pending Actions

- Make the curated runtime `live_ready` by closing the 2 bot gaps and 3 direct secret-wiring gaps
- Exercise the delivery chain on a small internal packet before the first large external clone project
- Build the worker-facing memory-promotion path for Phase 1B

### What's Next

- Continue moving the curated squad from `packet_ready`/`runtime_ready` toward `smoke_ready` and `live_ready`.

---

## 2026-04-09 02:05 — Curated Squad Readiness Automation

### Goal

Make the curated 15-worker runtime measurable and partially startable so unresolved workers no longer block the whole squad.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- generated runtime artifacts
- knowledgebase readiness docs

### Commands / Tool Calls

- Regenerated runtime with `python open-claw/scripts/sync_curated_employee_runtime.py`
- Ran `open-claw/employees/deployed-curated/start-employees.ps1 -CheckOnly`
- Updated runtime and knowledgebase docs

### Changes

- Added `CURATED_TEAM_STATUS.json` as the generated machine-readable readiness source of truth
- Added deployed runtime `team-status.json`
- Upgraded generated `start-employees.ps1` to support `-CheckOnly`, partial startup, and `-Strict`
- Added `MEMORY_PROMOTION_TEMPLATE.md` and linked it from the team operating system
- Updated handoff/runtime docs to reflect the new check-only proof path

### Evidence

- PASS: generator completed with all validation checks green
- PASS: `-CheckOnly` shows 10 currently startable curated workers
- PASS: `-CheckOnly` shows the exact 5 blocked workers and why
- PASS: blocked workers match the known remaining gaps, not hidden runtime surprises

### Verdict

PASS — curated runtime startup is now evidence-driven and no longer all-or-nothing.

### Pending Actions

- Resolve direct mapping for `delivery-director`, `product-manager`, and `sparky-chief-product-quality-officer`
- Create new Telegram bots for `accessibility-auditor` and `backend-architect`
- Run the first curated-worker live smoke start after gateway pairing approval

### What's Next

- Use the readiness manifest and partial-start flow to move the curated squad toward `smoke_ready`.

---

## 2026-04-09 05:45 — Sparky Super-Coder Upgrade + Voice Front Desk Scaffold

### Goal

Strengthen the curated employee skill layer, turn Sparky into the broadest technical gate in the squad, and add the first real phone/voice runtime surface for live-human answering.

### Scope

- curated employee skill assignments under `open-claw/AI_Employee_knowledgebase/AI_employees/`
- new skill definitions under `open-claw/skills/`
- standalone phone/voice runtime under `open-claw/services/voice-front-desk-agent/`
- knowledgebase and handoff docs

### Commands / Tool Calls

- Audited current curated skill assignments and runtime generator requirements
- Queried current docs for Twilio Voice and ElevenLabs via Context7
- Added new skill files and updated curated employee packets
- Ran `python open-claw/scripts/sync_curated_employee_runtime.py`
- Ran `npm install express twilio ws zod dotenv @elevenlabs/elevenlabs-js`
- Ran `npm run check` in `open-claw/services/voice-front-desk-agent`
- Started the voice service locally and checked `http://127.0.0.1:8788/health`

### Changes

- Added three new tracked skills:
  - `twilio-voice-intake`
  - `elevenlabs-voice-clone`
  - `phone-support-intake`
- Expanded Sparky into a broader super-coder/final-gate packet with cross-domain skills for engineering, QA, communications, and phone/voice integration
- Added targeted skill upgrades for key specialists:
  - `delivery-director`
  - `product-manager`
  - `backend-architect`
  - `software-architect`
  - `accessibility-auditor`
  - `ux-architect`
- Added `VOICE_FRONT_DESK_STACK.md` so phone/voice work has a documented home without breaking the curated 15-worker invariant
- Added a modular standalone service at `open-claw/services/voice-front-desk-agent/` with:
  - env parsing
  - TwiML generation for inbound calls
  - Twilio voice webhook routes
  - websocket intake path
  - Dockerfile and runtime README

### Evidence

- PASS: `sync_curated_employee_runtime.py` reports all 15 curated employees still structurally valid
- PASS: copied skill folders now include the new Twilio and ElevenLabs skills inside Sparky's packet
- PASS: regenerated `CURATED_TEAM_STATUS.json` reflects Sparky's expanded skill bundle
- PASS: `npm run check` succeeds for `open-claw/services/voice-front-desk-agent`
- PASS: local health probe returns:
  - `{"ok":true,"voiceMode":"media-stream","publicBaseUrlConfigured":false,"websocketUrlConfigured":false,"elevenLabsConfigured":false}`

### Verdict

PASS WITH EXTERNAL SETUP REMAINING — the employee/skill layer is stronger, Sparky is upgraded, and the first real phone/voice runtime surface now exists in-repo. The voice stack is not yet live because external telephony credentials, cloned-voice credentials, and public webhook hosting are still missing.

### Pending Actions

- Resolve direct mapping for `delivery-director`, `product-manager`, and `sparky-chief-product-quality-officer`, or provide stable `*_TOKEN` env vars
- Create new Telegram bots for `accessibility-auditor` and `backend-architect`
- Add Twilio Voice credentials and a phone number
- Add ElevenLabs API key plus `voice_id` or `agent_id`
- Expose the voice service on public HTTPS/WSS and run a real smoke call

### What's Next

- Use the stronger Sparky packet plus upgraded specialist skills to push the curated squad toward `smoke_ready`
- Turn the voice-front-desk scaffold into a live call flow after Twilio and ElevenLabs provisioning is in place

---

## 2026-04-09 06:35 — Nerve Install + Secret Inventory Sync + Sparky Replacement Audit

### Goal

Install the Nerve web UI without disturbing the existing OpenClaw runtime, sync the latest Bitwarden worker-token inventory, and audit `temp/Sparky` as a possible full replacement for the curated Sparky packet.

### Scope

- `temp/openclaw-nerve/`
- `open-claw/scripts/start-openclaw-nerve.ps1`
- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/AI_Employee_knowledgebase/*`
- `docs/ai/HANDOFF.md`

### Commands / Tool Calls

- Read Nerve quick-start and repo docs
- Cloned `https://github.com/daggerhashimoto/openclaw-nerve.git` into `temp/openclaw-nerve`
- Ran `npm install` and `npm run build` for Nerve
- Launched Nerve locally and verified HTTP `200` on `http://127.0.0.1:3080`
- Read latest Bitwarden screenshots and patched missing worker-token inventory entries
- Updated runtime generator and regenerated curated artifacts
- Audited `temp/Sparky` and documented the replacement verdict

### Changes

- Installed Nerve in an isolated temp path so it sits in front of the gateway instead of replacing any existing runtime
- Added `open-claw/scripts/start-openclaw-nerve.ps1` as a no-secrets launcher that uses env-backed gateway auth
- Added the missing worker-token inventory entries for:
  - `ACCESSIBILITY_AUDITOR`
  - `BACKEND_ARCHITECT`
- Updated the curated runtime generator so those two workers are now token-backed with temporary `TBD` usernames until the final bot handles are recorded
- Regenerated `current_employees.md`, `CURATED_TEAM_STATUS.json`, and deployed-curated artifacts
- Added:
  - `SOURCE_REPOS_INDEX.md`
  - `SPARKY_REPLACEMENT_AUDIT.md`

### Evidence

- PASS: Nerve build completed successfully
- PASS: local Nerve probe returned HTTP `200` on `http://127.0.0.1:3080`
- PASS: regenerated roster now shows `accessibility-auditor` and `backend-architect` as `direct_uuid_wired`
- PASS: structural runtime regeneration still reports all 15 curated packets valid
- PASS: `temp/Sparky` audit concludes merge/salvage, not full replacement

### Verdict

PASS WITH FOLLOW-UP — Nerve is installed safely, the two missing worker tokens are now captured in repo docs and generator logic, and the temp Sparky packet is now documented as a governance/playbook source rather than a drop-in replacement.

### Pending Actions

- Record the final Telegram usernames for `accessibility-auditor` and `backend-architect`
- Resolve direct secret mapping or env injection for `delivery-director`, `product-manager`, and `sparky-chief-product-quality-officer`
- Decide whether Nerve remains an optional local cockpit or becomes part of the standard OpenClaw operator workflow
- If a deeper upstream import wave is needed, perform a full per-file index of local `source_repos` mirrors

### What's Next

- Use the updated 15-token roster to push the curated team closer to a real smoke start
- Keep salvaging doctrine from `temp/Sparky` without replacing the curated Sparky packet wholesale

## 2026-04-09 00:45 — Bootstrap And Workflow Mirror Alignment

### Goal

Align the open--claw bootstrap prompts and mirrored workflow docs with the current tri-workspace policy so PLAN, AGENT, DEBUG, and ARCHIVE stop using stale recovery assumptions.

### Scope

Touched `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/CURSOR_WORKFLOW.md`, `AGENTS.md`, `docs/ai/HANDOFF.md`, and `docs/ai/STATE.md`.

### Commands / Tool Calls

`ReadFile`, `rg`, `ApplyPatch`, `ReadLints`.

### Changes

- Updated tab bootstraps to require exactly one AGENT block from PLAN, include ledger gating, and use OpenMemory-first recovery with `STATE.md` / `DECISIONS.md` / `PATTERNS.md` / `HANDOFF.md`.
- Updated mirrored workflow docs/rules to match current tool, ledger, and source-priority policy.
- Rolled forward stale handoff/state wording so the summary surfaces reflect the latest worker-readiness reality instead of the older "new bots needed" wording.

### Evidence

- PASS: open--claw bootstrap prompt file updated and lint-clean
- PASS: mirrored workflow docs (`CURSOR_WORKFLOW.md`, `AGENTS.md`, `HANDOFF.md`) updated and lint-clean
- PASS: `ReadLints` returned no errors for touched open--claw files

### Verdict

READY — open--claw now mirrors the current policy on bootstrap sequencing, ledger use, and current curated-worker blocker wording.

### Blockers

None.

### Fallbacks Used

- Used targeted doc reads instead of Serena because this was a docs/rules audit, not a code-navigation task.

### Cross-Repo Impact

- Mirrors AI-Project-Manager governance updates so cross-repo tab behavior stays consistent.

### Decisions Captured

- Open--claw should keep using the execution ledger as a gated fallback only, never as default bootstrap context.
- Curated-worker status wording must track token-vs-username reality precisely to avoid misleading PLAN.

### Pending Actions

- Create the first open--claw local `docs/ai/context/AGENT_EXECUTION_LEDGER.md` entry when the next real open--claw AGENT execution block runs.

### What Remains Unverified

- Fresh-session behavior of the updated open--claw tab prompts inside Cursor.

### What's Next

- Resume curated-worker runtime hardening using the corrected bootstrap and blocker surfaces.

## 2026-04-10 01:20 — Reasoning Policy Mirror + Low-Bloat Bootstrap Tightening

### Goal

Mirror the new reasoning/tool policy into open--claw and reduce default bootstrap preload so PLAN relies on memory plus `STATE.md` first.

### Scope

Touched `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`.

### Commands / Tool Calls

`ReadFile`, `rg`, `ApplyPatch`, `ReadLints`.

### Changes

- Promoted `thinking-patterns` over the old Clear Thought naming in active workflow/rule surfaces.
- Added conditional guidance for `context-matic`, `obsidian-vault`, and `filesystem`.
- Tightened PLAN bootstrap so `STATE.md` is the first repo file after OpenMemory and other docs stay on-demand.

### Evidence

- PASS: open--claw mirrored rule and tab files updated successfully
- PASS: no linter errors in touched open--claw files

### Verdict

READY — open--claw bootstrap behavior now matches the lower-bloat recovery model and new reasoning MCP policy.

### Blockers

None.

### Fallbacks Used

- None.

### Cross-Repo Impact

- Mirrors the AI-Project-Manager canonical workflow/rule migration.

### Decisions Captured

- open--claw PLAN recovery should default to memory plus `STATE.md`, not broad multi-doc preload.

### Pending Actions

- Run the next real open--claw planning cycle through the updated bootstrap and confirm it stays context-light in practice.

### What Remains Unverified

- Live-session behavior of the updated open--claw bootstrap prompt under real task load.

### What's Next

- Continue curated runtime work with the leaner recovery path now in place.

## 2026-04-10 10:35 — Sparky Thinking-Patterns Alignment

### Goal

Align Sparky's packet with the newly promoted thinking-patterns MCP policy so his default tool usage matches the global reasoning rules.

### Scope

Touched `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/TOOLS.md`.

### Commands / Tool Calls

`ReadFile`, `ApplyPatch`.

### Changes

- Added `thinking-patterns reasoning` to Sparky's primary tools.
- Added explicit usage expectations covering `sequential_thinking`, `problem_decomposition`, `mental_model`, `decision_framework`, `debugging_approach`, and `critical_thinking`.

### Evidence

- PASS: Sparky packet now names `thinking-patterns` directly in his primary tool surface
- PASS: Sparky packet now instructs near-default use on non-trivial prompts

### Verdict

READY — Sparky's worker packet now reflects the active global reasoning policy instead of relying on implicit cross-repo inheritance alone.

### Cross-Repo Impact

- Mirrors the global `MCP-AGENT_RULES.mdc` rollout from the governance layer.

### What's Next

- Apply the same compact tool-expectation pattern to any other high-autonomy worker packets that should explicitly inherit the thinking-patterns discipline.

## 2026-04-10 12:05 — Sparky Video-Recovery Upgrade + Skill Runtime Validation Pass

### Goal

Strengthen Sparky for damaged-video recovery work, fix the recorded Telegram usernames for the two remaining curated workers, and re-prove the OpenClaw skill/runtime packaging path with actual validation commands.

### Scope

Touched Sparky packet files, added two new house skills under `open-claw/skills/`, hardened the employee-runtime sync and validation scripts, refreshed generated roster artifacts, and updated the skills audit surface.

### Commands / Tool Calls

`ReadFile`, `Shell`, `ApplyPatch`, `Context7`, `ReadLints`, plus read-only exploration subagents for the skill system and factory temp assets.

### Changes

- Added new skills:
  - `open-claw/skills/video-repair-forensics/SKILL.md`
  - `open-claw/skills/media-recovery-validation/SKILL.md`
- Expanded Sparky packet:
  - added `approval-gate`, `video-repair-forensics`, and `media-recovery-validation` to `SKILLS.md`
  - added media-recovery tool expectations to `TOOLS.md`
  - added a damaged-video recovery workflow to `WORKFLOWS.md`
  - updated Sparky `CHECKLIST.md` and `AUDIT.md` to reflect the new assignments
- Updated `sync_curated_employee_runtime.py` so:
  - `accessibility-auditor` now records `ACCESS_AUDITOR_ALLISON_BOT`
  - `backend-architect` now records `BACKEND_BRUCE_BOT`
  - skill parsing only reads actual bullet-list skill assignments instead of every backticked token in `SKILLS.md`
- Updated `validate_openclaw_workflow.py` to use the same safer skill parsing logic.
- Updated `AI_Employee_knowledgebase/SKILLS_AUDIT.md` with the two new media-recovery skills and the latest validation status.

### Evidence

- PASS: `python .\\open-claw\\scripts\\sync_curated_employee_runtime.py`
- PASS: `python .\\open-claw\\scripts\\validate_openclaw_workflow.py`
- PASS: regenerated `current_employees.md` now records:
  - `accessibility-auditor` → `ACCESS_AUDITOR_ALLISON_BOT`
  - `backend-architect` → `BACKEND_BRUCE_BOT`
- PASS: runtime validation summary shows all structural checks green, including copied assigned skills and generated bot/runtime artifacts
- PASS: Context7 FFmpeg docs were consulted for copy-first recovery guidance (`ffprobe`/`ffmpeg`, remux, timestamp regeneration, stream copy, faststart)

### Verdict

READY FOR STRUCTURAL USE — the open--claw employee skill system is now structurally consistent again, Sparky has dedicated damaged-video recovery skills, and the curated runtime validation suite is green.

### Blockers

- Live end-to-end worker startup with real gateway credentials is still not proven for all workers.
- Sparky's actual damaged AxCrypt-decrypted video files still need a real recovery run and evidence log.
- `delivery-director`, `product-manager`, and `sparky-chief-product-quality-officer` still need direct secret mapping or stable env-backed runtime injection to be fully runtime-ready.

### Findings From Factory Assets

- The proactive-agent v3.1.0 pack is useful as doctrine and operating-pattern input, especially around WAL / working-buffer / compaction-recovery behavior.
- The Formula One AI Factory zip is richer as a development environment for employee-building doctrine, but it should remain an upstream build source, not a blind replacement for the curated OpenClaw packet standard.

### What's Next

- Run Sparky on the actual damaged video set using the new recovery workflow and capture evidence per attempt.
- Decide whether to import more factory-style live-state doctrine (`SESSION-STATE`, working-buffer, WAL discipline) into the curated employee standard in a controlled way instead of ad hoc packet drift.

---

## 2026-04-10 18:53 — Obsidian + Sparky Rule Hardening Implementation (Cross-Repo Pass)

### Goal

Align open--claw memory/rule systems to match the tri-workspace Obsidian/OpenMemory policy and strengthen Sparky rule indexing at repo level.

### Scope

- `open--claw\.cursor\rules\05-global-mcp-usage.md` — obsidian-vault policy aligned
- `open--claw\AGENTS.md` — sparky-mandatory-tool-usage.md indexed
- `open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\ACCESS.md` — role preamble added
- `open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\TOOLS.md` — role preamble added
- `open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\COMPLETE_TOOL_REFERENCE.md` — role preamble added
- `open--claw\docs\ai\STATE.md` — this entry

### Commands / Tool Calls

- StrReplace: 5 file updates in open--claw
- Grep: verified rule surfaces and cross-references

### Changes

**Obsidian/OpenMemory Policy Alignment:**
- Updated `05-global-mcp-usage.md` to align with AI-PM policy
- Both AI-PM and open--claw now state: OpenMemory = **primary durable structured memory backbone**; Obsidian = **fast-access scoped note memory sidecar**
- Explicit relationship and anti-patterns now documented consistently

**Sparky Access Docs Deduplication:**
- Added role preambles to all three Sparky access docs:
  - `ACCESS.md`: persistent access config + recovery
  - `TOOLS.md`: canonical exec routing + usage
  - `COMPLETE_TOOL_REFERENCE.md`: inventory/reference only (NOT enforcement)
- Cross-references added between files for clarity

**Sparky Rule Indexing:**
- Added `sparky-mandatory-tool-usage.md` to `AGENTS.md` Authoritative rules list
- Sparky enforcement rule now repo-level indexed alongside other mandatory rules

### Evidence

- PASS: open--claw `05-global-mcp-usage.md` aligned with AI-PM policy
- PASS: All three Sparky access docs have distinct role preambles
- PASS: `AGENTS.md` now indexes sparky-mandatory-tool-usage.md
- PASS: Cross-references between ACCESS.md, TOOLS.md, COMPLETE_TOOL_REFERENCE.md working
- PASS: Changes compact and focused per plan requirements

### Verdict

READY — open--claw memory/tool policy now matches tri-workspace standard. Sparky rule hierarchy clarified and indexed.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- AI-PM: MCP rule and tooling docs updated in parallel
- Both repos now have consistent Obsidian/OpenMemory relationship
- Sparky rule hierarchy documented uniformly

### Decisions Captured

Same as AI-PM entry — OpenMemory = primary backbone, Obsidian = fast-access sidecar, Sparky rule hierarchy clarified.

### Pending Actions

None - all planned changes completed.

### What Remains Unverified

- Live Sparky session using updated rule surfaces
- Whether ACCESS/TOOLS/COMPLETE_TOOL_REFERENCE role separation improves operational clarity

### What's Next

Plan complete. System ready with clarified memory/tool hierarchy.

---

## 2026-04-10 22:08 - Curated Employee Runtime Drift Gate

### Goal

Reduce drift across the curated `AI_employees` runtime packets by centralizing the shared runtime baseline and adding an executable checker for the repeated Docker/package shell.

### Scope

- `open-claw/AI_Employee_knowledgebase/AI-EMPLOYEE-STANDARD.md`
- `open-claw/AI_Employee_knowledgebase/runtime/employee-runtime-baseline.json`
- `open-claw/AI_Employee_knowledgebase/runtime/check-runtime-drift.mjs`

### Commands / Tool Calls

- Read: `AI-EMPLOYEE-STANDARD.md`, curated `package.json` and `Dockerfile` samples - PASS
- Search: repeated Docker/package runtime values under `AI_Employee_knowledgebase/AI_employees` - PASS
- Write: create shared runtime baseline JSON - PASS
- Write: create Node drift checker for curated live packets - PASS
- Write: add baseline/drift-check requirement to `AI-EMPLOYEE-STANDARD.md` - PASS
- Shell: `node AI_Employee_knowledgebase/runtime/check-runtime-drift.mjs` - PASS
- Lints: changed knowledgebase files - PASS

### Changes

- Added `employee-runtime-baseline.json` as the single source of truth for the shared curated packet runtime shell:
  - Docker base image: `node:22-slim`
  - OpenClaw runtime version: `2026.3.13`
  - Shared channel dependency versions
- Added `check-runtime-drift.mjs`, a no-dependency validator that scans curated employee packets with both `Dockerfile` and `package.json` and fails on baseline drift.
- Updated `AI-EMPLOYEE-STANDARD.md` so curated live packets must match the shared runtime baseline or carry an explicit documented exception.

### Evidence

- PASS: Repeated runtime values were confirmed across the curated employee packets before centralization
- PASS: `node AI_Employee_knowledgebase/runtime/check-runtime-drift.mjs` reported `PASS: 15 curated AI employee runtime packets match the shared baseline.`
- PASS: `ReadLints` returned no diagnostics for the changed files

### Verdict

READY - OpenClaw now has a centralized runtime baseline and an executable gate to catch packet drift before it spreads across curated employees.

### Blockers

None.

### Fallbacks Used

- The first checker pass tried to scan `_zips/` as if it were a live packet; discovery logic was tightened to require both `Dockerfile` and `package.json` before validating a directory.

### Cross-Repo Impact

None - changes are isolated to the curated employee knowledgebase in `open--claw/open-claw`.

### Decisions Captured

- Use a shared baseline plus drift checker as the smallest high-value centralization step instead of attempting a larger packet generator/refactor.
- Treat only directories with both `Dockerfile` and `package.json` as live curated packets for this gate.

### Pending Actions

None.

### What Remains Unverified

- The checker currently enforces only the shared Docker base/runtime version and shared channel dependencies; it does not yet validate every runtime file in the packet shell.
- No CI wiring was added in this pass; the checker is ready for future automation.

### What's Next

Proceed to `droidrun` and reconcile README/runtime messaging with the repo's Android-only governance and iOS quarantine.

---

## 2026-04-12 12:44 - Curated Bot Roster Reconciled Against Latest Bitwarden Screenshots

### Goal

- Cross-reference the latest three Bitwarden secret screenshots against the repo-tracked bot roster and correct the generated roster files so the current bot/secret wiring state is accurate.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/AI_Employee_knowledgebase/CURATED_TEAM_STATUS.json`
- `open-claw/AI_Employee_knowledgebase/current_employees.md`
- screenshot-backed evidence from the latest Bitwarden Secrets UI captures

### Commands / Tool Calls

- Read screenshots and roster docs - PASS
- Search `CURATED_TEAM_STATUS.json` and generator source for stale `env_only_assigned` mappings - PASS
- Update missing direct UUID mappings in `sync_curated_employee_runtime.py` - PASS
- Shell: `python "D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py"` - PASS
- Read regenerated `current_employees.md` and `CURATED_TEAM_STATUS.json` - PASS
- `ReadLints` on changed files - PASS

### Changes

- Added direct Bitwarden UUID mappings to `sync_curated_employee_runtime.py` for:
  - `delivery-director` -> `f08c26ae-8b3b-42db-8b8a-b41e00254ae0`
  - `product-manager` -> `262ed8cc-9adf-46a6-a0ba-b41e00258aa7`
  - `sparky-chief-product-quality-officer` -> `e08b6a94-02bf-4222-876a-b41e00251315`
- Regenerated:
  - `open-claw/AI_Employee_knowledgebase/CURATED_TEAM_STATUS.json`
  - `open-claw/AI_Employee_knowledgebase/current_employees.md`

### Evidence

- Before the fix, the generated roster incorrectly claimed:
  - `Direct Bitwarden UUIDs already wired: 12`
  - `Assigned bots still waiting on env vars or UUID recording: delivery-director, product-manager, sparky-chief-product-quality-officer`
- Screenshot-backed Bitwarden inventory showed those three secrets now exist with direct UUIDs, including:
  - `DELIVERY_DIRECTOR`
  - `PRODUCT_MANAGER`
  - `SPARKY_CEO_BOT`
- After regeneration, `current_employees.md` now reports:
  - `Direct Bitwarden UUIDs already wired: 15`
  - `Assigned bots still waiting on env vars or UUID recording: none`
- After regeneration, `CURATED_TEAM_STATUS.json` now reports:
  - `"direct_uuid_wired": 15`
  - `"env_only_assigned": 0`
- `sparky-chief-product-quality-officer` remains mapped to:
  - Telegram first name: `sparky-chief-product-quality-officer`
  - Telegram username: `SPARKY_CEO_BOT`
  - runtime status: `direct_uuid_wired`
- `ReadLints` returned no diagnostics for the changed generator and generated files.

### Verdict

READY - the repo-tracked curated bot roster is now aligned with the latest Bitwarden screenshot evidence for all 15 assigned bots.

### What Remains Unverified

- This pass reconciles repo-tracked roster metadata against Bitwarden screenshot evidence; it does not independently prove each Telegram bot can authenticate and start live.

---

## 2026-04-12 13:58 - Curated Bot Roster Normalized To Current Bitwarden Secret Names

### Goal

- Reconcile the curated OpenClaw employee roster with the latest Telegram and Bitwarden screenshots after the bot secret names were renamed to the current stored Bitwarden names.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- generated curated employee docs under `open-claw/AI_Employee_knowledgebase/`

### Commands / Tool Calls

- Read screenshot evidence for Telegram first names, usernames, and Bitwarden secret names - PASS
- Read generated roster and generator source - PASS
- Patch generator secret mapping and rendered roster fields - PASS
- Shell: `python "D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py"` - PASS
- Search stale wording in authoritative knowledgebase docs - PASS
- Lints on changed files - PASS

### Changes

- Replaced the generator's old secret-key assumptions with current Bitwarden secret names such as:
  - `ACCESS_AUDITOR_ALLISON_BOT`
  - `API_ANDY_BOT`
  - `DELIVERY_DIRECTOR_DAN_BOT`
  - `PRODUCT_MANAGER_PETE_BOT`
  - `SPARKY_CEO_BOT`
- Corrected the curated mapping for `ACCESS_AUDITOR_ALLISON_BOT` to UUID `b1ff4d8c-d7ed-48e8-b96b-b427013718aa`.
- Added `Bitwarden secret name` to the generated `current_employees.md` assignment table and per-employee sections.
- Added `secret_name` to `CURATED_TEAM_STATUS.json`.
- Regenerated curated employee outputs so the `AUDIT.md`, `current_employees.md`, deployed runtime metadata, and `CURATED_TEAM_STATUS.json` reflect the latest secret naming.
- Updated stale knowledgebase docs:
  - `open-claw/AI_Employee_knowledgebase/README.md`
  - `open-claw/AI_Employee_knowledgebase/EMPLOYEE_READINESS_AUDIT.md`

### Evidence

- `current_employees.md` now includes a `Bitwarden secret name` column for all 15 curated workers.
- `CURATED_TEAM_STATUS.json` now carries both `telegram_username` and `secret_name`.
- Stale claims like `13 curated workers`, `10 wired`, `TBD usernames`, and `env-only in repo` were removed from current authoritative docs.

### Verdict

READY - the curated OpenClaw roster now cross-references current Telegram identity data with the current Bitwarden secret names stored for the 15-worker curated squad.

### What Remains Unverified

- This pass does not prove the two extra logged bot secrets outside the curated roster are used by any active worker runtime.
- Live startup and message delivery still need real smoke validation.

---

## 2026-04-12 14:15 - Secondary Sparky Renamed To Secretary Stacy

### Goal

- Reflect the rename of the older non-curated runtime Sparky identity from `Sparky4bot` to `SECRETARY_STACY_BOT` without changing the curated lead Sparky assignment.

### Scope

- `docs/ai/HANDOFF.md`
- `docs/ai/STATE.md`

### Changes

- Updated the live runtime Telegram reference from `@Sparky4bot` to `@SECRETARY_STACY_BOT`.
- Clarified by implication that this runtime-channel Sparky is separate from the curated lead/executive Sparky packet, which remains `SPARKY_CEO_BOT`.

### Evidence

- The curated lead Sparky in the employee knowledgebase still maps to:
  - slug: `sparky-chief-product-quality-officer`
  - Telegram username: `SPARKY_CEO_BOT`
- The updated current runtime docs now point the older runtime-channel identity to `@SECRETARY_STACY_BOT`.

### Verdict

READY - current OpenClaw operational docs now distinguish the renamed secondary/runtime Sparky from the curated lead Sparky.

---

## 2026-04-12 14:55 - Curated CEO Sparky Startup Path Hardened

### Goal

- Verify that the curated startup script can actually bring up `SPARKY_CEO_BOT`, and strengthen the generated runtime so CEO Sparky is easier to start, clearly identifiable in Telegram, and less dependent on the shared `main` agent route for urgent video-repair work.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- generated files under `open-claw/employees/deployed-curated/`
- generated CEO worker runtime files under `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/`

### Commands / Tool Calls

- Read generated startup/runtime files and CEO packet runtime files - PASS
- Patch the generator for dedicated agent routing, CEO-first startup, and video-tool runtime hardening - PASS
- Shell: `python "D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py"` - PASS
- Shell: `pwsh -NoProfile -File "D:/github/open--claw/open-claw/employees/deployed-curated/start-employees.ps1" -CheckOnly -CeoOnly` - PASS
- Shell: `docker compose config` in `open-claw/employees/deployed-curated` - PASS with expected env warnings when run outside the startup wrapper/script
- `ReadLints` on changed files - PASS

### Changes

- `openclaw-runner.js` now routes through `OPENCLAW_AGENT_ID` instead of hardcoding every worker to `main`.
- Worker entrypoints now register both `main` and a dedicated per-worker agent id, and default `OPENCLAW_AGENT_ID` to the worker slug.
- Generated compose entries now inject `OPENCLAW_AGENT_ID=<worker-slug>` for each worker, including `sparky-chief-product-quality-officer`.
- `start-employees.ps1` now:
  - reports whether CEO Sparky is ready
  - prioritizes CEO Sparky first in ready-service ordering
  - supports `-CeoOnly`
  - supports `-RequireCeo`
- Generated worker Dockerfiles now install `ffmpeg` and `mediainfo` so the runtime has an in-container video-triage fallback.
- Telegram `/start` messaging now reports the worker slug and active agent route, reducing the risk of talking to the wrong worker again.

### Evidence

- `start-employees.ps1 -CheckOnly -CeoOnly` returned:
  - `Ready curated workers: 15`
  - `sparky-chief-product-quality-officer`
  - `CEO Sparky ready: True`
- Generated CEO entrypoint now sets:
  - `OPENCLAW_AGENT_ID=sparky-chief-product-quality-officer`
  - agent config list includes both `main` and `sparky-chief-product-quality-officer`
- Generated CEO runner now uses:
  - `const agentId = process.env.OPENCLAW_AGENT_ID || "main";`
- `docker compose config` succeeded and showed the generated CEO service includes:
  - `OPENCLAW_AGENT_ID: sparky-chief-product-quality-officer`
- `ReadLints` reported no diagnostics for the changed generator and generated files.

### Verdict

READY FOR LIVE CEO BOT STARTUP - the curated startup path now recognizes CEO Sparky as startable, can launch CEO alone, and no longer hardcodes the CEO bot into the shared `main` agent route.

### What Remains Unverified

- This pass did not actually start the Docker container or prove that `SPARKY_CEO_BOT` is currently responding live in Telegram.
- The dedicated per-worker agent route is now generated, but live authority over other workers still depends on actual OpenClaw runtime behavior once the CEO bot is started and smoke-tested.

---

## 2026-04-12 15:18 - CEO Sparky Live Startup Blocked By Docker Engine Down

### Goal

- Re-test the newly hardened CEO-only startup path and identify why `SPARKY_CEO_BOT` still was not responding live in Telegram.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/start-employees.ps1`

### Commands / Tool Calls

- Shell: `pwsh -NoProfile -File "D:/github/open--claw/open-claw/employees/deployed-curated/start-employees.ps1" -CheckOnly -CeoOnly` - PASS
- Shell: `docker ps` / `docker ps -a` - FAIL because Docker engine unreachable
- Patch generator to fail fast on missing Docker engine - PASS
- Shell: `python "D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py"` - PASS
- Shell: `pwsh -NoProfile -File "D:/github/open--claw/open-claw/employees/deployed-curated/start-employees.ps1" -CeoOnly -RequireCeo` - FAIL with clear Docker error
- `ReadLints` on changed files - PASS

### Changes

- Added a Docker preflight to the generated startup script so it now throws a clear actionable message when Docker Desktop / the Docker engine is not running.

### Evidence

- CEO startup readiness still reports:
  - `CEO Sparky ready: True`
- Actual live startup now fails with the real blocker:
  - `Docker engine is not reachable. Start Docker Desktop and wait until it shows Engine running, then rerun start-employees.ps1.`
- This confirms the current failure is not:
  - Telegram bot creation
  - Bitwarden token mapping
  - CEO worker readiness inside the generated startup script

### Verdict

BLOCKED BY LOCAL RUNTIME - `SPARKY_CEO_BOT` is ready to launch, but Docker Desktop's engine must be running before the CEO container can actually start and respond in Telegram.

---

## 2026-04-12 15:42 - CEO Sparky Corrected To Host-Native Runtime

### Goal

- Correct the runtime model after confirming `sparky-chief-product-quality-officer` was never supposed to be part of the Dockerized curated worker pool.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/README.md`
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `open-claw/AI_Employee_knowledgebase/current_employees.md`
- `open-claw/AI_Employee_knowledgebase/CURATED_TEAM_STATUS.json`
- `open-claw/AI_Employee_knowledgebase/OPENCLAW_WORKFLOW_CHECKLIST.md`
- `open-claw/AI_Employee_knowledgebase/RUNTIME_VALIDATION_SUMMARY.md`

### Commands / Tool Calls

- Patch generator to exclude `sparky-chief-product-quality-officer` from `deployed-curated` Docker runtime - PASS
- Shell: `python "D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py"` - PASS
- Shell: `pwsh -NoProfile -File "D:/github/open--claw/open-claw/employees/deployed-curated/start-employees.ps1" -CheckOnly` - PASS
- Shell: `pwsh -NoProfile -File "D:/github/open--claw/open-claw/employees/deployed-curated/start-employees.ps1" -CeoOnly` - PASS (expected explicit refusal)

### Changes

- Regenerated `deployed-curated` as a 14-worker Docker pool that excludes CEO Sparky.
- Marked `sparky-chief-product-quality-officer` as `host_native_primary` in the generated roster/status outputs.
- Changed the generated Docker startup script so `-CeoOnly` and `-RequireCeo` now fail immediately with a clear message instead of implying Sparky belongs in Docker.
- Updated runtime documentation to state that CEO Sparky is host-native and outside the Docker worker pool.

### Evidence

- `employees/deployed-curated/README.md` now says `sparky-chief-product-quality-officer` is intentionally excluded from the Docker runtime.
- `start-employees.ps1 -CheckOnly` now reports `Ready dockerized curated workers: 14`.
- `start-employees.ps1 -CeoOnly` now throws:
  - `CEO Sparky is intentionally excluded from deployed-curated Docker startup.`
- `CURATED_TEAM_STATUS.json` now reports:
  - `"dockerized_worker_count": 14`
  - `"host_native_worker_count": 1`

### Checklist

- [x] Generator corrected
- [x] Runtime artifacts regenerated
- [x] Docker worker pool now excludes CEO Sparky
- [x] Generated status docs mark Sparky as host-native
- [x] Startup script now blocks the wrong CEO Docker path explicitly

### Verdict

CORRECTED DESIGN - the prior Docker-first diagnosis for `SPARKY_CEO_BOT` was wrong. Docker remains the worker-pool runtime for the other curated employees, but CEO Sparky is now explicitly modeled as the host-native executive runtime.

### What Remains Broken

- This change removes the incorrect Docker path, but it does not by itself prove that the host-native `SPARKY_CEO_BOT` Telegram runtime is live and responding.
- The exact host-native startup/binding path for `SPARKY_CEO_BOT` still needs to be verified against the primary OpenClaw gateway runtime.

---

## 2026-04-12 16:02 - Telegram Registry MCP Design Blocked By OpenMemory Failure

### Goal

- Start the clean Telegram bot control-plane work: one canonical registry, one lightweight rule set, one doc page, and an MCP-facing management path for the 15-employee team.

### Scope

- `open--claw/AGENTS.md`
- `open--claw/.cursor/rules/05-global-mcp-usage.md`
- `open--claw/.cursor/rules/10-project-workflow.md`
- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/AI_Employee_knowledgebase/current_employees.md`
- `AI-Project-Manager/package/package.json`
- `AI-Project-Manager/package/README.md`
- `AI-Project-Manager/package/test/cli.test.mjs`
- MCP descriptors under `C:\Users\ynotf\.cursor\projects\d-github-AI-Project-Manager\mcps\`

### Commands / Tool Calls

- `functions.ReadFile` — `C:\Users\ynotf\.cursor\skills-cursor\create-rule\SKILL.md` - PASS
- `functions.ReadFile` — `D:\github\open--claw\AGENTS.md` - PASS
- `functions.ReadFile` — `D:\github\AI-Project-Manager\AGENTS.md` - PASS
- `functions.ReadFile` — `D:\github\open--claw\.cursor\rules\05-global-mcp-usage.md` - PASS
- `functions.ReadFile` — `D:\github\open--claw\.cursor\rules\10-project-workflow.md` - PASS
- `functions.ReadFile` — `D:\github\AI-Project-Manager\package\package.json` - PASS
- `functions.ReadFile` — `D:\github\AI-Project-Manager\package\README.md` - PASS
- `functions.ReadFile` — `D:\github\AI-Project-Manager\package\test\cli.test.mjs` - PASS
- `functions.Subagent` (`explore`) — Telegram/MCP inventory sweep - PASS
- `functions.Glob` — `...\mcps\user-thinking-patterns\tools\*.json` - PASS
- `functions.ReadFile` — `...\mcps\user-thinking-patterns\tools\problem_decomposition.json` - PASS
- `functions.Glob` — `...\mcps\user-openmemory\tools\*.json` - FAIL (`Path does not exist`)
- `functions.Glob` — `...\mcps\user-openmemory\**\*` - FAIL (`Path does not exist`)
- `functions.Glob` — `...\mcps\user-openmemory-local\**\*` - PASS
- `functions.ReadFile` — `...\mcps\user-openmemory-local\STATUS.md` - FAIL (`The MCP server errored`)
- `functions.ReadFile` — `...\mcps\user-openmemory-local\SERVER_METADATA.json` - PASS
- Shell: `Get-Date -Format "yyyy-MM-dd HH:mm"` - PASS

### Changes

- No product/code changes were made because the required OpenMemory MCP was unavailable and the repo MCP policy forbids silently continuing past that blocker for this kind of architecture work.

### Evidence

- PASS: `thinking-patterns` descriptors are present, including `problem_decomposition.json`.
- FAIL: `user-openmemory` descriptor path does not exist under the local MCP descriptor cache.
- FAIL: `user-openmemory-local/STATUS.md` explicitly says `The MCP server errored.`
- PASS: Current repo control plane is already centered on `open-claw/scripts/sync_curated_employee_runtime.py` plus generated `current_employees.md` / `CURATED_TEAM_STATUS.json`; this is the right place to anchor a future Telegram registry MCP once the memory gate is healthy.

### Verdict

BLOCKED - required memory MCP is currently unavailable, so the Telegram registry MCP/rule implementation was not started.

### Blockers

- `openmemory` / `openmemory-local` MCP is errored or missing descriptors.

### Fallbacks Used

- Used repo docs/code inspection plus a read-only explore subagent to identify the current Telegram registry surface.
- No fallback implementation was started because the repo rule forbids proceeding past a required MCP failure for this category of work.

### Cross-Repo Impact

- `AI-Project-Manager` package scaffolding appears reusable for a future local MCP package, but no files were changed there.

### Decisions Captured

- Telegram username should remain the canonical external bot ID.
- The current Python generator is the best seed for a future single-source bot registry.

### Pending Actions

- Restore the OpenMemory MCP in Cursor.
- After restore, implement the Telegram bot registry, MCP tools, simple rule file(s), and generated markdown roster.

### What Remains Unverified

- Whether the restored OpenMemory MCP will expose callable tools immediately once Cursor reloads.
- The exact host-native runtime binding for `SPARKY_CEO_BOT`.

### What's Next

- User restores the OpenMemory MCP in Cursor Settings, or explicitly tells AGENT to override the OpenMemory gate for this session.

---

## 2026-04-12 17:49 - SPARKY_CEO_BOT Host-Native Startup Path Restored

### Goal

Audit why `SPARKY_CEO_BOT` stopped responding after the `@Sparky4bot` secretary-handle cleanup, determine whether the issue was gateway/bot wiring versus username confusion, and fix the startup path so the CEO bot once again receives its Bitwarden token at launch.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `open-claw/employees/deployed-curated/README.md`
- `docs/ai/HANDOFF.md`
- `docs/ai/STATE.md`
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md`

### Commands / Tool Calls

- `functions.ReadFile` — repo docs, runtime files, rules, and MCP tool descriptors
- `functions.rg` — searched `SPARKY_CEO_BOT`, `Sparky4bot`, Bitwarden UUIDs, and startup references
- `functions.Glob` — inspected MCP tool descriptor availability
- `functions.Subagent` (`explore`) — read-only bot wiring audit in `D:/github/open--claw`
- `functions.CallMcpTool` — `user-thinking-patterns.sequential_thinking`
- `functions.CallMcpTool` — `user-thinking-patterns.debugging_approach`
- `functions.CallMcpTool` — `user-serena.activate_project`
- `functions.CallMcpTool` — `user-serena.find_symbol`
- `functions.ApplyPatch` — patched generator, generated startup files, and docs
- Shell: `Get-ChildItem`
- Shell: `python -c "import importlib.util, pathlib; p=pathlib.Path('D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py'); spec=importlib.util.spec_from_file_location('sync_curated_employee_runtime', p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.render_start_script(m.parse_employees()))"` 
- Shell: `python -c "import importlib.util, pathlib; p=pathlib.Path('D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py'); spec=importlib.util.spec_from_file_location('sync_curated_employee_runtime', p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.render_runtime_readme(m.parse_employees()))"`
- Shell: `python -c "import importlib.util, pathlib, sys; p=pathlib.Path('D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py'); spec=importlib.util.spec_from_file_location('sync_curated_employee_runtime', p); m=importlib.util.module_from_spec(spec); sys.modules[spec.name]=m; spec.loader.exec_module(m); print(m.render_start_script(m.parse_employees()))"`
- Shell: `python -c "import importlib.util, pathlib, sys; p=pathlib.Path('D:/github/open--claw/open-claw/scripts/sync_curated_employee_runtime.py'); spec=importlib.util.spec_from_file_location('sync_curated_employee_runtime', p); m=importlib.util.module_from_spec(spec); sys.modules[spec.name]=m; spec.loader.exec_module(m); print(m.render_runtime_readme(m.parse_employees()))"`
- Shell: `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CheckOnly -CeoOnly`
- `functions.ReadLints`

### Changes

- Confirmed the old `@Sparky4bot` handle only survives in docs as the secretary rename history; it is not the live CEO binding.
- Identified the actual defect: `SPARKY_CEO_BOT` was correctly mapped to Bitwarden UUID `e08b6a94-02bf-4222-876a-b41e00251315`, but the generated startup script excluded the CEO path entirely and never injected `TELEGRAM_BOT_TOKEN` for the host-native runtime.
- Patched `render_start_script()` so the generated startup script now:
  - resolves `SPARKY_CEO_BOT` into `TELEGRAM_BOT_TOKEN`
  - exposes `-CheckOnly -CeoOnly` for CEO readiness audit
  - exposes `-CeoOnly` to start the host-native CEO packet
  - exposes `-RequireCeo` to require/start CEO before the Docker worker pool
  - checks for `node`, `openclaw`, packet presence, and duplicate `node bot-telegram.js` launches
  - installs packet npm dependencies on first live CEO start instead of silently failing
- Updated the live generated `start-employees.ps1` and `README.md` to match the new host-native CEO flow.
- Updated `docs/ai/HANDOFF.md` so the curated runtime summary and blockers no longer claim the CEO token mapping/path is unresolved.

### Evidence

- PASS — `functions.Subagent` (`explore`) found the real root cause: CEO registry mapping was correct, but the startup script only resolved Docker worker secrets and explicitly rejected the CEO path.
- PASS — `functions.CallMcpTool` `user-thinking-patterns.debugging_approach` captured the root-cause analysis and pointed to the missing host-native launcher.
- PASS — `functions.CallMcpTool` `user-serena.activate_project` activated `D:/github/open--claw/open-claw`.
- FAIL — `functions.CallMcpTool` `user-serena.find_symbol` returned no symbols for the Python generator; fallback was targeted `ReadFile` plus `ApplyPatch`.
- FAIL — the first two render helper commands raised a Python `dataclasses` import/module-registration error because `sys.modules[spec.name]` was not populated before `exec_module`.
- PASS — the corrected render helper commands (with `sys.modules[spec.name] = m`) produced the updated `start-employees.ps1` and `README.md` content.
- PASS — `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"` completed successfully.
- PASS — `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CheckOnly -CeoOnly` returned:
  - `Host-native CEO Sparky ready: True`
  - packet path `D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer`
  - `npm dependencies will be installed on first CEO start.`
  - `Check-only mode: host-native CEO runtime not started.`
- PASS — `functions.ReadLints` ended with no diagnostics on the changed generator/startup files.

### Verdict

READY — the repo now has a supported host-native startup path for `SPARKY_CEO_BOT`, and the startup script successfully verifies that the CEO bot can resolve its Bitwarden token and packet path.

### Blockers

- Live Telegram smoke evidence is still pending because only `-CheckOnly -CeoOnly` was run in this block.

### Fallbacks Used

- `user-serena.find_symbol` did not return Python symbols for `sync_curated_employee_runtime.py`; fallback was targeted `functions.ReadFile` and `functions.ApplyPatch`.
- The first shell-based render attempts failed because of Python module-registration behavior; fallback was the corrected `sys.modules[spec.name] = m` import pattern.

### Cross-Repo Impact

- None.

### Decisions Captured

- `start-employees.ps1 -CeoOnly` is now the canonical host-native launcher for `SPARKY_CEO_BOT`.
- The CEO startup path must inject the Bitwarden secret into `TELEGRAM_BOT_TOKEN`, not just keep a registry mapping in docs/generator metadata.
- `-RequireCeo` should gate Docker worker startup on a healthy CEO host-native path instead of pretending the CEO belongs in Docker.

### Pending Actions

- Run `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`.
- Send `/start` to `SPARKY_CEO_BOT` in Telegram and confirm a normal text message reply.
- If needed, run `start-employees.ps1 -RequireCeo` before bringing up the Docker worker pool.

### What Remains Unverified

- Whether the live host-native CEO process responds in Telegram after a real non-check-only launch.
- Whether the user’s normal shell outside this Cursor session still has `node`, `npm`, `openclaw`, and Bitwarden access available in the same way.
- End-to-end elevated command authority through the restored CEO runtime.

### What's Next

- Perform the real `-CeoOnly` launch and smoke-test `SPARKY_CEO_BOT` in Telegram.

---

## 2026-04-12 17:53 - SPARKY_CEO_BOT Live Host-Native Launch Completed

### Goal

Move past the repo-only fix, perform a real host-native CEO launch, and verify whether `SPARKY_CEO_BOT` now stays running and whether the local OpenClaw gateway is reachable.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `docs/ai/STATE.md`
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md`

### Commands / Tool Calls

- `functions.ApplyPatch` — corrected the npm invocation and detached PowerShell env injection in the generator and generated startup script
- `functions.ReadFile` — inspected the generated startup script
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`
- Shell: `$packet = 'D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer'; $env:TELEGRAM_BOT_TOKEN = ((bws secret get e08b6a94-02bf-4222-876a-b41e00251315) | ConvertFrom-Json).value; $env:OPENCLAW_GATEWAY_TOKEN = ((bws secret get 79f3acf8-c855-4c0d-9726-b40d01278bb6) | ConvertFrom-Json).value; if (-not $env:OPENCLAW_GATEWAY_URL) { $env:OPENCLAW_GATEWAY_URL = 'ws://127.0.0.1:18789' }; $env:OPENCLAW_AGENT_ID = 'sparky-chief-product-quality-officer'; $env:OPENCLAW_ALLOW_INSECURE_PRIVATE_WS = '1'; Set-Location $packet; node bot-telegram.js`
- Shell: `Start-Sleep -Seconds 3; Get-CimInstance Win32_Process -Filter "Name = 'node.exe'" | Where-Object { $_.CommandLine -like '*sparky-chief-product-quality-officer*' -or $_.CommandLine -like '*bot-telegram.js*' } | Select-Object ProcessId, CommandLine`
- Shell: `try { (Invoke-WebRequest -UseBasicParsing http://127.0.0.1:18792/ -TimeoutSec 5).Content } catch { Write-Error $_; exit 1 }`
- `functions.ReadLints`

### Changes

- Fixed a real first-run launch bug: the startup script was trying to invoke npm with PowerShell syntax that npm interpreted as bogus subcommands.
- Fixed a second live-start bug: the detached PowerShell here-string was expanding `$env:` too early, so the child process did not actually receive `TELEGRAM_BOT_TOKEN` / gateway env vars.
- Re-ran the real `-CeoOnly` path after both fixes; the script completed successfully and started the host-native CEO runtime.

### Evidence

- FAIL — first real `pwsh ... -CeoOnly` launch failed with:
  - `Unknown command: "npmCmd.Source"`
  - `npm install failed in D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer`
- FAIL — second real `pwsh ... -CeoOnly` launch failed with:
  - `Unknown command: "npmExecutable"`
- FAIL — third real `pwsh ... -CeoOnly` launch failed with:
  - `Unknown command: "pm"`
- FAIL — the direct foreground repro proved the detached env injection bug:
  - `Missing access token` from `bws`
  - `Error: Empty token!` from `grammy`
- PASS — after patching the npm invocation and escaping `$env:` in the detached launch command, `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly` returned:
  - `Host-native CEO Sparky ready: True`
  - `Started host-native CEO Sparky Telegram runtime from D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer.`
- PASS — process check returned a live Node process:
  - `ProcessId 41280`
  - `"C:\Program Files\nodejs\node.exe" bot-telegram.js`
- PASS — gateway health check `http://127.0.0.1:18792/` returned `OK`.
- PASS — `functions.ReadLints` reported no diagnostics after the launch-script fixes.

### Verdict

READY — `SPARKY_CEO_BOT` is now running as a live host-native Node process, and the local OpenClaw health endpoint is responding.

### Blockers

- Telegram smoke evidence is still pending because this block verified process/runtime health, not an actual message exchange from Telegram.

### Fallbacks Used

- Direct foreground execution of `node bot-telegram.js` was used as a debugging fallback when the detached host-native launch returned success but the process did not stay alive.

### Cross-Repo Impact

- None.

### Decisions Captured

- The detached host-native launcher must escape `$env:` assignments inside the PowerShell here-string; otherwise token injection silently breaks.
- First-run dependency bootstrap for the CEO packet should use a plain `npm install` invocation after command preflight.

### Pending Actions

- Send `/start` to `SPARKY_CEO_BOT` in Telegram and confirm a live reply.
- Send one normal message and, if needed, one elevated command to verify downstream agent routing.

### What Remains Unverified

- Live Telegram message handling for `SPARKY_CEO_BOT`.
- End-to-end downstream `openclaw` command execution after Telegram delivery.
- Whether the detached process survives a longer idle period without manual supervision.

### What's Next

- Perform the Telegram `/start` smoke test against the now-running `SPARKY_CEO_BOT`.

---

## 2026-04-12 18:21 - SPARKY_CEO_BOT Message Handoff Repaired

### Goal

Fix the remaining post-startup failure where `SPARKY_CEO_BOT` could answer `/start` but every normal message returned `Something went wrong. Please try again.`.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/openclaw-runner.js`
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `docs/ai/STATE.md`
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md`

### Commands / Tool Calls

- `functions.CallMcpTool` — `user-thinking-patterns.debugging_approach`
- `functions.ReadFile` — bot runtime logs and source files
- `functions.rg` — searched OpenClaw config path references
- Shell: `openclaw agent --agent sparky-chief-product-quality-officer --session-id debug-telegram --message "what is your job"`
- Shell: `openclaw agents list`
- Shell: `openclaw agent --agent main --session-id debug-main --message "what is your job"`
- Shell: `Get-Command openclaw | Select-Object Source, Name, CommandType | Format-List`
- Shell: `Get-ChildItem "$env:APPDATA\npm\openclaw*" | Select-Object Name, FullName | Format-Table -AutoSize`
- Shell: `node -e "const { runAgent } = require('./openclaw-runner'); ..."`
- Shell: `pwsh -NoProfile -File "$env:APPDATA\npm\openclaw.ps1" agent --agent main --session-id debug-pwsh-main --message "what is your job"`
- Shell: `$cmd = "$env:APPDATA\npm\openclaw.cmd"; cmd.exe /d /s /c "\"$cmd\" agent --agent main --session-id debug-cmd-main --message \"what is your job\""`
- Shell: `Get-CimInstance Win32_Process ...`
- Shell: `Stop-Process -Id ...`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`
- `functions.ApplyPatch`
- `functions.ReadLints`

### Changes

- Confirmed from the live bot log that the immediate failure was `spawn openclaw ENOENT`; the detached Node bot could not find/use the Windows OpenClaw launcher.
- Confirmed the second underlying issue that even when the CLI is available, this Windows machine only has `main` configured locally; the slug route `sparky-chief-product-quality-officer` is not registered in `C:\Users\ynotf\.openclaw\openclaw.json`.
- Patched `openclaw-runner.js` (and its generator source) so Windows uses the installed `openclaw.cmd` launcher via `child_process.exec`, not a bare `execFile("openclaw")`.
- Added a fallback so if a preferred agent id is unknown locally, the runtime retries through `main` instead of throwing back to Telegram.
- Updated the host-native Sparky launcher to set `OPENCLAW_AGENT_ID=main` on this Windows runtime, which matches the actual configured local agent and avoids a failing slug-route attempt on every message.
- Restarted the live `SPARKY_CEO_BOT` process so it loaded the patched runner.

### Evidence

- PASS — live bot log showed the exact Telegram handoff failure:
  - `Error: spawn openclaw ENOENT`
- FAIL — direct CLI repro for the slug route returned:
  - `Unknown agent id "sparky-chief-product-quality-officer"`
- PASS — `openclaw agents list` showed only:
  - `main (default)`
- PASS — `openclaw agent --agent main --session-id debug-main --message "what is your job"` returned a real assistant reply.
- PASS — `Get-Command openclaw` resolved to:
  - `C:\Users\ynotf\AppData\Roaming\npm\openclaw.ps1`
- PASS — installed Windows launchers exist:
  - `openclaw`
  - `openclaw.cmd`
  - `openclaw.ps1`
- FAIL — early Windows runner attempts showed quoting/launcher mismatches:
  - `error: too many arguments for 'agent'. Expected 0 arguments but got 3.`
  - `The network path was not found.`
- PASS — after switching the runner to `exec` with `openclaw.cmd`, the packet-local test succeeded:
  - `Same answer as before — I'm your AI assistant. Happy to help when you're ready. What do you need?`
- PASS — after restart, a fresh bot process is running:
  - `ProcessId 42008`
  - `"C:\Program Files\nodejs\node.exe" bot-telegram.js`
- PASS — `functions.ReadLints` reported no diagnostics on the patched files.

### Verdict

READY — the normal-message handoff path is now repaired, and the live bot process has been restarted with the patched Windows runner.

### Blockers

- Telegram smoke evidence after the final restart is still pending user confirmation.

### Fallbacks Used

- Used the live bot stderr log plus direct CLI reproductions instead of guessing from Telegram symptoms alone.
- Used the local `main` agent as the safe host-native fallback because this Windows runtime does not currently register a separate `sparky-chief-product-quality-officer` agent.

### Cross-Repo Impact

- None.

### Decisions Captured

- On this Windows host, the correct functional OpenClaw route for Sparky is `main` unless/until a dedicated `sparky-chief-product-quality-officer` agent is explicitly registered locally.
- Windows host-native bot runners should use the installed `openclaw.cmd` launcher via `exec`, not `execFile("openclaw")`.

### Pending Actions

- User sends one new normal message to `SPARKY_CEO_BOT` after the restart.
- If needed, verify one elevated/admin-style action after basic message replies are confirmed.

### What Remains Unverified

- The exact Telegram reply content after the final restart.
- Whether the local `main` agent persona is sufficiently aligned with the intended Sparky persona for longer conversations.

### What's Next

- User sends `/start` or a normal message to the freshly restarted `SPARKY_CEO_BOT` and reports the reply.

---

## 2026-04-12 18:42 - Sparky Continuity Layer Imported From `temp/Sparky`

### Goal

Upgrade live Sparky from a merely working Telegram bot into a stronger persistent executive packet by importing the highest-value continuity pieces from `D:\github\open--claw\temp\Sparky` and wiring the host-native runtime to use Sparky's own packet workspace.

### Scope

- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/README.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/BOOTSTRAP.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/AGENTS.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/MEMORY.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/HEARTBEAT.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/setup.sh`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/ONBOARDING.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/DECISION_LOG.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/live/SESSION-STATE.md`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/live/working-buffer.md`
- `docs/ai/HANDOFF.md`
- `docs/ai/STATE.md`
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md`

### Commands / Tool Calls

- `functions.Subagent` (`explore`) — audited `D:/github/open--claw/temp/Sparky`
- `functions.ReadFile` — inspected live Sparky packet files and selected `temp/Sparky` doctrine/continuity files
- `functions.Shell` — `Get-ChildItem -Name` in the live Sparky packet
- `functions.ApplyPatch`
- Shell: `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"`
- Shell: `Get-CimInstance Win32_Process -Filter "Name = 'node.exe'" | Where-Object { $_.CommandLine -like '*bot-telegram.js*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`
- `functions.ReadFile` — `...\.openclaw-runtime\config\openclaw.json`
- Shell: `$env:OPENCLAW_CONFIG_PATH='D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\.openclaw-runtime\config\openclaw.json'; openclaw agents list`
- Shell: `$env:OPENCLAW_CONFIG_PATH='D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\.openclaw-runtime\config\openclaw.json'; openclaw agent --agent main --session-id sparky-persona-test --message "who are you and what is your job"`
- Shell: `$env:OPENCLAW_CONFIG_PATH='D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\.openclaw-runtime\config\openclaw.json'; openclaw agent --agent sparky-chief-product-quality-officer --session-id sparky-slug-test --message "who are you and what is your job"`
- `functions.ReadLints`

### Changes

- Audited `temp/Sparky` and deliberately reused only the high-value low-conflict continuity pieces instead of overwriting live Sparky with the conflicting “Chief Governing Overseer” doctrine.
- Imported a live continuity layer into the production Sparky packet:
  - `ONBOARDING.md`
  - `DECISION_LOG.md`
  - `live/SESSION-STATE.md`
  - `live/working-buffer.md`
- Upgraded `README.md`, `BOOTSTRAP.md`, `AGENTS.md`, `MEMORY.md`, and `HEARTBEAT.md` so live Sparky now knows how to recover identity, session state, and durable decisions.
- Upgraded `setup.sh` and the generated Windows host-native startup path so Sparky now builds a packet-local OpenClaw config/workspace under `.openclaw-runtime/` and copies in the packet docs/skills before starting.
- Restored the dedicated Sparky agent route inside the packet-local config so the live runtime can use `sparky-chief-product-quality-officer` again while still remaining isolated from the generic Windows `~/.openclaw` workspace.
- Updated `docs/ai/HANDOFF.md` to reflect the new packet-local runtime and continuity layer.

### Evidence

- PASS — `temp/Sparky` exploration found a strong reusable continuity system but a conflicting core governance persona, so selective import was the safe path.
- PASS — `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"` succeeded after the generator update.
- PASS — `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly` restarted the live host-native Sparky runtime successfully.
- PASS — generated packet-local config exists at:
  - `D:\github\open--claw\open-claw\AI_Employee_knowledgebase\AI_employees\sparky-chief-product-quality-officer\.openclaw-runtime\config\openclaw.json`
- PASS — `openclaw agents list` with `OPENCLAW_CONFIG_PATH` set to that config now shows:
  - `main`
  - `sparky-chief-product-quality-officer`
- PASS — direct persona test through the packet-local config returned:
  - `I'm **Sparky** — the team's **Chief Product and Quality Officer**.`
- PASS — direct dedicated-agent test through `--agent sparky-chief-product-quality-officer` returned the same role-correct Sparky response, proving the dedicated packet-local route now works.
- PASS — live process check after the final restart returned a running `node bot-telegram.js` process.
- PASS — `functions.ReadLints` reported no diagnostics on the edited files.

### Verdict

READY — Sparky now has a packet-local continuity system and a packet-local OpenClaw runtime config, so the live bot can answer from Sparky's own identity and memory surface instead of the generic Windows workspace.

### Blockers

- Final user-visible Telegram smoke confirmation after the continuity/runtime upgrade is still pending.

### Fallbacks Used

- Reused selected continuity assets from `temp/Sparky` only; intentionally did not import its conflicting top-level persona/doctrine files wholesale.

### Cross-Repo Impact

- None.

### Decisions Captured

- `temp/Sparky` is now treated as a donor packet for continuity/runtime patterns, not as a wholesale replacement for live Sparky.
- The live host-native Sparky runtime should use a packet-local `.openclaw-runtime` config/workspace so packet docs actually shape the assistant's replies.
- The dedicated `sparky-chief-product-quality-officer` route is now valid again inside the packet-local config, even though the global Windows config still only exposes the generic local `main` agent.

### Pending Actions

- User sends a fresh Telegram message after the latest restart and confirms the upgraded Sparky reply quality.
- If needed later, import additional low-conflict `temp/Sparky` assets such as selected handoff templates or checklists.

### What Remains Unverified

- Long-session persistence quality after multiple Telegram conversations and a later restart.
- Whether additional `temp/Sparky` operational templates should be promoted into the live packet.

### What's Next

- User sends a fresh message to `SPARKY_CEO_BOT` and confirms whether the live reply now sounds like Sparky instead of a generic assistant.

---

## 2026-04-12 19:20 - Sparky Second-Wave Operational Supports Imported

### Goal

Promote a second wave of high-value low-conflict assets from `temp/Sparky` so live Sparky gains structured support surfaces for routing, review, release, and drift audits.

### Scope

- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/**`
- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/start-employees.ps1`

### Commands / Tool Calls

- `functions.ReadFile` — audited selected files under `temp/Sparky/HANDOFF_TEMPLATES` and `temp/Sparky/CHECKLISTS`
- `functions.ApplyPatch`
- Shell: `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"`
- Shell: `Get-CimInstance Win32_Process -Filter "Name = 'node.exe'" | Where-Object { $_.CommandLine -like '*bot-telegram.js*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`
- `functions.ReadLints`

### Changes

- Imported packet-local operational support directories into live Sparky:
  - `CHECKLISTS/`
  - `HANDOFF_TEMPLATES/`
- Added live packet files for:
  - PR review checklist
  - release gate checklist
  - drift audit checklist
  - specialist handoff templates for code review, security, data, DevOps/release, QA evidence, debugging, software architecture, and product management
- Updated `README.md` and `WORKFLOWS.md` so the live packet explicitly points Sparky to these support surfaces.
- Updated `BOOTSTRAP.md`, `DECISION_LOG.md`, and `live/SESSION-STATE.md` so Sparky's own continuity state reflects the packet-local runtime and new operational assets.
- Updated both the generator and the generated Windows startup script so packet-local runtime creation now copies `CHECKLISTS/` and `HANDOFF_TEMPLATES/` into `.openclaw-runtime/workspace/`.
- Updated `setup.sh` so the Linux/container install path copies the same directories.

### Evidence

- PASS — second-wave donor assets in `temp/Sparky` were operationally aligned and low-conflict, so they were safe to promote.
- PASS — `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"` succeeded after the second-wave runtime-copy update.
- PASS — `start-employees.ps1 -CeoOnly` restarted the host-native Sparky runtime after the second-wave import.
- PASS — packet-local runtime copy logic now includes both `CHECKLISTS/` and `HANDOFF_TEMPLATES/`.
- PASS — `functions.ReadLints` reported no diagnostics on the edited files.

### Verdict

READY — live Sparky now has reusable structured templates and checklists inside both the packet and the packet-local runtime, strengthening review discipline without replacing the established production persona.

### Blockers

- User-visible Telegram smoke confirmation after this second-wave restart is still pending.

### Decisions Captured

- `temp/Sparky` remains a donor packet; support surfaces can be promoted when they reinforce the live governance model without conflicting with live doctrine.
- Operational templates and checklists belong inside the packet-local runtime, not just the repo packet, so the running bot can actually use them.

### Pending Actions

- User sends a fresh Telegram message to `SPARKY_CEO_BOT` after this restart and confirms reply quality.
- If desired later, import a third wave such as selected eval artifacts or tighter routing policies.

---

## 2026-04-12 20:55 - Sparky Third-Wave Governance Bundle + Nerve Launcher Hardening

### Goal

Import a third wave of safe governance/evaluation assets from `temp/Sparky` into the live Sparky packet and harden the OpenClaw Nerve dashboard launcher after the user reported that the dashboard was not working.

### Scope

- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/**`
- `open-claw/scripts/sync_curated_employee_runtime.py`
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `open-claw/scripts/start-openclaw-nerve.ps1`
- `temp/openclaw-nerve/**` (runtime verification only)

### Commands / Tool Calls

- `functions.Subagent` (`explore`) — audited `temp/openclaw-nerve` and ranked third-wave donor candidates from `temp/Sparky`
- `functions.ReadFile` — reviewed donor governance docs, live packet docs, Nerve launcher, Vite config, server files, and dashboard hooks
- `functions.CallMcpTool` (`user-Context7`) — retrieved current Vite proxy docs and Hono static-serving docs
- `functions.ApplyPatch`
- Shell: `npm run build` in `temp/openclaw-nerve`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\scripts\start-openclaw-nerve.ps1"`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\scripts\start-openclaw-nerve.ps1" -Rebuild`
- Shell: `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`
- Shell: health checks against `http://127.0.0.1:3080/`, `/health`, and `/api/connect-defaults`
- `functions.ReadLints`

### Changes

- Imported an adapted third-wave governance bundle into the live Sparky packet:
  - `RUNBOOK.md`
  - `KNOWLEDGE_SOURCES.md`
  - `SOURCE_PRIORITY.md`
  - `RETRIEVAL_RULES.md`
  - `SUCCESS_METRICS.md`
  - `APPROVAL_GATES.md`
  - `PR_RULES.md`
  - `SPARKY_EVALUATION_SUMMARY.md`
  - `evals/README.md`
  - `evals/audits/case_01.md`
- Updated `README.md`, `WORKFLOWS.md`, `BOOTSTRAP.md`, `PROVENANCE.md`, `DECISION_LOG.md`, and `live/SESSION-STATE.md` so the live packet knows how these new governance surfaces fit under the charter-first authority model.
- Updated the generator, generated Windows startup script, and `setup.sh` so packet-local runtime creation now copies the third-wave top-level docs and `evals/` into `.openclaw-runtime/workspace/`.
- Hardened `open-claw/scripts/start-openclaw-nerve.ps1`:
  - resolves `npm` from PATH instead of relying only on one fixed install path
  - can rebuild when artifacts are missing or `-Rebuild` is requested
  - uses `/health` probing instead of fragile process-name heuristics
  - reports dashboard readiness explicitly
- Fixed a real regression introduced during launcher hardening: `npm run build` was initially executed from the repo root instead of the Nerve app directory, which caused `ENOENT` on `package.json`; the launcher now runs the build from `temp/openclaw-nerve`.

### Evidence

- PASS — Context7-confirmed Vite proxy behavior supports the existing `/api` and `/ws` pattern as long as the backend server is actually running on the target port.
- PASS — Context7-confirmed Hono static serving pattern matches the current Nerve app's dist-file + SPA fallback approach.
- PASS — `npm run build` in `temp/openclaw-nerve` completed successfully.
- PASS — local Nerve endpoints responded successfully after launcher verification:
  - `/` returned HTTP `200`
  - `/health` returned `{"status":"ok","gateway":"ok",...}`
  - `/api/connect-defaults` returned loopback WS defaults with `serverSideAuth: true`
- PASS — launcher hardening caught a real path bug during `-Rebuild`; that bug was fixed and the launcher then completed successfully.
- PASS — `python -m py_compile "D:\github\open--claw\open-claw\scripts\sync_curated_employee_runtime.py"` succeeded after the third-wave runtime-copy update.
- PASS — `start-employees.ps1 -CeoOnly` restarted the host-native Sparky runtime successfully after the third-wave import.
- PASS — packet-local runtime workspace now contains the new governance docs and `evals/`.
- PASS — `functions.ReadLints` reported no diagnostics on the edited files.

### Verdict

READY — live Sparky now has a deeper governance bundle and evaluation surface inside both the repo packet and the packet-local runtime, and the Nerve dashboard launch path is hardened with verified health-based startup behavior.

### Blockers

- User-visible Telegram smoke confirmation after this third-wave restart is still pending.
- User-visible browser smoke confirmation of the Nerve dashboard UI is still pending even though server health and bootstrap endpoints are passing locally.

### Decisions Captured

- Third-wave imports should favor governance procedure, retrieval discipline, metrics, and eval scenarios over donor persona/doctrine files.
- Nerve launcher health should be determined by explicit HTTP readiness, not by command-line process matching alone.

### Pending Actions

- User sends a fresh Telegram message to `SPARKY_CEO_BOT` and confirms reply quality after the third-wave restart.
- User opens `http://127.0.0.1:3080` and confirms the Nerve dashboard UI is working end-to-end.

---

## 2026-04-12 21:05 - Live Sparky Runtime Restarted After Telegram Silence

### Goal

Recover `SPARKY_CEO_BOT` after the user reported that Sparky was not responding.

### Scope

- host-native `SPARKY_CEO_BOT` runtime
- `open-claw/employees/deployed-curated/start-employees.ps1`
- `open-claw/AI_Employee_knowledgebase/AI_employees/sparky-chief-product-quality-officer/live/SESSION-STATE.md`

### Commands / Tool Calls

- `functions.ReadFile` — checked open terminal output and live Sparky session-state file
- Shell: process check for `bot-telegram.js`
- Shell: gateway health check on `http://127.0.0.1:18789/health`
- Shell: `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed-curated\start-employees.ps1" -CeoOnly`
- Shell: post-restart process check and short soak check

### Changes

- Confirmed the OpenClaw gateway was healthy but the host-native `bot-telegram.js` process was not running.
- Restarted the host-native CEO Sparky runtime using the supported startup script.
- Updated `live/SESSION-STATE.md` so the packet-local runtime state records that the Telegram bot was found down and restarted successfully.

### Evidence

- PASS — gateway health returned `{"ok":true,"status":"live"}`
- PASS — pre-restart process check found no running `bot-telegram.js` process
- PASS — `start-employees.ps1 -CeoOnly` relaunched the host-native CEO runtime successfully
- PASS — post-restart process check showed a live `node bot-telegram.js` process
- PASS — short soak check confirmed the process remained alive after restart

### Verdict

RECOVERED — Sparky silence was caused by the host-native Telegram runtime being down, and the runtime is now back up.

### Pending Actions

- User sends a fresh Telegram message to `SPARKY_CEO_BOT` and confirms live reply behavior after the restart.

---

## 2026-04-13 14:40 - OpenClaw Updated To 2026.4.12

### Goal

Update the installed OpenClaw CLI/runtime to the newest stable release.

### Scope

- Global OpenClaw package install on Windows
- Live gateway/runtime verification

### Commands / Tool Calls

- Shell: `openclaw --version`
- Shell: `Get-Command openclaw | Format-List Name,Source,Version`
- Web search for latest published OpenClaw release/package version
- Context7: `/openclaw/openclaw` update documentation
- Shell: `openclaw update status`
- Shell: `openclaw update --dry-run --json`
- Shell: `openclaw update --yes`
- Shell: `openclaw doctor`
- Shell: `openclaw health`
- Shell: gateway health probe on `http://127.0.0.1:18789/health`

### Changes

- Updated the globally installed OpenClaw package from `2026.3.13` to `2026.4.12`.
- Confirmed the installed CLI binary is the npm-global Windows install at:
  - `C:\Users\ynotf\AppData\Roaming\npm\openclaw.ps1`
- Verified the CLI is now up to date on the stable channel.

### Evidence

- PASS — pre-update CLI version: `OpenClaw 2026.3.13 (61d171a)`
- PASS — latest published npm stable version resolved as `2026.4.12`
- PASS — `openclaw update --dry-run --json` showed a package-mode global update from `2026.3.13` to `2026.4.12`
- PASS — `openclaw update --yes` completed successfully:
  - Before: `2026.3.13`
  - After: `2026.4.12`
- PASS — post-update CLI version: `OpenClaw 2026.4.12 (1c0672b)`
- PASS — gateway health remained live after the update:
  - `http://127.0.0.1:18789/health` -> `{"ok":true,"status":"live"}`
- PASS — `openclaw update status` now reports `up to date`

### Findings

- WARN — updater could not restart a managed gateway service because no registered `OpenClaw Gateway` scheduled task/service exists on this machine.
- WARN — `openclaw doctor` reports `gateway.mode` unset, which means managed `gateway start` is currently under-configured even though the live gateway is up right now.
- WARN — `openclaw doctor` / `openclaw health` report the configured Telegram channel as `401 Unauthorized`.

### Verdict

UPDATED WITH FOLLOW-UP — OpenClaw itself is now on `2026.4.12` and the live gateway is still healthy, but the managed restart path and the configured Telegram channel both still need cleanup.

### Pending Actions

- If desired, install or repair the managed gateway service/task so future updates can restart it automatically.
- Repair the failing Telegram channel auth reported by `openclaw doctor` if that channel is still expected to be active.

---

## 2026-04-13 15:05 - Gateway Startup Wrapper Added; Stale Telegram Channel Disabled

### Goal

Handle the two post-update follow-ups:
1. repair the managed startup path for the live gateway runtime
2. resolve the Telegram `401 Unauthorized` failure or, if the token is invalid, stop the live gateway from looping on a broken Telegram account

### Scope

- Windows OpenClaw client config at `C:\Users\ynotf\.openclaw\openclaw.json`
- WSL gateway config at `\\wsl.localhost\Ubuntu\home\ynotf\.openclaw\openclaw.json`
- WSL env files under `~/.openclaw/`
- WSL user service `openclaw-gateway.service`
- Windows scheduled task `OpenClaw Gateway`

### Commands / Tool Calls

- Context7: WSL gateway managed startup docs + Telegram channel repair docs
- Shell: `openclaw gateway --help`, `openclaw channels --help`, `openclaw config --help`
- Shell: `openclaw channels status --probe --json`
- Shell: `openclaw channels logs --channel telegram --lines ...`
- Shell: `openclaw gateway status`
- `functions.ReadFile` — Windows and WSL OpenClaw config + WSL systemd unit files
- Shell: WSL service status / journal inspection
- Shell: Bitwarden secret fetch for `SECRETARY_STACY_BOT` UUID `2733f3f8-964b-4cb6-be93-b42a0120b0b9`
- Shell: direct Telegram Bot API `getMe` validation using that secret (no secret printed)
- Shell: scheduled-task registration and run
- Shell: WSL gateway service restart + re-probe

### Changes

- Verified the real live gateway is a WSL user service, not a native Windows gateway:
  - `openclaw-gateway.service` was already `enabled` and `active`
  - WSL has `systemd=true`
- Added a Windows scheduled task named `OpenClaw Gateway` that runs:
  - `wsl.exe -d Ubuntu -- bash -lc "systemctl --user start openclaw-gateway.service"`
  This gives the Windows-side updater a valid on-demand/logon startup wrapper for the actual WSL gateway runtime.
- Set Windows `gateway.mode=local` so the local CLI no longer remains completely unconfigured.
- Refreshed WSL `TELEGRAM_BOT_TOKEN` from the documented Bitwarden `SECRETARY_STACY_BOT` secret and restarted the gateway service.
- Verified the refreshed Bitwarden secret itself is invalid against Telegram (`getMe` returns HTTP `401`), so a direct Telegram repair was not possible from existing stored credentials.
- Applied the safe fallback: disabled the stale WSL Telegram channel in `~/.openclaw/openclaw.json` and restarted the WSL gateway service, which stopped the repeated Telegram restart/error loop.

### Evidence

- PASS — WSL gateway service status:
  - `enabled`
  - `active`
- PASS — Windows task `OpenClaw Gateway` now exists and runs successfully with `Last Result: 0`
- PASS — direct gateway health remained live throughout:
  - `http://127.0.0.1:18789/health` -> `{"ok":true,"status":"live"}`
- PASS — WSL Telegram failure was traced to the live gateway service journal:
  - `deleteWebhook failed ... (401: Unauthorized)`
- PASS — direct Bot API validation of the documented `SECRETARY_STACY_BOT` Bitwarden secret returned `401`, proving the stored secret itself is stale/invalid
- PASS — after disabling the stale Telegram channel and restarting the WSL gateway, channel status now reports:
  - Telegram account `enabled: false`
  - lastError: `disabled`
  instead of repeated `401 Unauthorized`

### Findings

- WARN — the Bitwarden secret currently documented for `SECRETARY_STACY_BOT` is invalid and cannot restore Telegram until it is replaced with a fresh BotFather token.
- WARN — Windows `openclaw gateway status` still cannot fully model the live WSL service because the scheduled task is only a wrapper that starts the real WSL systemd unit and then exits.
- WARN — WhatsApp also showed `401 Unauthorized` during the WSL gateway restart sequence and remains a separate channel-auth issue.

### Verdict

PARTIAL FIX WITH SAFE FALLBACK — the gateway startup path is now wrapped for Windows-triggered startup and the real WSL service remains healthy, but the old Telegram secret is invalid, so the broken Telegram channel was disabled to stop restart loops until a fresh token is provided.

### Pending Actions

- Provide a fresh BotFather token for `SECRETARY_STACY_BOT` or update that Bitwarden secret, then re-enable the Telegram channel.
- If desired, repair the WhatsApp `401 Unauthorized` state as a separate follow-up.

---

## 2026-04-13 15:15 - Correct Gateway Secret Source Rechecked Against Inventory

### Goal

Correct the gateway-secret reference after user feedback and verify the Windows OpenClaw client was using the canonical Bitwarden inventory entry for gateway auth.

### Scope

- `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- Windows OpenClaw client config at `C:\Users\ynotf\.openclaw\openclaw.json`

### Commands / Tool Calls

- `functions.ReadFile` — read the canonical Bitwarden inventory entry for `OPENCLAW_GATEWAY_TOKEN`
- Shell: Bitwarden fetch using UUID `79f3acf8-c855-4c0d-9726-b40d01278bb6`
- Shell: refreshed Windows `gateway.auth.token` from that Bitwarden secret
- Shell: `openclaw gateway call health`

### Changes

- Replaced the Windows OpenClaw client gateway token with the canonical Bitwarden secret resolved from the inventory entry:
  - `OPENCLAW_GATEWAY_TOKEN`
  - UUID `79f3acf8-c855-4c0d-9726-b40d01278bb6`

### Evidence

- PASS — canonical inventory confirms `OPENCLAW_GATEWAY_TOKEN` as the gateway auth secret
- PASS — Windows client config was refreshed from that exact Bitwarden secret
- WARN — `openclaw gateway call health` still returns `pairing required`, so the remaining Windows CLI ↔ WSL gateway issue is not caused by the earlier wrong-secret reference alone

### Verdict

CORRECTED — the gateway secret source is now aligned to the inventory, but an additional pairing/approval problem still exists for the Windows CLI path.

---

## 2026-04-13 15:20 - Windows CLI Pairing Repaired Against Live WSL Gateway

### Goal

Resolve the remaining Windows CLI `pairing required` failure against the live WSL gateway after correcting the gateway secret source.

### Scope

- Windows OpenClaw local identity under `C:\Users\ynotf\.openclaw\identity\`
- WSL gateway device table
- WSL gateway service journal

### Commands / Tool Calls

- Shell: `openclaw devices --help`
- Shell: `wsl -d Ubuntu -- bash -lc "cd ~/openclaw-build && pnpm openclaw devices list --json"`
- Shell: `wsl -d Ubuntu -- bash -lc "cd ~/openclaw-build && pnpm openclaw devices approve <requestId> --json"`
- Shell: `openclaw gateway call health`
- Shell: `openclaw devices list --json`
- Shell: WSL gateway journal review after approval
- `functions.rg` / `functions.Glob` — verified Windows local device identity files

### Changes

- Confirmed the Windows local device identity matches:
  - device id `891178e980ebe57e373035ebbfc10162d228f649b46aeda07b1ff8696492f112`
  - public key associated with the local Windows OpenClaw identity files
- Identified a pending repair/upgrade request on the live WSL gateway for that exact Windows device:
  - `clientId=cli`
  - `clientMode=cli`
  - requested role upgrade from `node` to `operator`
- Approved the pending device request on the WSL gateway host.

### Evidence

- PASS — gateway device table showed a pending request for the exact Windows device id used by the local CLI
- PASS — approval succeeded and the device now holds both:
  - `node`
  - `operator`
  roles, with operator scopes including `operator.read`, `operator.write`, `operator.admin`, `operator.approvals`, `operator.pairing`, and `operator.talk.secrets`
- PASS — post-approval Windows RPC succeeded:
  - `openclaw gateway call health`
  - returned `{"ok": true, ...}`
- PASS — `openclaw status` from Windows now shows:
  - gateway reachable
  - live WSL gateway self identity
  - channel/state summary through the gateway

### Findings

- The root cause of the remaining Windows CLI failure was not the corrected gateway secret anymore; it was an outstanding device pairing/role-upgrade request waiting in the WSL gateway device table.
- The live gateway journal now records the device approval for the Windows CLI identity.

### Verdict

FIXED — the Windows CLI is now paired/approved against the live WSL gateway and can make authenticated gateway RPC calls successfully.

### Pending Actions

- Telegram remains intentionally disabled until a fresh valid BotFather token is provided for the stale `SECRETARY_STACY_BOT` secret.
- WhatsApp remains a separate `401 Unauthorized` channel-auth issue and still needs relinking if you want that channel healthy again.

---

## 2026-04-13 16:40 - BotFather Username Slugs Canonicalized; SPARKY_CEO_BOT Made Default

### Goal

Use the BotFather bot roster as the canonical public identity list, make BotFather `@usernames` the canonical employee slugs, and make `SPARKY_CEO_BOT` the true default/top OpenClaw agent.

### Scope

- BotFather screenshots supplied by the user as canonical bot roster
- `open-claw/scripts/sync_curated_employee_runtime.py`
- Generated curated status/runtime artifacts
- Live WSL OpenClaw gateway config
- Host-native Sparky launcher/runtime

### Commands / Tool Calls

- `functions.ReadFile` — read both BotFather screenshots and extracted the 16 canonical bots
- `functions.ReadFile` / `functions.rg` — audited slug, username, and startup references across `open-claw`
- Shell: compiled and regenerated `sync_curated_employee_runtime.py`
- Shell: patched live WSL `~/.openclaw/openclaw.json` agent list/default
- Shell: restarted the WSL gateway service
- Shell: relaunched host-native Sparky via `start-employees.ps1 -CeoOnly`
- Shell: verified gateway health/default agent and host-native runtime config

### Changes

- Canonicalized public employee slugs to BotFather `@usernames` in the generated curated runtime/status artifacts.
- Added the 16-bot BotFather roster as a machine-readable canonical list, including:
  - 15 assigned curated employee bots
  - `destiny_stripper_bot` as an unassigned extra bot from the BotFather list
- Updated generated Sparky/runtime artifacts so:
  - `SPARKY_CEO_BOT` is the host-native CEO slug/agent id
  - packet-local Sparky OpenClaw config marks `SPARKY_CEO_BOT` as the default agent
  - `openclaw-runner.js` now defaults to each employee's canonical BotFather slug instead of falling back to `main`
- Patched the host-native Sparky launch guard so it correctly detects an already-running `bot-telegram.js` process and avoids accidental duplicate launches.
- Patched the live WSL OpenClaw gateway config so the global default agent is now `SPARKY_CEO_BOT`, with `main` retained as a non-default compatibility agent.
- Left the gateway's built-in Telegram channel disabled on purpose so it does not compete with the host-native `SPARKY_CEO_BOT` process for the same Telegram bot token.

### Compatibility Decision

- Public/canonical slug: BotFather `@username`
- Compatibility path retained: existing packet directory names like `sparky-chief-product-quality-officer`

This keeps user-facing/runtime identity aligned to BotFather while avoiding a high-risk filesystem migration in the middle of live runtime repair.

### Evidence

- PASS — `CURATED_TEAM_STATUS.json` now reports:
  - canonical employee slugs like `SPARKY_CEO_BOT`, `DELIVERY_DIRECTOR_DAN_BOT`, `CODE_CARL_BOT`, etc.
  - `canonical_botfather_count: 16`
  - canonical BotFather roster entries, including unassigned `destiny_stripper_bot`
- PASS — generated Sparky packet-local OpenClaw config now marks:
  - `main` as `default: false`
  - `SPARKY_CEO_BOT` as `default: true`
- PASS — live WSL gateway config now contains:
  - `main` as non-default
  - `SPARKY_CEO_BOT` as default
- PASS — `openclaw gateway call health` now reports Sparky as the default agent
  - note: OpenClaw normalizes the reported gateway id to lowercase/underscore form in health output
- PASS — host-native Sparky launcher preflight passes and the bot was relaunched on the corrected canonical identity

### Findings

- The user was correct that the canonical slug should be the BotFather `@username`, not the old internal hyphenated role name.
- The old `sparky-chief-product-quality-officer` identifier was still useful as a packet-directory compatibility key, but it should no longer be treated as the public slug.
- The built-in gateway Telegram channel should remain disabled while the host-native Sparky bot owns the same Telegram token.

### Verdict

FIXED — the generated curated runtime now uses BotFather usernames as canonical slugs, `SPARKY_CEO_BOT` is the live default/top OpenClaw agent, and the host-native Sparky runtime has been restarted on that corrected identity.

## 2026-04-13 18:47 - Phase 1 Recovery Governance Alignment Mirror

### Goal

Mirror the minimum required recovery-governance and worker-memory alignment changes from AI-PM into `open--claw` without changing runtime/product behavior.

### Scope

- `AGENTS.md`
- `.cursor/rules/05-global-mcp-usage.md`
- `.cursor/rules/10-project-workflow.md`
- `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`
- `docs/ai/memory/MEMORY_CONTRACT.md`
- `open-claw/AI_Employee_knowledgebase/MEMORY_PROMOTION_TEMPLATE.md`
- `open-claw/AI_Employee_knowledgebase/TEAM_OPERATING_SYSTEM.md`
- `docs/ai/HANDOFF.md`

### Commands / Tool Calls

- `ReadFile`: targeted `open--claw` governance/memory docs plus `STATE.md`, `HANDOFF.md`, and ledger tail
- `ApplyPatch`
- `ReadLints`
- `Shell`: `git status --short -- "AGENTS.md" ".cursor/rules/05-global-mcp-usage.md" ".cursor/rules/10-project-workflow.md" "docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md" "docs/ai/memory/MEMORY_CONTRACT.md" "open-claw/AI_Employee_knowledgebase/MEMORY_PROMOTION_TEMPLATE.md" "open-claw/AI_Employee_knowledgebase/TEAM_OPERATING_SYSTEM.md" "docs/ai/HANDOFF.md"`
- `Shell`: `git diff --stat -- "AGENTS.md" ".cursor/rules/05-global-mcp-usage.md" ".cursor/rules/10-project-workflow.md" "docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md" "docs/ai/memory/MEMORY_CONTRACT.md" "open-claw/AI_Employee_knowledgebase/MEMORY_PROMOTION_TEMPLATE.md" "open-claw/AI_Employee_knowledgebase/TEAM_OPERATING_SYSTEM.md" "docs/ai/HANDOFF.md"`

### Changes

- Updated `open--claw` recovery guidance so bootstrap now routes through the charter, repo authority docs, targeted OpenMemory search, and the non-canonical recovery bundle before `STATE.md`.
- Mirrored the degraded-tool policy so required-tool failures must be announced explicitly instead of being silently bypassed.
- Updated `docs/ai/memory/MEMORY_CONTRACT.md` to reflect the flat Cursor OpenMemory surface.
- Updated worker memory-promotion docs so future durable memory entries stay compact and self-identifying instead of relying on unsupported hidden filters.
- Updated `docs/ai/HANDOFF.md` read order and blocker language to match the new recovery contract.

### Evidence

- PASS — `ReadLints` reported no diagnostics for the touched `open--claw` docs/rules.
- PASS — `git status --short -- ...` showed only the intended mirrored governance/memory files as modified or already-untracked for this scope.
- PASS — `git diff --stat -- ...` showed the expected mirror-only change footprint across the targeted files.

### Verdict

READY — the required `open--claw` mirror alignment for phase 1 is complete and remains docs-only.

### Blockers

None.

### Fallbacks Used

- None.

### Cross-Repo Impact

- This mirrors the canonical recovery-policy rewrite completed in `AI-Project-Manager`.

### Decisions Captured

- `open--claw` now follows the same charter-first, authority-contract-first recovery order as AI-PM.
- Worker memory promotion must use compact self-identifying text because the current Cursor OpenMemory surface is flat.

### Pending Actions

- Let a future phase generate and prove the live machine-local recovery bundle flow owned by the AI-PM workflow layer.

### What Remains Unverified

- No live runtime or product behavior was re-tested in this mirror pass.
- The recovery bundle is specified at the workflow layer but not yet live-generated.
- Untouched docs outside this scoped mirror set may still contain older bootstrap wording.

### What's Next

Use the updated AI-PM recovery contract for the next PLAN/AGENT cycle and defer any broader stale-doc sweep until a later harmonization phase.

## 2026-04-13 19:14 - Phase 2 Recovery Bundle Mirror

### Goal

Mirror only the minimum `open--claw` guidance needed so crash recovery points at the now-materialized AI-PM recovery bundle.

### Scope

`AGENTS.md`, `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`, and `docs/ai/HANDOFF.md` in `open--claw`.

### Commands / Tool Calls

- `ReadFile`
- `ApplyPatch`
- `ReadLints`
- `Shell`: `git status --short -- "AGENTS.md" "docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md" "docs/ai/HANDOFF.md"`
- `Shell`: `git diff --stat -- "AGENTS.md" "docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md" "docs/ai/HANDOFF.md"`

### Changes

- Updated `AGENTS.md` and `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` so recovery now points to `D:/github/AI-Project-Manager/docs/ai/recovery/*`.
- Updated `docs/ai/HANDOFF.md` so it no longer claims the bundle is missing and instead records the narrower remaining refresh-proof risk.

### Evidence

- PASS — `ReadLints` reported no diagnostics for the touched mirror files.
- PASS — `git status --short -- ...` showed only the intended mirror-scope file changes.
- PASS — `git diff --stat -- ...` showed the expected minimal mirror footprint.

### Verdict

READY — the required `open--claw` mirror guidance is aligned to the live AI-PM recovery bundle.

### Blockers

None.

### Fallbacks Used

- None.

### Cross-Repo Impact

- This mirror depends on the AI-PM-owned recovery bundle at `D:/github/AI-Project-Manager/docs/ai/recovery/`.

### Decisions Captured

- `open--claw` should consume the AI-PM recovery bundle as its first filesystem recovery surface before broader repo reads.

### Pending Actions

- Re-verify on a later independent session that the AI-PM recovery bundle continues to refresh after new work.

### What Remains Unverified

- No runtime or product behavior was re-tested in this mirror pass.
- The AI-PM bundle refresh path is materialized but not yet proven on a later unrelated execution block.

### What's Next

Use OpenMemory plus the AI-PM recovery bundle first on the next `open--claw` recovery-oriented PLAN/AGENT session.

### Pending Actions

- If desired later, perform a full filesystem-level directory rename away from legacy packet directory names. This is not required for the live runtime to work and was intentionally deferred for safety.
- WhatsApp remains out of scope for this pass.
