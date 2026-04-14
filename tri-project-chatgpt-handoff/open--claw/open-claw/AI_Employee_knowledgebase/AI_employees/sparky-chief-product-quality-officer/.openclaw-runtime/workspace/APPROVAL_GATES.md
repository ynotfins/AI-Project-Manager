# APPROVAL_GATES.md

## Purpose

This file defines the gate criteria for the Sparky governance pipeline.

Gate passage is explicit. A later gate does not erase a failure in an earlier one.

## Stage Sequence

`INTAKE -> ROUTING -> REVIEW -> MERGE -> RELEASE`

## Intake Gate

Required:
- scoped objective
- named owner
- declared requested action
- inspectable artifact

Failure response:
- `DEFER` for missing basics
- `BLOCK` for bypass attempts

## Routing Gate

Required:
- risk classification
- system surface identification
- required specialist lanes named
- no self-certification bypass

Failure response:
- `BLOCK` for missing specialist lanes
- `ESCALATE` for unresolved ambiguity

## Review Gate

Required:
- relevant tests or runtime proof
- independent review where applicable
- drift assessment
- rollback posture for medium risk and above

Failure response:
- `REQUIRE_MORE_EVIDENCE` for missing proof
- `BLOCK` for missing mandatory specialist review

## Merge Gate

Required:
- prior gates passed
- evidence quality appropriate to risk
- blocking conditions resolved
- governance trace complete

Failure response:
- `BLOCK`

## Release Gate

Required:
- merge gate complete for all included changes
- rollback plan with action, trigger, owner
- blast radius documented
- observability expectation declared
- unresolved risks named and owned

Failure response:
- `BLOCK` or `REQUIRE_MORE_EVIDENCE`, depending on what is missing

## Audit Rule

Every gate decision should record:
- gate name
- work item
- timestamp
- conditions checked
- evidence used
- final outcome
