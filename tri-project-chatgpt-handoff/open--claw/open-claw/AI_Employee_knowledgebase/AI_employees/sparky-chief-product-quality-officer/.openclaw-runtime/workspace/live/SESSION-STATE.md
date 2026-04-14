# SESSION-STATE.md

This is Sparky's active working memory for the current environment.

Use it for state that affects the next action, not for long narrative.

## Active Work Items

### WORK-001
- State: in_progress
- Owner: sparky-chief-product-quality-officer
- Summary: Restore and harden the live `SPARKY_CEO_BOT` runtime, then upgrade Sparky's memory and operating context from the advanced development packet in `temp/Sparky`.
- Blockers: None currently known.
- Last Updated: 2026-04-12

## Runtime Notes
- Host-native Telegram startup path is active.
- Live runtime now uses the packet-local `.openclaw-runtime` config/workspace inside the Sparky packet.
- Packet-local continuity files were added to reduce generic replies and improve recovery after restarts.
- Packet-local `CHECKLISTS/` and `HANDOFF_TEMPLATES/` were added for structured routing, review, and release governance.
- Packet-local governance docs now also include `RUNBOOK.md`, retrieval/source-priority rules, gate rules, metrics, and `evals/`.
- The host-native Telegram bot was found down during a live incident check and was restarted successfully.

## Tool Status
- Telegram delivery: working
- Host-native Node bot process: working
- Local OpenClaw CLI: working
- Packet-local dedicated Sparky agent id: working
- Global Windows OpenClaw config dedicated Sparky agent id: not yet independently registered
- Nerve dashboard health endpoint: working on `127.0.0.1:3080`

## Recovery Note
If Sparky starts acting generic:
1. Read `README.md`, `SOUL.md`, `IDENTITY.md`, `AGENTS.md`.
2. Read this file.
3. Read `DECISION_LOG.md`.
4. Read `live/working-buffer.md`.
5. Run `ONBOARDING.md` if needed.
