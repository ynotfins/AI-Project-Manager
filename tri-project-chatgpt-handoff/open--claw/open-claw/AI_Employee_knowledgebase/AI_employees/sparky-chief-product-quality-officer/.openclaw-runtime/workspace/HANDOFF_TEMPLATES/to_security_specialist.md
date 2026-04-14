# Handoff Template: Security Specialist

## Objective

Request security review for a change that affects authentication, authorization, access control, data exposure, encryption, or session management.

## Routing Reason

Sparky has classified this work item as security-surface. Independent security specialist review is required before this item can advance past the review gate. Sparky cannot substitute for security specialist review.

## Current State

<!-- Fill in:
- Work item ID and title
- Risk classification: high | critical
- Specific security surface(s) affected: authentication | authorization | session | token | encryption | data-exposure | input-validation | multi-tenant-isolation | other
- What has already been reviewed (code review, architecture review, etc.)
- Trust level at routing time
-->

## Evidence Attached

<!-- List all attached evidence:
- Code diff (commit hash or PR link)
- Test results relevant to the security surface
- Architecture context (service boundaries, trust zones)
- Prior security review if any (cite which version)
- Dependency version information (if CVEs are relevant)
-->

## Specific Security Questions Requiring Answer

<!-- Be specific. Do not ask "is this secure?"
Examples:
- Does the modified authentication middleware correctly reject tokens that have been revoked post-issue?
- Can a user with role X access data belonging to user with role Y through the modified API endpoint?
- Does the updated encryption implementation handle key rotation without exposing plaintext during the transition?
-->

## Known Risk Signals

<!-- List what Sparky observed that triggered security routing:
- Changed file paths (e.g., auth/, middleware/, session/)
- Modified claims or token validation logic
- New API endpoints with authorization scope
- Dependency change touching a security library
- Other signals
-->

## What Security Specialist Must Return

To unblock this item, the security specialist must return:

1. **Finding summary:** what was reviewed, what was found
2. **Per-surface confirmation:** explicit confirmation or finding for each security surface listed above
3. **Evidence cited:** what specific code paths, tests, or observations support each conclusion
4. **Residual risk statement:** if any accepted risk remains, named owner and mitigation
5. **Decision:** ALLOW (cleared), BLOCK (specific finding), or ESCALATE (requires higher authority)

A response that says "it looks fine" without citing specific controls verified is classified as T10 evidence and does not satisfy this gate.

## Return Condition to Sparky

Return when:
- All listed security surfaces have been explicitly evaluated
- Each evaluation is supported by cited evidence
- A clear decision (ALLOW / BLOCK / ESCALATE) is produced

Sparky will re-evaluate at the review gate using the security specialist output as T6 evidence.
