# Agent Handoff — AI-Project-Manager

**Date**: 2026-03-29
**Status**: Current handoff
**Primary source of truth**: `docs/ai/STATE.md`

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
- Phase 1A — CrewClaw Worker Stabilization: IN PROGRESS (2026-03-29)
- Post-6C hardening and operations: ACTIVE

### Runtime highlights (verified 2026-03-29)

- OpenClaw CLI + systemd runtime aligned on `~/openclaw-build` tag `v2026.3.13-1`. Systemd `ExecStart` uses `openclaw-build/dist/index.js`.
- **Telegram**: healthy, running.
- **WhatsApp**: 401 Unauthorized — QR re-scan required (`pnpm openclaw channels login --channel whatsapp` in WSL).
- **Signal**: disabled by design.
- Windows Desktop node is currently reconnected and Sparky can execute on it again (`hostname` probe passed). Cursor CLI paths are visible from that node, but the node still tends to disconnect after reboot until `%USERPROFILE%\.openclaw\node.cmd` is relaunched.
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
| Memory bridge OpenClaw ↔ OpenMemory not implemented | HIGH | DEFERRED — Phase 1B | Design required before implementation |

---

## 4. Standing Constraints

Structural limits that affect all planning. Not resolvable in a single task block.

- **Windows node connectivity**: loses connection after Windows reboot until `node.cmd` is relaunched. Startup script handles IP update but requires manual launch.
- **Bitwarden dependency**: all secret injection requires `bws` CLI and vault access. Any automated deploy is blocked without it.
- **WhatsApp QR re-scan**: cannot be automated — requires physical phone access. Recurs after each gateway restart cycle if session expires.
- **CrewClaw device pairing**: first-run one-time approval per named Docker volume lifetime. Named volumes persist identity across container rebuilds.

---

## 5. Current Focus

1. Complete Phase 0 activation: keep the shared OpenAI -> Grok -> Anthropic model chain stable, then prove one real Telegram round trip through the paired worker fleet.
2. Maintain stable autonomous runtime (gateway/node/startup resiliency).
3. Use the curated employee standard in `open--claw/open-claw/AI_Employee_knowledgebase` as the new baseline for future website/app squads instead of trusting the raw CrewClaw ZIPs.
4. Keep the approved CrewClaw monitor-key local `.env` exception documented and use it for portal heartbeat activation as workers are added.
5. Keep documentation and phase records synchronized across governance and execution repos.

---

## 6. Read Order For New Sessions

1. `AGENTS.md`
2. `docs/ai/STATE.md`
3. `docs/ai/PLAN.md`
4. `docs/ai/memory/DECISIONS.md`
5. `docs/tooling/MCP_CANONICAL_CONFIG.md`

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
