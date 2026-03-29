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
- Windows Desktop node may be disconnected after reboot — verify `nodes status` and relaunch `%USERPROFILE%\.openclaw\node.cmd`.
- CrewClaw: 5 workers updated (node:22-slim, openclaw@2026.3.13, entrypoint.sh). **Pending**: bws deploy run + device pairing approval (one-time per worker).
- Context pressure mitigation active via lossless-claw context engine.

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
|---|---|---|---|
| WhatsApp 401 — session expired | MEDIUM | PENDING USER ACTION | Run `channels login --channel whatsapp` in WSL and scan QR |
| `OPENCLAW_GATEWAY_TOKEN_SECRET_ID` placeholder in `start-employees.ps1` | MEDIUM | PENDING USER ACTION | Replace with real Bitwarden secret UUID |
| CrewClaw device pairing not yet done | MEDIUM | PENDING USER ACTION | After bws deploy: `openclaw devices approve <id>` for each of 5 workers |
| Memory bridge OpenClaw ↔ OpenMemory not implemented | HIGH | DEFERRED — Phase 1B | Design required before implementation |

---

## 4. Standing Constraints

Structural limits that affect all planning. Not resolvable in a single task block.

- **Windows node connectivity**: loses connection after Windows reboot until `node.cmd` is relaunched. Startup script handles IP update but requires manual launch.
- **Bitwarden dependency**: all secret injection requires `bws` CLI and vault access. Any automated deploy is blocked without it.
- **WhatsApp QR re-scan**: cannot be automated — requires physical phone access. Recurs after each gateway restart cycle if session expires.
- **CrewClaw device pairing**: first-run one-time approval per named Docker volume lifetime. Named volumes persist identity across container rebuilds.
- **`openclaw agent --agent main`**: only the `main` agent is registered on the host gateway. Per-employee agent IDs require `setup.sh` (not run in Docker context); all CrewClaw bots must call `main`.

---

## 5. Current Focus

1. Complete Phase 1A: deploy CrewClaw workers end-to-end (bws run + device approval + smoke test).
2. Maintain stable autonomous runtime (gateway/node/startup resiliency).
3. Keep documentation and phase records synchronized across governance and execution repos.

---

## 6. Read Order For New Sessions

1. `AGENTS.md`
2. `docs/ai/STATE.md`
3. `docs/ai/PLAN.md`
4. `docs/ai/memory/DECISIONS.md`
5. `docs/tooling/MCP_CANONICAL_CONFIG.md`

Use archived docs only for historical evidence, not operational truth.
