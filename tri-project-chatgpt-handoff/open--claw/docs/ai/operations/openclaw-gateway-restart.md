# OpenClaw gateway — canonical restart (mirror)

Canonical copy lives in **AI-Project-Manager**: `docs/ai/operations/openclaw-gateway-restart.md`.

This file exists so the **open--claw** workspace has the same operational guidance without duplicating maintenance burden.

**Summary**

- Restart path: `AI-Project-Manager\scripts\restart-openclaw-gateway.ps1`
- Launcher: `$HOME\.openclaw\start-cursor-with-secrets.ps1` (via `bws run`)
- Align `~/openclaw-build` with gateway tag **v2026.3.13-1**; systemd uses `dist/index.js` from that tree.
