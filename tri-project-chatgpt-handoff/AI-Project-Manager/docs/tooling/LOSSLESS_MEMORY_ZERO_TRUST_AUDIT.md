# Lossless Memory Zero-Trust Audit

This document records the current, tested state of the tri-workspace memory and context system.

It separates:

- what is proven by direct runtime checks
- what is only documented
- what is currently failing

## Scope

This audit covers the tri-workspace opened by `C:\Users\ynotf\.openclaw\openclaw.code-workspace`:

- `D:\github\AI-Project-Manager`
- `D:\github\open--claw`
- `D:\github\droidrun`

In this workspace, the single PLAN authority is `AI-Project-Manager`.

## Legend

- `✓` = directly proven by a runtime test in this audit
- `✓✓` = directly proven and exercised in a live working task during this audit
- `FAIL` = directly tested and currently broken
- `HIGH` / `MED` / `LOW` = not fully proven end-to-end; trust rating based on surrounding evidence

## Current Wiring

### Control plane

- PLAN governance lives in `D:\github\AI-Project-Manager`
- Global MCP config lives in `C:\Users\ynotf\.cursor\mcp.json`
- Cursor is launched through `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`
- MCP patching is enforced by `C:\Users\ynotf\.openclaw\patch-mcp.ps1`
- Ledger rotation is configured by `D:\github\AI-Project-Manager\.cursor/hooks.json`

### Canonical repo-tracked context surfaces

- `docs/ai/STATE.md`
- `docs/ai/memory/DECISIONS.md`
- `docs/ai/memory/PATTERNS.md`
- `docs/ai/HANDOFF.md`
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` as a gated cold fallback only

### Memory system roles

- `openmemory` = durable compact long-horizon memory
- `obsidian-vault` = scoped fast-access operator-note sidecar
- repo docs = canonical operational truth
- rules = procedural and containment truth

## Endpoint And Tool Verification

| Surface | Expected role | Observed result | Status | Notes |
|---|---|---|---|---|
| `thinking-patterns` MCP | primary structured reasoning | `mental_model` call succeeded and was used during this audit | `✓✓` | Primary reasoning MCP is live |
| `Context7` MCP | current external docs | `resolve-library-id` and `query-docs` succeeded for `Cursor` and `mem0` during this audit | `✓✓` | Current docs available without broad web preload |
| `openmemory` MCP | durable long-term memory | `search-memories` succeeded; `check_openmemory_stack.ps1` passed all checks | `✓✓` | Server and descriptors are live |
| `openmemory` schema richness | scoped memory isolation | Live Cursor tool schema exposes only `query` for search and only `content` for add | `FAIL` | Current Cursor-exposed schema is much thinner than repo docs assume |
| `serena` MCP | exact-path project awareness | `activate_project` succeeded for `AI-Project-Manager`, `open--claw`, and `droidrun` | `✓✓` | Repo awareness is live |
| `obsidian-vault` MCP | fast note retrieval | Pre-fix calls failed with `fetch failed`; post-transport-correction probe now fails with `404 Not Found` | `FAIL` | Transport fix was necessary but not sufficient |
| Obsidian Local REST root | local note API | `http://127.0.0.1:27123` returned HTTP 200 | `✓` | Local API is alive |
| Obsidian HTTPS on 27123 | secure note API | `https://127.0.0.1:27123` failed with SSL wrong-version error | `FAIL` | Current `obsidian-vault` transport points here incorrectly |
| Obsidian OpenAPI server spec | authoritative local API wiring | `docs/obsidian/openapi.yaml` defines HTTP on `27123` and HTTPS on `27124` | `✓` | Confirms the current MCP config is wrong |
| `afterFileEdit` ledger hook config | auto-rotate ledger | Hook file and rotation script exist and are internally consistent | `HIGH` | Config/script proven; live Cursor hook fire not yet observed in this audit |
| Ledger auto-rotation in a real Cursor edit | no-manual ledger maintenance | Not re-tested live in this audit | `LOW` | Historical docs mention manual force test only |
| OpenClaw -> OpenMemory bridge | no-loss promotion path | `STATE.md` still marks this as NOT STARTED | `FAIL` | Architectural intent exists; implementation does not |
| Global secret-free MCP config | reproducible zero-trust launch | `openmemory`, `github`, `firecrawl-mcp`, and `Magic MCP` are secret-free in JSON, but Artiforge persists a PAT in the URL | `FAIL` | Current global config is not fully secret-free |

## Proven Contradictions

### 1. Obsidian transport is wrong in both docs and live config

Current docs and config point `obsidian-vault` at:

- `https://127.0.0.1:27123`

But runtime evidence shows:

- `http://127.0.0.1:27123` is live
- `https://127.0.0.1:27123` is wrong
- `docs/obsidian/openapi.yaml` defines HTTP on `27123` and HTTPS on `27124`

This is the direct cause of the current `obsidian-vault` MCP failure.

Follow-up evidence after correcting the transport:

- the failure mode changed from `fetch failed` to `404 Not Found`
- this strongly suggests the bridge is now reaching the API
- at least one additional adapter/plugin mismatch still remains

### 2. The documented OpenMemory model is richer than the live Cursor tool surface

Repo rules and architecture docs assume Cursor can do scoped calls like:

- `project_id`
- `namespace`
- `memory_types`
- `user_preference`

But the live Cursor descriptors currently expose:

- `search-memories(query)`
- `add-memory(content)`
- `list-memories()`
- `delete-all-memories()`

That means the current no-loss design cannot rely on rich in-tool filtering through Cursor alone.

### 3. The current secret-free MCP claim is only partially true

The live `C:\Users\ynotf\.cursor\mcp.json` is secret-free for several servers, but Artiforge currently embeds a PAT in the URL query string.

That violates the documented "no secrets in `mcp.json`" model.

### 4. Some no-loss claims are still aspirational

Directly from current repo evidence:

- OpenClaw <-> OpenMemory bridge is not started
- live ledger hook firing in Cursor is not proven in this audit
- memory exclusion behavior is documented but not re-proven in this audit

### 5. Fresh PLAN context waste still comes from always-apply rule mass

The explicit bootstrap prompts were reduced, but fresh chats still inherit heavy always-apply rule payloads, especially `openmemory.mdc` in `AI-Project-Manager`.

## Trust Model

### High trust

- `thinking-patterns` as the primary reasoning MCP
- `Context7` as the external-doc MCP
- `openmemory` server availability and stdio health
- Serena exact-path activation across the tri-workspace
- HTTP Obsidian API root on port `27123`

### Medium trust

- Ledger rotation logic in `.cursor/hooks/rotate_ledger.py`
- repo-level no-loss architecture intent in `NO_LOSS.md`
- current bootstrap and recovery policy encoded in rules and tab prompts

### Low trust

- live `afterFileEdit` hook firing in the current Cursor session
- end-to-end Obsidian MCP note retrieval until the transport is corrected and re-tested
- claims that OpenMemory namespace/project isolation is available through the current Cursor tool surface
- any "zero context loss" claim that depends on the unbuilt OpenClaw bridge

## Proposed Low-Bloat Lossless Memory System

The next version should be built around six layers.

### 1. Governance layer

Source:

- `AI-Project-Manager/.cursor/rules/*`
- `AI-Project-Manager/AGENTS.md`
- compact governance memories in OpenMemory

Role:

- cross-project routing
- tool policy
- containment rules
- PLAN preload policy

### 2. Canonical repo state layer

Source:

- `STATE.md`
- `DECISIONS.md`
- `PATTERNS.md`
- `HANDOFF.md`

Role:

- canonical crash recovery
- operational truth
- durable reasoning summaries

This layer must remain the default recovery source before any raw history.

### 3. Durable compact memory layer

Source:

- `openmemory`

Role:

- compact long-horizon recall
- reusable durable facts
- cross-session retrieval

Constraint:

- because the live Cursor tool surface is flat, memory entries must stay compact and self-identifying until a richer wrapper exists
- do not assume true namespace/project filtering is available from Cursor today

### 4. Fast operator note layer

Source:

- `obsidian-vault`

Role:

- fast targeted notes
- operator research
- daily-note workflow
- personal or cross-project context that should not become canonical project state

Constraint:

- never default preload
- never authoritative over repo docs or OpenMemory

### 5. Cold raw evidence layer

Source:

- `docs/ai/context/AGENT_EXECUTION_LEDGER.md`
- archived ledgers
- important screenshots/logs

Role:

- exact lookback
- forensics
- audit trail

Constraint:

- never default preload
- read one block at a time only

### 6. Recovery snapshot layer

This is the missing piece for "no handoff new chat" behavior.

Recommended addition:

- a compact `docs/ai/context/PLAN_RECOVERY.md` or equivalent top-of-`STATE.md` machine-generated summary

Role:

- one-screen crash recovery snapshot
- current objective
- active blockers
- active repo in scope
- last verified tool state
- last durable decisions promoted

This layer should be cheaper than reading the whole `STATE.md`.

## Recommended Preload Order

### PLAN

1. always-apply governance rules only
2. compact governance memory retrieval
3. compact active-project memory retrieval
4. recovery snapshot
5. `STATE.md` only if the snapshot is insufficient
6. `DECISIONS.md` / `PATTERNS.md` / `HANDOFF.md` on demand
7. ledger one block at a time only if canonical sources fail

### AGENT

1. PLAN prompt
2. active-project memory retrieval
3. recovery snapshot or latest `STATE.md` block
4. only the exact files needed for execution

### DEBUG

1. `thinking-patterns.debugging_approach`
2. recovery snapshot
3. relevant `STATE.md` evidence
4. smallest raw evidence slice needed

## Assets Still Needed

1. A compact recovery snapshot surface for PLAN
2. A thin local memory wrapper or adapter that exposes true project and namespace scoping on top of the current flat OpenMemory Cursor tool surface
3. A live-tested Obsidian bridge after transport correction
4. A live-tested ledger hook in a real Cursor edit path
5. A real OpenClaw <-> OpenMemory promotion bridge
6. Optional Cursor hook usage beyond `afterFileEdit`, especially `postToolUse`, for compact tool-result promotion and audit injection

## Immediate Implementation Order

1. Repair and verify the Obsidian MCP bridge
2. Write this audit into `STATE.md`
3. Split heavy always-apply memory instructions into lean bootstrap policy vs deeper execution policy
4. Add the compact recovery snapshot layer
5. Add a scoped memory wrapper strategy for OpenMemory
6. Only then design the full no-loss promotion and compaction workflow

## Bottom Line

The tri-workspace already has enough pieces to build a low-bloat lossless-style system, but not enough to honestly call it lossless today.

The biggest current blockers are:

- broken Obsidian MCP wiring
- overstated OpenMemory scoping assumptions
- unproven hook and bridge behavior
- always-apply rule bloat
- secret drift in the live global MCP config
