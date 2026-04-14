# STATE.md Archive — Release Docs Phase 0 + Gateway Crash Diagnosis (2026-03-16)

Archived: 2026-03-16
Source: docs/ai/STATE.md
Reason: Release docs phase 0 complete; gateway crash loop diagnosed and fixed.
These entries are NOT consulted by PLAN for operational decisions.

---

## 2026-03-16 20:00 — Release Documentation Phase 0: Foundation Docs

### Goal
Create the master release checklist and 5 foundation documents in AI-Project-Manager/docs/release/ using real data extracted from all three repos. Internal v1.0 release documentation — no public release language, no Google Play / App Store references.

### Scope
- AI-Project-Manager/docs/release/ (new directory + 6 files)
- AI-Project-Manager/docs/ai/STATE.md (this entry)
- No changes to open--claw or droidrun

### Commands / Tool Calls
- Shell: New-Item docs/release/ directory
- Read: vendor/openclaw/package.json (52 npm deps extracted)
- Read: open-claw/configs/openclaw.template.json5 (gateway/agents/channels/skills config)
- Read: droidrun/mcp_server.py (3 MCP tools, DEFAULT_DEVICE, provider logic)
- Read: droidrun/docs/architecture_overview.md (device info, network topology, secret injection)
- Read: droidrun/src/pyproject.toml (18 Python deps + optional extras)
- Read: vendor/openclaw/apps/android/app/build.gradle.kts (28 Android deps, signing config)
- Read: droidrun/src/.github/workflows/ (6 workflow files)
- Read: vendor/openclaw/docs/help/environment.md (OpenClaw env var precedence)
- Read: droidrun/docs/environment-config-reference.md (DroidRun config reference)
- Read: start-cursor-with-secrets.ps1 (required/optional env vars)
- Clear Thought 1.5: systems_thinking operation (architecture boundary analysis)
- Write: 6 files in docs/release/
- Shell: grep verification (no store refs, real package names present)

### Changes
| File | Action | Notes |
|------|--------|-------|
| docs/release/RELEASE_CHECKLIST.md | Created | 23 items + 4 release tasks; 5 checked |
| docs/release/system-architecture.md | Created | Mermaid diagrams (system, user→agent, phone control); service boundary table; MCP server table |
| docs/release/repo-boundaries.md | Created | 3-layer breakdown; integration contracts; mermaid cross-repo map; decision log |
| docs/release/sbom.md | Created | 52 npm + 28 Android + 18 Python + 0 AI-PM deps; license risk notes |
| docs/release/configuration.md | Created | All env vars from all 3 repos; secret delivery flow; rotation process |
| docs/release/ci-cd.md | Created | 6 droidrun workflows; no CI in open--claw (gap documented); Android manual build |

### Evidence
| Check | Result |
|-------|--------|
| docs/release/ directory exists | PASS |
| RELEASE_CHECKLIST.md has 5 [x] items | PASS |
| system-architecture.md has mermaid diagrams | PASS — 3 diagrams (graph TB, sequenceDiagram x2) |
| system-architecture.md uses real service names (:18789, :18792, Baileys, etc.) | PASS |
| sbom.md contains @whiskeysockets/baileys | PASS |
| sbom.md contains llama-index | PASS |
| sbom.md contains openclaw | PASS |
| No Google Play / App Store references in any doc | PASS |
| No secrets in any doc | PASS |
| ci-cd.md documents 6 droidrun workflows | PASS |
| ci-cd.md notes no CI in open--claw and AI-PM | PASS |
| STATE.md line count before entry (360) | PASS — no archive needed |
| Clear Thought 1.5 systems_thinking used before system-architecture.md | PASS |

### Verdict
READY — all 6 files created, grep verifications PASS, checklist updated.

### Blockers
None

### Fallbacks Used
- Clear Thought 1.5 systems_thinking returned JSON scaffold; architecture derived from real scanned data.

### Cross-Repo Impact
None — all changes in AI-Project-Manager only. open--claw and droidrun not modified.

### Decisions Captured
- Release docs live in AI-Project-Manager/docs/release/ (orchestration layer owns cross-cutting docs)
- droidrun CI/CD workflows are upstream (github.com/droidrun/droidrun) — they run in the upstream GitHub environment, not our local fork
- @whiskeysockets/baileys flagged Medium risk (GPL-3.0) — acceptable for internal deployment; must be reviewed if system is commercialized
- @lydell/node-pty flagged Medium risk (native shell access) — mitigated by sandbox config in openclaw.json
- open--claw has no CI/CD — gap documented; recommended workflows listed in ci-cd.md

### Pending Actions
- Phase 1: agent-skill-registry.md, security-data-privacy.md, owasp-llm-review.md, kill-switch-runbook.md, rollback-plan.md

### What Remains Unverified
- Token cost data for token-costs.md requires actual usage metrics from user
- Privacy Policy and Terms of Service drafts need legal review
- OWASP LLM review requires security expertise — Phase 1 item

### What's Next
Phase 1 — Security & Agent Docs:
1. agent-skill-registry.md (scan openclaw.template.json5 skills + vendored code)
2. security-data-privacy.md (data flow, Bitwarden, ADB tunnel security)
3. owasp-llm-review.md (OWASP Top 10 for LLM Apps)
4. kill-switch-runbook.md (gateway stop, systemd disable, feature flags)
5. rollback-plan.md (version rollback via VENDOR_PIN.md)

## 2026-03-16 21:15 — BLOCKER: Gateway Crash Loop on WSL Restart (API Keys Not Persisted)

### Goal
Document the recurring gateway crash-loop failure for PLAN to diagnose and design a permanent fix.
Gateway is currently RUNNING (manually recovered), but will crash again on next WSL restart.

### Scope
- open--claw: WSL2, ~/.config/systemd/user/openclaw-gateway.service + .service.d/api-keys.conf
- open--claw: ~/.openclaw/.gateway-env (transient — the root of the problem)
- AI-Project-Manager: this STATE.md entry
- No code changed in this entry — diagnosis only

---

## DIAGNOSIS: What Happened

### Failure Sequence (confirmed by journalctl)

`
1. WSL restarted (multiple times — different systemd PIDs: 343, 427, 447, 506, 433)
   Cause: WSL exits/restarts when all terminal sessions close, or after PC wake from sleep.

2. Cursor startup script (start-cursor-with-secrets.ps1) ran and:
   a. Fetched API keys from Bitwarden into PowerShell env vars
   b. Wrote transient ~/.openclaw/.gateway-env (chmod 600) to WSL
   c. Restarted openclaw-gateway.service via systemd
   d. Slept 8 seconds
   e. DELETED ~/.openclaw/.gateway-env  ← THE PROBLEM

3. Gateway started successfully (EnvironmentFile loaded keys from .gateway-env before deletion).
   This works ONCE.

4. Later: WSL restarted again (e.g., all terminal sessions closed, or next PC wake)
   - systemd auto-starts openclaw-gateway.service (WantedBy=default.target, Restart=always)
   - .gateway-env NO LONGER EXISTS (was deleted in step 2e)
   - Gateway reads EnvironmentFile=-... (the - means "optional, ignore if missing")
   - ANTHROPIC_API_KEY not in environment → gateway exits with code 1
   - systemd retries every 5 seconds → crash-loops indefinitely (76+ restarts observed today)
`

### First crash event today: 20:59:07
`
Mar 16 20:59:07 - WSL restarted (new systemd PID 506)
Mar 16 20:59:10 - ANTHROPIC_API_KEY missing → crash
Mar 16 20:59:30 - restart counter 1 → crash
... crash-loops until manually fixed at ~21:14
`

### Manual fix applied (works until next WSL restart):
`powershell
# Wrote .gateway-env again from PowerShell env vars
# Restarted systemd service
# Confirmed "active" after 10 seconds
# Deleted .gateway-env
`

---

## ROOT CAUSE ANALYSIS

### Why the transient file approach fails on WSL restart:

The current design assumes:
> "startup script runs → writes .gateway-env → service starts → file deleted → done"

But systemd has Restart=always. Every time WSL restarts, systemd auto-starts the service.
The EnvironmentFile is marked optional (-) so it silently succeeds with missing keys,
then the gateway fails because auth-profiles.json uses SecretRef pointing to env vars.

This is NOT a bug in the transient-file design for the FIRST startup.
It IS a bug for any subsequent WSL restart without running the full startup script again.

### Structural conflict:
| Component | Behavior |
|-----------|----------|
| Restart=always + WantedBy=default.target | Service starts automatically on every WSL boot |
| .gateway-env | Transient — deleted 8 seconds after startup script runs |
| EnvironmentFile=-/.../.gateway-env | Optional — silently absent after first startup |
| uth-profiles.json → SecretRef env | Requires ANTHROPIC_API_KEY in process environment |
| Result | Any WSL restart after startup = crash loop |

---

## ALL POSSIBLE FIX APPROACHES (for PLAN to evaluate)

### Option A — Persistent EnvironmentFile (simplest fix)
Write API keys to ~/.openclaw/.gateway-env and DON'T delete it.
File is chmod 600, not committed to git.
No security regression vs current openclaw.json (which has the gateway auth token).
- Pros: 1 line change in startup script (remove the rm command). Works on every WSL restart.
- Cons: Keys on disk (encrypted by WSL user perms, but plaintext in the file).
- Risk: Low — file is 600, same risk level as ~/.openclaw/.env which already has TELEGRAM_BOT_TOKEN.

### Option B — systemd Service with Inline Environment= (medium complexity)
Add the keys directly to the [Service] section of api-keys.conf using systemd Environment= directives.
Done via startup script: write the conf file instead of .gateway-env.
`
[Service]
Environment="ANTHROPIC_API_KEY=sk-ant-..."
Environment="OPENAI_API_KEY=sk-..."
`
- Pros: Keys survive WSL restarts (conf file persists).
- Cons: Plaintext in systemd drop-in; startup script must re-write the conf on each rotation.
- Risk: Similar to Option A. File is under ~/.config/ (user-only access).

### Option C — WSL Startup Hook (correct architecture, complex)
Write a WSL boot script (~/.profile or systemd service) that fetches keys from Bitwarden
and writes .gateway-env before openclaw-gateway.service starts.
Requires: bws CLI available in WSL, BWS_ACCESS_TOKEN stored somewhere in WSL.
- Pros: Fully automatic — no manual intervention after PC restart.
- Cons: BWS_ACCESS_TOKEN must be stored in WSL (e.g., ~/.config/bws/token) — this is a secret on disk.
  Order-of-operations: bws service must run BEFORE openclaw-gateway service starts.
- Risk: Medium — introduces another secret on disk in WSL (the bws token).

### Option D — Remove Restart=always from systemd (avoid auto-restart)
Set Restart=on-failure or Restart=no so the service doesn't auto-restart.
Only start gateway via startup script (manual trigger).
- Pros: No crash loop. Gateway only starts when script runs.
- Cons: Gateway dead after any crash (OOM, transient error, etc.). Not resilient.
  If WSL restarts while user is away, Sparky is unreachable until manual restart.
- Risk: Availability risk — not recommended for always-on use case.

### Option E — OpenClaw Native Secret Provider (future / best practice)
Configure openclaw.json to use openclaw doctor --generate-gateway-token equivalent for API keys.
Use OpenClaw's built-in Bitwarden integration (if it exists in v2026.3.8/13).
- Pros: Fully managed by OpenClaw.
- Cons: Unknown if OpenClaw 2026.3.8 supports Bitwarden as a native secret provider.
  Requires research (Context7 query: "OpenClaw secrets provider Bitwarden").
- Risk: Unknown — needs investigation before committing.

### RECOMMENDATION FOR PLAN:
Option A (persistent .gateway-env, don't delete) is the fastest safe fix with lowest risk.
Option C (WSL boot hook) is the correct long-term architecture.
These can be combined: Option A for now, Option C as Phase 7 hardening.

---

## CURRENT STATE (as of 21:15)

| Item | Status |
|------|--------|
| Gateway process | RUNNING — manually recovered |
| Health endpoint :18792 | OK |
| Telegram (@Sparky4bot) | Connected |
| WhatsApp | NOT LINKED (separate issue — needs QR scan) |
| Next WSL restart | WILL CRASH AGAIN without fix |
| .gateway-env | Deleted (as designed) |
| NRestarts since recovery | 0 |

---

## KEY FILES AND LOCATIONS

| File | Path | Contents |
|------|------|---------|
| Service unit | ~/.config/systemd/user/openclaw-gateway.service | ExecStart, Restart=always, no API key env vars |
| Drop-in | ~/.config/systemd/user/openclaw-gateway.service.d/api-keys.conf | EnvironmentFile=-~/.openclaw/.gateway-env |
| Startup script | C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1 | Writes+deletes .gateway-env; rm command is the problem |
| auth-profiles | ~/.openclaw/agents/main/agent/auth-profiles.json | SecretRef → ANTHROPIC_API_KEY (env source) |
| .env | ~/.openclaw/.env | TELEGRAM_BOT_TOKEN, GOG_KEYRING_PASSWORD (95 bytes; no LLM keys) |

---

## WHAT PLAN NEEDS TO DECIDE

1. Choose fix option (A, B, C, or combination)
2. For Option A: specify security acceptance — keys in ~/.openclaw/.gateway-env (chmod 600, no-secrets-in-files.mdc exception)
3. For Option C: decide where BWS_ACCESS_TOKEN lives in WSL and what starts it
4. Update no-secrets-in-files.mdc if persisting .gateway-env becomes policy
5. Determine if WhatsApp re-link is also in scope for the same fix block

### Verdicts
- Root cause: CONFIRMED — transient .gateway-env + Restart=always = crash on WSL restart
- Fix applied today: TEMPORARY — will break on next WSL restart
- Priority: HIGH — Sparky goes unreachable after every WSL exit

### Blockers
None preventing fix — all options are implementable.

### Cross-Repo Impact
Changes will be in: start-cursor-with-secrets.ps1 (Windows) and/or openclaw-gateway.service.d/api-keys.conf (WSL).
Neither file is in any git repo (both are local-only). No git commits required for the fix itself.
STATE.md update in AI-Project-Manager should document the chosen approach.

### What's Next
PLAN: evaluate options A-E above, choose approach, write AGENT execution block.
AGENT: implement chosen fix, verify gateway survives a WSL restart (test: wsl --shutdown then reopen).

