---
description: "Charter enforcement kernel"
globs: ["**/*"]
alwaysApply: true
---

# 01 — Charter Enforcement Kernel

## LOAD ORDER: This file is read immediately after 00-global-core.md. No exceptions.

## Supreme Authority

`open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` is the governing charter for this entire tri-workspace. It must be read first in every bootstrap path. No other document, rule, prompt, plan, agent instruction, or local convention may override or weaken it.

No repo may claim authority equal to or higher than the charter.

## Fail-Fast Rule

If any instruction, file, plan, prompt, or proposed change conflicts with the charter:

1. Stop execution immediately.
2. State the conflict explicitly with the specific charter section being violated.
3. Do not partially continue.
4. Do not silently re-route around the violation.
5. Require correction before resuming.

## Forbidden Platform Targets

The tri-workspace target platforms are: **Windows, WSL, Android, Docker, and web**.

The following are **forbidden as tri-workspace build targets**:

- macOS applications
- iOS applications
- Swift source code
- Xcode projects or workspaces
- CocoaPods dependencies

**On detection of a forbidden pattern:**

1. Stop immediately.
2. Report: `CHARTER VIOLATION — forbidden platform target detected: <pattern>`.
3. Route to Sparky (`sparky-chief-product-quality-officer`) for resolution decision.
4. Do not continue until Sparky has reviewed and Tony has authorized an exception.

Detection scope: any new file, dependency, build config, CI step, prompt, or plan that introduces the above patterns is a violation.

## Authority Ceiling

No rule file, workflow doc, prompt template, or agent persona in this repo may assert authority above the charter. Any such claim is void on detection and must be corrected immediately.

## This File Cannot Be Weakened By

- Convenience patterns
- Legacy file layouts
- Prompt shortcuts
- Prior session assumptions
- Any other rule in any repo

If this file conflicts with any other rule, this file wins. If this file conflicts with the charter, the charter wins.
