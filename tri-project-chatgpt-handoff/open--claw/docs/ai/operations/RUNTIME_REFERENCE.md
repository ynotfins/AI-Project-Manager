# Runtime Reference

Hardened operational facts for the open--claw runtime on ChaosCentral (WSL2).
This document captures values verified through Phase 0-6C execution evidence.

## Gateway

| Property | Value |
|----------|-------|
| Control UI port | **18789** (`http://localhost:18789`) |
| API health port | **18792** (`http://localhost:18792/` returns `OK`) |
| Process name | `openclaw-gateway` |
| Auth | Token-based (generated during `onboard`) |
| Config file | `~/.openclaw/openclaw.json` |

### Commands

```bash
pnpm openclaw gateway status      # Runtime: running, RPC probe: ok
pnpm openclaw health               # Agents: main (default), exit 0
pnpm openclaw doctor               # Full diagnostic
pnpm openclaw gateway --force      # Kill + restart gateway
pnpm openclaw dashboard            # Open Control UI with token
pnpm openclaw logs                 # Tail gateway file logs via RPC
pnpm openclaw sessions             # List stored conversation sessions
pnpm openclaw tui                  # Terminal UI connected to Gateway
```

### Gateway restart (after config/skill changes)

```bash
pnpm openclaw gateway --force
# or via systemd:
systemctl --user restart openclaw-gateway
```

## WSL Paths

| Path | Purpose |
|------|---------|
| `~/openclaw-build/` | Main build directory (ext4, never `/mnt/d/`) |
| `~/.openclaw/` | Config + state directory |
| `~/.openclaw/openclaw.json` | Gateway configuration |
| `~/openclaw-build/skills/` | Bundled skills |
| `~/.openclaw/workspace/skills/` | ClawHub-installed skills |
| `~/.nvm/` | Node Version Manager |

## Node / pnpm

| Tool | Version | Location |
|------|---------|----------|
| Node | v22.22.0 | `~/.nvm/versions/node/v22.22.0/bin/node` |
| pnpm | 10.23.0 | `~/.nvm/versions/node/v22.22.0/bin/pnpm` |
| nvm | managed via `~/.bashrc` | auto-loads on login shell |

If `node -v` fails in a fresh terminal, verify `~/.bashrc` has the nvm init block
and no hardcoded `export PATH=` clobbering it.

## Systemd Service

```bash
loginctl show-user ynotf -p Linger    # Linger=yes means service survives reboot
loginctl enable-linger ynotf          # Enable if not set
systemctl --user status openclaw-gateway
systemctl --user restart openclaw-gateway
```

## Secret Injection

All secrets are injected via Bitwarden Secrets Manager at runtime.
Never stored in plaintext on disk or in version control.

```powershell
# From PowerShell (Windows side):
bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
```

Prerequisite: `BWS_ACCESS_TOKEN` must be set in the parent shell.

## Health Check Quick Reference

```bash
# Minimal verification after reboot or session start:
node -v                                              # v22.x
pnpm -v                                              # 10.x
curl -s http://localhost:18792/                       # OK
pnpm openclaw gateway status                         # Runtime: running
pnpm openclaw skills check | head -5                 # Skills (N/50 ready)
```

## Agent Invocation

```bash
pnpm openclaw agent --message "Your prompt here"
pnpm openclaw agent --to +15555550123 --message "Run summary" --deliver
```

## Version

- OpenClaw: 2026.2.18 (b228c06)
- Build date: 2026-02-18
