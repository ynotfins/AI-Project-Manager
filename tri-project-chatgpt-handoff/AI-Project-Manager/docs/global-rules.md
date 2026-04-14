# Global Rules Reference

> Status note (2026-03-19): This file is a historical/generated reference snapshot.
> Canonical active behavior is defined by `.cursor/rules/*.md` and `AGENTS.md`.
> If content here conflicts with active rules, treat this document as non-authoritative.

All active Cursor rules across the global user scope (`~/.cursor/rules/`) and this project (`.cursor/rules/`).

**Generated:** 2026-02-23
**Source:** `C:\Users\ynotf\.cursor\rules\` + `D:\github\AI-Project-Manager\.cursor\rules\`

---

## Table of Contents

### Global Rules (`~/.cursor/rules/`)
| Rule File | Description | Always Applied |
|---|---|---|
| [auto-error-fixing](#auto-error-fixing) | Automatically fix errors when detected | Yes |
| [autonomous-rule-creation](#autonomous-rule-creation) | Automatically create rules from user feedback | Yes |
| [coding-standards](#coding-standards) | Python coding standards and style guidelines | No (Python files only) |
| [core](#core) | Core operational modes (Plan / Act) | Yes |
| [decisive-implementation](#decisive-implementation) | Make decisive technical choices and implement immediately | Yes |
| [enhance-documentation](#enhance-documentation) | Enhance documentation automatically for Python code | No (Python files only) |
| [fetch-rules](#fetch-rules) | Mandatory rule fetching before every action | Yes |
| [memory-bank-instructions](#memory-bank-instructions) | Memory Bank structure and cross-session continuity | Yes |
| [post-task-cleanup](#post-task-cleanup) | Clean up automatically after completing tasks | Yes |
| [proactive-completion](#proactive-completion) | Complete partial implementations proactively | Yes |
| [proactive-scanning](#proactive-scanning) | Scan for issues proactively and fix them | Yes |
| [rule-visibility](#rule-visibility) | Display applied rules at each AI action for transparency | Yes |
| [rules-location](#rules-location) | All rules are located in .cursor/rules directory | Yes |
| [smart-assumptions](#smart-assumptions) | Make intelligent assumptions to maintain workflow momentum | Yes |
| [yolo](#yolo) | YOLO mode — execute without confirmation when triggered | No |

### Project Rules (`.cursor/rules/`)
| Rule File | Description |
|---|---|
| [00-global-core](#00-global-core) | Non-negotiable tab separation, evidence-first, PASS/FAIL discipline |
| [05-global-mcp-usage](#05-global-mcp-usage) | Strict MCP tool usage policy with fallback chain |
| [10-project-workflow](#10-project-workflow) | PLAN/AGENT/DEBUG execution contracts |
| [20-project-quality](#20-project-quality) | Engineering standards: modularity, testing, secrets, diffs |

---

## Global Rules

---

### auto-error-fixing

**File:** `~/.cursor/rules/auto-error-fixing.mdc`
**Always applied:** Yes

When errors are detected, fix them immediately without asking.

**Auto-fix these errors:**
- Syntax errors
- Missing imports
- Undefined variables (infer or import)
- Type errors (add type hints or fix types)
- Linter errors
- Formatting issues

**After fixing:**
- Briefly state what was fixed
- Continue with the original task

---

### autonomous-rule-creation

**File:** `~/.cursor/rules/autonomous-rule-creation.mdc`
**Always applied:** Yes

Create a new rule in `.cursor/rules` whenever user feedback is received:
- Extract the main point of the feedback
- Create a new rule that captures this as a reusable instruction
- Save the new rule with a short, descriptive name
- Keep rules simple and avoid redundancy

Apply for every edit or create rule.

---

### coding-standards

**File:** `~/.cursor/rules/coding-standards.mdc`
**Always applied:** No — applies to `**/*.py` only

Python-specific coding standards:
- Use 4 spaces for indentation
- Maximum line length of 88 characters
- Follow PEP 8 naming conventions
- Use descriptive variable and function names
- Add docstrings for all functions and classes
- Imports in order: standard library, third-party, local application
- Use type hints for function parameters and return values

---

### core

**File:** `~/.cursor/rules/core.mdc`
**Always applied:** Yes

Two modes of operation:

1. **Plan mode** — Work with the user to define a plan; no code changes.
2. **Act mode** — Make changes to the codebase based on the approved plan.

Rules:
- Start in Plan mode; do not move to Act mode until the plan is approved.
- Print `# Mode: PLAN` or `# Mode: ACT` at the beginning of each response.
- Only switch to Act mode when user types `ACT`; revert to Plan after each response unless user types `PLAN`.
- In Plan mode, always output the full updated plan in every response.
- In Act mode, focus on implementing the agreed plan precisely and efficiently.

---

### decisive-implementation

**File:** `~/.cursor/rules/decisive-implementation.mdc`
**Always applied:** Yes

When a feature or change is requested, make technical decisions and implement immediately.

**Decide autonomously:**
- Design pattern, code structure, data structures
- Error handling approach and validation strategy
- Library selection (choose popular, well-maintained)

**Implementation philosophy:**
- Favor simplicity over cleverness
- Choose readability over performance (unless performance is critical)
- Use established patterns over novel approaches
- Prefer explicit over implicit

**Do not ask about:** variable names, function structure, file organization, standard patterns, common trade-offs.

---

### enhance-documentation

**File:** `~/.cursor/rules/enhance-documentation.mdc`
**Always applied:** No — applies to `**/*.py` only

Automatically improve documentation when working with Python code:
- Add docstrings for functions/classes missing them
- Add parameter and return value descriptions
- Document exceptions
- Add type hints where missing
- Follow Google-style docstrings

---

### fetch-rules

**File:** `~/.cursor/rules/fetch-rules.mdc`
**Always applied:** Yes

Call `fetch_rules` first — mandatory before every user request, before any code changes, and when topic or file type changes mid-conversation. Rules override built-in knowledge.

---

### memory-bank-instructions

**File:** `~/.cursor/rules/memory-bank-instructions.mdc`
**Always applied:** Yes

Memory resets completely between sessions. The Memory Bank is the only link to previous work — must be read at the start of every task.

**Core Memory Bank files (all required):**

| File | Purpose |
|---|---|
| `projectbrief.md` | Foundation: requirements, goals, source of truth |
| `productContext.md` | Why it exists, problems solved, UX goals |
| `activeContext.md` | Current focus, recent changes, next steps |
| `systemPatterns.md` | Architecture, key decisions, design patterns |
| `techContext.md` | Technologies, setup, constraints, dependencies |
| `progress.md` | What works, what's left, known issues |

**Update triggers:**
1. Discovering new project patterns
2. After implementing significant changes
3. When user says "update memory bank" (review ALL files)
4. When context needs clarification

---

### post-task-cleanup

**File:** `~/.cursor/rules/post-task-cleanup.mdc`
**Always applied:** Yes

After completing any task:

**Clean up:**
- Remove temporary test files created for debugging
- Remove debug print statements
- Clean up commented-out code
- Remove unused imports
- Format modified files

**Do not remove:**
- User's existing comments
- Intentional TODO comments
- Debug code explicitly requested by user
- Test files that are part of the project

---

### proactive-completion

**File:** `~/.cursor/rules/proactive-completion.mdc`
**Always applied:** Yes

When encountering incomplete code, complete it automatically:
- TODO comments with obvious implementation
- Stub functions with clear purpose
- Missing error handling in functions
- Incomplete docstrings
- Missing return type hints
- Partial test coverage

Ask only if the implementation intent is genuinely unclear.

---

### proactive-scanning

**File:** `~/.cursor/rules/proactive-scanning.mdc`
**Always applied:** Yes

When working in files, scan for obvious issues and fix them:

**Scan for:** inconsistent naming, duplicate code, missing error handling in critical operations, hardcoded values that should be constants, security issues (SQL injection, XSS), performance anti-patterns (N+1 queries, unnecessary loops).

**Fix immediately:** issues that are obvious and safe, follow clear best practices, have a single correct solution.

**Note but don't fix:** architectural issues requiring discussion, issues with possible business reasons, breaking changes to public APIs.

---

### rule-visibility

**File:** `~/.cursor/rules/rule-visibility.mdc`
**Always applied:** Yes

At the beginning of each response, list all rules currently being applied as a bulleted list with names and descriptions. Only display rules actually in use for the current action.

---

### rules-location

**File:** `~/.cursor/rules/rules-location.mdc`
**Always applied:** Yes

All rules must be created and stored in `.cursor/rules`. Apply this for every edit or rule creation.

---

### smart-assumptions

**File:** `~/.cursor/rules/smart-assumptions.mdc`
**Always applied:** Yes

Make reasonable assumptions rather than asking for every detail.

**Assume and infer:** file locations, naming conventions, code style, project structure, import paths, configuration formats.

**Ask only when:** the user's goal is ambiguous, business logic decisions are needed, multiple valid approaches with significant impact exist, or external dependencies or credentials are required.

**Process:** make best assumption → implement → verify against codebase → adjust if wrong.

---

### yolo

**File:** `~/.cursor/rules/yolo.mdc`
**Always applied:** No — triggered by user saying "YOLO mode"

When activated: execute planned steps without confirmation. Do not ask follow-ups unless the action is destructive or irreversible. Log what changed and proceed.

---

## Project Rules

---

### 00-global-core

**File:** `.cursor/rules/00-global-core.md`

#### Tab Separation (non-negotiable)

| Tab | Role | Edits files? | Runs commands? |
|---|---|---|---|
| PLAN | Architect / Strategist | No | No |
| AGENT | Executor / Implementer | Yes | Yes |
| DEBUG | Investigator / Forensics | No | No |
| ASK | Scratchpad / Exploration | No | No |
| ARCHIVE | Compressor / Handoff | Docs only | No |

Planning and execution are never mixed in the same tab.

#### Evidence-First
- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

#### PASS/FAIL Discipline
- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

#### State Updates
AGENT must update `docs/ai/STATE.md` after every execution block:
- What changed, what was run, PASS/FAIL evidence, what is next.

#### No Unauthorized Refactors
- Changes exceeding "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

#### Self-Consistency Checklist (required before completing any phase)
- [ ] No duplicate files differing only by case
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` updated with PASS/FAIL evidence

---

### 05-global-mcp-usage

**File:** `.cursor/rules/05-global-mcp-usage.md`

AGENT must use installed MCP tools by name. Manual approaches are fallbacks, never defaults.

#### Preferred Tools

| Category | Preferred tool | Fallback |
|---|---|---|
| Reasoning / planning | Clear Thought 1.5 | Break into sub-steps manually only if user explicitly approves continuing without it |
| Code intelligence | serena | Grep/glob + targeted file reads |
| Documentation | Context7 | Web search or manual doc fetch |
| Browser automation | playwright | Manual screenshot + describe |
| UI generation | Magic MCP | Hand-write component scaffold |
| Web extraction | firecrawl-mcp | Manual fetch + parse |
| Repo operations | github | CLI git + manual hosting UI |
| Web search | Exa Search | Manual search |
| Memory | mem0 (if installed) | File-based memory in `docs/ai/memory/` |

#### Mandatory Triggers

- **Clear Thought 1.5:** task has >5 connected steps, spans multiple files, involves migrations or refactors, or bug is ambiguous with multiple hypotheses.
- **serena:** locating symbols/references/call paths, editing more than one file in a phase, reading large files, understanding class/function relationships.
- **Context7:** after repo docs/code are consulted, use it for third-party APIs, dependencies, frameworks, SDKs, and cloud services relevant to the active repo only.
- **playwright:** verifying UI/web behavior after frontend changes, E2E testing, capturing screenshots.
- **Magic MCP:** creating new UI components, translating UI screenshots to scaffolds, generating design-system components.
- **firecrawl-mcp:** scraping structured data from web pages, crawling a site before scraping.
- **github:** creating/listing/reviewing branches, PRs, issues, managing releases, searching repos.
- **Exa Search:** when Context7 can't answer, searching current information, finding code examples not in Context7.
- **mem0/memory:** before planning (retrieve prior decisions), after completing a phase (store new decisions/patterns).

#### Failure and Fallback Policy
1. Report FAIL immediately with exact tool name and error.
2. Attempt the documented fallback.
3. Record both failed tool and fallback used in `docs/ai/STATE.md`.
4. If fallback also insufficient: stop and surface blocker to PLAN.
5. Never silently skip a tool.

---

### 10-project-workflow

**File:** `.cursor/rules/10-project-workflow.md`

#### PLAN Output Contract
PLAN must produce:
- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- If >5 connected steps: use a reasoning MCP tool before finalizing

#### AGENT Execution Contract
AGENT must:
- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run tests and commands required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict

#### DEBUG Output Contract
DEBUG must produce:
- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- One AGENT prompt to implement and verify the fix

#### Context Attachment Discipline
- Attach files with intent, not habit
- Attach the minimum set needed for the current tab's job
- Prefer referencing paths and targeted excerpts over pasting entire files

---

### 20-project-quality

**File:** `.cursor/rules/20-project-quality.md`

#### Modular Architecture
- Separate concerns: auth / data / api / ui / utils / types
- Favor composable functions and service classes
- No monolithic or inline procedural logic beyond ~20 lines in a single block

#### Diff Discipline
- Prefer small, focused diffs
- Avoid broad reformatting in the same commit as logic changes
- Each phase should end with a commit (or explicit justification)

#### Testing
- Add tests with changes (unit and integration as appropriate)
- Run tests before marking a phase complete

#### Input Validation
- Validate inputs at system boundaries
- Prefer strict typing and explicit error handling

#### Secrets Policy
- Never commit `.env*`, credentials, tokens, or service-account JSON
- Document a pointer (e.g., "API key in 1Password: Project/Key") — never the value
- Reference `docs/ai/memory/MEMORY_CONTRACT.md` for what to persist vs. omit

#### Dependency Hygiene
- Pin versions once stable
- Document upgrades in commit messages
- Use a docs MCP tool to verify library APIs before adopting new versions
