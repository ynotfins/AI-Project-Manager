# RUNBOOK.md

## Purpose

This runbook provides step-by-step operating procedures for Sparky's most common governance scenarios.

It is subordinate to:
- `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
- `README.md`
- `AGENTS.md`
- `WORKFLOWS.md`

Where `WORKFLOWS.md` defines the required operating model, this file provides the practical sequence to follow.

## RUN-01: Standard PR Governance

**Trigger:** A pull request or diff is submitted for Sparky evaluation.

1. Validate intake:
   - objective is present and scoped
   - owner is known
   - at least one inspectable artifact exists
   - requested action is explicit
2. Classify risk and surface:
   - work type
   - risk class
   - system surface
   - change posture
3. Verify routing:
   - identify required specialist lanes
   - confirm no self-certification bypass
4. Evaluate evidence:
   - retrieve artifacts
   - confirm version anchors
   - rate evidence quality
5. Check drift and rollback posture:
   - spec/code/behavior drift
   - rollback plan for medium risk and above
6. Issue decision using `PR_RULES.md`.
7. Record:
   - update `live/SESSION-STATE.md`
   - capture durable decision in `DECISION_LOG.md` if final

## RUN-02: Merge Gate Evaluation

**Trigger:** A reviewed work item requests merge authorization.

1. Re-read the prior review record.
2. Check for new commits since approval.
3. Confirm trust level and evidence still satisfy the risk class.
4. Verify every blocking condition is resolved with evidence.
5. Issue merge decision.
6. Record merge readiness or renewed block state.

## RUN-03: Release Gate Evaluation

**Trigger:** A release candidate requests deployment authorization.

1. Enumerate release scope.
2. Confirm included items already passed merge gate.
3. Verify rollback plan:
   - action
   - trigger
   - owner
4. Verify blast radius and observability expectations.
5. Check unresolved risks and ownership.
6. Issue release decision.
7. Record release outcome and next monitoring expectations.

## RUN-04: Incident Response Coordination

**Trigger:** A production incident is declared or detected.

1. Name and classify the incident.
2. Confirm an incident commander exists.
3. Route containment before optimization.
4. Require evidence for root-cause claims.
5. Apply accelerated but non-zero review standards to remediation changes.
6. Confirm resolution with observable proof.
7. Record incident outcome and required follow-up governance work.

## RUN-05: Context Reset Recovery

**Trigger:** Session reset, memory compaction, or generic-behavior recovery.

1. Read `BOOTSTRAP.md`.
2. Read `live/SESSION-STATE.md`.
3. Read recent `DECISION_LOG.md` entries.
4. Read `live/working-buffer.md`.
5. Promote any unresolved buffer entries.
6. Resume from the last recorded work item state rather than guessing.
