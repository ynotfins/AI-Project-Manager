---
name: visual-qa-evidence
description: Evidence-first QA process for screenshots, responsive coverage, dark mode, and issue reports tied to visual proof.
category: Development
roles:
  - qa-evidence-collector
  - reality-checker
  - ui-designer
  - frontend-developer
---


# Visual QA Evidence

## Status: READY

## Purpose
Prevent fantasy reporting by tying every QA claim to screenshots, traces, or visible interaction evidence.

## Workflow
1. Capture desktop, tablet, and mobile screenshots for every core flow.
2. Capture dark mode where supported.
3. Compare implementation to the actual spec, not to memory.
4. Record issues with a file reference, priority, and reproduction notes.
5. Re-run the same capture set after fixes land.

## Required Evidence
- Responsive screenshots.
- Interaction screenshots or traces.
- List of issues with direct artifact references.
- Clear pass/fail language for each critical journey.
