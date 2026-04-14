# Api Integration Specialist

## Identity

- Package name: `api-integration-specialist.zip`
- Deployed folder: `open-claw/employees/deployed/api-integration-specialist`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

The package is structurally complete, but its actual behavior definition is generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

The currently deployed Telegram wrapper routes to `main`, not to a dedicated API specialist agent.

## Website-Project Relevance

This worker is useful later in the website project for:

- forms
- backend/API integrations
- CRM or webhook connections
- external service wiring

It is not yet truly specialized enough to trust with those tasks autonomously.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: FAIL for specialist isolation in the current shared deployment
- ZIP packaging integrity: FAIL

## Missing

- real API/integration workflow instructions
- Next.js route handler / backend integration guidance
- form submission and webhook patterns
- environment-variable discipline for app integrations
- direct routing to a dedicated API integration agent in the current shared deployment
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Keep this available for later integration work, but do not treat it as a real specialist until re-specialized.
