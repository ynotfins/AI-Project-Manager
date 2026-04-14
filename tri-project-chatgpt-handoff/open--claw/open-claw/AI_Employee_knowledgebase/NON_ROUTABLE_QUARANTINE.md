# NON-ROUTABLE QUARANTINE REGISTRY

## Status: CANONICAL — This file is the authoritative quarantine list for the entire tri-workspace.

> **Authority**: This registry is subordinate only to `FINAL_OUTPUT_PRODUCT.md`. It governs search, routing, memory, and embeddings exclusions across all three repos: `AI-Project-Manager`, `open--claw`, and `droidrun`. Mirror repos enforce the same behavior but defer to this file as the canonical source of truth.

---

## Hard Rule

Quarantined paths listed in this file **must not** be:

- read by any agent for task design, planning, or implementation
- referenced, cited, or summarized in any agent response
- routed through any routing or orchestration layer
- searched as part of normal repo search operations
- stored to or recalled from any memory tool (OpenMemory, vector store, embeddings)
- used as context material for embeddings or semantic search
- promoted to live runtime use without explicit removal from this registry

The only permitted interaction with quarantined material is **maintenance of the quarantine itself** (e.g., updating this file, adding banners, extending the registry).

---

## Quarantined Paths

### open--claw repo

| Path | Reason | Banner Applied |
|------|---------|----------------|
| `open-claw/AI_Employee_knowledgebase/candidate_employees/**` | Imported upstream role library — not curated, not production-ready, not aligned to `FINAL_OUTPUT_PRODUCT.md` standards; 2,608 raw role packets awaiting promotion gating | Yes — `<!-- NON-ROUTABLE — OUT OF SCOPE -->` prepended to all 2,608 text files |

### droidrun repo

| Path | Reason | Banner Applied |
|------|---------|----------------|
| `src/droidrun/tools/driver/ios.py` | iOS implementation — out of scope for Android-only actuator layer; incomplete and not connected to any live runtime | Yes — `# NON-ROUTABLE — OUT OF SCOPE` prepended |
| `src/droidrun/tools/ui/ios_provider.py` | iOS UI state provider — out of scope for Android-only actuator layer | Yes — `# NON-ROUTABLE — OUT OF SCOPE` prepended |
| `src/droidrun/tools/ios/**` | iOS tools module — entire directory out of scope for Android-only actuator layer | Yes — `# NON-ROUTABLE — OUT OF SCOPE` prepended to all files |

---

## Exclusion Definitions

### Search Exclusion

Normal agent search operations (Grep, Glob, ripgrep, file listing for task purposes) must not traverse quarantined paths. When a search is executed across a repo, quarantined directories and files must be treated as if they do not exist for the purpose of that search.

Explicit exclusion globs for search tools:
```
open-claw/AI_Employee_knowledgebase/candidate_employees/**
src/droidrun/tools/driver/ios.py
src/droidrun/tools/ui/ios_provider.py
src/droidrun/tools/ios/**
```

### Memory Exclusion

Memory tools (OpenMemory MCP, any vector store, any embedding pipeline) must not ingest, store, index, or recall content from quarantined paths.

- `add-memory` calls must not include content sourced from quarantined files.
- `search-memory` results that surface quarantined content must be discarded and not acted upon.
- Embeddings pipelines must exclude quarantined paths from their ingestion scope.
- No namespace, project_id, or user_preference entry may be created from quarantined content.

### Embeddings Exclusion

Quarantined files are excluded context material. They must not be included in:
- any semantic similarity index built from this repo
- any context window assembled for agent reasoning
- any retrieval-augmented generation corpus

If an embeddings or semantic search system is configured for any of the three repos, quarantined paths must be added to its exclusion list before the first index run.

### Routing Exclusion

No routing rule, agent dispatch, skill loader, or orchestration layer may route a task to or through quarantined files. Quarantined paths must not appear as targets in any routing configuration.

---

## Promotion Gate

A quarantined path may only be removed from this registry (and thus become routable again) when **all** of the following conditions are met:

1. Tony explicitly approves the promotion in a session.
2. The file or directory has been updated to meet the `AI-EMPLOYEE-STANDARD.md` quality bar.
3. The `CHECKLIST.md` and `AUDIT.md` for any candidate employee packet have been completed.
4. The promotion is recorded in this file with a date and rationale.
5. The `NON-ROUTABLE — OUT OF SCOPE` banner is removed from the promoted files.

No agent may self-approve a promotion. This gate is reserved for Tony.

---

## Mirror Repos

The quarantine behavior defined here is mirrored (enforcement only, not registry) in:

- `AI-Project-Manager/.cursor/rules/02-non-routable-exclusions.md`
- `open--claw/.cursor/rules/02-non-routable-exclusions.md`
- `droidrun/.cursor/rules/02-non-routable-exclusions.md`

If the mirror rules conflict with this file, this file wins.

---

## Audit Trail

| Date | Action | Actor | Detail |
|------|--------|-------|--------|
| 2026-04-01 | Initial quarantine established | AGENT (Executioner) | 2,608 `candidate_employees` files bannered; 3 droidrun iOS files bannered; registry created; rule files created in all 3 repos |
