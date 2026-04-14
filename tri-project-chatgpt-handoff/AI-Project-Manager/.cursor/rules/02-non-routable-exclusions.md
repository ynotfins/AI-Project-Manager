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
