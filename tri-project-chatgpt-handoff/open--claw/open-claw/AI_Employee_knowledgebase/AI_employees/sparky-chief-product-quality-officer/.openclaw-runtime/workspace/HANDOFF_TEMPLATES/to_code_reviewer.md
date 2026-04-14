# Handoff Template: Code Reviewer

## Objective

Request independent code review for a work item that cannot be self-certified by its author.

## Routing Reason

Sparky has classified this work item as requiring an independent code reviewer. The author may not serve as the sole approver for this change.

## Current State

<!-- Fill in:
- Work item ID and title
- Risk classification: low | medium | high
- Change posture: additive | corrective | refactor | migration | hotfix
- System surface: UI | API | data | workflow | multi-surface
- What evidence has already been submitted (tests, QA, etc.)
- Current trust level
-->

## Evidence Attached

<!-- List all attached artifacts:
- Code diff (commit hash and PR link)
- Test results (specify version anchor: commit hash or build ID)
- Related issue or scoped objective
- Any prior review comments already addressed
-->

## Specific Review Focus Areas

<!-- Tell the reviewer what Sparky considers the highest-risk areas of this diff:
- Specific files or functions with behavior changes
- Claimed behavioral invariants to verify
- Known edge cases that should be covered
- Patterns that should be consistent with existing codebase
-->

## Known Evidence Gaps

<!-- List any gaps Sparky has already identified:
- Test coverage gaps for specific behavior claims
- Missing error handling
- Areas where the diff scope is wider than stated objective
- Potential drift from spec documents
-->

## What Code Reviewer Must Return

1. **Review scope confirmation:** which parts of the diff were reviewed
2. **Findings:** per-finding severity (low/medium/high/critical), description, and artifact reference
3. **Test adequacy assessment:** are the attached tests sufficient for the behavior being claimed?
4. **Drift check:** does the diff maintain consistency with existing patterns and spec?
5. **Decision:** ALLOW (reviewed, no blocking finding) | BLOCK (specific blocking findings listed) | REQUIRE_MORE_EVIDENCE (specific additional evidence needed before review can complete)

A review that says "looks good" without cited findings or confirmation of test adequacy is classified as T10 and does not satisfy the review gate.

## Return Condition to Sparky

Return when each of the five items above has been produced with specific citations.
Sparky will use this as T7 evidence for the review gate evaluation.
