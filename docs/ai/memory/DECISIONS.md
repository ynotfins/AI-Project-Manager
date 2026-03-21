# Decisions Log

Record key decisions with rationale. One entry per decision.

## Entries

<!-- Format:

## <Date> — <Decision Title>

**Context:** What prompted this decision
**Decision:** What was chosen
**Alternatives considered:** What else was evaluated
**Rationale:** Why this was selected
-->

## 2026-02-23 — Phase 5 Closure: bws run is the standard Cursor launch path

**Context:** Phase 5 required wiring GITHUB_PERSONAL_ACCESS_TOKEN, FIRECRAWL_API_KEY, and
TWENTY_FIRST_API_KEY into their respective MCP servers without storing secrets in mcp.json.

**Decision:** `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh start-cursor-with-secrets.ps1`
is the canonical and only supported way to launch Cursor on ChaosCentral. Cursor must not be
launched directly from taskbar/Start — always via the bws launch script.

**Alternatives considered:**
- Storing secrets directly in mcp.json (rejected: violates zero-trust policy)
- Using OS-level environment variables in .bashrc/.profile (rejected: persisted in plaintext on disk)
- Smithery hosted injection (rejected: Smithery HTTP 402 rate limit blocks reliability)

**Rationale:** bws run injects secrets only into the child process environment at runtime,
leaving no plaintext traces on disk or in version control. All 14 MCP servers receive their
credentials atomically at Cursor startup.

---

## 2026-02-23 — Phase 6 Decomposition: Split into 6A (architecture), 6B (gateway), 6C (integration)

**Context:** Phase 6 was originally a single monolithic goal ("Complete OpenClaw Build"). Upon
review, the prerequisite of `ANTHROPIC_API_KEY` injection is a human-only action (Bitwarden),
which blocks all Gateway-dependent work.

**Decision:** Phase 6 split into three sequential phases:
- 6A: Architecture Design (no external dependencies — can be done now)
- 6B: Gateway Boot (blocked on Tony: API key injection + secret rotation)
- 6C: First Live Integration (blocked on 6B)

**Alternatives considered:**
- Proceed with Gateway boot first (rejected: would fail without API key)
- Defer all Phase 6 work (rejected: architecture design has no blockers)

**Rationale:** Parallelizes work — architecture docs can be created and committed while Tony
completes Bitwarden actions in parallel. Reduces idle time.

---

## 2026-02-23 — open--claw Module Architecture: 8 Modules with Governance Overlay

**Context:** Phase 6A requires defining open--claw's module boundaries for safe autonomous
operation. Research from openclawlab.com official docs and community analyses (Bibek Poudel,
Raj Substack) confirmed OpenClaw's layered Gateway architecture.

**Decision:** 8 core modules defined:
Planner, Executor, Tool Router, Memory Engine, Code Generator, Deployment Engine, SEO Engine,
Finance Engine. AI-Project-Manager acts as the governance orchestrator; open--claw is the
executor. All High-risk actions require explicit human approval; Medium actions use notify +
30-min auto-approve timeout.

**Alternatives considered:**
- Fewer modules (4-5, merged domain engines): rejected for insufficient boundary clarity
- More modules (12+, split by tool): rejected as over-engineering for current scope

**Rationale:** 8 modules match OpenClaw's documented capability layers and align with the
three autonomy loops (App Builder, SEO Automation, Financial Management). Each module has a
clear risk level enabling precise governance gate placement.

---

## 2026-03-08 — Canonical runtime sources (Phase 6B.2)

**Context:** Governance audit identified that no rule declared official OpenClaw docs as the
canonical source for runtime/setup/hosting behavior. Local wrapper docs could drift without
a clear authority hierarchy. Additionally, the STATE template lacked HH:MM timestamps, making
same-day ordering ambiguous with 5+ blocks on a single date.

**Decision:**
- Official OpenClaw docs (https://docs.openclaw.ai/) and upstream repo
  (https://github.com/openclaw/openclaw) are canonical for runtime behavior, setup, hosting,
  and operator workflows.
- Local wrapper docs in `open--claw/open-claw/docs/` are subordinate and must not contradict
  official sources.
- AI-Project-Manager owns governance, workflow, and memory rules.
- HH:MM added to STATE template header for same-day ordering and cross-repo correlation.
- ClawHub skills: evaluate 5 candidates (gmail, gcal-pro, seo-optimizer, email-to-calendar,
  invoice-generator) during Phase 6C with mandatory code review before install (ClawHub
  security incident documented).
- Lobster: plan for Phase 7+ after first live integration proves stable.
- openclaw-studio: deferred indefinitely (community project; built-in Control UI is sufficient).
- Docker: deferred for local dev (official guidance confirms optional; plan for production later
  using official Hetzner/Oracle Cloud/Ansible guides).

**Alternatives considered:**
- Adopt cursor_chat20 15-section template (rejected: current 13 sections are sufficient per
  repo-truth audit)
- Install ClawHub skills now (rejected: no live integrations yet; security review required)
- Adopt Lobster now (rejected: early-stage, no workflows to run through it yet)
- Adopt openclaw-studio (rejected: overlaps with built-in Control UI, single maintainer)

**Rationale:** Minimum viable governance change. Official docs are comprehensive (2700+ pages)
and actively maintained. Establishing canonical-source hierarchy before Phase 6C prevents
wrapper drift during integration work. HH:MM is zero-cost prevention of ordering ambiguity.

---

## 2026-03-09 — Phase 6C.1 Pivot: weather skill as first integration test

**Context:** Phase 6C.1 attempted approval-gate + mem0-bridge activation but was BLOCKED:
skills are planning stubs only (not deployed to ~/openclaw-build/skills/), approval-gate
requires a paired messaging channel, and OpenMemory proxy is Windows-only. Meanwhile, 10/50
bundled skills are already `✓ ready` in the live runtime.

**Decision:** Pivot Phase 6C.1 to use the `weather` skill as the first integration test.
The `weather` skill exercises the full skill invocation pipeline (tool-calling, response
handling, audit logging) with zero credential requirements (uses public APIs: wttr.in,
Open-Meteo). Follow-up with `github` skill as second integration once weather passes.
Defer approval-gate and mem0-bridge until a messaging channel is configured and ClawHub
code review is completed.

**Alternatives considered:**
- healthcheck skill (considered: viable but is security-focused, less demonstrative of
  external API integration)
- github skill (considered: strong candidate, needs gh CLI auth verification; planned as
  second integration after weather)
- Unblock ClawHub install for approval-gate (rejected: requires code review per Phase 6B.2
  decision + messaging channel configuration — too many dependencies for first test)
- Build approval-gate from scratch (rejected: over-engineering; ready skills already exist)

**Rationale:** Lowest-risk path to prove the integration pipeline works end-to-end. Zero
credentials, non-destructive, exercises real external API. Validates tool-calling, response
formatting, and audit logging before moving to higher-risk integrations.

---

## 2026-03-09 — Gateway port correction: 18789 (UI) / 18792 (API)

**Context:** Previous STATE entries and patterns referenced port 3000 for gateway health
checks. Session bootstrap verification discovered the gateway actually listens on port 18789
(Control UI) and port 18792 (API health, returns `OK`).

**Decision:** All future references to gateway health/UI should use ports 18789 and 18792.
Port 3000 is incorrect and should not be used in commands or documentation.

**Alternatives considered:** None — this is a factual correction.

**Rationale:** Prevents false-negative health checks in future session bootstraps.

---

### 2026-03-09: ClawHub batch install of 12 skills approved

**Context:** Previous DECISIONS.md entry (2026-03-08) required "mandatory code review before ClawHub install" with a 5-candidate gate. User explicitly requested installing 12 specific skills in this session.

**Decision:** User approved batch install of 12 ClawHub skills, superseding the cautious 5-candidate code-review gate. Metadata inspection via `npx clawhub inspect` applied as a trust-but-verify measure for each skill before install. Two skills (proactive-agent-skill, api-gateway-zito) were flagged as suspicious by ClawHub; installed with `--force` per user approval.

**Skills installed:** self-improving-agent, proactive-agent-skill, openai-whisper, api-gateway-zito, humanize-ai-text, youtube-watcher, gmail, imap-smtp-email, whatsapp-business, web-search-exa, playwright-mcp, superdesign.

**Alternatives considered:** Blocking flagged skills — rejected because user explicitly approved all 12 and the metadata inspection showed legitimate content from known owners.

**Rationale:** Moving from cautious evaluation to operational usage. The gateway rollback mechanism (`npx clawhub uninstall` + restart) provides sufficient safety net.

---

### 2026-03-09: SOP documentation hardening

**Context:** After completing Phase 0 bootstrap and confirming stable operational facts (ports, paths, commands), the team decided to capture these as permanent reference documents.

**Decision:** Created three SOP documents:
1. `open--claw/docs/ai/operations/RUNTIME_REFERENCE.md` — gateway, WSL, node/pnpm, systemd, secrets
2. `open--claw/docs/ai/operations/SKILL_MANAGEMENT.md` — bundled/ClawHub skill lifecycle, credential mapping
3. `AI-Project-Manager/docs/ai/operations/SESSION_BOOTSTRAP_SOP.md` — 7-step bootstrap procedure with evidence requirements

**Rationale:** Hardening known-stable facts into permanent docs prevents re-discovery costs in future sessions and provides onboarding material for new agents.

---

### 2026-03-10: Removed Maton-dependent ClawHub skills (gmail, whatsapp-business) — security risk

**Context:** The `gmail` and `whatsapp-business` ClawHub skills (author: byungkyu) route ALL API traffic through `gateway.maton.ai`, a third-party service. Users must provide a `MATON_API_KEY`, after which Maton holds OAuth tokens for Gmail and WhatsApp Business and acts as a man-in-the-middle for all API calls. This is a credential-proxying pattern — Maton can read all emails and messages.

**Decision:** Uninstall both skills immediately. Use OpenClaw's built-in WhatsApp channel via Baileys (direct peer-to-peer connection, no third-party proxy). For Gmail, use the bundled `gog` skill (Google Workspace CLI) or direct Google API integration instead.

**Alternatives considered:**
- Keep skills but avoid providing the Maton key (rejected: skills are non-functional without it)
- Use Maton with a throwaway account (rejected: defeats purpose and normalizes the pattern)

**Rationale:** Any skill that requires routing credentials through a third-party proxy service should be treated as a security risk. The Maton gateway pattern is indistinguishable from credential-harvesting malware. OpenClaw provides native, direct-connection alternatives for both WhatsApp and Gmail.

**Action items:**
- Delete `MATON_API_KEY` from Bitwarden Secrets Manager (user action)
- Set up built-in WhatsApp channel: `pnpm openclaw configure --section channels` (user action, QR scan required)

---

### 2026-03-10: Vendor pin: v2026.3.8 shallow clone

**Context:** The `open--claw/vendor/openclaw/` shallow clone was pinned to an untagged commit (b228c06, 2026-02-18), ~3 weeks behind the latest stable release. The WSL build copy at `~/openclaw-build/` was at version 2026.2.18. The upstream repo had published v2026.3.2, v2026.3.7, and v2026.3.8 since our clone was created.

**Decision:** Replace both the Windows NTFS vendor clone and the WSL runtime build copy with fresh shallow clones (`--depth=1`) at the tagged release `v2026.3.8` (SHA 3caab92). Create `open--claw/VENDOR_PIN.md` as a tracked file documenting the exact pin state, clone command, and upgrade/rollback procedures.

**Alternatives considered:**
- Full clone with history (rejected: adds ~500MB+ of history we don't need; shallow at tagged release is deterministic and lightweight)
- Sparse checkout of only needed paths (rejected: we need the full tree for Android app, shared kit, skills, extensions, and gateway source)
- Git fetch + checkout to update in-place (rejected: shallow clone cannot reliably fetch arbitrary tags; fresh clone is cleaner)

**Rationale:** Pinning to a tagged release provides a deterministic, reproducible vendor state. The VENDOR_PIN.md file formalizes the upgrade procedure, preventing ad-hoc untracked drift. v2026.3.8 is the latest stable and includes security fixes. Skills count was preserved (19/58 → 19/59, gained 1 upstream skill).

---

### 2026-03-11: Replace Node.js node host with Molty (OpenClaw Windows Hub) v0.4.5

**Context:** The Windows node host was running as a foreground Node.js process (`node openclaw.mjs node run`) from the vendor clone. This required a terminal to stay open, had limited capabilities (browser, system.run, system.which), and disconnected when the terminal closed. The upstream ecosystem includes `shanselman/openclaw-windows-hub` (Molty), a .NET WinUI system tray companion with richer capabilities and persistent operation.

**Decision:** Install Molty v0.4.5 from pre-built GitHub release (`OpenClawTray-Setup-x64.exe`). Stop the Node.js node host. Configure Molty with gateway token and Node Mode. Add `gateway.nodes.allowCommands` (13 commands) to WSL gateway config.

**Alternatives considered:**
- Continue with Node.js node host (rejected: foreground-only, limited capabilities, terminal-bound)
- Build Molty from source (rejected: requires .NET 10 Preview SDK; pre-built release avoids SDK dependency)
- Use portable ZIP instead of installer (rejected: installer provides auto-start registration and Start Menu shortcut)

**Rationale:** Molty provides persistent system tray operation (survives terminal close), richer capabilities (canvas/WebView2, screen capture, camera, toast notifications), auto-start with Windows, embedded web chat, and PowerToys integration. The pre-built release from a reputable author (Scott Hanselman) avoids SDK dependencies entirely.

---

### 2026-03-14: Approval gate mechanism is exec-approvals.json + sandbox mode (not exec-policy.json)

**Context:** Phase 6C approval gate test revealed that `exec-policy.json` (Windows/Molty) is irrelevant after Molty removal. Two additional requirements were discovered: (1) `~/.openclaw/exec-approvals.json` must have a `defaults.security` policy set (not empty `{}`), and (2) the agent's `sandbox.mode` must be enabled in `openclaw.json` — without sandbox, exec-approvals.json is never consulted.

**Decision:** The canonical approval gate for the Linux/WSL gateway is:
- `~/.openclaw/exec-approvals.json` with `defaults.security: "deny"` and `agents.main.ask: "always"`
- `agents.defaults.sandbox.mode: "all"` in `~/.openclaw/openclaw.json`

exec-policy.json (Windows/Molty) is dead config and no longer applies.

**Alternatives considered:**
- Using exec-policy.json deny rules (rejected: Molty removed, no Windows node host)
- Using exec-approvals.json without sandbox (rejected: approvals not evaluated without sandbox active)
- Using `security: "allowlist"` without `ask: "always"` (rejected: would silently deny on-miss without surfacing approvals)

**Rationale:** The OpenClaw docs explicitly state exec-approvals are a "companion app / node host guardrail" for sandboxed agents. The sandbox intercepts exec calls and routes them through the approvals policy. Without sandbox, the `exec` tool runs in the gateway process context directly, bypassing approvals entirely. Enabling `sandbox.mode: "all"` activates isolation and approval evaluation for all agents.

---

### 2026-03-16: Phase 7.1 — exec-policy.json target policy set; Molty pairing blocked by WinUI3 crash

**Context:** Phase 7.1 attempted to re-pair Molty with full system access. BLOCK 2 completed successfully (exec-policy.json updated), but BLOCK 3+ blocked by a fatal Molty crash (`XamlParseException` on every launch since 2026-03-13).

**Decision:**
- `exec-policy.json defaultAction: "allow"` is the correct target policy for Phase 7.1. Pre-configured and saved. Minimal deny safety floor kept: Format-*, Stop-Computer, Restart-Computer, shutdown, reg delete.
- `gateway.nodes: {}` (no `allowCommands`) in WSL `openclaw.json` is the correct configuration for full Windows node access — no changes needed.
- Molty repair (MSIX reinstall) is the prerequisite before pairing can proceed.
- Security boundary for Windows node: exec-policy.json on Windows side handles command-level allow/deny. WSL-side exec-approvals.json (sandbox=off, currently unenforced) handles agent-level approval prompts separately.

**Alternatives considered:**
- Using headless openclaw node host instead of Molty (deferred: Molty provides richer capabilities — canvas, screen, camera, DroidRun MCP bridge)
- Skipping node host entirely (rejected: Windows file access and DroidRun MCP bridging require a node host)

**Rationale:** exec-policy.json as `allow` with targeted denies gives Sparky full PowerShell access while keeping the most destructive operations blocked at the policy level. The WSL exec-approvals layer (once sandbox is enabled via Docker) adds a second approval gate on top.

---

## Decision: Persist .gateway-env on disk (do not delete after startup)

**Date:** 2026-03-16  
**Status:** IMPLEMENTED

### Context
systemd Restart=always + transient .gateway-env = crash loop on every WSL restart.  
The startup script wrote ~/.openclaw/.gateway-env, started the service, waited 8 seconds, then deleted it.  
When WSL later restarted (all terminals closed, PC sleep/wake, etc.), systemd auto-started the gateway but .gateway-env was gone. ANTHROPIC_API_KEY missing → exit code 1 → crash-loop (76+ restarts observed 2026-03-16).

### Decision
Remove the m -f ~/.openclaw/.gateway-env line from start-cursor-with-secrets.ps1.  
Keep .gateway-env on disk at ~/.openclaw/.gateway-env (chmod 600, not in git).  
File is overwritten on every Cursor startup script run, so keys stay current.

### Alternatives Rejected
| Option | Why Rejected |
|--------|-------------|
| Option B — systemd Environment= in drop-in | Same security profile, more complex (conf file must be regenerated on rotation), no advantage over A |
| Option C — WSL boot hook fetches from Bitwarden | Correct long-term architecture but 30+ min to implement; introduces ws access token in WSL as a persistent secret |
| Option D — Remove Restart=always | Availability risk: Sparky unreachable after any crash without manual restart |
| Option E — OpenClaw native Bitwarden provider | Unknown support in v2026.3.8; needs research before committing |

### Security Rationale
.gateway-env is chmod 600 (owner-read-only).  
This is the same risk profile as ~/.openclaw/.env, which already persists TELEGRAM_BOT_TOKEN on disk.  
File is in .gitignore. Not committed to any repo. No external exposure.  
Approved exception to 
o-secrets-in-files.mdc — see that rule's "Allowed Exceptions" section.

### Consequences
- Gateway survives WSL restarts without manual intervention
- Sparky remains reachable on Telegram after any WSL exit/restart
- Keys are refreshed automatically every time the startup script runs (overwrite, not append)
- Future: Option C (WSL boot hook) remains valid as Phase 7 hardening if needed

### Test Evidence
- wsl --shutdown + 15s wait → gateway ctive (running) immediately
- .gateway-env present with chmod 600 after restart
- pnpm openclaw health → Telegram: ok (@Sparky4bot)
- NRestarts: 0

---

## Decision: Plugin allowlist established (plugins.allow)

**Date:** 2026-03-16  
**Status:** IMPLEMENTED

### Context
OpenClaw was starting with a warning: "plugins.allow is empty; discovered non-bundled plugins may auto-load". Without an explicit allowlist, any plugin in the extensions directory could load automatically.

### Decision
Set plugins.allow = ["whatsapp", "telegram", "lossless-claw"] in openclaw.json.

### Policy
- Update allowlist when adding new plugins (add entry before or during install)
- Review allowlist on OpenClaw version upgrades
- Source: OpenClaw security docs recommend explicit plugins.allow allowlists

### Consequences
- Warning eliminated from startup logs
- No unintended plugins can auto-load
- Future plugin additions require explicit allowlist update

---

## Decision: Personal use classification

**Date:** 2026-03-16  
**Status:** DOCUMENTED

### Context
PLAN and AGENT were generating release docs with enterprise/commercial framing. This system is personal.

### Classification
- **Users:** Tony, Kristina, Mia (family) + friends (free access)
- **"Employee" = friends using for free** — no employment relationship
- **NEVER commercial, NEVER for sale**
- **Regular WhatsApp (not WhatsApp Business)** — correct for personal family use; Baileys is appropriate
- **No Google Play / App Store distribution** planned
- **Rate limiting** = over-engineering for LAN-only personal system at this user scale
- **Privacy Policy / Terms of Service** in release checklist = internal family guidelines, not legal compliance

### Consequences
- Release docs should reflect internal/personal framing, not enterprise
- No legal counsel needed for current scope
- WhatsApp Business API not needed — regular Baileys connection is correct

---

## Decision: Dynamic WSL IP in allowedOrigins — pending enhancement

**Date:** 2026-03-16  
**Status:** PARTIAL — current IP added manually; auto-update pending

### Context
WSL IP (172.23.156.209) changes on WSL restart, making a statically configured gateway.controlUi.allowedOrigins fragile. Each WSL restart can change the IP, breaking any allowedOrigins-dependent logic.

### Current Fix
Manually added current IP to allowedOrigins array. Will need updating after WSL restart.

### Future Enhancement
Extend start-cursor-with-secrets.ps1 to auto-update openclaw.json's llowedOrigins with the new WSL IP on each startup run. The script already reads hostname -I for the node host — similar logic can patch the JSON.

### Note on Control UI Windows Access
The Control UI still rejects Windows browser connections with code=1008 "control ui requires device identity (use HTTPS or localhost secure context)". This is a separate Control UI security feature — it requires HTTPS for non-localhost WebSocket origins regardless of allowedOrigins. A solution requires either: (a) SSH tunnel from Windows to localhost, or (b) HTTPS reverse proxy. Not a blocker for Telegram/WhatsApp operation.

---

## Decision: gateway.nodes.autoApprove — Not Available in OpenClaw v2026.3.8 (ATTEMPTED, FAILED)

**Date:** 2026-03-17  
**Status:** FAILED — key not recognized in v2026.3.8

### Attempted
Added gateway.nodes.autoApprove = {local: True} to openclaw.json to auto-approve Windows node connections from the local host.

### Result
OpenClaw v2026.3.8 schema validator rejected the key:
`
Invalid config: gateway.nodes: Unrecognized key: "autoApprove"
`
Backup restored immediately. Gateway healthy.

### Pending
- Check v2026.3.13 changelog for the correct key name
- Consider upgrading OpenClaw vendor if autoApprove exists in newer version
- Alternative: evaluate if Windows node host is necessary given droidrun MCP already covers phone control

---

## Decision: Two-gate model for Windows node execution (2026-03-17)

**Date:** 2026-03-17  
**Status:** Gate 1 (pairing) DONE; Gate 2 (execution) PARTIAL — `nodes run` blocked by WSL-embedded node issue

### Context
ChaosCentral was connected (gate 1: device pairing — `paired · connected` in `nodes status`) but Sparky could not run commands (gate 2: execution approvals). These are separate security layers in OpenClaw.

### Decision
Set `tools.exec.host=node`, `tools.exec.security=allowlist`, `tools.exec.node=ChaosCentral` in `openclaw.json` via `openclaw config set`. Added wildcard `*` glob pattern to `exec-approvals.json` for ChaosCentral node ID (`847202f0...bea4e`) for all agents.

### Source
OpenClaw docs — device pairing determines whether a node is authorized to connect; execution approvals govern whether a node is permitted to run specific shell commands.

### Security
Acceptable for personal home system. `allowlist` mode with `*` glob is permissive but scoped to ChaosCentral node only. Can be narrowed to specific glob patterns later.

### Outcome / Consequences
Config applied successfully. However, `nodes run` fails with `invalid system.run.prepare response` because:
- `nodes status` shows "ChaosCentral" as connected, but this is the **WSL-embedded node** running inside the gateway's own process (v2026.3.13), not the actual Windows node.cmd host
- The Windows node.cmd STILL cannot connect to the gateway over plaintext `ws://` (SECURITY ERROR)
- The embedded WSL node does not support `system.run` as it is not a real remote execution host

### Root Cause
The Windows node.cmd uses the WSL gateway's LAN IP (`172.23.156.209:18789`) which is non-loopback → plaintext WebSocket rejected by OpenClaw security policy. Requires either:
- `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` env var in node.cmd (break-glass for trusted private networks — explicitly documented in OpenClaw error message)
- SSH tunnel (`ssh -N -L 18789:127.0.0.1:18789`) so Windows node connects to 127.0.0.1

### Recommended Next Fix
Add `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` to `C:\Users\ynotf\.openclaw\node.cmd` as the first environment variable, then restart the Windows node service. This is the lowest-friction resolution and is scoped to private/trusted networks per OpenClaw's own documentation.

---

## Decision: Windows node full resolution — OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1 + exec-approvals (2026-03-17)

**Date:** 2026-03-17  
**Status:** RESOLVED — PowerShell execution verified

### Context
Windows node.cmd rejected with `SECURITY ERROR: Cannot connect over plaintext ws://` despite being on a trusted private LAN (WSL↔Windows local bridge, 172.23.144.1). `exec-approvals.json` defaults were empty, causing approval socket timeout on all commands via the `nodes run` CLI path.

### Decisions Made
1. **Added `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` to `node.cmd`** — OpenClaw's documented break-glass flag for trusted private networks. The node.cmd connects to the WSL gateway over the Windows/WSL local bridge IP (172.23.144.1), which is not a public network. This flag is acceptable for a personal home system.

2. **Set `exec-approvals.json` defaults to `security=full, ask=off, askFallback=allow`** — `ask=off` disables the approval socket request path entirely; `askFallback=allow` ensures commands proceed even if the approval socket is unreachable. This bypasses the CLI `nodes run` hang issue while allowing the agent's invoke path to work.

3. **Added wildcard `*` to allowlist for all agents on Windows Desktop node** — permits all command patterns without per-pattern approval prompts.

### Durability
- `node.cmd`: local Windows file at `C:\Users\ynotf\.openclaw\node.cmd`. Not in git. Survives reboots.
- `exec-approvals.json`: local WSL file at `~/.openclaw/exec-approvals.json`. Not in git. Survives WSL restarts.
- WSL IP in `node.cmd` is auto-updated by `start-cursor-with-secrets.ps1` on each startup launch.

### Verification
- `nodes status`: Known:2 Paired:2 Connected:2 — ChaosCentral (WSL-embedded) + Windows Desktop (node.cmd, IP 172.23.144.1)
- `nodes invoke system.run hostname` → `ChaosCentral`
- `nodes invoke system.run powershell.exe Get-Date` → `Tuesday, March 17, 2026 5:08:20 PM`

### Known Limitation
`nodes run` CLI command hangs when approval socket communication fails between WSL and Windows processes. This is a CLI-only issue — the agent's `nodes()` tool uses the invoke path which bypasses the approval socket and works correctly. No action needed.

### Security Assessment
Acceptable for personal home system. `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` is scoped to the Windows/WSL local bridge — not exposed to public internet. `exec-approvals` allows all commands on Windows Desktop, which is the user's own machine. For future production use, tighten to specific glob patterns.

---

## Decision: Sparky full autonomous access — sudo + Windows admin + exec-approvals full (2026-03-18)

**Date:** 2026-03-18  
**Status:** IMPLEMENTED — all verified

### Context
Multiple security gates were blocking Sparky from running commands autonomously:
1. `openclaw.json`: `sandbox.mode="all"` and `tools.exec.host="sandbox"` — routing to non-functional sandbox path
2. `exec-approvals.json`: `defaults.security=deny` + `agents.main` had empty allowlist with `ask=always`
3. WSL: `sudo` required a password (blocking root-level operations)

### Decisions Made

**1. sandbox.mode stays "off" by design**
Sparky needs direct host access (WSL filesystem, Windows node, Docker daemon) for autonomous work. Docker sandbox containers (openclaw-sandbox:bookworm-slim) are for future CrewClaw employee containers only. Setting sandbox=off gives Sparky unrestricted access to the host environment — intentional for personal use.

**2. tools.exec.host=node, security=full**
Routes all command execution through the Windows Desktop node host (direct, no approval checks). `security=full` means the node runs any command without filtering.

**3. exec-approvals: security=full, ask=off, askFallback=allow, autoAllowSkills=true**
Applied to both `defaults` and `agents.main`:
- `ask=off`: disables the approval socket request path entirely
- `askFallback=allow`: fallback if approval socket unreachable → allow (not block)
- `autoAllowSkills=true`: skills auto-allowed without explicit approval
- Net effect: zero approval prompts for any command

**4. WSL passwordless sudo**
Created `/etc/sudoers.d/ynotf-nopasswd` with `ynotf ALL=(ALL) NOPASSWD: ALL`. Validated with `visudo -cf`. Allows Sparky to run `sudo` commands in WSL without any password prompt — required for system administration tasks (package installs, service management, file ownership changes, etc.).

**5. Windows Administrator (pre-existing)**
`ynotf` was already a member of the Administrators group — no change needed. Confirmed with `Get-LocalGroupMember`.

### Security Assessment
Acceptable for personal home system. ChaosCentral is a private PC with no public internet exposure. Risk is contained to:
- Sparky running arbitrary commands on the local machine (intentional — this is the design goal)
- No remote access path beyond WhatsApp/Telegram channels which are already owner-ID locked

---

## Decision: Docker v29.1.3 discovered installed — BLOCKER 1 resolved (2026-03-18)

**Date:** 2026-03-18  
**Status:** RESOLVED — Docker available, sandbox kept off by design

### Context
BLOCKER 1 was documented as "Docker not installed in WSL — sandbox mode causes gateway crash-loop." This was incorrect. Docker v29.1.3 + Docker Compose v2.40.3 ARE installed and the daemon is running. The `openclaw-sandbox:bookworm-slim` container was already active with 7h+ uptime.

### Decision
Keep `sandbox.mode=off` even though Docker is now confirmed available. Rationale:
- Sparky needs direct host access, not sandboxed containers
- Docker sandbox is reserved for future CrewClaw employee containers
- Changing to sandbox=on would re-introduce approval gate overhead that blocks autonomous operation

### Impact
BLOCKER 1 is resolved (Docker exists). STATE.md updated accordingly.

---

## Decision: Canonical OpenClaw gateway restart + build tag alignment (2026-03-21)

**Context:** Operational drift between OpenClaw CLI checkout and systemd gateway runtime; inconsistent secret injection when restarting from non-injected shells.

**Decision:** Use `AI-Project-Manager/scripts/restart-openclaw-gateway.ps1` as the only supported automation path for `.gateway-env` write + `systemctl --user restart openclaw-gateway`. Keep `~/openclaw-build` on `v2026.3.13-1` with systemd `dist/index.js` entrypoint.

**Alternatives considered:** Rely on npm global only (rejected: doctor/source-of-truth wanted explicit build tree); `openclaw doctor --repair` auto-migrate (deferred: manual alignment chosen for evidence).

**Rationale:** Fail-fast on missing keys prevents silent blank `.gateway-env`; aligned versions remove config warning noise.

**Full detail:** See repo root `docs/ai/DECISIONS.md` entry of same date.
