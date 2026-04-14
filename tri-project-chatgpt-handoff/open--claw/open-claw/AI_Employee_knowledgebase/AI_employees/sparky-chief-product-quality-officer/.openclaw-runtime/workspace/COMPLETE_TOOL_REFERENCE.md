# Sparky's Complete Tool Reference

**Document Role:** This file is a **comprehensive tool inventory and reference catalog**. It is NOT an enforcement surface. For mandatory tool usage rules, see `.cursor/rules/sparky-mandatory-tool-usage.md`. For exec routing examples, see `TOOLS.md`. For access configuration, see `ACCESS.md`.

This document lists ALL tools available to Sparky (Chief Product Quality Officer) across the entire OpenClaw ecosystem.

## Tool Categories

1. **Reasoning & Planning** (thinking-patterns MCP) — 15 tools
2. **Memory & Persistence** (openmemory, obsidian-vault) — 6 tools
3. **Code Intelligence** (serena) — ~25 tools
4. **External Knowledge** (Context7, Exa Search, firecrawl-mcp) — 5 tools
5. **Repository Operations** (github) — ~10 tools
6. **UI & Browser** (playwright, Magic MCP) — ~15 tools combined
7. **Phone Control** (droidrun) — 3 tools
8. **File Operations** (filesystem) — multiple tools
9. **Built-in OpenClaw** (exec, browser, system.run) — core tools

---

## 1. thinking-patterns (15 Reasoning Tools)

**PRIMARY REASONING ENGINE** — Must be used for ALL non-trivial work.

### Systematic Thinking (Core)
1. **sequential_thinking** — Multi-step reasoning with revision support
   - Use for: Planning, step-by-step analysis, iterative problem-solving
   - Required parameters: `thought`, `thoughtNumber`, `totalThoughts`, `nextThoughtNeeded`
   - Can branch and revise thoughts

2. **problem_decomposition** — Break complex problems into manageable tasks
   - Use for: Planning, work breakdown, task hierarchies
   - Required parameters: `problem`, `decomposition` (array of Task objects)
   - Most error-prone tool — decomposition MUST be Task objects, not strings

3. **recursive_thinking** — Apply recursive strategies
   - Use for: Self-similar problems, fractal patterns, hierarchical structures
   - Required parameters: `problem`, `baseCases`, `recursiveCases`, `terminationConditions`

### Mental Models & Frameworks
4. **mental_model** — Apply proven frameworks
   - Use for: First Principles, Inversion, Second-Order Thinking
   - Required parameters: `modelName`, `problem`
   - Simplest tool — just name the model and describe problem

5. **decision_framework** — Multi-criteria decision analysis
   - Use for: Trade-off analysis, option comparison, strategic choices
   - Required parameters: `decisionStatement`, `options`, `analysisType`, `stage`
   - Analysis types: expected-utility, multi-criteria, maximin, minimax-regret, satisficing

6. **domain_modeling** — Create conceptual models
   - Use for: System design, architecture, domain understanding
   - Required parameters: `domainName`, `entities`, `stage`, `paradigm`
   - Paradigms: object-oriented, relational, functional, event-driven, service-oriented, domain-driven

### Scientific & Critical Analysis
7. **scientific_method** — Formal hypothesis testing
   - Use for: Experiments, hypothesis validation, systematic investigation
   - Required parameters: `stage`, `inquiryId`, `iteration`, `nextStageNeeded`
   - Stages: observation, question, hypothesis, experiment, analysis, conclusion, iteration

8. **critical_thinking** — Systematic evaluation
   - Use for: Argument analysis, assumption validation, risk assessment
   - Required parameters: `subject`, `potentialIssues`, `edgeCases`, `invalidAssumptions`, `alternativeApproaches`
   - MANDATORY before final decisions

9. **debugging_approach** — Systematic troubleshooting
   - Use for: Error diagnosis, systematic debugging, root cause analysis
   - Required parameters: `approachName`, `issue`
   - Methods: Binary Search Debugging, 5 Whys, Root Cause Analysis, Log Analysis

### Collaborative & Dialectical
10. **collaborative_reasoning** — Multi-perspective problem solving
    - Use for: Team discussions, diverse viewpoints, consensus building
    - Required parameters: `topic`, `personas`, `contributions`, `stage`
    - Stages: problem-definition, ideation, critique, integration, decision, reflection

11. **structured_argumentation** — Dialectical reasoning
    - Use for: Thesis/antithesis/synthesis, debate, argument construction
    - Required parameters: `claim`, `premises`, `conclusion`, `argumentType`
    - Types: thesis, antithesis, synthesis, objection, rebuttal

### Advanced Cognitive Patterns
12. **metacognitive_monitoring** — Self-assessment of reasoning
    - Use for: Confidence assessment, uncertainty mapping, strategy evaluation
    - Required parameters: `task`, `stage`, `overallConfidence`, `uncertaintyAreas`
    - Use to validate your own reasoning quality

13. **visual_reasoning** — Diagram-based thinking
    - Use for: Spatial reasoning, visual design, system diagrams
    - Required parameters: `operation`, `diagramId`, `diagramType`
    - Diagram types: graph, flowchart, state-diagram, concept-map, tree-diagram, network-diagram

14. **temporal_thinking** — Time-based system analysis
    - Use for: State machines, process flows, temporal patterns
    - Required parameters: `context`, `initialState`, `states`, `events`, `transitions`

### Probabilistic & Optimization
15. **stochastic_algorithm** — Decision-making under uncertainty [BETA]
    - Use for: MDPs, MCTS, Multi-Armed Bandit, Bayesian Optimization, HMMs
    - Required parameters: `algorithm`, `problem`

---

## 2. openmemory (4 Memory Tools)

**LONG-HORIZON PERSISTENT MEMORY** — Use at session start and after durable decisions.

1. **search-memory** — Query stored memories
   - Use for: Session recovery, finding past decisions, pattern lookup
   - Parameters: query text, namespace filters, limit
   - Namespaces: `governance`, `project:open-claw`, `project:droidrun`, `session:YYYY-MM-DD`

2. **add-memory** — Store new memories
   - Use for: Storing decisions, patterns, architecture components, lessons learned
   - Required: memory content, namespace, tags
   - MANDATORY after significant decisions or work completion

3. **update-memory** — Modify existing memories
   - Use for: Refining stored information, correcting outdated memories

4. **delete-memory** — Remove obsolete memories
   - Use for: Cleaning up outdated or incorrect information

**Usage Pattern:**
1. Session start → `search-memory` for relevant context
2. Work execution → Use other tools
3. Session end → `add-memory` for durable artifacts

---

## 3. obsidian-vault (Task-Oriented Note Tools)

**PERSONAL KNOWLEDGE BRIDGE** — Use for cross-project user context, not agent state.

Available through `obsidian-local-rest-api-mcp` package:
- Note search and retrieval
- Task management
- Cross-reference lookup
- Personal knowledge queries

**Use for:** User-facing knowledge, research findings, cross-project insights
**Do NOT use for:** Agent operational state (use openmemory instead)

---

## 4. serena (~25 Code Intelligence Tools)

**SYMBOL-AWARE CODE OPERATIONS** — Use for all code work in registered projects.

### Project Management
1. **activate_project** — Register or activate a Serena project
2. **get_current_config** — View active project configuration
3. **list_projects** — List all registered projects

### Code Reading (Symbol-Aware)
4. **get_symbols_overview** — Get high-level file structure
5. **find_symbol** — Search for symbols with optional body inclusion
6. **find_referencing_symbols** — Find all references to a symbol
7. **list_dir** — List directory contents
8. **read_file** — Read full file contents

### Code Editing (Symbol-Based)
9. **replace_symbol_body** — Replace entire symbol definition
10. **insert_after_symbol** — Add code after a symbol
11. **insert_before_symbol** — Add code before a symbol

### Code Editing (File-Based)
12. **replace_content** — Regex-based content replacement
13. **create_text_file** — Create new files
14. **delete_file** — Remove files
15. **rename_file** — Rename or move files

### Advanced Operations
16. **search_for_pattern** — Fast pattern search in codebase
17. **apply_patch** — Apply multi-file patches
18. **get_git_status** — Git status information
19. **get_git_diff** — Git diff output

**Registered Projects:**
- `AI-Project-Manager` → `D:/github/AI-Project-Manager`
- `open--claw` → `D:/github/open--claw`
- `open-claw-runtime` → `D:/github/open--claw/open-claw`
- `droidrun` → `D:/github/droidrun`

---

## 5. Context7 (2 Documentation Tools)

**EXTERNAL LIBRARY DOCUMENTATION** — Query current library docs, not training data.

1. **resolve-library-id** — Find correct library identifier
   - Use for: Disambiguating library names, finding correct package
   - Input: Library name (e.g., "React", "Prisma")
   - Output: Canonical library ID

2. **query-docs** — Query library documentation
   - Use for: API reference, version-specific behavior, migration guides
   - Input: Library ID, query, optional version
   - Output: Current documentation

**Mandatory for:** React, Next.js, Prisma, Express, Tailwind, Django, FastAPI, TypeScript, etc.

---

## 6. Exa Search (1 Web Research Tool)

**LIVE WEB RESEARCH** — Use for current ecosystem research.

1. **search** — Semantic web search
   - Use for: Current best practices, recent changes, public documentation
   - Prefer Context7 for library docs; use Exa for broader research

---

## 7. firecrawl-mcp (3 Web Extraction Tools)

**STRUCTURED WEB SCRAPING** — Extract content from websites.

1. **scrape** — Extract content from single URL
2. **map** — Generate sitemap from domain
3. **search** — Search web and extract results

---

## 8. github (~10 Repository Tools)

**REPOSITORY OPERATIONS** — Git and GitHub integration.

Available tools include:
- Repository browsing
- File operations
- Issue management
- Pull request operations
- Branch management
- Commit operations

---

## 9. playwright (Browser Automation)

**UI VERIFICATION & TESTING** — Browser control for E2E testing.

Available tools include:
- Browser navigation
- Element interaction
- Screenshot capture
- Assertion checking
- Network monitoring

---

## 10. Magic MCP (UI Generation)

**RAPID INTERFACE SCAFFOLDING** — Generate UI components.

Use for: Quick UI mockups, component scaffolding, design starts

---

## 11. droidrun (3 Phone Control Tools)

**SAMSUNG GALAXY S25 ULTRA CONTROL** — Android device automation.

1. **phone_do** — Execute ADB commands
   - Use for: App control, system operations, automation
   - Target: Samsung Galaxy S25 Ultra (Tailscale IP: 100.71.228.18)

2. **phone_ping** — Check device connectivity
   - Use for: Verifying phone is reachable

3. **phone_apps** — List installed applications
   - Use for: App inventory, package discovery

---

## 12. filesystem (Multiple File Tools)

**LOCAL FILE ACCESS** — Read/write to allowed directories.

Allowed paths:
- `D:\github`
- `C:\Users\ynotf`

---

## 13. Built-in OpenClaw Tools

**CORE EXECUTION CAPABILITIES** — Always available.

### exec (Shell Execution)
```
exec [command]              # Default: WSL gateway
exec --host node [command]  # Windows Desktop node
```

### browser (Web Browsing)
- Navigate to URLs
- Capture screenshots
- Extract page content

### system.run (Direct Windows Commands)
- Direct node invocation
- Windows-specific operations

---

## Tool Usage Priority

For any non-trivial task, use tools in this order:

1. **thinking-patterns** → Structure your approach
2. **openmemory** → Check for existing knowledge
3. **context7** → Query external docs (if needed)
4. **serena** → Code intelligence (if code work)
5. **exec/browser/other** → Execute implementation
6. **thinking-patterns** → Critical review
7. **openmemory** → Store durable results

---

## Enforcement

**ALL non-trivial tasks must use thinking-patterns FIRST.**

**ALL durable decisions must be stored in openmemory LAST.**

**ALL code work in registered projects must use serena.**

**ALL external library work must query context7.**

See `sparky-mandatory-tool-usage.md` for detailed enforcement rules.
