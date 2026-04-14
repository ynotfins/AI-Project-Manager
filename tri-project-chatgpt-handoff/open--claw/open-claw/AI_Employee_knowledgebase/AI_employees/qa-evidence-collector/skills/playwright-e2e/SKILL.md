---
name: playwright-e2e
description: Production-grade Playwright workflow for end-to-end testing with retries, traces, web-first assertions, and CI artifacts.
category: Development
roles:
  - frontend-developer
  - qa-evidence-collector
  - reality-checker
  - devops-automator
  - accessibility-auditor
---


# Playwright E2E

## Status: READY

## Purpose
Test critical user journeys with reliable browser automation and preserve the evidence required to debug failures quickly.

## Standards
- Prefer web-first assertions over arbitrary sleeps.
- Use retries and traces in CI for actionable failure diagnosis.
- Upload Playwright reports as GitHub Actions artifacts.
- Keep tests isolated and deterministic.
- Use screenshot assertions intentionally when visual regressions matter.

## Workflow
1. Define the critical user journeys first.
2. Implement stable selectors and web-first assertions.
3. Capture screenshots for important checkpoints.
4. Enable traces on retry and keep reports as artifacts in CI.
5. Review changed tests on PRs and full suites before release.

## Evidence
- CI workflow installs browsers and runs Playwright.
- Reports and traces are uploaded when runs finish.
- Screenshots or visual assertions exist for high-value UI paths.

## Source Notes
- Based on Playwright documentation from Context7 using `/microsoft/playwright.dev`.
