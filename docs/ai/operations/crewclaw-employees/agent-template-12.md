# Agent Template 12

## Identity

- Source archive: `employees/generic/crewclaw-agent-deploy (12).zip`
- Internal agent ID: `my-agent`
- Portal/profile state seen in screenshots: `Agent` / `Agent`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

This is a generic CrewClaw template package, not a real specialist.

Declared strengths:

- research
- summarization
- data analysis

It also includes a generic site scanner helper in `tools/scan-site.cjs`.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Uniqueness: FAIL
- ZIP packaging integrity: FAIL

## Missing

- real employee name
- real role definition
- role-specific skills
- role-specific rules
- specialist workflows
- specialist tools
- unique identity relative to the other generic downloads
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Treat this as a blank template only. Do not use it as a real worker until it is renamed and fully specialized.
