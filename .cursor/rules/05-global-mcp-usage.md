# 05 — Global MCP Usage Policy (strict)

AGENT must use installed MCP tools by name. Manual approaches are fallbacks, never defaults.

## Preferred MCP tools (by name)

| Category             | Preferred tool    | Fallback                                |
|----------------------|-------------------|-----------------------------------------|
| Reasoning / analysis | Clear Thought 1.5 | sequential-thinking, then manual        |
| Code intelligence    | serena            | Grep/glob + targeted file reads         |
| Documentation        | Context7          | Built-in WebSearch / WebFetch           |
| Web extraction       | firecrawl-mcp     | Built-in WebFetch                       |
| Repo operations      | github            | gh CLI via built-in Shell               |
| Memory               | openmemory        | File-based in `docs/ai/memory/`         |
| Phone automation     | droidrun          | Manual device interaction               |

AGENT must use the preferred tool by name. If it is unavailable, use the fallback and record a FAIL entry in `docs/ai/STATE.md`.

## Mandatory tool triggers

### Clear Thought 1.5 — REQUIRED operations by situation

Clear Thought 1.5 (`clear_thought`) is the **primary reasoning tool**. sequential-thinking is a fallback only.

| Situation | Operation (required) |
|---|---|
| Bug investigation, build failures, test failures, unexpected behavior | `debugging_approach` |
| Starting a new project, major feature, or large architectural change | `mental_model` |
| Cross-repo changes or changes affecting 3+ modules | `systems_thinking` |
| Choosing between multiple implementation approaches or trade-offs | `decision_framework` |
| Root cause analysis when a failure has multiple possible causes | `causal_analysis` |
| Complex multi-path problems with no obvious single solution | `tree_of_thought` |
| Optimizing performance, costs, or resource usage | `optimization` |
| Hypothesis-driven investigation (e.g., "is the crash caused by X or Y?") | `scientific_method` |
| Basic step-by-step reasoning with >5 steps | `sequential_thinking` (via Clear Thought) |
| Exploring new technologies or unfamiliar domains | `research` |

### sequential-thinking — FALLBACK only (use Clear Thought 1.5 first):
- When Clear Thought 1.5 is unavailable or returns an error
- Record the fallback as FAIL in `docs/ai/STATE.md`

### serena — REQUIRED when:
- Locating symbols, references, or call paths
- Editing more than one file in a single phase
- Reading a large file (must locate the target symbol first, not read the entire file)
- Understanding class/function relationships before making changes

### Context7 — REQUIRED before:
- Changing behavior that depends on a third-party API or library
- Adopting a new dependency or upgrading an existing one
- Verifying correct usage of any framework or library function

### firecrawl-mcp — REQUIRED when:
- Scraping or extracting structured data from web pages
- Mapping a site to discover URLs before scraping specific pages
- Searching the web for current technical content

**Active tools:** `firecrawl_scrape`, `firecrawl_map`, `firecrawl_search` only.
If a task requires `crawl`, `extract`, or `firecrawl_agent`, stop and ask the user to enable those tools in Cursor MCP settings before proceeding.

### github — REQUIRED when:
- Creating, listing, or reviewing branches, pull requests, or issues
- Managing releases or file operations via the hosting platform
- Searching code or users across repositories

### openmemory — REQUIRED:
- Before planning: call `search-memory` to retrieve prior decisions and patterns related to the current task
- After completing a phase: call `add-memory` to store new decisions, patterns, or stable facts
- See `docs/ai/memory/MEMORY_CONTRACT.md` for what must and must not be stored

### droidrun — REQUIRED when:
- Interacting with the user's phone (Samsung Galaxy S25 Ultra)
- Testing mobile apps or checking device state
- Automating phone actions (tap, type, navigate, read screen)

Use `phone_ping` to verify device is connected before any `phone_do` or `phone_apps` call.

## Disabled tool activation policy

The following tools are currently **disabled** to reduce context window consumption:
Exa Search, playwright, Magic MCP, filesystem_scoped, shell-mcp, firestore-mcp, googlesheets, Stripe, extension-GitKraken, cloudflare-bindings, cloudflare-builds, cloudflare-docs, cloudflare-observability.

If a task requires a disabled tool, AGENT must:
1. **Stop** — do not attempt to work around the missing tool silently
2. Explain which tool is needed and exactly why the task requires it
3. Ask the user to enable it in Cursor MCP settings
4. Wait for confirmation before proceeding
5. Record the blocker in `docs/ai/STATE.md`

Never silently skip or substitute a disabled tool that the task specifically requires.

## PASS/FAIL evidence for tool usage

AGENT must explicitly state for each MCP tool invocation:
- The **exact tool name** that was invoked (e.g., `clear_thought`, `serena`, `Context7`, `firecrawl_scrape`, `github`, `openmemory`)
- What it returned (brief summary)
- PASS if successful; FAIL if it errored

This evidence must appear in the execution block recorded in `docs/ai/STATE.md`.

## Failure and fallback policy

1. If a preferred tool fails: report **FAIL** immediately with the exact tool name and error.
2. Attempt the fallback listed in the "Preferred MCP tools" table above.
3. Record both the failed tool and the fallback used in `docs/ai/STATE.md`.
4. If the fallback is also insufficient: **stop** and surface the blocker to PLAN.
5. Never silently skip a tool — always announce degradation by name.

## Boundaries

- Never hardcode MCP server URLs, tokens, or configuration in repo files.
- MCP configuration lives outside the repo (IDE settings, environment).
- Rules enforce behavior, not plumbing.
