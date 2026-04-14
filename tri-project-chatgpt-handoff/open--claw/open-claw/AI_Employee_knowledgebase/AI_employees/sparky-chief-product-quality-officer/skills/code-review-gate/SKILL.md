---
name: code-review-gate
description: High-signal review gate for correctness, security, maintainability, testing, and performance.
category: Development
roles:
  - code-reviewer
  - sparky-chief-product-quality-officer
  - software-architect
---


# Code Review Gate

## Status: READY

## Purpose
Turn code review into a consistent quality gate instead of a style argument.

## Priorities
- Blockers: correctness, data loss, auth/security, contract breaks, race conditions.
- Suggestions: validation gaps, unclear logic, missing tests, duplication, avoidable performance issues.
- Nits: low-impact polish only after higher-risk issues are covered.

## Output Format
- Start with a short summary.
- Use blocker, suggestion, and nit labels consistently.
- Explain why each issue matters and propose a concrete fix.
- End with next steps and positive patterns worth repeating.
