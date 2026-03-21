# Project Long-Term Awareness

This document preserves mission-level context so PLAN can act autonomously without drifting from each project's purpose.

## System view

- `AI-Project-Manager`: governance, planning contracts, state truth, quality/safety policy.
- `open--claw`: execution runtime (OpenClaw gateway, channels, node execution, autonomous workers).
- `droidrun`: mobile runtime control and phone automation layer.

## AI-Project-Manager long-term goals

- Maintain a reliable five-tab operating model.
- Keep evidence-first execution with deterministic PASS/FAIL reporting.
- Preserve high-signal documentation and prevent context-window collapse.
- Enforce secret hygiene and modular engineering standards.
- Coordinate cross-repo priorities without losing state continuity.

## open--claw long-term goals

- Stable autonomous agent runtime across reboot and network changes.
- Trusted operator behavior for family-safe personal use.
- Controlled expansion of integrations and employee agents.
- Strict credential isolation (Bitwarden/runtime injection, no committed secret files).
- Reliable Windows + WSL + Docker execution posture.

## Cross-repo constraints

- Governance truth lives in `AI-Project-Manager` and must be mirrored where needed.
- Runtime truth must be reflected in both repos' `STATE.md` entries.
- Archive historical detail; keep active docs concise.
- No feature work should block critical delivery paths.

## Planning heuristics for autonomy

- Select the smallest verifiable next block.
- Prefer recovery and observability improvements before new complexity.
- Resolve contradictions in docs/state before shipping new work.
- Keep rollback paths explicit for every risky change.
