# Ux Designer

## Identity

- Package name: `ux-designer.zip`
- Deployed folder: `open-claw/employees/deployed/ux-designer`
- Agent ID in package: `ux-designer`
- Declared role: `Custom Role`
- Declared model: `Claude Sonnet 4.5`

## What It Can Do Today

The package is structurally complete and routes directly to `ux-designer`, but its actual role definition is still generic.

Declared strengths:

- research
- summarization
- data analysis
- web search

## Why It Matters For A Next.js Website Clone

This should be one of the key workers for a rebrand, especially around:

- design consistency
- color system changes
- visual hierarchy
- usability review

Today it does not contain those responsibilities in a meaningful way.

## Current Audit Result

- Structure: PASS
- Specialist quality: FAIL
- Runtime routing: PASS
- ZIP packaging integrity: FAIL

## Missing

- real UX / design review instructions
- component-level UI critique patterns
- layout / spacing / typography guidance
- browser screenshot or visual-review workflow
- accessibility review guidance
- Figma/design-system style rules
- ZIP Dockerfile correctness (`COPY bot.js` bug)

## Recommendation

Use this only as a supporting review worker after re-specialization.

It should eventually own:

- visual review of the cloned site
- color and design-system consistency
- layout and readability checks
- mobile and desktop presentation review
