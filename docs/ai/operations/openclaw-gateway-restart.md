# OpenClaw gateway — canonical restart (WSL + systemd)

## Policy

- **Do not** run `pnpm openclaw gateway restart` / `openclaw gateway --force` from arbitrary shells without Bitwarden-injected API keys.
- **Do** use one of:
  1. **`$HOME\.openclaw\start-cursor-with-secrets.ps1`** (launched via `bws run …`) — calls the canonical script after Cursor starts.
  2. **`AI-Project-Manager\scripts\restart-openclaw-gateway.ps1`** from a shell that already has `ANTHROPIC_API_KEY` (+ `OPENAI_*` / `OPENROUTER_*` when required by `~/.openclaw/openclaw.json`).

## What the script does

1. Reads `~/.openclaw/openclaw.json` (inside WSL) to decide which env vars are required (`openclaw_gateway_required_env.py`).
2. **Fail-fast** if any required var is missing (no silent `.gateway-env` with blanks).
3. Writes `~/.openclaw/.gateway-env` with `chmod 600` (values never printed).
4. `systemctl --user restart openclaw-gateway.service`.

## CLI / build alignment

- Operational CLI: `source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw …`
- `~/openclaw-build` should track **`v2026.3.13-1`** (or newer stable) so CLI matches the gateway runtime.
- **systemd** `ExecStart` should use the **same** tree: `…/openclaw-build/dist/index.js gateway --port 18789` (see `openclaw doctor` — it expects `index.js` for a from-source install).

## Override repo path

If `AI-Project-Manager` is not at `D:\github\AI-Project-Manager`, set:

`$env:AI_PROJECT_MANAGER_ROOT = "D:\path\to\AI-Project-Manager"`

before running `start-cursor-with-secrets.ps1`.
