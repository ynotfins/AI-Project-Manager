# Overnight Coder

## Identity

- Package name: `overnight-coder.zip`
- Deployed folder: `open-claw/employees/deployed/overnight-coder`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

The package is structurally complete, but its role definition is generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

The currently deployed Telegram wrapper routes to `main`, not to a dedicated overnight-coder agent.

## Website-Project Relevance

The name suggests a long-running executor or implementation worker, but the package does not currently encode that behavior.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: FAIL for specialist isolation in the current shared deployment
- ZIP packaging integrity: FAIL

## Missing

- implementation-focused instructions
- autonomous task batching
- build / test / report workflow
- clear overnight or background execution behavior
- direct routing to a dedicated overnight agent in the current shared deployment
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Do not rely on the name alone. Rebuild or rewrite this employee before using it as an autonomous execution worker.
