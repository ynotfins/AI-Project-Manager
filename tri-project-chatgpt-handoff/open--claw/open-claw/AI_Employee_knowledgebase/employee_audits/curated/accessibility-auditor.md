# Accessibility Auditor Audit

## Grade
- **Current grade:** A-

## Role Snapshot
- **Slug:** `accessibility-auditor`
- **Title:** Accessibility Auditor
- **Manager:** `sparky-chief-product-quality-officer`
- **Status:** Strong curated packet, not yet live-runtime validated

## What This Employee Can Do Now
- Run automated checks and manual screen-reader or keyboard-first audits.
- Tie every issue to a specific WCAG criterion and user impact.
- Catch the 70% of accessibility problems automation misses.
- Push accessibility upstream into design and implementation choices.

## Assigned Skills
- `playwright-e2e`
- `visual-qa-evidence`
- `design-token-theming`

## Tool Expectations
- axe
- Lighthouse
- screen reader testing
- browser verification

## Collaboration Fit
- Share remediation guidance with `frontend-developer`, `ui-designer`, and `qa-evidence-collector`.
- Provide release evidence to `reality-checker`.

## Missing Before High-Level Runtime Readiness
- Not yet wrapped into the live `open-claw/employees` runtime packet layout with Docker and bot wiring.
- Tool access is documented, but not yet proven end-to-end against the real worker runtime and installed integrations.
- No per-role activation smoke test has been recorded yet for the current OpenClaw/CrewClaw deployment path.
- No full clone-and-rebrand rehearsal has been executed yet with this packet as the primary operator.
- Needs automated contrast, keyboard, and screen-reader verification integrated into the QA flow.
- Needs a documented remediation checklist for common website-clone accessibility regressions.

## Verdict
Use this packet as part of the authoritative standard now. Before treating it as a fully autonomous live worker, pair it with runtime packaging, real tool-entitlement proof, and a recorded smoke test.
