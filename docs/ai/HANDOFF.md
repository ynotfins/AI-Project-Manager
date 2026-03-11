# Agent Handoff — AI-Project-Manager

**Date**: 2026-03-11
**Handing off after**: Phase 6C.2 (WhatsApp verified, skill audit, Windows node host connected)
**Next action**: Phase 6C exit criteria — first integration connected, approval gate tested

Previous handoff archived at `docs/ai/archive/handoff-2026-03-08.md`.

---

## 1. What This Project Is

**AI-Project-Manager** is the governance repo for the Open Claw platform. It tracks phases, architecture decisions, execution state, and cross-repo coordination. It does **not** contain application code — that lives in `open--claw`.

| Repo | Role | Contains |
|------|------|----------|
| `AI-Project-Manager` | Governance | Phases, state logs, architecture docs, workflow rules, memory, tab prompts |
| `open--claw` | Execution | Project docs, skill stubs, configs, vendored OpenClaw runtime (`vendor/openclaw/`) |

Both repos share a five-tab Cursor workflow: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

---

## 2. Current State at Handoff

### OpenClaw Version

- Vendor: `v2026.3.8` (commit `3caab92`)
- Build location: `~/openclaw-build/` (WSL ext4)

### Phase Status

| Phase | Status |
|-------|--------|
| Phase 0 — Scaffold + Workflow | COMPLETE |
| Phase 1 — MCP Infrastructure | COMPLETE (14 servers) |
| Phase 2 — Secrets Management | COMPLETE (Bitwarden `bws`) |
| Phase 3 — OpenMemory Integration | COMPLETE (local proxy architecture) |
| Phase 4 — Multi-Machine Parity | COMPLETE (ChaosCentral + Laptop) |
| Phase 5 — Remaining Automation | COMPLETE (`bws run` injection for all) |
| Phase 6A — Architecture Design | COMPLETE (modules, loops, governance) |
| Phase 6B — Gateway Boot | COMPLETE |
| Phase 6C — First Live Integration | **OPEN** (6C.2 — audit log + model routing + WhatsApp + skill audit done) |

### Cross-Repo State (open--claw)

| Phase | Status |
|-------|--------|
| Phase 0 — Project Kickoff | COMPLETE |
| Phase 1 — Gateway Boot + Integration Scaffold | COMPLETE |
| Phase 2 — First Live Integration | **OPEN** |

### Runtime Environment (ChaosCentral)

- **WSL**: Ubuntu 24.04.3 LTS, Node v22.18.0 (nvm), pnpm 10.23.0
- **Gateway**: `127.0.0.1:18789`, loopback, token auth, systemd managed
- **WhatsApp**: linked, running, connected, selfChatMode, allowlist +15614193784
- **Windows node host**: paired, connected ("Windows Desktop"), capabilities: browser, system
- **Skills**: 19/58 ready (weather, github, gog, coding-agent, etc.)
- **Model routing**: primary `anthropic/claude-sonnet-4-20250514`, fallback `openai/gpt-4o-mini`
- **Agent**: not yet named (bootstrap pending first WhatsApp conversation)

### Startup Command

```
bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
```

This script: checks secrets → patches MCP → starts OpenMemory proxy → launches Cursor → starts WSL gateway → launches Windows node host in separate window.

---

## 3. Phase 6C — What Remains

**Completed exit criteria:**
- [x] Audit log captures actions (command-logger hook, config-audit.jsonl, gateway file log)
- [x] Hybrid model routing configured and verified
- [x] WhatsApp channel operational

**Remaining exit criteria:**
- [ ] First integration connected and tested
- [ ] Approval gate tested for simulated high-risk action

**Pending user actions:**
1. Name the agent via WhatsApp (bootstrap conversation)
2. Gmail OAuth setup: Google Cloud Console → enable APIs → create OAuth credential → `gog auth add`
3. MXRoute email: install `imap-smtp-email` skill from ClawHub + provide credentials

---

## 4. Key Technical Facts

- REST API chat returns 405 on this gateway version — all chat is WebSocket (Control UI) or channels
- `gog` skill installed but unauthenticated (binary at `~/.local/bin/gog`, `No tokens stored`)
- `imap-smtp-email` available on ClawHub v0.0.9, not yet installed
- Windows node host runs from `D:\github\open--claw\vendor\openclaw\` using dist copied from WSL build
- Gateway token must match between WSL (`~/.openclaw/openclaw.json`) and Windows (`%USERPROFILE%\.openclaw\openclaw.json`)

---

## 5. Files to Read First

1. `AGENTS.md` — operating contract
2. `.cursor/rules/00-global-core.md` — non-negotiable behaviors
3. `docs/ai/STATE.md` — full execution log (primary source of truth)
4. `docs/ai/PLAN.md` — what's planned
5. `docs/ai/memory/DECISIONS.md` — key decisions with rationale

---

## 6. Conventions

1. All WSL commands: `source ~/.nvm/nvm.sh` prefix
2. Build in `~/openclaw-build/`, never `/mnt/d/`
3. Update `docs/ai/STATE.md` after each execution block
4. Mirror STATE.md to `open--claw/docs/ai/STATE.md`
5. MCP-first per `05-global-mcp-usage.md`
6. No secrets in repo — `~/.openclaw/.env` only
7. `docs/ai/archive/` — never consulted by PLAN (historical only)
