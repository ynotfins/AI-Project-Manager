# Software Architect Audit

## Grade
- **Current grade:** A-

## Role Snapshot
- **Slug:** `software-architect`
- **Title:** Software Architect
- **Manager:** `sparky-chief-product-quality-officer`
- **Status:** Strong curated packet, not yet live-runtime validated

## What This Employee Can Do Now
- Prefer reversible, low-complexity designs over architecture theater.
- Choose system boundaries, integration contracts, and failure handling patterns.
- Create ADRs that explain why a direction was chosen.
- Protect modularity across ui, domain, data, and utils layers.

## Assigned Skills
- `architecture-adr`
- `mcp-integration`
- `release-readiness`

## Tool Expectations
- repo search
- diagramming
- ADR docs
- Context7 docs

## Collaboration Fit
- Provide implementation guidance to `frontend-developer`, `backend-architect`, and `mcp-integration-engineer`.
- Escalate risk and simplification recommendations to `sparky-chief-product-quality-officer`.

## Missing Before High-Level Runtime Readiness
- Not yet wrapped into the live `open-claw/employees` runtime packet layout with Docker and bot wiring.
- Tool access is documented, but not yet proven end-to-end against the real worker runtime and installed integrations.
- No per-role activation smoke test has been recorded yet for the current OpenClaw/CrewClaw deployment path.
- No full clone-and-rebrand rehearsal has been executed yet with this packet as the primary operator.
- Needs a packaging pattern that maps the curated architecture standard into the CrewClaw/OpenClaw runtime shell.
- Needs a reference implementation for modular boundaries inside a real starter repo.

## Verdict
Use this packet as part of the authoritative standard now. Before treating it as a fully autonomous live worker, pair it with runtime packaging, real tool-entitlement proof, and a recorded smoke test.
