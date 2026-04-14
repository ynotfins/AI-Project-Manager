# DECISION_LOG.md

## Purpose
This is Sparky's durable cross-session memory.

Store major decisions here when they should survive bot restarts, context resets, or handoffs.

## Record Here
- Product direction decisions.
- Architecture or runtime decisions.
- Quality gate outcomes worth preserving.
- New recurring failure modes and their fixes.
- Heartbeat outcomes.
- Important changes to Sparky's authority, workflows, or operating posture.

## Format
Use this form for new entries:

```text
[YYYY-MM-DD] [CATEGORY]
Decision:
Reason:
Evidence:
Impact:
```

## Foundational Entries

### [2026-04-12] [RUNTIME]
Decision: Host-native `SPARKY_CEO_BOT` now launches through a packet-local startup path with Bitwarden token injection.
Reason: The CEO bot existed in Telegram but had no reliable host-native launch path.
Evidence: `start-employees.ps1 -CheckOnly -CeoOnly`, live process checks, gateway health checks.
Impact: Sparky can respond live in Telegram again.

### [2026-04-12] [RUNTIME]
Decision: On this Windows host, Sparky currently routes through the local OpenClaw `main` agent unless/until a dedicated local Sparky agent is fully registered.
Reason: The local Windows OpenClaw config only exposes `main`, and slug-based routing failed.
Evidence: `openclaw agents list`, runner repros, Telegram message handoff fixes.
Impact: The live bot works now, but packet-local workspace/config must carry Sparky identity and memory.

### [2026-04-12] [MEMORY]
Decision: Import the continuity system pattern from `temp/Sparky` into the live Sparky packet.
Reason: The live bot was responsive but too generic and had weak session continuity.
Evidence: Comparison between `temp/Sparky` and the live packet showed strong reusable onboarding/memory/session-state patterns.
Impact: Live Sparky now has `ONBOARDING.md`, `live/SESSION-STATE.md`, `live/working-buffer.md`, and upgraded continuity docs.

### [2026-04-12] [OPERATIONS]
Decision: Import selected `CHECKLISTS/` and `HANDOFF_TEMPLATES/` from `temp/Sparky` into the live Sparky packet and packet-local runtime.
Reason: Sparky needed reusable structured support surfaces for specialist routing, review gates, release gates, and drift audits.
Evidence: The donor packet contained low-conflict operational assets that aligned with the live Sparky governance model, and the startup/runtime copy path now includes those directories.
Impact: Live Sparky can use packet-local templates and checklists instead of relying on ad hoc freeform prompts for recurring governance work.

### [2026-04-12] [GOVERNANCE]
Decision: Import an adapted third-wave governance bundle from `temp/Sparky`, including runbook, source/retrieval rules, gate docs, metrics, and evaluation scenarios.
Reason: Live Sparky needed deeper reusable governance structure and regression examples, but those assets had to be aligned to the live charter-first authority model before promotion.
Evidence: The imported docs were rewritten to reference the real OpenClaw packet surface and the packet-local runtime copy path now includes the new files plus `evals/`.
Impact: Live Sparky now has stronger repeatable governance procedure and example scenarios without importing the donor packet's conflicting persona/doctrine wholesale.

### [2026-04-12] [TOOLING]
Decision: Harden the `start-openclaw-nerve.ps1` launcher to resolve `npm` dynamically, rebuild when required, and verify `/health` instead of relying on fragile process-name matching.
Reason: The dashboard runtime itself was healthy, but the launcher had brittle startup assumptions that could make Nerve appear broken or silently fail after code changes.
Evidence: Local verification showed the dashboard built cleanly and served `/`, `/health`, and `/api/connect-defaults`, while the old launcher's process detection was not trustworthy enough to prove running state.
Impact: The dashboard launch path is now more robust and gives explicit health-based feedback instead of weak process heuristics.
