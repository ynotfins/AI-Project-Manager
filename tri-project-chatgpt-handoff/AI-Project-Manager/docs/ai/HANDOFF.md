# Agent Handoff — AI-Project-Manager

**Date**: 2026-04-13
**Status**: Current handoff — recovery bundle materialized and proven alive across a later normal execution; Obsidian sidecar catch-up now falls back to a pending summary in `docs/ai/recovery/session-summary.md`
**Crash-recovery path**: OpenMemory + `docs/ai/recovery/*` first, then `docs/ai/STATE.md` if needed

Previous handoff snapshot: `docs/ai/archive/handoff-2026-03-08.md`.

---

## 1. What This Repo Governs

`AI-Project-Manager` is the governance/orchestration repo for the AI Operating System stack:

- `AI-Project-Manager` (governance, workflow, memory, release and tooling docs)
- `open--claw` (agent runtime and execution)
- `droidrun` (mobile runtime control)

Application runtime code is not hosted here; this repo defines operating policy, evidence standards, and phase tracking.

---

## 2. Current Operational Truth

### Phase state (governance side)

- 0 through 6B: COMPLETE
- 6C — First Live Integration: COMPLETE (2026-03-14)
- Phase 1A — CrewClaw Worker Stabilization: COMPLETE (2026-03-29)
- Post-6C hardening and operations: ACTIVE

### Runtime highlights (verified 2026-03-29)

- OpenClaw CLI + systemd runtime aligned on `~/openclaw-build` tag `v2026.3.13-1`. Systemd `ExecStart` uses `openclaw-build/dist/index.js`.
- **Telegram**: healthy, running.
- **WhatsApp**: 401 Unauthorized — QR re-scan required (`pnpm openclaw channels login --channel whatsapp` in WSL).
- **Signal**: disabled by design.
- Windows Desktop node is connected again and now uses the stable loopback path (`127.0.0.1:18789`) plus a `pwsh` watchdog launcher. Cursor CLI paths are visible from that node, and user-level autostart is installed via both `HKCU\...\Run` and the Startup folder so Sparky keeps Windows access across logons/reboots.
- CrewClaw: 10 Telegram workers are now running from the shared deployment. The original 5 plus `personal-crm`, `script-builder`, `seo-specialist`, `software-engineer`, and `ux-designer` all have Bitwarden-backed Telegram bot tokens and live containers. The original 5 still route to host `main`; the newer 5 route to their own agent IDs.
- CrewClaw workers are active and paired, and the gateway is open. Live model order is now `openai/gpt-5.4` primary, `openrouter/x-ai/grok-4` fallback, `anthropic/claude-opus-4-6` fallback. Direct `main` replies and representative worker-routed replies both succeeded on 2026-03-29. The canonical gateway restart path is now xAI-aware, but direct `xai/*` fallback is still inactive because no `XAI_API_KEY` secret is exposed through the active Bitwarden project/injected env.
- CrewClaw dashboard monitoring now uses an approved narrow exception: per-worker local `.env` files may store `CREWCLAW_MONITOR_KEY` for `heartbeat.sh` only. This replaces the earlier assumption that monitor keys had to be Bitwarden-native. Portal activation is still per worker, but runtime prep and deployment can now be done in batches.
- A new curated source of truth now exists at `open--claw/open-claw/AI_Employee_knowledgebase`: 15 repo-tracked employee packets, zipped portable bundles, copied high-value reference assets, and 10 new development skills. This library is now a better future packaging base than the raw downloaded CrewClaw ZIPs.
- Context pressure mitigation active via lossless-claw context engine.

### Current Worker Routing (temporary workaround — Phase 1B item)

CrewClaw bots currently route all messages to `--agent main` because per-employee agent IDs require `setup.sh` to register them at build time, which is not run in the Docker build context. This is a known gap, not a permanent design. Resolving it is part of Phase 1B scope.

### Startup baseline

```powershell
bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
```

This wrapper is mandatory. If Cursor is relaunched outside it, Sparky may lose env-backed permissions and MCP auth.

### Canonical gateway restart (no ad-hoc CLI)

- Prefer the launcher above (it calls `AI-Project-Manager\scripts\restart-openclaw-gateway.ps1` after Cursor starts).
- Manual: from an injected shell, `pwsh -File D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1`
- See `docs/ai/operations/openclaw-gateway-restart.md`.

---

## 3. Recent Unresolved Issues

Issues that survived the last task block and remain relevant to future planning. Updated by AGENT after each block where turbulence remains open.

| Issue | Severity | Status | Context |
| --- | --- | --- | --- |
| WhatsApp 401 — session expired | MEDIUM | PENDING USER ACTION | Run `channels login --channel whatsapp` in WSL and scan QR |
| Direct xAI provider key missing from active Bitwarden path | MEDIUM | PENDING USER ACTION | Repo restart path now supports `XAI_API_KEY`, but the active Bitwarden project/injected env still does not expose any xAI/Grok secret, so desired direct `xai/*` fallback cannot be enabled yet |
| CrewClaw portal activation is still per-worker UI work | LOW | EXPECTED OPERATION | Runtime prep is now batched, but CrewClaw `Add Agent` / first-ping confirmation still happens per employee unless CrewClaw adds bulk tooling |
| CrewClaw ZIP packaging defect | HIGH | ACTIVE BLOCKER | All audited CrewClaw ZIPs currently ship with `Dockerfile` lines that `COPY bot.js`, but the packages contain `bot-telegram.js`, requiring manual repair before clean deploys |
| Most named CrewClaw employees are still generic templates | HIGH | ACTIVE BLOCKER | 9 of the 10 named worker packages are structurally complete but role-thin; their docs and skills do not yet justify their labels for autonomous website work |
| Five generic CrewClaw downloads are identical template clones | MEDIUM | ACTIVE BLOCKER | The `generic/crewclaw-agent-deploy (12-16).zip` files are the same `My Agent` template, not five distinct specialists |
| Curated standard not yet synced into deployed CrewClaw workers | HIGH | ACTIVE BLOCKER | `open--claw/open-claw/AI_Employee_knowledgebase` now contains the stronger 15-person standard, but the live deployed workers still use the older downloaded employee definitions |
| OpenMemory outage caused missed memory capture during `504 Gateway Time-out` incident | MEDIUM | RESOLVED SERVICE / RESEED IN PROGRESS | official `npx openmemory` stdio transport is now active again, but missed memories from the outage window still need reseeding |
| Direct upstream OpenMemory `/health` remains noisy | LOW | MONITOR | the standalone hosted health endpoint can still return `504`, but the actual MCP server now initializes and Cursor regenerated `user-openmemory/tools/` |
| Older bootstrap-summary OpenMemory entry still appears in search results | LOW | MONITOR | Fresh recovery succeeded, but one older low-relevance memory still surfaced with stale pre-bundle wording; it did not block recovery because newer entries plus the bundle were sufficient |
| Obsidian sidecar summary pending flush | LOW | ACTIVE FOLLOW-UP | New fallback rule prevents blocking on `obsidian-vault` failure: the pending sidecar payload now lives in `docs/ai/recovery/session-summary.md` with `obsidian_sync: pending` and should be flushed to `AI-PM/Recovery Sidecar/No-Loss Recovery Catch-Up.md` on the next successful Obsidian availability |
| Untouched docs may still contain stale no-loss guidance | MEDIUM | ACTIVE FOLLOW-UP | The targeted authority files are aligned, but a broader drift sweep across non-targeted docs is still pending |

---

## 4. Standing Constraints

Structural limits that affect all planning. Not resolvable in a single task block.

- **Windows node connectivity**: primary reconnect path is now automated through the `pwsh` watchdog and loopback host. Residual risk is limited to user-level autostart being blocked by local shell/profile changes; the old WSL-IP + `cmd.exe` path is no longer the intended runtime.
- **Bitwarden dependency**: all secret injection requires `bws` CLI and vault access. Any automated deploy is blocked without it.
- **WhatsApp QR re-scan**: cannot be automated — requires physical phone access. Recurs after each gateway restart cycle if session expires.
- **CrewClaw device pairing**: first-run one-time approval per named Docker volume lifetime. Named volumes persist identity across container rebuilds.

---

## 5. Current Focus

1. Continue LosslessClaw-style continuity with OpenMemory-first session recovery plus rolling repo docs and ledgers.
2. Maintain stable autonomous runtime (gateway/node/startup resiliency) and require wrapper-based launch integrity.
3. Keep Serena normalized across `AI-Project-Manager`, `open--claw`, `open-claw-runtime`, and `droidrun`.
4. Use the curated employee standard in `open--claw/open-claw/AI_Employee_knowledgebase` as the baseline for future squads.
5. Keep documentation, tooling records, screenshot evidence, and memory summaries synchronized across governance and execution repos.
6. Turn the curated OpenClaw employee library into a live-ready managed squad led by Sparky.
7. Build the worker-facing memory-promotion path so OpenClaw specialists can retain validated knowledge without bloating chat context.
8. Use generated readiness artifacts so curated worker activation is evidence-driven instead of all-or-nothing.

---

## 6. Read Order For New Sessions

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. `AGENTS.md`
3. `.cursor/rules/05-global-mcp-usage.md`
4. `.cursor/rules/10-project-workflow.md`
5. `docs/ai/memory/MEMORY_CONTRACT.md`
6. `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`
7. `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
8. Targeted OpenMemory search
9. Recovery bundle if present/current
10. `docs/ai/STATE.md` summary/current state section
11. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md`

Use archived docs only for historical evidence, not operational truth.

---

## 7. Durable Operator Behaviors (installed 2026-03-31)

### AGENT Execution Ledger

A non-canonical verbatim execution log is now active at `docs/ai/context/AGENT_EXECUTION_LEDGER.md`.

**Operator rules:**
- AGENT must append one entry after every completed prompt block (exact prompt + exact response + files changed + verdict). This is mandatory, as required as the STATE.md update.
- PLAN and DEBUG must NOT load this ledger by default or include it in bootstrap reads.
- PLAN/DEBUG may consult it only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed, one block at a time.
- **Ledger archival is now hook-enforced and automatic.** `.cursor/hooks.json` registers an `afterFileEdit` hook that runs `.cursor/hooks/rotate_ledger.py` after every AI edit to the ledger file. The hook moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md` when the active ledger exceeds 5 entries or ~300 lines. AGENT does NOT manage archival manually.
- If the hook fails or is unavailable: AGENT must archive manually before the next non-trivial block.
- Archived files are non-canonical and historical only.
- This ledger does not replace STATE.md — both must be maintained independently.

### Serena project activation

Serena is now normalized as exact-path, repo-local project activation:

- `D:/github/AI-Project-Manager` — workflow/process layer repo
- `D:/github/open--claw/open-claw` — OpenClaw runtime code project
- `D:/github/droidrun` — DroidRun code project

Do not rely on dashboard names when switching repos. `D:/github/open--claw` repo root is docs/governance heavy and is not the default Serena code project. For docs-only areas or unsupported roots, record Serena FAIL and fall back to targeted search/read tools.

### MCP configuration

All 10 active MCP servers live in the single global config at `C:/Users/ynotf/.cursor/mcp.json`:

Context7, thinking-patterns, openmemory, github, serena, Exa Search, firecrawl-mcp, playwright, Magic MCP, droidrun, context-matic, filesystem, obsidian-vault.

No workspace-local `.cursor/mcp.json` files. The earlier split caused duplicate tool loading in multi-root workspaces.

Removed from toolchain: `sequential-thinking`, `shell-mcp`, GitKraken MCP, `googlesheets-tvi8pq-94`, `firestore-mcp`.

### No-Loss memory system

Architecture defined in `docs/ai/architecture/NO_LOSS.md`. Key points:

- OpenMemory is the primary durable structured recall backbone
- The live Cursor surface is flat: `search-memories(query)`, `list-memories()`, `add-memory(content)`
- Recovery now uses the authority contract first, then OpenMemory, then the filesystem recovery bundle, then `STATE.md`
- The recovery bundle is non-canonical and exists only to reduce reread thrash after restart
- The execution ledger stays one-block fallback only and is never default preload
- Worker memory flow is defined in `docs/ai/architecture/OPENCLAW_WORKER_MEMORY_FLOW.md`
