# SOURCE_PRIORITY.md

## Purpose

When sources conflict on a material claim, this file defines which one governs.

Priority is based on authority for the specific claim, not confidence or convenience.

## Priority Order

| Tier | Source Type | Applies To |
| --- | --- | --- |
| T1 | Live runtime observation with timestamps | Behavior and runtime state claims |
| T2 | Current version-anchored test results | Behavior correctness claims |
| T3 | Current authoritative doctrine | Governance compliance and operating rules |
| T4 | Context7 library documentation | External API and library behavior |
| T5 | Reviewed architecture and design docs | Architecture compliance |
| T6 | Security or domain-specialist signed review with evidence | Security and specialist claims |
| T7 | Independent code review with citations | Code correctness claims |
| T8 | Prior committed Sparky records | Continuity and prior decisions |
| T9 | Specialist assertions with cited evidence but no formal sign-off | Contextual technical claims |
| T10 | Assertions without cited evidence | Context only |
| T11 | Narrative descriptions without artifacts | Lowest-confidence context only |

## T3 Charter Rule

Within T3, not all doctrine is equal:
1. `FINAL_OUTPUT_PRODUCT.md` is supreme.
2. `README.md`, `AGENTS.md`, `WORKFLOWS.md`, and `AUDIT.md` define the live packet core.
3. `RUNBOOK.md`, `APPROVAL_GATES.md`, `PR_RULES.md`, `SOURCE_PRIORITY.md`, `RETRIEVAL_RULES.md`, `KNOWLEDGE_SOURCES.md`, `CHECKLISTS/`, and `HANDOFF_TEMPLATES/` are subordinate operational support surfaces.

If a support surface conflicts with the charter or live packet core, the higher layer governs and the lower file must be corrected.

## Conflict Rules

1. Higher tier wins.
2. Same-tier conflict requires escalation or further retrieval.
3. Current lower-tier evidence may outrank stale higher-tier evidence when the higher-tier source predates a material change, but the stale source must then be flagged for update.
4. Re-labeling a weak source does not increase its tier.

## Minimum Requirements

### T1 runtime observations
- timestamp
- environment or version context
- observable output

### T2 tests
- suite or command
- version anchor
- pass/fail result

### T4 Context7 retrieval
- library
- retrieved topic
- timestamp

### T6/T7 reviews
- reviewer identity
- scope reviewed
- evidence cited

Without those fields, downgrade the source.
