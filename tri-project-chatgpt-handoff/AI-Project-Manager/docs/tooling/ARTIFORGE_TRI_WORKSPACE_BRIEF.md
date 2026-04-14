# Artiforge Tri-Workspace Brief

This document is the handoff brief for the Artiforge AI MCP server.

Its purpose is to explain the tri-project workspace, the five-tab workflow, the authority hierarchy, the mandatory docs/rules, and the responsibilities Artiforge must respect when generating scaffolds or project guidance.

## Core Directive

Artiforge is not the authority.

It is a supporting tool inside a governed tri-workspace:

- `AI-Project-Manager` manages the workflow for all projects.
- `open--claw` holds the supreme product charter and quality mandate.
- `droidrun` is the Android actuator/runtime-control layer.

If Artiforge generates anything that conflicts with the charter, repo rules, or workflow contracts, Artiforge is wrong and the repo wins.
Artiforge is a scaffold and synthesis helper only.

## Authority Hierarchy

Read and obey this order:

1. `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. Tony's explicit permission to change that file
3. `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/AUTHORITATIVE_STANDARD.md`
4. `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md`
5. Repo-local rules and workflow docs
6. `docs/ai/STATE.md` and `docs/ai/HANDOFF.md` as operational evidence only

Interpretation:

- `FINAL_OUTPUT_PRODUCT.md` is supreme product law.
- `AI-Project-Manager` governs workflow/process, not product law.
- `STATE.md` and `HANDOFF.md` describe what happened; they do not redefine the product.

## Tri-Workspace Model

| Workspace | Role | What it owns |
| --- | --- | --- |
| `AI-Project-Manager` | Workflow and process layer | Tab discipline, planning protocol, execution contracts, state logging, MCP policy, cross-repo orchestration |
| `open--claw` | Strict enforcement center | Product charter, AI employee knowledgebase, quality standards, Sparky's mandate |
| `droidrun` | Actuator layer | Android device automation, phone MCP tooling, Portal/APK bridge, execution on devices |

### Practical meaning

- `AI-Project-Manager` is the management/governance hub for all projects.
- `PLAN` lives conceptually under this management layer and must maintain constant accurate cross-project awareness.
- `PLAN` writes the execution prompt for `AGENT`.
- `AGENT` executes edits from that prompt and must log actions exactly as the workflow docs require.
- `open--claw` decides what the system must become.
- `droidrun` performs device-side execution and Android automation.

## Five-Tab Workflow

The workspace uses exactly five Cursor tabs:

| Tab | Role | File edits | Commands |
| --- | --- | --- | --- |
| `PLAN` | Architect / strategist | No | No |
| `AGENT` | Executor / implementer | Yes | Yes |
| `DEBUG` | Investigator / forensics | No | No |
| `ASK` | Scratchpad / exploration | No | No |
| `ARCHIVE` | Documentation curator / compressor | Docs only | No |

### PLAN

PLAN is the orchestrator and prompt-writer.

PLAN must:

- not edit files
- not run commands
- reconstruct state from canonical sources before reasoning
- minimize context waste while preserving No-Loss awareness
- end with exactly one copy-pastable AGENT prompt
- explicitly choose the AGENT model and reasoning mode

### AGENT

AGENT is the executor.

AGENT must:

- execute the PLAN prompt exactly
- perform file edits and commands
- use MCP tools according to policy
- update `docs/ai/STATE.md` after every execution block
- append one block to `docs/ai/context/AGENT_EXECUTION_LEDGER.md` after every completed prompt block
- keep `docs/ai/HANDOFF.md` accurate when project state changes
- record PASS/FAIL evidence for every command and tool

### DEBUG

DEBUG investigates without editing. It produces ranked causes, evidence needs, root cause, and an AGENT fix prompt.

### ASK

ASK is a non-binding exploration tab for options, trade-offs, and quick research. Nothing becomes authoritative until promoted into PLAN.

### ARCHIVE

ARCHIVE is docs-only. It compresses and promotes durable knowledge, keeps handoff concise, and never implements product features.

## Must-Read Files For Artiforge

These are the minimum files Artiforge should be given or read before generating scaffolding for this workspace.

### Universal required reads

Read these in this order:

1. `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. `D:/github/AI-Project-Manager/AGENTS.md`
3. `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md`
4. `D:/github/AI-Project-Manager/.cursor/rules/10-project-workflow.md`
5. `D:/github/AI-Project-Manager/docs/ai/memory/MEMORY_CONTRACT.md`
6. `D:/github/AI-Project-Manager/docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`
7. `D:/github/AI-Project-Manager/docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`
8. `D:/github/AI-Project-Manager/docs/ai/CURSOR_WORKFLOW.md`
9. `D:/github/AI-Project-Manager/docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md`

### Workflow and governance reads

- `D:/github/AI-Project-Manager/docs/ai/operations/SESSION_BOOTSTRAP_SOP.md`
- `D:/github/AI-Project-Manager/docs/ai/operations/POLICY_DRIFT_CHECKER.md`
- `D:/github/AI-Project-Manager/docs/tooling/MCP_CANONICAL_CONFIG.md`
- `D:/github/AI-Project-Manager/docs/tooling/PRIORITY_TOOL_USAGE.md`
- `D:/github/AI-Project-Manager/docs/ai/context/TRI_WORKSPACE_CONTEXT_BRIEF.md` only if repo selection is unclear
- `D:/github/AI-Project-Manager/docs/ai/STATE.md` summary/current state only after the authority contract
- `D:/github/AI-Project-Manager/docs/ai/HANDOFF.md`, `DECISIONS.md`, or `PATTERNS.md` on demand only

### Product-law reads from `open--claw`

- `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
- `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/AUTHORITATIVE_STANDARD.md`
- `D:/github/open--claw/open-claw/AI_Employee_knowledgebase/TEAM_ROSTER.md`
- `D:/github/open--claw/AGENTS.md`
- `D:/github/open--claw/docs/ai/CURSOR_WORKFLOW.md`

### Open Claw project definition docs

- `D:/github/open--claw/README.md`
- `D:/github/open--claw/open-claw/docs/VISION.md`
- `D:/github/open--claw/open-claw/docs/REQUIREMENTS.md`
- `D:/github/open--claw/open-claw/docs/MODULES.md`
- `D:/github/open--claw/open-claw/docs/INTEGRATIONS.md`

### DroidRun project reads

- `D:/github/droidrun/README.md`
- `D:/github/droidrun/AGENTS.md`
- `D:/github/droidrun/docs/ai/CURSOR_WORKFLOW.md`
- `D:/github/droidrun/src/README.md`

## Project Responsibilities

## `AI-Project-Manager`

### What it is

The governance hub for all Cursor-managed projects under `D:\github` and `D:\github_2`.

### What it contains

- Cursor workflow rules and agent contracts
- execution state and planning docs
- MCP server configuration references
- tooling health logs
- memory policies

### What it is responsible for

- governing the five-tab workflow
- defining how PLAN and AGENT operate
- maintaining state, handoff, decisions, patterns, and workflow evidence
- managing cross-repo orchestration
- defining tool policy and launch/bootstrap discipline

### What it is not

- not the supreme product authority
- not the main application runtime
- not the Android execution layer

## `open--claw`

### What it is

The strict enforcement center of the tri-workspace.

### What it contains

- the supreme product charter
- the curated AI employee knowledgebase
- Open Claw project docs
- role/quality standards and model-routing policy

### What it is responsible for

- defining what the finished product must become
- defining the AI employee operating standard
- defining team structure and Sparky's authority
- enforcing quality, simplicity, modularity, and acceptance discipline

### What it is not

- not the workflow manager for the whole workspace
- not the Android device actuator

## `droidrun`

### What it is

The Android actuator layer for the wider Cursor/OpenClaw stack.

### What it contains

- Android device control framework
- natural-language-driven mobile automation
- phone MCP tooling
- Portal/APK + ADB transport boundary

### What it is responsible for

- executing Android automation tasks
- providing device-side control primitives
- acting as the phone/runtime bridge for the larger autonomous system

### What it is not

- not the supreme authority
- not the workflow orchestrator
- not a general iOS/mobile repo in this workspace

## Mandatory Logging and Documentation Duties

If Artiforge outputs prompts, scaffolds, or guidance for AGENT work, it must assume these logging duties are mandatory:

- `docs/ai/STATE.md` must be updated after every execution block
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` must get one block after every completed prompt block
- `docs/ai/HANDOFF.md` must stay accurate when state meaningfully changes
- PASS/FAIL evidence must be recorded for each tool call and command
- unresolved turbulence belongs in `HANDOFF.md`, not only in `STATE.md`

## Canonical Context Reconstruction Rules

When generating prompts or scaffolds for PLAN/AGENT behavior, Artiforge must assume this retrieval order:

1. product charter first
2. repo authority contract
3. targeted OpenMemory search
4. recovery bundle, if present and current
5. `STATE.md` summary/current state section
6. exactly one of `DECISIONS.md`, `PATTERNS.md`, or `HANDOFF.md` if needed
7. `docs/ai/context/` only when canonical sources are insufficient
8. past chat only as a last resort

Additional No-Loss rules:

- OpenMemory is the retrieval pre-step before broad file reading
- the current OpenMemory Cursor surface is flat, so Artiforge must not invent unsupported metadata filters
- the recovery bundle is a non-canonical filesystem speed layer only
- `obsidian-vault` is optional sidecar memory, not canonical state
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is non-canonical and must never be default preload

## Rules Artiforge Must Respect

## Repo-tracked mandatory rules across the tri-workspace

These are the canonical project rules. Read them from the repo files, not from summaries.

### Common tri-workspace rule stack

- `D:/github/AI-Project-Manager/.cursor/rules/00-global-core.md`
- `D:/github/AI-Project-Manager/.cursor/rules/01-charter-enforcement.md`
- `D:/github/AI-Project-Manager/.cursor/rules/02-non-routable-exclusions.md`
- `D:/github/AI-Project-Manager/.cursor/rules/05-global-mcp-usage.md`
- `D:/github/AI-Project-Manager/.cursor/rules/10-project-workflow.md`
- `D:/github/AI-Project-Manager/.cursor/rules/20-project-quality.md`
- `D:/github/AI-Project-Manager/.cursor/rules/openmemory.mdc`

### What these rules mean

- `00-global-core.md`: authority, tab separation, evidence-first, PASS/FAIL discipline, mandatory `STATE.md` updates
- `01-charter-enforcement.md`: hard-stop enforcement of the product charter
- `02-non-routable-exclusions.md`: quarantined/out-of-scope paths
- `05-global-mcp-usage.md`: MCP-first behavior and tool triggers
- `10-project-workflow.md`: PLAN/AGENT/DEBUG contracts and `STATE.md` template
- `20-project-quality.md`: modularity, testing, secrets, diff discipline
- `openmemory.mdc`: durable memory retrieval/storage behavior

## Open Claw-specific overlays

In addition to the common stack, `open--claw` has these extra rule files:

- `D:/github/open--claw/.cursor/rules/15-model-routing.md`
- `D:/github/open--claw/.cursor/rules/25-ai-employee-standard.mdc`
- `D:/github/open--claw/.cursor/rules/sparky-mandatory-tool-usage.md`

### What they add

- `15-model-routing.md`: tab defaults, internal model escalation, Sparky routing, no silent degradation
- `25-ai-employee-standard.mdc`: required AI employee packet structure and quality gates
- `sparky-mandatory-tool-usage.md`: mandatory tool usage and evidence discipline for Sparky

## Machine-global user rules

Machine-global rules also exist, but they are subordinate to the charter and repo-tracked rules.

Reference file:

- `D:/github/AI-Project-Manager/docs/global-rules.md`

Important note:

- `docs/global-rules.md` is a historical/generated reference snapshot, not the canonical authority
- canonical active behavior is still defined by `.cursor/rules/*` and `AGENTS.md`

Machine-global overlays listed there include items such as:

- `core`
- `decisive-implementation`
- `auto-error-fixing`
- `memory-bank-instructions`
- `post-task-cleanup`
- `proactive-completion`
- `proactive-scanning`
- `smart-assumptions`
- `autonomous-rule-creation`
- `rule-visibility`

Artiforge should treat these as secondary overlays, never as a replacement for repo authority.

## Tooling Expectations

Artiforge should assume the workspace is MCP-first.

Key policy points from `05-global-mcp-usage.md`:

- `thinking-patterns` is required for non-trivial reasoning
- `serena` is required for code intelligence on multi-file or symbol-heavy work
- `Context7` is required for external library/framework docs
- `openmemory` is required for durable cross-session decision/pattern retrieval
- `filesystem` is the recovery-bundle access path when machine-local recovery artifacts matter
- `obsidian-vault` is a sidecar-note path only
- `Artiforge` output itself is never authoritative
- `droidrun` is required for phone interaction
- `github` is required for repo/PR/issue operations

## Non-Negotiables For Generated Scaffolding

Anything Artiforge produces for this workspace must preserve these invariants:

- never weaken or bypass `FINAL_OUTPUT_PRODUCT.md`
- never collapse the five-tab model into a single mixed workflow
- never let PLAN edit files or run commands
- never let AGENT skip `STATE.md` / ledger / handoff obligations
- never treat `STATE.md` as product law
- never use archived docs as active truth
- never use `obsidian-vault` as a replacement for OpenMemory or repo docs
- never route through quarantined iOS or candidate-employee paths
- always favor modular boundaries such as `ui`, `domain`, `data`, and `utils`
- always preserve evidence-first, PASS/FAIL, and no-secrets discipline

## Short Operating Summary For Artiforge

If Artiforge needs the shortest accurate mental model, use this:

- `AI-Project-Manager` runs the workflow.
- `open--claw` defines the law.
- `droidrun` executes Android/device actions.
- `PLAN` must maintain full, accurate, lossless project awareness and write the next AGENT prompt.
- `AGENT` executes edits and must log every meaningful action into the required docs.
- All outputs are subordinate to the charter and repo-tracked rules.
