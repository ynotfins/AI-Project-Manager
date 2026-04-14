# Open Claw

A modular AI assistant platform for code, communication, and workflow automation.

Current status: Phase 2 (First Live Integration) is complete; runtime hardening and autonomous operations are active.

## Project structure

- `.cursor/rules/` — layered Cursor rules (global + project)
- `docs/ai/` — workflow docs, state tracking, planning, memory
- `open-claw/docs/` — project vision, requirements, modules, integrations
- `AGENTS.md` — agent operating contract

This execution repo is governed by `AI-Project-Manager` in the tri-workspace stack (`AI-Project-Manager` + `open--claw` + `droidrun`).

## Getting started

1. Open this folder in Cursor.
2. Create five chat tabs: PLAN / AGENT / DEBUG / ASK / ARCHIVE.
3. Paste the first prompts from `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` into each tab.
4. PLAN produces Phase 0; AGENT executes it.

## Docs

- `open-claw/docs/VISION.md` — what Open Claw is and why
- `open-claw/docs/REQUIREMENTS.md` — initial requirements
- `open-claw/docs/MODULES.md` — module boundaries
- `open-claw/docs/INTEGRATIONS.md` — target integrations
- `docs/ai/memory/MEMORY_CONTRACT.md` — memory persistence policy
