# QA Evidence Collector Audit

## Grade
- **Current grade:** A-

## Role Snapshot
- **Slug:** `qa-evidence-collector`
- **Title:** QA Evidence Collector
- **Manager:** `delivery-director`
- **Status:** Strong curated packet, not yet live-runtime validated

## What This Employee Can Do Now
- Capture visual evidence for core paths and responsive states.
- Default to finding real issues instead of approving first passes.
- Compare product behavior to the actual specification.
- Document failures clearly enough that engineers can fix them quickly.

## Assigned Skills
- `playwright-e2e`
- `visual-qa-evidence`
- `release-readiness`

## Tool Expectations
- Playwright
- screenshots
- traces
- browser verification

## Collaboration Fit
- Send evidence-backed findings to engineering owners and `reality-checker`.
- Coordinate with `accessibility-auditor` on inclusive QA coverage.

## Missing Before High-Level Runtime Readiness
- Not yet wrapped into the live `open-claw/employees` runtime packet layout with Docker and bot wiring.
- Tool access is documented, but not yet proven end-to-end against the real worker runtime and installed integrations.
- No per-role activation smoke test has been recorded yet for the current OpenClaw/CrewClaw deployment path.
- No full clone-and-rebrand rehearsal has been executed yet with this packet as the primary operator.
- Needs a repeatable screenshot and artifact capture pipeline for desktop, tablet, and mobile after each rebrand pass.
- Needs a standard evidence bundle format for handing findings to Sparky and Delivery Director.

## Verdict
Use this packet as part of the authoritative standard now. Before treating it as a fully autonomous live worker, pair it with runtime packaging, real tool-entitlement proof, and a recorded smoke test.
