# Seo Specialist

## Identity

- Package name: `seo-specialist.zip`
- Deployed folder: `open-claw/employees/deployed/seo-specialist`
- Agent ID in package: `seo-specialist`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

This package routes directly to `seo-specialist`, but the role definition is still generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

## Why It Matters For A Next.js Website Clone

This worker can become valuable after the first website clone is stable, especially for:

- page titles and descriptions
- metadata cleanup
- schema and on-page SEO
- copy review

Right now, those responsibilities are implied by the name, not by the package contents.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: PASS
- ZIP packaging integrity: FAIL

## Missing

- actual SEO heuristics and workflow
- metadata and schema ownership
- content optimization rules
- crawlability / internal-link checks
- browser verification of metadata output
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Keep this in the website squad for later-stage optimization, not for first-pass implementation.

After re-specialization, it should own:

- metadata updates
- content and heading cleanup
- title/description consistency
- technical SEO review
