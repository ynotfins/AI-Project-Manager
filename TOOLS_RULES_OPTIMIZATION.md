# Tools Rules Optimization — Rules Audit

This document inventories Cursor rule files from the scoped directories only. It excludes AGENTS.md, chat instructions, and non-rule documentation.

## Master List of Rules

### Global Rules

#### Global 1 — `D:/github/.cursor/rules/00-memory-autopilot.mdc`
Global
When Applied: always
```
---
description: Autopilot memory bootstrap + hygiene for all workspaces
globs: ["*"]
alwaysApply: true
---

# Memory Autopilot (Global)

You have MCP memory tools (mem0, Memory Tool). Work autonomously.

## At session start
1. Check if memory MCP tools are available. If unavailable, proceed without error.
2. Search for existing observations about the current project and user.
3. If `docs/ai/memory/` exists in the workspace, scan headlines from files there.
4. Summarize to <=10 atomic facts. Store only missing observations (avoid duplicates).

## What to persist
- Stable, reusable facts: stacks, frameworks, naming conventions, key decisions.
- One observation per fact, <=120 chars, present tense.

## Never persist
- Secrets, tokens, API keys, credentials, personal data, large blobs.
- Save a pointer instead (e.g., "API key in 1Password: Project/Key").
- Transient brainstorming (keep that in docs).

## When files change
If meaningful changes to package config, environment examples, or newly added services:
- Update/add observations that reflect the change (avoid duplicates).

## On exit
If architectural changes or new standards were created, persist a brief observation and link to the relevant file path.

## Source of truth
Repo docs (`docs/ai/`) always win over stored memory observations. See `docs/ai/memory/MEMORY_CONTRACT.md` if it exists.
```

#### Global 2 — `D:/github/.cursor/rules/auto-error-fixing.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Automatically fix errors when detected
---

# Auto Error Fixing

When errors are detected, fix them immediately without asking.

## Auto-fix These Errors:
- Syntax errors
- Missing imports
- Undefined variables (infer or import)
- Type errors (add type hints or fix types)
- Linter errors
- Formatting issues

## After Fixing:
- Briefly state what was fixed
- Continue with the original task

This rule complements coding standards by enforcing them automatically.
```

#### Global 3 — `D:/github/.cursor/rules/autonomous-rule-creation.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Create rules only when explicitly requested or clearly warranted
---

# Rule Creation Policy

Do NOT create a new rule on every piece of user feedback. Rule sprawl causes contradictions.

## Create a rule ONLY when:
- The user explicitly says "make this a rule" or "remember this for all projects"
- A pattern has been repeated 3+ times and the user confirms it should be standard
- The feedback represents a durable, project-wide convention (not a one-off preference)

## Before creating:
- Check existing rules in `.cursor/rules/` for overlap
- If an existing rule covers it, update that rule instead of creating a new one
- Keep rules small, testable, and non-overlapping

## Naming:
- Use numbered prefixes matching the layer (00-09 global, 10-19 workflow, 20-29 quality)
- Use kebab-case descriptive names
```

#### Global 4 — `D:/github/.cursor/rules/decisive-implementation.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Make decisive technical choices and implement immediately
---

# Decisive Implementation

When user requests a feature or change, make technical decisions and implement.

## Decide Autonomously:
- Which design pattern to use
- How to structure the code
- What data structures to use
- Error handling approach
- Validation strategy
- Which library to use (choose popular, well-maintained)

## Implementation Philosophy:
- Favor simplicity over cleverness
- Choose readability over performance (unless performance critical)
- Use established patterns over novel approaches
- Prefer explicit over implicit

## After Implementation:
- Briefly explain key decisions if non-obvious
- Note trade-offs if significant
- Mention alternative approaches only if user asks

## Don't Ask About:
- Variable names
- Function structure
- File organization (follow project rules)
- Standard patterns
- Common trade-offs

This rule eliminates decision paralysis and maintains flow.
```

#### Global 5 — `D:/github/.cursor/rules/post-task-cleanup.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Clean up automatically after completing tasks
---

# Post-Task Cleanup

After completing any task, perform automatic cleanup.

## Cleanup Actions:
- Remove temporary test files created for debugging
- Remove debug print statements added during work
- Clean up commented-out code
- Remove unused imports
- Format modified files
- Ensure files are in correct directories per project rules

## What NOT to Remove:
- User's existing comments
- TODO comments that are intentional
- Debug code explicitly requested by user
- Test files that are part of the project

## Timing:
- Execute cleanup at task completion
- Before presenting final results
- Note cleanup actions briefly

This rule maintains codebase hygiene without manual intervention.
```

#### Global 6 — `D:/github/.cursor/rules/proactive-completion.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Complete partial implementations proactively
---

# Proactive Completion

When encountering incomplete code, complete it automatically.

## Complete These Automatically:
- TODO comments with obvious implementation
- Stub functions with clear purpose
- Missing error handling in functions
- Incomplete docstrings
- Missing return type hints
- Partial test coverage

## Approach:
- Implement the obvious solution
- Follow existing patterns in codebase
- Note what was completed
- Ask only if the implementation intent is unclear

This rule helps maintain momentum in development.
```

#### Global 7 — `D:/github/.cursor/rules/proactive-scanning.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Scan for issues proactively and fix them
---

# Proactive Scanning

When working in files, scan for obvious issues and fix them.

## Scan For:
- Inconsistent naming in same file
- Duplicate code blocks
- Missing error handling in critical operations
- Hardcoded values that should be constants
- Security issues (SQL injection, XSS vulnerabilities)
- Performance anti-patterns (N+1 queries, unnecessary loops)

## Fix Immediately:
- Issues that are obvious and safe to fix
- Issues that follow clear best practices
- Issues with single correct solution

## Note But Don't Fix:
- Architectural issues requiring discussion
- Issues that might have business reasons
- Breaking changes to public APIs

## Communication:
- Mention what was found and fixed
- Continue with original task
- Don't derail the main objective

This rule improves code quality opportunistically.
```

#### Global 8 — `D:/github/.cursor/rules/rule-visibility.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Lightweight rule awareness without token waste
---

# Rule Visibility (lightweight)

Do NOT list all active rules at the start of every response. That wastes tokens and slows execution.

Instead:
- When a rule influences a decision, name it briefly inline (e.g., "per 20-project-quality, keeping diff small").
- If the user asks "what rules are active?", then list them.
- AGENTS.md is the canonical entry point; reference it when onboarding.
```

#### Global 9 — `D:/github/.cursor/rules/smart-assumptions.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Make intelligent assumptions to maintain workflow momentum
---

# Smart Assumptions

Make reasonable assumptions rather than asking for every detail.

## Assume and Infer:
- File locations (check codebase first)
- Naming conventions (follow existing patterns)
- Code style (match existing files)
- Project structure (explore and mirror)
- Import paths (infer from structure)
- Configuration formats (match existing)

## When to Ask:
- User's specific goal is ambiguous
- Business logic decisions needed
- Multiple valid approaches exist and impact is significant
- External dependencies or credentials required

## Process:
1. Make best assumption
2. Implement based on assumption
3. Verify by checking codebase
4. Adjust if assumption was wrong

This rule minimizes interruptions while maintaining accuracy.
```

#### Global 10 — `D:/.cursor/rules/00-memory-autopilot.mdc`
Global
When Applied: Not always-on (alwaysApply: false); globs ["*"]
```
---
description: Autopilot memory bootstrap + hygiene for all workspaces
globs: ["*"]
alwaysApply: false
---

# Memory Autopilot (Global)

Optional helper rule. Use only when a memory MCP is available and relevant.

## Session start
1) If memory MCP is unavailable, continue with repo docs only.
2) Prefer repo-tracked state docs over memory entries.
3) Use memory to recall stable decisions/patterns, not transient chat details.

## What to persist
- Stable, reusable facts and decisions only.
- Keep entries short and non-duplicative.

## Never persist
- Secrets, tokens, API keys, credentials, or large blobs.
- Transient brainstorming and long chat summaries.

## On exit
If architectural standards or durable decisions changed, persist a concise memory entry and link the source file path.
```

#### Global 11 — `D:/.cursor/rules/01-ai-pm-canonical-governance.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Use AI-Project-Manager as canonical governance source when present
---

# AI-PM Canonical Governance

When `D:\github\AI-Project-Manager` is available in the workspace or referenced by path:

1. Treat AI-PM repo-tracked rules and docs as the workflow/process authority layer, subordinate to the product charter and the authority order declared in `AI-Project-Manager/AGENTS.md`.
2. Prefer these sources for workflow/state policy:
   - `AI-Project-Manager/.cursor/rules/*`
   - `AI-Project-Manager/docs/ai/STATE.md`
   - `AI-Project-Manager/docs/ai/operations/*`
3. For other repos (`open--claw`, `droidrun`), keep mirrored rules aligned with AI-PM.
4. If drift is detected, report it and propose/perform harmonization.

This global rule is an activation hint only. It must not broaden bootstrap order, force extra reads, or silently override narrower repo-tracked AI-PM policy.
```

#### Global 12 — `D:/.cursor/rules/auto-error-fixing.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Automatically fix errors when detected
---

# Auto Error Fixing

When errors are detected, fix them immediately without asking.

## Auto-fix These Errors:
- Syntax errors
- Missing imports
- Undefined variables (infer or import)
- Type errors (add type hints or fix types)
- Linter errors
- Formatting issues

## After Fixing:
- Briefly state what was fixed
- Continue with the original task

This rule complements coding standards by enforcing them automatically.
```

#### Global 13 — `D:/.cursor/rules/autonomous-rule-creation.mdc`
Global
When Applied: Explicit user rule request or clear policy-drift failures (alwaysApply: false)
```
---
alwaysApply: false
description: Automatically create rules from user feedback
---

# Autonomous Rule Creation

Create or update a rule only when the user explicitly asks for a rule change, or when policy drift is clearly causing repeated failures.
- Extract the main point of the feedback
- Create a new rule that captures this as a reusable instruction
- Save the new rule with a short, descriptive name
- Keep rules simple and avoid redundancy

Do not auto-create rules during normal implementation work.
```

#### Global 14 — `D:/.cursor/rules/coding-standards.mdc`
Global
When Applied: applies_to: **/*.py
```
---
description: Python coding standards and style guidelines
applies_to: **/*.py
---

# Python Coding Standards

- Use 4 spaces for indentation
- Maximum line length of 88 characters
- Follow PEP 8 naming conventions
- Use descriptive variable and function names
- Add docstrings for all functions and classes
- Imports in order: standard library, third-party, local application
- Use type hints for function parameters and return values
- Insert print("Hello, beautiful learner") at the start of every Python function

These standards ensure readability and consistency throughout our codebase.
```

#### Global 15 — `D:/.cursor/rules/core.mdc`
Global
When Applied: always
```
---
description: Core operational rules for the Cursor agent
globs: 
alwaysApply: true
---
## Core Rules

- Respect host plan/act mode controls and system instructions first.
- In planning mode: gather evidence and produce an actionable plan; do not implement.
- In execution mode: implement approved work with minimal, verifiable diffs.
- Never require synthetic mode tokens (for example, `ACT`/`PLAN`) unless the user explicitly uses them.
- Prioritize repo-tracked truth and explicit user intent over generic defaults.
```

#### Global 16 — `D:/.cursor/rules/decisive-implementation.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Make decisive technical choices and implement immediately
---

# Decisive Implementation

When user requests a feature or change, make technical decisions and implement.

## Decide Autonomously:
- Which design pattern to use
- How to structure the code
- What data structures to use
- Error handling approach
- Validation strategy
- Which library to use (choose popular, well-maintained)

## Implementation Philosophy:
- Favor simplicity over cleverness
- Choose readability over performance (unless performance critical)
- Use established patterns over novel approaches
- Prefer explicit over implicit

## After Implementation:
- Briefly explain key decisions if non-obvious
- Note trade-offs if significant
- Mention alternative approaches only if user asks

## Don't Ask About:
- Variable names
- Function structure
- File organization (follow project rules)
- Standard patterns
- Common trade-offs

This rule eliminates decision paralysis and maintains flow.
```

#### Global 17 — `D:/.cursor/rules/enhance-documentation.mdc`
Global
When Applied: applies_to: **/*.py
```
---
description: Enhance documentation automatically for Python code
applies_to: **/*.py
---

# Enhance Documentation

Automatically improve documentation when working with Python code.

## Add Automatically:
- Docstrings for functions without them
- Docstrings for classes without them
- Parameter descriptions in existing docstrings
- Return value descriptions
- Exception documentation
- Type hints where missing

## Documentation Style:
- Follow Google-style docstrings
- Be concise but complete
- Document the "why" for non-obvious code
- Include examples for complex functions

## When Applied:
- When creating new functions/classes
- When modifying existing functions/classes
- When reviewing code

This rule complements coding-standards by ensuring documentation completeness.
```

#### Global 18 — `D:/.cursor/rules/fetch-rules.mdc`
Global
When Applied: Before substantial work (per rule text)
```
# Rule Discovery

Before substantial work, verify applicable repo/global rules from `.cursor/rules/`.

Guidance:
- Re-check rules when scope or file types change significantly.
- Prefer concise, relevant rules over broad boilerplate.
- If rule intent conflicts with explicit user instruction, ask or defer to higher-priority system/developer constraints.
```

#### Global 19 — `D:/.cursor/rules/MCP-AGENT_RULES.mdc`
Global
When Applied: always
```
---
description: Force proper thinking-patterns MCP usage
alwaysApply: true
---

# Thinking-Patterns Protocol

Use `thinking-patterns` for non-trivial reasoning work instead of relying on implicit freeform reasoning.

Repo-tracked MCP policy defines the exact required/optional triggers and fallback behavior for a given workspace. This global rule is a reminder, not an override.

## Required Triggers

- Use `sequential_thinking` before acting when the task is multi-step, ambiguous, or lacks an obvious execution path.
- Use `problem_decomposition` after `sequential_thinking` when the task must be broken into concrete subproblems or phases.
- Use `mental_model` for architecture, strategy, system design, or large refactors.
- Use `decision_framework` when choosing between competing options, libraries, designs, or rollout paths.
- Use `debugging_approach` for bugs, regressions, failures, unexpected behavior, or conflicting evidence.
- Use `critical_thinking` to challenge a draft plan, synthesized answer, or risky implementation before finalizing.
- Use `domain_modeling` when the task requires understanding entities, relationships, or constraints in a new/problem domain.

## Do Not Overuse

- Do not force `thinking-patterns` on trivial one-step tasks, direct file reads, or simple mechanical edits.
- Do not load long manuals by default; use tool schemas and compact repo guidance first.
- Do not expand repo-local tool requirements or treat a repo-marked optional/not-applicable tool as globally mandatory.

## Schema Discipline

Before any complex `thinking-patterns` call with nested objects:

1. Check all required parameters.
2. Verify case-sensitive enum values.
3. Verify nested object structure.
4. Verify array item types.
5. Verify numbers/booleans are not strings.

## Failure Protocol

- If a `thinking-patterns` call fails, assume schema mismatch first.
- Correct once after checking the schema.
- If it still fails, stop retrying blindly, report the tool failure, and continue with the safest fallback allowed by repo policy.
```

#### Global 20 — `D:/.cursor/rules/memory-bank-instructions.mdc`
Global
When Applied: Optional; when workspace uses memory-bank/ (alwaysApply: false)
```
---
alwaysApply: false
description: Optional legacy memory-bank guidance. Prefer repo-native memory docs.
---

# Memory Bank Instructions (Optional)

Use only when a workspace explicitly uses a `memory-bank/` directory.

Preferred priority in modern repos:
1. `docs/ai/STATE.md`
2. `docs/ai/memory/DECISIONS.md`
3. `docs/ai/memory/PATTERNS.md`
4. `docs/ai/operations/*` context governance docs

Do not force full memory-bank scans when those files are absent.
---
alwaysApply: false
---
description: Optional legacy memory-bank guidance. Prefer repo-native memory docs.

# Memory Bank Instructions (Optional)

Use only when a workspace explicitly uses a `memory-bank/` directory.

Preferred priority in modern repos:
1. `docs/ai/STATE.md`
2. `docs/ai/memory/DECISIONS.md`
3. `docs/ai/memory/PATTERNS.md`
4. `docs/ai/operations/*` context governance docs

Avoid forcing full-memory-bank reads when those files do not exist.

## Memory Bank Structure

The Memory Bank consists of core files and optional context files, all in Markdown format. Files build upon each other in a clear hierarchy:

flowchart TD
    PB[projectbrief.md] --> PC[productContext.md]
    PB --> SP[systemPatterns.md]
    PB --> TC[techContext.md]
    
    PC --> AC[activeContext.md]
    SP --> AC
    TC --> AC
    
    AC --> P[progress.md]

### Core Files (Required)
1. `projectbrief.md`
   - Foundation document that shapes all other files
   - Created at project start if it doesn't exist
   - Defines core requirements and goals
   - Source of truth for project scope

2. `productContext.md`
   - Why this project exists
   - Problems it solves
   - How it should work
   - User experience goals

3. `activeContext.md`
   - Current work focus
   - Recent changes
   - Next steps
   - Active decisions and considerations
   - Important patterns and preferences
   - Learnings and project insights

4. `systemPatterns.md`
   - System architecture
   - Key technical decisions
   - Design patterns in use
   - Component relationships
   - Critical implementation paths

5. `techContext.md`
   - Technologies used
   - Development setup
   - Technical constraints
   - Dependencies
   - Tool usage patterns

6. `progress.md`
   - What works
   - What's left to build
   - Current status
   - Known issues
   - Evolution of project decisions

## Core Workflows

### Plan Mode
flowchart TD
    Start[Start] --> ReadFiles[Read Memory Bank]
    ReadFiles --> CheckFiles{Files Complete?}
    
    CheckFiles -->|No| Plan[Create Plan]
    Plan --> Document[Document in Chat]
    
    CheckFiles -->|Yes| Verify[Verify Context]
    Verify --> Strategy[Develop Strategy]
    Strategy --> Present[Present Approach]

### Act Mode
flowchart TD
    Start[Start] --> Context[Check Memory Bank]
    Context --> Update[Update Documentation]
    Update --> Execute[Execute Task]
    Execute --> Document[Document Changes]

## Documentation Updates

Memory Bank updates occur when:
1. Discovering new project patterns
2. After implementing significant changes
3. When user requests with **update memory bank** (MUST review ALL files)
4. When context needs clarification

flowchart TD
    Start[Update Process]
    
    subgraph Process
        P1[Review ALL Files]
        P2[Document Current State]
        P3[Clarify Next Steps]
        P4[Document Insights & Patterns]
        
        P1 --> P2 --> P3 --> P4
    end
    
    Start --> Process

Note: When triggered by **update memory bank**, I MUST review every memory bank file, even if some don't require updates.
Focus particularly on activeContext.md and progress.md as they track current state.

REMEMBER: After every memory reset, I begin completely fresh. The Memory Bank is my only link to previous work.
It must be maintained with precision and clarity, as my effectiveness depends entirely on its accuracy.
```

#### Global 21 — `D:/.cursor/rules/no-secrets-in-files.mdc`
Global
When Applied: always
```
---
description: No secrets in any files — all credentials injected via Bitwarden/WSLENV
alwaysApply: true
---

# No Secrets in Files (Cross-Project)

## Hard Rule: Zero Secrets on Disk in Any Committed or Local Config File

**NEVER** write secrets to any file — committed or local — including:
- `.env`, `.env.local`, `*.env.*`
- `openclaw.json`, `auth-profiles.json`
- `STATE.md`, `DECISIONS.md`, or any documentation
- PowerShell scripts, shell scripts, batch files
- Any file in `~/.openclaw/`, `%USERPROFILE%\.openclaw\`, or project dirs

## Approved Secret Delivery Paths

### 1. Bitwarden Secrets Manager → PowerShell environment vars (at Cursor launch)
```powershell
# In start-cursor-with-secrets.ps1 — secrets land in $env:VAR only
bws run --project-id <id> -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
```

### 2. WSLENV injection (Windows → WSL, in-memory only)
```powershell
$env:WSLENV = "ANTHROPIC_API_KEY/u:OPENAI_API_KEY/u:OPENROUTER_API_KEY/u"
wsl bash -c "source ~/.nvm/nvm.sh && pnpm openclaw gateway start"
$env:WSLENV = ""  # Clear immediately after
```

### 3. OpenClaw SecretRef objects (env, never plaintext)
```json
{ "source": "env", "provider": "default", "id": "ANTHROPIC_API_KEY" }
```

## What to Do If You Find a Secret

1. **Remove it immediately** — replace with placeholder or SecretRef
2. If it was committed: rotate the secret, then remove from git history
3. Scan with: `openclaw secrets audit` (WSL) + PowerShell `Select-String` on docs

## Scan Commands

```powershell
# Scan both repos
Get-ChildItem -Path D:\github -Recurse -File |
  Where-Object { $_.FullName -notlike "*node_modules*" } |
  Select-String -Pattern "sk-ant|sk-or-v1|sk-proj|ghp_[A-Za-z0-9]{30}|AKIA[A-Z0-9]{16}" |
  Select-Object Filename, LineNumber, Line
```

```bash
# WSL audit
openclaw secrets audit
```

## Allowed Exceptions

- `gateway.auth.token` in `~/.openclaw/openclaw.json` — OpenClaw-managed internal token (not a user secret; can't be moved to env)
- `TELEGRAM_BOT_TOKEN` and `GOG_KEYRING_PASSWORD` in `~/.openclaw/.env` — low-risk channel tokens (not API keys; acceptable until Bitwarden flow covers them)

## .gitignore Requirements (both repos)

```
.env
.env.*
*.env
*.env.*
auth-profiles.json
gmail-client-secret*.json
service-account*.json
*-key-ed25519.json
```
```

#### Global 22 — `D:/.cursor/rules/obsidian-memory-gate.mdc`
Global
When Applied: always
```
---
description: "Optional Obsidian sidecar guidance subordinate to repo-tracked policy"
alwaysApply: true
---

# Obsidian Memory Gate (Global)

Repo-tracked policy wins over this global overlay.

Use `obsidian-vault` only when both of these are true:

1. The active repo policy does not forbid or narrow the Obsidian step.
2. The task explicitly needs operator notes or personal research already known to live in Obsidian.

Do not trigger Obsidian just because a request mentions prior work, decisions, docs, architecture, notes, memory, or background.

## Failure rule

If `obsidian-vault` is relevant and unavailable:

1. Say so explicitly.
2. Follow the repo-tracked fallback path.
3. Do not block canonical repo work when the repo policy marks Obsidian as sidecar-only/non-blocking.

## Scope

This overlay applies only as a subordinate sidecar reminder across workspaces.
```

#### Global 23 — `D:/.cursor/rules/post-task-cleanup.mdc`
Global
When Applied: Not always-on (alwaysApply: false); follow rule body for triggers
```
---
alwaysApply: false
description: Clean up automatically after completing tasks
---

# Post-Task Cleanup

After completing any task, perform automatic cleanup.

## Cleanup Actions:
- Remove temporary test files created for debugging
- Remove debug print statements added during work
- Clean up commented-out code
- Remove unused imports
- Format modified files
- Ensure files are in correct directories per project rules

## What NOT to Remove:
- User's existing comments
- TODO comments that are intentional
- Debug code explicitly requested by user
- Test files that are part of the project

## Timing:
- Execute cleanup at task completion
- Before presenting final results
- Note cleanup actions briefly

This rule maintains codebase hygiene without manual intervention.
```

#### Global 24 — `D:/.cursor/rules/proactive-completion.mdc`
Global
When Applied: Not always-on (alwaysApply: false); follow rule body for triggers
```
---
alwaysApply: false
description: Complete partial implementations proactively
---

# Proactive Completion

When encountering incomplete code, complete it automatically.

## Complete These Automatically:
- TODO comments with obvious implementation
- Stub functions with clear purpose
- Missing error handling in functions
- Incomplete docstrings
- Missing return type hints
- Partial test coverage

## Approach:
- Implement the obvious solution
- Follow existing patterns in codebase
- Note what was completed
- Ask only if the implementation intent is unclear

This rule helps maintain momentum in development.
```

#### Global 25 — `D:/.cursor/rules/proactive-scanning.mdc`
Global
When Applied: Not always-on (alwaysApply: false); follow rule body for triggers
```
---
alwaysApply: false
description: Scan for issues proactively and fix them
---

# Proactive Scanning

When working in files, scan for obvious issues and fix them.

## Scan For:
- Inconsistent naming in same file
- Duplicate code blocks
- Missing error handling in critical operations
- Hardcoded values that should be constants
- Security issues (SQL injection, XSS vulnerabilities)
- Performance anti-patterns (N+1 queries, unnecessary loops)

## Fix Immediately:
- Issues that are obvious and safe to fix
- Issues that follow clear best practices
- Issues with single correct solution

## Note But Don't Fix:
- Architectural issues requiring discussion
- Issues that might have business reasons
- Breaking changes to public APIs

## Communication:
- Mention what was found and fixed
- Continue with original task
- Don't derail the main objective

This rule improves code quality opportunistically.
```

#### Global 26 — `D:/.cursor/rules/python-file-location.md`
Global
When Applied: applies_to: **/*.py
```
---
description: All Python files should be placed in the src folder
applies_to: **/*.py
---

# Python File Location

All Python files should be placed in the `src` folder.

## Requirements
- Place all `.py` files in the `src/` directory
- Create subdirectories within `src/` as needed for organization
- Only test files or build scripts may exist in the root if absolutely necessary

## Application
- Apply this rule when creating new Python files
- Apply this rule when organizing existing Python files
```

#### Global 27 — `D:/.cursor/rules/rule-visibility.mdc`
Global
When Applied: Not always-on (alwaysApply: false); follow rule body for triggers
```
---
alwaysApply: false
description: Display applied rules at each AI action for transparency
---

# Rule Visibility

Keep rule visibility lightweight to reduce response bloat.

## Requirements
- Only list active rules when the user asks for a rule audit or policy trace.
- Otherwise, apply rules silently and focus on task output.

## Application
- Use this rule only for explicit governance/debugging discussions.
```

#### Global 28 — `D:/.cursor/rules/rules-location.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: All rules are located in .cursor/rules directory
---

# Cursor Rules Location

Locate all rules in .cursor/rules

Apply this rule for every edit or create rule
```

#### Global 29 — `D:/.cursor/rules/smart-assumptions.mdc`
Global
When Applied: always
```
---
alwaysApply: true
description: Make intelligent assumptions to maintain workflow momentum
---

# Smart Assumptions

Make reasonable assumptions rather than asking for every detail.

## Assume and Infer:
- File locations (check codebase first)
- Naming conventions (follow existing patterns)
- Code style (match existing files)
- Project structure (explore and mirror)
- Import paths (infer from structure)
- Configuration formats (match existing)

## When to Ask:
- User's specific goal is ambiguous
- Business logic decisions needed
- Multiple valid approaches exist and impact is significant
- External dependencies or credentials required

## Process:
1. Make best assumption
2. Implement based on assumption
3. Verify by checking codebase
4. Adjust if assumption was wrong

This rule minimizes interruptions while maintaining accuracy.
```

### Project Rules

#### Project 1 — `D:/github/AI-Project-Manager/.cursor/rules/00-global-core.md`
Project: AI-Project-Manager
When Applied: always
```
---
description: "Global core non-negotiables: charter, tabs, evidence, state discipline"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

The supreme governing document for this tri-workspace is `FINAL_OUTPUT_PRODUCT.md` in `open--claw/open-claw/AI_Employee_knowledgebase/`. No rule, prompt, plan, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It is not the product authority.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects. `@Past Chats` is a last resort only — consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Do not pre-load or attach the full ledger.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
```

#### Project 2 — `D:/github/AI-Project-Manager/.cursor/rules/01-charter-enforcement.md`
Project: AI-Project-Manager
When Applied: always
```
---
description: "Charter enforcement kernel: FINAL_OUTPUT_PRODUCT.md supreme, forbidden platforms, fail-fast"
globs: ["**/*"]
alwaysApply: true
---

# 01 — Charter Enforcement Kernel

## LOAD ORDER: This file is read immediately after 00-global-core.md. No exceptions.

## Supreme Authority

`open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` is the governing charter for this entire tri-workspace. It must be read first in every bootstrap path. No other document, rule, prompt, plan, agent instruction, or local convention may override or weaken it.

No repo may claim authority equal to or higher than the charter.

## Fail-Fast Rule

If any instruction, file, plan, prompt, or proposed change conflicts with the charter:

1. Stop execution immediately.
2. State the conflict explicitly with the specific charter section being violated.
3. Do not partially continue.
4. Do not silently re-route around the violation.
5. Require correction before resuming.

## Forbidden Platform Targets

The tri-workspace target platforms are: **Windows, WSL, Android, Docker, and web**.

The following are **forbidden as tri-workspace build targets**:

- macOS applications
- iOS applications
- Swift source code
- Xcode projects or workspaces
- CocoaPods dependencies

**On detection of a forbidden pattern:**

1. Stop immediately.
2. Report: `CHARTER VIOLATION — forbidden platform target detected: <pattern>`.
3. Route to Sparky (`sparky-chief-product-quality-officer`) for resolution decision.
4. Do not continue until Sparky has reviewed and Tony has authorized an exception.

Detection scope: any new file, dependency, build config, CI step, prompt, or plan that introduces the above patterns is a violation.

## Authority Ceiling

No rule file, workflow doc, prompt template, or agent persona in this repo may assert authority above the charter. Any such claim is void on detection and must be corrected immediately.

## This File Cannot Be Weakened By

- Convenience patterns
- Legacy file layouts
- Prompt shortcuts
- Prior session assumptions
- Any other rule in any repo

If this file conflicts with any other rule, this file wins. If this file conflicts with the charter, the charter wins.
```

#### Project 3 — `D:/github/AI-Project-Manager/.cursor/rules/02-non-routable-exclusions.md`
Project: AI-Project-Manager
When Applied: always
```
---
description: "Non-routable quarantine enforcement for AI-Project-Manager. Canonical registry lives in open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — AI-Project-Manager

> **Canonical registry**: `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file mirrors the enforcement behavior defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (cross-repo, enforced here)

The following paths across the tri-workspace are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations in this repo's sessions:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
../droidrun/src/droidrun/tools/driver/ios.py
../droidrun/src/droidrun/tools/ui/ios_provider.py
../droidrun/src/droidrun/tools/ios/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
../droidrun/src/droidrun/tools/driver/ios.py
../droidrun/src/droidrun/tools/ui/ios_provider.py
../droidrun/src/droidrun/tools/ios/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured across this workspace, quarantined paths must be in its exclusion list.

---

## Banner Markers

Files are quarantined if they begin with any of these banners:

```
<!-- NON-ROUTABLE — OUT OF SCOPE -->   (Markdown/HTML files)
# NON-ROUTABLE — OUT OF SCOPE         (Python/script files)
```

Treat all such files as quarantined regardless of whether their path is explicitly listed above.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Reading `NON_ROUTABLE_QUARANTINE.md` to understand the registry
- Updating quarantine docs when instructed

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Project 4 — `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md`
Project: AI-Project-Manager
When Applied: globs: ["**/*"]
```
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
```

#### Project 5 — `D:/github/AI-Project-Manager/.cursor/rules/10-project-workflow.md`
Project: AI-Project-Manager
When Applied: always
```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy, ledger discipline"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** of the tri-workspace. It does not supersede the product charter.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3 (required): `Rationale: <one-line reason for this model and mode>`
- Model selection is intentional — PLAN must not silently default. Allowed choices:
  - `Composer2 — non-thinking`: straightforward execution, high-volume or long-but-simple tasks. Use as default when no complexity flag is present.
  - `Sonnet 4.6 — non-thinking`: medium complexity, multi-file scope, conditional branching.
  - `Sonnet 4.6 — thinking`: multi-step reasoning, debugging, non-obvious trade-offs.
  - `Opus 4.6 — thinking`: high-ambiguity novel problems or complex architecture decisions. Explicit justification required; do not use by default.
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- A `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified. Do not bury active turbulence in STATE.md alone.
- After every meaningful execution, write the recovery bundle via `filesystem` to:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- After every meaningful execution, write at least one compact durable update via `openmemory`
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the user explicitly requests it or the phase instructions require it. If commit/push is intentionally skipped, record why in `docs/ai/STATE.md`.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by the token/size thresholds in `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. Read the recovery bundle in `docs/ai/recovery/` before any broad repo logs or scans
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and the four recovery bundle files, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/memory/MEMORY_CONTRACT.md`, `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`, and `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
3. `docs/ai/STATE.md` summary/current state section — operational evidence
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` on demand
5. `docs/ai/context/` — non-canonical artifacts (on-demand only)
6. Chat history / `@Past Chats` — last resort only

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The filesystem recovery bundle is a non-canonical speed layer for post-crash or post-reboot recovery.

- Use it after the authority contract and OpenMemory, not before them.
- Use only these files for default recovery:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If the bundle is stale, missing, or known-degraded, record that and continue with repo docs.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry using the format defined in the ledger file itself. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management (hook-enforced — automatic):**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, the `afterFileEdit` Cursor hook (`.cursor/hooks.json` → `.cursor/hooks/rotate_ledger.py`) automatically moves the oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- AGENT must still append the new entry. Archival of old entries is automatic after each ledger edit — AGENT does NOT manage archival manually.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — the hook moves them verbatim.
- If the hook is unavailable or fails, AGENT must archive manually following the same policy before proceeding to the next non-trivial block.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Project 6 — `D:/github/AI-Project-Manager/.cursor/rules/20-project-quality.md`
Project: AI-Project-Manager
When Applied: always
```
---
description: "Modular architecture, diff/testing/secrets hygiene, Context7 for dependencies"
globs: ["**/*"]
alwaysApply: true
---

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
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
```

#### Project 7 — `D:/github/AI-Project-Manager/.cursor/rules/openmemory.mdc`
Project: AI-Project-Manager
When Applied: always
```
---
description: "Flat OpenMemory runtime policy for no-loss recovery and durable storage"
globs: ["**/*"]
alwaysApply: true
---

# OpenMemory Runtime Policy

OpenMemory is the primary durable structured recall layer for this repo, but it is never canonical authority.

## Recovery order

Use OpenMemory in the lean no-loss path:

1. Read the charter
2. Read repo authority docs
3. Run a targeted OpenMemory query for the active repo/task
4. Then use the recovery bundle, `STATE.md` summary, and one selective deep read if needed

Do not preload `docs/ai/context/AGENT_EXECUTION_LEDGER.md`. It stays one-block fallback only.

## Live runtime only

The verified Cursor-side surface is flat:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Do not claim or require `project_id`, `namespace`, `user_preference`, `memory_types`, metadata dicts, or direct filter support unless a proven wrapper exists in the active runtime.

## Retrieval behavior

- Run targeted searches for non-trivial PLAN, AGENT, or DEBUG recovery work.
- Keep queries specific to the active repo, task, or policy question.
- Do not invent multi-phase search quotas or block execution on arbitrary search counts.

## Storage behavior

- Store only validated durable knowledge: decisions, reusable patterns, stable debug findings, and recovery-policy updates.
- Use compact self-identifying plain text, for example:
  - `[repo=ai-pm][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
  - `[repo=tri-workspace][kind=policy][status=active][source=docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md] ...`
- Never store secrets, credentials, raw transcripts, or copied ledger blocks.

## Failure behavior

If OpenMemory is required and degraded:

1. Announce FAIL immediately
2. Name the exact failed step
3. Use repo docs plus the recovery bundle only if the task remains safely satisfiable
4. Record the fallback path and any reseed debt in `docs/ai/STATE.md`

## Guide discipline

Keep `openmemory.md` aligned with the live flat runtime and the compact text convention. Do not treat it as an aspirational mem0 schema.
```

#### Project 8 — `D:/github/open--claw/.cursor/rules/00-global-core.md`
Project: open--claw
When Applied: always
```
---
description: "Global core non-negotiables"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

`open--claw` is the **strict enforcement center** of the tri-workspace. The supreme governing document for this entire project is `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No rule, prompt, plan, workflow doc, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It does not issue product law.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Read **one block at a time**; stop as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
```

#### Project 9 — `D:/github/open--claw/.cursor/rules/01-charter-enforcement.md`
Project: open--claw
When Applied: always
```
---
description: "Charter enforcement kernel"
globs: ["**/*"]
alwaysApply: true
---

# 01 — Charter Enforcement Kernel

## LOAD ORDER: This file is read immediately after 00-global-core.md. No exceptions.

## Supreme Authority

`open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` is the governing charter for this entire tri-workspace. It must be read first in every bootstrap path. No other document, rule, prompt, plan, agent instruction, or local convention may override or weaken it.

No repo may claim authority equal to or higher than the charter.

## Fail-Fast Rule

If any instruction, file, plan, prompt, or proposed change conflicts with the charter:

1. Stop execution immediately.
2. State the conflict explicitly with the specific charter section being violated.
3. Do not partially continue.
4. Do not silently re-route around the violation.
5. Require correction before resuming.

## Forbidden Platform Targets

The tri-workspace target platforms are: **Windows, WSL, Android, Docker, and web**.

The following are **forbidden as tri-workspace build targets**:

- macOS applications
- iOS applications
- Swift source code
- Xcode projects or workspaces
- CocoaPods dependencies

**On detection of a forbidden pattern:**

1. Stop immediately.
2. Report: `CHARTER VIOLATION — forbidden platform target detected: <pattern>`.
3. Route to Sparky (`sparky-chief-product-quality-officer`) for resolution decision.
4. Do not continue until Sparky has reviewed and Tony has authorized an exception.

Detection scope: any new file, dependency, build config, CI step, prompt, or plan that introduces the above patterns is a violation.

## Authority Ceiling

No rule file, workflow doc, prompt template, or agent persona in this repo may assert authority above the charter. Any such claim is void on detection and must be corrected immediately.

## This File Cannot Be Weakened By

- Convenience patterns
- Legacy file layouts
- Prompt shortcuts
- Prior session assumptions
- Any other rule in any repo

If this file conflicts with any other rule, this file wins. If this file conflicts with the charter, the charter wins.
```

#### Project 10 — `D:/github/open--claw/.cursor/rules/02-non-routable-exclusions.md`
Project: open--claw
When Applied: always
```
---
description: "Non-routable quarantine exclusions for the open--claw repo. Canonical registry lives in open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — open--claw

> **Canonical registry**: `open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file enforces the quarantine defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (this repo)

The following paths are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations:

```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured for this repo, the following paths must be in its exclusion list:

```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Banner Marker

Any file marked with the following banner at the top is quarantined:

```
<!-- NON-ROUTABLE — OUT OF SCOPE -->
```

Treat all such files as quarantined regardless of whether their path is listed above.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Updating `NON_ROUTABLE_QUARANTINE.md`
- Adding or correcting banners on quarantined files
- Extending the quarantine registry

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Project 11 — `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md`
Project: open--claw
When Applied: always
```
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
```

#### Project 12 — `D:/github/open--claw/.cursor/rules/10-project-workflow.md`
Project: open--claw
When Applied: always
```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** for the open--claw repo. Routine delivery work does not require user approval — Sparky is the internal approval authority. Tony approval is required only for Tony-gate actions defined in `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md`.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Choose lowest-cost model that safely fits task complexity; default non-thinking for straightforward execution
  - PLAN may escalate to a stronger model internally without waiting for user confirmation — see `15-model-routing.md`
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified.
- Refresh the non-canonical recovery bundle after meaningful verified work, or record why it was deferred
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict — route to Sparky for internal resolution, not to the user
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the phase instructions explicitly require it or the user requests it. If commit or push is skipped, record why in `docs/ai/STATE.md`.
- May escalate to a stronger model or route a problem to Sparky without waiting for user confirmation — see `15-model-routing.md`

## Sparky review — mandatory on every file change

After any employee makes a file change, Sparky must review the changed files and determine:

- Whether the change followed best practices
- Whether architectural integrity was preserved
- Whether the change moves the project closer to the finished product in `FINAL_OUTPUT_PRODUCT.md`
- Whether refactoring is required before the work is accepted

Sparky's review does not require user involvement. It is an internal quality gate.

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory first for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. If present and current, read the machine-local recovery bundle before broad repo logs
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and recovery bundle, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/memory/MEMORY_CONTRACT.md`
3. `docs/ai/STATE.md` summary/current state section
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md`
5. `docs/ai/context/`
6. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The recovery bundle is a non-canonical filesystem speed layer.

- Use it after the authority contract and OpenMemory, not before them.
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If it is stale or missing, record that and continue with canonical sources.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Project 13 — `D:/github/open--claw/.cursor/rules/15-model-routing.md`
Project: open--claw
When Applied: always
```
---
description: "Model routing policy for Open Claw: labels, thinking vs non-thinking, escalation"
globs: ["**/*"]
alwaysApply: true
---

# 15 — Model Routing (Open Claw)

> Extends: `10-project-workflow.md`
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

Routine delivery work does not stop to wait for user-confirmed model switches. The team escalates internally — AGENT may route to a stronger model or to Sparky without user confirmation. Tony approval is not required for model selection.

---

## Model Inventory

All model references must use these exact labels. No aliases, no abbreviations.

### Thinking-class models

These models perform extended internal reasoning before responding. Use for ambiguous,
high-stakes, multi-step, or architectural tasks where correctness matters more than speed.

- **GPT-5.2 High**
- **GPT-5.2 Extra High**
- **GPT-5.2 Codex High**
- **GPT-5.2 Codex High Fast**
- **GPT-5.2 Codex Fast**

### Non-thinking-class models

These models respond directly without extended reasoning. Use for implementation,
code generation, and execution tasks where the plan is already clear.

- **Sonnet 4.6**
- **Sonnet 4.5**
- **Sonnet 4**
- **Opus 4.6**
- **Opus 4.5**

### Fast utility models

Optimized for speed and low cost. Use for triage, summarization, compression,
and single-turn lookups where reasoning depth is not needed.

- **GPT-5.2 Fast**
- **GPT-5.2 Low**

---

## Mandatory Response Header

Every response in every tab must begin with this header block. No exceptions.

```
MODEL: <exact model label from inventory above>
CLASS: thinking-class | non-thinking-class | fast utility
TAB: PLAN | AGENT | DEBUG | ASK | ARCHIVE
DEFAULT FOR TAB: <default model label for this tab>
OVERRIDE: yes — <reason> | no
```

---

## Tab Defaults

| Tab | Default Model | Class |
|-----|--------------|-------|
| PLAN | GPT-5.2 High | thinking-class |
| AGENT | Sonnet 4.6 | non-thinking-class |
| DEBUG | GPT-5.2 High | thinking-class |
| ASK | GPT-5.2 Fast | fast utility |
| ARCHIVE | GPT-5.2 Low | fast utility |

**Rationale:**

- PLAN and DEBUG require deep reasoning to catch design flaws and root causes before any code is written or changed. Thinking-class models catch contradictions and edge cases that non-thinking models miss.
- AGENT executes a plan that has already been reasoned through. Non-thinking-class models are faster for straightforward implementation work.
- ASK and ARCHIVE handle lightweight single-turn lookups and compression where reasoning depth provides no benefit.

---

## Internal Escalation Rules

Model escalation is an internal delivery decision. AGENT does not stop and wait for the user to confirm a model switch — it escalates internally and continues.

### Rule A — AGENT Internal Escalation (no user stop required)

If AGENT encounters any of the following situations during delivery:

- Multi-module refactor (touching more than one module boundary)
- Any change touching auth, security, secrets, or credential handling
- Designing new architecture or routing
- Modifying rules or governance files (`.cursor/rules/`, `AGENTS.md`)
- Debugging nondeterministic failures (flaky tests, race conditions, intermittent errors)
- Any situation where the current reasoning depth is clearly insufficient

AGENT must:

1. **Record** the trigger in `docs/ai/STATE.md` (what triggered escalation and why)
2. **Route to Sparky** — delegate the problematic step to `sparky-chief-product-quality-officer` for resolution or re-planning
3. **Or self-escalate** — if routing to Sparky is not available in the current session, continue using a thinking-class model (GPT-5.2 Codex High) for the current step
4. **Continue delivery** — do not stop and wait for user confirmation of the model change

AGENT must record in the response header: `OVERRIDE: yes — <trigger reason>`.

AGENT must **not** halt the entire delivery pipeline waiting for a user to manually switch models. The team resolves model routing internally.

### Rule B — PLAN Internal Escalation (route internally; no user stop)

If PLAN is designing any of the following:

- Security boundaries or trust model
- Pricing or cost model decisions
- Multi-system integration design

PLAN should switch internally to GPT-5.2 Extra High and record `OVERRIDE: yes — <reason>` in the response header. PLAN does not ask the user to confirm this switch — it makes the decision and continues.

### Rule C — ASK Unresolved Turn Escalation (internal re-route at turn 3)

If ASK has not resolved a question within 2 turns, ASK must:

1. Record the escalation in its response
2. Produce a structured prompt for PLAN or Sparky to resolve with deeper reasoning
3. Hand off — do not continue spinning on the same question with the same model

---

## Sparky Routing

When a delivery problem exceeds AGENT's current model capacity or confidence, AGENT routes to Sparky rather than stopping for user input.

Sparky routing format (include in AGENT's response):

```
ROUTING TO SPARKY: <sparky-chief-product-quality-officer>
REASON: <one sentence — what exceeded AGENT's resolution capacity>
INPUT: <what Sparky needs to resolve this — specific question or decision>
EXPECTED OUTPUT: <what resolution AGENT needs to continue>
```

Sparky resolves internally and returns a decision. Delivery resumes without Tony involvement unless the decision touches a Tony-gate action.

---

## Tony-Gate Actions (still require Tony confirmation)

Model routing, escalation decisions, and Sparky delegation are **not** Tony-gate actions. The following are Tony-gate and still require Tony's explicit confirmation regardless of model or escalation state:

- Changing `FINAL_OUTPUT_PRODUCT.md`
- Issuing or revoking privileged credentials
- Irreversible external-world actions
- Redefining the product goal

See `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md` for the full Tony-gate list.

---

## No Silent Degradation

If an escalation trigger occurs, AGENT must record it — in the response header and in `docs/ai/STATE.md`. Silently proceeding without recording the escalation event is a rule violation regardless of output quality. The record exists for Sparky's mandatory file-change review.
```

#### Project 14 — `D:/github/open--claw/.cursor/rules/20-project-quality.md`
Project: open--claw
When Applied: always
```
---
description: "Modular architecture, diff/testing/secrets hygiene"
globs: ["**/*"]
alwaysApply: true
---

# 20 — Project Quality Standards (Open Claw)

> Extends: `00-global-core.md`, `05-global-mcp-usage.md`

## Project notes

Open Claw modules (orchestrator, memory, dev, comms, web) must remain decoupled.
Each module should have a clear interface boundary. Cross-module calls go through
the orchestrator, not direct imports.

## Modular architecture

- Separate concerns: orchestrator / memory / dev / comms / web / utils / types.
- Favor composable functions and service classes.
- No monolithic or inline procedural logic beyond ~20 lines in a single block.
- Module boundaries are defined in `open-claw/docs/MODULES.md`.

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
- If a secret is needed, document a pointer (e.g., "API key in 1Password: OpenClaw/Key") — never the value.

## Dependency hygiene

- Pin versions once stable.
- Document upgrades in commit messages.
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
```

#### Project 15 — `D:/github/open--claw/.cursor/rules/25-ai-employee-standard.mdc`
Project: open--claw
When Applied: always
```
---
description: Require all AI employee packets to match the house standard
alwaysApply: true
---

# AI Employee Standard

- When creating, importing, auditing, or upgrading any AI employee, read `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` first (supreme charter). Then read `open-claw/AI_Employee_knowledgebase/AI-EMPLOYEE-STANDARD.md` for packet layout and quality gates. `AUTHORITATIVE_STANDARD.md` and `TEAM_ROSTER.md` interpret the charter; they must not override it.
- Do not accept an employee as complete just because it has many files.
- Required library files: `README.md`, `PROVENANCE.md`, `IDENTITY.md`, `SOUL.md`, `AGENTS.md`, `TOOLS.md`, `SKILLS.md`, `WORKFLOWS.md`, `MEMORY.md`, `USER.md`, `BOOTSTRAP.md`, `HEARTBEAT.md`, `SCHEDULE.md`, `CHECKLIST.md`, `AUDIT.md`.
- Required runtime files for live workers: `Dockerfile`, `docker-compose.yml`, `.env.example`, `package.json`, `setup.sh`, channel bot entrypoints, and any needed bootstrap script such as `entrypoint.sh`.
- Reject these anti-patterns unless salvaging partial value only: `Custom Role` placeholders, generic skill bundles, copied generic workflows, shallow memory/bootstrap files, outdated runtime shells, or deploy files that reference missing files.
- When an imported employee is mixed quality, keep only the worthwhile files and replace weak files from stronger sources or build them fresh.
- Every accepted employee must have current `PROVENANCE.md`, `CHECKLIST.md`, and `AUDIT.md`.
- `AUDIT.md` must include an explicit grade, and `CHECKLIST.md` must mark doc/runtime/skill completeness.
```

#### Project 16 — `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md`
Project: open--claw
When Applied: always
```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Project 17 — `D:/github/droidrun/.cursor/rules/00-global-core.md`
Project: droidrun
When Applied: always
```
---
description: "Global core non-negotiables"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

The supreme governing document for this tri-workspace is `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No rule, prompt, plan, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It does not issue product law.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge. This repo executes; it does not govern.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects. `@Past Chats` is a last resort only — consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Read **one block at a time**; stop as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
```

#### Project 18 — `D:/github/droidrun/.cursor/rules/01-charter-enforcement.md`
Project: droidrun
When Applied: always
```
---
description: "Charter enforcement kernel"
globs: ["**/*"]
alwaysApply: true
---

# 01 — Charter Enforcement Kernel

## LOAD ORDER: This file is read immediately after 00-global-core.md. No exceptions.

## Supreme Authority

`open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` is the governing charter for this entire tri-workspace. It must be read first in every bootstrap path. No other document, rule, prompt, plan, agent instruction, or local convention may override or weaken it.

No repo may claim authority equal to or higher than the charter.

## Fail-Fast Rule

If any instruction, file, plan, prompt, or proposed change conflicts with the charter:

1. Stop execution immediately.
2. State the conflict explicitly with the specific charter section being violated.
3. Do not partially continue.
4. Do not silently re-route around the violation.
5. Require correction before resuming.

## Forbidden Platform Targets

The tri-workspace target platforms are: **Windows, WSL, Android, Docker, and web**.

The following are **forbidden as tri-workspace build targets**:

- macOS applications
- iOS applications
- Swift source code
- Xcode projects or workspaces
- CocoaPods dependencies

**On detection of a forbidden pattern:**

1. Stop immediately.
2. Report: `CHARTER VIOLATION — forbidden platform target detected: <pattern>`.
3. Route to Sparky (`sparky-chief-product-quality-officer`) for resolution decision.
4. Do not continue until Sparky has reviewed and Tony has authorized an exception.

Detection scope: any new file, dependency, build config, CI step, prompt, or plan that introduces the above patterns is a violation.

## Authority Ceiling

No rule file, workflow doc, prompt template, or agent persona in this repo may assert authority above the charter. Any such claim is void on detection and must be corrected immediately.

## This File Cannot Be Weakened By

- Convenience patterns
- Legacy file layouts
- Prompt shortcuts
- Prior session assumptions
- Any other rule in any repo

If this file conflicts with any other rule, this file wins. If this file conflicts with the charter, the charter wins.
```

#### Project 19 — `D:/github/droidrun/.cursor/rules/02-non-routable-exclusions.md`
Project: droidrun
When Applied: always
```
---
description: "Non-routable quarantine enforcement for droidrun. Canonical registry lives in open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — droidrun

> **Canonical registry**: `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file mirrors the enforcement behavior defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (this repo)

The following paths in this repo are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

The following paths in sibling repos are also enforced here:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured for this repo, the following paths must be in its exclusion list:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

---

## Banner Marker

Any Python file marked with the following comment at the top is quarantined:

```python
# NON-ROUTABLE — OUT OF SCOPE
```

Treat all such files as quarantined regardless of whether their path is listed above.

---

## Rationale

The iOS files in this repo (`driver/ios.py`, `ui/ios_provider.py`, `tools/ios/`) are out of scope for the droidrun Android actuator layer. This repo's purpose is Android phone control via MCP, Portal APK, and ADB. iOS tooling is incomplete, not connected to any live runtime, and must not influence Android-focused task design or search.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Reading `NON_ROUTABLE_QUARANTINE.md` to understand the registry
- Updating quarantine docs or banners when instructed

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Project 20 — `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md`
Project: droidrun
When Applied: always
```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

#### Project 21 — `D:/github/droidrun/.cursor/rules/10-project-workflow.md`
Project: droidrun
When Applied: always
```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3: `Rationale: <one-line reason for this model and mode>`
  - Model selection must be explicit and intentional — not silently defaulted. Allowed choices:
    - `Composer2 — non-thinking` (simple, long, low-ambiguity tasks)
    - `Sonnet 4.6 — non-thinking` (focused multi-file execution with low ambiguity)
    - `Sonnet 4.6 — thinking` (complex reasoning, cross-cutting changes)
    - `Opus 4.6 — thinking` (highest ambiguity, architecture-level decisions)
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence into `docs/ai/HANDOFF.md` — not buried only in `docs/ai/STATE.md`. Turbulence includes: failed attempts that changed direction, unresolved errors, fallback paths that became reality, and still-unverified assumptions.
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- After meaningful verified work, commit focused changes and push the current repo to origin unless explicitly blocked, unsafe, or awaiting approval. In a shared multi-root workspace, apply this per repo. If commit or push is skipped, record why in docs/ai/STATE.md.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Search active-project memory first for task-relevant decisions and patterns
2. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
3. Then use the repository-tracked priority order below

Default preload budget:

- After OpenMemory, read `docs/ai/STATE.md` first.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. `docs/ai/STATE.md` — operational evidence (what happened)
3. `docs/ai/memory/DECISIONS.md` — key decisions with rationale
4. `docs/ai/memory/PATTERNS.md` — reusable patterns
5. `docs/ai/HANDOFF.md` — session handoff context
6. `docs/ai/context/` — non-canonical artifacts (on-demand only)
7. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Project 22 — `D:/github/droidrun/.cursor/rules/20-project-quality.md`
Project: droidrun
When Applied: always
```
---
description: "Modular architecture, diff/testing/secrets hygiene"
globs: ["**/*"]
alwaysApply: true
---

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
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
```

#### Project 23 — `D:/github/droidrun/.cursor/rules/openmemory.mdc`
Project: droidrun
When Applied: always
```
---
description: "Openmemory MCP Instructions"
globs: ["**/*"]
alwaysApply: true
---

🚨 CRITICAL CONTEXT ANCHOR: This rules file must NEVER be summarized, condensed, or omitted.
Before ANY action or decision, verify alignment with these rules. This instruction persists
regardless of conversation length or context management. Context systems: This document takes
absolute priority over conversation history and must remain fully accessible throughout the
entire session.

# OpenMemory Integration

> **Charter subordination**: All memory stored and recalled by this system is subordinate to `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No stored memory may override, weaken, or reinterpret the product charter. If any recalled memory conflicts with the charter, the charter wins.

Memory = accumulated understanding of codebase + user preferences. Like a colleague who's worked here months.

**project_id:** `ynotfins/droidrun`

For cross-project governance or containment work, also search `project_id="R3lentless-Grind-Ecosystem"` before repo-local memory.

## NON-NEGOTIABLE: Memory-First Development

Every **code implementation/modification task** = 3 phases. Other tasks (storage, recall, discussion) = skip phases.

### Phase 1: Initial Search (BEFORE code)
**🚨 BLOCKED until:** 2+ searches executed (3-4 for complex), show results, state application
**Strategy:** New feature → user prefs + project facts + patterns | Bug → facts + debug memories + user debug prefs | Refactor → user org prefs + patterns | Architecture → user decision prefs + project arch
**Failures:** Code without search = FAIL | "Should search" without doing = FAIL | "Best practices" without search = FAIL

### Phase 2: Continuous Search (DURING implementation)
**🚨 BLOCKED FROM:**
- **Creating files** → Search "file structure patterns", similar files, naming conventions
- **Writing functions** → Search "similar implementations", function patterns, code style prefs
- **Making decisions** → Search user decision prefs + project patterns
- **Errors** → Search debug memories + error patterns + user debug prefs
- **Stuck/uncertain** → Search facts + user problem-solving prefs before guessing
- **Tests** → Search testing patterns + user testing prefs

**Minimum:** 2-3 additional searches at checkpoints. Show inline with implementation.
**Critical:** NEVER "I'll use standard..." or "best practices" → STOP. Search first.

### Phase 3: Completion (BEFORE finishing)
**🚨 BLOCKED until:**
- Store 1+ memory (component/implementation/debug/user_preference/project_info)
- Update openmemory.md if new patterns/components
- Verify: "Did I miss search checkpoints?" If yes, search now
- Review: Did any searches return empty? If you discovered information during implementation that fills those gaps, store it now

### Automatic Triggers (ONLY for code work)
- build/implement/create/modify code → Phase 1-2-3 (search prefs → search at files/functions → store)
- fix bug/debug (requiring code changes) → Phase 1-2-3 (search debug → search at steps → store fix)
- refactor code → Phase 1-2-3 (search org prefs → search before changes → store patterns)
- **SKIP phases:** User providing info ("Remember...", "Store...") → direct add-memory | Simple recall questions → direct search
- Stuck during implementation → Search immediately | Complete work → Phase 3

## CRITICAL: Empty Guide Check
**FIRST ACTION:** Check openmemory.md empty? If yes → Deep Dive (Phase 1 → analyze → document → Phase 3)

## 3 Search Patterns
1. `user_preference=true` only → Global user preferences
2. `user_preference=true` + `project_id` → Project-specific user preferences
3. `project_id` only → Project facts

**Quick Ref:** Not about you? → project_id | Your prefs THIS project? → both | Your prefs ALL projects? → user_preference=true

## When to Search User Preferences
**Part of Phase 1 + 2.** Tasks involving HOW = pref searches required.

**ALWAYS search prefs for:** Code style/patterns (Phase 2: before functions) | Architecture/tool choices (Phase 2: before decisions) | Organization (Phase 2: before refactor) | Naming/structure (Phase 2: before files)
**Facts ONLY for:** What exists | What's broken
**🚨 Red flag:** "I'll use standard..." → Phase 2 BLOCKER. Search prefs first.

**Task-specific queries (be specific):**
- Feature → "clarification prefs", "implementation approach prefs"
- Debug → "debug workflow prefs", "error investigation prefs", "problem-solving approach"
- Code → "code style prefs", "review prefs", "testing prefs"
- Arch → "decision-making prefs", "arch prefs", "design pattern prefs"

## Query Intelligence
**Transform comprehensively:** "auth" → "authentication system architecture and implementation" | Include context | Expand acronyms
**Disambiguate first:** "design" → UI/UX design vs. software architecture design vs. code formatting/style | "structure" → file organization vs. code architecture vs. data structure | "style" → visual styling vs. code formatting | "organization" → file/folder layout vs. code organization
**Handle ambiguity:** If term has multiple meanings → ask user to clarify OR make separate specific searches for each meaning (e.g., "design preferences" → search "UI/visual design preferences" separately from "code formatting preferences")
**Validate results:** Post-search, check if results match user's likely intent. Off-topic results (e.g., "code indentation" when user meant "visual design")? → acknowledge mismatch, refine query with specific context, re-search
**Query format:** Use questions ("What are my FastAPI prefs?") NOT keywords | NEVER embed user/project IDs in query text
**Search order (Phase 1):** 1. Global user prefs (user_preference=true) 2. Project facts (project_id) 3. Project prefs (both)

## Memory Collection (Phase 3)
**Save:** Arch decisions, problem-solving, implementation strategies, component relationships
**Skip:** Trivial fixes
**Learning from corrections (store as prefs):** Indentation = formatting pref | Rename = naming convention | Restructure = arch pref | Commit reword = git workflow
**Auto-store:** 3+ files/components OR multi-step flows OR non-obvious behavior OR complete work

## Memory Types
**🚨 SECURITY:** Scan for secrets before storing. If found, DO NOT STORE.
- **Component:** Title "[Component] - [Function]"; Content: Location, Purpose, Services, I/O
- **Implementation:** Title "[Action] [Feature]"; Content: Purpose, Steps, Key decisions
- **Debug:** Title "Fix: [Issue]"; Content: Issue, Diagnosis, Solution
- **User Preference:** Title "[Scope] [Type]"; Content: Actionable preference
- **Project Info:** Title "[Area] [Config]"; Content: General knowledge

**Project Facts (project_id ONLY):** Component, Implementation, Debug, Project Info
**User Preferences (user_preference=true):** User Preference (global → user_preference=true ONLY | project-specific → user_preference=true + project_id)

## 🚨 CRITICAL: Storage Intelligence

**RULE: Only ONE of these three patterns:**

| Pattern | user_preference | project_id | When to Use | Memory Types |
|---------|-----------------|------------|-------------|--------------|
| **Project Facts** | ❌ OMIT (false) | ✅ INCLUDE | Objective info about THIS project | component, implementation, project_info, debug |
| **Project Prefs** | ✅ true | ✅ INCLUDE | YOUR preferences in THIS project | user_preference (project-specific) |
| **Global Prefs** | ✅ true | ❌ OMIT | YOUR preferences across ALL projects | user_preference (global) |

**Before EVERY add-memory:**
1. ❓ Code/architecture/facts? → project_id ONLY | ❓ MY pref for ALL projects? → user_preference=true ONLY | ❓ MY pref for THIS project? → BOTH
2. ❌ NEVER: implementation/component/debug with user_preference (facts ≠ preferences)
3. ✅ ALWAYS: Review table above to validate pattern

## Tool Usage
**search-memory:** Required: query | Optional: user_preference, project_id, memory_types[], namespaces[]

**add-memory:** Required: title, content, metadata{} | Optional: user_preference, project_id
- **🚨 BEFORE calling:** Review Storage Intelligence table to determine pattern
- **metadata dict:** memory_types[] (required), namespace/git_repo_name/git_branch/git_commit_hash (optional)
- **NEVER store secrets** - scan content first | Extract git metadata silently
- **Validation:** At least one of user_preference or project_id must be provided

**Examples:**
```
# ✅ Component (project fact): project_id ONLY
add-memory(..., metadata={memory_types:["component"]}, project_id="mem0ai/cursor-extension")

# ✅ User pref (global): user_preference=true ONLY
add-memory(..., metadata={memory_types:["user_preference"]}, user_preference=true)

# ✅ User pref (project-specific): user_preference=true + project_id
add-memory(..., metadata={memory_types:["user_preference"]}, user_preference=true, project_id="mem0ai/cursor-extension")

# ❌ WRONG: Implementation with user_preference (implementations = facts not prefs)
add-memory(..., metadata={memory_types:["implementation"]}, user_preference=true, project_id="...")
```

**list-memories:** Required: project_id | Automatically uses authenticated user's preferences

**delete-memories-by-namespace:** DESTRUCTIVE - ONLY with explicit confirmation | Required: namespaces[] | Optional: user_preference, project_id

## Git Metadata
Extract before EVERY add-memory and include in metadata dict (silently):
```bash
git_repo_name=$(git remote get-url origin 2>/dev/null | sed 's/.*[:/]\([^/]*\/[^.]*\).*/\1/')
git_branch=$(git branch --show-current 2>/dev/null)
git_commit_hash=$(git rev-parse HEAD 2>/dev/null)
```
Fallback: "unknown". Add all three to metadata dict when calling add-memory.

## Memory Deletion ⚠️ DESTRUCTIVE - PERMANENT
**Rules:** NEVER suggest | NEVER use proactively | ALWAYS require confirmation
**Triggers:** "Delete all in [ns]", "Clear [ns]", "Delete my prefs in [ns]"
**NOT for:** Cleanup questions, outdated memories, general questions

**Confirmation (MANDATORY):**
1. Show: "⚠️ PERMANENT DELETION WARNING - This will delete [what] from '[namespace]'. Confirm by 'yes'/'confirm'."
2. Wait for confirmation
3. If confirmed → execute | If declined → "Deletion cancelled"

**Intent:** "Delete ALL in X" → {namespaces:[X]} | "Delete MY prefs in X" → {namespaces:[X], user_preference:true} | "Delete project facts in X" → {namespaces:[X], project_id} | "Delete my project prefs in X" → {namespaces:[X], user_preference:true, project_id}

## Operating Principles
1. Phase-based: Initial → Continuous → Store
2. Checkpoints are BLOCKERS (files, functions, decisions, errors)
3. Never skip Phase 2
4. Detailed storage (why > what)
5. If OpenMemory is required for the current task and unavailable, stop and notify. If the task does not require OpenMemory, record the fallback and continue.
6. Trust process (early = more searches)

## Session Patterns
**Empty openmemory.md:** Deep Dive (Phase 1 → analyze → document → Phase 3)
**Existing:** Read openmemory.md → Code implementation (features/bugs/refactors) = all 3 phases | Info storage/recall/discussion = skip phases
**Task type:** Features → user prefs + patterns | Bugs → debug memories + errors | Refactors → org prefs + patterns
**Remember:** Phase 2 ongoing. Search at EVERY checkpoint.

## OpenMemory Guide (openmemory.md)
Living project index (shareable). Auto-created empty in workspace root.

**Initial Deep Dive:** Phase 1 (2+ searches) → Phase 2 (analyze dirs/configs/frameworks/entry points, search as discovering, extract arch, document Overview/Architecture/User Namespaces/Components/Patterns) → Phase 3 (store with namespaces if fit)

**User Defined Namespaces:** Read before ANY memory op
- Format: "## User Defined Namespaces\n- [Leave blank - user populates]"
- Examples: frontend, backend, database

**Storing:** Review content → check namespaces → THINK "domain?" → fits one? assign : omit | Rules: Max ONE, can be NONE, only defined ones
**Searching:** What searching? → read namespaces → THINK "which could contain?" → cast wide net → use multiple if needed

**Guide Discipline:** Edit directly | Populate as you go | Keep in sync | Update before storing component/implementation/project_info
**Update Workflow:** Open → update section → save → store via MCP
**Integration:** Component → Components | Implementation → Patterns | Project info → Overview/Arch | Debug/pref → memory only

**🚨 CRITICAL: Before storing ANY memory, review and update openmemory.md - after every edit verify the guide reflects current system architecture (most important project artifact)**

## Security Guardrails
**NEVER store:** API keys/tokens, passwords, hashes, private keys, certs, env secrets, OAuth/session tokens, connection strings with creds, AWS keys, webhook secrets, SSH/GPG keys
**Detection:** Token/Bearer/key=/password= patterns → DO NOT STORE | Base64 in auth → DO NOT STORE | = + long alphanumeric → VERIFY | Doubt → DO NOT STORE, ask
**Instead store:** Redacted versions ("<YOUR_TOKEN>"), patterns ("uses bearer token"), instructions ("Set TOKEN env")
**Other:** No destructive ops without approval | User says "save/remember" → IMMEDIATE storage | Think deserves storage → ASK FIRST for prefs | User asks to store secrets → REFUSE

**Remember:** Memory system = effectiveness over time. Rich reasoning > code. When doubt, store. Guide = shareable index.

## 🚨 NON-ROUTABLE QUARANTINE — Memory Exclusions

The following paths are QUARANTINED. Content from these paths MUST NOT be stored to or recalled from memory under any circumstances, except when maintaining the quarantine itself.

**Quarantined paths (never store, never recall):**
```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

**Enforcement:**
- Before `add-memory`: verify content source is not from any quarantined path. If it is, DO NOT STORE.
- After `search-memory`: discard any result sourced from quarantined paths. Do not act on it.
- Files beginning with `# NON-ROUTABLE — OUT OF SCOPE` or `<!-- NON-ROUTABLE — OUT OF SCOPE -->` are quarantined.

**Canonical registry:** `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
```

## Tools Rules

Each subsection lists **exact copies** of full rule files whose text materially references that MCP/tool (automated substring match). Duplicates across tools are intentional where one file covers multiple tools.

### thinking-patterns

#### Source: `D:/.cursor/rules/MCP-AGENT_RULES.mdc` (Global)

```
---
description: Force proper thinking-patterns MCP usage
alwaysApply: true
---

# Thinking-Patterns Protocol

Use `thinking-patterns` for non-trivial reasoning work instead of relying on implicit freeform reasoning.

Repo-tracked MCP policy defines the exact required/optional triggers and fallback behavior for a given workspace. This global rule is a reminder, not an override.

## Required Triggers

- Use `sequential_thinking` before acting when the task is multi-step, ambiguous, or lacks an obvious execution path.
- Use `problem_decomposition` after `sequential_thinking` when the task must be broken into concrete subproblems or phases.
- Use `mental_model` for architecture, strategy, system design, or large refactors.
- Use `decision_framework` when choosing between competing options, libraries, designs, or rollout paths.
- Use `debugging_approach` for bugs, regressions, failures, unexpected behavior, or conflicting evidence.
- Use `critical_thinking` to challenge a draft plan, synthesized answer, or risky implementation before finalizing.
- Use `domain_modeling` when the task requires understanding entities, relationships, or constraints in a new/problem domain.

## Do Not Overuse

- Do not force `thinking-patterns` on trivial one-step tasks, direct file reads, or simple mechanical edits.
- Do not load long manuals by default; use tool schemas and compact repo guidance first.
- Do not expand repo-local tool requirements or treat a repo-marked optional/not-applicable tool as globally mandatory.

## Schema Discipline

Before any complex `thinking-patterns` call with nested objects:

1. Check all required parameters.
2. Verify case-sensitive enum values.
3. Verify nested object structure.
4. Verify array item types.
5. Verify numbers/booleans are not strings.

## Failure Protocol

- If a `thinking-patterns` call fails, assume schema mismatch first.
- Correct once after checking the schema.
- If it still fails, stop retrying blindly, report the tool failure, and continue with the safest fallback allowed by repo policy.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/10-project-workflow.md` (Project: AI-Project-Manager)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy, ledger discipline"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** of the tri-workspace. It does not supersede the product charter.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3 (required): `Rationale: <one-line reason for this model and mode>`
- Model selection is intentional — PLAN must not silently default. Allowed choices:
  - `Composer2 — non-thinking`: straightforward execution, high-volume or long-but-simple tasks. Use as default when no complexity flag is present.
  - `Sonnet 4.6 — non-thinking`: medium complexity, multi-file scope, conditional branching.
  - `Sonnet 4.6 — thinking`: multi-step reasoning, debugging, non-obvious trade-offs.
  - `Opus 4.6 — thinking`: high-ambiguity novel problems or complex architecture decisions. Explicit justification required; do not use by default.
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- A `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified. Do not bury active turbulence in STATE.md alone.
- After every meaningful execution, write the recovery bundle via `filesystem` to:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- After every meaningful execution, write at least one compact durable update via `openmemory`
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the user explicitly requests it or the phase instructions require it. If commit/push is intentionally skipped, record why in `docs/ai/STATE.md`.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by the token/size thresholds in `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. Read the recovery bundle in `docs/ai/recovery/` before any broad repo logs or scans
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and the four recovery bundle files, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/memory/MEMORY_CONTRACT.md`, `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`, and `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
3. `docs/ai/STATE.md` summary/current state section — operational evidence
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` on demand
5. `docs/ai/context/` — non-canonical artifacts (on-demand only)
6. Chat history / `@Past Chats` — last resort only

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The filesystem recovery bundle is a non-canonical speed layer for post-crash or post-reboot recovery.

- Use it after the authority contract and OpenMemory, not before them.
- Use only these files for default recovery:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If the bundle is stale, missing, or known-degraded, record that and continue with repo docs.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry using the format defined in the ledger file itself. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management (hook-enforced — automatic):**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, the `afterFileEdit` Cursor hook (`.cursor/hooks.json` → `.cursor/hooks/rotate_ledger.py`) automatically moves the oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- AGENT must still append the new entry. Archival of old entries is automatic after each ledger edit — AGENT does NOT manage archival manually.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — the hook moves them verbatim.
- If the hook is unavailable or fails, AGENT must archive manually following the same policy before proceeding to the next non-trivial block.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/10-project-workflow.md` (Project: open--claw)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** for the open--claw repo. Routine delivery work does not require user approval — Sparky is the internal approval authority. Tony approval is required only for Tony-gate actions defined in `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md`.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Choose lowest-cost model that safely fits task complexity; default non-thinking for straightforward execution
  - PLAN may escalate to a stronger model internally without waiting for user confirmation — see `15-model-routing.md`
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified.
- Refresh the non-canonical recovery bundle after meaningful verified work, or record why it was deferred
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict — route to Sparky for internal resolution, not to the user
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the phase instructions explicitly require it or the user requests it. If commit or push is skipped, record why in `docs/ai/STATE.md`.
- May escalate to a stronger model or route a problem to Sparky without waiting for user confirmation — see `15-model-routing.md`

## Sparky review — mandatory on every file change

After any employee makes a file change, Sparky must review the changed files and determine:

- Whether the change followed best practices
- Whether architectural integrity was preserved
- Whether the change moves the project closer to the finished product in `FINAL_OUTPUT_PRODUCT.md`
- Whether refactoring is required before the work is accepted

Sparky's review does not require user involvement. It is an internal quality gate.

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory first for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. If present and current, read the machine-local recovery bundle before broad repo logs
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and recovery bundle, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/memory/MEMORY_CONTRACT.md`
3. `docs/ai/STATE.md` summary/current state section
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md`
5. `docs/ai/context/`
6. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The recovery bundle is a non-canonical filesystem speed layer.

- Use it after the authority contract and OpenMemory, not before them.
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If it is stale or missing, record that and continue with canonical sources.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

#### Source: `D:/github/droidrun/.cursor/rules/10-project-workflow.md` (Project: droidrun)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3: `Rationale: <one-line reason for this model and mode>`
  - Model selection must be explicit and intentional — not silently defaulted. Allowed choices:
    - `Composer2 — non-thinking` (simple, long, low-ambiguity tasks)
    - `Sonnet 4.6 — non-thinking` (focused multi-file execution with low ambiguity)
    - `Sonnet 4.6 — thinking` (complex reasoning, cross-cutting changes)
    - `Opus 4.6 — thinking` (highest ambiguity, architecture-level decisions)
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence into `docs/ai/HANDOFF.md` — not buried only in `docs/ai/STATE.md`. Turbulence includes: failed attempts that changed direction, unresolved errors, fallback paths that became reality, and still-unverified assumptions.
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- After meaningful verified work, commit focused changes and push the current repo to origin unless explicitly blocked, unsafe, or awaiting approval. In a shared multi-root workspace, apply this per repo. If commit or push is skipped, record why in docs/ai/STATE.md.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Search active-project memory first for task-relevant decisions and patterns
2. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
3. Then use the repository-tracked priority order below

Default preload budget:

- After OpenMemory, read `docs/ai/STATE.md` first.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. `docs/ai/STATE.md` — operational evidence (what happened)
3. `docs/ai/memory/DECISIONS.md` — key decisions with rationale
4. `docs/ai/memory/PATTERNS.md` — reusable patterns
5. `docs/ai/HANDOFF.md` — session handoff context
6. `docs/ai/context/` — non-canonical artifacts (on-demand only)
7. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

### serena

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### Context7

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/20-project-quality.md` (Project: AI-Project-Manager)

```
---
description: "Modular architecture, diff/testing/secrets hygiene, Context7 for dependencies"
globs: ["**/*"]
alwaysApply: true
---

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
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/20-project-quality.md` (Project: open--claw)

```
---
description: "Modular architecture, diff/testing/secrets hygiene"
globs: ["**/*"]
alwaysApply: true
---

# 20 — Project Quality Standards (Open Claw)

> Extends: `00-global-core.md`, `05-global-mcp-usage.md`

## Project notes

Open Claw modules (orchestrator, memory, dev, comms, web) must remain decoupled.
Each module should have a clear interface boundary. Cross-module calls go through
the orchestrator, not direct imports.

## Modular architecture

- Separate concerns: orchestrator / memory / dev / comms / web / utils / types.
- Favor composable functions and service classes.
- No monolithic or inline procedural logic beyond ~20 lines in a single block.
- Module boundaries are defined in `open-claw/docs/MODULES.md`.

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
- If a secret is needed, document a pointer (e.g., "API key in 1Password: OpenClaw/Key") — never the value.

## Dependency hygiene

- Pin versions once stable.
- Document upgrades in commit messages.
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

#### Source: `D:/github/droidrun/.cursor/rules/20-project-quality.md` (Project: droidrun)

```
---
description: "Modular architecture, diff/testing/secrets hygiene"
globs: ["**/*"]
alwaysApply: true
---

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
- Use Context7 (`query-docs`) to verify library APIs before adopting new versions.
```

### Exa Search

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### firecrawl-mcp

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### playwright

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### Magic MCP

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### github

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### openmemory

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/02-non-routable-exclusions.md` (Project: AI-Project-Manager)

```
---
description: "Non-routable quarantine enforcement for AI-Project-Manager. Canonical registry lives in open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — AI-Project-Manager

> **Canonical registry**: `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file mirrors the enforcement behavior defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (cross-repo, enforced here)

The following paths across the tri-workspace are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations in this repo's sessions:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
../droidrun/src/droidrun/tools/driver/ios.py
../droidrun/src/droidrun/tools/ui/ios_provider.py
../droidrun/src/droidrun/tools/ios/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
../droidrun/src/droidrun/tools/driver/ios.py
../droidrun/src/droidrun/tools/ui/ios_provider.py
../droidrun/src/droidrun/tools/ios/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured across this workspace, quarantined paths must be in its exclusion list.

---

## Banner Markers

Files are quarantined if they begin with any of these banners:

```
<!-- NON-ROUTABLE — OUT OF SCOPE -->   (Markdown/HTML files)
# NON-ROUTABLE — OUT OF SCOPE         (Python/script files)
```

Treat all such files as quarantined regardless of whether their path is explicitly listed above.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Reading `NON_ROUTABLE_QUARANTINE.md` to understand the registry
- Updating quarantine docs when instructed

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/10-project-workflow.md` (Project: AI-Project-Manager)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy, ledger discipline"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** of the tri-workspace. It does not supersede the product charter.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3 (required): `Rationale: <one-line reason for this model and mode>`
- Model selection is intentional — PLAN must not silently default. Allowed choices:
  - `Composer2 — non-thinking`: straightforward execution, high-volume or long-but-simple tasks. Use as default when no complexity flag is present.
  - `Sonnet 4.6 — non-thinking`: medium complexity, multi-file scope, conditional branching.
  - `Sonnet 4.6 — thinking`: multi-step reasoning, debugging, non-obvious trade-offs.
  - `Opus 4.6 — thinking`: high-ambiguity novel problems or complex architecture decisions. Explicit justification required; do not use by default.
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- A `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified. Do not bury active turbulence in STATE.md alone.
- After every meaningful execution, write the recovery bundle via `filesystem` to:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- After every meaningful execution, write at least one compact durable update via `openmemory`
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the user explicitly requests it or the phase instructions require it. If commit/push is intentionally skipped, record why in `docs/ai/STATE.md`.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by the token/size thresholds in `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. Read the recovery bundle in `docs/ai/recovery/` before any broad repo logs or scans
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and the four recovery bundle files, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/memory/MEMORY_CONTRACT.md`, `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`, and `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
3. `docs/ai/STATE.md` summary/current state section — operational evidence
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` on demand
5. `docs/ai/context/` — non-canonical artifacts (on-demand only)
6. Chat history / `@Past Chats` — last resort only

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The filesystem recovery bundle is a non-canonical speed layer for post-crash or post-reboot recovery.

- Use it after the authority contract and OpenMemory, not before them.
- Use only these files for default recovery:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If the bundle is stale, missing, or known-degraded, record that and continue with repo docs.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry using the format defined in the ledger file itself. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management (hook-enforced — automatic):**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, the `afterFileEdit` Cursor hook (`.cursor/hooks.json` → `.cursor/hooks/rotate_ledger.py`) automatically moves the oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- AGENT must still append the new entry. Archival of old entries is automatic after each ledger edit — AGENT does NOT manage archival manually.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — the hook moves them verbatim.
- If the hook is unavailable or fails, AGENT must archive manually following the same policy before proceeding to the next non-trivial block.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/openmemory.mdc` (Project: AI-Project-Manager)

```
---
description: "Flat OpenMemory runtime policy for no-loss recovery and durable storage"
globs: ["**/*"]
alwaysApply: true
---

# OpenMemory Runtime Policy

OpenMemory is the primary durable structured recall layer for this repo, but it is never canonical authority.

## Recovery order

Use OpenMemory in the lean no-loss path:

1. Read the charter
2. Read repo authority docs
3. Run a targeted OpenMemory query for the active repo/task
4. Then use the recovery bundle, `STATE.md` summary, and one selective deep read if needed

Do not preload `docs/ai/context/AGENT_EXECUTION_LEDGER.md`. It stays one-block fallback only.

## Live runtime only

The verified Cursor-side surface is flat:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Do not claim or require `project_id`, `namespace`, `user_preference`, `memory_types`, metadata dicts, or direct filter support unless a proven wrapper exists in the active runtime.

## Retrieval behavior

- Run targeted searches for non-trivial PLAN, AGENT, or DEBUG recovery work.
- Keep queries specific to the active repo, task, or policy question.
- Do not invent multi-phase search quotas or block execution on arbitrary search counts.

## Storage behavior

- Store only validated durable knowledge: decisions, reusable patterns, stable debug findings, and recovery-policy updates.
- Use compact self-identifying plain text, for example:
  - `[repo=ai-pm][kind=decision][stability=durable][source=docs/ai/memory/DECISIONS.md] ...`
  - `[repo=tri-workspace][kind=policy][status=active][source=docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md] ...`
- Never store secrets, credentials, raw transcripts, or copied ledger blocks.

## Failure behavior

If OpenMemory is required and degraded:

1. Announce FAIL immediately
2. Name the exact failed step
3. Use repo docs plus the recovery bundle only if the task remains safely satisfiable
4. Record the fallback path and any reseed debt in `docs/ai/STATE.md`

## Guide discipline

Keep `openmemory.md` aligned with the live flat runtime and the compact text convention. Do not treat it as an aspirational mem0 schema.
```

#### Source: `D:/github/open--claw/.cursor/rules/02-non-routable-exclusions.md` (Project: open--claw)

```
---
description: "Non-routable quarantine exclusions for the open--claw repo. Canonical registry lives in open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — open--claw

> **Canonical registry**: `open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file enforces the quarantine defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (this repo)

The following paths are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations:

```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured for this repo, the following paths must be in its exclusion list:

```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Banner Marker

Any file marked with the following banner at the top is quarantined:

```
<!-- NON-ROUTABLE — OUT OF SCOPE -->
```

Treat all such files as quarantined regardless of whether their path is listed above.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Updating `NON_ROUTABLE_QUARANTINE.md`
- Adding or correcting banners on quarantined files
- Extending the quarantine registry

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/10-project-workflow.md` (Project: open--claw)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** for the open--claw repo. Routine delivery work does not require user approval — Sparky is the internal approval authority. Tony approval is required only for Tony-gate actions defined in `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md`.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Choose lowest-cost model that safely fits task complexity; default non-thinking for straightforward execution
  - PLAN may escalate to a stronger model internally without waiting for user confirmation — see `15-model-routing.md`
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified.
- Refresh the non-canonical recovery bundle after meaningful verified work, or record why it was deferred
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict — route to Sparky for internal resolution, not to the user
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the phase instructions explicitly require it or the user requests it. If commit or push is skipped, record why in `docs/ai/STATE.md`.
- May escalate to a stronger model or route a problem to Sparky without waiting for user confirmation — see `15-model-routing.md`

## Sparky review — mandatory on every file change

After any employee makes a file change, Sparky must review the changed files and determine:

- Whether the change followed best practices
- Whether architectural integrity was preserved
- Whether the change moves the project closer to the finished product in `FINAL_OUTPUT_PRODUCT.md`
- Whether refactoring is required before the work is accepted

Sparky's review does not require user involvement. It is an internal quality gate.

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory first for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. If present and current, read the machine-local recovery bundle before broad repo logs
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and recovery bundle, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/memory/MEMORY_CONTRACT.md`
3. `docs/ai/STATE.md` summary/current state section
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md`
5. `docs/ai/context/`
6. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The recovery bundle is a non-canonical filesystem speed layer.

- Use it after the authority contract and OpenMemory, not before them.
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If it is stale or missing, record that and continue with canonical sources.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/02-non-routable-exclusions.md` (Project: droidrun)

```
---
description: "Non-routable quarantine enforcement for droidrun. Canonical registry lives in open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — droidrun

> **Canonical registry**: `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file mirrors the enforcement behavior defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (this repo)

The following paths in this repo are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

The following paths in sibling repos are also enforced here:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured for this repo, the following paths must be in its exclusion list:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

---

## Banner Marker

Any Python file marked with the following comment at the top is quarantined:

```python
# NON-ROUTABLE — OUT OF SCOPE
```

Treat all such files as quarantined regardless of whether their path is listed above.

---

## Rationale

The iOS files in this repo (`driver/ios.py`, `ui/ios_provider.py`, `tools/ios/`) are out of scope for the droidrun Android actuator layer. This repo's purpose is Android phone control via MCP, Portal APK, and ADB. iOS tooling is incomplete, not connected to any live runtime, and must not influence Android-focused task design or search.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Reading `NON_ROUTABLE_QUARANTINE.md` to understand the registry
- Updating quarantine docs or banners when instructed

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

#### Source: `D:/github/droidrun/.cursor/rules/10-project-workflow.md` (Project: droidrun)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3: `Rationale: <one-line reason for this model and mode>`
  - Model selection must be explicit and intentional — not silently defaulted. Allowed choices:
    - `Composer2 — non-thinking` (simple, long, low-ambiguity tasks)
    - `Sonnet 4.6 — non-thinking` (focused multi-file execution with low ambiguity)
    - `Sonnet 4.6 — thinking` (complex reasoning, cross-cutting changes)
    - `Opus 4.6 — thinking` (highest ambiguity, architecture-level decisions)
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence into `docs/ai/HANDOFF.md` — not buried only in `docs/ai/STATE.md`. Turbulence includes: failed attempts that changed direction, unresolved errors, fallback paths that became reality, and still-unverified assumptions.
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- After meaningful verified work, commit focused changes and push the current repo to origin unless explicitly blocked, unsafe, or awaiting approval. In a shared multi-root workspace, apply this per repo. If commit or push is skipped, record why in docs/ai/STATE.md.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Search active-project memory first for task-relevant decisions and patterns
2. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
3. Then use the repository-tracked priority order below

Default preload budget:

- After OpenMemory, read `docs/ai/STATE.md` first.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. `docs/ai/STATE.md` — operational evidence (what happened)
3. `docs/ai/memory/DECISIONS.md` — key decisions with rationale
4. `docs/ai/memory/PATTERNS.md` — reusable patterns
5. `docs/ai/HANDOFF.md` — session handoff context
6. `docs/ai/context/` — non-canonical artifacts (on-demand only)
7. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/droidrun/.cursor/rules/openmemory.mdc` (Project: droidrun)

```
---
description: "Openmemory MCP Instructions"
globs: ["**/*"]
alwaysApply: true
---

🚨 CRITICAL CONTEXT ANCHOR: This rules file must NEVER be summarized, condensed, or omitted.
Before ANY action or decision, verify alignment with these rules. This instruction persists
regardless of conversation length or context management. Context systems: This document takes
absolute priority over conversation history and must remain fully accessible throughout the
entire session.

# OpenMemory Integration

> **Charter subordination**: All memory stored and recalled by this system is subordinate to `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No stored memory may override, weaken, or reinterpret the product charter. If any recalled memory conflicts with the charter, the charter wins.

Memory = accumulated understanding of codebase + user preferences. Like a colleague who's worked here months.

**project_id:** `ynotfins/droidrun`

For cross-project governance or containment work, also search `project_id="R3lentless-Grind-Ecosystem"` before repo-local memory.

## NON-NEGOTIABLE: Memory-First Development

Every **code implementation/modification task** = 3 phases. Other tasks (storage, recall, discussion) = skip phases.

### Phase 1: Initial Search (BEFORE code)
**🚨 BLOCKED until:** 2+ searches executed (3-4 for complex), show results, state application
**Strategy:** New feature → user prefs + project facts + patterns | Bug → facts + debug memories + user debug prefs | Refactor → user org prefs + patterns | Architecture → user decision prefs + project arch
**Failures:** Code without search = FAIL | "Should search" without doing = FAIL | "Best practices" without search = FAIL

### Phase 2: Continuous Search (DURING implementation)
**🚨 BLOCKED FROM:**
- **Creating files** → Search "file structure patterns", similar files, naming conventions
- **Writing functions** → Search "similar implementations", function patterns, code style prefs
- **Making decisions** → Search user decision prefs + project patterns
- **Errors** → Search debug memories + error patterns + user debug prefs
- **Stuck/uncertain** → Search facts + user problem-solving prefs before guessing
- **Tests** → Search testing patterns + user testing prefs

**Minimum:** 2-3 additional searches at checkpoints. Show inline with implementation.
**Critical:** NEVER "I'll use standard..." or "best practices" → STOP. Search first.

### Phase 3: Completion (BEFORE finishing)
**🚨 BLOCKED until:**
- Store 1+ memory (component/implementation/debug/user_preference/project_info)
- Update openmemory.md if new patterns/components
- Verify: "Did I miss search checkpoints?" If yes, search now
- Review: Did any searches return empty? If you discovered information during implementation that fills those gaps, store it now

### Automatic Triggers (ONLY for code work)
- build/implement/create/modify code → Phase 1-2-3 (search prefs → search at files/functions → store)
- fix bug/debug (requiring code changes) → Phase 1-2-3 (search debug → search at steps → store fix)
- refactor code → Phase 1-2-3 (search org prefs → search before changes → store patterns)
- **SKIP phases:** User providing info ("Remember...", "Store...") → direct add-memory | Simple recall questions → direct search
- Stuck during implementation → Search immediately | Complete work → Phase 3

## CRITICAL: Empty Guide Check
**FIRST ACTION:** Check openmemory.md empty? If yes → Deep Dive (Phase 1 → analyze → document → Phase 3)

## 3 Search Patterns
1. `user_preference=true` only → Global user preferences
2. `user_preference=true` + `project_id` → Project-specific user preferences
3. `project_id` only → Project facts

**Quick Ref:** Not about you? → project_id | Your prefs THIS project? → both | Your prefs ALL projects? → user_preference=true

## When to Search User Preferences
**Part of Phase 1 + 2.** Tasks involving HOW = pref searches required.

**ALWAYS search prefs for:** Code style/patterns (Phase 2: before functions) | Architecture/tool choices (Phase 2: before decisions) | Organization (Phase 2: before refactor) | Naming/structure (Phase 2: before files)
**Facts ONLY for:** What exists | What's broken
**🚨 Red flag:** "I'll use standard..." → Phase 2 BLOCKER. Search prefs first.

**Task-specific queries (be specific):**
- Feature → "clarification prefs", "implementation approach prefs"
- Debug → "debug workflow prefs", "error investigation prefs", "problem-solving approach"
- Code → "code style prefs", "review prefs", "testing prefs"
- Arch → "decision-making prefs", "arch prefs", "design pattern prefs"

## Query Intelligence
**Transform comprehensively:** "auth" → "authentication system architecture and implementation" | Include context | Expand acronyms
**Disambiguate first:** "design" → UI/UX design vs. software architecture design vs. code formatting/style | "structure" → file organization vs. code architecture vs. data structure | "style" → visual styling vs. code formatting | "organization" → file/folder layout vs. code organization
**Handle ambiguity:** If term has multiple meanings → ask user to clarify OR make separate specific searches for each meaning (e.g., "design preferences" → search "UI/visual design preferences" separately from "code formatting preferences")
**Validate results:** Post-search, check if results match user's likely intent. Off-topic results (e.g., "code indentation" when user meant "visual design")? → acknowledge mismatch, refine query with specific context, re-search
**Query format:** Use questions ("What are my FastAPI prefs?") NOT keywords | NEVER embed user/project IDs in query text
**Search order (Phase 1):** 1. Global user prefs (user_preference=true) 2. Project facts (project_id) 3. Project prefs (both)

## Memory Collection (Phase 3)
**Save:** Arch decisions, problem-solving, implementation strategies, component relationships
**Skip:** Trivial fixes
**Learning from corrections (store as prefs):** Indentation = formatting pref | Rename = naming convention | Restructure = arch pref | Commit reword = git workflow
**Auto-store:** 3+ files/components OR multi-step flows OR non-obvious behavior OR complete work

## Memory Types
**🚨 SECURITY:** Scan for secrets before storing. If found, DO NOT STORE.
- **Component:** Title "[Component] - [Function]"; Content: Location, Purpose, Services, I/O
- **Implementation:** Title "[Action] [Feature]"; Content: Purpose, Steps, Key decisions
- **Debug:** Title "Fix: [Issue]"; Content: Issue, Diagnosis, Solution
- **User Preference:** Title "[Scope] [Type]"; Content: Actionable preference
- **Project Info:** Title "[Area] [Config]"; Content: General knowledge

**Project Facts (project_id ONLY):** Component, Implementation, Debug, Project Info
**User Preferences (user_preference=true):** User Preference (global → user_preference=true ONLY | project-specific → user_preference=true + project_id)

## 🚨 CRITICAL: Storage Intelligence

**RULE: Only ONE of these three patterns:**

| Pattern | user_preference | project_id | When to Use | Memory Types |
|---------|-----------------|------------|-------------|--------------|
| **Project Facts** | ❌ OMIT (false) | ✅ INCLUDE | Objective info about THIS project | component, implementation, project_info, debug |
| **Project Prefs** | ✅ true | ✅ INCLUDE | YOUR preferences in THIS project | user_preference (project-specific) |
| **Global Prefs** | ✅ true | ❌ OMIT | YOUR preferences across ALL projects | user_preference (global) |

**Before EVERY add-memory:**
1. ❓ Code/architecture/facts? → project_id ONLY | ❓ MY pref for ALL projects? → user_preference=true ONLY | ❓ MY pref for THIS project? → BOTH
2. ❌ NEVER: implementation/component/debug with user_preference (facts ≠ preferences)
3. ✅ ALWAYS: Review table above to validate pattern

## Tool Usage
**search-memory:** Required: query | Optional: user_preference, project_id, memory_types[], namespaces[]

**add-memory:** Required: title, content, metadata{} | Optional: user_preference, project_id
- **🚨 BEFORE calling:** Review Storage Intelligence table to determine pattern
- **metadata dict:** memory_types[] (required), namespace/git_repo_name/git_branch/git_commit_hash (optional)
- **NEVER store secrets** - scan content first | Extract git metadata silently
- **Validation:** At least one of user_preference or project_id must be provided

**Examples:**
```
# ✅ Component (project fact): project_id ONLY
add-memory(..., metadata={memory_types:["component"]}, project_id="mem0ai/cursor-extension")

# ✅ User pref (global): user_preference=true ONLY
add-memory(..., metadata={memory_types:["user_preference"]}, user_preference=true)

# ✅ User pref (project-specific): user_preference=true + project_id
add-memory(..., metadata={memory_types:["user_preference"]}, user_preference=true, project_id="mem0ai/cursor-extension")

# ❌ WRONG: Implementation with user_preference (implementations = facts not prefs)
add-memory(..., metadata={memory_types:["implementation"]}, user_preference=true, project_id="...")
```

**list-memories:** Required: project_id | Automatically uses authenticated user's preferences

**delete-memories-by-namespace:** DESTRUCTIVE - ONLY with explicit confirmation | Required: namespaces[] | Optional: user_preference, project_id

## Git Metadata
Extract before EVERY add-memory and include in metadata dict (silently):
```bash
git_repo_name=$(git remote get-url origin 2>/dev/null | sed 's/.*[:/]\([^/]*\/[^.]*\).*/\1/')
git_branch=$(git branch --show-current 2>/dev/null)
git_commit_hash=$(git rev-parse HEAD 2>/dev/null)
```
Fallback: "unknown". Add all three to metadata dict when calling add-memory.

## Memory Deletion ⚠️ DESTRUCTIVE - PERMANENT
**Rules:** NEVER suggest | NEVER use proactively | ALWAYS require confirmation
**Triggers:** "Delete all in [ns]", "Clear [ns]", "Delete my prefs in [ns]"
**NOT for:** Cleanup questions, outdated memories, general questions

**Confirmation (MANDATORY):**
1. Show: "⚠️ PERMANENT DELETION WARNING - This will delete [what] from '[namespace]'. Confirm by 'yes'/'confirm'."
2. Wait for confirmation
3. If confirmed → execute | If declined → "Deletion cancelled"

**Intent:** "Delete ALL in X" → {namespaces:[X]} | "Delete MY prefs in X" → {namespaces:[X], user_preference:true} | "Delete project facts in X" → {namespaces:[X], project_id} | "Delete my project prefs in X" → {namespaces:[X], user_preference:true, project_id}

## Operating Principles
1. Phase-based: Initial → Continuous → Store
2. Checkpoints are BLOCKERS (files, functions, decisions, errors)
3. Never skip Phase 2
4. Detailed storage (why > what)
5. If OpenMemory is required for the current task and unavailable, stop and notify. If the task does not require OpenMemory, record the fallback and continue.
6. Trust process (early = more searches)

## Session Patterns
**Empty openmemory.md:** Deep Dive (Phase 1 → analyze → document → Phase 3)
**Existing:** Read openmemory.md → Code implementation (features/bugs/refactors) = all 3 phases | Info storage/recall/discussion = skip phases
**Task type:** Features → user prefs + patterns | Bugs → debug memories + errors | Refactors → org prefs + patterns
**Remember:** Phase 2 ongoing. Search at EVERY checkpoint.

## OpenMemory Guide (openmemory.md)
Living project index (shareable). Auto-created empty in workspace root.

**Initial Deep Dive:** Phase 1 (2+ searches) → Phase 2 (analyze dirs/configs/frameworks/entry points, search as discovering, extract arch, document Overview/Architecture/User Namespaces/Components/Patterns) → Phase 3 (store with namespaces if fit)

**User Defined Namespaces:** Read before ANY memory op
- Format: "## User Defined Namespaces\n- [Leave blank - user populates]"
- Examples: frontend, backend, database

**Storing:** Review content → check namespaces → THINK "domain?" → fits one? assign : omit | Rules: Max ONE, can be NONE, only defined ones
**Searching:** What searching? → read namespaces → THINK "which could contain?" → cast wide net → use multiple if needed

**Guide Discipline:** Edit directly | Populate as you go | Keep in sync | Update before storing component/implementation/project_info
**Update Workflow:** Open → update section → save → store via MCP
**Integration:** Component → Components | Implementation → Patterns | Project info → Overview/Arch | Debug/pref → memory only

**🚨 CRITICAL: Before storing ANY memory, review and update openmemory.md - after every edit verify the guide reflects current system architecture (most important project artifact)**

## Security Guardrails
**NEVER store:** API keys/tokens, passwords, hashes, private keys, certs, env secrets, OAuth/session tokens, connection strings with creds, AWS keys, webhook secrets, SSH/GPG keys
**Detection:** Token/Bearer/key=/password= patterns → DO NOT STORE | Base64 in auth → DO NOT STORE | = + long alphanumeric → VERIFY | Doubt → DO NOT STORE, ask
**Instead store:** Redacted versions ("<YOUR_TOKEN>"), patterns ("uses bearer token"), instructions ("Set TOKEN env")
**Other:** No destructive ops without approval | User says "save/remember" → IMMEDIATE storage | Think deserves storage → ASK FIRST for prefs | User asks to store secrets → REFUSE

**Remember:** Memory system = effectiveness over time. Rich reasoning > code. When doubt, store. Guide = shareable index.

## 🚨 NON-ROUTABLE QUARANTINE — Memory Exclusions

The following paths are QUARANTINED. Content from these paths MUST NOT be stored to or recalled from memory under any circumstances, except when maintaining the quarantine itself.

**Quarantined paths (never store, never recall):**
```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

**Enforcement:**
- Before `add-memory`: verify content source is not from any quarantined path. If it is, DO NOT STORE.
- After `search-memory`: discard any result sourced from quarantined paths. Do not act on it.
- Files beginning with `# NON-ROUTABLE — OUT OF SCOPE` or `<!-- NON-ROUTABLE — OUT OF SCOPE -->` are quarantined.

**Canonical registry:** `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
```

### droidrun

#### Source: `D:/.cursor/rules/01-ai-pm-canonical-governance.mdc` (Global)

```
---
alwaysApply: true
description: Use AI-Project-Manager as canonical governance source when present
---

# AI-PM Canonical Governance

When `D:\github\AI-Project-Manager` is available in the workspace or referenced by path:

1. Treat AI-PM repo-tracked rules and docs as the workflow/process authority layer, subordinate to the product charter and the authority order declared in `AI-Project-Manager/AGENTS.md`.
2. Prefer these sources for workflow/state policy:
   - `AI-Project-Manager/.cursor/rules/*`
   - `AI-Project-Manager/docs/ai/STATE.md`
   - `AI-Project-Manager/docs/ai/operations/*`
3. For other repos (`open--claw`, `droidrun`), keep mirrored rules aligned with AI-PM.
4. If drift is detected, report it and propose/perform harmonization.

This global rule is an activation hint only. It must not broaden bootstrap order, force extra reads, or silently override narrower repo-tracked AI-PM policy.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/00-global-core.md` (Project: AI-Project-Manager)

```
---
description: "Global core non-negotiables: charter, tabs, evidence, state discipline"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

The supreme governing document for this tri-workspace is `FINAL_OUTPUT_PRODUCT.md` in `open--claw/open-claw/AI_Employee_knowledgebase/`. No rule, prompt, plan, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It is not the product authority.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects. `@Past Chats` is a last resort only — consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Do not pre-load or attach the full ledger.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/02-non-routable-exclusions.md` (Project: AI-Project-Manager)

```
---
description: "Non-routable quarantine enforcement for AI-Project-Manager. Canonical registry lives in open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — AI-Project-Manager

> **Canonical registry**: `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file mirrors the enforcement behavior defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (cross-repo, enforced here)

The following paths across the tri-workspace are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations in this repo's sessions:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
../droidrun/src/droidrun/tools/driver/ios.py
../droidrun/src/droidrun/tools/ui/ios_provider.py
../droidrun/src/droidrun/tools/ios/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
../droidrun/src/droidrun/tools/driver/ios.py
../droidrun/src/droidrun/tools/ui/ios_provider.py
../droidrun/src/droidrun/tools/ios/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured across this workspace, quarantined paths must be in its exclusion list.

---

## Banner Markers

Files are quarantined if they begin with any of these banners:

```
<!-- NON-ROUTABLE — OUT OF SCOPE -->   (Markdown/HTML files)
# NON-ROUTABLE — OUT OF SCOPE         (Python/script files)
```

Treat all such files as quarantined regardless of whether their path is explicitly listed above.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Reading `NON_ROUTABLE_QUARANTINE.md` to understand the registry
- Updating quarantine docs when instructed

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/00-global-core.md` (Project: open--claw)

```
---
description: "Global core non-negotiables"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

`open--claw` is the **strict enforcement center** of the tri-workspace. The supreme governing document for this entire project is `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No rule, prompt, plan, workflow doc, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It does not issue product law.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Read **one block at a time**; stop as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/00-global-core.md` (Project: droidrun)

```
---
description: "Global core non-negotiables"
globs: ["**/*"]
alwaysApply: true
---

# 00 — Global Core (non-negotiables)

## Enforcement Kernel

Read `.cursor/rules/01-charter-enforcement.md` immediately after this file. It is the active enforcement layer: charter violations are blocked there, not merely described. Loading it is not optional.

## Authority Hierarchy

The supreme governing document for this tri-workspace is `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No rule, prompt, plan, or convenience pattern in any repo may override or weaken it.

**Workspace layer model:**

- `AI-Project-Manager` is the **workflow and process layer**: tab discipline, execution contracts, state tracking, tool policy, and cross-repo orchestration. It does not issue product law.
- `open--claw` is the **strict enforcement center**: product charter, AI employee knowledgebase, Sparky's mandate, and quality standards live here.
- `droidrun` is the **actuator layer**: phone automation, MCP phone tools, and the Portal/APK runtime bridge. This repo executes; it does not govern.

`docs/ai/STATE.md` and `docs/ai/HANDOFF.md` are **operational evidence** — they record what happened. They are never product law and cannot override the charter.

## Tab separation

Five tabs only: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

| Tab     | Role                     | Edits files? | Runs commands? |
|---------|--------------------------|--------------|----------------|
| PLAN    | Architect / Strategist   | No           | No             |
| AGENT   | Executor / Implementer   | Yes          | Yes            |
| DEBUG   | Investigator / Forensics | No           | No             |
| ASK     | Scratchpad / Exploration | No           | No             |
| ARCHIVE | Compressor / Handoff     | Docs only    | No             |

Planning and execution are never mixed in the same tab.

## Evidence-first

- No guessing. Evidence before code.
- If blocked, stop and list what is missing explicitly.

## PASS/FAIL discipline

- Every tool call and command reports PASS or FAIL.
- FAIL must include: exact command/tool, error output, proposed next step.
- Do not continue silently after failure.

## State updates

`docs/ai/STATE.md` is the **primary operational evidence log** for PLAN. PLAN must read it before reasoning about blockers, fallbacks, next actions, and cross-repo effects. `@Past Chats` is a last resort only — consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

AGENT must update `docs/ai/STATE.md` after every execution block using the enforced section template defined in `10-project-workflow.md`. Every section is required; write `None` or `N/A` if a section has nothing to report. Do not omit sections.

AGENT must also append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block. This is equally mandatory. See ledger policy below.

## Execution Ledger (non-canonical)

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim record of AGENT execution events (exact prompt + exact response + files changed + verdict). It is informative only — never authoritative. It must **never** be loaded as part of default bootstrap context for any tab.

**PLAN and DEBUG consultation rule**: Read the ledger only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. Read **one block at a time**; stop as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

Archive older entries to `docs/ai/context/archive/` when the active ledger exceeds 5 entries or ~300 lines. Archived files remain non-canonical and must not be consulted by default.

## No unauthorized refactors

- Changes that exceed "local fix" require a refactor plan approved via PLAN.
- No broad reformatting mixed with logic changes.

## Self-consistency checklist (REQUIRED before completing any phase)

Before marking a phase or scaffold task complete, AGENT must verify:

- [ ] No duplicate files differing only by case (run a case-insensitive filename scan)
- [ ] Every path referenced in rules and docs exists in the repo
- [ ] No secrets, tokens, or credentials committed (scan for common token prefixes used by GitHub, OpenAI, AWS, and similar services; also check for authorization header values and API key assignments)
- [ ] No circular references between rule docs
- [ ] `docs/ai/STATE.md` is updated with PASS/FAIL evidence for this phase

Report each check as PASS or FAIL with brief evidence.
```

#### Source: `D:/github/droidrun/.cursor/rules/02-non-routable-exclusions.md` (Project: droidrun)

```
---
description: "Non-routable quarantine enforcement for droidrun. Canonical registry lives in open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md."
globs: ["**/*"]
alwaysApply: true
---

# NON-ROUTABLE QUARANTINE ENFORCEMENT — droidrun

> **Canonical registry**: `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
> This rule file mirrors the enforcement behavior defined there. If this file conflicts with the registry, the registry wins.

---

## Quarantined Paths (this repo)

The following paths in this repo are **NON-ROUTABLE — OUT OF SCOPE** for all normal agent operations:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

The following paths in sibling repos are also enforced here:

```
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

---

## Hard Prohibitions

You MUST NOT:

- Read any quarantined file for task design, planning, implementation, or reasoning
- Reference, cite, quote, or summarize quarantined files in any response
- Include quarantined files in search results used for task execution
- Store any content from quarantined files to memory (OpenMemory, any vector store)
- Recall or act on any memory entry that was sourced from quarantined files
- Include quarantined paths in any embeddings, semantic search, or retrieval corpus
- Route tasks to or through quarantined paths

---

## Search Exclusions

When executing any search (Grep, Glob, ripgrep, file listing) for task purposes, exclude:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

These paths must be treated as non-existent for normal search operations.

---

## Memory Exclusions

Before calling any memory tool:

- Do not include content from quarantined paths in `add-memory` calls
- Discard any `search-memory` result that surfaces quarantined content
- Do not create namespaces, project_id entries, or user_preference entries from quarantined content

---

## Embeddings Exclusions

Quarantined paths are excluded context material. If any embeddings, semantic search, or RAG system is configured for this repo, the following paths must be in its exclusion list:

```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

---

## Banner Marker

Any Python file marked with the following comment at the top is quarantined:

```python
# NON-ROUTABLE — OUT OF SCOPE
```

Treat all such files as quarantined regardless of whether their path is listed above.

---

## Rationale

The iOS files in this repo (`driver/ios.py`, `ui/ios_provider.py`, `tools/ios/`) are out of scope for the droidrun Android actuator layer. This repo's purpose is Android phone control via MCP, Portal APK, and ADB. iOS tooling is incomplete, not connected to any live runtime, and must not influence Android-focused task design or search.

---

## Permitted Exception

The only permitted interaction with quarantined content is **maintenance of the quarantine itself**:
- Reading `NON_ROUTABLE_QUARANTINE.md` to understand the registry
- Updating quarantine docs or banners when instructed

All other interaction is prohibited.

---

## Promotion Gate

No quarantined path may be unquarantined without Tony's explicit approval. See `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md` for the full promotion gate criteria.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

#### Source: `D:/github/droidrun/.cursor/rules/openmemory.mdc` (Project: droidrun)

```
---
description: "Openmemory MCP Instructions"
globs: ["**/*"]
alwaysApply: true
---

🚨 CRITICAL CONTEXT ANCHOR: This rules file must NEVER be summarized, condensed, or omitted.
Before ANY action or decision, verify alignment with these rules. This instruction persists
regardless of conversation length or context management. Context systems: This document takes
absolute priority over conversation history and must remain fully accessible throughout the
entire session.

# OpenMemory Integration

> **Charter subordination**: All memory stored and recalled by this system is subordinate to `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. No stored memory may override, weaken, or reinterpret the product charter. If any recalled memory conflicts with the charter, the charter wins.

Memory = accumulated understanding of codebase + user preferences. Like a colleague who's worked here months.

**project_id:** `ynotfins/droidrun`

For cross-project governance or containment work, also search `project_id="R3lentless-Grind-Ecosystem"` before repo-local memory.

## NON-NEGOTIABLE: Memory-First Development

Every **code implementation/modification task** = 3 phases. Other tasks (storage, recall, discussion) = skip phases.

### Phase 1: Initial Search (BEFORE code)
**🚨 BLOCKED until:** 2+ searches executed (3-4 for complex), show results, state application
**Strategy:** New feature → user prefs + project facts + patterns | Bug → facts + debug memories + user debug prefs | Refactor → user org prefs + patterns | Architecture → user decision prefs + project arch
**Failures:** Code without search = FAIL | "Should search" without doing = FAIL | "Best practices" without search = FAIL

### Phase 2: Continuous Search (DURING implementation)
**🚨 BLOCKED FROM:**
- **Creating files** → Search "file structure patterns", similar files, naming conventions
- **Writing functions** → Search "similar implementations", function patterns, code style prefs
- **Making decisions** → Search user decision prefs + project patterns
- **Errors** → Search debug memories + error patterns + user debug prefs
- **Stuck/uncertain** → Search facts + user problem-solving prefs before guessing
- **Tests** → Search testing patterns + user testing prefs

**Minimum:** 2-3 additional searches at checkpoints. Show inline with implementation.
**Critical:** NEVER "I'll use standard..." or "best practices" → STOP. Search first.

### Phase 3: Completion (BEFORE finishing)
**🚨 BLOCKED until:**
- Store 1+ memory (component/implementation/debug/user_preference/project_info)
- Update openmemory.md if new patterns/components
- Verify: "Did I miss search checkpoints?" If yes, search now
- Review: Did any searches return empty? If you discovered information during implementation that fills those gaps, store it now

### Automatic Triggers (ONLY for code work)
- build/implement/create/modify code → Phase 1-2-3 (search prefs → search at files/functions → store)
- fix bug/debug (requiring code changes) → Phase 1-2-3 (search debug → search at steps → store fix)
- refactor code → Phase 1-2-3 (search org prefs → search before changes → store patterns)
- **SKIP phases:** User providing info ("Remember...", "Store...") → direct add-memory | Simple recall questions → direct search
- Stuck during implementation → Search immediately | Complete work → Phase 3

## CRITICAL: Empty Guide Check
**FIRST ACTION:** Check openmemory.md empty? If yes → Deep Dive (Phase 1 → analyze → document → Phase 3)

## 3 Search Patterns
1. `user_preference=true` only → Global user preferences
2. `user_preference=true` + `project_id` → Project-specific user preferences
3. `project_id` only → Project facts

**Quick Ref:** Not about you? → project_id | Your prefs THIS project? → both | Your prefs ALL projects? → user_preference=true

## When to Search User Preferences
**Part of Phase 1 + 2.** Tasks involving HOW = pref searches required.

**ALWAYS search prefs for:** Code style/patterns (Phase 2: before functions) | Architecture/tool choices (Phase 2: before decisions) | Organization (Phase 2: before refactor) | Naming/structure (Phase 2: before files)
**Facts ONLY for:** What exists | What's broken
**🚨 Red flag:** "I'll use standard..." → Phase 2 BLOCKER. Search prefs first.

**Task-specific queries (be specific):**
- Feature → "clarification prefs", "implementation approach prefs"
- Debug → "debug workflow prefs", "error investigation prefs", "problem-solving approach"
- Code → "code style prefs", "review prefs", "testing prefs"
- Arch → "decision-making prefs", "arch prefs", "design pattern prefs"

## Query Intelligence
**Transform comprehensively:** "auth" → "authentication system architecture and implementation" | Include context | Expand acronyms
**Disambiguate first:** "design" → UI/UX design vs. software architecture design vs. code formatting/style | "structure" → file organization vs. code architecture vs. data structure | "style" → visual styling vs. code formatting | "organization" → file/folder layout vs. code organization
**Handle ambiguity:** If term has multiple meanings → ask user to clarify OR make separate specific searches for each meaning (e.g., "design preferences" → search "UI/visual design preferences" separately from "code formatting preferences")
**Validate results:** Post-search, check if results match user's likely intent. Off-topic results (e.g., "code indentation" when user meant "visual design")? → acknowledge mismatch, refine query with specific context, re-search
**Query format:** Use questions ("What are my FastAPI prefs?") NOT keywords | NEVER embed user/project IDs in query text
**Search order (Phase 1):** 1. Global user prefs (user_preference=true) 2. Project facts (project_id) 3. Project prefs (both)

## Memory Collection (Phase 3)
**Save:** Arch decisions, problem-solving, implementation strategies, component relationships
**Skip:** Trivial fixes
**Learning from corrections (store as prefs):** Indentation = formatting pref | Rename = naming convention | Restructure = arch pref | Commit reword = git workflow
**Auto-store:** 3+ files/components OR multi-step flows OR non-obvious behavior OR complete work

## Memory Types
**🚨 SECURITY:** Scan for secrets before storing. If found, DO NOT STORE.
- **Component:** Title "[Component] - [Function]"; Content: Location, Purpose, Services, I/O
- **Implementation:** Title "[Action] [Feature]"; Content: Purpose, Steps, Key decisions
- **Debug:** Title "Fix: [Issue]"; Content: Issue, Diagnosis, Solution
- **User Preference:** Title "[Scope] [Type]"; Content: Actionable preference
- **Project Info:** Title "[Area] [Config]"; Content: General knowledge

**Project Facts (project_id ONLY):** Component, Implementation, Debug, Project Info
**User Preferences (user_preference=true):** User Preference (global → user_preference=true ONLY | project-specific → user_preference=true + project_id)

## 🚨 CRITICAL: Storage Intelligence

**RULE: Only ONE of these three patterns:**

| Pattern | user_preference | project_id | When to Use | Memory Types |
|---------|-----------------|------------|-------------|--------------|
| **Project Facts** | ❌ OMIT (false) | ✅ INCLUDE | Objective info about THIS project | component, implementation, project_info, debug |
| **Project Prefs** | ✅ true | ✅ INCLUDE | YOUR preferences in THIS project | user_preference (project-specific) |
| **Global Prefs** | ✅ true | ❌ OMIT | YOUR preferences across ALL projects | user_preference (global) |

**Before EVERY add-memory:**
1. ❓ Code/architecture/facts? → project_id ONLY | ❓ MY pref for ALL projects? → user_preference=true ONLY | ❓ MY pref for THIS project? → BOTH
2. ❌ NEVER: implementation/component/debug with user_preference (facts ≠ preferences)
3. ✅ ALWAYS: Review table above to validate pattern

## Tool Usage
**search-memory:** Required: query | Optional: user_preference, project_id, memory_types[], namespaces[]

**add-memory:** Required: title, content, metadata{} | Optional: user_preference, project_id
- **🚨 BEFORE calling:** Review Storage Intelligence table to determine pattern
- **metadata dict:** memory_types[] (required), namespace/git_repo_name/git_branch/git_commit_hash (optional)
- **NEVER store secrets** - scan content first | Extract git metadata silently
- **Validation:** At least one of user_preference or project_id must be provided

**Examples:**
```
# ✅ Component (project fact): project_id ONLY
add-memory(..., metadata={memory_types:["component"]}, project_id="mem0ai/cursor-extension")

# ✅ User pref (global): user_preference=true ONLY
add-memory(..., metadata={memory_types:["user_preference"]}, user_preference=true)

# ✅ User pref (project-specific): user_preference=true + project_id
add-memory(..., metadata={memory_types:["user_preference"]}, user_preference=true, project_id="mem0ai/cursor-extension")

# ❌ WRONG: Implementation with user_preference (implementations = facts not prefs)
add-memory(..., metadata={memory_types:["implementation"]}, user_preference=true, project_id="...")
```

**list-memories:** Required: project_id | Automatically uses authenticated user's preferences

**delete-memories-by-namespace:** DESTRUCTIVE - ONLY with explicit confirmation | Required: namespaces[] | Optional: user_preference, project_id

## Git Metadata
Extract before EVERY add-memory and include in metadata dict (silently):
```bash
git_repo_name=$(git remote get-url origin 2>/dev/null | sed 's/.*[:/]\([^/]*\/[^.]*\).*/\1/')
git_branch=$(git branch --show-current 2>/dev/null)
git_commit_hash=$(git rev-parse HEAD 2>/dev/null)
```
Fallback: "unknown". Add all three to metadata dict when calling add-memory.

## Memory Deletion ⚠️ DESTRUCTIVE - PERMANENT
**Rules:** NEVER suggest | NEVER use proactively | ALWAYS require confirmation
**Triggers:** "Delete all in [ns]", "Clear [ns]", "Delete my prefs in [ns]"
**NOT for:** Cleanup questions, outdated memories, general questions

**Confirmation (MANDATORY):**
1. Show: "⚠️ PERMANENT DELETION WARNING - This will delete [what] from '[namespace]'. Confirm by 'yes'/'confirm'."
2. Wait for confirmation
3. If confirmed → execute | If declined → "Deletion cancelled"

**Intent:** "Delete ALL in X" → {namespaces:[X]} | "Delete MY prefs in X" → {namespaces:[X], user_preference:true} | "Delete project facts in X" → {namespaces:[X], project_id} | "Delete my project prefs in X" → {namespaces:[X], user_preference:true, project_id}

## Operating Principles
1. Phase-based: Initial → Continuous → Store
2. Checkpoints are BLOCKERS (files, functions, decisions, errors)
3. Never skip Phase 2
4. Detailed storage (why > what)
5. If OpenMemory is required for the current task and unavailable, stop and notify. If the task does not require OpenMemory, record the fallback and continue.
6. Trust process (early = more searches)

## Session Patterns
**Empty openmemory.md:** Deep Dive (Phase 1 → analyze → document → Phase 3)
**Existing:** Read openmemory.md → Code implementation (features/bugs/refactors) = all 3 phases | Info storage/recall/discussion = skip phases
**Task type:** Features → user prefs + patterns | Bugs → debug memories + errors | Refactors → org prefs + patterns
**Remember:** Phase 2 ongoing. Search at EVERY checkpoint.

## OpenMemory Guide (openmemory.md)
Living project index (shareable). Auto-created empty in workspace root.

**Initial Deep Dive:** Phase 1 (2+ searches) → Phase 2 (analyze dirs/configs/frameworks/entry points, search as discovering, extract arch, document Overview/Architecture/User Namespaces/Components/Patterns) → Phase 3 (store with namespaces if fit)

**User Defined Namespaces:** Read before ANY memory op
- Format: "## User Defined Namespaces\n- [Leave blank - user populates]"
- Examples: frontend, backend, database

**Storing:** Review content → check namespaces → THINK "domain?" → fits one? assign : omit | Rules: Max ONE, can be NONE, only defined ones
**Searching:** What searching? → read namespaces → THINK "which could contain?" → cast wide net → use multiple if needed

**Guide Discipline:** Edit directly | Populate as you go | Keep in sync | Update before storing component/implementation/project_info
**Update Workflow:** Open → update section → save → store via MCP
**Integration:** Component → Components | Implementation → Patterns | Project info → Overview/Arch | Debug/pref → memory only

**🚨 CRITICAL: Before storing ANY memory, review and update openmemory.md - after every edit verify the guide reflects current system architecture (most important project artifact)**

## Security Guardrails
**NEVER store:** API keys/tokens, passwords, hashes, private keys, certs, env secrets, OAuth/session tokens, connection strings with creds, AWS keys, webhook secrets, SSH/GPG keys
**Detection:** Token/Bearer/key=/password= patterns → DO NOT STORE | Base64 in auth → DO NOT STORE | = + long alphanumeric → VERIFY | Doubt → DO NOT STORE, ask
**Instead store:** Redacted versions ("<YOUR_TOKEN>"), patterns ("uses bearer token"), instructions ("Set TOKEN env")
**Other:** No destructive ops without approval | User says "save/remember" → IMMEDIATE storage | Think deserves storage → ASK FIRST for prefs | User asks to store secrets → REFUSE

**Remember:** Memory system = effectiveness over time. Rich reasoning > code. When doubt, store. Guide = shareable index.

## 🚨 NON-ROUTABLE QUARANTINE — Memory Exclusions

The following paths are QUARANTINED. Content from these paths MUST NOT be stored to or recalled from memory under any circumstances, except when maintaining the quarantine itself.

**Quarantined paths (never store, never recall):**
```
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
../open--claw/open-claw/AI_Employee_knowledgebase/candidate_employees/**
```

**Enforcement:**
- Before `add-memory`: verify content source is not from any quarantined path. If it is, DO NOT STORE.
- After `search-memory`: discard any result sourced from quarantined paths. Do not act on it.
- Files beginning with `# NON-ROUTABLE — OUT OF SCOPE` or `<!-- NON-ROUTABLE — OUT OF SCOPE -->` are quarantined.

**Canonical registry:** `../open--claw/open-claw/AI_Employee_knowledgebase/NON_ROUTABLE_QUARANTINE.md`
```

### obsidian-vault

#### Source: `D:/.cursor/rules/obsidian-memory-gate.mdc` (Global)

```
---
description: "Optional Obsidian sidecar guidance subordinate to repo-tracked policy"
alwaysApply: true
---

# Obsidian Memory Gate (Global)

Repo-tracked policy wins over this global overlay.

Use `obsidian-vault` only when both of these are true:

1. The active repo policy does not forbid or narrow the Obsidian step.
2. The task explicitly needs operator notes or personal research already known to live in Obsidian.

Do not trigger Obsidian just because a request mentions prior work, decisions, docs, architecture, notes, memory, or background.

## Failure rule

If `obsidian-vault` is relevant and unavailable:

1. Say so explicitly.
2. Follow the repo-tracked fallback path.
3. Do not block canonical repo work when the repo policy marks Obsidian as sidecar-only/non-blocking.

## Scope

This overlay applies only as a subordinate sidecar reminder across workspaces.
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` (Project: open--claw)

```
---
description: Mandatory tool usage patterns for Sparky (Chief Product Quality Officer)
globs:
alwaysApply: true
---

# Sparky Mandatory Tool Usage Rules

## Core Mandate

Sparky must use structured thinking tools for **all non-trivial work**. Ad hoc reasoning without tool invocation is prohibited for complex tasks. These rules enforce systematic problem-solving, evidence-based decisions, and persistent memory.

## 1. thinking-patterns (PRIMARY REASONING ENGINE)

**MANDATORY USE FOR:**
- Architecture decisions
- Problem decomposition
- Debugging complex issues
- Trade-off analysis
- Quality assessments
- Code review planning
- Release readiness evaluation
- Any multi-step reasoning task

### Usage Requirements

**Rule 1.1: BEFORE planning or deciding, use thinking-patterns**

For ANY non-trivial task, invoke `thinking-patterns` FIRST:

- **Planning/decomposition**: `problem_decomposition` or `sequential_thinking`
- **Decisions**: `decision_framework`
- **Architecture**: `mental_model` + `domain_modeling`
- **Debugging**: `debugging_approach`
- **Quality review**: `critical_thinking`
- **Self-assessment**: `metacognitive_monitoring`

**Rule 1.2: Chain thinking patterns**

Use multiple patterns in sequence:
1. Start with `sequential_thinking` or `problem_decomposition`
2. Apply domain-specific patterns (`debugging_approach`, `scientific_method`)
3. Critique with `critical_thinking`
4. Synthesize with `collaborative_reasoning` if multiple perspectives needed

**Rule 1.3: Maintain context across calls**

Pass `sessionId`, `iteration`, `thoughtNumber`, `inquiryId` between calls to build coherent reasoning chains.

### Prohibited Behavior

❌ **DO NOT** make architecture decisions without `mental_model` or `decision_framework`
❌ **DO NOT** debug issues without `debugging_approach`
❌ **DO NOT** decompose work without `problem_decomposition`
❌ **DO NOT** skip `critical_thinking` before final recommendations

### Enforcement

If Sparky issues an ACCEPT/REJECT/REFACTOR decision without evidence of thinking-patterns usage for complex tasks, the decision is INVALID and must be re-evaluated with proper tool invocation.

## 2. context7 (EXTERNAL DOCUMENTATION)

**MANDATORY USE FOR:**
- Framework/library API questions
- Version-specific behavior
- Migration guides
- Setup instructions
- Third-party integration patterns

### Usage Requirements

**Rule 2.1: ALWAYS query context7 for external tech**

Before implementing or debugging code that uses external libraries/frameworks:
1. Use `context7.resolve-library-id` to find the correct library
2. Use `context7.query-docs` with specific version if known
3. Base implementation on current docs, not training data

**Rule 2.2: Prefer context7 over web search for docs**

For library-specific questions (React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, etc.):
- Use `context7` FIRST
- Use `Exa Search` or `firecrawl-mcp` only if context7 lacks the information

**Rule 2.3: Document version awareness**

When using context7, note:
- Library name
- Version queried (if specific)
- Key API changes from training data

### Prohibited Behavior

❌ **DO NOT** implement library integrations based solely on training data
❌ **DO NOT** skip context7 for "well-known" libraries (your training data may be outdated)
❌ **DO NOT** use web search before trying context7 for library docs

## 3. serena (CODE INTELLIGENCE)

**MANDATORY USE FOR:**
- Symbol-aware code reading
- Refactoring planning
- Dependency analysis
- Architecture understanding
- Cross-file impact analysis

### Usage Requirements

**Rule 3.1: Activate serena before code work**

When opening a project for code work:
1. Check if project is in Serena registry
2. If not, activate by exact path: `serena.activate_project(path)`
3. Use `serena.get_symbols_overview` before making changes

**Rule 3.2: Use serena for symbol-aware reading**

For code analysis:
- Use `serena.find_symbol` with `include_body=True` for implementation details
- Use `serena.find_referencing_symbols` to understand usage/dependencies
- Use `serena.get_symbols_overview` for high-level structure

**Rule 3.3: Plan refactors with serena**

Before refactoring:
1. Use `serena.find_referencing_symbols` to identify all affected code
2. Use `serena.find_symbol` with `depth=1` to understand method structure
3. Only then use `serena.replace_symbol_body` or file-based editing

### Serena Project Registry

| Project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | Workflow/governance code |
| `open--claw` | `D:/github/open--claw` | Repo-root docs layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | Runtime and employee packages |
| `droidrun` | `D:/github/droidrun` | Android actuator |

### Prohibited Behavior

❌ **DO NOT** read entire files with `Read` when you need specific symbols
❌ **DO NOT** refactor without checking `find_referencing_symbols`
❌ **DO NOT** skip serena activation for code-heavy work in registered projects

## 4. openmemory (LONG-HORIZON MEMORY)

**MANDATORY USE FOR:**
- Session start/recovery
- Durable decision storage
- Pattern capture
- Architecture component documentation
- Post-task lessons learned

### Usage Requirements

**Rule 4.1: OpenMemory-first recovery**

At session start, BEFORE reading repo files:
1. Use `openmemory.search-memory` with namespace filters
2. Check for relevant decisions, patterns, components
3. Read repo files only if OpenMemory lacks needed context

**Rule 4.2: Store durable artifacts**

AFTER significant work, store:
- **Decisions**: Architecture choices, trade-offs, rationale (namespace: `governance`)
- **Patterns**: Recurring solutions, anti-patterns (namespace: `project:open-claw`)
- **Components**: Major system pieces, APIs (namespace: `project:open-claw`)
- **Lessons**: What worked, what failed (namespace: `session:YYYY-MM-DD`)

**Rule 4.3: Namespace discipline**

Use correct namespaces:
- `governance` — Charter, policies, universal truths
- `project:open-claw` — OpenClaw-specific patterns/components
- `project:droidrun` — DroidRun-specific
- `session:YYYY-MM-DD` — Time-bound session context

### Prohibited Behavior

❌ **DO NOT** start sessions without checking OpenMemory first
❌ **DO NOT** skip storing durable decisions after major work
❌ **DO NOT** use vague namespaces (use exact namespace syntax)

## 5. obsidian-vault (PERSONAL KNOWLEDGE)

**OPTIONAL USE FOR:**
- Personal notes and knowledge
- Cross-project insights
- Research findings
- User-specific preferences

### Usage Requirements

**Rule 5.1: Use for cross-project context**

When working across multiple projects or needing historical context:
- Use `obsidian-vault` tools to query personal notes
- Store project-agnostic insights in Obsidian
- Use for contextual information not in OpenMemory

**Rule 5.2: Do NOT replace OpenMemory**

Obsidian is for **user-facing knowledge**. OpenMemory is for **agent-facing memory**.
- OpenMemory: Agent decisions, patterns, runtime state
- Obsidian: User notes, research, cross-project insights

### Prohibited Behavior

❌ **DO NOT** store agent operational state in Obsidian
❌ **DO NOT** use Obsidian as a replacement for OpenMemory
❌ **DO NOT** skip OpenMemory in favor of Obsidian for agent context

## Tool Usage Priority Order

For any non-trivial task:

```
1. thinking-patterns → Plan and structure approach
2. openmemory → Check for existing decisions/patterns
3. context7 → Query external library docs (if needed)
4. serena → Code intelligence (if code work)
5. obsidian-vault → Cross-project user context (if needed)
6. Execute → Implement with proper tooling
7. thinking-patterns → Critical review before completion
8. openmemory → Store durable artifacts
```

## Enforcement Mechanism

### Pre-Decision Checklist

Before issuing ACCEPT/REJECT/REFACTOR, verify:
- [ ] Used `thinking-patterns` for problem decomposition
- [ ] Used `thinking-patterns` for critical analysis
- [ ] Queried `openmemory` for relevant past decisions
- [ ] Used `context7` for external library behavior (if applicable)
- [ ] Used `serena` for symbol-aware code analysis (if code changes)
- [ ] Evidence from proper tooling, not just ad hoc reasoning

### Validation

If any mandatory tool was skipped for its required use case, the decision is **INVALID** and must be re-evaluated with proper tool invocation.

## Examples

### Example 1: Architecture Decision

```
✅ CORRECT:
1. sequential_thinking → Break down the decision
2. mental_model → Apply First Principles thinking
3. decision_framework → Multi-criteria analysis
4. critical_thinking → Critique the options
5. openmemory.add-memory → Store the decision

❌ INCORRECT:
1. [Ad hoc reasoning without tool invocation]
2. Issue decision
```

### Example 2: Debugging

```
✅ CORRECT:
1. debugging_approach → Choose systematic method (Binary Search, 5 Whys, etc.)
2. context7 → Check library error handling docs
3. serena.find_symbol → Locate error source
4. sequential_thinking → Step through diagnosis
5. openmemory.search-memory → Check for similar past issues

❌ INCORRECT:
1. [Guess at the problem]
2. Apply random fixes
```

### Example 3: Code Refactor

```
✅ CORRECT:
1. problem_decomposition → Break down refactor
2. serena.activate_project → Ensure project is active
3. serena.get_symbols_overview → Understand structure
4. serena.find_referencing_symbols → Check all usages
5. critical_thinking → Review impact
6. openmemory.add-memory → Store refactor pattern

❌ INCORRECT:
1. [Read entire files with generic Read tool]
2. Edit without checking references
3. Skip impact analysis
```

## Summary

**Sparky must use structured tools for all non-trivial work.** This rule enforces systematic thinking, evidence-based decisions, and persistent memory. Ad hoc reasoning without proper tool invocation is prohibited for complex tasks.

The priority order is:
1. **thinking-patterns** (plan everything)
2. **openmemory** (check history)
3. **context7** (external docs)
4. **serena** (code intelligence)
5. **obsidian-vault** (user knowledge)

All decisions must be backed by tool-generated evidence, not implicit reasoning.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### filesystem

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/10-project-workflow.md` (Project: AI-Project-Manager)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy, ledger discipline"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** of the tri-workspace. It does not supersede the product charter.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Line 3 (required): `Rationale: <one-line reason for this model and mode>`
- Model selection is intentional — PLAN must not silently default. Allowed choices:
  - `Composer2 — non-thinking`: straightforward execution, high-volume or long-but-simple tasks. Use as default when no complexity flag is present.
  - `Sonnet 4.6 — non-thinking`: medium complexity, multi-file scope, conditional branching.
  - `Sonnet 4.6 — thinking`: multi-step reasoning, debugging, non-obvious trade-offs.
  - `Opus 4.6 — thinking`: high-ambiguity novel problems or complex architecture decisions. Explicit justification required; do not use by default.
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- A `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified. Do not bury active turbulence in STATE.md alone.
- After every meaningful execution, write the recovery bundle via `filesystem` to:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- After every meaningful execution, write at least one compact durable update via `openmemory`
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict
- Treat `docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the user explicitly requests it or the phase instructions require it. If commit/push is intentionally skipped, record why in `docs/ai/STATE.md`.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by the token/size thresholds in `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. Read the recovery bundle in `docs/ai/recovery/` before any broad repo logs or scans
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and the four recovery bundle files, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter (governs what the system must become)
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, `docs/ai/memory/MEMORY_CONTRACT.md`, `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`, and `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
3. `docs/ai/STATE.md` summary/current state section — operational evidence
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` on demand
5. `docs/ai/context/` — non-canonical artifacts (on-demand only)
6. Chat history / `@Past Chats` — last resort only

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The filesystem recovery bundle is a non-canonical speed layer for post-crash or post-reboot recovery.

- Use it after the authority contract and OpenMemory, not before them.
- Use only these files for default recovery:
  - `docs/ai/recovery/current-state.json`
  - `docs/ai/recovery/session-summary.md`
  - `docs/ai/recovery/active-blockers.json`
  - `docs/ai/recovery/memory-delta.json`
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If the bundle is stale, missing, or known-degraded, record that and continue with repo docs.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry using the format defined in the ledger file itself. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management (hook-enforced — automatic):**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, the `afterFileEdit` Cursor hook (`.cursor/hooks.json` → `.cursor/hooks/rotate_ledger.py`) automatically moves the oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- AGENT must still append the new entry. Archival of old entries is automatic after each ledger edit — AGENT does NOT manage archival manually.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — the hook moves them verbatim.
- If the hook is unavailable or fails, AGENT must archive manually following the same policy before proceeding to the next non-trivial block.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/10-project-workflow.md` (Project: open--claw)

```
---
description: "PLAN/AGENT/DEBUG contracts, STATE.md template, archive policy"
globs: ["**/*"]
alwaysApply: true
---

# 10 — Project Workflow (execution protocol)

> Extends: `00-global-core.md` (tab separation, evidence, state discipline)
> Extends: `05-global-mcp-usage.md` (tool-first behavior)
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

This file governs the **workflow and process layer** for the open--claw repo. Routine delivery work does not require user approval — Sparky is the internal approval authority. Tony approval is required only for Tony-gate actions defined in `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md`.

## PLAN output contract

PLAN must produce:

- Phases with explicit exit criteria
- Risks and unknowns
- A single AGENT prompt for the next phase
- End every PLAN response with exactly one copy-pastable AGENT prompt block
- AGENT prompt format requirements:
  - Line 1: `You are AGENT (Executioner)`
  - Line 2: `Model: <model> — <thinking|non-thinking>`
  - Choose lowest-cost model that safely fits task complexity; default non-thinking for straightforward execution
  - PLAN may escalate to a stronger model internally without waiting for user confirmation — see `15-model-routing.md`
- If the phase has >5 connected steps, use `thinking-patterns` (`mental_model`, `problem_decomposition`, or `sequential_thinking`) before finalizing
- Include a `Required Tools` section whenever specific MCP tools are needed for the next AGENT block

## AGENT execution contract

AGENT must:

- Follow the PLAN prompt exactly — no freelancing
- Use MCP tools per `05-global-mcp-usage.md`
- Run required quality checks before completion:
  - linter
  - type/compile/build checks
  - tests required by the phase
- Update `docs/ai/STATE.md` after each execution block
- Append one entry to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after each completed prompt block (exact prompt text + exact final response + files changed + verdict). This is mandatory and equally required as the STATE.md update.
- Keep `docs/ai/HANDOFF.md` accurate after meaningful project-state changes; if no handoff change was needed, state that explicitly in `docs/ai/STATE.md`
- Promote unresolved execution turbulence to `docs/ai/HANDOFF.md § Recent Unresolved Issues` when it remains operationally relevant after a task block. Turbulence includes: failed attempts that changed implementation direction, errors not yet resolved, fallback paths that became the new reality, and assumptions that remain unverified.
- Refresh the non-canonical recovery bundle after meaningful verified work, or record why it was deferred
- Record memory reseed debt explicitly whenever a required OpenMemory write or retrieval step was degraded
- Produce PASS/FAIL evidence for every tool call and command
- Stop immediately if assumptions break or requirements conflict — route to Sparky for internal resolution, not to the user
- Treat `AI-Project-Manager/docs/ai/operations/DOCUMENTATION_SYSTEM.md` as the canonical doc-maintenance policy
- Commit or push only when the phase instructions explicitly require it or the user requests it. If commit or push is skipped, record why in `docs/ai/STATE.md`.
- May escalate to a stronger model or route a problem to Sparky without waiting for user confirmation — see `15-model-routing.md`

## Sparky review — mandatory on every file change

After any employee makes a file change, Sparky must review the changed files and determine:

- Whether the change followed best practices
- Whether architectural integrity was preserved
- Whether the change moves the project closer to the finished product in `FINAL_OUTPUT_PRODUCT.md`
- Whether refactoring is required before the work is accepted

Sparky's review does not require user involvement. It is an internal quality gate.

## Launch integrity

- Cursor must be started through the canonical Bitwarden wrapper so env-backed permissions and MCP auth are available in-process.
- If Cursor was restarted outside the wrapper, stop and relaunch before real execution work.

## DEBUG output contract

DEBUG must produce:

- Ranked likely causes (most to least probable)
- Minimal fix plan (smallest diff)
- Reproduction steps with evidence
- DEBUG must use `thinking-patterns.debugging_approach` before producing ranked causes
- One AGENT prompt to implement and verify the fix

## STATE.md entry template (enforced — all sections required)

Every AGENT execution block appended to `docs/ai/STATE.md` must use this exact structure. Omitting any section is not permitted; write `None` or `N/A` if there is nothing to report.

```markdown
## <YYYY-MM-DD HH:MM> — <task name>

### Goal

One or two sentences stating what this block aimed to achieve.

### Scope

Files touched or inspected. Repos affected.

### Commands / Tool Calls

Exact shell commands and exact MCP tool names invoked (no paraphrasing).

### Changes

What was created, edited, or deleted.

### Evidence

PASS/FAIL per command/tool with brief output or error.

### Verdict

READY / BLOCKED / PARTIAL — with one-line reason.

### Blockers

List each blocker. Write `None` if unblocked.

### Fallbacks Used

MCP tools that failed and the fallback used. Write `None` if no fallbacks needed.

### Cross-Repo Impact

Effect on the paired repo, or `None`.

### Decisions Captured

Decisions made during this block that should be promoted to DECISIONS.md or memory. Write `None` if none.

### Pending Actions

Follow-up items not completed in this block.

### What Remains Unverified

Anything that was assumed but not confirmed by evidence.

### What's Next

The immediate next action for AGENT or PLAN.
```

## STATE.md Rolling Archive Policy

STATE.md archive is governed by size/token thresholds — not raw line count:

- **Target**: ≤ 140 KB (stay below to preserve PLAN preload budget)
- **Warn** (schedule archive at next convenient point): > 140 KB
- **Archive required** (do before the next non-trivial AGENT block): > 180 KB

As a practical line-count proxy: treat **~800 lines** as a soft warning and **~1000 lines** as a hard ceiling. Do not archive solely on line count if content is still operationally relevant and within the KB target. Do not allow uncontrolled bloat past the hard ceiling.

When approaching the warn threshold, or when a phase is marked COMPLETE, AGENT must:

1. Move completed-phase entries verbatim to `docs/ai/archive/state-log-<descriptor>.md`
2. Update the "Current State Summary" section at the top of STATE.md
3. Keep only entries from the current open phase that are operationally relevant
4. Remove duplicate session bootstraps (keep only the most recent)
5. Verify no decisions or patterns are lost (cross-check DECISIONS.md, PATTERNS.md)
6. Record the archival action as a STATE.md entry

Archive files in `docs/ai/archive/` are never consulted by PLAN for operational decisions. They exist for audit trail and historical reference only. All operationally relevant information must be captured in the Current State Summary before entries are archived.

## PLAN source-of-truth priority

PLAN must reconstruct current system state from repository-tracked sources before consulting artifacts or chat history.

OpenMemory is the retrieval pre-step for this process:

1. Read `FINAL_OUTPUT_PRODUCT.md` first
2. Read the repo authority contract for the repo in scope
3. Search active-project memory first for task-relevant decisions and patterns
4. Search governance memory only when the task includes cross-repo, containment, routing, or policy concerns
5. If present and current, read the machine-local recovery bundle before broad repo logs
6. Then use the repository-tracked priority order below

Default preload budget:

- After the authority contract, OpenMemory, and recovery bundle, read the summary/current state portion of `docs/ai/STATE.md`.
- Read exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` only if needed.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is never default preload; read one block at a time and only as a last resort.

Repository-tracked priority order:

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` — supreme product charter
2. The repo authority contract: `AGENTS.md`, `.cursor/rules/01-charter-enforcement.md`, `.cursor/rules/05-global-mcp-usage.md`, `.cursor/rules/10-project-workflow.md`, and `docs/ai/memory/MEMORY_CONTRACT.md`
3. `docs/ai/STATE.md` summary/current state section
4. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md`
5. `docs/ai/context/`
6. Chat history / pasted artifacts (last resort)

If repository-tracked sources and chat context disagree, repository-tracked sources win unless current execution evidence proves otherwise.

## Recovery bundle discipline

The recovery bundle is a non-canonical filesystem speed layer.

- Use it after the authority contract and OpenMemory, not before them.
- Keep it compact and pointer-heavy.
- Never let it override repo docs.
- If it is stale or missing, record that and continue with canonical sources.

## docs/ai/context/ — non-canonical artifact storage

`docs/ai/context/` stores transcript-derived artifacts, bulk session dumps, and ephemeral context files. It is **informative only** — never authoritative. PLAN should consult it only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md` are insufficient. Do not promote content from `docs/ai/context/` into rules or architecture docs without explicit review.

## docs/ai/archive/ — never consulted

`docs/ai/archive/` stores superseded documents that have been replaced by newer versions. PLAN must **never** consult this directory when reconstructing system state. It exists solely for historical reference and audit trails. Files moved here are considered retired from the active governance surface.

## AGENT Execution Ledger — non-canonical verbatim record

`docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a durable, non-canonical log. It records the verbatim execution prompt and verbatim final AGENT response for every completed prompt block, plus files changed and verdict.

**AGENT append requirement (mandatory):** After every completed prompt block, AGENT must append one entry. This is as required as the STATE.md update. If a block produces no artifacts (pure investigation), record that explicitly.

**PLAN/DEBUG consultation gate (strict):** PLAN and DEBUG must NOT load this ledger by default or attach it to standard bootstrap reads. They may read it only when:
1. STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient to answer the question.
2. The exact prompt text or exact response text from a prior AGENT block is specifically needed.
3. Read **one block at a time**. Stop reading as soon as sufficient context is recovered. Do not preload multiple entries unless one block proves insufficient.

**Size management:**
- Active ledger: keep the 3–5 most recent entries.
- Archive threshold: when entries exceed 5 or file exceeds ~300 lines, AGENT moves oldest entries verbatim to `docs/ai/context/archive/ledger-<YYYY-MM-DD>.md`.
- Archived files are non-canonical and historical only. PLAN and DEBUG must not include them in default reads.
- Exact prompt and response text must never be summarized or paraphrased when archiving — move verbatim.

## Context attachment discipline

- Attach files with intent, not habit.
- Attach the minimum set needed for the current tab's job.
- Prefer referencing paths and targeted excerpts over pasting entire files.
- If a file is attached, assume it is read fully.
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

### Artiforge

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

### context-matic

#### Source: `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` (Project: AI-Project-Manager)

```
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
```

#### Source: `D:/github/open--claw/.cursor/rules/05-global-mcp-usage.md` (Project: open--claw)

```
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
```

#### Source: `D:/github/droidrun/.cursor/rules/05-global-mcp-usage.md` (Project: droidrun)

```
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

Use `filesystem` only when local machine files outside the active repo are explicitly required and no repo-native source exists.

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

## Unavailable-tool policy

If a high-value tool is required for the current task and it is disabled, unavailable, or failing:

1. Stop immediately.
2. Name the exact tool.
3. State exactly why it is required for this task.
4. Ask the user to enable or restore it in Cursor if it is a toggle/config issue.
5. Record the blocker in `docs/ai/STATE.md`.

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
```

## Summary and Recommendations

### How rules are applied in practice

- **Cursor layering**: User-global rules under `D:/.cursor/rules` and `D:/github/.cursor/rules` load alongside per-repo `.cursor/rules` when those folders are on the Cursor rules path for the session. Overlapping filenames (for example `smart-assumptions.mdc`) can exist in both global roots with **different** `alwaysApply` / behavior (notably `00-memory-autopilot.mdc`).
- **Tri-workspace project packs**: `AI-Project-Manager`, `open--claw`, and `droidrun` share a family of numbered workflow rules (`00`, `01`, `02`, `05`, `10`, `20`, plus repo-specific extensions). `AI-Project-Manager` versions are the most expansive for MCP/recovery-bundle policy; `open--claw` adds `15-model-routing.md` and `sparky-mandatory-tool-usage.md` plus stricter employee standards.
- **When Applied metadata**: Several files omit normal YAML fences (`fetch-rules.mdc` has no frontmatter; `AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` begins with `description:` without an opening `---`). The audit still includes them verbatim; `When Applied` is taken from `alwaysApply`, `globs` / `applies_to`, explicit triggers in the rule text (for example “Before substantial work”), or defaults to `always` when nothing more specific applies.

### Contradictions / inconsistencies

- **`00-memory-autopilot.mdc` (global)**: `D:/github/.cursor/rules` sets `alwaysApply: true` and pushes proactive memory MCP usage; `D:/.cursor/rules` sets `alwaysApply: false` and frames memory as optional. Same filename, opposite default.
- **Autonomous rule creation**: `D:/github/.cursor/rules/autonomous-rule-creation.mdc` says do NOT create rules except on explicit user request / confirmed repetition; `D:/.cursor/rules/autonomous-rule-creation.mdc` (`alwaysApply: false`) frames automatic creation from feedback. Different defaults and triggers.
- **Post-task cleanup / proactive rules**: Several paired files differ by `alwaysApply` true vs false between `D:/github/.cursor/rules` and `D:/.cursor/rules`.
- **OpenMemory schema**: `AI-Project-Manager` / `open--claw` / `droidrun` `openmemory.mdc` and `05-global-mcp-usage.md` emphasize a **flat** tool surface (`search-memories`, `list-memories`, `add-memory`) and warn against claiming `project_id` / namespaces unless proven. `open--claw/.cursor/rules/sparky-mandatory-tool-usage.md` still prescribes namespace-heavy OpenMemory flows (`openmemory.search-memory` with namespace filters, `governance`, `project:open-claw`, etc.).
- **Thinking-patterns failure behavior**: `MCP-AGENT_RULES.mdc` instructs retry-once then safest fallback per repo policy; `AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md` states architecture work should **stop** if `thinking-patterns` is degraded. These can diverge under failure.
- **Required-tool failure policy**: `AI-Project-Manager` `05-global-mcp-usage.md` allows explicit degraded fallbacks for some tools; `droidrun` `05-global-mcp-usage.md` uses a stricter **stop + ask user** pattern for unavailable tools.
- **`memory-bank-instructions.mdc`**: The file contains duplicated frontmatter/body segments mid-file; it is included verbatim.
- **`coding-standards.mdc`**: Contains a line instructing to insert a debug print in every Python function; this conflicts with typical hygiene rules elsewhere (and with `no-secrets`/production quality expectations).

### Suggestions for stronger autonomy (vibe-coder expectations)

- **Collapse global duplicates**: Pick one canonical `alwaysApply` stance per basename for shared global rules, or rename one copy to avoid Cursor merging conflicting instructions.
- **Make failure modes uniform**: Align "stop vs degrade" per tool tier across `AI-Project-Manager` and `droidrun` 05-files so autonomous agents do not need a human to interpret which repo root is authoritative in a multi-root session.
- **Reconcile Sparky OpenMemory guidance** with the flat-runtime contract (remove or gate namespace examples behind an explicit "if wrapper exists" flag).
- **Automate heavy evidence**: Where rules demand PASS/FAIL for every tool call plus large `STATE.md` templates, add hooks/scripts that reduce manual templating friction so autonomy stays high without skipping compliance.

### Preferred-tool reinforcement (user “10 best tools” note)

The preferred-tool list is now a true set of **10** tools: Artiforge, Context7, Exa Search, filesystem, Magic MCP, Obsidian Vault, openmemory, playwright, thinking-patterns, and **serena**.

- **thinking-patterns**: Keep `MCP-AGENT_RULES.mdc` triggers but align failure policy with `05-global-mcp-usage.md` so PLAN/ARCH agents know when stop is mandatory vs fallback.
- **Context7**: Already REQUIRED for dependency/API work in tri-workspace `05`/`20`; add a lightweight pre-commit checklist item in AGENT prompts: "Context7 PASS/FAIL recorded" whenever imports change.
- **Exa Search / firecrawl-mcp**: Tie explicitly to research phases in PLAN templates whenever tasks include "current web" or structured extraction acceptance criteria.
- **filesystem**: Centralize recovery-bundle writes in one small script invoked post-block to reduce skipped bundle updates.
- **Magic MCP / playwright**: For UI tasks, require a two-line PLAN preamble naming the acceptance screenshots or DOM checks so browser tools are not optional in practice.
- **Obsidian Vault**: Keep the global + repo gates (explicit task need only); autonomy improves when Obsidian failure never blocks canonical work (already reflected in `AI-Project-Manager` policy).
- **openmemory**: Prefer the flat self-identifying text convention from `AI-Project-Manager` rules as the single writer spec; demote namespace examples in Sparky doc to avoid agents hallucinating unsupported parameters.
- **Artiforge**: Keep conditional post-canonical-read placement, but add an explicit "non-authoritative" footer requirement in prompts so autonomy does not confuse synthesis with policy.
- **serena**: Promote it into the preferred-tool set explicitly for multi-file code navigation, symbol-aware impact analysis, and refactor planning; require PLAN prompts for code-heavy work to state whether `serena` is required, optional, or not applicable so agents do not silently fall back to generic text search.
