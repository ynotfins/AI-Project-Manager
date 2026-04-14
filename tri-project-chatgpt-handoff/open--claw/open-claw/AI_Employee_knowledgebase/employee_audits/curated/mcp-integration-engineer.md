# MCP Integration Engineer Audit

## Grade
- **Current grade:** A-

## Role Snapshot
- **Slug:** `mcp-integration-engineer`
- **Title:** MCP Integration Engineer
- **Manager:** `software-architect`
- **Status:** Strong curated packet, not yet live-runtime validated

## What This Employee Can Do Now
- Define descriptive tool names, typed parameters, and structured outputs.
- Prefer stateless, single-responsibility tools with clear error messages.
- Expose resources and prompts that help agents act with context.
- Test integrations with real agent loops before calling them ready.

## Assigned Skills
- `mcp-integration`
- `architecture-adr`
- `handoff-state`

## Tool Expectations
- MCP SDK
- TypeScript
- Python
- Context7 docs

## Collaboration Fit
- Coordinate with `backend-architect` and `software-architect` on contracts.
- Provide new capabilities to the broader team with docs and examples.

## Missing Before High-Level Runtime Readiness
- Not yet wrapped into the live `open-claw/employees` runtime packet layout with Docker and bot wiring.
- Tool access is documented, but not yet proven end-to-end against the real worker runtime and installed integrations.
- No per-role activation smoke test has been recorded yet for the current OpenClaw/CrewClaw deployment path.
- No full clone-and-rebrand rehearsal has been executed yet with this packet as the primary operator.
- Needs a live entitlement matrix showing which runtime workers can reach which tools safely.
- Needs a standard fallback plan for missing tools so worker quality does not collapse when an integration is unavailable.

## Verdict
Use this packet as part of the authoritative standard now. Before treating it as a fully autonomous live worker, pair it with runtime packaging, real tool-entitlement proof, and a recorded smoke test.
