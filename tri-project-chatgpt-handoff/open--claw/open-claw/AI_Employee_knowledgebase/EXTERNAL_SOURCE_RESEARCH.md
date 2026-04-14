# External Source Research

## Goal
Identify the strongest outside sources for building high-quality AI employees, not just role labels or personality packs.

## Best Sources By Category
### 1. Best role-definition source
- `agency-agents`

Why:
- deepest role files
- real deliverables and templates inside the role docs
- strong specialist depth across product, design, engineering, testing, and operations

Best example files:
- `source_repos/agency-agents/agency-agents-main/product/product-manager.md`
- `source_repos/agency-agents/agency-agents-main/engineering/engineering-backend-architect.md`

### 2. Best official file-map authority
- OpenClaw official docs

Why:
- confirms what belongs in an OpenClaw workspace
- confirms the role of `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, `MEMORY.md`, `HEARTBEAT.md`, and `BOOTSTRAP.md`
- confirms that workspace files are injected into prompt context and must be managed carefully

Most useful docs found:
- `https://docs.openclaw.ai/reference/templates/AGENTS`
- `https://docs.openclaw.ai/reference/templates/SOUL`
- `https://docs.openclaw.ai/cli/agents`

### 3. Best OpenClaw-shaped agent packaging source
- `awesome-openclaw-agents`

Why:
- strongest OpenClaw-native folder shape
- good `SOUL.md` quality
- good `README.md` with examples and configuration ideas
- good example-driven packaging

Best example folder:
- `source_repos/awesome-openclaw-agents/awesome-openclaw-agents-main/agents/security/vuln-scanner/`

### 4. Best workspace optimization source
- `ocaudit`

Why:
- strongest external source for token efficiency, file purpose boundaries, and anti-bloat rules
- turns “have lots of files” into measurable workspace quality
- especially useful for defining what should and should not live in `AGENTS.md`, `SOUL.md`, and `HEARTBEAT.md`

Most useful files:
- `https://github.com/johnpaulhayes/ocaudit/blob/main/README.md`
- `https://github.com/johnpaulhayes/ocaudit/blob/main/references/best-practices.md`

### 5. Best simple memory-and-workspace pattern
- `agent-template`

Why:
- clean explanation of identity files plus persistent memory structure
- useful for multi-agent pipelines and handoff thinking
- not OpenClaw-native, but strong on the concept of a durable agent workspace

Most useful files:
- `https://github.com/ExpertVagabond/agent-template/blob/main/README.md`
- `https://github.com/ExpertVagabond/agent-template/blob/main/QUICKSTART.md`

## Public OpenClaw Collection Notes
### `will-assistant/openclaw-agents`
Value:
- good public collection of OpenClaw-style personality packs
- useful for `SOUL.md`, `README.md`, `IDENTITY.md`, examples, and metadata ideas

Limitation:
- most folders are still lighter than the house standard needed for full autonomous software employees
- stronger for persona packaging than for deep specialist execution systems

## Purchased CrewClaw Packet Position
The purchased non-generic CrewClaw packets are not the best source overall.

Best purchased packet:
- `software-engineer.zip`

Value:
- six role files worth partial salvage
- useful as a lower-tier reference for code-oriented role language

Limitation:
- not complete end-to-end
- outdated runtime shell
- generic workflows
- most sibling purchased packets are mostly wrapper-level quality

## Key Research Conclusion
There is still no single imported folder that can be accepted unchanged as the perfect AI employee.

The best standard is a hybrid:
1. OpenClaw docs for official workspace structure
2. `agency-agents` for role-definition depth
3. `awesome-openclaw-agents` for OpenClaw-facing packaging examples
4. `ocaudit` for token-budget and file-boundary discipline
5. house curation for provenance, audits, and runtime readiness
