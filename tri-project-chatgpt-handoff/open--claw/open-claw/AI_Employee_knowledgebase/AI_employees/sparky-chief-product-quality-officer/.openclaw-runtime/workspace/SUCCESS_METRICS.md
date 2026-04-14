# SUCCESS_METRICS.md

## Purpose

These metrics define what strong Sparky governance looks like in operation.

Success is not approval volume. Success is evidence-backed decisions that prevent weak work from escaping.

## Benchmark Table

| Metric | Target | Minimum Acceptable |
| --- | --- | --- |
| Weak PR block rate | >85% | >70% |
| False-positive block rate | <5% | <10% |
| Routing accuracy on first pass | >90% | >80% |
| Drift detected before merge | >80% | >60% |
| Evidence sufficiency on approved work | >90% | >80% |
| Trace completeness | 100% | 100% |
| Post-release incident escape rate on Sparky-approved work | <10% | <20% |

## Core Success Checks

### Blocking Precision
- Blocks should identify real governance gaps.
- Repeated overturned blocks indicate over-blocking or broken criteria.

### Evidence Coverage At Merge
- Approved work should carry evidence appropriate to its risk class.
- Any merge without adequate evidence is a governance failure.

### Routing Accuracy
- Work should reach the right specialist on first routing pass.
- Frequent reroutes indicate classification drift.

### Drift Detection
- Drift should be caught before merge whenever possible.
- Post-merge drift is a sign that review depth is insufficient.

### Trace Completeness
- An independent reviewer should be able to reconstruct the decision from the record.

### Release Escape Rate
- Track incidents on Sparky-approved work inside the first 72 hours after release.

## Failure Signals

Escalate for review if:
- blocks are frequently overturned as incorrect
- trace quality is high on paper but decisions still cannot be reconstructed
- release incidents remain high despite apparently strong review records
