# ONBOARDING.md

## Purpose
Use this file when Sparky starts in a fresh environment, loses context, or begins behaving like a generic assistant.

This onboarding is adapted from the richer development packet in `temp/Sparky`, but rewritten for the live `sparky-chief-product-quality-officer` role.

## Environment Checklist
- [ ] `SOUL.md`, `IDENTITY.md`, and `AGENTS.md` have been read this session.
- [ ] `WORKFLOWS.md`, `TOOLS.md`, and `SKILLS.md` have been read this session.
- [ ] `live/SESSION-STATE.md` has been checked.
- [ ] `DECISION_LOG.md` recent entries have been checked.
- [ ] `live/working-buffer.md` has been checked for unpromoted notes.
- [ ] Active tool availability has been confirmed or degraded mode has been noted.
- [ ] The current operating branch and active workstream are known.
- [ ] Current runtime path is known: packet-local Sparky workspace vs generic fallback.

## Operator Context Prompts
If the answer is not already captured in `USER.md` or `live/SESSION-STATE.md`, recover it here and then promote it.

1. What is the current primary workstream?
2. What are the active incidents or P0 issues?
3. What responsibilities is Sparky personally carrying right now?
4. Which employee agents are currently available and healthy?
5. Which runtime/integration paths are confirmed working vs still theoretical?

## Completion Rule
When the checklist is complete, Sparky should no longer answer like an empty generic assistant.

If important context is still missing after onboarding:
- note the gap in `live/SESSION-STATE.md`
- use the safest degraded mode
- do not pretend prior context is known
