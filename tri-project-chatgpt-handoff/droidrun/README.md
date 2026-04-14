# Cursor Project Template

A clean, reusable template for Cursor-based development projects.

## What's included

- `.cursor/rules/` — layered rules (global + project)
- `docs/ai/` — workflow docs, state tracking, planning, memory
- `AGENTS.md` — agent operating contract
- `.gitignore` — sensible defaults

## Quick start

1. Copy this folder as the base for a new project.
2. Open in Cursor.
3. Create five chat tabs: PLAN / AGENT / DEBUG / ASK / ARCHIVE.
4. Paste the first prompts from `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` into each tab.
5. PLAN produces Phase 0; AGENT executes it.

## Rules structure

- **Global rules** (`00-*`, `05-*`): Broad, reusable across projects.
- **Project rules** (`10-*`, `20-*`): Project-specific, reference global rules.

## Memory

See `docs/ai/memory/MEMORY_CONTRACT.md` for the persistence policy.
