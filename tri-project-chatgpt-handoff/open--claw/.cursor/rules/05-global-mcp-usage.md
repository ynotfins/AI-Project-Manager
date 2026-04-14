---
description: "MCP tool selection and No-Loss memory integration"
globs: ["**/*"]
alwaysApply: true
---

# 05 — Global MCP Usage Policy (strict)

AGENT must use the best available tool for the job. Manual approaches are fallbacks, never defaults.

## Preferred tools

| Category | Preferred tool | Fallback |
|---|---|---|
| Reasoning / analysis | thinking-patterns | Manual reasoning only if the user explicitly approves continuing without it |
| Code intelligence | serena | `rg`/`Glob`/`ReadFile` |
| External library docs | Context7 | Built-in WebSearch / WebFetch |
| Current web research | Exa Search | Built-in WebSearch |
| Web extraction | firecrawl-mcp | Built-in WebFetch |
| Browser verification | playwright | Manual browser / screenshot verification |
| UI generation / design scaffolding | Magic MCP | Hand-written scaffold |
| Repo operations | github | `gh` CLI via built-in `Shell` |
| Memory | openmemory | File-based in `docs/ai/memory/` |
| Phone automation | droidrun | Manual device interaction |

## Repo-first discipline

- Project docs and repo code are the authority for project-specific behavior.
- External tools supplement repo truth; they do not replace it.
- For the active repo, read internal docs/code first, then use external-doc tools only for outside dependencies or current public information.

## Mandatory tool triggers

### thinking-patterns — REQUIRED

Use `thinking-patterns` for:

- non-trivial PLAN work before finalizing the AGENT prompt: `sequential_thinking` by default unless another reasoning pattern is a better fit
- bug investigation, build failures, test failures, unexpected behavior: `debugging_approach`
- starting a new project, major feature, or large architecture change: `mental_model`
- cross-repo changes or changes affecting 3+ modules: `problem_decomposition`, `domain_modeling`, or `sequential_thinking`
- choosing between multiple implementation approaches: `decision_framework`
- critique, challenge, or assumption-checking passes: `critical_thinking` or `structured_argumentation`
- hypothesis-driven investigations: `scientific_method`

The old standalone `sequential-thinking` server remains removed. The `sequential_thinking` tool inside `thinking-patterns` is allowed. If `thinking-patterns` is unavailable for a task that requires structured reasoning, stop and notify the user.

### serena — REQUIRED when:

- locating symbols, references, or call paths
- editing more than one code file in a single phase
- reading a large code file
- understanding class/function relationships before changing code

### serena — activation protocol:

- Activate Serena by exact path on first access to the codebase actually in scope.
- Do not rely on dashboard names when switching between tri-workspace repos.
- Serena project map:
  - `D:/github/AI-Project-Manager`
  - `D:/github/open--claw`
  - `D:/github/open--claw/open-claw`
  - `D:/github/droidrun`
- If a path is missing from Serena, activate it by exact path immediately to register it.
- `D:/github/open--claw` repo root is the governance/docs Serena project; `D:/github/open--claw/open-claw` is the runtime Serena project.
- If the task is docs-only or the root in scope has no valid Serena project, declare Serena not applicable and use targeted `rg`/`Glob`/`ReadFile` work instead.
- If Serena is required but disabled, unavailable, or failing, stop and notify the user.

### Context7 — REQUIRED when:

- changing behavior that depends on a third-party API, framework, SDK, CLI, or cloud service
- adopting a new dependency or upgrading an existing one
- verifying correct usage of external library/framework APIs

Context7 is for external docs only. It must be constrained to the technologies relevant to the active repo. It is not a substitute for project docs.

### context-matic — CONDITIONAL

Use `context-matic` only for vendor API integration work when:

- the task is specifically about integrating with a third-party API or SDK
- repo docs and Context7 are not sufficient by themselves
- you need endpoint discovery, SDK-oriented integration steps, or generated guideline scaffolding

Preferred sequence:

1. `fetch_api`
2. `ask`
3. `add_guidelines` only if the workspace does not already contain the needed language guideline files

Do not use `context-matic` for general repo planning, business logic debugging, or as a substitute for Context7.

### Exa Search — REQUIRED when:

- current web research is needed beyond vendor docs
- Context7 cannot answer because the task depends on public examples, current ecosystem state, or broader web discovery

### firecrawl-mcp — REQUIRED when:

- scraping or extracting structured data from public web pages
- mapping a site before scraping specific pages
- collecting structured public-web evidence

Use only `firecrawl_scrape`, `firecrawl_map`, and `firecrawl_search`.

### playwright — REQUIRED when:

- verifying browser-based UI behavior after web/frontend changes
- capturing screenshots as evidence
- smoke-testing a dev server or live page where browser execution is part of acceptance

### Magic MCP — REQUIRED when:

- generating UI component scaffolds from design intent
- translating visual references into component structure
- producing design-system-oriented UI starting points

### github — REQUIRED when:

- creating, listing, or reviewing branches, pull requests, or issues
- managing releases or file operations via GitHub
- searching code or users across repositories

### openmemory — REQUIRED when:

- before planning: retrieve prior decisions and patterns related to the task
- after completing a phase: store new stable decisions or patterns

**Live Cursor reality:**

- The current tool surface is flat and thin:
  - `search-memories(query)`
  - `list-memories()`
  - `add-memory(content)`
- Do not claim `project_id`, `namespace`, or `memory_types` filters unless a proven wrapper exists in the active runtime.
- Use compact self-identifying memory text instead, for example:
  - `[repo=openclaw][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
  - `[repo=openclaw][kind=pattern][scope=worker-memory][source=MEMORY_PROMOTION_TEMPLATE.md] ...`

### droidrun — REQUIRED when:

- interacting with the user's phone
- testing mobile apps or checking device state
- automating phone actions

Use `phone_ping` before `phone_do` or `phone_apps`.

### obsidian-vault — CONDITIONAL

Use `obsidian-vault` only when the task explicitly needs operator notes or personal research already known to live in Obsidian.

**Role:**
- Fast-access scoped note-memory sidecar
- Prefer targeted note reads/searches over broad vault dumps
- Useful for operator notes, personal research, and quick-reference lookups already known to exist there

**Never treat it as canonical project state:**
- Not repo truth
- Not a replacement for OpenMemory
- Not default bootstrap context
- Not for agent operational state
- Not a replacement for `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, or `HANDOFF.md`

### filesystem — CONDITIONAL

Use `filesystem` when machine-local files outside the active repo are explicitly required, especially the non-canonical recovery bundle.

### Artiforge — CONDITIONAL

Use `Artiforge` only after the charter and repo authority docs are read, and only for synthesis or scaffold help. Its output is never authoritative.

## Tool management protocol

PLAN must include a `Required Tools` section in every AGENT prompt when specific MCP tools matter:

```text
Required Tools: [tool1, tool2]
Optional Tools: [tool3]
Safe to disable: [tool4, tool5]
```

Tool tiers:

- Core default-on: `openmemory`, `Context7`, `thinking-patterns`
- Code work: `serena`, `github`
- Research: `Exa Search`, `firecrawl-mcp`, `context-matic`
- UI/testing: `playwright`, `Magic MCP`
- Device/knowledge: `droidrun`, `obsidian-vault`, `filesystem`

## Required-tool failure policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Announce the failure immediately.
2. Name the exact tool and the exact failed step.
3. State why it is required for this task.
4. State whether a safe degraded-mode fallback exists.
5. If safe fallback exists, use it explicitly and record the evidence gap or memory reseed debt.
6. If safe fallback does not exist, stop and ask for restoration.
7. Record the incident in `docs/ai/STATE.md`.

Do not silently continue without a required high-value tool.
Do not pretend a disabled tool is active.

## Removed / unsupported toolchain

- `sequential-thinking` — removed as a standalone server; use `thinking-patterns.sequential_thinking` instead
- `shell-mcp` — removed; use built-in `Shell` when terminal access is required
- `extension-GitKraken` / GitKraken MCP — removed from the supported toolchain
- `googlesheets-tvi8pq-94` — removed from the supported toolchain
- `firestore-mcp` — removed from the supported toolchain

## Tool isolation model

- Serena depends on exact project activation and repo-local `project.yml`.
- Context7, Exa Search, Firecrawl, Playwright, and Magic are query-scoped: use them only when the active repo's task actually needs them.
- OpenMemory and other MCPs stay repo-aware through repo-local rules, prompts, and task framing.

## MCP configuration model

- Active MCP servers live in the single global config at `C:\Users\ynotf\.cursor\mcp.json`. No workspace-local `.cursor/mcp.json` files.
- Never hardcode secrets in committed repo files.
- MCP configuration is tooling plumbing, not product law.

## PASS/FAIL evidence for tool usage

AGENT must explicitly state for each MCP tool invocation:

- the exact tool name
- what it returned
- PASS if successful; FAIL if it errored

This evidence must appear in the execution block recorded in `docs/ai/STATE.md`.
