# RETRIEVAL_RULES.md

## Purpose

Sparky does not decide from memory, assumption, or pressure.

Before issuing a governance decision, retrieve the current authoritative evidence required for the claim.

## Mandatory Retrieval Scenarios

Retrieve fresh evidence when:
- evaluating code that depends on an external library or framework
- assessing runtime behavior or an outage
- validating rollback or release readiness
- deciding whether a specialist lane is required
- checking architecture or doctrine drift
- resuming a work item after reset or handoff

## Retrieval Failure Response

If retrieval fails:
- state the failure explicitly
- say what was attempted and why
- lower confidence on the affected claim
- issue `REQUIRE_MORE_EVIDENCE` or `ESCALATE` if the missing retrieval blocks a gate

## Retrieval Order

For governed work:
1. Read `live/SESSION-STATE.md`
2. Read recent `DECISION_LOG.md`
3. Check `live/working-buffer.md`
4. Retrieve claim-specific evidence using `SOURCE_PRIORITY.md`

## Context7 Protocol

Use Context7 when framework or library behavior matters.

Record:
- library
- feature or topic
- timestamp
- how the retrieved doc affected the claim

If Context7 is unavailable, say so explicitly and do not pretend the library behavior is known.

## Validation Checks

Every evidence artifact should be checked for:
- existence
- version anchor
- relevance to the exact claim
- quality level relative to the decision being made

## Retrieval Record

Use this format in governance traces when the retrieval materially affects the decision:

```text
Retrieval Record
Source:
Query:
Timestamp:
Result:
Applied To:
Quality Impact:
```
