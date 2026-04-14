# PR_RULES.md

## Purpose

A PR is a decision packet, not just a code bundle.

Sparky evaluates whether the change is safe, scoped, owned, and evidenced well enough for its risk class.

## Required PR Fields

- objective
- scope
- owner
- evidence list
- test reference or explicit test gap
- rollback note for medium risk and above
- drift note or explicit `not applicable`

## Evaluation Sequence

1. Validate scope against the stated objective.
2. Reclassify risk if Sparky's classification is higher.
3. Evaluate evidence quality.
4. Confirm required specialist lanes are complete.
5. Check for drift.
6. Check rollback posture when applicable.
7. Record the governance trace before issuing the final decision.

## Blocking Conditions

Sparky blocks a PR when:
- scope is materially wider than declared
- a required specialist lane is missing
- evidence quality is below the risk threshold
- rollback is required but missing
- high-severity drift is unresolved
- a prior block was bypassed without satisfying the listed conditions

## PR Block Format

```text
PR BLOCKED: [work item]
Risk Class:
Trust Level:

Blocking Conditions:
1.
2.

Unblock Requirements:
- evidence required
- re-evaluation required

Trace ID:
```

## PR Approval Format

```text
PR APPROVED: [work item]
Risk Class:
Trust Level:
Evidence Summary:
Gate Results:
Drift Assessment:
Rollback Status:
Reviewer Lanes:
Trace ID:
Next Action:
```
