# Financial Analyst

## Identity

- Package name: `financial-analyst.zip`
- Deployed folder: `open-claw/employees/deployed/financial-analyst`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

The package is structurally complete, but the role content is generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

The currently deployed Telegram wrapper routes to `main`, not to a dedicated finance agent.

## Website-Project Relevance

This employee is low-value for the current Next.js rebrand workflow.

It may become useful later for:

- pricing comparison
- budget modeling
- ROI analysis
- cost planning

It is not a primary website execution worker.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: FAIL for specialist isolation in the current shared deployment
- ZIP packaging integrity: FAIL

## Missing

- finance-specific workflows
- pricing / forecasting guidance
- budget-analysis instructions
- clear boundaries for when to use this worker
- direct routing to a dedicated financial analyst agent in the current shared deployment
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Do not include this in the first website-clone squad.
