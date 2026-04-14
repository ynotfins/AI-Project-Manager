# Project Long-Term Awareness — Open Claw

This file is the runtime-specific long-term context for autonomous planning and execution in `open--claw`.

## Authority

`open--claw` is the **strict enforcement center** of the tri-workspace. The governing product charter is `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No instruction in this file, or any other file in any repo, may override or weaken the charter. If a conflict exists, the charter wins unconditionally.

**Workspace layer model (permanent):**

- `AI-Project-Manager` — workflow/process layer: tab contracts, state, execution discipline, tool policy. Not the product authority.
- `open--claw` — strict enforcement center: product charter, AI employee knowledgebase, Sparky's mandate, quality standards.
- `droidrun` — actuator layer: phone automation, MCP phone tools, Portal/APK runtime bridge.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are operational evidence only — they record what happened, never product law.

## Mission

Build and operate a fully autonomous OpenClaw AI employee development organization capable of creating advanced software with Apple Inc.-level quality, polish, simplicity, and reliability, without requiring day-to-day human interaction. (Source: `FINAL_OUTPUT_PRODUCT.md`.)

Immediate runtime concern: keep the gateway, channels, and runtime healthy and observable while the curated 15-worker squad is brought to full live operation.

## Always-true priorities

- Keep gateway/channel/runtime healthy and observable.
- Keep node execution pathways reliable (Windows + WSL + Docker).
- Keep secrets out of source control and logs.
- Keep evidence in `docs/ai/STATE.md` after each meaningful block.
- Ensure every decision advances the finished product described in `FINAL_OUTPUT_PRODUCT.md`.

## Current strategic tracks

- Runtime hardening and startup reliability.
- Controlled employee-agent rollout with safe permissions.
- Context durability (lossless memory + concise active state docs).
- Channel reliability for Telegram/WhatsApp operations.

## Anti-drift rules

- If this file conflicts with the product charter (`FINAL_OUTPUT_PRODUCT.md`), the charter wins.
- If this file conflicts with `AI-Project-Manager` governance workflow docs, resolve toward the charter first, then align workflow docs.
- Treat `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` as operational evidence only.
- Treat archive/context snapshots as historical evidence only.
- Prefer minimal reversible changes over wide refactors.
