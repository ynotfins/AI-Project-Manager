# KNOWLEDGE_SOURCES.md

## Purpose

This file registers the authoritative sources Sparky may use for governance decisions.

If a source is not registered here, it may provide context but should not satisfy a gate condition on its own.

## Internal Doctrine Sources

These are the primary internal governance sources.

| Source | Location | Authority Scope |
| --- | --- | --- |
| Product charter | `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` | Supreme product law |
| Role and authority | `README.md`, `AGENTS.md` | Live role, authority, and operating posture |
| Governance flow | `WORKFLOWS.md`, `RUNBOOK.md` | Required workflow and execution procedure |
| Quality gate | `AUDIT.md`, `APPROVAL_GATES.md`, `PR_RULES.md` | Review, merge, and release criteria |
| Evidence discipline | `SOURCE_PRIORITY.md`, `RETRIEVAL_RULES.md` | Source conflict handling and retrieval requirements |
| Operating supports | `CHECKLISTS/`, `HANDOFF_TEMPLATES/`, `evals/` | Repeatable checklists, specialist routing, and regression scenarios |
| Tooling policy | `TOOLS.md`, `SKILLS.md`, `ACCESS.md`, `COMPLETE_TOOL_REFERENCE.md` | Tool expectations and access boundaries |

## Runtime State Sources

| Source | Location | Authority Scope |
| --- | --- | --- |
| Durable decisions | `DECISION_LOG.md` | Prior committed decisions |
| Active work state | `live/SESSION-STATE.md` | Current runtime work state |
| In-flight notes | `live/working-buffer.md` | Pending notes not yet promoted |

## External Documentation Sources

| Source | Authority Scope | Retrieval Method |
| --- | --- | --- |
| Context7 library docs | Current framework and library behavior | Context7 MCP |
| GitHub state | PR state, review comments, checks | `gh` CLI or GitHub MCP |
| Runtime observations | Current system behavior | Logs, process checks, health checks, live responses |

## Review Sources

| Source Type | Authority Scope | Minimum Evidence Standard |
| --- | --- | --- |
| Security specialist review | Security correctness | Specific controls and evidence cited |
| Architecture review | Boundaries and contracts | Specific structural findings cited |
| Code review | Code correctness and tests | Specific files, findings, and tests cited |
| DevOps/release review | Release readiness and rollback | Deployment posture and rollback evidence cited |
| Data review | Schema, data exposure, migrations | Specific data risks and rollback path cited |

Reviews without cited evidence are context only and should not satisfy a gate.

## Registration Rule

When a new source becomes authoritative:
1. Add it here.
2. Link it from `README.md` or the relevant governance doc.
3. Record the promotion in `DECISION_LOG.md`.
