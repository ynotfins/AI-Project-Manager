# Execution State

`docs/ai/STATE.md` is the **primary operational source of truth** for PLAN.
PLAN reads this before reasoning about blockers, fallbacks, next actions, and cross-repo effects.
`@Past Chats` is a last resort — consult only after this file, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

---

## Enforced entry template (apply to ALL future blocks — no sections may be omitted)

```
## <YYYY-MM-DD HH:MM> — <task name>
### Goal
### Scope
### Commands / Tool Calls
### Changes
### Evidence
### Verdict
### Blockers
### Fallbacks Used
### Cross-Repo Impact
### Decisions Captured
### Pending Actions
### What Remains Unverified
### What's Next
```

Write `None` or `N/A` for any section with nothing to report. Do not omit sections.

---

## Current State Summary

> Last updated: 2026-03-16 (MCP context optimization + secrets fix)
> Last verified runtime: 2026-03-16 (headless node host connected)

### Phase Status
| Phase | Status | Closed |
|-------|--------|--------|
| 0 — Scaffold + Workflow | COMPLETE | 2026-02-23 |
| 1 — MCP Infrastructure | COMPLETE | 2026-02-26 |
| 2 — Secrets Management | COMPLETE | 2026-02-27 |
| 3 — OpenMemory Integration | COMPLETE | 2026-03-02 |
| 4 — Multi-Machine Parity | COMPLETE | 2026-03-04 |
| 5 — Remaining Automation | COMPLETE | 2026-03-04 |
| 6A — Architecture Design | COMPLETE | 2026-03-06 |
| 6B — Gateway Boot | COMPLETE | 2026-03-08 |
| **6C — First Live Integration** | **COMPLETE** | **2026-03-14** |

### Phase 6C Exit Criteria — ALL PASSED (2026-03-14)
- [x] Audit log captures actions — gateway file log `/tmp/openclaw/`, confirmed
- [x] Hybrid model routing configured — primary: claude-sonnet-4-20250514, fallback: gpt-4o-mini
- [x] WhatsApp channel operational (Baileys, selfChatMode, allowlist)
- [x] Telegram secured (owner ID 6873660400, dmPolicy: allowlist)
- [x] Signal disabled
- [x] Approval gate tested — sandbox mode + exec-approvals; `rm -rf` blocked from real host (2026-03-14)
- [x] gog OAuth complete (Gmail read access verified)
- [x] First integration tested — weather skill, 42°F NY, runId 2a3f0990 (2026-03-14)

### Runtime Snapshot (as of 2026-03-16)
- Gateway: 127.0.0.1:18789 (UI), :18792 (API health), systemd managed — **openclaw v2026.3.13** (updated from 2026.3.8)
- Install type: npm global, stable channel (was: git tag detached HEAD — `openclaw update` now works)
- Node: v22.22.0 (nvm), pnpm 10.23.0
- Skills: 19/59 ready
- Channels: WhatsApp (linked), Telegram (secured), Signal (disabled)
- Windows nodes: **1 connected** — headless node host v2026.3.13, `system` + `browser` caps, paired 2026-03-16
- Model routing: anthropic/claude-sonnet-4-20250514, fallback openai/gpt-4o-mini
- **Sandbox: mode=off** (reverted 2026-03-15 — Docker not installed in WSL; sandbox=all caused gateway crash loop)
- **Context engine: lossless-claw v0.3.0** (LCM active, db=`~/.openclaw/lcm.db`, native API — legacy fallback warning resolved by 2026.3.13 upgrade)
- exec-approvals.json: security=deny in defaults — policy file exists but NOT enforced without sandbox
- **DroidRun MCP**: added to other Cursor project window (2026-03-16) — phone automation tool for Samsung Galaxy S25 Ultra

### Active Blockers

#### BLOCKER 3 — Windows node host — **RESOLVED 2026-03-16**
- **Was:** Molty removed 2026-03-16 (XamlParseException crash loop, never functional post-restart)
- **Fix:** Installed headless OpenClaw node host via `openclaw node install`. Node connects to WSL gateway via WSL LAN IP (172.23.x.x:18789). Gateway set to `bind: lan`. `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` in `node.cmd` for private network.
- **Status:** `paired · connected (just now)` — ID: `891178e9...6492f112`, caps: `browser, system`

#### BLOCKER 1 — Sandbox requires Docker (not installed)
- **Symptom:** Setting `agents.defaults.sandbox.mode: "all"` in `openclaw.json` causes the gateway to crash-loop on every agent request with: `Failed to inspect sandbox image: failed to connect to docker API at unix:///var/run/docker.sock`
- **Impact:** exec-approvals policy is NOT enforced (sandbox=off means the approval gate is bypassed)
- **Current state:** Reverted to `sandbox.mode: "off"` as emergency fix. Gateway healthy but exec-approvals not active.
- **Fix options:** (A) Install Docker Desktop for Windows + enable WSL2 integration, OR (B) research whether OpenClaw supports a non-Docker sandbox mode (e.g. firejail, bubblewrap, or process-level isolation)
- **Ref:** DECISIONS.md 2026-03-14 — exec-approvals + sandbox mechanism

#### BLOCKER 2 — Agent session context overflow — **RESOLVED 2026-03-16**
- **Was:** Agent session `e3853d85` overflowed at 171 messages / 171,384 tokens, causing silent failures on WhatsApp/Telegram.
- **Fix (permanent):** Installed `lossless-claw` v0.3.0 LCM plugin (`pnpm openclaw plugins install @martian-engineering/lossless-claw`). Plugin is now the active `contextEngine`. DAG-based summarization prevents overflow permanently.
- **Config:** `freshTailCount=32`, `contextThreshold=0.75`, `incrementalMaxDepth=-1`, `session.reset.idleMinutes=10080`
- **Evidence:** `[lcm] Plugin loaded (enabled=true, db=~/.openclaw/lcm.db, threshold=0.75)` — warning gone, agent responsive.

### Pending User Actions
1. Decide on Docker installation (enables sandbox + approval gate enforcement)
2. Name agent via WhatsApp (bootstrap conversation) — cosmetic, non-blocking
3. MXRoute email: install imap-smtp-email skill + provide credentials — Phase 7 work

### Known Recurring Issues
| Issue | Trigger | Fix | Permanent Fix Needed |
|---|---|---|---|
| Gateway WebSocket `1006 abnormal closure` | CLI connects before gateway finishes warm-up after restart | Wait 10–12s after restart before running CLI commands | None needed — cosmetic timing issue |
| Agent context overflow → silent no-response | Session accumulates >170 messages over days | Delete session file, restart gateway | Tune `compaction` settings in openclaw.json |
| Gateway crash loop (Docker missing) | `sandbox.mode: "all"` set without Docker | Revert to `sandbox.mode: "off"` | Install Docker or find non-Docker sandbox |
| Signal restart loop | signal-cli Java version mismatch (needs Java 21, has older) | N/A — channel is disabled | Leave disabled; no action needed |

### Cross-Repo State (open--claw)
- Branch: master, clean
- Phase 2 (First Live Integration): COMPLETE — mirrors Phase 6C

---

## Archived Entries

Historical STATE.md entries have been archived to reduce context size.
These files preserve original content verbatim. PLAN does not consult them.

| Archive File | Contents | Entries |
|---|---|---|
| docs/ai/archive/state-log-phases-0-5.md | Phases 0-5 (2026-02-23 to 2026-03-04) | ~30 |
| docs/ai/archive/state-log-phase-6ab.md | Phases 6A-6B (2026-03-04 to 2026-03-08) | ~33 |
| docs/ai/archive/state-log-phase-6c-archive.md | Superseded Phase 6C entries | ~14 |
| docs/ai/archive/state-log-phase-6c-active.md | Phase 6C active execution entries (2026-03-08 to 2026-03-14) | 7 |
| docs/ai/archive/state-log-post-6c-ops.md | Post-6C operational fixes (sandbox, lossless-claw, OpenClaw update, headless node) | 4 |

---

## State Log

<!-- AGENT appends entries below this line after each execution block. -->


## 2026-03-16 14:00 — MCP Context Optimization + Governance Rules Update

### Goal
Fix context window exhaustion (90% consumed before conversation starts) by reducing active MCP tools from ~200 to ~52, mandating Clear Thought 1.5 as primary reasoning tool, and updating governance rules to reflect the new toolset.

### Scope
- AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md (rewritten)
- AI-Project-Manager/.cursor/rules/10-project-workflow.md (2 targeted edits)
- AI-Project-Manager/.cursor/rules/20-project-quality.md (1 targeted edit)
- AI-Project-Manager/docs/tooling/MCP_CANONICAL_CONFIG.md (restructured)
- AI-Project-Manager/docs/ai/STATE.md (rolling archive + this entry)
- AI-Project-Manager/docs/ai/archive/state-log-phase-6c-active.md (new archive file)

### Commands / Tool Calls
- Read: 05-global-mcp-usage.md, 10-project-workflow.md, 20-project-quality.md, MCP_CANONICAL_CONFIG.md
- Write: 05-global-mcp-usage.md (full rewrite)
- StrReplace x2: 10-project-workflow.md (PLAN output contract + DEBUG contract)
- StrReplace x1: 20-project-quality.md (dependency hygiene section)
- Write: MCP_CANONICAL_CONFIG.md (full restructure with enabled/disabled split)
- PowerShell: Get-Content STATE.md line count check (1188 lines → triggered archive)
- PowerShell: archive Phase 6C entries to state-log-phase-6c-active.md (633 lines)
- PowerShell: rebuild STATE.md keeping header + post-6C entries (563 lines)
- StrReplace: STATE.md archive reference table updated

### Changes
- **05-global-mcp-usage.md**: Full rewrite. Clear Thought 1.5 is now primary reasoning tool with mandatory operation table by situation. sequential-thinking demoted to fallback. droidrun section added. Disabled tool activation policy added (stop, explain, ask user, wait). firecrawl active tool list clarified (scrape/map/search only). Playwright, Magic MCP, Exa Search references removed.
- **10-project-workflow.md**: PLAN output contract line updated ("reasoning MCP tool" → "Clear Thought 1.5 mental_model or sequential_thinking"). DEBUG contract: added "DEBUG must use Clear Thought 1.5 debugging_approach operation before producing ranked causes".
- **20-project-quality.md**: Dependency hygiene: "docs MCP tool" → "Context7 (query-docs)".
- **MCP_CANONICAL_CONFIG.md**: Last verified date updated to 2026-03-16. Working server list split into "Enabled" and "Disabled" sections with active tool counts. JSON template split into enabled block + disabled commented block. Context budget rationale added. Secrets section updated to include WSLENV + .gateway-env transient file flow.
- **docs/ai/archive/state-log-phase-6c-active.md**: 7 Phase 6C active execution entries archived verbatim (2026-03-08 to 2026-03-14).
- **docs/ai/STATE.md**: Rolling archive applied (1188 → 565 lines). Archive reference table updated.

### Evidence
| Check | Result |
|---|---|
| 05-global-mcp-usage.md exists at expected path | PASS |
| 05-global-mcp-usage.md has no playwright/Magic MCP/Exa Search as mandatory | PASS |
| 05-global-mcp-usage.md contains Clear Thought 1.5 mandatory ops table | PASS |
| 05-global-mcp-usage.md contains disabled tool activation policy | PASS |
| 10-project-workflow.md PLAN output contract updated | PASS |
| 10-project-workflow.md DEBUG contract updated | PASS |
| 20-project-quality.md dependency hygiene updated | PASS |
| MCP_CANONICAL_CONFIG.md last verified = 2026-03-16 | PASS |
| MCP_CANONICAL_CONFIG.md has enabled/disabled split | PASS |
| STATE.md line count before archive | 1188 (over 500 — archive triggered) |
| Phase 6C entries archived | PASS — 633 lines to state-log-phase-6c-active.md |
| STATE.md line count after archive | 565 |
| Secret scan | PASS — no secrets in committed files |

### Verdict
READY — all 4 rule/doc files updated; STATE.md archived and under control.

### Blockers
None

### Fallbacks Used
None — all edits performed with Write/StrReplace tools directly.

### Cross-Repo Impact
Rules files are AI-Project-Manager only. open--claw does not duplicate rules.

### Decisions Captured
- Clear Thought 1.5 is now the mandatory primary reasoning tool; sequential-thinking is fallback only
- Disabled MCP servers must NOT be silently worked around — agent must stop, explain, ask user
- firecrawl active tools: scrape, map, search only (8 others disabled for context budget)
- MCP tool count: ~200 → ~52 active (context budget restored)

### Pending Actions
None from this block.

### What Remains Unverified
- Whether the actual Cursor MCP panel reflects the disabled servers (user-managed, outside repo)

### What's Next
Continue with gateway Bitwarden/WSLENV secret injection verification (Sparky responsiveness).

## 2026-03-16 15:00 — Tri-Workspace Expansion: Add DroidRun

### Goal
Expand from dual-workspace (AI-Project-Manager + open--claw) to tri-workspace by adding droidrun as the runtime/mobile control layer. Merge DroidRun startup logic into the main launch script, register droidrun in Serena, synchronize cursor rules, and document the tri-workspace architecture.

### Scope
- C:\Users\ynotf\.openclaw\openclaw.code-workspace (workspace file)
- C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1 (startup script)
- C:\Users\ynotf\.serena\serena_config.yml (Serena project registry)
- D:\github\droidrun\.cursor\rules\ (00, 05, 10, 20 synced from AI-PM)
- AI-Project-Manager\docs\tooling\MCP_CANONICAL_CONFIG.md (tri-workspace section added)
- AI-Project-Manager\docs\ai\STATE.md (this entry)
Repos affected: AI-Project-Manager (governance), droidrun (rules sync). open--claw: no changes.

### Commands / Tool Calls
- Read: startup_droidrun.ps1, start-cursor-with-secrets.ps1, openclaw.code-workspace, serena_config.yml, all 4 droidrun rule files, all 4 AI-PM rule files
- Write: openclaw.code-workspace (add droidrun folder)
- StrReplace x2: start-cursor-with-secrets.ps1 (optionalVars + DroidRun block)
- StrReplace: serena_config.yml (add open--claw + droidrun to projects list)
- Shell: Copy-Item x4 (rules sync AI-PM → droidrun)
- Shell: Get-FileHash x4 (verify identical content)
- StrReplace: MCP_CANONICAL_CONFIG.md (tri-workspace section prepended)

### Changes
- **openclaw.code-workspace**: Added droidrun as third folder (D:\github\droidrun)
- **start-cursor-with-secrets.ps1**:
  - Added DROIDRUN_DEEPSEEK_KEY and DROIDRUN_OPENROUTER_KEY to $optionalVars
  - Inserted DroidRun block (try/catch, non-blocking) between proxy start and Cursor launch:
    - Block A: Bootstrap BWS_DROIDRUN_TOKEN from regular Bitwarden vault → fetch DeepSeek + OpenRouter keys via droidrun machine account → store as User env vars + process env
    - Block B: Smart ADB reconnect (check → connect → db_find_port.ps1 → WARNING if all fail)
- **serena_config.yml**: Added D:\github\open--claw and D:\github\droidrun to projects list
- **droidrun/.cursor/rules/**: Synced  0-global-core.md,  5-global-mcp-usage.md, 10-project-workflow.md, 20-project-quality.md from AI-PM (all previously outdated — referenced playwright, old sequential-thinking as primary)
- **MCP_CANONICAL_CONFIG.md**: Added "Tri-workspace architecture" section documenting project roles, integration points, both Bitwarden accounts, merged startup flow, and rules sync table. Updated "Last verified" date.

### Evidence
| Check | Result |
|---|---|
| openclaw.code-workspace has exactly 3 folders | PASS |
| startup_droidrun.ps1 exists at expected path | PASS |
| start-cursor-with-secrets.ps1 exists | PASS |
| serena_config.yml exists | PASS |
| DroidRun optionalVars added | PASS |
| DroidRun block inserted before Cursor launch | PASS |
| DroidRun block wrapped in try/catch | PASS |
| BWS_DROIDRUN_TOKEN uses separate bw account | PASS — w get item BWS_DROIDRUN_TOKEN pattern; OpenClaw BWS_ACCESS_TOKEN restored after |
| serena_config.yml: droidrun added | PASS |
| 00-global-core.md synced (was outdated) | PASS — MD5 identical |
| 05-global-mcp-usage.md synced | PASS — MD5 identical |
| 10-project-workflow.md synced | PASS — MD5 identical |
| 20-project-quality.md synced | PASS — MD5 identical |
| MCP_CANONICAL_CONFIG.md tri-workspace section | PASS |
| No secrets in committed files | PASS — BWS_DROIDRUN_TOKEN, API keys not committed; IDs are non-secret references |
| Existing OpenClaw flow intact | PASS — proxy, gateway, node host sections unmodified |

### Verdict
READY — tri-workspace expansion complete. droidrun integrated into workspace, startup, Serena, and governance docs.

### Blockers
None

### Fallbacks Used
None — all edits performed with Read/Write/StrReplace/Shell tools directly.

### Cross-Repo Impact
- **droidrun**: .cursor/rules/ synced (4 files updated). droidrun is now governed by the same rules as AI-Project-Manager.
- **open--claw**: No changes made.
- **AI-Project-Manager**: MCP_CANONICAL_CONFIG.md updated, this STATE.md entry appended.

### Decisions Captured
- DroidRun uses a separate Bitwarden machine account (droidrun-windows) with its own BWS_DROIDRUN_TOKEN, independent from OpenClaw's BWS_ACCESS_TOKEN
- DroidRun block in startup script is fully non-blocking (try/catch); failure prints warning and continues
- Cursor rules are canonical in AI-Project-Manager; droidrun gets copies (not symlinks); sync must be re-run when rules change
- open--claw was NOT previously registered in serena_config.yml; added alongside droidrun

### Pending Actions
- Restart Serena (toggle in MCP panel or restart Cursor) to pick up the new project registrations
- Test DroidRun key injection on next ws run launch (verify DROIDRUN_DEEPSEEK_KEY appears in ENV_CHECK output)
- Verify phone reconnect logic on next startup

### What Remains Unverified
- Whether BWS_DROIDRUN_TOKEN is actually present in the regular Bitwarden vault (value not verified — runtime test needed)
- Whether db_find_port.ps1 correctly re-locks to port 5555 in a post-reboot scenario

### What's Next
Next startup via ws run ... start-cursor-with-secrets.ps1 will exercise the new DroidRun block. Monitor output for DROIDRUN: status lines.

## 2026-03-16 16:00 — Update TAB_BOOTSTRAP_PROMPTS.md (Clear Thought 1.5 + tri-workspace)

### Goal
Update TAB_BOOTSTRAP_PROMPTS.md to reflect Clear Thought 1.5 as primary reasoning tool (replacing sequential-thinking as primary) and add droidrun to the tri-workspace context block.

### Scope
- AI-Project-Manager/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md (4 targeted edits)
- AI-Project-Manager/docs/ai/STATE.md (rolling archive + this entry)
- AI-Project-Manager/docs/ai/archive/state-log-post-6c-ops.md (new archive file)

### Commands / Tool Calls
- Read: TAB_BOOTSTRAP_PROMPTS.md (209 lines confirmed)
- StrReplace x3 (workspace context, DEBUG tool ref, ASK tool ref) — 2 succeeded via StrReplace, 1 (DEBUG) succeeded
- Shell: PowerShell Unicode-aware Replace for reasoning tool gate (file had curly quotes + CRLF requiring direct byte replacement)
- Shell: Select-String grep verification (sequential-thinking fallback-only, Clear Thought 1.5 in PLAN+DEBUG, Context7 in ASK, droidrun in workspace)
- Shell: STATE.md line count check (726 — archive triggered)
- Shell: Archive entries L130-L477 to state-log-post-6c-ops.md (356 lines)
- Shell: Rebuild STATE.md (726 → 291 lines, keeping 4 most recent entries)

### Changes
- **TAB_BOOTSTRAP_PROMPTS.md**:
  - Workspace context block: added droidrun line; updated "both repos" → "all three repos"; updated "both repos are relevant" → "multiple repos are relevant"
  - Reasoning tool gate (PLAN): replaced sequential-thinking as primary with Clear Thought 1.5 (mental_model or sequential_thinking operation); added proper 3-line fallback chain
  - DEBUG non-negotiable: replaced "structured reasoning tool" with "Clear Thought 1.5 debugging_approach operation"; added fallback to sequential-thinking
  - ASK tool reference: "docs MCP tool" → "Context7"
- **docs/ai/archive/state-log-post-6c-ops.md**: 4 post-6C entries archived verbatim (sandbox crash, pre-restart checkpoint, lossless-claw install, OpenClaw update + Molty/headless node entries)
- **docs/ai/STATE.md**: Rolling archive applied (726 → 293 lines); archive table updated

### Evidence
| Check | Result |
|---|---|
| TAB_BOOTSTRAP_PROMPTS.md exists | PASS |
| Workspace context has droidrun (L20) | PASS |
| Reasoning tool gate: Clear Thought 1.5 primary (L63) | PASS |
| Reasoning tool gate: sequential-thinking fallback only (L64-65) | PASS |
| DEBUG: Clear Thought 1.5 debugging_approach (L124) | PASS |
| ASK: Context7 (L166) | PASS |
| grep sequential-thinking — no primary usage | PASS — only appears as fallback |
| grep Clear Thought 1.5 — present in PLAN + DEBUG | PASS — L63, L64, L65, L124 |
| AGENT tab unchanged | PASS — lines 99-111 untouched |
| ARCHIVE tab unchanged | PASS — lines 174-209 untouched |
| STATE.md rolling archive applied | PASS — 726 → 293 lines |
| No secrets committed | PASS |

### Verdict
READY — all 4 edits applied and grep-verified. STATE.md archived.

### Blockers
None

### Fallbacks Used
- StrReplace failed for reasoning tool gate due to curly quotes (U+201C/U+201D) + CRLF in file — used PowerShell [System.IO.File]::ReadAllText + Unicode literal replacement as fallback. PASS.

### Cross-Repo Impact
None — TAB_BOOTSTRAP_PROMPTS.md is AI-Project-Manager only.

### Decisions Captured
- TAB_BOOTSTRAP_PROMPTS.md uses curly quotes (U+201C/U+201D) — StrReplace tool cannot match these; use PowerShell Unicode replacement for future edits to this file.

### Pending Actions
None from this block.

### What Remains Unverified
None.

### What's Next
Continue with next planned work item.
