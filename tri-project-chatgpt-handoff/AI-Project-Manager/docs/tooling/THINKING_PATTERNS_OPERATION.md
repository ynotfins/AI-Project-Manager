# Thinking Patterns Operation

This is the active repo guidance for using the `thinking-patterns` MCP server without bloating context.

## Why This Server Matters

- It externalizes reasoning structure into tool schemas instead of long prompt instructions.
- It improves consistency for planning, debugging, and critique work.
- It is most valuable when the task is non-trivial, ambiguous, risky, or multi-step.

## Default Tool Mapping

| Situation | Use |
|---|---|
| multi-step planning, ambiguous task | `sequential_thinking` |
| phase/step breakdown | `problem_decomposition` |
| architecture, strategy, large refactor | `mental_model` |
| compare options or choose trade-offs | `decision_framework` |
| debugging or failure analysis | `debugging_approach` |
| challenge a draft plan or answer | `critical_thinking` |
| understand entities and constraints | `domain_modeling` |

## Low-Bloat Rule

- Use the MCP tools themselves as the reasoning structure.
- Do not paste or preload the large upstream manuals into PLAN or AGENT bootstrap context.
- Read only compact local policy plus tool schemas unless a specific tool example is needed.

## Schema Pre-Flight

Before complex nested calls:

1. verify required parameters
2. verify enums exactly
3. verify nested object shape
4. verify array item types
5. verify primitives are the correct types

## Source Pack

These temp-source documents were reviewed and distilled into this operating guide:

- `open--claw/temp/MCP-AGENT_RULES.mdc`
- `open--claw/temp/MCP_AGENT_RULES.md`
- `open--claw/temp/README.md`
- `open--claw/temp/SUMMARY.md`
- `open--claw/temp/SYSTEM_INTENT.md`
- `open--claw/temp/TOOL_REFERENCE.md`
- `open--claw/temp/CLAUDE.md`
- `open--claw/temp/EXAMPLES.md`
