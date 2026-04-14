# Agent Handoff — DroidRun

**Date**: 2026-03-19  
**Status**: Active handoff  
**Primary source of truth**: `docs/ai/STATE.md`

---

## 1. What This Repo Covers

`droidrun` is the **actuator layer** of the tri-workspace stack. It executes phone automation tasks; it does not govern.

**Workspace layer model (durable operating truth):**

- `AI-Project-Manager` — workflow/process layer: tab contracts, state tracking, execution discipline, tool policy. Does not issue product law.
- `open--claw` — strict enforcement center: the supreme product charter (`FINAL_OUTPUT_PRODUCT.md`), AI employee knowledgebase, Sparky's mandate, quality standards.
- `droidrun` — actuator layer: phone automation, MCP phone tools, Portal/APK runtime bridge.

The governing product charter for all three workspaces is `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No rule or doc in this repo overrides it.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` (this file) are **operational evidence only**. They record current state and blockers. They are not product law.

---

## 2. Current Operating Focus

- Stable device connectivity and reconnection behavior
- Reliable MCP tool availability for phone operations
- Evidence-first diagnostics for ADB/port/connection failures

---

## 3. Read Order For New Sessions

1. `../open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (read this first, always)
2. `AGENTS.md`
3. `docs/ai/STATE.md` — operational evidence
4. `docs/ai/PLAN.md`
5. `docs/ai/memory/DECISIONS.md`
6. `docs/ai/memory/PATTERNS.md`

Use `docs/ai/HANDOFF.md` (this file) and archive/chat artifacts as operational evidence only — never as product law.

### Serena local scope

Use Serena for DroidRun code through `D:/github/droidrun`. Upstream charter/governance docs are still read normally, but they are not part of the DroidRun Serena project. If work moves into AI-Project-Manager or OpenClaw runtime code, activate that project by exact path first.

---

## 4. Recent Unresolved Issues

_AGENT: promote unresolved turbulence here — failed attempts that changed direction, unresolved errors, fallback paths that became reality, still-unverified assumptions. Keep concise; one line per item._

- Live bootstrap adherence with updated tab prompts not yet verified in a real session.

---

## 5. Standing Constraints

_Constraints that affect future planning regardless of current phase._

- ADB port 5555 resets on phone reboot → always run `scripts/reconnect_remote.ps1` before MCP use.
- `adb forward tcp:8080 tcp:8080` must be re-established after every new ADB connection.
- DeepSeek does not support vision (image_url format) → use `-Vision` flag to route to OpenRouter/Gemini.
- OpenClaw uses Grok-4 by default; WhatsApp channel on +15614193784.
