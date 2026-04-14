# Open Claw — Module Boundaries (responsibility-pure)

## Overview

Open Claw is organized into five modules. Each module has a single responsibility,
a defined interface, and explicit anti-responsibilities. Cross-module communication
goes through the orchestrator only.

---

## orchestrator

**Responsibility:** Route tasks, select tools, enforce rule compliance, output execution prompts.

| Inputs | Outputs |
|--------|---------|
| Natural-language instruction | Routed task to target module |
| Phase plan from PLAN tab | Execution prompt for AGENT |
| PASS/FAIL results from modules | Aggregated state update for `docs/ai/STATE.md` |

**Anti-responsibilities (must NOT do):**
- Must NOT perform codegen, testing, or repo operations directly
- Must NOT send communications or interact with external services
- Must NOT store or retrieve memory directly (delegates to memory module)
- Must NOT scrape or automate browsers

---

## memory

**Responsibility:** Manage local truth (repo docs) and cross-project recall (memory MCP tool).

| Inputs | Outputs |
|--------|---------|
| Store request (fact, decision, pattern) | Confirmation + deduplication check |
| Retrieve request (query) | Matching facts, decisions, or patterns |
| Conflict check (memory vs repo) | Resolution: repo docs win |

**Read/write policy:**
- Read: retrieve before every planning phase (see `docs/ai/memory/MEMORY_CONTRACT.md`)
- Write: store after every completed phase; one fact per entry; no secrets
- Conflict: if memory disagrees with repo docs, discard or update the memory entry

**Anti-responsibilities (must NOT do):**
- Must NOT store secrets, tokens, credentials, or personal data
- Must NOT execute code or run commands
- Must NOT make decisions (only stores and retrieves)

---

## dev

**Responsibility:** Code generation, testing, and repository operations.

| Inputs | Outputs |
|--------|---------|
| Execution prompt from orchestrator | Code changes, test results, build artifacts |
| Symbol/ref queries | Located symbols, references, call paths |
| Library API lookups | Verified API usage |

**Anti-responsibilities (must NOT do):**
- Must NOT send emails, messages, or notifications
- Must NOT automate browsers or scrape web pages
- Must NOT interact with spreadsheets, CRMs, or communication platforms
- Must NOT store memory (delegates to memory module via orchestrator)

---

## comms

**Responsibility:** Email, spreadsheets, CRM-style interactions via connectors with policy gates.

| Inputs | Outputs |
|--------|---------|
| Send request (message, data, destination) | Delivery confirmation + PASS/FAIL |
| Read request (inbox, sheet, channel) | Structured data from external source |
| Policy check (is this action allowed?) | Approved / denied with reason |

**Policy gates:**
- Every outbound action must be approved by the orchestrator before execution
- No bulk sends without explicit PLAN approval
- Credentials are never embedded; connector config lives outside the repo

**Anti-responsibilities (must NOT do):**
- Must NOT generate or modify code
- Must NOT automate browsers or scrape web pages
- Must NOT make architectural decisions

---

## web

**Responsibility:** Browser automation, scraping, and structured data extraction with verification discipline.

| Inputs | Outputs |
|--------|---------|
| URL + verification criteria | Screenshot, accessibility snapshot, PASS/FAIL |
| Extraction request (URL + schema) | Structured data matching schema |
| UI test scenario | Test result with evidence |

**Verification discipline:**
- Every browser action must produce observable evidence (screenshot, snapshot, or extracted data)
- Extraction results must be validated against the requested schema
- Failures must include the URL, action attempted, and error

**Anti-responsibilities (must NOT do):**
- Must NOT generate or modify code
- Must NOT send emails or messages
- Must NOT store credentials or login tokens in repo
- Must NOT make architectural decisions

---

## Boundary rules

- Modules do not import from each other directly.
- All cross-module communication goes through the orchestrator.
- Each module defines its own interface contract (this document).
- Violations of anti-responsibilities must be reported as FAIL in `docs/ai/STATE.md`.
