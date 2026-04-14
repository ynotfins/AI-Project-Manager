---
description: "Modular architecture, diff/testing/secrets hygiene"
globs: ["**/*"]
alwaysApply: true
---

# 20 — Project Quality Standards (Open Claw)

> Extends: `00-global-core.md`, `05-global-mcp-usage.md`

## Project notes

Open Claw modules (orchestrator, memory, dev, comms, web) must remain decoupled.
Each module should have a clear interface boundary. Cross-module calls go through
the orchestrator, not direct imports.

## Modular architecture

- Separate concerns: orchestrator / memory / dev / comms / web / utils / types.
- Favor composable functions and service classes.
- No monolithic or inline procedural logic beyond ~20 lines in a single block.
- Module boundaries are defined in `open-claw/docs/MODULES.md`.

## Diff discipline

- Prefer small, focused diffs.
- Avoid broad reformatting in the same commit as logic changes.
- Each phase should end with a commit (or explicit justification why not).

## Testing

- Add tests with changes (unit and integration as appropriate).
- Run tests before marking a phase complete.

## Input validation

- Validate inputs at system boundaries.
- Prefer strict typing and explicit error handling.

## Secrets policy

- Never commit `.env*`, credentials, tokens, or service-account JSON.
- Reference `docs/ai/memory/MEMORY_CONTRACT.md` for what to persist vs. omit.
- If a secret is needed, document a pointer (e.g., "API key in 1Password: OpenClaw/Key") — never the value.

## Dependency hygiene

- Pin versions once stable.
- Document upgrades in commit messages.
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
