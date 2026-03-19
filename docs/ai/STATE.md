# Execution State

`docs/ai/STATE.md` is the **primary operational source of truth** for PLAN.
PLAN reads this before reasoning about blockers, fallbacks, next actions, and cross-repo effects.
`@Past Chats` is a last resort � consult only after this file, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

---

## Enforced entry template (apply to ALL future blocks � no sections may be omitted)

```
## <YYYY-MM-DD HH:MM> � <task name>
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

> Last updated: 2026-03-18 (CrewClaw 5 employees deployed via Docker + Bitwarden injection; Sparky full autonomous access)
> Last verified runtime: 2026-03-18 (WSL sudo root, Windows PowerShell, Docker v29.1.3, nodes invoke verified)

### Phase Status
| Phase | Status | Closed |
|-------|--------|--------|
| 0 � Scaffold + Workflow | COMPLETE | 2026-02-23 |
| 1 � MCP Infrastructure | COMPLETE | 2026-02-26 |
| 2 � Secrets Management | COMPLETE | 2026-02-27 |
| 3 � OpenMemory Integration | COMPLETE | 2026-03-02 |
| 4 � Multi-Machine Parity | COMPLETE | 2026-03-04 |
| 5 � Remaining Automation | COMPLETE | 2026-03-04 |
| 6A � Architecture Design | COMPLETE | 2026-03-06 |
| 6B � Gateway Boot | COMPLETE | 2026-03-08 |
| **6C � First Live Integration** | **COMPLETE** | **2026-03-14** |

### Phase 6C Exit Criteria � ALL PASSED (2026-03-14)
- [x] Audit log captures actions � gateway file log `/tmp/openclaw/`, confirmed
- [x] Hybrid model routing configured � primary: claude-sonnet-4-20250514, fallback: gpt-4o-mini
- [x] WhatsApp channel operational (Baileys, selfChatMode, allowlist)
- [x] Telegram secured (owner ID 6873660400, dmPolicy: allowlist)
- [x] Signal disabled
- [x] Approval gate tested � sandbox mode + exec-approvals; `rm -rf` blocked from real host (2026-03-14)
- [x] gog OAuth complete (Gmail read access verified)
- [x] First integration tested � weather skill, 42�F NY, runId 2a3f0990 (2026-03-14)

### Runtime Snapshot (as of 2026-03-18)
- Gateway: 127.0.0.1:18789 (UI), :18792 (API health), systemd managed � **openclaw v2026.3.13** (updated from 2026.3.8)
- Install type: npm global, stable channel (was: git tag detached HEAD � `openclaw update` now works)
- Node: v22.22.0 (nvm), pnpm 10.23.0
- Skills: 19/59 ready
- Channels: WhatsApp (linked), Telegram (secured), Signal (disabled)
- - Windows nodes: **1 connected** — Windows Desktop (node.cmd v2026.3.13, IP: 172.23.144.1, caps: browser+system) — PowerShell + hostname VERIFIED. WSL sudo: root (passwordless). ynotf: Windows Administrator.
- Model routing: anthropic/claude-sonnet-4-20250514, fallback openai/gpt-4o-mini
- **Sandbox: mode=off** (reverted 2026-03-15 � Docker not installed in WSL; sandbox=all caused gateway crash loop)
- **Docker: v29.1.3 installed + running** — openclaw-sandbox:bookworm-slim container active. sandbox.mode stays off by design (Sparky needs direct host access)
- **Context engine: lossless-claw v0.3.0** (LCM active, db=`~/.openclaw/lcm.db`, native API � legacy fallback warning resolved by 2026.3.13 upgrade)
- exec-approvals.json: security=deny in defaults � policy file exists but NOT enforced without sandbox
- **DroidRun MCP**: added to other Cursor project window (2026-03-16) � phone automation tool for Samsung Galaxy S25 Ultra
- **CrewClaw Employees**: 5/10 deployed in Docker (api-integration-specialist, code-reviewer, financial-analyst, frontend-developer, overnight-coder) — Bitwarden injection, 512M limit each, D:/github:/workspace:rw; 5 pending Telegram bot creation

### Active Blockers

#### BLOCKER 3 — Windows node host — **FULLY RESOLVED 2026-03-17**
- **Was:** Molty removed 2026-03-16 (XamlParseException crash loop)
- **Fix chain:**
  1. Installed headless node host v2026.3.13 via `openclaw node install`
  2. Added `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` to `node.cmd` (break-glass for trusted private LAN)
  3. Device d8e1ddb2 approved in gateway (`openclaw devices approve`)
  4. `tools.exec`: host=node, security=allowlist, node="Windows Desktop"
  5. `exec-approvals.json`: defaults set to security=full, ask=off, askFallback=allow + wildcard `*` allowlist
- **Verified:** hostname→ChaosCentral, powershell.exe Get-Date→Tuesday, March 17, 2026 5:08:20 PM
- **Status:** `nodes status` shows Known:2 Paired:2 Connected:2 — Windows Desktop (IP: 172.23.144.1, v2026.3.13, caps: browser+system)
- **Known limitation:** `nodes run` CLI hangs due to approval socket; agent's `nodes()` tool uses invoke path which works correctly
#### BLOCKER 1 — Sandbox + Docker — **RESOLVED 2026-03-18**
- **Was:** Docker not found in WSL; sandbox.mode: "all" caused gateway crash-loop.
- **Discovery 2026-03-18:** Docker v29.1.3 IS installed and running. Sandbox container openclaw-sandbox:bookworm-slim already active (7h uptime).
- **Decision:** sandbox.mode stays "off" by design — Sparky needs direct host access for autonomous work. Docker sandbox is reserved for CrewClaw employee containers if/when needed.
- **exec-approvals:** Set to security=full, ask=off, askFallback=allow, autoAllowSkills=true — commands run without any approval prompts.
- **Status:** No blocking issue. Sparky has full autonomous access.
#### BLOCKER 2 � Agent session context overflow � **RESOLVED 2026-03-16**
- **Was:** Agent session `e3853d85` overflowed at 171 messages / 171,384 tokens, causing silent failures on WhatsApp/Telegram.
- **Fix (permanent):** Installed `lossless-claw` v0.3.0 LCM plugin (`pnpm openclaw plugins install @martian-engineering/lossless-claw`). Plugin is now the active `contextEngine`. DAG-based summarization prevents overflow permanently.
- **Config:** `freshTailCount=32`, `contextThreshold=0.75`, `incrementalMaxDepth=-1`, `session.reset.idleMinutes=10080`
- **Evidence:** `[lcm] Plugin loaded (enabled=true, db=~/.openclaw/lcm.db, threshold=0.75)` � warning gone, agent responsive.

### Pending User Actions
1. Name agent via WhatsApp (bootstrap conversation) � cosmetic, non-blocking
2. MXRoute email: install imap-smtp-email skill + provide credentials � Phase 7 work

### Known Recurring Issues
| Issue | Trigger | Fix | Permanent Fix Needed |
|---|---|---|---|
| Gateway WebSocket `1006 abnormal closure` | CLI connects before gateway finishes warm-up after restart | Wait 10�12s after restart before running CLI commands | None needed � cosmetic timing issue |
| Agent context overflow ? silent no-response | Session accumulates >170 messages over days | Delete session file, restart gateway | Tune `compaction` settings in openclaw.json |
| Gateway crash loop (Docker missing) | `sandbox.mode: "all"` set without Docker | Revert to `sandbox.mode: "off"` | Install Docker or find non-Docker sandbox |
| Signal restart loop | signal-cli Java version mismatch (needs Java 21, has older) | N/A � channel is disabled | Leave disabled; no action needed |
|| Windows node loses connection after Windows reboot | WSL IP changes on reboot | Run startup script (bws run) which auto-updates IP in node.cmd | None — startup script handles it |

### Cross-Repo State (open--claw)
- Branch: master, clean
- Phase 2 (First Live Integration): COMPLETE � mirrors Phase 6C

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
| docs/ai/archive/state-log-mcp-triworkspace-2026-03-16.md | MCP context optimization + tri-workspace expansion (2026-03-16) | 2 |
| docs/ai/archive/state-log-tab-bootstrap-2026-03-16.md | TAB_BOOTSTRAP_PROMPTS update � Clear Thought 1.5 + tri-workspace (2026-03-16) | 1 |
| docs/ai/archive/state-log-release-p0-gateway-fix-2026-03-16.md | Release docs phase 0 + gateway crash loop diagnosis and fix (2026-03-16) | 3 |

---

## State Log

<!-- AGENT appends entries below this line after each execution block. -->






## 2026-03-17 00:00 � FAIL: gateway.nodes.autoApprove Not Supported in v2026.3.8

### Goal
Add gateway.nodes.autoApprove.local = true to openclaw.json to auto-approve Windows node connections.

### Scope
- ~/.openclaw/openclaw.json (WSL, local-only)

### Commands / Tool Calls
- Shell: backup ? openclaw.json.bak.autoapprove (PASS)
- Shell: Python3 heredoc � add c['gateway']['nodes']['autoApprove'] = {'local': True} (PASS � written)
- Shell: verify {'autoApprove': {'local': True}} in gateway.nodes (PASS)
- Shell: systemctl --user restart openclaw-gateway.service (PASS)
- Shell: openclaw nodes status ? config validation error (FAIL)
- Shell: restore from backup (PASS), verify JSON valid (PASS)
- Shell: restart gateway with clean config (PASS), health check PASS

### Changes
None � backup restored. openclaw.json is identical to pre-edit state.

### Evidence
| Check | Result |
|-------|--------|
| Backup created (.bak.autoapprove) | PASS |
| JSON edit applied (autoApprove written) | PASS |
| gateway.nodes.autoApprove.local verified in file | PASS |
| Gateway restart with new config | PASS (restarted) |
| openclaw nodes status after restart | **FAIL** |
| Error | Invalid config: gateway.nodes: Unrecognized key: "autoApprove" |
| Backup restored | PASS |
| Restored JSON valid | PASS |
| Gateway restarted with clean config | PASS |
| Gateway health � Telegram: ok | PASS |

### Root Cause
gateway.nodes.autoApprove is **not a recognized key in OpenClaw v2026.3.8**. The schema validator rejects it at startup. The feature either:
- Exists in v2026.3.13 (newer version the config was last written by)
- Does not exist under this exact key path in any version
- Uses a different config key name

### Verdict
**FAIL** � config key not supported in installed version. Backup restored. Gateway healthy.

### Blockers
Windows node connection remains blocked by code=1008 device identity requirement.

### Fallbacks Used
- Restored from openclaw.json.bak.autoapprove after validation failure.

### Cross-Repo Impact
None � no files committed.

### Pending Actions for PLAN
1. Check OpenClaw v2026.3.13 changelog for correct autoApprove config key name
2. Query Context7: "OpenClaw node auto-approve device pairing configuration"
3. Option: upgrade to v2026.3.13 if autoApprove is available there
4. Option: evaluate if Windows node is actually needed � droidrun MCP already provides phone control

### What's Next
STOP � escalate to PLAN. Windows node connection remains BLOCKED.

## 2026-03-17 � PARTIAL: Windows Execution Config Applied; node run Blocked by WSL Node Identity Issue

### Goal
Configure Sparky's agent execution to use ChaosCentral (Windows node) and set an execution allowlist so Sparky can run Windows commands without per-command approval prompts.

### Scope
- ~/.openclaw/openclaw.json (WSL, local-only, via openclaw config set)
- ~/.openclaw/exec-approvals.json (WSL, local-only, via openclaw approvals allowlist add)
- AI-Project-Manager/docs/ai/STATE.md
- AI-Project-Manager/docs/ai/memory/DECISIONS.md

### Commands / Tool Calls
`
pnpm openclaw config set tools.exec.host node
pnpm openclaw config set tools.exec.security allowlist
pnpm openclaw config set tools.exec.node ChaosCentral
pnpm openclaw config get tools.exec
pnpm openclaw approvals allowlist add --node ChaosCentral '*'
pnpm openclaw approvals get
systemctl --user restart openclaw-gateway.service
pnpm openclaw nodes status
pnpm openclaw nodes run --node ChaosCentral --raw 'hostname'
`

### Changes
- 	ools.exec.host = 
ode (PASS)
- 	ools.exec.security = llowlist (PASS)
- 	ools.exec.node = ChaosCentral (PASS)
- xec-approvals.json: wildcard * pattern added for ChaosCentral node ID 847202f0...bea4e, agent * (PASS)

### Evidence
| Check | Result |
|-------|--------|
| tools.exec.host=node set | PASS |
| tools.exec.security=allowlist set | PASS |
| tools.exec.node=ChaosCentral set | PASS |
| config get tools.exec verified | PASS � {host:node, security:allowlist, node:ChaosCentral} |
| pprovals allowlist add --allow-all | FAIL � unknown option |
| pprovals allowlist add '*' (glob wildcard) | PASS � allowlist entry created |
| pprovals get shows ChaosCentral in allowlist | PASS |
| Gateway restart | PASS |
| 
odes status after restart | PASS � Known:1 Paired:1 Connected:1 |
| 
odes run --raw 'hostname' | FAIL � invalid system.run.prepare response |
| 
odes run --raw 'echo hello' | FAIL � same error |

### Root Cause of 
odes run Failure
The "ChaosCentral" node shown in 
odes status is the **WSL-embedded node host** (running inside the gateway's own v2026.3.13 process), NOT the Windows node.cmd host. Evidence:
1. Node Detail column shows path: ~/.nvm/versions/node/v22.22.0/bin:/usr/local/bin... � these are WSL paths, not Windows paths
2. 
ode-host.log.err shows the Windows node.cmd STILL failing: SECURITY ERROR: Cannot connect to "172.23.156.209" over plaintext ws://
3. Gateway log shows 
ode host PATH: /home/ynotf/.nvm/... � confirming WSL node
4. WSL embedded node has caps rowser, system but system.run.prepare fails because it's not a real execution host � it's the gateway's own loopback node
5. OpenClaw v2026.3.8 (installed via build) vs v2026.3.13 (Windows node.cmd version) � the embedded node runs v2026.3.13

### Verdict
**PARTIAL** � 	ools.exec config and xec-approvals.json successfully configured. Windows node.cmd still cannot connect due to plaintext WebSocket security rejection. The connected node is the WSL embedded node, not Windows.

### Blockers
**BLOCKER (UNCHANGED):** Windows node.cmd cannot connect to gateway over ws://172.23.156.209:18789 because OpenClaw enforces WSS (TLS) for non-loopback connections. Error: SECURITY ERROR: Cannot connect over plaintext ws://. Set OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 for trusted private networks.

### Fallbacks Used
- --allow-all not supported ? used glob '*' pattern instead

### Cross-Repo Impact
None committed. openclaw.json and exec-approvals.json are WSL-local files.

### Decisions Captured
See DECISIONS.md: 	ools.exec config + allowlist applied; Windows node still blocked by plaintext WS.

### Pending Actions for PLAN
**Option A (easiest):** Set OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 in the Windows node.cmd environment � the gateway already accepts it over a private network (Tailscale/LAN). The error message explicitly mentions this env var as the break-glass option.
**Option B:** SSH tunnel from Windows to WSL (ssh -N -L 18789:127.0.0.1:18789) so Windows node connects to 127.0.0.1 (loopback-safe).
**Option C:** Accept WSL node as the execution host � but system.run is not working on embedded WSL node.
**Option D:** Re-evaluate whether Windows node is needed given droidrun MCP already covers phone control.

### What Remains Unverified
- Whether OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 in 
ode.cmd resolves the connection without further issues
- Whether system.run works on a real Windows node once connected

### What's Next
STOP � escalate to PLAN. Recommend trying Option A (OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1) as lowest-friction fix.


## 2026-03-17 17:08 — RESOLVED: Windows Desktop Node Connected + PowerShell Execution Verified

### Goal
Complete Windows node connection and verify PowerShell execution access for Sparky (gate 2: execution, after gate 1 pairing already done).

### Scope
- `C:\Users\ynotf\.openclaw\node.cmd` (local Windows file, not in git)
- `~/.openclaw/exec-approvals.json` (local WSL file, not in git)
- `~/.openclaw/openclaw.json` (local WSL file, not in git, via `openclaw config set`)
- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/memory/DECISIONS.md`

### Commands / Tool Calls
- Added `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` to `node.cmd` (line 12)
- Restarted Windows node service
- `openclaw devices approve d8e1ddb2` (approved Windows Desktop pairing request)
- `openclaw config set tools.exec.node "Windows Desktop"`
- `exec-approvals.json`: defaults changed to `security=full, ask=off, askFallback=allow`
- `openclaw approvals allowlist add --node "Windows Desktop" '*'`
- `openclaw nodes status` (verified Known:2 Paired:2 Connected:2)
- `openclaw nodes invoke --node "Windows Desktop" system.run hostname`
- `openclaw nodes invoke --node "Windows Desktop" system.run powershell.exe Get-Date`

### Changes
| File | Change |
|------|--------|
| `node.cmd` | Added `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` env var |
| `exec-approvals.json` | defaults: security=full, ask=off, askFallback=allow |
| `openclaw.json` | `tools.exec.node` = "Windows Desktop" |
| `exec-approvals.json` | Wildcard `*` allowlist for Windows Desktop, all agents |

### Evidence
| Check | Result | Output |
|-------|--------|--------|
| `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` added to node.cmd | PASS | — |
| Device d8e1ddb2 approved | PASS | — |
| `nodes status`: Known:2 Paired:2 Connected:2 | PASS | Windows Desktop IP: 172.23.144.1, v2026.3.13, caps: browser+system |
| `nodes invoke system.run hostname` | PASS | ChaosCentral |
| `nodes invoke system.run powershell.exe Get-Date` | PASS | Tuesday, March 17, 2026 5:08:20 PM |
| `nodes run` CLI | FAIL | Hangs — approval socket communication issue (WSL↔Windows). Not blocking for agent. |

### Verdict
**PASS** — Windows Desktop node fully operational. Sparky can run PowerShell and system commands on Windows via `nodes()` invoke path.

### Blockers
None for Windows node execution. The only remaining blocker is BLOCKER 1 (sandbox/Docker for exec-approvals enforcement).

### Fallbacks Used
- `exec-approvals.json` defaults set to `askFallback=allow` so commands don't block when approval socket is unreachable from CLI.

### Cross-Repo Impact
None — no files committed in other repos.

### Decisions Captured
See DECISIONS.md: "Windows node full resolution — OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 + exec-approvals"

### Pending Actions
1. Decide on Docker installation (BLOCKER 1 — sandbox enforcement)
2. Name agent via WhatsApp (cosmetic)
3. MXRoute email: install imap-smtp-email skill (Phase 7)

### What Remains Unverified
- Whether `nodes run` CLI hang can be resolved (lower priority — agent invoke path works)
- Long-term stability of Windows node after multiple reboots (startup script should handle IP changes)

### What's Next
Phase 7 planning — agent naming, MXRoute email integration, expanded skill setup.

## 2026-03-18 19:11 — RESOLVED: Sparky Full Autonomous Access (sudo + Windows Admin + exec-approvals full + Docker confirmed)

### Goal
Remove all execution blocks so Sparky can run commands on WSL, Windows, and Docker without per-command approval prompts or password requirements, enabling autonomous unattended operation.

### Scope
- `~/.openclaw/openclaw.json` (WSL, local-only)
- `~/.openclaw/exec-approvals.json` (WSL, local-only)
- `/etc/sudoers.d/ynotf-nopasswd` (WSL, local-only)
- `C:\Users\ynotf\.openclaw\node.cmd` (Windows, local-only)
- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/ai/memory/DECISIONS.md`

### Commands / Tool Calls
- Shell: `cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak.fullaccess` (backup)
- Shell: Python3 — set `sandbox.mode=off`, `tools.exec.host=node`, `tools.exec.security=full`, `tools.exec.node="Windows Desktop"`
- Shell: Python3 — set `exec-approvals.json` defaults + agents.main: `security=full, ask=off, askFallback=allow, autoAllowSkills=true`
- Shell: `wsl -u root` — write `/etc/sudoers.d/ynotf-nopasswd` + `visudo -cf` validation
- PowerShell: `Get-LocalGroupMember` — verified ynotf already in Administrators
- Shell: `systemctl --user restart openclaw-gateway.service`
- Shell: Killed stale node processes, restarted `node.cmd`
- Shell: `pnpm openclaw nodes status` — Windows Desktop paired · connected
- Shell: `nodes invoke system.run hostname` → ChaosCentral (PASS)
- Shell: `nodes invoke system.run powershell.exe -Command Get-Date` → Wednesday, March 18, 2026 7:11:57 PM (PASS)
- Shell: `sudo whoami` (direct WSL) → root (PASS)
- Shell: `docker ps` + `docker info` → v29.1.3 running, sandbox container active (PASS)

### Changes
| Target | Change |
|--------|--------|
| `openclaw.json` | `sandbox.mode`: all → off |
| `openclaw.json` | `tools.exec.host`: sandbox → node |
| `openclaw.json` | `tools.exec.security`: allowlist → full |
| `openclaw.json` | `tools.exec.node`: ChaosCentral → Windows Desktop |
| `exec-approvals.json` | defaults: security=full, ask=off, askFallback=allow, autoAllowSkills=true |
| `exec-approvals.json` | agents.main: security=full, ask=off, askFallback=allow, autoAllowSkills=true |
| `/etc/sudoers.d/ynotf-nopasswd` | Created: `ynotf ALL=(ALL) NOPASSWD: ALL` |
| Windows Administrators | ynotf already a member (no change needed) |

### Evidence
| Check | Result | Output |
|-------|--------|--------|
| openclaw.json backup | PASS | .bak.fullaccess created |
| sandbox.mode=off | PASS | verified via Python3 |
| tools.exec.host=node | PASS | verified |
| tools.exec.security=full | PASS | verified |
| exec-approvals defaults | PASS | security=full, ask=off, askFallback=allow |
| exec-approvals agents.main | PASS | security=full, ask=off, askFallback=allow |
| sudoers file written | PASS | visudo parsed OK |
| `sudo whoami` (no prompt) | PASS | root |
| ynotf in Administrators | PASS | already member |
| Gateway restart | PASS | |
| nodes status | PASS | Windows Desktop paired · connected (891178e9) |
| `nodes invoke hostname` | PASS | ChaosCentral |
| `nodes invoke powershell Get-Date` | PASS | Wednesday, March 18, 2026 7:11:57 PM |
| Docker v29.1.3 | PASS | sandbox container running |
| `nodes invoke ChaosCentral` | FAIL (expected) | ChaosCentral = WSL-embedded, only connected when gateway first starts |

### Verdict
**PASS** — Sparky has full autonomous access: WSL root (passwordless sudo), Windows Administrator, Docker, exec-approvals full (no approval prompts). Windows Desktop node operational.

### Blockers
None. All execution blockers resolved.

### Fallbacks Used
- `sudo` required `wsl -u root` approach (interactive prompt avoided)
- Used `nodes invoke` instead of `nodes run` for testing (socket hang workaround)

### Cross-Repo Impact
None — all changed files are local-only (not in any repo).

### Decisions Captured
See DECISIONS.md: "Sparky full autonomous access" + "Docker v29.1.3 discovered — BLOCKER 1 resolved"

### Pending Actions
1. Name agent via WhatsApp (cosmetic, non-blocking)
2. MXRoute email integration (Phase 7)

### What Remains Unverified
- `nodes run` CLI still hangs (known limitation — agent invoke path works, not blocking)
- Docker sandbox mode available if ever needed (currently off by design)

### What's Next
Phase 7 — agent persona setup, MXRoute email skill, expanded integrations.

## 2026-03-18 21:30 -- CrewClaw Employees Deployed via Docker + Bitwarden Injection

### Goal
Deploy 5 pre-configured CrewClaw employees as Docker containers with secrets injected at startup via Bitwarden -- no .env files ever touch disk.

### Scope
- `D:\github\open--claw\open-claw\employees\deployed\` (gitignored)
- `D:\github\open--claw\.gitignore` (added `open-claw/employees/deployed/`)
- `D:\github\AI-Project-Manager\.gitignore` (added `docs/ai/protected/` and `.openclaw/`)
- `AI-Project-Manager/docs/ai/STATE.md` (this entry)
- `AI-Project-Manager/docs/ai/DECISIONS.md` (new entry)

### Commands / Tool Calls
- `bws secret get <id>` x 6 (anthropic + 5 telegram tokens)
- `Expand-Archive` x 5 employee zips
- `Get-ChildItem -Recurse -Filter ".env*" | Remove-Item` -- removed 5 .env.example files
- `docker compose build` -- all 5 images built
- `docker compose up -d` -- all 5 started in one shell call with env vars in scope
- `docker ps --filter "name=crewclaw"` -- 5 containers Up verified

### Changes
- `.gitignore` (AI-PM): added `docs/ai/protected/` + `.openclaw/`
- `.gitignore` (open--claw): added `open-claw/employees/deployed/`
- `deployed/start-employees.ps1`: created -- fetches secrets from Bitwarden, sets env vars, runs docker compose up -d
- `deployed/docker-compose.yml`: created -- 5 services, 512M limit each, D:/github:/workspace:rw mount, env from process vars
- Dockerfiles: fixed `COPY bot.js` to `COPY bot-telegram.js` in all 5 (bug in CrewClaw template)
- `.env.example` removed from all 5 employee directories

### Evidence
- PASS: All 6 secrets fetched (ANTHROPIC len=108, Telegram tokens len=46 x5)
- PASS: 5 containers Up (api-integration-specialist, code-reviewer, financial-analyst, frontend-developer, overnight-coder)
- PASS: docker logs -- all 5 show "Bot is running..."
- PASS: zero .env files in deployed/ directory
- PASS: zero secret pattern hits in any file on disk

### Verdict
PASS -- All 5 ready employees deployed. No secrets on disk.

### Blockers
- restart: unless-stopped means containers restart on Docker daemon restart but WITHOUT secrets (tokens will be blank). start-employees.ps1 must be re-run after each system restart.
- 5 pending employees (personal-crm, script-builder, seo-specialist, software-engineer, ux-designer) need Telegram bots created first.

### Fallbacks Used
- BWS_ACCESS_TOKEN loaded from User registry (stored there by startup script but not always inherited by Cursor terminals)
- Dockerfile bot.js bug fixed in all 5 employees before build

### Cross-Repo Impact
- open--claw/.gitignore updated (deployed/ excluded)
- AI-Project-Manager/.gitignore updated (protected/ excluded)

### Decisions Captured
See DECISIONS.md: "CrewClaw employees deployed with Bitwarden secret injection -- no .env files (2026-03-18)"

### Pending Actions
1. Create Telegram bots for 5 pending employees -> add tokens to Bitwarden -> deploy
2. Document restart procedure: run start-employees.ps1 after each system restart
3. Consider: Windows Task Scheduler trigger for start-employees.ps1 on Docker start

### What Remains Unverified
- Container behavior after Windows reboot (restart: unless-stopped restarts with blank tokens without start-employees.ps1)
- Long-term Telegram bot connectivity

### What's Next
CrewClaw employee naming/persona setup, pending employee Telegram bot creation, Phase 7 integrations.
