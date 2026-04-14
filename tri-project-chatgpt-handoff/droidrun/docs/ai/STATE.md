<!-- markdownlint-disable MD024 -->

# DroidRun Project State

> **Authority note**: This file is operational evidence only. It is not product law. The supreme governing charter is `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. If this file conflicts with the charter, the charter wins. `droidrun` is the actuator layer — it executes; it does not govern.

## 2026-04-01 — Non-Routable Quarantine System Installed (Prompt 8) — Cross-Repo Impact

### Goal

Apply the tri-workspace quarantine pass to droidrun to prevent iOS out-of-scope material from entering routing, search, memory, or embeddings flows. droidrun is the Android-only actuator layer; iOS paths are permanently non-routable.

### Scope

- `droidrun/.cursor/rules/02-non-routable-exclusions.md` — mirror enforcement rule (new)
- `droidrun/.cursor/rules/openmemory.mdc` — memory exclusions added
- `droidrun/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` — quarantine block added to PLAN and AGENT tabs
- `droidrun/src/droidrun/tools/driver/ios.py` — `# NON-ROUTABLE — OUT OF SCOPE` banner prepended
- `droidrun/src/droidrun/tools/ui/ios_provider.py` — `# NON-ROUTABLE — OUT OF SCOPE` banner prepended
- `droidrun/src/droidrun/tools/ios/__init__.py` — `# NON-ROUTABLE — OUT OF SCOPE` banner prepended
- `droidrun/docs/ai/STATE.md` — this entry

### Commands / Tool Calls

- Write: Created `02-non-routable-exclusions.md` with alwaysApply: true, excluding iOS paths and candidate_employees/** from search, memory, embeddings, routing — PASS
- StrReplace: Updated `openmemory.mdc` with iOS path and candidate_employees/** memory exclusions — PASS
- StrReplace: Updated `TAB_BOOTSTRAP_PROMPTS.md` — quarantine notice block added to PLAN and AGENT tabs — PASS
- StrReplace: Prepended `# NON-ROUTABLE — OUT OF SCOPE` to `ios.py`, `ios_provider.py`, `ios/__init__.py` — PASS
- Write: Updated `docs/ai/STATE.md` — PASS

### Changes

- Created `.cursor/rules/02-non-routable-exclusions.md`: alwaysApply: true; excludes `src/droidrun/tools/driver/ios.py`, `src/droidrun/tools/ui/ios_provider.py`, `src/droidrun/tools/ios/` and `candidate_employees/**` from search, memory, embeddings, routing
- Updated `.cursor/rules/openmemory.mdc`: memory exclusions for iOS paths and candidate_employees/**
- Updated `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`: quarantine notice block surfaced in PLAN and AGENT tab bootstrap reads
- Prepended `# NON-ROUTABLE — OUT OF SCOPE` to 3 iOS source files; files not deleted

### Evidence

- PASS: `02-non-routable-exclusions.md` created with alwaysApply: true
- PASS: `openmemory.mdc` updated with iOS and candidate_employees/** exclusions
- PASS: `TAB_BOOTSTRAP_PROMPTS.md` updated in PLAN and AGENT tabs
- PASS: 3 iOS files bannered via StrReplace — not deleted
- PASS: `docs/ai/STATE.md` updated
- PASS: FINAL_OUTPUT_PRODUCT.md not modified

### Verdict

READY — iOS quarantine active. droidrun confirmed as Android-only actuator layer. Memory, search, routing, and embeddings exclusions enforced at rule layer and openmemory.mdc.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

open--claw: canonical quarantine registry `NON_ROUTABLE_QUARANTINE.md` created; `02-non-routable-exclusions.md` created; 2,608 candidate_employees files bannered; knowledgebase docs updated; TAB_BOOTSTRAP_PROMPTS.md updated.
AI-Project-Manager: `02-non-routable-exclusions.md` created; `openmemory.mdc` updated; `TRI_WORKSPACE_CONTEXT_BRIEF.md` updated.

### Decisions Captured

- droidrun iOS paths (`src/droidrun/tools/driver/ios.py`, `src/droidrun/tools/ui/ios_provider.py`, `src/droidrun/tools/ios/`) are permanently non-routable.
- Canonical source of truth for all quarantine status decisions: `open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`.
- Quarantine is banner-only — no deletions.

### Pending Actions

- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` and `docs/ai/context/archive/` do not exist in droidrun yet — create when the first droidrun AGENT block appends a ledger entry.

### What Remains Unverified

- openmemory.mdc exclusions require a live memory search test to confirm iOS and candidate_employees paths are excluded.
- TAB_BOOTSTRAP_PROMPTS.md quarantine block: not tested in a live Cursor session to confirm it surfaces correctly on session start.

### What's Next

Proceed to next planned prompt block. Create `docs/ai/context/` structure on next droidrun AGENT block.

## 2026-03-31 — Charter Enforcement Kernel Installed (Reconciliation Pass)

- **Goal**: Install enforcement kernel in droidrun so charter violations are blocked by rules, not described only in docs.
- **Files created**: `.cursor/rules/01-charter-enforcement.md` — PASS
- **Files updated**: `AGENTS.md`, `.cursor/rules/00-global-core.md`, `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` (all five tabs), `docs/ai/STATE.md` — PASS
- **FINAL_OUTPUT_PRODUCT.md**: not modified — PASS
- **Verdict**: PASS — Enforcement kernel active. Forbidden platforms (macOS/iOS/Swift/Xcode/CocoaPods) blocked at rule layer. Violations route to Sparky.
- **Cross-repo**: Same pass applied in AI-Project-Manager and open--claw.

---

## 2026-03-15 — Documentation System Generated

- **39 new documentation files** created in `/docs/`
- **Total: 40 files, 383 KB** of machine+human readable docs
- **AI Handoff summary**: `docs/ai-handoff-summary.md` (start here for AI-Project-Manager)
- **Master index**: `docs/PROJECT_INTELLIGENCE_INDEX.md`
- **Machine-readable**: `docs/project-context.json`
- All checklist items marked complete in `docs/DOCS_CHECKLIST.md`

---

**Last updated:** 2026-03-15 (documentation run)  
**Status:** COMPLETE — fully operational + full documentation system generated

---

## What's Working

| Component            | Status | Details                                                   |
| -------------------- | ------ | --------------------------------------------------------- |
| DroidRun install     | ✅     | v0.5.1 in `.venv`, source at `src/`                       |
| Phone connection     | ✅     | Samsung S25 Ultra via Tailscale `100.71.228.18:5555`      |
| DroidRun Portal      | ✅     | v0.6.1, accessibility service enabled                     |
| DeepSeek (no vision) | ✅     | `droidrun_run.ps1 -Task "..."`                            |
| OpenRouter vision    | ✅     | `droidrun_run.ps1 -Task "..." -Vision` (Gemini 2.0 Flash) |
| MCP server           | ✅     | `mcp_server.py` — phone_do / phone_ping / phone_apps      |
| Cursor MCP           | ✅     | Added to `~/.cursor/mcp.json`                             |
| OpenClaw MCP         | ✅     | Added to `~/.openclaw/openclaw.json`                      |
| Claude Desktop MCP   | ✅     | Added to `%APPDATA%/Claude/claude_desktop_config.json`    |
| API key security     | ✅     | Bitwarden Secrets Manager → Windows user env vars         |

---

## Key Details

| Item           | Value                                                 |
| -------------- | ----------------------------------------------------- |
| Phone          | Samsung Galaxy S25 Ultra (SM-S938U)                   |
| Phone serial   | R5CY51LWKCR                                           |
| Tailscale IP   | 100.71.228.18 (stable)                                |
| ADB port       | 5555 (fixed via `adb tcpip 5555`)                     |
| ADB forward    | `adb -s 100.71.228.18:5555 forward tcp:8080 tcp:8080` |
| Python         | 3.12.10                                               |
| DroidRun       | 0.5.1                                                 |
| Portal         | 0.6.1                                                 |
| ADB            | 1.0.41 at C:\platform-tools                           |
| Tailscale (PC) | 1.94.2                                                |

---

## Bitwarden Setup

| Item               | Location                                              |
| ------------------ | ----------------------------------------------------- |
| DEEPSEEK_API_KEY   | Secrets Manager, DroidRun project, ID: `14d69c11-...` |
| OPENROUTER_API_KEY | Secrets Manager, DroidRun project, ID: `f9ed80a7-...` |
| BWS machine token  | Password Manager, item: `BWS_DROIDRUN_TOKEN`          |
| Windows env vars   | `DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY`    |

---

## Scripts Reference

| Script                              | Purpose                                                |
| ----------------------------------- | ------------------------------------------------------ |
| `scripts/droidrun_run.ps1`          | Main run script (auto-selects provider)                |
| `scripts/reconnect_remote.ps1`      | Smart reconnect after reboot                           |
| `scripts/adb_find_port.ps1`         | Auto-discover wireless debug port                      |
| `scripts/store_api_keys_to_env.ps1` | Cache keys to Windows env (run after rotation)         |
| `scripts/start_mcp_server.ps1`      | MCP server launcher (called by Cursor/OpenClaw/Claude) |
| `scripts/adb_status.ps1`            | Show ADB device status                                 |
| `scripts/droidrun_ping.ps1`         | Ping DroidRun portal                                   |

---

## Pending After Cursor Restart

- [ ] Run `.\scripts\store_api_keys_to_env.ps1` in PowerShell (needs master password)
- [ ] Verify Cursor MCP shows `droidrun` in MCP servers list
- [ ] Verify OpenClaw can call `phone_do` tool
- [ ] Test MCP by asking Cursor: "use phone_do to open the camera"

---

## Known Issues / Notes

- ADB port 5555 resets on phone reboot → run `reconnect_remote.ps1`
- DeepSeek doesn't support vision (image_url format) → use `-Vision` flag for OpenRouter
- `adb forward tcp:8080 tcp:8080` must be run after every new ADB connection
- OpenClaw uses Grok-4 by default + WhatsApp channel on +15614193784

---

## 2026-03-19 18:07 - Governance Sync: AI-PM Canonical Authority

### Goal

Align droidrun governance posture with tri-workspace policy where AI-Project-Manager is canonical authority for workflow/state/tool rules.

### Scope

- `.cursor/rules/00-global-core.md`
- `AGENTS.md`

### Commands / Tool Calls

- ReadFile for current rule/docs baseline
- ApplyPatch for targeted governance updates

### Changes

- Added canonical-authority statement to `.cursor/rules/00-global-core.md`.
- Added canonical-authority statement to `AGENTS.md`.

### Evidence

PASS — droidrun now explicitly mirrors AI-PM governance authority and rule discipline.

### Verdict

READY - governance linkage added.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- Improves tri-workspace governance consistency.

### Decisions Captured

- droidrun follows AI-PM as canonical architect/governance source.

### Pending Actions

- Continue parity checks using AI-PM policy drift checker process.

### What Remains Unverified

- None for this documentation-only change.

### What's Next

- Keep droidrun mirrors synchronized when AI-PM rules evolve.

## 2026-03-19 18:44 — DroidRun Workflow Strengthening + Handoff Addition

### Goal

Bring droidrun workflow/docs to the same tri-workspace standard for PLAN prompt output, AGENT checker discipline, and handoff-based context continuity.

### Scope

- `.cursor/rules/10-project-workflow.md`
- `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`
- `docs/ai/CURSOR_WORKFLOW.md`
- `docs/ai/HANDOFF.md` (new)

### Commands / Tool Calls

- ReadFile for existing workflow docs
- ApplyPatch for workflow + bootstrap updates
- `npx prettier --write` on changed docs
- ReadLints validation

### Changes

- Updated workflow rule to require PLAN responses to end with one AGENT prompt block with explicit first two lines and model-mode format.
- Added AGENT required completion checks (lint + type/compile/build + required tests).
- Added handoff maintenance requirement after meaningful state changes.
- Rewrote DroidRun tab bootstrap prompts with `@` doc references including handoff.
- Created `docs/ai/HANDOFF.md` as concise operational snapshot for new sessions.
- Updated `docs/ai/CURSOR_WORKFLOW.md` to reflect PLAN output and handoff policy.

### Evidence

PASS — droidrun workflow docs updated and lint-clean.

### Verdict

READY.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- Keeps droidrun aligned with AI-PM and open--claw governance contracts.

### Decisions Captured

- droidrun now uses handoff snapshot pattern for session continuity.

### Pending Actions

1. Validate first live bootstrap cycle with the new tab prompts.

### What Remains Unverified

- Live adherence in user-run bootstrap session.

### What's Next

- Use updated bootstrap prompts for next droidrun planning/execution cycle.

## 2026-03-29 — Governance/Documentation Drift Fixes

### Goal

Apply minimum wording-only governance updates to fix documentation drift around archival policy, unresolved turbulence promotion, and PLAN model-selection behavior.

### Scope

- `.cursor/rules/10-project-workflow.md`
- `docs/ai/CURSOR_WORKFLOW.md`
- `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`
- `AGENTS.md`
- `docs/ai/HANDOFF.md`
- `docs/ai/STATE.md` (this entry)

### Commands / Tool Calls

- Read: all six target files + `docs/ai/memory/DECISIONS.md` + `docs/ai/memory/PATTERNS.md` + AI-PM `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`
- StrReplace: targeted wording-only edits per file

### Changes

- `.cursor/rules/10-project-workflow.md`: Added `Rationale:` third line requirement to AGENT prompt format; added explicit allowed model choices (Composer2, Sonnet 4.6, Opus 4.6); added turbulence promotion rule to AGENT contract; replaced blunt `~500 lines` archive trigger with size/token-first policy deferring to `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`.
- `docs/ai/CURSOR_WORKFLOW.md`: Mirrored `Rationale:` line requirement and explicit model choices in PLAN output requirement.
- `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`: Updated PLAN bootstrap with named model choices and when-to-use guidance; added `Rationale:` line to AGENT prompt template; replaced implicit `MODEL: Sonnet 4.6 non-thinking` AGENT tab header with neutral model-selection reference.
- `AGENTS.md`: Added turbulence promotion requirement to Agent contract.
- `docs/ai/HANDOFF.md`: Added `Recent Unresolved Issues` and `Standing Constraints` sections; populated with existing known constraints.

### Evidence

- PASS — `.cursor/rules/10-project-workflow.md`: turbulence rule, model list, Rationale line, size-first archive policy all added.
- PASS — `docs/ai/CURSOR_WORKFLOW.md`: Rationale line and model policy mirrored.
- PASS — `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`: PLAN model policy named; AGENT prompt has Rationale; header bias removed.
- PASS — `AGENTS.md`: turbulence promotion requirement added.
- PASS — `docs/ai/HANDOFF.md`: `Recent Unresolved Issues` and `Standing Constraints` sections added.

### Verdict

READY — all requested governance fixes applied. Wording-only; no workflow broadening.

### Blockers

None.

### Fallbacks Used

None. All reads and edits completed directly.

### Cross-Repo Impact

Changes are droidrun-local governance docs. AI-Project-Manager is the canonical authority; these changes bring droidrun into alignment with AI-PM policy direction. No cross-repo file edits required.

### Decisions Captured

- Archive trigger is size/token-first per `CONTEXT_WINDOW_MONITORING.md`; line counts are soft proxy only.
- PLAN must name model and provide Rationale in every AGENT prompt it emits.
- Unresolved turbulence must be visible in HANDOFF.md, not only buried in STATE.md.

### Pending Actions

- Create `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` in droidrun (currently only in AI-Project-Manager) to make the archive policy self-contained.

### What Remains Unverified

- Whether PLAN tab (currently uses a non-standard `GPT-5.4 high thinking` model label) will be corrected to an actual Cursor-available model in a live session.

### What's Next

- PLAN or operator: optionally create `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` in droidrun mirroring AI-PM version.

---

## 2026-03-31 17:00 — Tri-Workspace Governance Normalization (Prompt 7) — Cross-Repo Impact

### Goal

Normalize governance rules for STATE.md archive policy, AGENT execution-ledger policy, AGENT contract language, PLAN source-of-truth order across all three repos. This entry records the droidrun-specific changes.

### Scope

- `droidrun/.cursor/rules/10-project-workflow.md`
- `droidrun/.cursor/rules/00-global-core.md`
- `droidrun/AGENTS.md`
- `droidrun/docs/ai/CURSOR_WORKFLOW.md`

### Commands / Tool Calls

- Read: droidrun governance files — PASS
- Write: StrReplace on 4 files — PASS

### Changes

- `10-project-workflow.md`: Replaced ~400/~600 line proxy with canonical KB-based thresholds (≤140KB/warn/>180KB archive; ~800 soft/~1000 hard). Added ledger append to AGENT contract. Added FINAL_OUTPUT_PRODUCT.md at position 1 of PLAN source-of-truth priority. Added full AGENT Execution Ledger section with one-block-at-a-time gate.
- `00-global-core.md`: Added ledger append requirement and Execution Ledger (non-canonical) section with one-block-at-a-time rule.
- `AGENTS.md`: Added Context source priority section (FINAL_OUTPUT_PRODUCT.md first). Added ledger append to Agent contract. Added Execution Ledger (non-canonical) section. Added docs/ai/context/ and archive/ to State tracking.
- `CURSOR_WORKFLOW.md`: Added Authority Hierarchy section. Added Workspace layer model table. Added ledger reference and archive note in State and Planning section. Added Context source priority section.

### Evidence

- PASS: ~400/~600 line proxy rule removed — replaced with KB thresholds
- PASS: FINAL_OUTPUT_PRODUCT.md is now position 1 in PLAN source-of-truth priority
- PASS: Ledger policy explicit and consistent in all four changed files
- PASS: FINAL_OUTPUT_PRODUCT.md unchanged
- PASS: No default bootstrap prompt reads the ledger

### Verdict

READY — droidrun governance normalized to match tri-workspace standard.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

AI-Project-Manager and open--claw also updated in same pass.

### Decisions Captured

- Legacy ~400/~600 soft archive proxy permanently replaced with KB-based policy.
- Ledger is non-canonical, non-default, one-block-at-a-time in droidrun.
- FINAL_OUTPUT_PRODUCT.md is now the authoritative position-1 source for PLAN state reconstruction.

### Pending Actions

- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` and `docs/ai/context/archive/` do not exist in droidrun yet — create when first AGENT block appends a ledger entry.

### What Remains Unverified

None.

### What's Next

Proceed to Prompt 8.
---

## 2026-04-06 23:25 — Serena Project Normalization

### Goal

Add the repo-local Serena project for DroidRun and mirror only the local scope guidance needed so DroidRun code uses its own exact-path Serena project without inheriting upstream repo assumptions.

### Scope

- `droidrun/.gitignore`
- `droidrun/.serena/project.yml`
- `droidrun/AGENTS.md`
- `droidrun/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`
- `droidrun/docs/ai/HANDOFF.md`

### Commands / Tool Calls

- Tools: `ReadFile`, `ApplyPatch`
- Cross-repo verification tools used from AI-Project-Manager: `Glob`, `rg`

### Changes

- Updated `.gitignore` so `.serena/project.yml` is commit-tracked while other Serena-local artifacts remain ignored.
- Created `.serena/project.yml` with the DroidRun-specific Serena scope and iOS quarantined paths ignored.
- Added minimal repo-local guidance to `AGENTS.md`, `TAB_BOOTSTRAP_PROMPTS.md`, and `HANDOFF.md` telling sessions to activate `D:/github/droidrun` by exact path for code work.

### Evidence

- PASS: `.serena/project.yml` exists and is readable.
- PASS: `.gitignore` now unignores only `.serena/project.yml`.
- PASS: `AGENTS.md`, tab bootstrap prompts, and handoff all state that upstream governance docs are outside the DroidRun Serena project.

### Verdict

READY — DroidRun now has the intended repo-local Serena project and the local guidance keeps its code scope isolated from the other repos.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- Matches the AI-PM Serena project map and fallback policy.
- Keeps DroidRun aligned with the OpenClaw runtime and AI-PM exact-path activation model.

### Decisions Captured

- DroidRun Serena scope is `D:/github/droidrun`.
- Upstream charter/governance docs are read normally but are not part of the DroidRun Serena project.

### Pending Actions

- Live-test a fresh DroidRun session to confirm the exact-path activation works as documented.

### What Remains Unverified

- Fresh-session Serena activation for `D:/github/droidrun` has not yet been manually exercised after this normalization.

### What's Next

Use `D:/github/droidrun` as the first Serena activation path on the next DroidRun code task.
---

## 2026-04-07 00:12 — MCP Tool Governance Alignment

### Goal

Mirror the updated tri-workspace tool policy so DroidRun work uses repo-first docs, requires the right high-value tools only when relevant, and stops to notify the user if a required tool is unavailable.

### Scope

- `droidrun/.cursor/rules/05-global-mcp-usage.md`
- Local config: `droidrun/.cursor/mcp.json`

### Commands / Tool Calls

- Tools: `ReadFile`, `ApplyPatch`
- Cross-repo verification from AI-Project-Manager: `WebSearch`, `ReadLints`

### Changes

- Rewrote the active MCP rule to align with the new repo-first docs and stop-notify tool policy.
- Added local `.cursor/mcp.json` so `serena` and `Exa Search` can be project-scoped in this workspace.
- Removed `sequential-thinking`, `shell-mcp`, and GitKraken MCP from the supported toolchain in the active rule surface.

### Evidence

- PASS: `.cursor/rules/05-global-mcp-usage.md` now requires repo docs first and external-doc query discipline.
- PASS: `.cursor/mcp.json` exists for this repo with the intended project-local servers.

### Verdict

READY — DroidRun now mirrors the cleaned high-value tool policy and has a project-local MCP config for the heavy servers it actually needs.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

- Matches the canonical tool policy in AI-Project-Manager.

### Decisions Captured

- DroidRun keeps `serena` and `Exa Search` local to this workspace rather than global.

### Pending Actions

- Reload Cursor to apply the new local MCP config.

### What Remains Unverified

- The new local MCP tool set has not yet been live-smoke-tested after reload.

### What's Next

Reload Cursor and verify the DroidRun workspace exposes the expected project-local tools.

---

## 2026-04-08 00:15 — Serena Registration + Workflow Parity

### Goal

Register `droidrun` in Serena and mirror the latest workflow/tool-discipline updates from AI-Project-Manager.

### Scope

`.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`, Serena registration state.

### Commands / Tool Calls

- Serena `activate_project(D:/github/droidrun)`
- direct file edits from AI-Project-Manager governance pass

### Changes

- Registered `droidrun` in Serena by exact path.
- Added `Required Tools` prompt contract and launch-integrity rule parity.
- Updated Serena activation guidance to include the full tri-workspace path map.

### Evidence

- PASS: Serena created and activated project `droidrun` at `D:/github/droidrun`.

### Verdict

PASS — DroidRun is now registered in Serena and aligned with the latest governance workflow.

### Blockers

None.

### Fallbacks Used

- None.

### Cross-Repo Impact

- Mirrors AI-Project-Manager governance updates.

### Decisions Captured

- Exact-path Serena activation is the canonical project-registration mechanism for new repos.

### Pending Actions

- Confirm the registered `droidrun` project appears in Serena after restart.

### What Remains Unverified

- Post-restart Serena project list visibility from the UI.

### What's Next

- After restart, verify `droidrun` remains registered and activate it again as a smoke test.

## 2026-04-09 00:45 — DroidRun Workflow Surface Alignment

### Goal

Bring DroidRun's bootstrap prompts and mirrored workflow/rule docs into alignment with the current tri-workspace policy and fix the missing root AGENTS contract.

### Scope

Touched `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `.cursor/rules/openmemory.mdc`, `docs/ai/CURSOR_WORKFLOW.md`, `AGENTS.md`, and `docs/ai/STATE.md`.

### Commands / Tool Calls

`ReadFile`, `rg`, `ApplyPatch`, `ReadLints`.

### Changes

- Updated DroidRun tab bootstraps to match the current one-AGENT PLAN contract, ledger gate, and OpenMemory-first recovery order.
- Repaired the malformed Serena activation block in `05-global-mcp-usage.md`.
- Updated `10-project-workflow.md` and `openmemory.mdc` to remove stale policy drift and reflect the current OpenMemory/tool-required behavior.
- Added a root `AGENTS.md` so workflow docs no longer point to a missing file.

### Evidence

- PASS: DroidRun bootstrap/rule/doc surfaces updated successfully
- PASS: new `AGENTS.md` created at repo root
- PASS: `ReadLints` returned no errors for touched DroidRun files

### Verdict

READY — DroidRun now has a complete root contract and aligned bootstrap/rule surfaces.

### Blockers

None.

### Fallbacks Used

- Used targeted doc reads instead of Serena because this was policy/documentation work, not source-symbol analysis.

### Cross-Repo Impact

- Mirrors AI-Project-Manager governance updates so the actuator repo follows the same bootstrap and ledger policy.

### Decisions Captured

- DroidRun needs a repo-root `AGENTS.md` to keep workflow docs self-consistent.
- The OpenMemory rule must follow the same "required tool => stop and notify" contract as the shared MCP policy.

### Pending Actions

- Verify the new DroidRun root `AGENTS.md` is the file future tabs and audits reference by default.

### What Remains Unverified

- Fresh-session behavior of the updated DroidRun tab prompts and local OpenMemory retrieval flow.

### What's Next

- Use the aligned DroidRun policy surfaces for future Android/actuator task planning instead of older mirrored docs.

## 2026-04-10 01:20 — Reasoning Policy Mirror + Low-Bloat Bootstrap Tightening

### Goal

Mirror the new reasoning/tool policy into droidrun and reduce default bootstrap preload so PLAN relies on memory plus `STATE.md` first.

### Scope

Touched `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`.

### Commands / Tool Calls

`ReadFile`, `rg`, `ApplyPatch`, `ReadLints`.

### Changes

- Promoted `thinking-patterns` over the old Clear Thought naming in active workflow/rule surfaces.
- Added conditional guidance for `context-matic`, `obsidian-vault`, and `filesystem`.
- Tightened PLAN bootstrap so `STATE.md` is the first repo file after OpenMemory and other docs stay on-demand.

### Evidence

- PASS: droidrun mirrored rule and tab files updated successfully
- PASS: no linter errors in touched droidrun files

### Verdict

READY — droidrun bootstrap behavior now matches the lower-bloat recovery model and new reasoning MCP policy.

### Blockers

None.

### Fallbacks Used

- None.

### Cross-Repo Impact

- Mirrors the AI-Project-Manager canonical workflow/rule migration.

### Decisions Captured

- droidrun PLAN recovery should default to memory plus `STATE.md`, not broad multi-doc preload.

### Pending Actions

- Run the next real droidrun planning cycle through the updated bootstrap and confirm it stays context-light in practice.

### What Remains Unverified

- Live-session behavior of the updated droidrun bootstrap prompt under real task load.

### What's Next

- Use the leaner recovery path for future Android/runtime work.

## 2026-04-10 22:09 - Android-Only README Alignment

### Goal

Align the public DroidRun README with this repo's Android-only actuator role so it no longer advertises active iOS support while iOS paths remain quarantined.

### Scope

- `src/README.md`
- `docs/ai/STATE.md`

### Commands / Tool Calls

- Read: `src/README.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/02-non-routable-exclusions.md`, `AGENTS.md` - PASS
- Search: repo-wide iOS references to confirm the highest-risk mismatch was in the public README - PASS
- Write: update `src/README.md` intro and feature bullets, add scope note and documentation note - PASS
- Lints: `src/README.md` - PASS

### Changes

- Reworded the top-level `src/README.md` description from Android+iOS support to Android-only for this tri-workspace fork.
- Added a clear scope note that this repo is the Android actuator layer and that the retained iOS paths are quarantined for upstream compatibility only.
- Added a documentation note warning that upstream references to experimental iOS support are out of scope in this workspace and that operators should use the Android Portal/APK + ADB flow only.

### Evidence

- PASS: `src/README.md` no longer contains the public-facing phrase `Android and iOS devices`
- PASS: `ReadLints` returned no diagnostics for `src/README.md`
- PASS: README language now matches `AGENTS.md` and `.cursor/rules/02-non-routable-exclusions.md`, which define `droidrun` as the Android actuator layer

### Verdict

READY - DroidRun's public README now matches the repo's Android-only governance and quarantine model.

### Blockers

None.

### Fallbacks Used

- Left upstream/generated docs that still mention experimental iOS support unchanged in this pass; the README now explicitly warns that those references are out of scope for this workspace.

### Cross-Repo Impact

None - change is local to `droidrun`.

### Decisions Captured

- Use an explicit Android-only scope note in the README as the minimum high-value alignment step instead of attempting a broader rewrite of upstream documentation sources in one pass.

### Pending Actions

- If this fork continues diverging from upstream, propagate the Android-only scope note into generated docs surfaces in a later docs-specific pass.

### What Remains Unverified

- Generated docs under `src/docs/` still contain historical upstream iOS references; they were not rewritten in this minimum-scope remediation.

### What's Next

- Keep future droidrun documentation and runtime work aligned with the Android-only actuator role unless Tony explicitly approves lifting the quarantine.
