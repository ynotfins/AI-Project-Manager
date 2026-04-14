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
