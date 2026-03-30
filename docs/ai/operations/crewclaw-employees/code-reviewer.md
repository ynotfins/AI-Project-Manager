# Code Reviewer

## Identity

- Package name: `code-reviewer.zip`
- Deployed folder: `open-claw/employees/deployed/code-reviewer`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

This package is structurally complete, but the actual role configuration is generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

The deployed Telegram wrapper currently routes to `main`, not to a dedicated code-reviewer agent.

## Why It Matters For A Next.js Website Clone

A real code-review worker would be extremely useful for this workflow, especially after the first clone/rebrand pass.

Right now, this package does not yet justify the `code-reviewer` label.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: FAIL for specialist isolation in the current shared deployment
- ZIP packaging integrity: FAIL

## Missing

- actual code-review instructions
- defect-finding / regression-review workflow
- build/lint/test review checklist
- Next.js review criteria
- Tailwind / CSS regression criteria
- direct routing to a dedicated code-reviewer agent in the current shared deployment
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Do not rely on this as the quality gate until it is re-specialized.

Once improved, it should own:

- lint/build/test review
- UI regression review
- code-smell review
- PR-level change assessment
