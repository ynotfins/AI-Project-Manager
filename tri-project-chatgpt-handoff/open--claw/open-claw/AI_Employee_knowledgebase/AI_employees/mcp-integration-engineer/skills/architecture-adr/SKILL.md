---
name: architecture-adr
description: Architecture decision record workflow for design choices, trade-offs, rollback paths, and modular boundaries.
category: Development
roles:
  - software-architect
  - backend-architect
  - sparky-chief-product-quality-officer
  - code-reviewer
  - mcp-integration-engineer
---


# Architecture ADR

## Status: READY

## Purpose
Make architectural choices explicit, reversible where possible, and easy for future contributors to understand.

## Requirements
- State the problem, options, decision, and consequences.
- Call out what gets easier and what gets harder.
- Document rollback or migration paths for risky changes.
- Keep boundaries explicit across ui, domain, data, and utils.

## When To Use
- New subsystem or service boundary.
- New runtime or framework integration.
- Non-trivial data model or API contract change.
- Any decision likely to affect the next quarter of work.
