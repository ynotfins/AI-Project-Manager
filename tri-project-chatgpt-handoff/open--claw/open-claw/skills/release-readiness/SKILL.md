---
name: release-readiness
description: Release gate for build verification, regression evidence, rollback planning, and final go/no-go decisions.
category: Development
roles:
  - devops-automator
  - reality-checker
  - qa-evidence-collector
  - sparky-chief-product-quality-officer
---


# Release Readiness

## Status: READY

## Purpose
Define the minimum proof needed before a release or handoff is called ready.

## Gate Checklist
- Build passes in CI.
- Critical tests pass.
- QA evidence is current for primary journeys.
- Accessibility issues have been reviewed for release impact.
- Rollback or revert path is known.
- Open risks are written down, not implied.

## Verdicts
- READY: evidence is complete and no critical issues remain.
- NEEDS WORK: incomplete proof or unresolved release risk.
- FAILED: known breakage, missing evidence, or blocked deployment path.
