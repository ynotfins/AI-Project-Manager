# Software Engineer

## Identity

- Package name: `software-engineer.zip`
- Deployed folder: `open-claw/employees/deployed/software-engineer`
- Agent ID in package: `software-engineer`
- Declared role: `Software Engineer`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

Based on the package files, this is the strongest current implementation worker in the fleet.

Declared strengths:

- code generation
- research
- data analysis
- direct agent-specific routing in `bot-telegram.js`
- Telegram / Discord / Slack / WhatsApp bot wrappers present
- full CrewClaw doc set present (`SOUL.md`, `TOOLS.md`, `SKILLS.md`, `WORKFLOWS.md`, etc.)

## Why It Matters For A Next.js Website Clone

This is the best current starting point for the workflow you described:

- clone an existing site
- change brand name and contact information
- update color palette and styling foundation
- build and verify the result before image/content replacement

It is the only current employee package whose declared skill set actually includes code generation.

## Current Audit Result

- Structure: PASS
- Specialist quality: PASS relative to the rest of the fleet, but still incomplete
- Runtime routing: PASS
- ZIP packaging integrity: FAIL

## Missing

- explicit Next.js App Router specialization
- explicit React / TypeScript / Tailwind specialization
- browser-based visual QA instructions
- a documented clone-and-rebrand checklist
- build/test commands in the employee docs
- explicit use of Cursor / Windows node / git workflow
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Use this employee as the lead builder for the first Next.js website trial.

Before trusting it with a full autonomous website rebrand, add:

- Next.js-specific instructions
- Tailwind / CSS theming expectations
- git clone / branch / test / review steps
- browser verification requirements
- a rule to update metadata, logos, colors, and contact info first before touching images
