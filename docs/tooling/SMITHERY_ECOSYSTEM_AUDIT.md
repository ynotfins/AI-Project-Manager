# Smithery Ecosystem Audit

Last updated: 2026-04-08

## Purpose

Evaluate whether Smithery-managed MCP servers should replace, supplement, or remain separate from the current directly configured MCP stack.

## Executive Summary

Smithery is valuable as:

- a discovery/index layer
- a managed connection layer for OAuth-heavy or externally hosted MCPs
- a place to evaluate alternative implementations

Smithery should **not** currently become the single critical dependency for the tri-workspace's highest-priority infrastructure servers.

Reason:

- the system already depends on multiple external services
- critical memory/governance tools must be as direct and debuggable as possible
- Smithery itself showed instability during this audit (`docs.smithery.ai` returned `503`)

Recommended stance:

- keep the current direct/global MCP stack for critical infrastructure
- use Smithery selectively for discovery, evaluation, and optional specialized servers

## Clear Thought Findings

### Variants observed

From screenshots and web research:

- `@waldzellai/clear-thought` / Clear Thought 1.5
- `@ThinkFar/clear-thought-mcp`
- other community variants

### Comparison

| Variant | Evidence | Assessment |
|---|---|---|
| WaldzellAI Clear Thought 1.5 | screenshots, installed tool schema, Smithery page | strongest fit |
| ThinkFar Clear Thought Server | screenshot shows older multi-tool style | likely useful, but narrower/older model |
| sequential-thinking style servers | historical baseline only | too narrow for current system needs |

### Why WaldzellAI wins

- unified reasoning surface
- broad operation set (systems, debugging, decision, research, simulation, graph-style reasoning)
- better fit for governance + architecture + debugging + planning in one server
- replaces `sequential-thinking` with a more capable reasoning platform instead of just a like-for-like clone

Decision:

- keep the current WaldzellAI Clear Thought path as the primary reasoning server
- do not revert to a single-purpose sequential-thinking replacement

## Server-by-Server Smithery Position

| Server | Current path | Smithery value | Recommended action |
|---|---|---|---|
| Clear Thought 1.5 | direct/global (`waldzellai`) | useful for discovery/comparison, but current direct path is already the right family | keep current |
| OpenMemory | direct via local proxy | Smithery adds another failure layer on top of an already fragile upstream | keep direct/local |
| Serena | direct `uvx` | Smithery listing exists, but local exact-path behavior is more important than marketplace mediation | keep direct |
| Context7 | direct hosted endpoint | already purpose-built and stable enough | keep direct |
| Exa Search | direct hosted endpoint | Smithery may help discover variants, but direct is clean | keep direct |
| Firecrawl | direct npm/stdIO | Smithery optional only | keep direct |
| Playwright | direct npm/stdIO | direct path simpler | keep direct |
| Magic MCP | direct npm/stdIO | optional via Smithery only if it adds auth/session advantages | keep direct |

## Smithery-Specific Opportunity Areas

Smithery may still be worth using for:

- optional OpenClaw ecosystem servers like `openclaw-direct`, `openclaw-intel`, `clawnet`
- experimentation with connection-managed remote servers
- evaluating better hosted variants before promoting them into the core stack

### OpenClaw ecosystem servers observed

From screenshot evidence:

- `openclaw-direct/openclaw`
- `openclaw-ai/intel`
- `xmintl/claw-net`

These are interesting as optional business/system extensions, not as replacements for the core governance-memory-tooling substrate.

## Screenshot Evidence Summary

Screenshots preserved at:

- `docs/screenshots/2026-04-08-post-restart/`

Observed:

- Clear Thought 1.5 page under WaldzellAI family
- ThinkFar Clear Thought page with older multi-tool presentation
- mem0 dashboard showing requests, memories, API keys, billing, and plugin/SDK install flows
- Smithery connection dashboard showing at least one existing connection object
- OpenClaw ecosystem servers (`openclaw-direct`, `openclaw-intel`, `clawnet`) on Smithery

## Current Recommendation

1. Keep core infrastructure direct.
2. Use Smithery as a research and optional expansion layer.
3. Revisit Smithery-managed replacements only if they provide a concrete advantage:
   - better auth/session management
   - higher uptime than the direct version
   - materially better tool surface
   - easier cross-platform deployment
