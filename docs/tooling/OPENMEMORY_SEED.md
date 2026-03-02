## OpenMemory Seed Pack (governed)

Purpose: bootstrap high-signal, durable memory for governed Cursor workflows **without storing secrets**.

This is designed for the OpenMemory MCP tools visible in Cursor (e.g., `add-memory`, `search-memory`).

### Conventions

- **project_id**:
  - `ynotfins/AI-Project-Manager`
  - `ynotfins/open--claw`
- **namespaces**:
  - `global`, `AI-Project-Manager`, `open--claw`
- **memory_types** (metadata): `component | implementation | debug | project_info | user_preference`
- **No secrets**: do not store tokens, env values, credentials, or URLs containing secrets.

---

## Seed memories (copy/paste as individual `add-memory` calls)

### 1) Global preference — governance gates

- **title**: `Global - Governance gates (PASS/FAIL evidence)`
- **content**: `Use deterministic phase gates (PASS/FAIL/BLOCKED) with command/tool evidence; never silently continue on degraded tools. Update docs/ai/STATE.md after each execution block.`
- **metadata**: `{ "memory_types": ["user_preference"], "namespace": "global" }`
- **scope**: `user_preference=true`

### 2) Global preference — secrets policy

- **title**: `Global - No secrets in repos or mcp.json`
- **content**: `Never store secrets in git, source, or Cursor mcp.json. Inject at runtime via Bitwarden Secrets Manager (bws run). Never print secret values; only prove presence without echoing.`
- **metadata**: `{ "memory_types": ["user_preference"], "namespace": "global" }`
- **scope**: `user_preference=true`

### 3) AI-Project-Manager project info — OpenMemory auth architecture

- **title**: `AI-Project-Manager - OpenMemory auth via local proxy`
- **content**: `Cursor connects to OpenMemory through a local proxy at 127.0.0.1:8766 that injects Authorization from OPENMEMORY_API_KEY in the process environment. mcp.json stores no auth headers.`
- **metadata**: `{ "memory_types": ["project_info"], "namespace": "AI-Project-Manager" }`
- **scope**: `project_id="ynotfins/AI-Project-Manager"`

### 4) AI-Project-Manager component — local automation scripts

- **title**: `AI-Project-Manager - Local automation scripts (.openclaw)`
- **content**: `Local scripts (not in git): patch-mcp.ps1 (enforces secret-free mcp.json), start-cursor-with-secrets.ps1 (patches MCP, starts proxy, launches Cursor), openmemory-proxy.mjs (forwards to api.openmemory.dev).`
- **metadata**: `{ "memory_types": ["component"], "namespace": "AI-Project-Manager" }`
- **scope**: `project_id="ynotfins/AI-Project-Manager"`

### 5) open--claw project info — canonical identity

- **title**: `open--claw - Canonical repo identity`
- **content**: `Canonical naming: GitHub repo ynotfins/open--claw; local Windows path D:\\github\\open--claw; WSL path /mnt/d/github/open--claw. Avoid single-dash variants.`
- **metadata**: `{ "memory_types": ["project_info"], "namespace": "open--claw" }`
- **scope**: `project_id="ynotfins/open--claw"`

### 6) open--claw preference — build determinism

- **title**: `open--claw - Build determinism preference`
- **content**: `Prefer deterministic toolchain pinning and evidence logging over convenience. If a required tool is degraded, stop and surface restoration steps; do not proceed silently.`
- **metadata**: `{ "memory_types": ["user_preference"], "namespace": "open--claw" }`
- **scope**: `user_preference=true + project_id="ynotfins/open--claw"`

---

## Verification query (after seeding)

Run `search-memory` for:

- `governance gates PASS/FAIL evidence`
- `OpenMemory auth via local proxy`
- `Canonical repo identity open--claw`

Expected: at least 1 hit per query; if not, wait 2–4 seconds and retry (async ingestion).

