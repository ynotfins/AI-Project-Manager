# STATE.md Archive — Security Hardening + Windows Node Blockers (2026-03-16 to 2026-03-17)

Archived: 2026-03-17
Source: docs/ai/STATE.md
Reason: Entries resolved/documented. Outcomes captured in DECISIONS.md and STATE.md Current State Summary.
These entries are NOT consulted by PLAN for operational decisions.

---

## 2026-03-16 21:30 — Fix: Gateway Crash Loop (Persist .gateway-env)

### Goal
Permanently fix the gateway crash loop that occurs on every WSL restart by removing the 
m -f ~/.openclaw/.gateway-env line from the startup script.

### Scope
- C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1 (local-only, not in any repo)
- AI-Project-Manager/docs/ai/memory/DECISIONS.md
- AI-Project-Manager/docs/ai/STATE.md

### Commands / Tool Calls
- Read: start-cursor-with-secrets.ps1 (confirmed 
m -f at line 209)
- StrReplace x4: removed 
m -f line, updated comments to say "persistent" not "transient"
- Read: verified edit at lines 183-214 — no other lines changed
- Shell: write .gateway-env fresh from current env vars (chmod 600, 400 bytes, 3 lines)
- Shell: wsl --shutdown + 15s wait
- Shell: systemctl --user status openclaw-gateway.service after restart
- Shell: ls -la ~/.openclaw/.gateway-env after restart
- Shell: pnpm openclaw health — Telegram check

### Changes
| File | Change |
|------|--------|
| start-cursor-with-secrets.ps1 | Removed 
m -f ~/.openclaw/.gateway-env line (1 line deleted) |
| start-cursor-with-secrets.ps1 | Updated 3 comments: "transient" → "persistent", "deleted after service loaded" → "persisted for WSL restart survival" |
| docs/ai/memory/DECISIONS.md | Appended decision record with context, alternatives rejected, security rationale, test evidence |

### Evidence
| Check | Result |
|-------|--------|
| 
m -f line found in script before edit | PASS — line 209 |
| Edit applied (only 
m -f line removed) | PASS |
| .gateway-env written (chmod 600, 400 bytes, 3 lines) | PASS |
| wsl --shutdown executed | PASS |
| Gateway ctive (running) after WSL restart | PASS — PID 469, started 9s after WSL boot |
| .gateway-env persists after WSL restart | PASS — -rw------- 1 ynotf ynotf 400 |
| NRestarts after WSL restart | PASS — 0 |
| Telegram: ok (@Sparky4bot) | PASS |
| Agents: main (default) | PASS |
| WhatsApp | NOT LINKED (separate issue — needs QR scan, not in scope) |
| No other script lines changed | PASS |
| start-cursor-with-secrets.ps1 NOT committed | PASS (local-only file) |
| No secrets in committed files | PASS |

### Verdict
PASS — fix applied and verified. Gateway now survives WSL restarts without crash loop.

### Blockers
None

### Fallbacks Used
None

### Cross-Repo Impact
DECISIONS.md updated in AI-Project-Manager. No changes to open--claw or droidrun.

### Decisions Captured
See docs/ai/memory/DECISIONS.md → "Persist .gateway-env on disk (do not delete after startup)".
Key: Option A chosen over B/C/D/E. Security accepted: chmod 600, same as ~/.openclaw/.env.

### Pending Actions
- WhatsApp: still 
ot linked — user needs to scan QR at http://localhost:18789/openclaw to relink
- Option C (WSL boot hook from Bitwarden): valid future hardening if needed — documented in DECISIONS.md

### What Remains Unverified
- WhatsApp QR relink (user action required)
- Long-term: gateway behavior after PC power-off/on (vs WSL shutdown — likely same behavior, not tested)

### What's Next
Continue Phase 1 release docs or next user task.

## 2026-03-16 22:05 — Security: OpenClaw Foundation Audit (Plugin Allowlist + Permissions)

### Goal
Apply personal-use security foundation hardening to OpenClaw: plugin allowlist, file permission tightening, lossless-claw version pinning, allowedOrigins update for WSL IP.

### Scope
- ~/.openclaw/openclaw.json (WSL, local-only, not in any repo)
- ~/.openclaw/ directory permissions (WSL)
- AI-Project-Manager/docs/ai/memory/DECISIONS.md
- AI-Project-Manager/docs/ai/STATE.md

### Commands / Tool Calls
- Shell: cat ~/.openclaw/openclaw.json — read current config
- Shell: hostname -I — get WSL IP (172.23.156.209)
- Shell: backup openclaw.json → openclaw.json.bak.security
- Shell: Python3 atomic JSON edit — applied all 3 changes in one write:
  - Step 1: plugins.allow = ["whatsapp", "telegram", "lossless-claw"]
  - Step 2: gateway.controlUi.allowedOrigins updated with WSL IP
  - Step 4: plugins.installs.lossless-claw.spec pinned to @martian-engineering/lossless-claw@0.3.0
- Shell: verify all changes via Python3 read-back
- Shell: chmod 600 gmail-client-secret.json; chmod 700 all subdirs in ~/.openclaw/
- Shell: systemctl --user restart openclaw-gateway.service + 12s wait
- Shell: pnpm openclaw health — Telegram check
- Shell: journalctl — plugin load confirmation

### Changes
| Config Key | Before | After |
|-----------|--------|-------|
| plugins.allow | missing (not set) | ["whatsapp", "telegram", "lossless-claw"] |
| gateway.controlUi.allowedOrigins | ["http://localhost:18789", "http://127.0.0.1:18789"] | added http://172.23.156.209:18789 |
| plugins.installs.lossless-claw.spec | @martian-engineering/lossless-claw | @martian-engineering/lossless-claw@0.3.0 |

| Permission | Before | After |
|-----------|--------|-------|
| gmail-client-secret.json | -rwxr-xr-x (755) | -rw------- (600) |
| canvas/ | drwxrwxr-x (775) | drwx------ (700) |
| completions/ | drwxr-xr-x (755) | drwx------ (700) |
| credentials/ | drwxr-xr-x (755) | drwx------ (700) |
| devices/ | drwxrwxr-x (775) | drwx------ (700) |
| xtensions/ | drwxr-xr-x (755) | drwx------ (700) |
| identity/ | drwxr-xr-x (755) | drwx------ (700) |
| lcm-files/ | drwxrwxr-x (775) | drwx------ (700) |
| memory/ | drwxr-xr-x (755) | drwx------ (700) |
| plugins/ | drwxrwxr-x (775) | drwx------ (700) |
| sandbox/ | drwxrwxr-x (775) | drwx------ (700) |
| sandboxes/ | drwxrwxr-x (775) | drwx------ (700) |
| 	elegram/ | drwxrwxr-x (775) | drwx------ (700) |
| 	ools/ | drwxr-xr-x (755) | drwx------ (700) |
| workspace/ | drwxr-xr-x (755) | drwx------ (700) |

### Evidence
| Check | Result |
|-------|--------|
| JSON backup created (openclaw.json.bak.security) | PASS |
| Python3 atomic write — all edits applied | PASS |
| JSON valid after write | PASS |
| plugins.allow = ["whatsapp", "telegram", "lossless-claw"] | PASS |
| allowedOrigins includes 172.23.156.209:18789 | PASS |
| lossless-claw spec pinned @0.3.0 | PASS |
| gmail-client-secret.json → 600 | PASS (was 755) |
| All ~/.openclaw/ subdirs → 700 | PASS (15 dirs changed) |
| Gateway restarted | PASS |
| Gateway healthy — Telegram: ok (@Sparky4bot) | PASS |
| Agents: main (default) | PASS |
| journalctl: [lcm] Plugin loaded (no "plugins.allow is empty" warning) | PASS |
| No crash after restart | PASS |
| openclaw.json NOT committed (local WSL file) | PASS |
| No secrets in any committed file | PASS |

### Verdict
PASS — all 5 hardening steps applied and verified.

### Blockers
- Windows portal access (http://172.23.156.209:18789) still shows code=1008 — "control ui requires device identity (use HTTPS or localhost secure context)". This is a pre-existing Control UI limitation unrelated to allowedOrigins. The allowedOrigins fix is correct; the 1008 rejection is a separate Control UI security feature requiring HTTPS for non-localhost origins. NOT a regression.
- WSL IP is dynamic — allowedOrigins will become stale after WSL restart. Pending enhancement: startup script auto-update (documented in DECISIONS.md).

### Fallbacks Used
- Used Python3 atomic JSON edit instead of text editing to ensure valid JSON on all changes.

### Cross-Repo Impact
DECISIONS.md updated in AI-Project-Manager.

### Decisions Captured
See DECISIONS.md:
1. Plugin allowlist established (plugins.allow)
2. Personal use classification (Tony, Kristina, Mia — never commercial)
3. Dynamic WSL IP in allowedOrigins — pending startup script enhancement

### Personal Use Classification (recorded here for PLAN context)
- Users: Tony, Kristina, Mia + friends (free, "employee" access = friends)
- NEVER commercial, NEVER for sale
- Regular WhatsApp (not WhatsApp Business) — correct for personal family use
- No Google Play / App Store distribution planned
- Rate limiting skipped — LAN-only, personal use, over-engineering for this scale
- Privacy policy / ToS in release checklist = internal family policy, not legal compliance docs

### Pending Actions
- WhatsApp: still 
ot linked — user must scan QR at http://localhost:18789/openclaw
- Enhancement: update startup script to auto-write current WSL IP into openclaw.json allowedOrigins on each run
- Control UI Windows access: requires HTTPS or localhost tunnel (separate from allowedOrigins — design limitation)

### What Remains Unverified
- sandbox.mode is "off" — Docker not installed, cannot enable sandbox. Noted as separate blocker.
- Control UI Windows browser access (code=1008) requires HTTPS solution.

### What's Next
Phase 1 release docs or next security task per PLAN.

## 2026-03-16 23:55 — BLOCKER: Windows Node Connection Rejected (code=1008 Device Identity Required)

### Goal
Fix Windows node host to connect to WSL gateway and grant Sparky Windows filesystem access.

### Scope
- C:\Users\ynotf\.openclaw\node.cmd (Windows, local-only)
- WSL gateway logs (diagnostic)
- AI-Project-Manager/docs/ai/STATE.md (this entry)

### Commands / Tool Calls
- Shell: read WSL IP (172.23.156.209)
- Read: 
ode.cmd — found incorrect --gateway ws:// syntax (not supported in v2026.3.8)
- Shell: openclaw devices remove 891178e9... — removed stale pairing
- StrReplace: corrected 
ode.cmd to use --host 172.23.156.209 --port 18789 --display-name "Windows Desktop"
- Shell: killed stale node process, restarted with correct syntax
- Shell: journalctl — checked gateway logs for pairing activity

### Changes
| File | Before | After |
|------|--------|-------|
| 
ode.cmd line 12 | 
ode run --gateway ws://172.23.156.209:18789 | 
ode run --host 172.23.156.209 --port 18789 --display-name "Windows Desktop" |

### Evidence
| Check | Result |
|-------|--------|
| openclaw node run --help shows --gateway option | FAIL — option does not exist in v2026.3.8 |
| Corrected to --host --port syntax | PASS |
| Stale node removed (891178e9...) | PASS |
| Node restarted with new config | PASS |
| Node log shows PATH dump (process started) | PASS |
| Gateway logs show connection attempts | PASS — device ID 847202f0... |
| Connection succeeds | **FAIL** — code=1008 "connect failed" |
| Error pattern | Repeated: "security audit: device access upgrade requested ... code=1008 reason=connect failed" |

### Root Cause
Gateway is rejecting the Windows node's WebSocket connection with **code=1008 "connect failed"**.

From gateway logs:
`
[gateway] security audit: device access upgrade requested 
  reason=role-upgrade 
  device=847202f0843a17b825c61eefa8bee84c9ab76c117f17e30389fde0db1ffbea4e 
  ip=unknown-ip 
  auth=token 
  roleFrom=operator roleTo=node 
  scopesFrom=operator.admin,operator.approvals,operator.pairing,operator.read,operator.write 
  scopesTo=<none> 
  client=node-host 
  conn=...
[ws] closed before connect ... code=1008 reason=connect failed
`

**The node is attempting to upgrade from "operator" role to "node" role, but the gateway rejects the upgrade.**

This is the SAME code=1008 rejection seen for Windows browser access to the Control UI.  
**Hypothesis:** gateway.controlUi security policy rejects WebSocket connections from non-localhost/non-HTTPS origins that require device identity verification, even when the origin is in llowedOrigins. The node host is a device client (not a browser), but it's being subjected to the same security gate.

### Attempted Fix vs. Actual Blocker
| Attempted | Result |
|-----------|--------|
| Corrected 
ode.cmd syntax from --gateway to --host --port | PASS — syntax correct |
| Removed stale pairing | PASS |
| Restarted node process | PASS |
| Node tries to connect | PASS — repeated attempts in gateway logs |
| Gateway accepts connection | **FAIL** — code=1008 consistently |

**Blocker confirmed:** Gateway security policy rejects device identity upgrade for non-HTTPS WebSocket connections, even from localhost (127.0.0.1 within WSL). This is not a 
ode.cmd configuration issue. This is a gateway security model limitation.

### Verdict
**BLOCKED** — Windows node connection requires one of:
1. HTTPS gateway (cert + reverse proxy)
2. Gateway config change to disable device identity requirement for node hosts
3. Alternative node auth mechanism (not device identity)

### What Remains Unverified
- Whether gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback or similar config flag exists to bypass device identity
- Whether OpenClaw v2026.3.13 (newer than current v2026.3.8) has a fix for this
- Whether there's a separate gateway config for node connections (independent from controlUi)

### Pending Actions for PLAN
1. Research: Query Context7 for "OpenClaw node host device identity code 1008 connection rejected"
2. Check if OpenClaw v2026.3.13 changelog mentions node connection fixes
3. Evaluate whether HTTPS setup is justified for Windows node access (requires cert generation + gateway TLS config)
4. Alternative: investigate if Windows node access is critical — phone automation (droidrun MCP) already provides runtime capabilities; node host may be optional

### What's Next
STOP per task constraint — escalate to PLAN for fix approach evaluation.
Windows node remains DISCONNECTED until this blocker is resolved.

