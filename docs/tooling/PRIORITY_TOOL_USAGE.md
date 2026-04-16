# Priority Tool Usage

This file is a quick trigger guide only.

- `docs/tooling/MCP_CANONICAL_CONFIG.md` owns the live installed-tool matrix
- `.cursor/rules/05-global-mcp-usage.md` owns mandatory triggers and degraded-tool policy
- `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md` owns the numbered bootstrap order

## Must Use

| Tool | Use when | Failure behavior |
| --- | --- | --- |
| `thinking-patterns` | non-trivial PLAN/AGENT/DEBUG reasoning, cross-repo decomposition, proof work | if unavailable for required reasoning, stop and record FAIL |
| `openmemory` | targeted recovery before non-trivial work and durable memory write after verified governance/code changes | if degraded and the task is still safely satisfiable, use repo docs + recovery bundle and record reseed debt |
| `filesystem` | reading and writing the four AI-PM recovery-bundle files | if degraded, use built-in file tools only for repo files and record the evidence gap |
| `serena` | code/symbol work inside a valid project path | if the task is docs-only, mark not applicable; if symbol-aware code work is required and Serena fails, stop |
| `Context7` | external library, framework, SDK, API, CLI, or cloud-service docs | if unavailable, fall back to built-in web tools and record reduced confidence |

## May Use

| Tool | Normal role | Default stance |
| --- | --- | --- |
| `Exa Search` | current public-web research beyond vendor docs | avoid unless current-web evidence is needed |
| `playwright` | browser verification and screenshots | avoid unless browser execution is part of acceptance |
| `Magic MCP` | UI/design scaffolding | avoid unless UI scaffold generation is requested |
| `droidrun` | phone/device interaction | task-scoped only |
| `Artiforge` | post-canonical synthesis/scaffold help | avoid by default; never authoritative |
| `obsidian-vault` | sidecar operator notes | optional and always non-blocking |

## Avoid By Default

These tools are not part of the current installed default surface and must not be described as installed/current without fresh proof:

- `github`
- `firecrawl-mcp`
- `context-matic`
- standalone `sequential-thinking`

## Live OpenMemory Reality

The current proven runtime is flat:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Do not claim `project_id`, `namespace`, `user_preference`, `memory_types`, or metadata-filter semantics unless the active runtime proves them again.

## Trigger Corrections

- `Context7` is often overforced when docs frame it as default-on for ordinary recovery; it should stay external-docs-only.
- `obsidian-vault` is overforced whenever a doc implies it belongs in bootstrap; it does not.
- `filesystem` is underused if a pass updates recovery state without refreshing `docs/ai/recovery/*`.
- `serena` is overforced if a docs-only governance pass pretends symbol tooling is required.

## Serena Project Map

- `D:/github/AI-Project-Manager`
- `D:/github/open--claw/open-claw`
- `D:/github/droidrun`

Use exact-path activation. `D:/github/open--claw` repo root is governance/docs-heavy and is not the default Serena code project.

## Failure Protocol

When a required tool fails:

1. Announce FAIL immediately.
2. Name the exact tool and exact lost step.
3. State the safe fallback, if one exists.
4. Record the evidence gap in `docs/ai/STATE.md`.
