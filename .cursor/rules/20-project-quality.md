# 20 — Project Quality Standards

> Extends: `00-global-core.md`, `05-global-mcp-usage.md`

## Modular architecture

- Separate concerns where applicable: auth / data / api / ui / utils / types.
- Favor composable functions and service classes.
- No monolithic or inline procedural logic beyond ~20 lines in a single block.

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
- If a secret is needed, document a pointer (e.g., "API key in 1Password: Project/Key") — never the value.

## Dependency hygiene

- Pin versions once stable.
- Document upgrades in commit messages.
- Use a docs MCP tool to verify library APIs before adopting new versions.
