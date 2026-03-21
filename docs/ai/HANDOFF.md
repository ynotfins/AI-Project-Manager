# Agent Handoff — AI-Project-Manager

**Date**: 2026-03-21  
**Status**: Current handoff (replaces 2026-03-11 snapshot)  
**Primary source of truth**: `docs/ai/STATE.md`

Previous handoff snapshot remains at `docs/ai/archive/handoff-2026-03-08.md`.

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
- Post-6C hardening and operations: ACTIVE

### Runtime highlights (from latest verified state)

- OpenClaw **CLI + systemd runtime aligned** on `~/openclaw-build` **tag `v2026.3.13-1`** (eliminates mixed 2026.3.8 CLI vs 2026.3.13 service drift). Systemd `ExecStart` uses `openclaw-build/dist/index.js` (matches `openclaw doctor` expectations).
- Core channels: Telegram and WhatsApp healthy; Signal disabled by design.
- Windows **Desktop node may be disconnected after reboot** — verify `nodes status` and relaunch `%USERPROFILE%\.openclaw\node.cmd` when host execution is needed.
- CrewClaw deployment is active with Docker + Bitwarden-injected secrets model.
- Context pressure mitigation is active via lossless-claw context engine.

### Startup baseline

```powershell
bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
```

### Canonical gateway restart (no ad-hoc CLI)

- Prefer the launcher above (it calls `AI-Project-Manager\scripts\restart-openclaw-gateway.ps1` after Cursor starts).
- Manual: from an injected shell, `pwsh -File D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1`
- See `docs/ai/operations/openclaw-gateway-restart.md`.
- Override repo path: `$env:AI_PROJECT_MANAGER_ROOT = "D:\path\to\AI-Project-Manager"` if needed.

---

## 3. Current Focus

1. Maintain stable autonomous runtime (gateway/node/startup resiliency).
2. Keep documentation and phase records synchronized across governance and execution repos.
3. Expand employee automation safely with strict secret isolation (Bitwarden injection; no `.env*` in git).

---

## 4. Read Order For New Sessions

1. `AGENTS.md`
2. `docs/ai/STATE.md`
3. `docs/ai/PLAN.md`
4. `docs/ai/memory/DECISIONS.md`
5. `docs/tooling/MCP_CANONICAL_CONFIG.md`

Use archived docs only for historical evidence, not operational truth.
