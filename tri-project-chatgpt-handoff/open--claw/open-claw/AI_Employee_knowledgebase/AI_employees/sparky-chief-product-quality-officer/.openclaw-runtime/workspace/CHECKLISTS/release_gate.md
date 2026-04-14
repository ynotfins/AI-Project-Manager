# Release Gate Checklist

## Entry criteria
- release candidate exists
- release scope is defined
- responsible operator or owner is known

## Required evidence
- test status
- QA proof where applicable
- rollback path
- blast radius notes
- monitoring expectation
- unresolved risk list

## Questions
- what is being released
- what evidence proves readiness
- what is the rollback path and trigger
- who owns operational response if the release degrades
- what remains uncertain

## Stop conditions
- rollback is missing
- blast radius is unclear on meaningful change
- risky unresolved defect remains unowned
- release confidence rests on narrative rather than proof

## Escalation triggers
- production-sensitive change without clear operator
- security-sensitive release
- conflicting specialist readiness signals

## Completion criteria
- allow, block, or escalate decision recorded with reasons
