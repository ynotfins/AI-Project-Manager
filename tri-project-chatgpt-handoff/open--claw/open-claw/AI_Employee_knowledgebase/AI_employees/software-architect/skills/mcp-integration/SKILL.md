---
name: mcp-integration
description: Pattern for designing and validating MCP integrations with typed parameters, descriptive tools, and graceful failure handling.
category: Development
roles:
  - mcp-integration-engineer
  - backend-architect
  - software-architect
---


# MCP Integration

## Status: READY

## Purpose
Extend agent capabilities with MCP servers that are understandable, secure, and genuinely usable by agents.

## Standards
- Tool names must be descriptive verb_noun phrases.
- Validate all inputs and return structured outputs.
- Use environment variables for secrets only.
- Keep tools stateless and single-purpose.
- Test real tool-call loops, not just unit tests.
