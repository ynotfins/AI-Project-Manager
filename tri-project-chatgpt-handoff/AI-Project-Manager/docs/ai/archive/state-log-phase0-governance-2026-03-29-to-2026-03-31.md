# STATE.md Archive — AI-Project-Manager
<!-- Entries moved verbatim from docs/ai/STATE.md on 2026-04-01 (archive/compaction pass). -->
<!-- Do NOT edit these entries. Historical record only. PLAN and DEBUG must not load this by default. -->

Archive pass date: 2026-04-01
Covers: 2026-03-29 through 2026-03-31 (Phase 0 operations, governance normalization, Prompt 7, and earlier Prompt 8 bookkeeping)
Source file: docs/ai/STATE.md
Moved by: AGENT (Executioner) — dedicated archive/compaction pass

---

## 2026-04-01 — Non-Routable Quarantine System Installed (Tri-Workspace)

### Goal
Implement explicit path-based quarantine system that prevents out-of-scope material from entering routing, search, memory, or embeddings flows across AI-Project-Manager, open--claw, and droidrun.

### Scope
- `.cursor/rules/02-non-routable-exclusions.md` — new enforcement rule (mirror; canonical in open--claw)
- `.cursor/rules/openmemory.mdc` — memory exclusion block added
- `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` — quarantine table and common-misunderstandings bullet added
- `docs/ai/STATE.md` — this entry

### Commands / Tool Calls
- Created `.cursor/rules/02-non-routable-exclusions.md` — PASS
- Updated `.cursor/rules/openmemory.mdc` with NON-ROUTABLE QUARANTINE memory exclusions section — PASS
- Updated `TRI_WORKSPACE_CONTEXT_BRIEF.md` with quarantine table and updated Common Misunderstandings — PASS
- Updated `STATE.md` — PASS

### Changes
- New rule file enforces 4 quarantined paths (candidate_employees and 3 droidrun iOS paths) for this repo's sessions
- openmemory.mdc now blocks memory storage/recall for quarantined content
- TRI_WORKSPACE_CONTEXT_BRIEF now surfaces quarantine as a routing-layer concern

### Evidence
- All 3 rule files exist and are `alwaysApply: true`
- Canonical registry in `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
- 2,608 candidate_employees files bannered; 3 droidrun iOS files bannered

### Verdict
PASS

### Blockers
None

### Fallbacks Used
None

### Cross-Repo Impact
- `open--claw`: canonical registry + rule file + knowledgebase docs updated
- `droidrun`: rule file + openmemory.mdc + bootstrap prompts + STATE.md updated

### Decisions Captured
- open--claw is the canonical quarantine registry; AI-Project-Manager and droidrun mirror enforcement only
- Promotion gate requires Tony's explicit approval; no agent may self-approve

### Pending Actions
None — quarantine is complete for this pass

### What Remains Unverified
Live embeddings/RAG pipeline exclusion (no such pipeline is currently running)

### What's Next
Normal operations. Quarantine enforcement is now passive via rules.

---

## 2026-03-31 — Install AGENT Execution Ledger System

### Goal

Install a non-canonical execution-ledger system so AGENT records the exact execution prompt and final AGENT response after each completed prompt block, without bloating default PLAN/DEBUG bootstrap context. Make the ledger mandatory for AGENT and strictly non-default for PLAN/DEBUG.

### Scope

AI-Project-Manager only. Files: `docs/ai/context/AGENT_EXECUTION_LEDGER.md` (new), `docs/ai/context/archive/.gitkeep` (new), `AGENTS.md`, `.cursor/rules/00-global-core.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/CURSOR_WORKFLOW.md`, `docs/ai/HANDOFF.md`, `docs/ai/memory/MEMORY_CONTRACT.md`, `docs/ai/STATE.md`.

### Commands / Tool Calls

- Read: `AGENTS.md`, `00-global-core.md`, `10-project-workflow.md`, `CURSOR_WORKFLOW.md`, `HANDOFF.md`, `MEMORY_CONTRACT.md`, `STATE.md` — PASS
- Write: `docs/ai/context/AGENT_EXECUTION_LEDGER.md` — PASS
- Write: `docs/ai/context/archive/.gitkeep` — PASS
- StrReplace: `AGENTS.md` — PASS
- StrReplace: `.cursor/rules/00-global-core.md` — PASS
- StrReplace: `.cursor/rules/10-project-workflow.md` (×2) — PASS
- StrReplace: `docs/ai/CURSOR_WORKFLOW.md` — PASS
- StrReplace: `docs/ai/HANDOFF.md` — PASS
- StrReplace: `docs/ai/memory/MEMORY_CONTRACT.md` — PASS

### Changes

- **Created** `docs/ai/context/AGENT_EXECUTION_LEDGER.md` — active ledger with full policy (non-canonical declaration, PLAN/DEBUG consultation gate, size management, entry format, AGENT append requirement) and initial entry LEDGER-001.
- **Created** `docs/ai/context/archive/.gitkeep` — establishes archive directory.
- **Updated** `AGENTS.md` — added ledger append to Agent contract; added Execution Ledger section.
- **Updated** `.cursor/rules/00-global-core.md` — added ledger append requirement in State updates section; added Execution Ledger non-canonical policy block.
- **Updated** `.cursor/rules/10-project-workflow.md` — added ledger append to AGENT execution contract; added dedicated `AGENT Execution Ledger` section with mandatory append, strict PLAN/DEBUG consultation gate, and size management rules.
- **Updated** `docs/ai/CURSOR_WORKFLOW.md` — added ledger reference with non-canonical policy in State and Planning section.
- **Updated** `docs/ai/HANDOFF.md` — added Section 7: Durable Operator Behaviors with ledger operator rules.
- **Updated** `docs/ai/memory/MEMORY_CONTRACT.md` — added ledger entry to non-canonical source list with consultation gate.

### Evidence

- PASS: `AGENT_EXECUTION_LEDGER.md` created with non-canonical declaration, PLAN/DEBUG gate (3 conditions required before consultation), size management (3–5 entries active, archive at >5 or ~300 lines), mandatory append requirement, entry format, and LEDGER-001 initial entry.
- PASS: `archive/` directory established with `.gitkeep`.
- PASS: `AGENTS.md` updated — ledger append is now listed alongside STATE.md update as equally mandatory in Agent contract.
- PASS: `00-global-core.md` updated — ledger policy added with explicit PLAN/DEBUG consultation gate and archive policy.
- PASS: `10-project-workflow.md` updated — `AGENT Execution Ledger` section added after `docs/ai/context/` section; AGENT execution contract includes ledger append bullet.
- PASS: `CURSOR_WORKFLOW.md` updated — ledger entry added to State and Planning section with non-canonical and consultation-gate wording.
- PASS: `HANDOFF.md` updated — Section 7 added with durable operator behaviors for the ledger system.
- PASS: `MEMORY_CONTRACT.md` updated — ledger listed as non-canonical source with consultation gate.
- PASS: `TAB_BOOTSTRAP_PROMPTS.md` deliberately NOT updated — ledger must not appear in default tab reads.
- PASS: `FINAL_OUTPUT_PRODUCT.md` not modified.
- PASS: STATE.md, HANDOFF.md requirements not weakened.

### Verdict

PASS — Ledger system installed. Non-canonical policy enforced. AGENT append requirement is durable across all binding docs (AGENTS.md, 00-global-core.md, 10-project-workflow.md). PLAN/DEBUG consultation is strictly gated in all three rule/workflow docs.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

None — ledger system is AI-Project-Manager only. No open--claw or droidrun files modified.

### Decisions Captured

- Ledger is non-canonical: it records verbatim facts but does not govern behavior. Canonical sources (STATE.md, DECISIONS.md, PATTERNS.md, HANDOFF.md, rules) always win.
- PLAN/DEBUG consultation requires 3 conditions: canonical sources insufficient + exact text specifically needed + only minimum blocks read.
- Archive threshold: 5 entries or ~300 lines; archived entries must be moved verbatim, never summarized.
- TAB_BOOTSTRAP_PROMPTS.md must never reference the ledger.

### Pending Actions

None — system is operational. First real ledger append test will be the next AGENT block.

### What Remains Unverified

- Ledger append discipline in practice — rule is installed, but first live test by a new AGENT session will confirm adherence.

### What's Next

AGENT or PLAN to proceed with next task. Ledger will be appended after that block per the installed requirement.

---

## 2026-03-31 — Sparky Enforcement Gate + Non-Overlapping Delegation Chain

### Goal
Rewrite open--claw leadership and quality packets so Sparky is the mandatory post-edit enforcement gate, the delegation chain has no overlap, and every role has a single clear authority boundary.

### Scope
open--claw repo only. Files: `TEAM_ROSTER.md`, Sparky `AGENTS.md`, Sparky `WORKFLOWS.md`, `delivery-director/AGENTS.md`, `product-manager/AGENTS.md`, `code-reviewer/AGENTS.md`, `qa-evidence-collector/AGENTS.md`, `reality-checker/AGENTS.md`, `software-architect/AGENTS.md`, `backend-architect/AGENTS.md`, `open--claw/docs/ai/STATE.md`.

### Commands / Tool Calls
- Read: `FINAL_OUTPUT_PRODUCT.md`, `TEAM_ROSTER.md`, Sparky `AGENTS.md`, Sparky `WORKFLOWS.md`, all 8 target `AGENTS.md` files — PASS
- Write: 10 files in `open-claw/AI_Employee_knowledgebase/` — PASS (all)
- StrReplace: `open--claw/docs/ai/STATE.md` — PASS
- StrReplace: `AI-Project-Manager/docs/ai/STATE.md` (this file) — PASS
- Append: `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md` — PASS

### Changes
See `open--claw/docs/ai/STATE.md` entry `2026-03-31 — Sparky Enforcement Gate` for full change detail. Summary:
- `TEAM_ROSTER.md` — Role Boundaries table + Deterministic Handoff Chain (6-step).
- Sparky `AGENTS.md` — Mandatory Post-Edit Review Gate section; ACCEPT/REFACTOR/REJECT vocabulary; exclusive authority declared.
- Sparky `WORKFLOWS.md` — Handoff chain diagram; post-edit review procedure; pre-release checklist; ongoing cadence.
- `delivery-director/AGENTS.md` — Sequencing/routing only; explicit "does not accept or reject" boundary.
- `product-manager/AGENTS.md` — Briefs/scope/acceptance criteria only; explicit "does not make quality decisions" boundary.
- `code-reviewer/AGENTS.md` — Evidence provider and advisor; explicit "no final authority" boundary.
- `qa-evidence-collector/AGENTS.md` — Evidence provider; explicit "does not make final quality decisions" boundary.
- `reality-checker/AGENTS.md` — Go/no-go recommender to Sparky only; removed parallel delivery-director routing.
- `software-architect/AGENTS.md` — Technical advisor; explicit "does not accept or reject independently" boundary.
- `backend-architect/AGENTS.md` — Technical advisor; explicit "does not accept or reject independently" boundary.

### Evidence
- PASS: All 10 target files written without error.
- PASS: Sparky is the only entity with ACCEPT/REFACTOR/REJECT authority in all updated files.
- PASS: Reality Checker no longer routes decisions to Delivery Director — recommender to Sparky only.
- PASS: `FINAL_OUTPUT_PRODUCT.md` not modified.
- PASS: Role language is non-overlapping across all 10 files.
- PASS: `open--claw/docs/ai/STATE.md` updated with full evidence block.

### Verdict
PASS — Enforcement gate installed. Delegation chain is deterministic and non-overlapping.

### Blockers
None.

### Fallbacks Used
None.

### Cross-Repo Impact
open--claw: 10 files + STATE.md updated. droidrun: not affected. AI-Project-Manager: this STATE.md entry + AGENT_EXECUTION_LEDGER.md entry.

### Decisions Captured
- Sparky is the exclusive ACCEPT/REFACTOR/REJECT authority for all file changes and release decisions.
- Canonical handoff chain: brief → routing → implement → evidence collection (parallel) → Sparky gate → release → post-release verification.
- Reality Checker = go/no-go recommender, not a parallel decision-maker.
- Delivery Director = sequencing and routing only; no quality authority.
- Product Manager = briefs and acceptance criteria only; no quality authority.

### Pending Actions
Commit and push both open--claw and AI-Project-Manager changes to origin.

### What Remains Unverified
Deployed CrewClaw workers still use older packets; curated knowledgebase standard applies until workers are re-synced.

### What's Next
Commit open--claw and AI-Project-Manager changes. Optionally extend role-boundary language into BOOTSTRAP.md/SOUL.md/IDENTITY.md files per Sparky's judgment.

---

## 2026-03-31 17:00 — Charter Enforcement Kernel Installed (Reconciliation Pass)
### Goal
Install enforcement kernel across all three repos so charter violations are blocked by rules, not merely described in docs.
### Scope
All three repos: AI-Project-Manager, open--claw, droidrun.
### Commands / Tool Calls
- Created `.cursor/rules/01-charter-enforcement.md` in all three repos — PASS
- Updated `AGENTS.md` in all three repos to reference enforcement kernel — PASS
- Updated `.cursor/rules/00-global-core.md` in all three repos to load enforcement kernel — PASS
- Updated `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` in all three repos to include enforcement kernel in every tab read list — PASS
- Updated `docs/ai/STATE.md` in all three repos — PASS
### Changes
- New: `AI-Project-Manager/.cursor/rules/01-charter-enforcement.md`
- New: `open--claw/.cursor/rules/01-charter-enforcement.md`
- New: `droidrun/.cursor/rules/01-charter-enforcement.md`
- Modified: AGENTS.md in all three repos (added enforcement kernel to authoritative rules)
- Modified: 00-global-core.md in all three repos (added Enforcement Kernel section at top)
- Modified: TAB_BOOTSTRAP_PROMPTS.md in all three repos (added `01-charter-enforcement.md` to every tab's read list)
### Evidence
- PASS: All three `01-charter-enforcement.md` files written with fail-fast rule, forbidden platform list (macOS/iOS/Swift/Xcode/CocoaPods), Sparky routing, and authority ceiling.
- PASS: All three `00-global-core.md` files updated with Enforcement Kernel section directing load of `01-charter-enforcement.md` after 00.
- PASS: All five tabs in each repo's `TAB_BOOTSTRAP_PROMPTS.md` updated to include `01-charter-enforcement.md` as second item in read list after `FINAL_OUTPUT_PRODUCT.md`.
- PASS: `AGENTS.md` in all three repos updated with enforcement kernel bullet in authoritative rules section.
- PASS: `FINAL_OUTPUT_PRODUCT.md` not modified.
### Verdict
PASS — Enforcement kernel installed. Charter violations are now blocked at the rule layer.
### Blockers
None.
### Fallbacks Used
None.
### Cross-Repo Impact
All three repos updated. Changes are additive and non-destructive. Authority hierarchy from Prompts 1 and 2 preserved.
### Decisions Captured
- `01-charter-enforcement.md` is the enforcement kernel; loads after `00-global-core.md` in every bootstrap.
- Forbidden platforms for tri-workspace: macOS, iOS, Swift, Xcode, CocoaPods.
- Violations route to Sparky before any continuation is allowed.
### Pending Actions
None. Kernel is installed.
### What Remains Unverified
Cursor's rule-loading order cannot be tested in this session; runtime confirmation requires a new tab bootstrap.
### What's Next
Next PLAN session should verify enforcement kernel is loaded correctly in an active tab.

---

## Current State Summary

> Last updated: 2026-03-29 (Phase 0B: CrewClaw Bitwarden activation ? shared deploy fixed, secret inventory added, all five workers running + paired, gateway route still blocked, dashboard heartbeat still absent)
> Last verified runtime: 2026-03-29 (systemd gateway OK; Telegram healthy; WhatsApp 401 ? QR re-scan required; Windows Desktop Connected:1; CrewClaw workers running with Bitwarden-injected tokens; all five point to host `main`; representative gateway route times out at host model call; CrewClaw first ping still unproven)

### Phase Status

| Phase                           | Status       | Closed         |
| ------------------------------- | ------------ | -------------- |
| 0 - Scaffold + Workflow         | COMPLETE     | 2026-02-23     |
| 1 - MCP Infrastructure          | COMPLETE     | 2026-02-26     |
| 2 - Secrets Management          | COMPLETE     | 2026-02-27     |
| 3 - OpenMemory Integration      | COMPLETE     | 2026-03-02     |
| 4 - Multi-Machine Parity        | COMPLETE     | 2026-03-04     |
| 5 - Remaining Automation        | COMPLETE     | 2026-03-04     |
| 6A - Architecture Design        | COMPLETE     | 2026-03-06     |
| 6B - Gateway Boot               | COMPLETE     | 2026-03-08     |
| **6C - First Live Integration** | **COMPLETE** | **2026-03-14** |
| **Phase 1A ? CrewClaw Stabilization** | **IN PROGRESS** | ? |

### Phase 6C Exit Criteria - ALL PASSED (2026-03-14)

- [x] Audit log captures actions - gateway file log `/tmp/openclaw/`, confirmed
- [x] Hybrid model routing configured - primary: claude-sonnet-4-20250514, fallback: gpt-4o-mini
- [x] WhatsApp channel operational (Baileys, selfChatMode, allowlist)
- [x] Telegram secured (owner ID 6873660400, dmPolicy: allowlist)
- [x] Signal disabled
- [x] Approval gate tested - sandbox mode + exec-approvals; `rm -rf` blocked from real host (2026-03-14)
- [x] gog OAuth complete (Gmail read access verified)
- [x] First integration tested - weather skill, 42F NY, runId 2a3f0990 (2026-03-14)

### Runtime Snapshot (as of 2026-03-29)

- Gateway: 0.0.0.0:18789 (bind=lan), :18792 (API health), systemd ? **OpenClaw 2026.3.13** via `~/openclaw-build` tag v2026.3.13-1, `ExecStart` uses `dist/index.js`
- CLI ops: `source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw <cmd>`
- Canonical restart: `AI-Project-Manager/scripts/restart-openclaw-gateway.ps1` (+ `openclaw_gateway_required_env.py`)
- Node: v22.22.0 (nvm), pnpm 10.23.0
- Skills: 19/59 ready
- Channels: **WhatsApp: 401 Unauthorized (QR re-scan required)**, Telegram (healthy/running, `@Sparky4bot`), Signal (disabled)
- Windows nodes: **Connected:1** ? Windows Desktop (v2026.3.13, caps: browser+system)
- Model routing: anthropic/claude-sonnet-4-20250514, fallback openai/gpt-4o-mini
- **Sandbox: mode=off** by design (direct host access)
- **Docker: v29.1.3** running; openclaw-sandbox:bookworm-slim active
- **Context engine: lossless-claw v0.3.0** (LCM active, db=`~/.openclaw/lcm.db`)
- **DroidRun MCP**: enabled (Samsung Galaxy S25 Ultra)
- **CrewClaw Employees (Phase 0B updated)**: 5 workers deployed ? node:22-slim, openclaw@2026.3.13, entrypoint.sh writes gateway config, bot calls `--agent main`, named volumes for device persistence, Bitwarden-backed startup script now uses the real gateway-token UUID and fails closed on missing secrets. **Verified**: all five containers running, Telegram bot tokens valid, gateway health reachable, pairing requests approved. **Still failing**: shared gateway route to host `main` times out on the Anthropic model call; dashboard heartbeat path is absent from the shared deployment.

### Active Blockers

#### BLOCKER 4 - WhatsApp NOT LINKED - **ACTIVE 2026-03-21** (requires user QR scan)

- **Cause:** WhatsApp Baileys session expired on restart (401 Unauthorized, reason: `vll`/`cco` ? auth key invalidated by WhatsApp servers). Session cache cleared via `channels login` first-run.
- **Fix:** User must run `source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw channels login --channel whatsapp` in a WSL terminal and scan the QR with WhatsApp ? Linked Devices.
- **Telegram: unaffected.** Remains healthy and running.
- **Status:** Pending user QR scan. Cannot be automated ? requires physical phone access.

#### BLOCKER 3 - Windows node host - **RESOLVED 2026-03-21** (re-connected after node.cmd launch)

- **Was:** Molty removed 2026-03-16 (XamlParseException crash loop)
- **Fix chain:**
  1. Installed headless node host v2026.3.13 via `openclaw node install`
  2. Added `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` to `node.cmd` (break-glass for trusted private LAN)
  3. Device d8e1ddb2 approved in gateway (`openclaw devices approve`)
  4. `tools.exec`: host=node, security=allowlist, node="Windows Desktop"
  5. `exec-approvals.json`: defaults set to security=full, ask=off, askFallback=allow + wildcard `*` allowlist
- **Verified:** hostname?ChaosCentral, powershell.exe Get-Date?Tuesday, March 17, 2026 5:08:20 PM
- **Status (2026-03-21 Phase 1 hardening):** Re-connected. Stale second entry (847202f0?) removed. `nodes status` shows Known:1 Paired:1 **Connected:1** after node.cmd launched.
- **Known limitation:** Loses connection after reboot until node.cmd is relaunched (startup script handles IP update).

#### BLOCKER 1 - Sandbox + Docker - **RESOLVED 2026-03-18**

- **Was:** Docker not found in WSL; sandbox.mode: "all" caused gateway crash-loop.
- **Discovery 2026-03-18:** Docker v29.1.3 IS installed and running. Sandbox container openclaw-sandbox:bookworm-slim already active (7h uptime).
- **Decision:** sandbox.mode stays "off" by design ? Sparky needs direct host access for autonomous work. Docker sandbox is reserved for CrewClaw employee containers if/when needed.
- **exec-approvals:** Set to security=full, ask=off, askFallback=allow, autoAllowSkills=true ? commands run without any approval prompts.
- **Status:** No blocking issue. Sparky has full autonomous access.

#### BLOCKER 2 - Agent session context overflow - **RESOLVED 2026-03-16**

- **Was:** Agent session `e3853d85` overflowed at 171 messages / 171,384 tokens, causing silent failures on WhatsApp/Telegram.
- **Fix (permanent):** Installed `lossless-claw` v0.3.0 LCM plugin (`pnpm openclaw plugins install @martian-engineering/lossless-claw`). Plugin is now the active `contextEngine`. DAG-based summarization prevents overflow permanently.
- **Config:** `freshTailCount=32`, `contextThreshold=0.75`, `incrementalMaxDepth=-1`, `session.reset.idleMinutes=10080`
- **Evidence:** `[lcm] Plugin loaded (enabled=true, db=~/.openclaw/lcm.db, threshold=0.75)` - warning gone, agent responsive.

### Pending User Actions

1. **WhatsApp re-link (REQUIRED):** Run in WSL terminal: `source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw channels login --channel whatsapp` ? scan QR in WhatsApp ? Linked Devices
2. **CrewClaw host gateway route**: diagnose/fix the host `main` gateway run timeout (`[agent/embedded] Profile anthropic:default timed out`) so paired workers stop falling back locally.
3. **CrewClaw dashboard heartbeat**: decide whether dashboard compatibility remains required, then add Bitwarden-backed `CREWCLAW_MONITOR_KEY` mapping(s) to the shared deployment or explicitly drop dashboard compatibility.
4. Name agent via WhatsApp (bootstrap conversation) ? cosmetic, non-blocking
5. MXRoute email: install imap-smtp-email skill + provide credentials ? Phase 7 work

### Known Recurring Issues

| Issue                                              | Trigger                                                     | Fix                                                                | Permanent Fix Needed                        |
| -------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| Gateway WebSocket `1006 abnormal closure`          | CLI connects before gateway finishes warm-up after restart  | Wait 10-12s after restart before running CLI commands              | None needed - cosmetic timing issue         |
| Agent context overflow -> silent no-response       | Session accumulates >170 messages over days                 | Delete session file, restart gateway                               | Tune `compaction` settings in openclaw.json |
| Gateway crash loop (Docker missing)                | `sandbox.mode: "all"` set without Docker                    | Revert to `sandbox.mode: "off"`                                    | Install Docker or find non-Docker sandbox   |
| Signal restart loop                                | signal-cli Java version mismatch (needs Java 21, has older) | N/A - channel is disabled                                          | Leave disabled; no action needed            |
| Windows node loses connection after Windows reboot | WSL IP changes on reboot                                    | Run startup script (`bws run`) which auto-updates IP in `node.cmd` | None - startup script handles it            |

### Cross-Repo State (open--claw)

- Branch: master, clean
- Phase 2 (First Live Integration): COMPLETE ? mirrors Phase 6C

---

## Archived Entries

Historical STATE.md entries have been archived to reduce context size.
These files preserve original content verbatim. PLAN does not consult them.

| Archive File                                                   | Contents                                                                           | Entries |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------- |
| docs/ai/archive/state-log-phases-0-5.md                        | Phases 0-5 (2026-02-23 to 2026-03-04)                                              | ~30     |
| docs/ai/archive/state-log-phase-6ab.md                         | Phases 6A-6B (2026-03-04 to 2026-03-08)                                            | ~33     |
| docs/ai/archive/state-log-phase-6c-archive.md                  | Superseded Phase 6C entries                                                        | ~14     |
| docs/ai/archive/state-log-phase-6c-active.md                   | Phase 6C active execution entries (2026-03-08 to 2026-03-14)                       | 7       |
| docs/ai/archive/state-log-post-6c-ops.md                       | Post-6C operational fixes (sandbox, lossless-claw, OpenClaw update, headless node) | 4       |
| docs/ai/archive/state-log-mcp-triworkspace-2026-03-16.md       | MCP context optimization + tri-workspace expansion (2026-03-16)                    | 2       |
| docs/ai/archive/state-log-tab-bootstrap-2026-03-16.md          | TAB_BOOTSTRAP_PROMPTS update - Clear Thought 1.5 + tri-workspace (2026-03-16)      | 1       |
| docs/ai/archive/state-log-release-p0-gateway-fix-2026-03-16.md | Release docs phase 0 + gateway crash loop diagnosis and fix (2026-03-16)           | 3       |
| docs/ai/archive/state-log-security-winnode-2026-03-16.md       | Foundation security hardening + Windows node execution fixes (2026-03-16)          | 1       |
| docs/ai/archive/state-log-windows-node-crewclaw-2026-03-17-18.md | Windows node resolution + Sparky full access + CrewClaw deploy (2026-03-17 to 2026-03-18) | 5 |
| docs/ai/archive/state-log-ops-governance-2026-03-19.md         | Doc truth reconciliation + markdown norm + governance/rule audit (2026-03-19)       | 5       |

---

## State Log

<!-- AGENT appends entries below this line after each execution block. -->
## 2026-03-29 09:30 - Phase 0 verification: tri-workspace autonomous model redesign

### Goal
Evidence-first verification of current truth across OpenMemory, OpenClaw runtime memory bridge, CrewClaw inactivity root cause, and Sparky/main identity naming. Phase 1 readiness decision.

### Scope
- open--claw/docs/ai/STATE.md, PLAN.md, HANDOFF.md, memory/MEMORY_CONTRACT.md
- AI-Project-Manager/openmemory.md, docs/tooling/MCP_HEALTH.md
- open--claw/open-claw/configs/openclaw.template.json5
- open--claw/open-claw/employees/deployed/* (compose, setup, heartbeat, README, agent dirs)
- open--claw/open-claw/skills/mem0-bridge/SKILL.md
- Live docker container inspection + WSL gateway commands

### Commands / Tool Calls
- `user-openmemory-health-check` MCP ? health response
- `user-openmemory-search-memory` (user_preference=true) ? search test
- `docker ps --filter name=crewclaw` ? container state
- `docker logs crewclaw-api-integration-specialist --tail 20` ? runtime logs
- `docker inspect crewclaw-api-integration-specialist` ? entrypoint, env, volumes
- `docker exec crewclaw-api-integration-specialist env` ? env vars
- WSL: `pnpm openclaw --version`, `pnpm openclaw health`, `pnpm openclaw channels status --probe`
- WSL: `pnpm openclaw nodes status`
- WSL: `pnpm openclaw skills list`
- WSL: `pnpm openclaw doctor` (grep key warnings)
- WSL: `pnpm openclaw memory status --deep`
- WSL: `pnpm openclaw agent --agent main --message 'what is your name?'`
- Python script inspection of live `~/.openclaw/openclaw.json`
- File reads: all scoped files above

### Changes
None ? verification-only task.

### Evidence

#### 1. OpenMemory (Cursor-side path)

| Check | Result | Detail |
|---|---|---|
| MCP health endpoint | **PASS** | `{"status":"healthy","version":"1.0.0","tools_available":7}` |
| `search-memory` with `user_preference=true` | **PASS** | Returns 1 result (gateway boot pattern, score 0.56) |
| `search-memory` without scope arg | **FAIL** | Error: `At least one of user_preference or project_id must be provided` ? requires explicit scope |
| `add-memory` test | **NOT TESTED** | Search-only was sufficient to prove path works |
| Memory proxy running | **INFERRED PASS** | Search returned data ? proxy is live and injecting auth from env |

**Verdict: OpenMemory Cursor-side path is FUNCTIONAL.** Scoping rule confirmed: always pass `user_preference` or `project_id`.

#### 2. OpenClaw Runtime Memory Bridge

| Check | Result | Detail |
|---|---|---|
| `openclaw memory status --deep` | **PARTIAL** | Provider: none (requested: auto). 7/8 files indexed, 27 chunks, FTS ready |
| Embeddings | **FAIL** | Unavailable ? no API key found for openai/google/voyage/mistral in `auth-profiles.json` |
| Vector search | **unknown** | Cannot function without embeddings provider |
| FTS (full-text search) | **PASS** | Ready |
| mem0-bridge skill status | **NOT LOADED** | Skill exists in `open-claw/skills/mem0-bridge/` but not in `openclaw.json` skills.entries; references mem0 MCP at `localhost:8080` (not the same as OpenMemory proxy on :8766) |
| `openclaw.json` skills.entries | **PASS (partial)** | Only 1 skill loaded: `gog` (enabled=true). mem0-bridge, approval-gate, etc. NOT in live config |

**Verdict: Runtime-side memory bridge is NOT PROVEN FUNCTIONAL.**
- Built-in sqlite/FTS memory works for context recall within sessions.
- Semantic vector search (embeddings) is broken ? no embedding provider API key configured.
- mem0-bridge skill (which would bridge to a mem0 MCP server) is: (a) designed for mem0 MCP at localhost:8080, NOT the OpenMemory proxy at :8766; (b) not enabled in live `openclaw.json`; (c) not loaded per `skills list`.
- **Gap:** There is no proven runtime path from the OpenClaw agent (Sparky) to OpenMemory. The two memory systems are currently SILOED.

#### 3. CrewClaw Inactivity Root Cause

**Deployment path analysis:**

| Layer | Path | What it does |
|---|---|---|
| Top-level compose | `deployed/docker-compose.yml` | Defines all 5 agents; env injected via `start-employees.ps1` (no .env file) |
| Per-agent compose | `deployed/<agent>/docker-compose.yml` | Defines `agent` + `heartbeat` services; uses `.env` file (`env_file: .env`) |
| Startup script | `start-employees.ps1` | Fetches secrets via `bws`, sets process env, runs `docker compose up -d --build` from `$PSScriptRoot` (= `deployed/`) ? uses **top-level compose** |
| Per-agent setup | `<agent>/setup.sh` | Copies agent/*.md to `~/.openclaw/agents/<agent>/`; creates `.env` from `.env.example`; runs `npm install` |
| Per-agent heartbeat | `<agent>/heartbeat.sh` | Reads `CREWCLAW_MONITOR_KEY` from `.env`; pings `crewclaw.com/api/ping/` every 5m |

**Root cause chain:**

1. **Top-level compose is what runs** ? `start-employees.ps1` runs `docker compose up` from `deployed/`, which resolves to `deployed/docker-compose.yml`. This compose file has NO `heartbeat` service and NO `.env` file reference ? secrets come from process env only.

2. **Heartbeat silently exits** ? Per-agent `heartbeat.sh` requires `CREWCLAW_MONITOR_KEY` in a `.env` file inside each agent directory. The top-level compose does NOT mount per-agent `.env` files and does NOT pass `CREWCLAW_MONITOR_KEY` as an env var. Result: `heartbeat.sh` exits immediately with "No CREWCLAW_MONITOR_KEY in .env, skipping monitoring."

3. **Per-agent compose is NOT used** ? `deployed/<agent>/docker-compose.yml` uses `env_file: .env` and has a separate `heartbeat` service. This is the crewclaw.com-generated template, but `start-employees.ps1` bypasses it entirely by running from the parent directory.

4. **CREWCLAW_MONITOR_KEY is never configured** ? Not in Bitwarden secret fetch list in `start-employees.ps1`. Not passed to containers. Not in any `.env.example` that was checked. The heartbeat service that would register agents on `crewclaw.com` dashboard never fires.

5. **Containers run `node bot-telegram.js`** ? Confirmed via `docker inspect`. Bot starts, connects to Telegram via the `grammy` library, and calls `openclaw agent --agent api-integration-specialist --message ...` on each message. The `openclaw agent` CLI subcommand **exists and works** (verified: `agent --help` shows valid options).

6. **CONTRADICTION:** Bot calls `openclaw agent --agent api-integration-specialist` but the installed openclaw only has agent `main`. The `api-integration-specialist` agent was registered via `setup.sh` copying markdown files to `~/.openclaw/agents/api-integration-specialist/` ? but this setup.sh was never run in the Docker context. The Dockerfile `npm install` only installs node deps; it does not run `setup.sh`. Therefore the agent identity inside the container is unregistered with openclaw.

| Root Cause | Severity | Status |
|---|---|---|
| CREWCLAW_MONITOR_KEY never set ? heartbeat never pings crewclaw.com dashboard | MEDIUM | CONFIRMED |
| Per-agent `setup.sh` not run in Dockerfile ? openclaw agent `api-integration-specialist` (et al.) not registered inside containers | HIGH | CONFIRMED |
| `openclaw agent --agent <non-main>` call inside container will fail (agent not registered) | HIGH | INFERRED ? not live-tested but follows from above |
| Per-agent docker-compose.yml bypassed by top-level compose | LOW (by design) | CONFIRMED ? intentional architecture |

#### 4. Runtime Naming: Sparky vs main

| Check | Result | Detail |
|---|---|---|
| `openclaw agent --message 'what is your name?'` | **PASS** | Response: "I'm Sparky! Tony's brilliant companion..." |
| `openclaw.json` agents.defaults.name | **NOT SET** | No `name` field in defaults or main agent block |
| `~/.openclaw/agents/main/` directory | **PASS** | Agent ID is `main`; SOUL.md not present in agent dir (only `auth-profiles.json`, `models.json`) |
| `openclaw health` output | **PASS** | Shows `Agents: main (default)` |
| SOUL.md / identity definition | **UNLOCATED** | No SOUL.md in `~/.openclaw/agents/main/agent/`. Sparky name is in model/system prompt, not a file |
| References in docs | **MIXED** | AI-Project-Manager STATE.md: "Sparky" used consistently. open--claw STATE.md: "Sparky" in some entries but "main" used in CLI context ? appropriate |
| CrewClaw employee SOUL.md files | **GENERIC** | e.g. `api-integration-specialist/agents/.../SOUL.md` says "Name: Api Integration Specialist" ? no Sparky reference, correct isolation |

**Verdict: Naming state is CONSISTENT but source of "Sparky" identity is OPAQUE.**
- Runtime agent ID is `main`. Display name "Sparky" comes from the model's system prompt (not a config file or SOUL.md on disk).
- No naming conflict with CrewClaw employees ? they use separate agent IDs.
- Drift risk: if gateway is reset/re-onboarded, Sparky's name/personality must be re-established via conversation (no persistent SOUL.md file guards it).

### Verdict

| Domain | Status | Severity |
|---|---|---|
| OpenMemory Cursor-side (health + search) | **PASS** | ? |
| OpenClaw runtime memory (FTS) | **PARTIAL** | LOW |
| OpenClaw runtime memory (embeddings/vector) | **FAIL** | MEDIUM |
| mem0-bridge skill ? OpenMemory bridge | **NOT PROVEN** | HIGH |
| CrewClaw containers running | **PASS** | ? |
| CrewClaw heartbeat/dashboard registration | **FAIL** | MEDIUM |
| CrewClaw agent identity inside containers | **FAIL** | HIGH |
| Sparky/main naming consistency | **PASS (opaque source)** | LOW |
| open--claw STATE.md in compliance | **FAIL** | MEDIUM (1903 lines ? far exceeds 500-line policy) |

### Blockers

- **BLOCKER A ? CrewClaw agents not registered in OpenClaw inside containers**: `setup.sh` never runs during `docker build`; the `openclaw agent --agent api-integration-specialist` call in `bot-telegram.js` will fail silently or use wrong agent.
- **BLOCKER B ? OpenMemory ? OpenClaw runtime bridge: not proven**: mem0-bridge skill points to localhost:8080 (not OpenMemory proxy); embeddings provider has no API key.
- **BLOCKER C ? open--claw STATE.md rolling archive compliance**: 1903 lines (target: ?500). Needs archiving before Phase 1.

### Fallbacks Used
None ? verification only.

### Cross-Repo Impact
- AI-Project-Manager STATE.md: this entry (current file).
- open--claw STATE.md: needs mirror entry + rolling archive pass before Phase 1 execution.

### Decisions Captured
- mem0-bridge skill target is mem0 MCP (localhost:8080), NOT OpenMemory hosted MCP (localhost:8766 proxy). Two separate systems. Any "OpenClaw ? OpenMemory" bridge is currently unbuilt.
- CrewClaw top-level compose is the canonical deploy path; per-agent composes are crewclaw.com templates (reference only, not used in production).
- Sparky identity lives in model system prompt only ? no on-disk SOUL.md in `~/.openclaw/agents/main/agent/`.

### Pending Actions
1. Phase 1 planning (PLAN tab): decide memory bridge architecture before any code changes.
2. Fix BLOCKER A: add `setup.sh` execution or equivalent agent registration step to Dockerfiles.
3. Fix BLOCKER B: configure embedding provider OR redesign memory bridge to use OpenMemory proxy.
4. Fix BLOCKER C: archive open--claw STATE.md before Phase 1 execution begins.

### What Remains Unverified
- Whether `openclaw agent --agent api-integration-specialist` actually errors inside a container (inferred only; live test needed).
- Whether Sparky's "Sparky" name survives a full gateway wipe + re-onboard (no config file found).
- MCP_HEALTH.md: entries from 2026-03-19 may be stale re: MCP server availability.

### What's Next
Phase 1 readiness: **NO-GO pending blockers A, B, C.**
Recommended sequence: (1) archive open--claw STATE.md [BLOCKER C], (2) design memory bridge in PLAN tab, (3) fix CrewClaw agent registration [BLOCKER A], (4) execute Phase 1.

---

## 2026-03-29 14:00 - Phase 1A: CrewClaw Worker Stabilization

### Goal
Fix Blocker A (CrewClaw workers unable to call OpenClaw gateway), Blocker C (open--claw STATE.md rolling archive compliance), and truth drift in HANDOFF.md.

### Scope
- open--claw/open-claw/employees/deployed/ (docker-compose.yml, all 5 Dockerfiles, entrypoint.sh, bot-telegram.js)
- open--claw/open-claw/employees/deployed/start-employees.ps1
- open--claw/docs/ai/STATE.md (archival)
- open--claw/docs/ai/archive/ (state-log-full-history-2026-02-18-to-2026-03-21.md, README.md)
- open--claw/docs/ai/HANDOFF.md
- AI-Project-Manager/docs/ai/STATE.md (this file, rolling archive + mirror)
- AI-Project-Manager/docs/ai/archive/state-log-2026-03-21.md (new)

### Commands / Tool Calls
- docker ps --filter name=crewclaw (container states)
- docker exec crewclaw-* openclaw --version (version probe)
- docker exec crewclaw-* openclaw agent --agent api-integration-specialist --message 'health ping' (FAIL baseline)
- Read/write: all 5 Dockerfiles, docker-compose.yml, start-employees.ps1, entrypoint.sh, bot-telegram.js
- Get-Content STATE.md count verification (open--claw: 2864?172 lines; AI-PM: 587 lines)
- PowerShell archive slice

### Changes

**Blocker A ? CrewClaw Docker fixes:**
| Component | Before | After |
|---|---|---|
| Base image | node:20-slim | node:22-slim |
| openclaw install | npm install -g openclaw (stub v0.0.1) | npm install -g openclaw@2026.3.13 --ignore-scripts |
| git + ca-certificates | not installed | apt-get install -y git ca-certificates |
| SSH?HTTPS git rewrite | missing | git config --global url.'https://github.com/'.insteadOf 'ssh://git@github.com/' |
| entrypoint.sh | none | writes openclaw.json (gateway remote mode) from env vars |
| bot-telegram.js agent target | openclaw agent --agent api-integration-specialist | openclaw agent --agent main (only registered agent) |
| Session IDs | single session | per-user: telegram-worker-{persona}-{userId} |
| Named volumes | none | crewclaw-openclaw-{agent}:/root/.openclaw (device identity persistence) |
| docker-compose.yml env | partial (no gateway vars) | OPENCLAW_GATEWAY_URL, OPENCLAW_GATEWAY_TOKEN, OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 |
| start-employees.ps1 | no gateway token/URL fetch | fetches OPENCLAW_GATEWAY_TOKEN via bws; sets OPENCLAW_GATEWAY_URL |

**Blocker C ? open--claw STATE.md archive:**
| Item | Before | After |
|---|---|---|
| STATE.md lines | 2864 | 172 |
| Archive file created | ? | docs/ai/archive/state-log-full-history-2026-02-18-to-2026-03-21.md (2776 lines) |
| archive/README.md | stale | updated with new archive entry |
| HANDOFF.md | 2026-03-21, stale WhatsApp claim | 2026-03-29, truthful channel/worker state |

**AI-PM STATE.md archive:**
- state-log-2026-03-21.md: 3 entries (13:30, 18:00, 19:00) archived (269 lines)
- Current file: archived entries removed, Phase 0 + this entry retained

### Evidence

| Check | Result |
|---|---|
| docker exec openclaw --version (before) | FAIL ? stub v0.0.1 or npm not found |
| node:22-slim base image | PASS |
| openclaw@2026.3.13 installed in build | PASS ? version matches gateway |
| entrypoint.sh writes openclaw.json | PASS ? validated in all 5 containers |
| Gateway config mode=remote accepted | PASS (prior config: Unrecognized key "url" fixed to nested remote.url) |
| Named volumes declared in compose | PASS ? 5 volumes in volumes: section |
| open--claw STATE.md line count | PASS ? 172 lines (target ?500) |
| open--claw archive README updated | PASS |
| HANDOFF.md WhatsApp stale claim | FIXED ? now states "401 Unauthorized ? needs QR re-scan" |
| AI-PM STATE.md line count post-archive | ~295 lines (PASS) |

### Verdict
**PARTIAL PASS** ? All code changes implemented and validated by inspection. Container live-testing blocked by missing Telegram bot tokens (bws not available in this session). Device pairing requires first-run manual step.

### Blockers
- **WhatsApp 401**: user must re-scan QR (pnpm openclaw channels login --channel whatsapp in WSL)
- **Bitwarden secret ID**: OPENCLAW_GATEWAY_TOKEN_SECRET_ID placeholder in start-employees.ps1 must be updated with real Bitwarden secret UUID
- **Device pairing**: after start-employees.ps1 runs successfully, user must run openclaw devices approve <id> for each of the 5 workers (one-time per named volume)
- **Memory bridge (Phase 1B)**: deferred ? OpenClaw ? OpenMemory bridge not implemented

### Fallbacks Used
- SSH?HTTPS git rewrite (fallback for containers without SSH keys)
- --ignore-scripts npm flag (fallback to skip native build failures in Baileys/libsignal)
- Named volumes (fallback to persist device identity without pre-baking)

### Cross-Repo Impact
- open--claw: STATE.md archived, HANDOFF.md updated, all 5 employee dirs modified, docker-compose.yml modified, start-employees.ps1 modified
- AI-Project-Manager: this STATE entry + state-log-2026-03-21.md archive

### Decisions Captured
- Agent target changed from individual agent IDs to main ? only main is registered on the host gateway; per-employee agent IDs require setup.sh to run (not done in Docker context).
- Named volumes chosen over pre-baked identity ? allows gateway admin to approve once per volume lifetime; volumes survive container rebuilds.
- --ignore-scripts chosen over full build ? Baileys/libsignal not needed for Telegram-only bot path.
- Memory bridge explicitly deferred to Phase 1B per scope constraint.

### Pending Actions
1. User: update OPENCLAW_GATEWAY_TOKEN_SECRET_ID in start-employees.ps1 with real Bitwarden secret UUID.
2. User: run start-employees.ps1 (requires bws + Bitwarden vault unlocked).
3. User: run openclaw devices list on host gateway; approve each crewclaw-* device.
4. User: re-scan WhatsApp QR (unrelated to Phase 1A but remains open blocker).
5. Phase 1B: design OpenClaw ? OpenMemory memory bridge architecture.

### What Remains Unverified
- Live end-to-end test: Telegram message ? bot-telegram.js ? openclaw agent --agent main ? gateway ? response (blocked by Telegram tokens not available in this session)
- Whether OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 is sufficient for ws:// (not wss://) connection from container to host gateway

### What's Next
User completes pending actions 1-3 above (Bitwarden + deploy + device approval). Then: live smoke test from Telegram ? CrewClaw bot ? Sparky response. If PASS: Phase 1A COMPLETE; proceed to Phase 1B memory bridge design.

---

## 2026-03-29 15:00 - Workflow governance update: turbulence promotion, archival policy, model selection

### Goal
Implement minimum workflow changes to ensure unresolved AGENT turbulence is reliably surfaced in HANDOFF.md, replace the blunt ~500 line archive limit with a token/size-first policy, and require PLAN to explicitly justify model selection with rationale.

### Scope
- .cursor/rules/10-project-workflow.md
- docs/ai/CURSOR_WORKFLOW.md
- docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md
- AGENTS.md
- docs/ai/HANDOFF.md
- docs/ai/STATE.md (this entry)

### Commands / Tool Calls
- Read: AGENTS.md, CURSOR_WORKFLOW.md, TAB_BOOTSTRAP_PROMPTS.md, 00-global-core.md, 10-project-workflow.md, STATE.md, HANDOFF.md, DECISIONS.md, PATTERNS.md, CONTEXT_WINDOW_MONITORING.md
- StrReplace: 10-project-workflow.md (3 changes), CURSOR_WORKFLOW.md (1 change), TAB_BOOTSTRAP_PROMPTS.md (2 changes), AGENTS.md (1 change)
- Write: HANDOFF.md (full rewrite with new structure)

### Changes

| File | Change |
|---|---|
| 10-project-workflow.md | Model selection matrix + rationale requirement in AGENT prompt (3rd line); turbulence promotion rule added to AGENT contract; ~500 lines replaced with 140KB/180KB size policy + ~800/1000 line proxies |
| CURSOR_WORKFLOW.md | PLAN output requirement updated: rationale line required; explicit model choices named |
| TAB_BOOTSTRAP_PROMPTS.md | PLAN tab: model policy rewritten with justification requirement; AGENT tab header: removed implicit Sonnet 4.6 default bias |
| AGENTS.md | Added turbulence promotion requirement to Agent contract |
| HANDOFF.md | Full rewrite: date updated to 2026-03-29; WhatsApp staleness fixed; added ? Recent Unresolved Issues (4 items); added ? Standing Constraints (5 items) |

### Evidence

| Check | Result |
|---|---|
| 10-project-workflow.md model policy update | PASS ? added rationale requirement + Composer2/Sonnet 4.6/Opus 4.6 matrix |
| 10-project-workflow.md turbulence promotion rule | PASS ? added to AGENT execution contract |
| 10-project-workflow.md archive policy | PASS ? ~500 lines replaced with 140KB/180KB + ~800/1000 proxy |
| CURSOR_WORKFLOW.md model wording | PASS ? rationale line + explicit choices required |
| TAB_BOOTSTRAP_PROMPTS.md PLAN tab | PASS ? justification requirement added to model policy |
| TAB_BOOTSTRAP_PROMPTS.md AGENT tab header | PASS ? removed "Sonnet 4.6 non-thinking" implicit default |
| AGENTS.md turbulence promotion | PASS ? bullet added to Agent contract |
| HANDOFF.md staleness fix | PASS ? WhatsApp now correctly states 401/QR-rescan |
| HANDOFF.md new sections | PASS ? Recent Unresolved Issues + Standing Constraints added |
| CONTEXT_WINDOW_MONITORING.md | No change needed ? already authoritative; 10-project-workflow.md now references it |
|  0-global-core.md | No change needed ? delegates correctly to 10-project-workflow.md |

### Verdict
READY ? All five required changes implemented and consistent across docs.

### Blockers
None.

### Fallbacks Used
None.

### Cross-Repo Impact
Governance-only change. open--claw HANDOFF.md was updated separately in Phase 1A commit. No open--claw changes needed for this governance update.

### Decisions Captured
- Archive policy: token/size-first (CONTEXT_WINDOW_MONITORING.md thresholds) is authoritative. Line count (~800 soft, ~1000 hard) is a practical proxy only ? do not trigger archive on line count alone if content is within KB target.
- Model selection: PLAN must explicitly choose and justify. No silent defaults. Composer2 non-thinking is the default when no complexity flag is present; Sonnet 4.6 non-thinking for medium complexity; Sonnet 4.6 thinking for reasoning tasks; Opus 4.6 thinking for novel/high-ambiguity only.
- Turbulence promotion: AGENT must update HANDOFF.md ? Recent Unresolved Issues when open issues survive a task block, not only STATE.md.

### Pending Actions
None for this governance block. Open operational items in HANDOFF.md ? Recent Unresolved Issues.

### What Remains Unverified
- Whether PLAN tabs in existing sessions will adopt the new rationale requirement without re-bootstrapping (requires session restart to take effect).

### What's Next
PLAN to use new model-selection rationale format in next AGENT prompt. AGENT to consult HANDOFF.md ? Recent Unresolved Issues at start of next task block.

---

## 2026-03-29 16:00 ? Governance consistency pass: source-priority unification + HANDOFF routing fix

### Goal
Verify all recent governance changes are present and internally consistent, unify PLAN source-of-truth priority across all three workflow docs, and fix the HANDOFF.md agent-routing entry that read as a permanent architectural constraint.

### Scope
- docs/ai/CURSOR_WORKFLOW.md
- .cursor/rules/10-project-workflow.md
- docs/ai/HANDOFF.md
- docs/ai/STATE.md (Phase Status table + this entry)

### Commands / Tool Calls
- Read: AGENTS.md, 10-project-workflow.md, CURSOR_WORKFLOW.md, TAB_BOOTSTRAP_PROMPTS.md, HANDOFF.md, STATE.md, CONTEXT_WINDOW_MONITORING.md
- Shell: file size / line count check (PowerShell)
- StrReplace: CURSOR_WORKFLOW.md (source priority), 10-project-workflow.md (item 6 wording), HANDOFF.md (routing entry moved)
- Shell: STATE.md Phase Status table update

### Changes

| File | Change |
|---|---|
| CURSOR_WORKFLOW.md | Context source priority: 7-item divergent list ? 6-item canonical list matching AGENTS.md and 10-project-workflow.md. HANDOFF.md added at position 4; PROJECT_LONGTERM_AWARENESS.md and CONTEXT_WINDOW_MONITORING.md moved to a "Supporting planning references" note below the list |
| 10-project-workflow.md | Item 6: "Chat history / pasted artifacts (last resort)" ? "Chat history / @Past Chats ? last resort only" (matches AGENTS.md exactly) |
| HANDOFF.md | Removed openclaw agent --agent main from ? Standing Constraints; added ? Current Worker Routing (temporary workaround ? Phase 1B item) under ?2 Runtime highlights, clearly marking it as a gap not a design |
| STATE.md | Added Phase 1A row to Phase Status table; this entry |

### Evidence

| Check | Result |
|---|---|
| 10-project-workflow.md: Line 3 Rationale requirement | PASS ? present |
| 10-project-workflow.md: model selection matrix (Composer2/Sonnet 4.6/Opus 4.6) | PASS ? present |
| 10-project-workflow.md: turbulence promotion rule | PASS ? present |
| 10-project-workflow.md: 140KB/180KB archive thresholds + ~800/1000 line proxy | PASS ? present |
| HANDOFF.md: ? Recent Unresolved Issues | PASS ? present (4 items) |
| HANDOFF.md: ? Standing Constraints | PASS ? present (4 items after routing entry removed) |
| TAB_BOOTSTRAP_PROMPTS.md: model policy + Rationale line | PASS ? present |
| CURSOR_WORKFLOW.md source priority: was 7-item (missing HANDOFF.md, had ops docs inline) | FAIL ? FIXED |
| 10-project-workflow.md item 6: "pasted artifacts" vs @Past Chats | FAIL ? FIXED |
| HANDOFF.md routing entry read as permanent constraint | FAIL ? FIXED ? moved to Current Worker Routing subsection with explicit "temporary workaround" label |
| STATE.md Phase Status table: Phase 1A row missing | FAIL ? FIXED |
| STATE.md ? HANDOFF.md WhatsApp status alignment | PASS ? both say 401 Unauthorized / QR re-scan required |
| STATE.md ? HANDOFF.md CrewClaw status alignment | PASS ? both say pending bws deploy + device approval |
| STATE.md file size: 33.2 KB / ~8500 tokens | PASS ? well within 140KB target |
| HANDOFF.md file size: 4.4 KB | PASS ? well within 16KB target |
| No conflicting PLAN source-priority list remains | PASS ? AGENTS.md, 10-project-workflow.md, CURSOR_WORKFLOW.md now identical order |

### Verdict
READY ? All four targeted fixes applied. All governance changes from previous session verified present. No deeper contradictions found.

### Blockers
None.

### Fallbacks Used
- PowerShell String.Replace() for STATE.md Phase Status table (StrReplace could not match due to encoding ? fallback succeeded).

### Cross-Repo Impact
None ? governance-only changes in AI-Project-Manager.

### Decisions Captured
- PROJECT_LONGTERM_AWARENESS.md and CONTEXT_WINDOW_MONITORING.md are supporting planning references, not part of the authoritative source-priority list. This distinction is now explicit in CURSOR_WORKFLOW.md.
- Worker routing workaround (--agent main) is a Phase 1B item, not a standing architectural constraint. Documented as such in HANDOFF.md.

### Pending Actions
None for this block. Open operational items in HANDOFF.md ? Recent Unresolved Issues.

### What Remains Unverified
- Whether existing PLAN sessions will pick up the source-priority unification without re-bootstrapping from TAB_BOOTSTRAP_PROMPTS.md.

### What's Next
PLAN: use updated source-priority order (HANDOFF.md at position 4, no ops docs in the list) on next session bootstrap. AGENT: Phase 1A completion ? bws deploy + device approval smoke test.

---

## 2026-03-29 16:35 ? Phase 0A: CrewClaw baseline + deployment-path verification

### Goal

Prove the active CrewClaw deployment path, capture the current dashboard-access baseline, and classify whether the worker fleet is blocked by architecture conflict or by incomplete Bitwarden-backed activation.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `open--claw/AGENTS.md`
- `open--claw/open-claw/employees/deployed/start-employees.ps1`
- `open--claw/open-claw/employees/deployed/docker-compose.yml`
- `open--claw/open-claw/employees/deployed/*/docker-compose.yml`
- `open--claw/open-claw/employees/deployed/*/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/api-integration-specialist/{Dockerfile,bot-telegram.js,entrypoint.sh}`
- Live Docker state for `crewclaw-financial-analyst`

### Commands / Tool Calls

- `ReadFile` ? `D:\github\AI-Project-Manager\AGENTS.md`
- `ReadFile` ? `D:\github\open--claw\AGENTS.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\.cursor\rules\00-global-core.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\.cursor\rules\05-global-mcp-usage.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\.cursor\rules\10-project-workflow.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\.cursor\rules\20-project-quality.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\docs\ai\STATE.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\docs\ai\HANDOFF.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\docs\ai\PLAN.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\docs\ai\memory\DECISIONS.md`
- `ReadFile` ? `D:\github\AI-Project-Manager\docs\ai\memory\PATTERNS.md`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\start-employees.ps1`
- `user-Clear_Thought_1_5-clear_thought` (`causal_analysis`)
- `user-serena-activate_project` (`D:\github\open--claw`)
- `user-serena-check_onboarding_performed`
- `ListMcpResources`
- `user-openmemory-search-memory`
- `ReadFile` ? `agent-browser` skill
- `user-serena-initial_instructions`
- `user-serena-onboarding`
- `user-serena-search_for_pattern`
- `Shell` ? `Get-ChildItem -Force "D:\github\open--claw\open-claw\employees\deployed"`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\docker-compose.yml`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\api-integration-specialist\Dockerfile`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\api-integration-specialist\bot-telegram.js`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\api-integration-specialist\entrypoint.sh`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\api-integration-specialist\docker-compose.yml`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\financial-analyst\heartbeat.sh`
- `ReadFile` ? `D:\github\open--claw\open-claw\employees\deployed\financial-analyst\docker-compose.yml`
- `rg` ? `crewclaw\.com|CREWCLAW_MONITOR_KEY|waiting for first ping|dashboard`
- `Shell` ? `docker compose ps`
- `Shell` ? `docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}"`
- `Shell` ? `docker inspect crewclaw-financial-analyst`
- `Shell` ? `agent-browser --version`
- `Subagent` (`browser-use`) ? CrewClaw dashboard baseline attempt
- `Shell` ? `docker logs crewclaw-financial-analyst --tail 100`
- `Shell` ? `git status --short` (`D:\github\AI-Project-Manager`)
- `Shell` ? `git status --short` (`D:\github\open--claw`)
- `Shell` ? `$env:BWS_ACCESS_TOKEN | ForEach-Object { if ($_){'SET'} else {'EMPTY'} }`
- `Shell` ? `bws --version`
- `Shell` ? `docker inspect --format "{{.Config.Image}}|{{.Config.Labels.com.docker.compose.project.config_files}}|{{.State.Status}}|{{.RestartCount}}" crewclaw-financial-analyst`
- `Shell` ? `[System.Environment]::GetEnvironmentVariable('BWS_ACCESS_TOKEN','User')`
- `firecrawl_scrape` ? `https://www.crewclaw.com/app/my-agents`
- `WebFetch` ? `https://www.crewclaw.com/app/my-agents`

### Changes

Appended this verification block to `AI-Project-Manager/docs/ai/STATE.md`. No runtime code changed yet.

### Evidence

| Check | Result | Detail |
|---|---|---|
| `ReadFile` / requested governance docs | PASS | All requested AI-PM governance docs and both `AGENTS.md` files loaded successfully. |
| `user-Clear_Thought_1_5-clear_thought` | PASS (low-value output) | Tool returned a minimal causal-analysis shell; usable outcome came mainly from repo evidence rather than the tool graph. |
| `user-serena-activate_project` | PASS | Activated `open--claw` project. |
| `user-serena-check_onboarding_performed` | FAIL | Serena reported onboarding not yet performed for this project. |
| `ListMcpResources` | FAIL | Returned no MCP resources. |
| `user-openmemory-search-memory` | PASS | Query succeeded but returned 0 related memories. |
| `user-serena-search_for_pattern` | PASS | Found prior repo-tracked evidence showing the placeholder gateway-token issue and prior dashboard assumptions. |
| `user-serena-read_file` on `open-claw/employees/deployed/*` | FAIL | Serena safety layer refused ignored-path reads; fallback to direct `ReadFile` was required. |
| `Get-ChildItem -Force "D:\github\open--claw\open-claw\employees\deployed"` | PASS | Confirmed top-level shared deployment root plus 5 generated per-agent subfolders. |
| `ReadFile` top-level `deployed/docker-compose.yml` | PASS | Shared compose injects env from process vars only; no `.env` file dependency. |
| `ReadFile` per-agent `docker-compose.yml` | PASS | Generated per-agent templates still depend on `.env` and separate `heartbeat` services. |
| `ReadFile` `financial-analyst/heartbeat.sh` | PASS | Heartbeat requires `CREWCLAW_MONITOR_KEY` from local `.env`, proving dashboard ping is absent from the shared runtime path. |
| `docker compose ps` | FAIL | No active services from the current top-level compose in this shell; Compose warned that required env vars were unset in the current process. |
| `docker ps --format ...` | FAIL | No `crewclaw-*` containers currently running; only unrelated `seatrush-*` containers were up. |
| `docker inspect crewclaw-financial-analyst` | PASS | Existing container object proved prior launch came from `D:\github\open--claw\open-claw\employees\deployed\docker-compose.yml` and used named volume persistence. |
| `docker logs crewclaw-financial-analyst --tail 100` | FAIL | Container crash-looped with `Error: Empty token!` from `grammy`, proving `TELEGRAM_BOT_TOKEN` was blank at runtime. |
| `agent-browser --version` | FAIL | `agent-browser` CLI is not installed in this environment. |
| `Subagent` (`browser-use`) | FAIL | Subagent reported no browser tools available; could not perform authenticated dashboard automation. |
| `firecrawl_scrape https://www.crewclaw.com/app/my-agents` | PASS | Page redirected to `https://www.crewclaw.com/login`; fallback proved dashboard is not publicly readable without login. |
| `WebFetch https://www.crewclaw.com/app/my-agents` | PASS (limited) | Returned public site/login-marketing content, not per-worker dashboard state. |
| `git status --short` in `AI-Project-Manager` | PASS | Only pre-existing dirty file: `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`. |
| `git status --short` in `open--claw` | PASS | Deployment subtree is untracked (`?? open-claw/employees/`); no tracked-file conflicts found. |
| `$env:BWS_ACCESS_TOKEN` in current shell | FAIL | Current shell env is empty; this session was not launched via `bws run`. |
| `bws --version` | PASS | Bitwarden CLI available: `bws 2.0.0`. |
| User-registry `BWS_ACCESS_TOKEN` check | PASS | Registry copy exists, so `start-employees.ps1` can still attempt Bitwarden-backed activation. |
| `start-employees.ps1` gateway secret ID | FAIL | Still uses `PLACEHOLDER_OPENCLAW_GATEWAY_TOKEN_SECRET_ID` instead of the active Bitwarden UUID `79f3acf8-c855-4c0d-9726-b40d01278bb6`. |
| Canonical deploy path vs generated path | PASS | No architecture conflict proven: top-level shared compose is the active/canonical runtime path; per-agent `.env` composes are generated templates, not runtime truth. |
| Dashboard baseline for all 5 workers | FAIL | Could not access authenticated CrewClaw dashboard state in this session; public fallback only proved login is required. |

### Verdict

PARTIAL ? no architecture-stop conflict found, but Phase 0 activation is still blocked operationally by the placeholder gateway-token UUID, missing browser automation, and at least one worker crash-loop caused by an empty Telegram token.

### Blockers

- `start-employees.ps1` still uses a placeholder for `OPENCLAW_GATEWAY_TOKEN_SECRET_ID`.
- Browser automation is unavailable in this session, so authenticated CrewClaw dashboard baseline could not be captured.
- `financial-analyst` crash-loops with blank `TELEGRAM_BOT_TOKEN`, so representative-worker verification cannot pass until Bitwarden-backed redeploy succeeds.

### Fallbacks Used

- Serena ignored-path read failure ? fallback to direct `ReadFile`.
- Browser automation failure (`browser-use` + missing `agent-browser`) ? fallback to `firecrawl_scrape` and `WebFetch` for unauthenticated page-state proof.

### Cross-Repo Impact

- `open--claw` runtime truth was reclassified: top-level `deployed/docker-compose.yml` is canonical; per-agent `.env` compose files remain generated reference templates only.

### Decisions Captured

- The generated per-agent CrewClaw deployment path does not currently conflict with the Bitwarden-native shared path; it is legacy/generated scaffolding, not active runtime truth.
- `waiting for first ping` cannot be blamed on dashboard alone: the current shared path omits heartbeat entirely, and the representative worker is also failing earlier with an empty Telegram token.

### Pending Actions

1. Patch `start-employees.ps1` to use the real Bitwarden UUID for `OPENCLAW_GATEWAY_TOKEN`.
2. Fail closed on missing required Bitwarden secrets so workers do not start with blank tokens.
3. Re-run deployment and verify `financial-analyst` first.
4. Decide whether dashboard compatibility remains required, then either restore heartbeat through the shared path or document its intentional removal.

### What Remains Unverified

- Authenticated CrewClaw dashboard state for all five workers.
- Whether the registry-backed Bitwarden token is still sufficient for a full `bws secret get` deployment in this session.
- Device pairing, routing validity, and Telegram end-to-end behavior after a corrected redeploy.

### What's Next

Patch the shared deployment script with the real Bitwarden gateway-token UUID, enforce hard failure on missing worker secrets, then redeploy and verify `financial-analyst` as the representative worker.

---

## 2026-03-29 18:05 ? Phase 0B: CrewClaw Bitwarden-native activation + representative proof

### Goal

Activate the shared Bitwarden-native CrewClaw deployment, prove `financial-analyst` across the required runtime states, and generalize the resulting classification to the other four workers without assuming containers being up means the fleet is actually working.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- `open--claw/open-claw/employees/deployed/start-employees.ps1`
- `open--claw/open-claw/employees/deployed/docker-compose.yml`
- Live Docker workers: all five `crewclaw-*` containers
- Host gateway runtime via WSL `~/openclaw-build`

### Commands / Tool Calls

- `ApplyPatch` ? `open--claw/open-claw/employees/deployed/start-employees.ps1`
- `ApplyPatch` ? `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed\start-employees.ps1"` (initial run)
- `ApplyPatch` ? `open--claw/open-claw/employees/deployed/start-employees.ps1` (PowerShell interpolation fix)
- `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed\start-employees.ps1"` (retry)
- `docker exec crewclaw-financial-analyst sh -lc '...TELEGRAM_BOT_TOKEN...OPENCLAW_GATEWAY_TOKEN...'`
- `docker exec crewclaw-financial-analyst node -e "fetch('http://host.docker.internal:18792/')..."`
- `docker logs crewclaw-financial-analyst --tail 50`
- `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw devices list"`
- `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw nodes status"`
- `docker exec crewclaw-financial-analyst openclaw agent --agent main --message "phase-0 direct probe" --timeout 60`
- `user-Context7-resolve-library-id` ? `OpenClaw`
- `user-Context7-query-docs` ? device pairing / remote mode / timeout docs
- `docker exec crewclaw-financial-analyst node -e "fetch('https://api.telegram.org/bot'+process.env.TELEGRAM_BOT_TOKEN+'/getMe')..."`
- `docker update --memory 1g crewclaw-financial-analyst`
- `docker exec crewclaw-financial-analyst sh -lc 'cat /sys/fs/cgroup/memory.max'`
- `docker exec -e NODE_OPTIONS=--max-old-space-size=1536 crewclaw-financial-analyst openclaw agent --agent main --message "phase-0 direct probe" --timeout 60`
- `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw devices list --json"`
- `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw devices approve 155b2556-22a9-4efa-aec7-3246b55f0393"`
- `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"` (failed)
- `$env:BWS_ACCESS_TOKEN = [System.Environment]::GetEnvironmentVariable('BWS_ACCESS_TOKEN','User'); bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"` (passed)
- `wsl bash -lc "journalctl --user -u openclaw-gateway.service -n 120 --no-pager"`
- `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw gateway status"`
- `rg` ? `const agentId = "main"|OPENCLAW_GATEWAY_URL=|OPENCLAW_GATEWAY_TOKEN=|OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1`
- Batch shell check for `api-integration-specialist`, `code-reviewer`, `frontend-developer`, `overnight-coder`:
  - container status
  - masked env presence
  - gateway health fetch
  - Telegram `getMe`
- `ApplyPatch` ? `open--claw/open-claw/employees/deployed/docker-compose.yml`
- `pwsh -NoProfile -File "D:\github\open--claw\open-claw\employees\deployed\start-employees.ps1"` (redeploy after compose fix)
- `docker exec crewclaw-{api-integration-specialist,code-reviewer,frontend-developer,overnight-coder} openclaw agent --agent main --message "pairing probe" --timeout 60`
- `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw devices approve <requestId>"` (four approvals)

### Changes

| File | Change |
|---|---|
| `open--claw/open-claw/employees/deployed/start-employees.ps1` | Replaced placeholder gateway-token UUID with the live Bitwarden UUID; changed missing gateway/worker secrets from WARN/blank start to hard failure; fixed PowerShell string interpolation bug. |
| `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md` | Added repo-tracked inventory with active Bitwarden names + UUIDs only; `CREWCLAW_MONITOR_KEY` recorded as reserved with UUID pending. |
| `open--claw/open-claw/employees/deployed/docker-compose.yml` | Raised all worker memory limits from `512M` to `2G` and added `NODE_OPTIONS=--max-old-space-size=1536` to prevent worker-local heap OOM before gateway routing. |
| `AI-Project-Manager/docs/ai/STATE.md` | Updated summary and appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| `start-employees.ps1` first run | FAIL | Parser error at `"$name: token fetched"` proved the script had a latent PowerShell interpolation bug. |
| `start-employees.ps1` after syntax fix | PASS | Loaded `BWS_ACCESS_TOKEN` from User registry, fetched all seven active Bitwarden secrets, rebuilt containers, and brought all five workers `Up`. |
| Secret inventory doc | PASS | Added governance-side Bitwarden inventory with names + UUIDs only; no raw values written. |
| `financial-analyst` token injection | PASS | `TELEGRAM_BOT_TOKEN=SET`, `OPENCLAW_GATEWAY_TOKEN=SET`, `OPENCLAW_GATEWAY_URL=ws://host.docker.internal:18789`. |
| `financial-analyst` container running | PASS | Container logs show `[bot-telegram] financial-analyst bot is running`; `docker inspect` reported `running|0` after redeploy. |
| `financial-analyst` gateway reachable | PASS | In-container fetch to `http://host.docker.internal:18792/` returned `OK`. |
| `financial-analyst` Telegram bot token validity | PASS | Telegram `getMe` returned `ok=true`, username `FINANCE_FRANKY_BOT`. |
| `financial-analyst` initial route probe at original `512M` | FAIL | `openclaw agent` crashed with V8 heap OOM around 250 MB. |
| `financial-analyst` route probe at `1G` | FAIL | Heap OOM moved to ~500 MB, proving the original shared memory cap was too low. |
| `financial-analyst` route probe at `2G` + `NODE_OPTIONS=--max-old-space-size=1536` | PASS (diagnostic) | Worker cleared local OOM and exposed the real gateway error: `pairing required`. |
| `financial-analyst` device pairing | PASS | `devices list --json` showed pending request `155b2556-22a9-4efa-aec7-3246b55f0393`; `devices approve` succeeded; later `devices list --json` showed the device under `paired`. |
| `financial-analyst` post-pair gateway routing | FAIL | Same direct probe no longer hit pairing/OOM, but gateway timed out after 90s and worker fell back to embedded execution. |
| Host gateway restart via `bws run` | FAIL | First attempt failed with `Missing access token` because `bws run` only saw process env, not registry env. |
| Host gateway restart with registry token copied into process env | PASS | Canonical restart script refreshed `.gateway-env` and restarted the systemd gateway successfully. |
| Host gateway route after restart | FAIL | Host `pnpm openclaw agent --agent main ...` still timed out via gateway after 90s. |
| Gateway service logs | FAIL | Journal showed the live failure inside the host process: `[agent/embedded] Profile anthropic:default timed out` and `FailoverError: LLM request timed out.` OpenRouter fallback was then unavailable. |
| Dashboard compatibility baseline | FAIL | Shared path still has no heartbeat service; generated per-agent heartbeat remains `.env`-bound; no authenticated dashboard automation was available in this session; no first-ping proof exists. |
| `api-integration-specialist` generalized preconditions | PASS | Running, both tokens injected, gateway health reachable, Telegram bot valid (`API_ANDY_BOT`). |
| `code-reviewer` generalized preconditions | PASS | Running, both tokens injected, gateway health reachable, Telegram bot valid (`CODE_CARL_BOT`). |
| `frontend-developer` generalized preconditions | PASS | Running, both tokens injected, gateway health reachable, Telegram bot valid (`FRONTEND_FELIX_BOT`). |
| `overnight-coder` generalized preconditions | PASS | Running, both tokens injected, gateway health reachable, Telegram bot valid (`OVERNIGHT_OLIVER_BOT`). |
| Other four device-pair trigger | PASS | Each first probe returned `pairing required`; subsequent `devices list --json` showed four pending backend requests. |
| Other four device approvals | PASS | All four pending worker requests were approved successfully. |
| Other four routing classification | FAIL (generalized) | All five workers route to shared host `main` via the same gateway URL/token and the same `agentId = "main"` code path; after pairing, they inherit the same shared host-gateway timeout until the gateway-side model timeout is fixed. |
| Telegram end-to-end message success | FAIL / UNPROVEN | Bot tokens are valid and bots are running, but no real chat/update evidence was available (`financial-analyst` `getUpdates` returned `updates=0`), and gateway-routed execution still times out. |

### Verdict

BLOCKED ? Bitwarden-native activation succeeded up to running + paired workers, but the exact failed step is gateway-routed inference: the host `main` agent times out on the Anthropic model call, so workers fall back locally and true Telegram end-to-end success is not proven. Dashboard `first ping` is also still blocked because the shared deployment has no heartbeat path or active `CREWCLAW_MONITOR_KEY` mapping.

### Blockers

- Shared host gateway run for `main` times out (`[agent/embedded] Profile anthropic:default timed out` / `LLM request timed out` in gateway journal).
- Shared deployment still lacks a Bitwarden-native dashboard heartbeat path; `CREWCLAW_MONITOR_KEY` UUID mapping is still pending.
- Authenticated CrewClaw dashboard baseline could not be captured in this session because browser automation was unavailable and the page requires login.

### Fallbacks Used

- Registry `BWS_ACCESS_TOKEN` ? copied into process env before `bws run` gateway restart.
- Worker-local embedded fallback responses were used only as diagnostics after gateway failures; they were not counted as successful gateway routing.

### Cross-Repo Impact

- `open--claw` deployment files now match the active Bitwarden-native path more closely (`start-employees.ps1`, `docker-compose.yml`).
- `AI-Project-Manager` now carries the authoritative CrewClaw Bitwarden inventory and the updated activation state.

### Decisions Captured

- CrewClaw dashboard compatibility is still treated as a requirement; the absence of heartbeat in the shared path is a live FAIL, not an intentional removal.
- Worker pairing is real for the shared backend clients; the old ?pending device approval? story was partially stale only because it had not been triggered yet in this deployment session.
- The fleet-wide routing blocker is shared-host, not per-worker token wiring: all five route to the same `main` agent and therefore share the same gateway timeout once paired.

### Pending Actions

1. Diagnose/fix the host gateway Anthropic timeout or provide a working fallback model/provider for `main`.
2. Add Bitwarden-native `CREWCLAW_MONITOR_KEY` mapping(s) and a shared heartbeat path if dashboard compatibility remains required.
3. Re-run a real Telegram conversation against at least one paired worker after the gateway timeout is fixed.

### What Remains Unverified

- Authenticated CrewClaw dashboard state for each worker after heartbeat restoration.
- Whether the host Anthropic timeout is network/provider latency, account-level API behavior, or another gateway-side transport issue.
- Real Telegram chat round-trip with user-originated input after shared gateway routing is fixed.

### What's Next

Stay in execution mode only long enough to fix the shared host gateway timeout or wire a working fallback model; do not start memory-bridge or unrelated follow-on work until one paired worker can complete a real gateway-routed Telegram round trip and, if retained, a dashboard heartbeat appears.

---

## 2026-03-29 18:25 ? Phase 0C: Dashboard first-ping verification

### Goal

Verify whether the CrewClaw dashboard is still showing `waiting for first ping` because the shared deployment lacks a live heartbeat path, and determine whether a Bitwarden-backed monitor-key secret exists to restore that contract.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- `open--claw/open-claw/employees/deployed/docker-compose.yml`
- `open--claw/open-claw/employees/deployed/financial-analyst/heartbeat.sh`
- Live shared worker container env for `crewclaw-financial-analyst`

### Commands / Tool Calls

- `user-Clear_Thought_1_5-clear_thought` (`debugging_approach`)
- `ReadFile` ? `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- `ReadFile` ? `open--claw/open-claw/employees/deployed/financial-analyst/heartbeat.sh`
- `ReadFile` ? `open--claw/open-claw/employees/deployed/docker-compose.yml`
- `Shell` ? `bws secret list f14a97bb-5183-4b11-a6eb-b3fe0015fedf`
- `Shell` ? `bws secret list f14a97bb-5183-4b11-a6eb-b3fe0015fedf | Select-String -Pattern 'CREWCLAW|MONITOR|PING|FINANCIAL|FRONTEND|CODE|API|OVERNIGHT'`
- `Shell` ? `docker compose ps`
- `Shell` ? `docker inspect --format "{{.Name}}|{{json .Config.Env}}" crewclaw-financial-analyst`

### Changes

| File | Change |
|---|---|
| `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md` | Updated reserved `CREWCLAW_MONITOR_KEY` row from `UUID pending` to `absent from Bitwarden project`. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Added sharper unresolved blockers: no shared heartbeat path and no `CREWCLAW_MONITOR_KEY` secret in Bitwarden. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this verification block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| `ReadFile` inventory doc | PASS | Inventory still had `CREWCLAW_MONITOR_KEY` only as reserved, not active. |
| `ReadFile` `financial-analyst/heartbeat.sh` | PASS | Generated heartbeat script still requires `CREWCLAW_MONITOR_KEY` from local `.env` and exits early when absent. |
| `ReadFile` shared `docker-compose.yml` | PASS | Shared deployment runs only the five worker services; no heartbeat service or monitor-key env appears anywhere in the canonical compose. |
| `docker compose ps` | PASS | Live shared deployment currently consists only of the five worker containers. |
| `docker inspect ... crewclaw-financial-analyst` | PASS | Live worker env includes gateway/token/bot settings but no `CREWCLAW_MONITOR_KEY`, confirming the running shared path has no dashboard-ping variable to send. |
| `bws secret list f14a97bb-5183-4b11-a6eb-b3fe0015fedf` | PASS | Active Bitwarden project secrets include the worker bot tokens and gateway token, but no `CREWCLAW_MONITOR_KEY` secret exists to inject. |
| `Select-String` on Bitwarden secret names | PASS | Search returned no CrewClaw monitor/ping secret name; only the existing worker/gateway keys were present. |
| Dashboard first-ping contract | FAIL | `waiting for first ping` is still expected because the canonical shared deployment has no heartbeat implementation and no monitor-key secret to drive one. |

### Verdict

BLOCKED ? exact cause proven: the active shared CrewClaw deployment cannot send dashboard pings because it has no heartbeat service/env wiring, and the Bitwarden project currently has no `CREWCLAW_MONITOR_KEY` secret/UUID to inject.

### Blockers

- No heartbeat path in the canonical shared deployment.
- No `CREWCLAW_MONITOR_KEY` secret exists in the active Bitwarden project.
- Authenticated dashboard automation is still unavailable in this session, so the website state cannot be captured directly beyond the user?s report.

### Fallbacks Used

- Browser/dashboard evidence still relies on user-observed state because authenticated browser automation remains unavailable.

### Cross-Repo Impact

- `open--claw`: no code change required for this proof block; canonical compose remains the operative source showing the missing heartbeat.
- `AI-Project-Manager`: inventory, handoff, and state now reflect the exact dashboard blocker.

### Decisions Captured

- Dashboard compatibility remains retained by behavior: until it is explicitly dropped, `waiting for first ping` must be treated as a real failure, not cosmetic drift.
- The next heartbeat fix cannot be implemented Bitwarden-natively until a `CREWCLAW_MONITOR_KEY` secret is created and its UUID is recorded.

### Pending Actions

1. Create the required `CREWCLAW_MONITOR_KEY` Bitwarden secret(s) and capture the UUID(s).
2. Add a shared heartbeat path to the canonical compose using Bitwarden-backed env injection only.
3. Re-verify the dashboard after the first successful ping.

### What Remains Unverified

- Whether CrewClaw expects one shared monitor key or one distinct key per worker.
- The exact per-worker mapping between dashboard tiles and monitor keys.

### What's Next

Create the missing `CREWCLAW_MONITOR_KEY` secret(s) in Bitwarden, then wire a heartbeat path into the shared deployment and re-check the dashboard.

---

## 2026-03-29 20:20 — Phase 0D: Worker activity + Sparky gateway diagnosis

### Goal

Verify whether the five CrewClaw employees are actually active and configured correctly, determine whether the gateway is open, and diagnose the exact cause of Sparky failing with stale OpenAI model errors.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- Live host config: `~/.openclaw/openclaw.json`
- Live host model registry: `~/.openclaw/agents/main/agent/models.json`
- Live host auth store: `~/.openclaw/agents/main/agent/auth-profiles.json`
- Live Docker workers
- Host gateway journal + health

### Commands / Tool Calls

- `user-Clear_Thought_1_5-clear_thought` (`debugging_approach`)
- `user-Context7-resolve-library-id` — `OpenClaw`
- `user-Context7-query-docs` — model config / models.json / auth profile behavior
- `Shell` — `docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw gateway status && printf '\n---\n' && pnpm openclaw health"`
- `Shell` — `wsl bash -lc "journalctl --user -u openclaw-gateway.service -n 120 --no-pager"`
- `Shell` — Python inspection of `~/.openclaw/agents/main/agent/models.json`
- `Shell` — Python inspection of `~/.openclaw/openclaw.json`
- `Shell` — `docker exec crewclaw-financial-analyst ... getMe`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw devices list --json"`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models status"`
- `Shell` — Python inspection of `auth-profiles.json`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models set anthropic/claude-sonnet-4-20250514 && pnpm openclaw models fallbacks clear && pnpm openclaw models status"`
- `Shell` — `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw agent --agent main --message 'Say only: Sparky is back.' --timeout 60"`
- `Shell` — `docker exec crewclaw-financial-analyst openclaw agent --agent main --message "Say only: financial worker route ok." --timeout 60`
- `Shell` — `wsl bash -lc "journalctl --user -u openclaw-gateway.service -n 80 --no-pager"`
- `Shell` — Python inspection of `.gateway-env` provider key presence
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models list | head -n 60"`

### Changes

| File | Change |
|---|---|
| `~/.openclaw/openclaw.json` | Live runtime default model changed from `openai/gpt-4-turbo-preview` to `anthropic/claude-sonnet-4-20250514`; stale OpenAI fallback chain cleared. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated unresolved issue from generic Anthropic timeout to the now-proven Anthropic usage-limit blocker. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Worker fleet running | PASS | All five `crewclaw-*` containers were `Up 4 hours` during verification. |
| Gateway open | PASS | `gateway status` reported `Runtime: running`, `RPC probe: ok`, listening on `*:18789`. |
| Gateway health | PASS | `health` reported Telegram OK, `Agents: main (default)`, and the usual channel summary. |
| Representative worker bot validity | PASS | `crewclaw-financial-analyst` Telegram token still returned `ok=true`, username `FINANCE_FRANKY_BOT`. |
| Worker pairing state | PASS | `devices list --json` showed no pending requests and all backend worker devices remained paired. |
| Root cause of user-reported stale OpenAI error | PASS | Live `~/.openclaw/openclaw.json` showed `agents.defaults.model.primary = openai/gpt-4-turbo-preview` with fallbacks `openai/gpt-4` and `openai/gpt-3.5-turbo-0125`, exactly matching the user-facing failure. |
| Live configured models | PASS | `models status` showed only one configured model: `anthropic/claude-sonnet-4-20250514`; the stale OpenAI default chain was config drift. |
| Auth profile state | PASS | `anthropic:default` existed as `ref(env:ANTHROPIC_API_KEY)`; `openrouter:default` and `openai:default` were missing. |
| Live model fix | PASS | `pnpm openclaw models set anthropic/claude-sonnet-4-20250514` and `pnpm openclaw models fallbacks clear` succeeded. |
| Gateway restart after fix | PASS | Canonical Bitwarden-backed restart completed successfully. |
| Post-fix direct Sparky probe | FAIL | Old OpenAI model error is gone, but request now fails with `LLM request rejected: You have reached your specified API usage limits. You will regain access on 2026-04-01 at 00:00 UTC.` |
| Post-fix worker route | FAIL | Representative worker inherited the same Anthropic usage-limit rejection. |
| Gateway logs after fix | PASS | Recent journal shows gateway booting with `agent model: anthropic/claude-sonnet-4-20250514`; the stale OpenAI chain no longer appears after the fix window. |

### Verdict

PARTIAL — employees are active, paired, and mostly set up correctly; the gateway is open; the stale OpenAI-model misconfiguration causing the quoted error has been fixed. Sparky is still not responding because the Anthropic account itself is now over its usage limit until `2026-04-01 00:00 UTC`.

### Blockers

- Anthropic provider usage limit is currently exhausted for the host `main` agent.
- No OpenRouter/OpenAI fallback profile is configured in the live auth store, so there is no immediate automatic backup model.
- Dashboard heartbeat is still unwired and independent of worker functionality.

### Fallbacks Used

- None beyond the documented canonical gateway restart path.

### Cross-Repo Impact

- Host runtime state changed outside the repo (`~/.openclaw/openclaw.json`).
- Governance docs in `AI-Project-Manager` now reflect the more precise live blocker.

### Decisions Captured

- Worker activity and dashboard heartbeat must be treated separately: employees can be active even while the CrewClaw dashboard still says `waiting for first ping`.
- The reported OpenAI model error was real config drift, not a closed gateway.

### Pending Actions

1. Wait for Anthropic limit reset or configure a working fallback provider/profile (for example OpenRouter) for `main`.
2. After model access is restored, re-test Sparky and a representative worker route.
3. Separately, wire dashboard heartbeat once the monitor key is available.

### What Remains Unverified

- Whether OpenRouter fallback can be enabled cleanly from the existing env keys without broader runtime changes.
- End-to-end Telegram conversation after provider access is restored.

### What's Next

If immediate recovery is needed before Anthropic resets, configure an OpenRouter fallback profile for `main`; otherwise wait for the Anthropic reset window and re-test Sparky after `2026-04-01 00:00 UTC`.

---

## 2026-03-29 20:40 — Phase 0E: Switch live model chain to OpenAI with Grok backup

### Goal

Change the live host gateway model order to OpenAI first, Grok second, Anthropic third, using a reasoning-capable OpenAI primary that is the closest current OpenClaw-supported match to the user's request for "ChatGPT 4.5 thinking."

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- Live host config: `~/.openclaw/openclaw.json`
- Live host auth store: `~/.openclaw/agents/main/agent/auth-profiles.json`
- Host gateway journal + live agent routing
- Representative worker route through `crewclaw-financial-analyst`

### Commands / Tool Calls

- `user-Context7-query-docs` — OpenClaw OpenAI provider docs, xAI provider docs, OpenRouter provider docs
- `WebSearch` — OpenRouter Grok model ID verification
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models set openai/gpt-5.4 && pnpm openclaw models status"`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models fallbacks add openrouter/x-ai/grok-4 && pnpm openclaw models fallbacks add anthropic/claude-sonnet-4-20250514 && pnpm openclaw models status"`
- `Shell` — Python update of `~/.openclaw/agents/main/agent/auth-profiles.json` to add env-backed `openai:default` and `openrouter:default`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models status"`
- `Shell` — `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw agent --agent main --message 'Reply with exactly: model chain works.' --timeout 90"`
- `Shell` — `docker exec crewclaw-financial-analyst openclaw agent --agent main --message "Reply with exactly: worker chain works." --timeout 90`
- `Shell` — `wsl bash -lc "journalctl --user -u openclaw-gateway.service -n 80 --no-pager"`

### Changes

| File | Change |
|---|---|
| `~/.openclaw/openclaw.json` | Live model order changed to `openai/gpt-5.4` primary, `openrouter/x-ai/grok-4` fallback, `anthropic/claude-sonnet-4-20250514` fallback. |
| `~/.openclaw/agents/main/agent/auth-profiles.json` | Added env-backed `openai:default` and `openrouter:default` profiles referencing `OPENAI_API_KEY` and `OPENROUTER_API_KEY`. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Replaced stale Anthropic usage-limit blocker with the new live model-chain truth and remaining direct-xAI note. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Closest current OpenAI match in OpenClaw docs | PASS | Context7 docs show current direct API-key path uses `openai/gpt-5.4`; no current OpenClaw doc path exposed a `gpt-4.5 thinking` model ID. |
| Desired Grok backup path | PASS | OpenClaw docs confirm `openrouter/<provider>/<model>` model naming; external verification confirmed `x-ai/grok-4` as a valid Grok model ID on OpenRouter. |
| Direct xAI env availability | FAIL | `XAI_API_KEY` / `GROK_API_KEY` were not present in `.gateway-env`, so direct `xai/grok-*` could not be wired without new credentials. |
| OpenAI primary configured | PASS | `models status` resolved `Default: openai/gpt-5.4`. |
| Fallback order configured | PASS | `models status` resolved fallbacks in the requested order: `openrouter/x-ai/grok-4`, then `anthropic/claude-sonnet-4-20250514`. |
| Env-backed auth profiles present | PASS | `models status` resolved `openai:default=ref(env:OPENAI_API_KEY)` and `openrouter:default=ref(env:OPENROUTER_API_KEY)` alongside Anthropic. |
| Gateway restart after model-chain change | PASS | Canonical Bitwarden-backed restart completed successfully. |
| Gateway boot model | PASS | Journal shows `agent model: openai/gpt-5.4` after restart. |
| Direct Sparky reply after switch | PASS | `pnpm openclaw agent --agent main ...` returned `model chain works.` |
| Representative worker-routed reply after switch | PASS | `docker exec crewclaw-financial-analyst openclaw agent --agent main ...` returned `worker chain works.` |

### Verdict

PASS — the live gateway is now using OpenAI first, Grok second, Anthropic third, and both direct host routing and representative worker routing succeeded after the change.

### Blockers

- Direct xAI fallback is not configured because `XAI_API_KEY` is not present; Grok fallback currently runs through OpenRouter instead.
- Dashboard heartbeat remains unwired and independent of worker/model functionality.
- WhatsApp channel is still logged out and requires user re-link.

### Fallbacks Used

- Grok fallback is currently implemented through `openrouter/x-ai/grok-4` rather than direct `xai/grok-4` because no live xAI API key is present.

### Cross-Repo Impact

- Host runtime state changed outside the repo (`~/.openclaw/openclaw.json`, `~/.openclaw/agents/main/agent/auth-profiles.json`).
- Governance docs in `AI-Project-Manager` now reflect the working provider chain and remaining blockers.

### Decisions Captured

- The closest current OpenClaw-supported OpenAI choice to "ChatGPT 4.5 thinking" is `openai/gpt-5.4`, so that is now the live primary.
- Until an `XAI_API_KEY` exists, Grok is best implemented through the already-present OpenRouter credential instead of delaying the working fallback chain.

### Pending Actions

1. If desired later, switch Grok from `openrouter/x-ai/grok-4` to direct `xai/grok-4` once an `XAI_API_KEY` is available.
2. Re-link WhatsApp in WSL if Sparky needs to answer there.
3. Wire dashboard heartbeat once the `CREWCLAW_MONITOR_KEY` is available.

### What Remains Unverified

- Whether the live OpenAI primary selected for this simple probe will remain the preferred provider under heavier real-world conversations versus falling through to Grok or Anthropic.
- Real user-originated Telegram round-trip after the provider switch.

### What's Next

Use Telegram or the CLI to exercise a real conversation against Sparky on the new provider chain; if you later add `XAI_API_KEY`, convert the Grok fallback from OpenRouter-backed to direct xAI-backed routing.

---

## 2026-03-29 21:10 — Phase 0F: XAI readiness + Windows node / Cursor access verification

### Goal

Prepare the canonical gateway restart path for direct xAI-backed Grok fallback, verify whether an actual Grok/xAI Bitwarden secret is available on the active path, and make sure Sparky again has working access to the Windows node and local Cursor CLI surface.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/scripts/openclaw_gateway_required_env.py`
- `AI-Project-Manager/scripts/restart-openclaw-gateway.ps1`
- `AI-Project-Manager/docs/ai/operations/openclaw-gateway-restart.md`
- `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`
- Live Bitwarden secret visibility
- Live node host state for `Windows Desktop`

### Commands / Tool Calls

- `user-Context7-query-docs` — OpenClaw OpenAI/xAI/OpenRouter/nodes docs
- `Shell` — `bws secret list f14a97bb-5183-4b11-a6eb-b3fe0015fedf | Select-String ...`
- `Shell` — `bws secret list | ConvertFrom-Json | Where-Object { $_.key -match 'XAI|GROK' } ...`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw nodes status && printf '\n---\n' && pnpm openclaw models status"`
- `ReadFile` — `AI-Project-Manager/scripts/restart-openclaw-gateway.ps1`
- `ReadFile` — `AI-Project-Manager/scripts/openclaw_gateway_required_env.py`
- `ReadFile` — `AI-Project-Manager/docs/ai/operations/openclaw-gateway-restart.md`
- `ReadFile` — `C:\Users\ynotf\.openclaw\node.cmd`
- `ReadFile` — `C:\Users\ynotf\.openclaw\exec-approvals.json`
- `ReadFile` — `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`
- `Shell` — relaunch `C:\Users\ynotf\.openclaw\node.cmd`, then `pnpm openclaw nodes status`
- `Shell` — `pnpm openclaw nodes run --agent main --node 'Windows Desktop' --raw 'hostname'`
- `Shell` — `pnpm openclaw nodes run --agent main --node 'Windows Desktop' --raw 'C:\Windows\System32\where.exe cursor'`

### Changes

| File | Change |
|---|---|
| `AI-Project-Manager/scripts/openclaw_gateway_required_env.py` | Added `xai/` detection so `XAI_API_KEY` becomes a required env var whenever the live config references direct xAI models. |
| `AI-Project-Manager/scripts/restart-openclaw-gateway.ps1` | Added `XAI_API_KEY` to `WSLENV` export and `.gateway-env` writing path. |
| `AI-Project-Manager/docs/ai/operations/openclaw-gateway-restart.md` | Documented that `XAI_API_KEY` is part of the canonical restart path when `xai/*` is configured. |
| `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1` | Added `XAI_API_KEY` to optional startup env checks so launcher output reflects Grok/xAI readiness. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated runtime truth and unresolved issue wording for xAI readiness and Windows-node availability. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| OpenAI "thinking" support | PARTIAL | OpenClaw docs do not expose a `gpt-4.5 thinking` ID. They do show `openai/gpt-5.4` as the current direct API-key model path, and provider docs note `fastMode` lowers reasoning effort, which implies normal mode is the closest supported "thinking" path on direct OpenAI. |
| xAI reasoning-capable models in docs | PASS | Context7 docs list explicit reasoning-capable xAI IDs including `grok-4-fast-reasoning`, `grok-4-1-fast-reasoning`, and `grok-4.20-reasoning`. |
| OpenRouter Grok fallback | PASS | Existing `openrouter/x-ai/grok-4` fallback remains valid and reasoning-capable by model family. |
| Active Bitwarden project contains xAI secret | FAIL | Project secret listing showed `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, and `OPENROUTER_API_KEY`, but no xAI/Grok secret entry. |
| Accessible Bitwarden vault contains xAI/Grok secret by name | FAIL | Global secret-name search under the current Bitwarden account returned no secret with `XAI` or `GROK` in the key name. |
| Canonical restart path xAI readiness | PASS | Repo helper + restart script now support `XAI_API_KEY` whenever `~/.openclaw/openclaw.json` references `xai/*`. |
| Windows node launcher configuration | PASS | `node.cmd` already includes `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` and targets the current WSL gateway host/port. |
| Windows node connectivity after relaunch | PASS | `nodes status` moved from `Connected: 0` to `Connected: 1`. |
| Sparky execution on Windows node | PASS | `pnpm openclaw nodes run --agent main --node 'Windows Desktop' --raw 'hostname'` returned `ChaosCentral`. |
| Cursor CLI visible from Windows node | PASS | `pnpm openclaw nodes run --agent main --node 'Windows Desktop' --raw 'C:\Windows\System32\where.exe cursor'` returned the installed Cursor CLI paths. |

### Verdict

PARTIAL — Sparky now has working Windows-node access again and the canonical gateway restart path is ready for direct xAI fallback, but the requested direct `xai/*` backup cannot be activated yet because no xAI/Grok secret is currently exposed through the active Bitwarden path.

### Blockers

- No accessible `XAI_API_KEY` / Grok secret is available under the active Bitwarden project/injected environment.
- OpenClaw docs still do not expose a direct `gpt-4.5 thinking` model ID on the OpenAI API-key path; `openai/gpt-5.4` remains the closest supported choice.
- WhatsApp remains logged out and independent of the model/node work.

### Fallbacks Used

- Kept the currently working chain `openai/gpt-5.4` -> `openrouter/x-ai/grok-4` -> `anthropic/claude-sonnet-4-20250514` instead of switching to a broken direct-xAI path without credentials.

### Cross-Repo Impact

- Repo restart tooling now supports future direct xAI enablement.
- Local launcher / local node host state on the Windows machine was updated outside the repo.

### Decisions Captured

- There is no separate "Cursor node" architecture required here: the Windows node host is the mechanism that gives Sparky access to Windows tools, and Cursor is reachable through that node's executable path/CLI surface.
- Direct xAI fallback should not be enabled until the key is actually available on the active Bitwarden project/injected path.

### Pending Actions

1. Add or expose the actual xAI/Grok secret to the active Bitwarden project used by `bws run`, or provide its exact secret UUID/name so it can be injected as `XAI_API_KEY`.
2. After the key is available, switch the fallback order to direct `xai/*` first, then OpenRouter, then Anthropic.
3. If desired, tune the Anthropic fallback from Sonnet to Opus for a more reasoning-heavy final fallback.

### What Remains Unverified

- The exact secret key name / UUID of the user's Grok API key in Bitwarden.
- Whether the user wants `xai/grok-4.20-reasoning` or a faster `xai/grok-4-fast-reasoning` variant once the key is available.

### What's Next

Once the Grok/xAI secret is available on the active Bitwarden path, switch the chain to a direct xAI reasoning fallback, then OpenRouter Grok, then Anthropic, and re-test `main` plus one worker route.

---

## 2026-03-29 21:18 — Phase 0G: Strengthen final Anthropic fallback

### Goal

Align the final fallback more closely with the user's "everything should be thinking" request by upgrading the Anthropic fallback from Sonnet to Opus while preserving the working OpenAI-first chain.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- Live host config: `~/.openclaw/openclaw.json`
- Host gateway runtime

### Commands / Tool Calls

- `user-Context7-query-docs` — Anthropic model examples in OpenClaw docs
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw models fallbacks remove anthropic/claude-sonnet-4-20250514 && pnpm openclaw models fallbacks add anthropic/claude-opus-4-6 && pnpm openclaw models status"`
- `Shell` — `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"`
- `Shell` — `wsl bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw agent --agent main --message 'Reply with exactly: final chain ok.' --timeout 90"`
- `Shell` — `wsl bash -lc "journalctl --user -u openclaw-gateway.service -n 60 --no-pager"`

### Changes

| File | Change |
|---|---|
| `~/.openclaw/openclaw.json` | Replaced final Anthropic fallback `anthropic/claude-sonnet-4-20250514` with `anthropic/claude-opus-4-6`. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated runtime truth to reflect the stronger final Anthropic fallback. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Anthropic reasoning-heavy fallback candidate | PASS | Current OpenClaw docs expose `anthropic/claude-opus-4-6` as a current Anthropic model example and suitable high-end fallback choice. |
| Updated fallback order | PASS | `models status` now shows `openrouter/x-ai/grok-4, anthropic/claude-opus-4-6`. |
| Gateway restart after fallback update | PASS | Canonical Bitwarden-backed restart completed successfully. |
| Direct `main` reply after fallback update | PASS | `pnpm openclaw agent --agent main ...` returned `final chain ok.` |
| Runtime after fallback update | PASS | Journal shows the gateway came back cleanly with `agent model: openai/gpt-5.4` and hot-reloaded the Opus fallback. |

### Verdict

PASS — the working chain remains healthy and the final Anthropic fallback is now the more reasoning-oriented `claude-opus-4-6`.

### Blockers

- Direct xAI fallback still cannot be enabled until `XAI_API_KEY` is available on the active Bitwarden path.
- WhatsApp remains logged out and unrelated to the model-chain change.

### Pending Actions

1. Surface the actual `XAI_API_KEY` on the active Bitwarden project/injected env.
2. After that, switch the fallback order to direct xAI first, OpenRouter second, Anthropic Opus third.

### What's Next

Keep the current chain in service: `openai/gpt-5.4` -> `openrouter/x-ai/grok-4` -> `anthropic/claude-opus-4-6`, then cut over to direct xAI once the secret path is available.

---

## 2026-03-30 00:05 — Phase 0H: Manual dashboard activation for `api-integration-specialist`

### Goal

Follow CrewClaw's local monitor setup instructions for the existing `api-integration-specialist` worker, verify that it receives a monitor key, and confirm that heartbeat pings are now succeeding from the local worker project folder.

### Scope

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `open--claw/open-claw/employees/deployed/api-integration-specialist/.env`
- `open--claw/open-claw/employees/deployed/api-integration-specialist/heartbeat.sh`
- Runtime heartbeat process for `api-integration-specialist`

### Commands / Tool Calls

- `ReadFile` — `C:\Users\ynotf\Downloads\Screenshot 2026-03-29 195649.png`
- `ReadFile` — `open--claw/open-claw/employees/deployed/api-integration-specialist/README.md`
- `WebFetch` / `Shell` — `https://www.crewclaw.com/monitor.sh`
- `ReadFile` — `open--claw/open-claw/employees/deployed/api-integration-specialist/agents/api-integration-specialist/SOUL.md`
- `Shell` — POST `https://www.crewclaw.com/api/monitor/register`
- `Shell` — write local `.env` with `CREWCLAW_MONITOR_KEY`
- `Shell` — POST first ping to `https://www.crewclaw.com/api/ping/<agent_key>`
- `Shell` — start `heartbeat.sh` as a managed background process
- `ReadFile` — background terminal output for the heartbeat process

### Changes

| File | Change |
|---|---|
| `open--claw/open-claw/employees/deployed/api-integration-specialist/.env` | Created local monitor env containing `CREWCLAW_MONITOR_KEY`. |
| Runtime | Started `api-integration-specialist` `heartbeat.sh` as a background process from the worker project folder. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated dashboard truth to reflect one manually activated worker heartbeat. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| CrewClaw setup instruction captured | PASS | Screenshot showed the required local command pattern `curl -fsSL https://www.crewclaw.com/monitor.sh | bash`. |
| Monitor script behavior | PASS | Script inspects `SOUL.md`, registers via `https://www.crewclaw.com/api/monitor/register`, writes `CREWCLAW_MONITOR_KEY`, creates/uses `heartbeat.sh`, and sends a first ping. |
| Target worker folder | PASS | `api-integration-specialist` deploy folder already contained `README.md`, `heartbeat.sh`, and the nested `SOUL.md` identity file expected by the setup flow. |
| Registration API | PASS | Manual registration succeeded and returned monitor key `ak_834pjuk0up83`. |
| Local monitor env | PASS | `.env` now contains `CREWCLAW_MONITOR_KEY=ak_834pjuk0up83`. |
| Background heartbeat process | PASS | Managed background run of `bash heartbeat.sh` started successfully from the worker project folder. |
| Heartbeat ping status | PASS | Live process output showed `[heartbeat] ping ok` after startup. |

### Verdict

PASS — `api-integration-specialist` is now manually activated for CrewClaw dashboard monitoring and is sending successful heartbeat pings from its local project folder.

### Blockers

- This is still a manual/local activation path, not the desired Bitwarden-native shared-compose path.
- The remaining workers still do not have monitor keys or heartbeat processes wired.

### Decisions Captured

- Manual per-worker dashboard activation is viable immediately when a worker already exists in the CrewClaw portal, even before the shared compose heartbeat contract is restored.
- The local worker folder can carry a monitor-only `.env` containing `CREWCLAW_MONITOR_KEY` without changing the current shared Docker runtime truth.

### Pending Actions

1. Repeat this registration + heartbeat setup for the remaining prepared workers if desired.
2. Later, decide whether to keep per-worker local heartbeat loops or move to a shared Bitwarden-native heartbeat design.

### What's Next

If the goal is to light up the other prepared workers tonight, repeat the same local registration flow for each worker folder under `open-claw/employees/deployed/`.

---

## 2026-03-30 00:22 — Phase 0I: CrewClaw employee install runbook + activation/deactivation strategy

### Goal

Create a durable repo-tracked runbook for installing CrewClaw employees, capturing both the real CrewClaw monitor setup flow and the operating strategy of proving employees work, then leaving only currently needed employees active.

### Scope

- `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md`
- `AI-Project-Manager/docs/ai/STATE.md`

### Commands / Tool Calls

- `ReadFile` — `C:\Users\ynotf\Downloads\Screenshot 2026-03-29 200715.png`
- `ReadFile` — `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- `ReadFile` — `open--claw/open-claw/employees/deployed/start-employees.ps1`
- `Shell` — inventory listing for `open--claw/open-claw/employees`
- `ApplyPatch` — create `crewclaw-employee-install.md`
- `ApplyPatch` — append this STATE entry

### Changes

| File | Change |
|---|---|
| `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md` | Added a new runbook covering inventory, install flow, CrewClaw monitor activation, proof checklist, deactivation steps, and the strategy of keeping most employees ready-but-off. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Real CrewClaw setup flow captured | PASS | Screenshot showed both the automatic install command `curl -fsSL https://www.crewclaw.com/monitor.sh | bash` and the advanced manual path exposing local `.env` plus direct ping pattern. |
| Current package inventory captured | PASS | Local listing confirmed five shared deployed workers plus six additional prepared ZIP packages relevant to the current 11-worker plan. |
| Shared runtime limitation documented | PASS | `start-employees.ps1` still hardcodes only the five current shared workers, so newly unpacked employees are not automatically part of runtime until explicitly added. |
| Activation strategy documented | PASS | New runbook now defines the intended lifecycle: prepare -> portal add -> activate -> prove -> deactivate unless currently needed. |
| Secret hygiene preserved | PASS | New doc explicitly avoids storing raw monitor keys or other secret values in the repo. |

### Verdict

PASS — the repo now contains a concrete CrewClaw employee install runbook that matches the observed portal flow and documents the intended "prove then turn off unless needed" operating model.

### Blockers

- The six additional prepared ZIP packages are not yet unpacked and wired into shared runtime.
- `CREWCLAW_MONITOR_KEY` is still not tracked as a Bitwarden-backed shared runtime secret for the whole fleet.
- Full runtime enablement for new employees still requires compose and startup-script expansion beyond the current five-worker set.

### Pending Actions

1. Use the new runbook to unpack and dashboard-activate the next prepared employees.
2. Decide which of the six additional prepared workers should be promoted from dashboard-ready to fully runtime-active.
3. Later, extend the shared deployment if the user wants those workers always available instead of on-demand.

### What's Next

Follow the runbook worker-by-worker: add in CrewClaw, activate heartbeat, verify first ping, record proof, then stop anything not actively needed in the current workflow.

---

## 2026-03-30 00:57 — Phase 0J: Batch-expand CrewClaw runtime to 10 Telegram workers

### Goal

Stop treating CrewClaw employee preparation as a one-by-one runtime task, codify the approved local monitor-key exception, and bring the five additional token-backed Telegram workers into the shared deployment so they are ready for portal add and heartbeat activation.

### Scope

- `open--claw/open-claw/employees/deployed/personal-crm/*`
- `open--claw/open-claw/employees/deployed/script-builder/*`
- `open--claw/open-claw/employees/deployed/seo-specialist/*`
- `open--claw/open-claw/employees/deployed/software-engineer/*`
- `open--claw/open-claw/employees/deployed/ux-designer/*`
- `open--claw/open-claw/employees/deployed/docker-compose.yml`
- `open--claw/open-claw/employees/deployed/start-employees.ps1`
- `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md`
- `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/docs/ai/STATE.md`

### Commands / Tool Calls

- `Shell` — list deployed folders and inspect ZIP contents
- `Shell` — unpack `personal-crm`, `script-builder`, `seo-specialist`, `software-engineer`, `ux-designer`
- `ReadFile` — shared compose, shared launcher, new worker package files
- `ApplyPatch` — extend shared compose and launcher with the five new Bitwarden token UUIDs
- `ApplyPatch` — fix generated Dockerfile mismatch in the five new worker folders (`bot.js` -> `bot-telegram.js`)
- `Shell` — `docker compose config`
- `Shell` — `pwsh -NoProfile -File start-employees.ps1`
- `Shell` — `docker ps`
- `Shell` — `docker logs --tail 40 crewclaw-personal-crm`
- `Shell` — `docker logs --tail 40 crewclaw-software-engineer`

### Changes

| File | Change |
|---|---|
| `open--claw/open-claw/employees/deployed/personal-crm/*` | Unpacked package into deployed runtime and fixed generated Dockerfile copy target. |
| `open--claw/open-claw/employees/deployed/script-builder/*` | Unpacked package into deployed runtime and fixed generated Dockerfile copy target. |
| `open--claw/open-claw/employees/deployed/seo-specialist/*` | Unpacked package into deployed runtime and fixed generated Dockerfile copy target. |
| `open--claw/open-claw/employees/deployed/software-engineer/*` | Unpacked package into deployed runtime and fixed generated Dockerfile copy target. |
| `open--claw/open-claw/employees/deployed/ux-designer/*` | Unpacked package into deployed runtime and fixed generated Dockerfile copy target. |
| `open--claw/open-claw/employees/deployed/docker-compose.yml` | Added five new services and persistent volumes for the new Telegram workers. |
| `open--claw/open-claw/employees/deployed/start-employees.ps1` | Added the five new Bitwarden token UUIDs and updated comments/output to allow CrewClaw monitor-key local `.env` files only. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md` | Added the CrewClaw-only `.env` exception and documented batch runtime prep vs per-worker portal add. |
| `AI-Project-Manager/docs/ai/operations/CREWCLAW_BITWARDEN_SECRET_INVENTORY.md` | Added the five new worker token UUIDs and documented the monitor-key exception. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated operational truth from 5 to 10 workers and removed the old Bitwarden-native monitor-key assumption. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Five new worker packages identified | PASS | `personal-crm`, `script-builder`, `seo-specialist`, `software-engineer`, and `ux-designer` matched the new Bitwarden token UUIDs provided by the user. |
| "Sixth" extra package classification | PASS | `crewclaw-anthony-bundle.zip` is a multi-agent bundle archive, not one additional single Telegram worker in the current 10-token set. |
| New folders unpacked | PASS | All five new worker folders now exist under `open-claw/employees/deployed/`. |
| Shared launcher updated | PASS | `start-employees.ps1` now fetches all 10 Telegram worker tokens from Bitwarden. |
| Shared compose updated | PASS | `docker compose config` rendered all 10 worker services successfully. |
| Generated package defect found | PASS | First batch deploy failed because the five new generated `Dockerfile`s referenced missing `bot.js` files. |
| Generated package defect fixed | PASS | Patched the five new `Dockerfile`s to copy `bot-telegram.js`, matching the actual package contents. |
| Shared batch deploy | PASS | `start-employees.ps1` rebuilt and started all 10 worker containers successfully. |
| Running container count | PASS | `docker ps` showed all 10 `crewclaw-*` containers up. |
| New worker runtime sanity | PASS | `docker logs` for `crewclaw-personal-crm` and `crewclaw-software-engineer` both reported `Bot is running...`. |
| Monitor-key local `.env` rule | PASS | Governance docs now explicitly allow per-worker local `.env` storage for `CREWCLAW_MONITOR_KEY` only. |

### Verdict

PASS — the shared CrewClaw runtime is now expanded from 5 to 10 Telegram workers, and the approved setup contract is now: runtime secrets in Bitwarden, monitor keys in untracked per-worker local `.env` files for CrewClaw only.

### Ready For Portal Add

- `personal-crm`
- `script-builder`
- `seo-specialist`
- `software-engineer`
- `ux-designer`

### Blockers

- CrewClaw portal add / first-ping activation is still manual per worker.
- The new workers have been deployed and are running, but their dashboard heartbeat still depends on portal add plus monitor-key activation.
- `crewclaw-anthony-bundle.zip` remains outside the current 10-worker Telegram runtime set and needs a separate design decision if it should be adopted.

### Pending Actions

1. User adds the five new workers in the CrewClaw portal.
2. After each is added, use the approved local `.env` monitor-key path to confirm heartbeat.
3. Later, decide whether `crewclaw-anthony-bundle.zip` should become a separate deployment track or remain excluded.

### What's Next

The next five names to add in the CrewClaw portal are: `personal-crm`, `script-builder`, `seo-specialist`, `software-engineer`, and `ux-designer`.

---

## 2026-03-30 01:38 — Phase 0K: Restore named worker heartbeats from portal screenshots

### Goal

Use the user's CrewClaw portal screenshots to restore dashboard heartbeat for the named shared workers that had valid monitor keys visible in the UI but were still showing offline.

### Scope

- `open--claw/open-claw/employees/deployed/code-reviewer/.env`
- `open--claw/open-claw/employees/deployed/financial-analyst/.env`
- `open--claw/open-claw/employees/deployed/frontend-developer/.env`
- `open--claw/open-claw/employees/deployed/overnight-coder/.env`
- `open--claw/open-claw/employees/deployed/code-reviewer/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/financial-analyst/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/frontend-developer/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/overnight-coder/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/api-integration-specialist/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/personal-crm/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/script-builder/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/seo-specialist/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/software-engineer/heartbeat.sh`
- `open--claw/open-claw/employees/deployed/ux-designer/heartbeat.sh`
- `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md`
- `AI-Project-Manager/docs/ai/STATE.md`

### Commands / Tool Calls

- `ReadFile` — CrewClaw screenshots for `code-reviewer`, `financial-analyst`, `frontend-developer`, `overnight-coder`
- `Shell` — write local monitor `.env` files for the four workers
- `Shell` — start heartbeat loops for all four workers
- `ReadFile` — terminal outputs showing initial ping failure
- `Shell` — direct `curl` probe proving one screenshot key worked via GET
- `ApplyPatch` — change heartbeat implementation from POST payload ping to simple GET ping
- `ApplyPatch` — trim `\r` from `CREWCLAW_MONITOR_KEY` when `.env` is written from Windows
- `Shell` — restart the four heartbeat loops
- `ReadFile` — terminal outputs showing `ping ok`

### Changes

| File | Change |
|---|---|
| `open--claw/open-claw/employees/deployed/code-reviewer/.env` | Wrote local `CREWCLAW_MONITOR_KEY` from portal screenshot. |
| `open--claw/open-claw/employees/deployed/financial-analyst/.env` | Wrote local `CREWCLAW_MONITOR_KEY` from portal screenshot. |
| `open--claw/open-claw/employees/deployed/frontend-developer/.env` | Wrote local `CREWCLAW_MONITOR_KEY` from portal screenshot. |
| `open--claw/open-claw/employees/deployed/overnight-coder/.env` | Wrote local `CREWCLAW_MONITOR_KEY` from portal screenshot. |
| `open--claw/open-claw/employees/deployed/*/heartbeat.sh` | Standardized heartbeat loader to trim CRLF and standardized ping call to the simple CrewClaw GET endpoint. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md` | Documented the Windows `.env` / CRLF tolerance requirement for CrewClaw monitor keys. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Portal screenshots captured valid named worker keys | PASS | Screenshots exposed monitor keys for `code-reviewer`, `financial-analyst`, `frontend-developer`, and `overnight-coder`. |
| Initial scripted heartbeat attempt | FAIL | The generated `heartbeat.sh` scripts reported `ping failed` for all four workers. |
| Direct endpoint probe | PASS | Manual `curl https://www.crewclaw.com/api/ping/<key>` returned `{"ok":true}` for a screenshot key, proving the key itself was valid. |
| Root cause 1 | PASS | Generated scripts were using POST, while the CrewClaw portal advanced/manual path clearly matched a simple GET ping. |
| Root cause 2 | PASS | Windows-written `.env` files introduced CRLF line endings, so bash read `CREWCLAW_MONITOR_KEY` with a trailing `\r`. |
| Script remediation | PASS | Heartbeat scripts now trim trailing `\r` and use the simple GET ping call. |
| Restarted named worker loops | PASS | New background heartbeat loops for all four named workers started successfully after the script fix. |
| Named worker first ping after fix | PASS | Live terminal output for all four workers showed `[heartbeat] ping ok`. |

### Verdict

PASS — the named worker heartbeat failure was caused by a generated-script mismatch plus Windows CRLF handling, not by bad monitor keys. The four screenshot-backed workers are now restored to successful heartbeat ping status.

### Blockers

- The five `My Agent` rows still need either monitor-key screenshots or a fresh mapping from the CrewClaw portal before they can be wired.
- The separate `Api Integration Specialist - Custom Role` portal entry is still distinct from the original `Api Integration Specialist` row and may need cleanup later.

### Pending Actions

1. Refresh the CrewClaw portal to confirm the four named workers have moved back to green.
2. Capture or map the five `My Agent` monitor keys if those five new workers should also be brought online.

### What's Next

The next user-visible task is on the CrewClaw side: provide the five unnamed `My Agent` monitor keys, or rename those portal entries so each can be matched to `personal-crm`, `script-builder`, `seo-specialist`, `software-engineer`, and `ux-designer`.

---

## 2026-03-30 02:10 — Phase 0L: Audit CrewClaw employees for Next.js website workflow readiness

### Goal

Audit the current CrewClaw employee fleet, generic downloads, and local tooling surface to determine which workers are actually usable for a Next.js website clone/rebrand workflow, then create durable per-employee docs that describe capabilities and missing pieces.

### Scope

- `AI-Project-Manager/docs/ai/operations/CREWCLAW_WEBSITE_AGENT_AUDIT.md`
- `AI-Project-Manager/docs/ai/operations/crewclaw-employees/README.md`
- `AI-Project-Manager/docs/ai/operations/crewclaw-employees/*.md`
- `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/docs/ai/STATE.md`
- local Cursor extension inventory
- `open--claw/open-claw/employees/*.zip`
- `open--claw/open-claw/employees/generic/*.zip`
- representative deployed worker files under `open--claw/open-claw/employees/deployed/*`

### Commands / Tool Calls

- `ReadFile` — CrewClaw portal screenshots for current roster and generic-agent edit pages
- `Shell` — list generic ZIPs, main employee ZIPs, local skills, plugin caches, and installed Cursor extensions
- `Shell` — inspect ZIP manifests and compare generic package hashes
- `Shell` — inspect Dockerfile `COPY` references inside ZIPs
- `ReadFile` / `Shell` — inspect representative `SOUL.md`, `TOOLS.md`, `SKILLS.md`, and `bot-telegram.js` files
- `user-Context7-resolve-library-id` / `user-Context7-query-docs` — current Next.js App Router guidance for rebrand workflow assumptions
- `Shell` — install `ms-playwright.playwright`
- `Shell` — attempt to install Copilot extensions via Cursor CLI
- `user-serena-create_text_file` — create audit summary and per-employee markdown files
- `ApplyPatch` — update install runbook, HANDOFF, and append this STATE block

### Changes

| File | Change |
|---|---|
| `AI-Project-Manager/docs/ai/operations/CREWCLAW_WEBSITE_AGENT_AUDIT.md` | Added the main website-agent audit summary with PASS/FAIL findings, tooling audit, routing analysis, and recommended Next.js squad. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/README.md` | Added index of the per-employee audit files. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/api-integration-specialist.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/code-reviewer.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/financial-analyst.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/frontend-developer.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/overnight-coder.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/personal-crm.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/script-builder.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/seo-specialist.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/software-engineer.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/ux-designer.md` | Added capability and missing-pieces audit for this worker. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/agent-template-12.md` | Added audit doc for generic download `(12)`. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/agent-template-13.md` | Added audit doc for generic download `(13)`. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/agent-template-14.md` | Added audit doc for generic download `(14)`. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/agent-template-15.md` | Added audit doc for generic download `(15)`. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/agent-template-16.md` | Added audit doc for generic download `(16)`. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employees/crewclaw-anthony-bundle.md` | Added audit doc for the multi-agent bundle archive. |
| `AI-Project-Manager/docs/ai/operations/crewclaw-employee-install.md` | Added known package issues and cross-links to the audit docs. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated operational truth and unresolved issues with the website-agent audit findings. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Current portal roster captured | PASS | Screenshot showed 5 named workers plus 5 generic `My Agent` rows and one duplicate `Api Integration Specialist - Custom Role` entry. |
| Generic edit screens captured | PASS | The five generic agent edit screenshots all showed blank `Agent`/`Agent` fields with no personality, skills, or rules. |
| Generic ZIP identity | PASS | Hash comparison showed `crewclaw-agent-deploy (12)` through `(16)` are identical `My Agent` template packages. |
| Named ZIP structural completeness | PASS | Named employee ZIPs include the expected core files and the full agent-doc set. |
| ZIP packaging defect | FAIL | Every audited CrewClaw ZIP uses a `Dockerfile` that copies missing `bot.js` instead of `bot-telegram.js`. |
| Named role specificity | FAIL | 9 of the 10 named employees still use mostly generic role docs, tools, and skills despite specialist names. |
| Strongest current implementation worker | PASS | `software-engineer` is the only current package that clearly declares code-generation behavior and direct agent routing. |
| Runtime routing split | PASS | Older shared workers still route to `main`; newer workers route to their own agent IDs. |
| Cursor extension baseline | PASS | Existing extension set already covered ESLint, Prettier, Tailwind, Docker, GitLens, markdown, YAML, and other useful workflow tools. |
| Playwright extension install | PASS | `ms-playwright.playwright` installed successfully through Cursor CLI. |
| Copilot extension install | FAIL | Standard Copilot IDs were not found through the current Cursor CLI marketplace path. |
| Next.js framework guidance | PASS | Current Next.js docs confirmed App Router metadata, metadata-file conventions, global CSS handling, and `NEXT_PUBLIC_` env naming expectations. |

### Verdict

PARTIAL PASS — the local machine tooling is good enough to support a Next.js clone/rebrand workflow, but the CrewClaw employee definitions themselves are not yet strong enough for broad autonomous website work. The practical current lead is `software-engineer`; most of the remaining named employees require re-specialization before they should be trusted.

### Recommended Website Squad

- `software-engineer` — primary builder
- `frontend-developer` — secondary UI worker after re-specialization
- `ux-designer` — design review after re-specialization
- `code-reviewer` — review gate after re-specialization
- `seo-specialist` — later-stage metadata/copy/SEO pass
- `api-integration-specialist` — later-stage forms/integrations

### Blockers

- Most named employees are still generic templates behind specialist names.
- The original five shared workers still route to `main`, limiting true per-employee specialization.
- All CrewClaw ZIP downloads currently need manual Dockerfile repair before clean deploy.
- Copilot could not be added through the current Cursor CLI marketplace path.

### Pending Actions

1. Re-specialize the website-relevant employees, starting with `frontend-developer`, `ux-designer`, `code-reviewer`, and `seo-specialist`.
2. Decide whether to regenerate the five generic CrewClaw portal agents or discard them as duplicates.
3. Fix the ZIP packaging defect at the source or document a standard repair step for all future downloads.
4. If Copilot is still desired, resolve the correct marketplace/manual installation path and complete sign-in.

### What's Next

The most effective next move is not adding more agents; it is upgrading the existing website squad definitions so `software-engineer`, `frontend-developer`, `ux-designer`, `code-reviewer`, and `seo-specialist` actually contain the right workflow, tools, and acceptance criteria for a Next.js clone-and-rebrand project.

---

## 2026-03-30 00:55 — Phase 0M: Build curated AI employee standard from imported repo sources

### Goal

Turn the imported `Agents-Bulk` repo collection into a durable, repo-tracked AI employee standard with a real leadership hierarchy, a 10-15 person development team, copied high-value source assets, portable employee packets, and missing software-delivery skills.

### Scope

- `open--claw/.gitignore`
- `open--claw/open-claw/scripts/generate_ai_employee_knowledgebase.py`
- `open--claw/open-claw/AI_Employee_knowledgebase/**`
- `open--claw/open-claw/skills/nextjs-app-router/SKILL.md`
- `open--claw/open-claw/skills/design-token-theming/SKILL.md`
- `open--claw/open-claw/skills/playwright-e2e/SKILL.md`
- `open--claw/open-claw/skills/visual-qa-evidence/SKILL.md`
- `open--claw/open-claw/skills/architecture-adr/SKILL.md`
- `open--claw/open-claw/skills/code-review-gate/SKILL.md`
- `open--claw/open-claw/skills/release-readiness/SKILL.md`
- `open--claw/open-claw/skills/repo-clone-rebrand/SKILL.md`
- `open--claw/open-claw/skills/mcp-integration/SKILL.md`
- `open--claw/open-claw/skills/handoff-state/SKILL.md`
- `AI-Project-Manager/docs/ai/operations/CREWCLAW_WEBSITE_AGENT_AUDIT.md`
- `AI-Project-Manager/docs/ai/HANDOFF.md`
- `AI-Project-Manager/docs/ai/STATE.md`

### Commands / Tool Calls

- `Shell` — inventory `Agents-Bulk`, `AI_Employee_knowledgebase`, and git state across touched repos
- `Subagent` — parallel read-only audits of `agency-agents`, `agent-factory`, `awesome-openclaw-agents`, `Startup-Agents`, `PraisonAI`, `autogen`, `cursor-starter`, `openlabor`, `openclaw-android`, `calfkit-sdk`, and related sources
- `ReadFile` — representative source role definitions, current employee packet files, current skill files, and governance docs
- `user-Context7-resolve-library-id` / `user-Context7-query-docs` — current Next.js App Router and Playwright best-practice guidance
- `user-serena-create_text_file` — add generator script
- `ApplyPatch` — update `.gitignore`, website audit doc, HANDOFF, and append this STATE block
- `Shell` — run the generator and inspect the resulting folders and zip archives

### Changes

| File | Change |
|---|---|
| `open--claw/.gitignore` | Added local-source ignores for `open-claw/Agents-Bulk/`, `open-claw/AI_Employee_knowledgebase/source_repos/`, and `open-claw/employees/` so purchased zips and extracted research stay local while curated assets remain trackable. |
| `open--claw/open-claw/scripts/generate_ai_employee_knowledgebase.py` | Added a reproducible generator that builds the curated knowledgebase, copied reference assets, employee packets, zip bundles, and development skills. |
| `open--claw/open-claw/AI_Employee_knowledgebase/README.md` | Added top-level knowledgebase map and source-of-truth explanation. |
| `open--claw/open-claw/AI_Employee_knowledgebase/AUTHORITATIVE_STANDARD.md` | Added the local authoritative employee standard and required release discipline. |
| `open--claw/open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md` | Added the 15-person dream team roster and reporting hierarchy. |
| `open--claw/open-claw/AI_Employee_knowledgebase/PROVENANCE_MATRIX.md` | Added employee-to-source mapping plus copied reference asset inventory. |
| `open--claw/open-claw/AI_Employee_knowledgebase/SKILLS_AUDIT.md` | Added the before/after skill inventory and the missing software-delivery skill layer. |
| `open--claw/open-claw/AI_Employee_knowledgebase/reference_assets/**` | Copied the strongest reusable role files, runtime templates, CI patterns, and prompt docs into tracked reference folders. |
| `open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/**` | Added 15 full employee packets plus zipped portable bundles. |
| `open--claw/open-claw/skills/*/SKILL.md` | Added 10 development skills covering Next.js, Playwright, visual QA, ADRs, code review, release readiness, clone/rebrand, MCP integration, and handoff state. |
| `AI-Project-Manager/docs/ai/operations/CREWCLAW_WEBSITE_AGENT_AUDIT.md` | Appended the follow-on buildout summary and pointed future work to the curated knowledgebase. |
| `AI-Project-Manager/docs/ai/HANDOFF.md` | Updated operational truth, unresolved issues, and current focus to reflect the new authoritative standard and the remaining live-runtime gap. |
| `AI-Project-Manager/docs/ai/STATE.md` | Appended this execution block. |

### Evidence

| Check | Result | Detail |
|---|---|---|
| Bulk source repo audit completed | PASS | Parallel source audits identified `agency-agents` as the strongest specialist-role source, `awesome-openclaw-agents` as the cleanest OpenClaw-native role source, `agent-factory` as the strongest operational-pattern source, and the proactive-agent pack as the best full employee file layout. |
| Current repo gap identified | PASS | The tracked `open-claw/skills` directory contained mostly communication/utilities skills and lacked a software-delivery skill layer. |
| Authoritative standard chosen | PASS | Local authority was explicitly set to `open--claw/open-claw/AI_Employee_knowledgebase`, not any single upstream repo. |
| Leadership hierarchy built | PASS | The curated roster includes `sparky-chief-product-quality-officer` as boss plus `delivery-director` beneath Sparky, followed by product, architecture, design, QA, release, SEO, and MCP roles. |
| Team size target met | PASS | 15 repo-tracked employee packets were generated and zipped successfully. |
| Development skill layer added | PASS | 10 new tracked skill docs were created for Next.js, Playwright, visual QA, architecture, release gating, MCP integration, and handoffs. |
| Reference assets copied | PASS | 24 high-value upstream files were copied into tracked reference folders with provenance. |
| Generator validation | PASS | The generator script ran successfully and emitted a manifest showing `employee_count: 15`, `skill_count: 10`, and tracked copied assets. |
| Portable employee bundles created | PASS | `_zips/` contains zipped packets for all 15 curated employees. |
| Framework guidance freshness | PASS | Next.js App Router and Playwright CI/test guidance were refreshed through Context7 and folded into the new standard. |

### Verdict

PASS — the project now has a durable, repo-tracked AI employee standard with a real leadership spine, strong provenance, reusable source assets, and a missing software-delivery skill layer that did not previously exist.

### Blockers

- The live deployed CrewClaw workers still use the older downloaded employee definitions; the curated `AI_Employee_knowledgebase` library has not yet been synced back into the runtime packages.
- Copilot availability through the current Cursor CLI marketplace path remains unresolved.
- The raw CrewClaw ZIP packaging defect still exists upstream and still requires manual repair if future downloads are adopted directly.

### Pending Actions

1. Decide whether to replace or regenerate the currently deployed CrewClaw worker packets from the new curated standard.
2. Choose the first live pilot squad from the 15-person standard and wire those packets into the runtime deployment path.
3. Resolve the Copilot installation path only if Copilot remains strategically important after the stronger local team standard is in use.

### What's Next

The highest-leverage next move is to promote the curated standard into the live runtime by selecting a first pilot squad and replacing the current role-thin deployed worker definitions with the stronger `AI_Employee_knowledgebase` packets.

---

## 2026-03-30 21:34 - Tri-workspace context bootstrap

### Goal

Create a durable, repo-tracked context brief that lets future sessions route work to the correct repo and entry points without re-discovering the tri-workspace architecture.

### Scope

- Inspected: `README.md`, `AGENTS.md`, `.cursor/rules/00-global-core.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `.cursor/rules/20-project-quality.md`, `docs/ai/STATE.md`, `docs/ai/HANDOFF.md`, `docs/ai/PLAN.md`, `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, `docs/ai/architecture/CODEBASE_ORIENTATION.md`, `openmemory.md`
- Cross-repo inspection: `../open--claw/README.md`, `../open--claw/.cursor/rules/00-global-core.md`, `../open--claw/docs/ai/HANDOFF.md`, `../droidrun/.cursor/rules/00-global-core.md`, `../droidrun/docs/ai-handoff-summary.md`, `../droidrun/docs/project-context.json`
- Touched: `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md`, `openmemory.md`, `docs/ai/STATE.md`

### Commands / Tool Calls

- `TodoWrite`
- `user-serena-activate_project`
- `user-serena-check_onboarding_performed`
- `user-serena-read_memory`
- `user-serena-list_dir`
- `ReadFile`
- `rg`
- `Subagent`
- `user-openmemory-add-memory`
- `user-openmemory-search-memory`
- `user-Clear_Thought_1_5-clear_thought`
- `ApplyPatch`
- `ReadLints`
- `Shell`:
  - `ls`
  - `Get-Date -Format "yyyy-MM-dd HH:mm"`
  - `git rev-parse --abbrev-ref HEAD`
  - `git rev-parse HEAD`
  - `git remote get-url origin`
  - `git status --short`
  - duplicate file casing scan via `Get-ChildItem -Recurse -File | Group-Object { $_.ToLowerInvariant() }`
  - referenced path existence scan via `Test-Path`

### Changes

- Added `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` with repo responsibilities, canonical source order, task-routing guidance, first-code-file entry points, and a current cross-repo operational snapshot.
- Updated `openmemory.md` to register the new brief as a reusable routing component/pattern.
- Appended this STATE block.

### Evidence

| Check | Result | Detail |
| --- | --- | --- |
| Governance source sweep | PASS | Authoritative docs and rules agree that `AI-Project-Manager` is governance/control plane, not runtime code. |
| Cross-repo boundary check | PASS | `open--claw` and `droidrun` both explicitly defer workflow/state governance to `AI-Project-Manager`. |
| Runtime entry point identification | PASS | OpenClaw runtime boot path and DroidRun actuator entry points were confirmed and recorded in the new brief. |
| OpenMemory project search | PASS | Searches ran successfully but returned zero relevant stored bootstrap memories, so repo docs remained canonical. |
| OpenMemory writeback | PASS | `user-openmemory-add-memory` accepted the new tri-workspace bootstrap brief as async ingestion. |
| OpenMemory recall verification | PASS | Follow-up `user-openmemory-search-memory` returned the stored tri-workspace bootstrap memory after the async ingestion delay. |
| Clear Thought reasoning gate | PASS | `user-Clear_Thought_1_5-clear_thought` was invoked for the tri-workspace mental model before finalizing the plan/brief. |
| Malformed `rg` call | FAIL | One `rg` invocation was sent with invalid JSON parameters and returned a parsing error; reran the search with corrected arguments and continued with evidence. |
| New brief path verification | PASS | `Test-Path` checks passed for all files referenced from the brief, including downstream repo entry points. |
| Duplicate file casing check | PASS | Case-insensitive scan returned `PASS: no case-insensitive duplicate file paths`. |
| Secret scan on changed docs | PASS | `rg` found no token-like secrets in `openmemory.md`, `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md`, or this file. |
| Markdown diagnostics | PASS | `ReadLints` showed the edited files introduced no new blocking issues; remaining warnings are longstanding markdown-style warnings concentrated in `docs/ai/STATE.md`. |
| Handoff update needed | PASS | No verified operational drift required `docs/ai/HANDOFF.md` changes in this block. |

### Verdict

READY - the tri-workspace context brief now exists in-repo and is sufficient to route future governance, OpenClaw runtime, and DroidRun work without re-mapping the architecture.

### Blockers

None.

### Fallbacks Used

- `user-openmemory-search-memory` returned no relevant bootstrap memories; fallback was the repo-tracked source-of-truth docs.
- `user-openmemory-add-memory` ingested asynchronously; fallback for immediate confirmation was to wait briefly, then re-run `user-openmemory-search-memory` until the memory became searchable.
- One malformed `rg` call failed before execution; fallback was an immediate corrected `rg` query.

### Cross-Repo Impact

None - this block only added a governance-side context brief and did not edit `open--claw` or `droidrun`.

### Decisions Captured

- `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` is the preferred fast-routing document for new tri-workspace sessions.
- `openmemory.md` now points to that brief as a reusable bootstrap component.

### Pending Actions

- Use the new brief as the first routing document when the next task moves from governance into either `vendor/openclaw` or `droidrun`.

### What Remains Unverified

- The cross-repo runtime snapshot in the brief is doc-backed, not freshly re-verified against live services in this block.

### What's Next

Use `docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` to route the next implementation or debugging task directly to the correct repo and entry points.

## 2026-03-31 14:00 — tri-workspace authority surface rewrite

### Goal

Rewrite all tri-workspace authority surfaces to enforce a strict charter hierarchy with FINAL_OUTPUT_PRODUCT.md as supreme, remove all claims that AI-Project-Manager is the supreme authority, and establish the correct layer model across all repos.

### Scope

18 files across three repos plus three STATE.md updates:
- AI-Project-Manager: AGENTS.md, .cursor/rules/00-global-core.md, .cursor/rules/10-project-workflow.md, .cursor/rules/openmemory.mdc, docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md, docs/ai/CURSOR_WORKFLOW.md, docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md, docs/ai/STATE.md
- open--claw: AGENTS.md, .cursor/rules/00-global-core.md, docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md, docs/ai/CURSOR_WORKFLOW.md, docs/ai/HANDOFF.md, docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md, docs/ai/STATE.md
- droidrun: AGENTS.md, .cursor/rules/00-global-core.md, .cursor/rules/openmemory.mdc, docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md, docs/ai/HANDOFF.md, docs/ai/STATE.md

### Commands / Tool Calls

- Read: FINAL_OUTPUT_PRODUCT.md, AUTHORITATIVE_STANDARD.md, TEAM_ROSTER.md
- Read: all 18 target files before editing
- Write/StrReplace: all target files
- Shell: markdownlint-cli2 validation on changed files across all three repos

### Changes

- All AGENTS.md files: added explicit authority hierarchy table; replaced AI-Project-Manager supremacy claim with correct layer model (AI-PM = workflow/process, open--claw = strict enforcement center, droidrun = actuator)
- All 00-global-core.md files: added authority hierarchy section with layer model; replaced old first-line claims
- AI-Project-Manager 10-project-workflow.md: added subordination note to charter
- Both openmemory.mdc files: added charter subordination clause
- All TAB_BOOTSTRAP_PROMPTS.md files: FINAL_OUTPUT_PRODUCT.md added as first item in every read list
- All CURSOR_WORKFLOW.md files: added authority hierarchy section and layer model table
- open--claw HANDOFF.md: rewritten §1 with durable authority model; FINAL_OUTPUT_PRODUCT.md added first to read order
- open--claw PROJECT_LONGTERM_AWARENESS.md: rewritten with charter authority, correct mission statement, anti-drift rules
- droidrun HANDOFF.md: rewritten §1 with durable authority model; read order updated
- TRI_WORKSPACE_CONTEXT_BRIEF.md: completely rewritten with authority table, corrected layer model, FINAL_OUTPUT_PRODUCT.md first in canonical source order
- All STATE.md files: added authority note clarifying operational evidence status

### Evidence

- PASS: markdownlint-cli2 — no MD032 errors in any changed file
- PASS: MD013 line-length errors pre-existing throughout all repos (not introduced by this work)
- PASS: All 18 target files written without errors
- PASS: FINAL_OUTPUT_PRODUCT.md not modified (per task rules)

### Verdict

READY — all 18 target files updated; authority hierarchy enforced throughout tri-workspace.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

open--claw and droidrun both updated with consistent authority model. All three repos now enforce identical hierarchy.

### Decisions Captured

- FINAL_OUTPUT_PRODUCT.md is supreme; AI-Project-Manager is the workflow/process layer only.
- open--claw is the strict enforcement center.
- droidrun is the actuator layer.
- STATE.md and HANDOFF.md are operational evidence only, never product law.
- All memory rules are explicitly subordinate to the charter.

### Pending Actions

None — task complete.

### What Remains Unverified

- Bootstrap prompts referencing @../open--claw/FINAL_OUTPUT_PRODUCT.md path work correctly in multi-root Cursor sessions (path may need adjustment per Cursor workspace resolution).

### What's Next

Verify bootstrap prompt paths resolve correctly in a live Cursor session using the updated TAB_BOOTSTRAP_PROMPTS.md files.

## 2026-03-31 15:30 — autonomy model rewrite

### Goal

Rewrite the autonomy model across six files so routine software-delivery work no longer requires user approval, user-confirmed model switches, or human sequencing. Sparky becomes the internal approval authority; Tony-gates remain only for the four hard-reserved categories.

### Scope

- AI-Project-Manager: docs/ai/architecture/GOVERNANCE_MODEL.md, docs/ai/STATE.md
- open--claw: .cursor/rules/05-global-mcp-usage.md, .cursor/rules/10-project-workflow.md, .cursor/rules/15-model-routing.md, open-claw/docs/VISION.md, open-claw/docs/REQUIREMENTS.md, docs/ai/STATE.md

### Commands / Tool Calls

- Read: GOVERNANCE_MODEL.md, 05-global-mcp-usage.md, 10-project-workflow.md, 15-model-routing.md, VISION.md, REQUIREMENTS.md
- Write: all six target files
- Shell: markdownlint-cli2 validation on all changed files

### Changes

- GOVERNANCE_MODEL.md: Full rewrite. Three-tier authority structure (auto-approve / Sparky-notified / Tony-gate). Routine delivery work — planning, refactoring, rule rewrites, model escalation, PRs, staging deploys, code changes — moved to auto-approve. Sparky introduced as internal approval authority. Tony-gate list narrowed to: FINAL_OUTPUT_PRODUCT.md changes, privileged credentials, financial transactions, external communications, irreversible external-world actions, product goal changes.
- 05-global-mcp-usage.md: Disabled-tool policy rewritten. Routine delivery no longer pauses for user to enable a tool — Sparky routes to fallback or proceeds. firecrawl active-tools clause updated to same policy.
- 10-project-workflow.md: AGENT stop/approval language replaced with internal routing to Sparky. Sparky mandatory file-change review section added. PLAN source-of-truth priority updated to put FINAL_OUTPUT_PRODUCT.md first. Subordination note added.
- 15-model-routing.md: Rule A hard-stop replaced with internal escalation — AGENT routes to Sparky or self-escalates to thinking-class model without waiting for user confirmation. Rule B updated to internal switch without user confirmation. Rule C updated to hand off to PLAN/Sparky. Sparky routing format added. Tony-gate section clarifies model routing is never a Tony-gate. "No Silent Escalation" renamed "No Silent Degradation" — recording requirement kept, user-stop requirement removed.
- VISION.md: Fully rewritten. Removed "orchestrates, not generates" framing. Added autonomous AI employee organization model, Sparky leadership, Tony-reserved authority scope.
- REQUIREMENTS.md: Removed "Autonomous long-running agents (all actions are human-triggered)" from out-of-scope. Added autonomous delivery, Sparky review, and self-improving as core requirements. Tony-reserved actions listed explicitly.

### Evidence

- PASS: markdownlint-cli2 — no MD032/MD025/MD001 structural errors in any changed file
- PASS: All six target files written without errors

### Verdict

READY — all six files updated; autonomy model enforced; Tony-gates narrowed to four categories.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

open--claw: five files updated. AI-Project-Manager: GOVERNANCE_MODEL.md updated.

### Decisions Captured

- Sparky is the internal approval/reject/refactor authority for all routine delivery work.
- Tony-gate actions: FINAL_OUTPUT_PRODUCT.md changes, privileged credentials, financial transactions, external communications to real people, irreversible external-world actions, product goal redefinition.
- AGENT may escalate model or route to Sparky without user confirmation.
- Autonomous long-running agents are in scope; they are the primary delivery mechanism.

### Pending Actions

None — task complete.

### What Remains Unverified

- The Sparky routing format in 15-model-routing.md requires live testing in a multi-agent session to confirm routing plumbing works.
- Governance overlay enforcement (wiring into Gateway) is still Phase 6B (blocked on ANTHROPIC_API_KEY).

### What's Next

Verify bootstrap prompt paths and Sparky routing in a live multi-agent session.

---

## 2026-03-31 17:00 — Tri-Workspace Context-Governance Normalization (Prompt 7)

### Goal

Normalize STATE.md archive policy, AGENT execution-ledger policy, AGENT contract language, PLAN source-of-truth order, and PLAN bootstrap/workflow wording consistently across all three repos (AI-Project-Manager, open--claw, droidrun).

### Scope

Files changed:
- `AI-Project-Manager/.cursor/rules/10-project-workflow.md`
- `open--claw/.cursor/rules/10-project-workflow.md`
- `open--claw/.cursor/rules/00-global-core.md`
- `open--claw/AGENTS.md`
- `open--claw/docs/ai/CURSOR_WORKFLOW.md`
- `droidrun/.cursor/rules/10-project-workflow.md`
- `droidrun/.cursor/rules/00-global-core.md`
- `droidrun/AGENTS.md`
- `droidrun/docs/ai/CURSOR_WORKFLOW.md`
- `AI-Project-Manager/docs/ai/STATE.md` (this file)
- `open--claw/docs/ai/STATE.md`
- `droidrun/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md`

### Commands / Tool Calls

- Read: All governance files across three repos (AGENTS.md, 00-global-core.md, 10-project-workflow.md, TAB_BOOTSTRAP_PROMPTS.md, CURSOR_WORKFLOW.md, MEMORY_CONTRACT.md, AGENT_EXECUTION_LEDGER.md) — PASS
- Grep: Search for `~500 lines` across all repos — PASS (found in open--claw/10-project-workflow.md; droidrun had ~400/~600 variant)
- Write: StrReplace on 9 governance files across 3 repos — PASS

### Changes

**AI-Project-Manager/.cursor/rules/10-project-workflow.md**:
- PLAN source-of-truth priority: Added FINAL_OUTPUT_PRODUCT.md at position 1; shifted other entries down by 1.
- Ledger consultation gate: Made one-block-at-a-time rule explicit ("Read one block at a time. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.").

**open--claw/.cursor/rules/10-project-workflow.md**:
- STATE.md Rolling Archive Policy: Replaced `STATE.md must not exceed ~500 lines` with canonical KB-based thresholds (≤140KB target, >140KB warn, >180KB archive required; ~800 lines soft, ~1000 lines hard).
- AGENT contract: Added ledger append requirement and turbulence promotion rule.
- Added AGENT Execution Ledger section with PLAN/DEBUG consultation gate (one-block-at-a-time rule), size management, and archive verbatim requirement.

**open--claw/.cursor/rules/00-global-core.md**:
- Added ledger append requirement to State updates section.
- Added Execution Ledger (non-canonical) section with one-block-at-a-time consultation rule and archive policy.

**open--claw/AGENTS.md**:
- Agent contract: Added ledger append and turbulence promotion.
- Added Execution Ledger (non-canonical) section.

**open--claw/docs/ai/CURSOR_WORKFLOW.md**:
- Added ledger reference in Excluded directories section (non-canonical, one-block-at-a-time on-demand only).

**droidrun/.cursor/rules/10-project-workflow.md**:
- STATE.md Rolling Archive Policy: Replaced ~400/~600 proxy with canonical KB-based thresholds.
- AGENT contract: Added ledger append requirement.
- PLAN source-of-truth priority: Added FINAL_OUTPUT_PRODUCT.md at position 1.
- Added AGENT Execution Ledger section with one-block-at-a-time consultation gate and size management.

**droidrun/.cursor/rules/00-global-core.md**:
- Added ledger append requirement to State updates section.
- Added Execution Ledger (non-canonical) section with one-block-at-a-time rule.

**droidrun/AGENTS.md**:
- State tracking: Added context/ and archive/ to tracked docs.
- Added Context source priority section (FINAL_OUTPUT_PRODUCT.md first).
- Agent contract: Added ledger append requirement.
- Added Execution Ledger (non-canonical) section.

**droidrun/docs/ai/CURSOR_WORKFLOW.md**:
- Added Authority Hierarchy section.
- Added Workspace layer model table.
- Enriched State and Planning section with ledger and archive references.
- Added Context source priority section.

### Evidence

- PASS: All StrReplace operations completed without error (no conflict detected)
- PASS: open--claw/10-project-workflow.md no longer contains `~500 lines` rule (replaced with KB-based policy)
- PASS: droidrun/10-project-workflow.md no longer contains `~400/~600` soft proxy (replaced with KB-based policy)
- PASS: Ledger non-canonical, one-block-at-a-time rule is now explicit in all three repos (00, 10, AGENTS.md)
- PASS: FINAL_OUTPUT_PRODUCT.md is position 1 in PLAN source-of-truth priority in all three repos
- PASS: No default bootstrap prompt in any repo reads the ledger automatically
- PASS: FINAL_OUTPUT_PRODUCT.md not modified

### Verdict

READY — Tri-workspace governance normalization complete. All five correction areas addressed.

### Blockers

None.

### Fallbacks Used

None.

### Cross-Repo Impact

open--claw: 4 files updated. droidrun: 4 files updated. AI-Project-Manager: 1 rule file updated.

### Decisions Captured

- KB-based STATE.md archive policy (≤140KB/warn/archive) is now canonical across all three repos, replacing all legacy line-count-only triggers.
- Ledger one-block-at-a-time rule is now explicit in all repos.
- FINAL_OUTPUT_PRODUCT.md is enforced as position 1 in PLAN source-of-truth priority across all three repos.
- Ledger remains non-canonical in all repos; no bootstrap prompt reads it by default.

### Pending Actions

- STATE.md archival for AI-Project-Manager: file is at ~2245 lines, well above the ~1000 line hard ceiling. Archive should be scheduled as the next standalone AGENT task before the next non-trivial execution block. Content remains operationally relevant so this pass correctly deferred it per task scope rules.

### What Remains Unverified

- Droidrun `docs/ai/context/AGENT_EXECUTION_LEDGER.md` and `docs/ai/context/archive/` directories do not yet exist — will need to be created when the first droidrun AGENT block appends a ledger entry.

### What's Next

Proceed to Prompt 8 (tri-workspace is clean and normalized).

---

