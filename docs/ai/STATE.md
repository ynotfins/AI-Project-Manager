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

---

## State Log

<!-- AGENT appends entries below this line after each execution block. -->

## 2026-03-15 12:30 — Post-6C Operational Issues: Sandbox Crash + Context Overflow

### Goal
Document and resolve two operational failures discovered after Phase 6C close: gateway crash loop from sandbox mode requiring Docker, and agent context overflow causing silent no-response on all channels.

### Scope
- `~/.openclaw/openclaw.json` (WSL, not in git) — sandbox mode reverted
- `/home/ynotf/.openclaw/agents/main/sessions/e3853d85-eb46-4a93-979f-fd75fb7bad4f.jsonl` (WSL) — deleted
- `AI-Project-Manager/docs/ai/STATE.md` — Current State Summary updated with blockers

### Commands / Tool Calls
- `systemctl --user is-active openclaw-gateway.service` → `active` (but port 18789 not listening)
- `ss -tlnp | grep 18789` → empty (port down)
- `journalctl --user -u openclaw-gateway.service -n 30` → revealed Docker socket errors on every agent call
- `pnpm openclaw agent --agent main --message ping --json` → revealed context overflow: 171 messages, 171384 tokens
- Python3 JSON edit: `agents.defaults.sandbox.mode: "all"` → `"off"`
- `systemctl --user restart openclaw-gateway.service && sleep 12 && curl http://127.0.0.1:18792/` → `OK`
- `rm /home/ynotf/.openclaw/agents/main/sessions/e3853d85-eb46-4a93-979f-fd75fb7bad4f.jsonl`
- `pnpm openclaw agent --agent main --message ping --json` → `"Pong! ⚡ I'm here"` (fresh session, 22k tokens)

### Changes
- `~/.openclaw/openclaw.json`: `agents.defaults.sandbox.mode: "all"` → `"off"` (emergency revert)
- Session file `e3853d85` deleted (171 messages, context-overflowed)
- Gateway restarted clean

### Evidence
| Check | Result | Detail |
|---|---|---|
| Gateway port after sandbox=all | FAIL | Port 18789 not listening despite systemd `active` |
| Journal crash reason | FOUND | `Failed to inspect sandbox image: dial unix /var/run/docker.sock: no such file or directory` — repeated on every lane |
| Context overflow error | FOUND | `input length and max_tokens exceed context limit: 171384 + 34048 > 200000` — 171 messages in session |
| Sandbox revert + gateway restart | PASS | Port 18789 listening; curl 18792 → `OK` |
| Fresh session ping | PASS | Agent responded in 3.3s, 22k tokens, model: claude-sonnet-4-20250514 |
| WhatsApp/Telegram channels | PASS (post-fix) | Health: WhatsApp linked, Telegram ok |

### Verdict
OPERATIONAL — both issues resolved for now. Permanent fixes required (see Blockers in Current State Summary).

### Blockers
1. **Docker not installed** — sandbox mode permanently broken until Docker Desktop installed with WSL2 integration. exec-approvals.json policy exists but unenforced without sandbox.
2. **Context overflow is recurring** — current `compaction.mode: "safeguard"` + `contextPruning.ttl: "1h"` insufficient for multi-day sessions. Will overflow again.

### Fallbacks Used
- Gateway WebSocket CLI fallback: used direct systemd restart + curl health check instead of `pnpm openclaw health` (which hangs when gateway is mid-crash)

### Cross-Repo Impact
- `open--claw/docs/ai/STATE.md`: needs mirror entry (deferred to next commit)

### Decisions Captured
- Sandbox mode requires Docker. Without Docker in WSL, `sandbox.mode` must stay `"off"`.
- Context overflow produces silent no-response — not a visible error on WhatsApp/Telegram. Only detectable via gateway CLI or log file.
- Emergency session recovery: delete `.jsonl` session file + restart gateway. Clean session starts at ~18-22k tokens.

### Pending Actions
1. **PLAN: Evaluate Docker Desktop installation** — Docker Desktop for Windows with WSL2 backend would enable sandbox mode and exec-approvals enforcement
2. **PLAN: Tune context compaction** — change `compaction.mode` to `"auto"` or set explicit `maxMessages` limit in `openclaw.json` to prevent overflow
3. **PLAN: Add monitoring** — consider a cron-based healthcheck that alerts via WhatsApp if session token count approaches limit

### What Remains Unverified
- Whether `compaction.mode: "auto"` exists in openclaw.json schema (needs Context7 lookup)
- Whether OpenClaw supports non-Docker sandboxing (firejail/bubblewrap) — needs research
- Whether the gateway's session compaction actually triggers at `ttl: "1h"` or only on explicit `/reset`

### What's Next
PLAN: Phase 7 scoping. Priority items: (1) fix context overflow permanently, (2) decide on Docker for sandbox, (3) MXRoute email integration.

---

## 2026-03-15 13:00 — Pre-Restart Checkpoint

### Goal
Safe state before PC restart.

### Scope
- Both repos
- WSL gateway

### Commands / Tool Calls
- `git status` both repos → clean
- `pnpm openclaw health` → healthy

### Changes
None.

### Evidence
- AI-Project-Manager: clean (untracked: `build_apk.bat`, `build_apk_fixed.bat` — pre-existing, not ours)
- open--claw: clean
- Gateway health: WhatsApp linked (auth age 9m), Telegram ok (@Sparky4bot), Signal failed (expected)
- Active sessions: `agent:main:main` (264m ago), `agent:main:telegram:slash:6873660400` (364m ago)
- Config warning: `plugins.entries.lossless-claw: plugin not found` — stale config entry in `openclaw.json`, non-blocking

### Verdict
READY for restart.

### Blockers
None blocking restart. Post-restart: follow PATTERNS.md Host Restart Verification.

### Fallbacks Used
None.

### Cross-Repo Impact
None.

### Decisions Captured
None.

### Pending Actions
Post-restart: run `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"` to restore secrets + start Cursor. Gateway is systemd-managed and will auto-start in WSL.

### What Remains Unverified
- Whether `lossless-claw` stale plugin entry causes any functional issue (appears cosmetic only — gateway still healthy)

### What's Next
Post-restart: verify gateway health, confirm WhatsApp + Telegram responsive. Then PLAN: Phase 7 — fix context overflow + Docker decision.

---

## 2026-03-16 00:15 — lossless-claw (LCM) Plugin Install + Context Overflow Fix

### Goal
Install and activate the lossless-claw LCM (Lossless Context Management) plugin to permanently resolve BLOCKER 2 (agent context overflow). Plugin was in `~/.openclaw/plugins/lossless-claw/` as unbuilt source — no `dist/`, never loaded.

### Scope
- WSL: `~/.openclaw/openclaw.json` (modified by installer)
- WSL: `~/.openclaw/extensions/lossless-claw/` (new install target)
- WSL: `~/.openclaw/lcm.db` (SQLite DAG store, created on first session)
- AI-Project-Manager/docs/ai/STATE.md

### Commands / Tool Calls
```
pnpm openclaw plugins list          # confirmed lossless-claw not discovered (no dist/)
pnpm openclaw plugins install @martian-engineering/lossless-claw  # installed v0.3.0
pnpm openclaw gateway restart       # reload with plugin
pnpm openclaw health                # verify plugin loaded
pnpm openclaw agent --agent main --message 'ping'  # live agent test
```

### Changes
- **Removed**: stale `~/.openclaw/plugins/lossless-claw/` (unbuilt source, ignored by gateway)
- **Added**: `~/.openclaw/extensions/lossless-claw/` (properly installed with node_modules)
- **openclaw.json** (updated by installer):
  - `plugins.slots.contextEngine: "lossless-claw"` — LCM is now the context engine
  - `plugins.entries.lossless-claw.enabled: true`
  - `plugins.entries.lossless-claw.config.contextThreshold: 0.75`
  - `plugins.entries.lossless-claw.config.freshTailCount: 32`
  - `plugins.entries.lossless-claw.config.incrementalMaxDepth: -1`
  - `session.reset.mode: "idle"`, `session.reset.idleMinutes: 10080` (7 days)

### Evidence
- Health output: `[lcm] Plugin loaded (enabled=true, db=/home/ynotf/.openclaw/lcm.db, threshold=0.75)`
- Config warning `plugins.entries.lossless-claw: plugin not found` is **GONE**
- Agent ping responded: "Pong! I'm back and running on the new Lossless-Claw engine! Context overflow is now a thing of the past"
- Non-blocking warning: `[lcm] using legacy auth-profiles fallback` — lossless-claw v0.3.0 expects OpenClaw >2026.3.8; fallback active, fully functional

### Verdict
PASS. BLOCKER 2 (context overflow) resolved permanently. LCM active.

### Blockers
None remaining for this task.  
Legacy auth fallback in lossless-claw v0.3.0 is non-blocking; will auto-resolve when OpenClaw upgrades past 2026.3.8.

### Fallbacks Used
None.

### Cross-Repo Impact
None (openclaw.json is WSL-local, not in git).

### Decisions Captured
- lossless-claw is the permanent context management solution; do NOT revert to compaction.mode tweaks
- `session.reset.idleMinutes: 10080` (7 days) — sessions long-lived, LCM handles compaction internally
- BLOCKER 2 closed

### Pending Actions
None for this task.

### What Remains Unverified
- Whether `lcm.db` DAG persists correctly across gateway restarts (will verify after next natural session)

### What's Next
BLOCKER 2 closed. Remaining PLAN work:
1. BLOCKER 1: Docker decision (sandbox mode for exec-approvals enforcement)
2. Phase 7 scoping: MXRoute email integration, agent naming, monitoring

---

## 2026-03-16 — OpenClaw Update 2026.3.8 → 2026.3.13 + DroidRun

### Goal
Update OpenClaw to latest stable (2026.3.13) to get native lossless-claw API support and eliminate legacy fallback warning. Document DroidRun MCP addition.

### Scope
- WSL: openclaw global npm install (was git tag detached HEAD)
- WSL: `~/.openclaw/openclaw.json` (updated by installer during update)
- AI-Project-Manager/docs/ai/STATE.md
- open--claw/docs/ai/STATE.md (mirror)

### Commands / Tool Calls
```
pnpm openclaw update --channel stable --yes   # updated 2026.3.8 → 2026.3.13, restarted gateway
openclaw health                                # verified post-update
```

### Changes
- OpenClaw: 2026.3.8 → **2026.3.13** (stable channel, npm global)
- Install type changed: git tag (detached HEAD, no branch) → **npm global** (`~/.nvm/.../node_modules/openclaw`)
- lossless-claw: re-pinned at v0.3.0, now uses native `runtime.modelAuth` API (no legacy fallback)
- `openclaw update` now works correctly going forward (stable channel tracked)
- DroidRun MCP tool added to Cursor (separate project window, 2026-03-16) — enables phone automation for Samsung Galaxy S25 Ultra via natural language commands

### Evidence
- Update output: `Update Result: OK — After: 2026.3.13`
- Health: `[lcm] Plugin loaded (enabled=true, db=~/.openclaw/lcm.db, threshold=0.75)` — no fallback warning
- WhatsApp: linked (auth age 0m), Telegram: ok, gateway auto-restarted by update

### Verdict
PASS.

### Blockers
BLOCKER 1 (Docker/sandbox) still open — unrelated to this update.

### Fallbacks Used
`--channel stable` flag used because install was a git tag with no branch, causing `openclaw update` git flow to fail (`pathspec 'main' did not match`). Switching channel to stable triggered npm global update path instead.

### Cross-Repo Impact
Mirror entry to be appended to open--claw/docs/ai/STATE.md.

### Decisions Captured
- OpenClaw will be maintained on stable npm channel going forward — git tag checkout abandoned
- Future updates: `openclaw update` (no flags needed, stable channel persisted)

### Pending Actions
- PC restart pending (user-initiated, other project window needs restart)
- After restart: verify gateway health per PATTERNS.md Host Restart Verification
- Inform openclaw agent of lossless-claw capabilities and DroidRun addition via WhatsApp

### What Remains Unverified
- lcm.db DAG persistence across gateway restarts (first real test after restart)
- DroidRun MCP integration details (added in other window, not yet tested here)

### What's Next
1. PC restart → post-restart health check
2. Give agent orientation prompt (lossless-claw + DroidRun)
3. PLAN: Phase 7 — Docker/sandbox decision, MXRoute email, agent naming

---

## 2026-03-16 — Phase 7.1: Windows Node Setup — BLOCKED (Molty XamlParseException crash)

### Goal
Re-pair Molty (OpenClaw Windows Hub v0.4.5) with WSL gateway for full Windows system access and DroidRun MCP bridging.

### Scope
- `%LOCALAPPDATA%\OpenClawTray\exec-policy.json` (modified — see Changes)
- `%LOCALAPPDATA%\OpenClawTray\openclaw-tray.log` (read for diagnostics)
- `%USERPROFILE%\.openclaw\openclaw.json` (read — not modified)
- WSL `~/.openclaw/openclaw.json` (not modified — `gateway.nodes: {}` confirmed correct for full access)

### Commands / Tool Calls
```
# BLOCK 1 — Research
Context7 query: OpenClaw node pairing, devices add, exec-policy nodes allowCommands
# → pairing flow: node.pair.request → openclaw devices approve <requestId>
# → gateway.nodes: {} with no allowCommands = unrestricted (confirmed)

# BLOCK 2 — exec-policy.json
Get-Content "$env:LOCALAPPDATA\OpenClawTray\exec-policy.json"
Copy-Item ... exec-policy.json.bak
# Rewrote with defaultAction: "allow", minimal deny rules (Format-*, shutdown, reg delete)
Get-Content ... | ConvertFrom-Json | Out-Null  # JSON VALID

# BLOCK 3+ — STOPPED
# Molty crash detected before proceeding to gateway config changes
Get-Content "$env:LOCALAPPDATA\OpenClawTray\openclaw-tray.log" -Tail 60
Stop-Process -Name "OpenClaw.Tray.WinUI" -Force; Start-Process ...  # restart test
# → crash persists on fresh start
```

### Changes
- `exec-policy.json`: `defaultAction` changed from `"deny"` → `"allow"`. Old allow rules replaced with minimal deny-only safety floor (Format-*, Stop-Computer, Restart-Computer, shutdown, reg delete). Backup: `exec-policy.json.bak`.
- No WSL changes made (gateway.nodes: {} is correct for full access per docs).

### Evidence
**Molty crash (recurring since 2026-03-13, confirmed 2026-03-16):**
```
[2026-03-16 01:19:03.140] [ERROR] CRASH UnhandledException:
Microsoft.UI.Xaml.Markup.XamlParseException: XAML parsing failed.
  at OpenClawTray.Windows.TrayMenuWindow.InitializeComponent()
  at OpenClawTray.App.InitializeTrayIcon()
  at OpenClawTray.App.OnLaunched()
```
- Crash happens on every startup — before gateway connection is attempted
- Process PID stays alive (18628) but tray menu and UI are dead
- Last successful Molty operation: 2026-03-11 (device removal confirmed)
- Crash began: 2026-03-13 16:05 (after PC restart post-Phase 6C)
- Molty version: v0.4.5 (latest)
- Windows App Runtime: 1.1 through 1.8 all present — version mismatch unlikely
- Cause: Corrupted WinUI3 XAML resource or missing MSIX package registration

**WSL nodes status (pre-change):** `Known: 0 · Paired: 0 · Connected: 0` — confirmed unpaired.

**Windows openclaw.json (read):**
- Gateway token present (matches WSL gateway token — stored in `~/.openclaw/openclaw.json`, not committed)
- DroidRun MCP configured: `mcpServers.droidrun` pointing to `start_mcp_server.ps1`
- Config is set as a gateway config, not a node host config — may need review when Molty is repaired

### Verdict
**BLOCKED — STOP CONDITION MET.** Molty cannot connect to gateway because its WinUI3 UI layer crashes on launch before any connection attempt. exec-policy.json was successfully updated but cannot be tested until Molty is repaired.

### Blockers
#### BLOCKER 3 — Molty XamlParseException (WinUI3 crash on every launch)
- **Symptom:** `XamlParseException: XAML parsing failed` at `TrayMenuWindow.InitializeComponent()` on every startup since 2026-03-13
- **Impact:** Molty process runs but tray, UI, and gateway connection are all dead. Cannot pair.
- **Fix options (in order of preference):**
  1. **Reinstall via MSIX** (not EXE): `OpenClawTray-0.4.5-win-x64.msix` from GitHub releases — MSIX installs register the app properly in the Windows package store and fix XAML resource loading issues
  2. **Repair Windows App Runtime**: `winget install Microsoft.WindowsAppRuntime.1.6` (Molty targets 1.6 based on DLL version `6000.519.329.0`)
  3. **Full uninstall + reinstall**: `%LOCALAPPDATA%\OpenClawTray\Uninstall.exe` → reinstall from `OpenClawTray-Setup-x64.exe`
  4. **Isolate XAML resource issue**: Check if `CommandPalette/` dir (found in install dir) has corrupt XAML files
- **Recommended action for PLAN:** Try Fix 1 (MSIX reinstall) first — it's non-destructive and fixes registration. If fails, try Fix 3 (full reinstall).

### Fallbacks Used
- Context7 (primary for docs research) — PASS
- Exa/Firecrawl not needed — Context7 returned sufficient detail

### Cross-Repo Impact
Mirror entry to open--claw/docs/ai/STATE.md.

### Decisions Captured
- `exec-policy.json defaultAction: "allow"` is now the target policy for Phase 7.1 (pre-configured, ready for when Molty is repaired)
- `gateway.nodes: {}` (no allowCommands) in WSL openclaw.json is correct for full access — no changes needed there
- Molty's Windows-side `openclaw.json` is configured as a gateway (not node host) — needs investigation when Molty pairing resumes

### Pending Actions
1. **USER ACTION REQUIRED:** Repair Molty — try in order:
   a. Download `OpenClawTray-0.4.5-win-x64.msix` from https://github.com/openclaw/openclaw-windows-node/releases/tag/v0.4.5 and install (double-click MSIX)
   b. If a) fails: uninstall via `%LOCALAPPDATA%\OpenClawTray\Uninstall.exe` then reinstall via `OpenClawTray-Setup-x64.exe`
2. After Molty repair: restart Molty, verify tray icon appears, then re-run Phase 7.1 BLOCK 3+
3. Investigate Windows-side `openclaw.json` — currently structured as gateway config, may need to be a node-host config pointing at WSL gateway URL

### What Remains Unverified
- Whether Molty's Windows-side `openclaw.json` (gateway mode) is correct for node host operation or needs restructuring
- Whether DroidRun MCP in Windows `openclaw.json` is surfaced to the WSL agent via the node bridge or needs separate WSL-side mcpServers config
- Whether `device-key-ed25519.json` (from 2026-03-11 pairing) is still valid or needs regeneration after reinstall

### What's Next
PLAN decision: repair Molty (MSIX reinstall recommended) then resume Phase 7.1 BLOCK 3+.

---

## 2026-03-16 — Phase 7.1: Headless Windows Node Host — CONNECTED

### Goal
Install headless OpenClaw node host service on Windows (no GUI) to replace Molty, giving Sparky full Windows system access (PowerShell, file system, DroidRun MCP bridge).

### Scope
- `C:\Users\ynotf\.openclaw\openclaw.json` — replaced gateway config with clean minimal node config; backed up as `openclaw.json.gateway-backup`
- `C:\Users\ynotf\.openclaw\node.cmd` — generated by `openclaw node install`, modified to add `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1`
- `~/.openclaw/openclaw.json` (WSL) — `gateway.bind` changed from `loopback` → `lan` (listens on `0.0.0.0:18789`)
- `C:\Users\ynotf\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\OpenClaw Node.cmd` — startup item installed
- Windows: `npm install -g openclaw@latest` — updated Windows OpenClaw 2026.3.8 → 2026.3.13

### Commands / Tool Calls
```
# Windows
npm install -g openclaw@latest                                          # → 2026.3.13
openclaw --version                                                       # → 2026.3.13
openclaw node status                                                     # → missing, stopped
# (rewrote openclaw.json to clean minimal config)
openclaw node install --host 127.0.0.1 --port 18789 --display-name "Windows Desktop"  # initial (127.0.0.1 not reachable)
# (changed gateway.bind: loopback → lan in WSL)
openclaw node install --host 172.23.156.209 --port 18789 --display-name "Windows Desktop" --force
# (added OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 to node.cmd)
Start-Process node.cmd (hidden, stdout/stderr redirected to node-host.log)

# WSL
wsl bash -lc "ss -tlnp | grep 18789"    # → 0.0.0.0:18789 after bind: lan
wsl bash -lc "pnpm openclaw nodes status"  # → Known: 1, Paired: 1, Connected: 1
wsl bash -lc "pnpm openclaw health"     # → healthy, WhatsApp + Telegram ok
```

### Changes
- **Windows `openclaw.json`**: replaced old gateway/channel/Molty config with minimal `{"meta":{...}}` node-client config
- **WSL `openclaw.json`**: `gateway.bind: "loopback"` → `"lan"` (gateway now listens on `0.0.0.0:18789`, reachable from Windows)
- **`node.cmd`**: added `set "OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1"` (break-glass for private WSL network — prevents security refusal on non-TLS ws:// to private IP)
- **Windows startup item**: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\OpenClaw Node.cmd` — runs on login
- **Windows OpenClaw**: updated 2026.3.8 → 2026.3.13 (version parity with WSL systemd service)
- **`node.cmd` gateway URL**: `--host 172.23.156.209` (WSL LAN IP — not 127.0.0.1 which is Windows loopback only)

### Evidence
```
pnpm openclaw nodes status output:
Known: 1 · Paired: 1 · Connected: 1
Windows Desktop — paired · connected (just now)
  ID: 891178e980ebe57e373035ebbfc10162d228f649b46aeda07b1ff8696492f112
  IP: 172.23.144.1
  version: v2026.3.13
  caps: browser, system

pnpm openclaw health:
Telegram: ok (@Sparky4bot)
WhatsApp: linked (auth age 141m)
Agents: main (default)
```

### Verdict
**PASS** — Windows Desktop node paired and connected. Sparky now has `system` capabilities on Windows (PowerShell, file access). BLOCKER 3 resolved.

### Blockers
- **WSL IP is dynamic** — if WSL restarts, the IP (172.23.156.209) may change. The startup script uses the IP baked at install time. On next WSL restart, `node.cmd` may fail to connect and will need `openclaw node install --force` with the new IP.
- **BLOCKER 1 still open** — sandbox=off, exec-approvals not enforced.

### Fallbacks Used
- `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` break-glass env var (documented in OpenClaw error message as supported for trusted private networks)
- `gateway.bind: lan` instead of loopback (required for WSL2 cross-namespace connectivity)

### Cross-Repo Impact
Mirror entry to open--claw/docs/ai/STATE.md.

### Decisions Captured
- Headless `openclaw node install` chosen over Molty reinstall — no WinUI3 dependency, lighter, no crash risk
- `gateway.bind: lan` is the correct setting for WSL-to-Windows node connectivity
- `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` is acceptable for WSL internal private network (token auth still enforces identity)
- Windows `openclaw.json` should be a minimal node-client config (not a gateway config) — the old Molty gateway config has been backed up

### Pending Actions
1. Test Sparky running a Windows PowerShell command via the node (e.g., `Get-ComputerInfo`)
2. Address dynamic WSL IP issue — consider using `openclaw node install` as part of WSL startup hook or documenting as a post-restart step
3. DroidRun MCP: confirm whether it surfaces to Sparky through the node's `system` cap or needs separate WSL-side `mcpServers` config

### What Remains Unverified
- Whether DroidRun MCP is accessible to the agent via the Windows node bridge
- Whether Sparky can successfully execute PowerShell commands (node is connected but agent-level test not run)
- Reconnection behavior after WSL restart (WSL IP may change)

### What's Next
Test Sparky executing a Windows command. Then assess DroidRun MCP accessibility.

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
