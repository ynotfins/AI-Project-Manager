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
