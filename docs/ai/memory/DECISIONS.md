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
