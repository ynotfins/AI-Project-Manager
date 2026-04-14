---
name: design-token-theming
description: Design token and theming system for light, dark, and system modes with accessible, reusable UI primitives.
category: Development
roles:
  - ux-architect
  - ui-designer
  - frontend-developer
  - accessibility-auditor
---


# Design Token Theming

## Status: READY

## Purpose
Define reusable colors, spacing, typography, and component states so interfaces stay consistent under iteration.

## Standards
- Use semantic tokens instead of hard-coded colors.
- Support light, dark, and system mode.
- Respect WCAG AA contrast and reduced-motion preferences.
- Keep component states explicit: default, hover, focus, active, disabled, loading, empty, and error.

## Workflow
1. Define color, spacing, typography, radius, and shadow tokens.
2. Map tokens to components and page patterns.
3. Verify contrast, focus visibility, and touch-target size.
4. Validate screenshots in light and dark contexts before approval.

## Evidence
- Token file or theme contract exists.
- All primary UI surfaces work in light and dark mode.
- Contrast and focus are verified in QA.
