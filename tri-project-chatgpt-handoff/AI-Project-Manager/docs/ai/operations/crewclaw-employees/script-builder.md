# Script Builder

## Identity

- Package name: `script-builder.zip`
- Deployed folder: `open-claw/employees/deployed/script-builder`
- Agent ID in package: `script-builder`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

This package routes directly to `script-builder`, but the role definition is still generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

## Website-Project Relevance

This could become useful for automation support around the website project:

- rename scripts
- content replacement scripts
- image/asset migration helpers
- repo utility scripts

Today that specialization is not encoded in the employee docs.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: PASS
- ZIP packaging integrity: FAIL

## Missing

- code-generation emphasis
- automation and scripting workflows
- file migration / batch rewrite guidance
- testing and safety checks for generated scripts
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Promote this to a real automation specialist before using it heavily.
