# Code Reviewer Audit

## Grade
- **Current grade:** A-

## Role Snapshot
- **Slug:** `code-reviewer`
- **Title:** Code Reviewer
- **Manager:** `sparky-chief-product-quality-officer`
- **Status:** Strong curated packet, not yet live-runtime validated

## What This Employee Can Do Now
- Classify feedback as blocker, suggestion, or nit.
- Explain why issues matter and propose concrete fixes.
- Protect contracts, performance, and readability.
- Spot missing tests, duplication, and confusing logic early.

## Assigned Skills
- `code-review-gate`
- `architecture-adr`
- `handoff-state`

## Tool Expectations
- git diff
- tests
- static analysis
- artifact review

## Collaboration Fit
- Return actionable review notes to engineering owners.
- Escalate systemic quality concerns to `sparky-chief-product-quality-officer`.

## Missing Before High-Level Runtime Readiness
- Not yet wrapped into the live `open-claw/employees` runtime packet layout with Docker and bot wiring.
- Tool access is documented, but not yet proven end-to-end against the real worker runtime and installed integrations.
- No per-role activation smoke test has been recorded yet for the current OpenClaw/CrewClaw deployment path.
- No full clone-and-rebrand rehearsal has been executed yet with this packet as the primary operator.
- Needs automated review hooks or a repeatable diff-review procedure attached to the runtime delivery loop.
- Needs explicit rejection criteria for low-quality clone/rebrand edits before they reach release.

## Verdict
Use this packet as part of the authoritative standard now. Before treating it as a fully autonomous live worker, pair it with runtime packaging, real tool-entitlement proof, and a recorded smoke test.
