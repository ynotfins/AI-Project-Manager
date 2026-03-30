# Frontend Developer

## Identity

- Package name: `frontend-developer.zip`
- Deployed folder: `open-claw/employees/deployed/frontend-developer`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

The package name says frontend specialist, but the actual package content is mostly generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

The currently deployed Telegram wrapper routes to `main`, not to a dedicated frontend agent.

## Why It Matters For A Next.js Website Clone

By name, this should be one of the most important employees for the website project.

In its current state, it is not truly a frontend specialist. It behaves more like a generic research worker with a frontend label.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: FAIL for specialist isolation in the current shared deployment
- ZIP packaging integrity: FAIL

## Missing

- code generation as a declared skill
- explicit Next.js / React / Tailwind / CSS theming focus
- component editing guidance
- responsive layout and accessibility guidance
- browser QA workflow
- direct routing to a dedicated frontend agent in the current shared deployment
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Do not treat this as a trusted autonomous frontend worker yet.

It should be re-specialized before use in the website squad. Once rewritten, it should own:

- theme/color updates
- contact info/UI text changes
- component-level cleanup
- responsive polish
- accessibility pass
