# Sparky Replacement Audit

## Candidate
`D:\github\open--claw\temp\Sparky`

## Verdict
Do **not** replace the current curated Sparky packet wholesale.

Use the temp packet as a **merge/salvage source** for governance doctrine, handoff patterns, and evaluation material.

## Why Not A Full Replacement
- It does not match the current curated OpenClaw packet blueprint.
- It is missing required curated packet files such as the house-style `BOOTSTRAP.md`, `SCHEDULE.md`, and `CHECKLIST.md`.
- It does not ship the current OpenClaw runtime shell used by the curated employee packets.
- Its role definition leans toward overseer/governor behavior and conflicts with the current curated Sparky mandate as both final gate and hands-on technical escalation path.
- Its TypeScript/live runtime appears development-grade, not deployment-ready.

## Strongest Files To Salvage
- `AGENTS.md`
- `OPERATING_RULES.md`
- `APPROVAL_GATES.md`
- `MERGE_POLICY.md`
- `PR_RULES.md`
- `ESCALATION_RULES.md`
- `ANTI_PATTERNS.md`
- `LIMITS.md`
- `SECURITY.md`
- `WORKFLOWS.md`
- `RUNBOOK.md`
- `CHECKLISTS/*`
- `HANDOFF_TEMPLATES/*`
- `evals/*`

## Code Risks In The Temp Packet
- `agent.ts` includes side-effecting PR enforcement behavior that should not be adopted blindly.
- `schema.ts` and the agent/live runtime contract appear out of sync.
- `tools.ts` assumes `gh`-driven GitHub operations and may not align with the current OpenClaw worker runtime.
- `live/*` looks like an experiment or staging harness, not a validated OpenClaw worker deployment surface.

## Recommended Merge Strategy
1. Keep the current curated Sparky packet as the active packet.
2. Promote the best governance doctrine from `temp/Sparky` into curated docs selectively.
3. Do not import the temp runtime/code paths until their TypeScript contracts and runtime assumptions are validated separately.
4. Treat the temp packet as a doctrine and evaluation asset, not a deployment target.
