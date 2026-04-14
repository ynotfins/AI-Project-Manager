description: "MCP tool selection, recovery triggers, degraded-tool handling, and flat OpenMemory discipline"
globs: ["**/*"]
alwaysApply: true
---

# 05 — Global MCP Usage Policy (strict)

AGENT must use the best available tool for the job. Manual approaches are fallbacks, never defaults.

## Preferred tools

| Category | Preferred tool | Fallback |
|---|---|---|
| Reasoning / analysis | thinking-patterns | Manual reasoning only when the task can still be completed safely after a documented tool failure |
| Code intelligence | serena | `rg`/`Glob`/`ReadFile` |
| External library docs | Context7 | Built-in WebSearch / WebFetch |
| Current web research | Exa Search | Built-in WebSearch |
| Web extraction | firecrawl-mcp | Built-in WebFetch |
| Browser verification | playwright | Manual browser / screenshot verification |
| UI generation / design scaffolding | Magic MCP | Hand-written scaffold |
| Repo operations | github | `gh` CLI via built-in `Shell` |
| Durable memory | openmemory | Recovery bundle + repo memory docs when degraded mode is explicitly allowed |
| Phone automation | droidrun | Manual device interaction |
| Operator notes | obsidian-vault | Repo docs or user-provided notes |
| Recovery bundle files | filesystem | Built-in file tools for repo files only |
| Synthesis / scaffold drafts | Artiforge | Hand-written draft after canonical reads |

## Repo-first discipline

- The product charter and repo-tracked rules/docs are the authority.
- External tools supplement repo truth; they never replace it.
- Use tools in the recovery order defined by `10-project-workflow.md` and `docs/ai/memory/MEMORY_CONTRACT.md`.

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

- before PLAN, AGENT, or DEBUG reconstructs prior context for a non-trivial task
- after validated durable decisions, patterns, debug findings, or recovery-policy changes are produced
- when ARCHIVE promotes durable conclusions out of `STATE.md`, `HANDOFF.md`, or worker packets
- after every meaningful execution block that refreshes the recovery bundle

**Live Cursor reality:**

- The current tool surface is flat and thin:
  - `search-memories(query)`
  - `list-memories()`
  - `add-memory(content)`
- Do not claim `project_id`, `namespace`, `memory_types`, or direct filter support unless a proven wrapper exists in the active runtime.
- Use compact self-identifying memory text instead, for example:
  - `[repo=ai-pm][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
  - `[repo=openclaw][kind=pattern][scope=worker-memory][source=MEMORY_PROMOTION_TEMPLATE.md] ...`

### obsidian-vault — CONDITIONAL

Use `obsidian-vault` only when the task explicitly needs operator notes or personal research already known to live in Obsidian.

Do not call it just because a prompt mentions prior work, previous decisions, docs, architecture, notes, memory, or background. In this repo, Obsidian is sidecar-only and never part of the default bootstrap path.

**Role:**

- Fast-access sidecar memory
- Prefer targeted reads/searches over vault-wide dumps
- Useful for operator notes, personal research, and quick-reference lookups

**Never treat it as canonical project state:**

- Not repo truth
- Not a replacement for OpenMemory
- Not default bootstrap context
- Not a replacement for `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, or `HANDOFF.md`

If `obsidian-vault` fails:

- do not retry aggressively
- do not block execution
- write the pending sidecar summary into `docs/ai/recovery/session-summary.md`
- mark `obsidian_sync: pending`
- flush the pending summary into Obsidian on the next successful `obsidian-vault` availability

### filesystem — REQUIRED when:

- reading the recovery bundle before broad repo reads
- writing the recovery bundle after meaningful execution

Concrete AI-PM recovery bundle paths:

- `docs/ai/recovery/current-state.json`
- `docs/ai/recovery/session-summary.md`
- `docs/ai/recovery/active-blockers.json`
- `docs/ai/recovery/memory-delta.json`

Do not use it to redefine repo truth. Recovery-bundle contents are a speed layer only.

### Artiforge — CONDITIONAL

Use `Artiforge` only after the charter, repo authority contract, and any required recovery docs are read.

Use it for:

- synthesis drafts
- scaffold generation
- structured summaries that will still be reviewed against repo rules

Never use Artiforge output as policy authority or as a substitute for canonical repo docs.

### droidrun — REQUIRED when:

- interacting with the user's phone
- testing mobile apps or checking device state
- automating phone actions

Use `phone_ping` before `phone_do` or `phone_apps`.

## Tool management protocol

PLAN must include a `Required Tools` section in every AGENT prompt:

```
Required Tools: [tool1, tool2]
Optional Tools: [tool3]
Safe to disable: [tool4, tool5]
```

Tool tiers for context optimization:

| Tier | Servers | When to enable |
|------|---------|---------------|
| Core default-on | openmemory, Context7, thinking-patterns | Every session where the tools are available |
| Code tasks | serena, github | Any code or multi-file config changes |
| Research | Exa Search, firecrawl-mcp, context-matic | Web research or third-party API integration work |
| UI/Testing | playwright, Magic MCP | UI work, browser verification |
| Device/knowledge | droidrun, obsidian-vault, filesystem, Artiforge | Only when the task explicitly needs them |

Default recommendation: keep the core default-on tier stable and enable the on-demand tiers only when the active task requires them.

## Required-tool failure policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Announce the failure immediately. Never continue silently.
2. Name the exact tool and the exact failed step.
3. State why the tool is required for this task.
4. State whether a safe degraded-mode fallback exists for this task.
5. If safe fallback exists, use it explicitly and record the resulting evidence gap or memory reseed debt.
6. If safe fallback does not exist, stop and ask the user to restore the tool.
7. Record the incident in `docs/ai/STATE.md`.

Examples:

- `openmemory` degraded during recovery: announce FAIL, use the recovery bundle plus repo docs if the task remains satisfiable, then record reseed debt
- `thinking-patterns` degraded for architecture work: stop normal flow and restore it before proceeding
- `serena` degraded during docs-only work: mark not applicable instead of pretending it was required
- `obsidian-vault` degraded during sidecar sync: record FAIL, store the pending sidecar summary in `docs/ai/recovery/session-summary.md`, mark `obsidian_sync: pending`, and continue without blocking canonical work

## Removed / unsupported toolchain

- `sequential-thinking` — removed as a standalone server; use `thinking-patterns.sequential_thinking` instead
- `shell-mcp` — removed; use built-in `Shell`
- `extension-GitKraken` / GitKraken MCP — removed (extension uninstalled)
- `googlesheets-tvi8pq-94` — removed
- `firestore-mcp` — removed

## MCP configuration model

- Active MCP servers live in the single global config at `C:\Users\ynotf\.cursor\mcp.json`.
- No workspace-local `.cursor/mcp.json` files. The earlier split caused duplicate tool loading.
- Never hardcode secrets in committed repo files.
- Secrets are injected at runtime via `bws run`.

## No-Loss memory integration

See `docs/ai/architecture/NO_LOSS.md`, `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`, and `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`.

- OpenMemory is the primary durable structured recall layer.
- The filesystem recovery bundle in `docs/ai/recovery/` is the non-canonical speed layer when a reboot or crash would otherwise force broad file rereads.
- `STATE.md` and `HANDOFF.md` are operational evidence, not the first authority reads.
- Context7 outputs are not durable project memory unless they lead to a validated project decision documented in repo docs.

## Tool output discipline

When a tool returns a large response:

1. Extract the relevant facts only
2. Store durable facts in OpenMemory using the compact self-identifying text convention when the current runtime supports storage
3. Do not paste full tool outputs into `STATE.md` or `HANDOFF.md`
4. Reference canonical docs or the recovery bundle, not imaginary metadata fields

## PASS/FAIL evidence for tool usage

AGENT must explicitly state for each MCP tool invocation:

- the exact tool name
- what it returned (summary, not full output)
- PASS if successful; FAIL if it errored

This evidence must appear in the execution block recorded in `docs/ai/STATE.md`.
