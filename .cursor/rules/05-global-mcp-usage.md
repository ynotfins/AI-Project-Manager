# 05 — Global MCP Usage Policy (strict)

AGENT must use installed MCP tools by name. Manual approaches are fallbacks, never defaults.

## Preferred MCP tools (by name)

| Category              | Preferred tool         | Fallback                                      |
|-----------------------|------------------------|-----------------------------------------------|
| Reasoning / planning  | sequential-thinking    | Break into sub-steps manually; record in PLAN |
| Code intelligence     | serena                 | Grep/glob + targeted file reads               |
| Documentation         | Context7               | Web search or manual doc fetch                 |
| Browser automation    | playwright             | Manual screenshot + describe                   |
| UI generation         | Magic MCP              | Hand-write component scaffold                  |
| Web extraction        | firecrawl-mcp          | Manual fetch + parse                           |
| Repo operations       | github                 | CLI git + manual hosting UI                    |
| Web search            | Exa Search             | Manual search                                  |
| Memory                | openmemory             | File-based memory in `docs/ai/memory/`         |

AGENT must use the preferred tool by name. If it is unavailable, use the fallback and record a FAIL entry in `docs/ai/STATE.md`.

## Mandatory tool triggers

### sequential-thinking — REQUIRED when:
- The task has >5 connected steps
- The change spans multiple files
- The task involves migrations or refactors
- A bug is ambiguous with multiple hypotheses

### serena — REQUIRED when:
- Locating symbols, references, or call paths
- Editing more than one file in a single phase
- Reading a large file (must locate the target symbol first, not read the entire file)
- Understanding class/function relationships before making changes

### Context7 — REQUIRED before:
- Changing behavior that depends on a third-party API or library
- Adopting a new dependency or upgrading an existing one
- Verifying correct usage of any framework or library function

### playwright — REQUIRED when:
- Verifying UI or web behavior after frontend changes
- Testing web-based workflows end-to-end
- Capturing screenshots or accessibility snapshots for evidence

### Magic MCP — REQUIRED when:
- Creating new UI components from natural-language descriptions
- Translating UI screenshots or specs into component scaffolds
- Generating design-system-consistent UI blocks
- Converting wireframes into code skeletons

### firecrawl-mcp — REQUIRED when:
- Scraping or extracting structured data from web pages
- Crawling a site to discover URLs before scraping specific pages

### github — REQUIRED when:
- Creating, listing, or reviewing branches, pull requests, or issues
- Managing releases or file operations via the hosting platform
- Searching code or users across repositories

### Exa Search — REQUIRED when:
- Context7 cannot answer a library or framework question
- Searching for current information, news, or technical content across the web
- Finding code examples or documentation not covered by Context7

### openmemory — REQUIRED:
- Before planning: call `search-memory` to retrieve prior decisions and patterns related to the current task
- After completing a phase: call `add-memory` to store new decisions, patterns, or stable facts
- See `docs/ai/memory/MEMORY_CONTRACT.md` for what must and must not be stored

## PASS/FAIL evidence for tool usage

AGENT must explicitly state for each MCP tool invocation:
- The **exact tool name** that was invoked (e.g., "serena", "Context7", "sequential-thinking", "firecrawl-mcp", "github", "Exa Search")
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
