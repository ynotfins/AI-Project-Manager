## OpenMemory Verification Suite (ChaosCentral + Laptop)

Goal: prove OpenMemory works **and** that we are not persisting auth secrets in `mcp.json`.

### Preconditions (non-negotiable)

- OpenMemory MCP is configured in `%USERPROFILE%\\.cursor\\mcp.json` with:
  - `openmemory.url` pointing to `http://127.0.0.1:8766/mcp-stream?client=cursor`
  - **no** `openmemory.headers.Authorization` present
- `OPENMEMORY_API_KEY` is injected at runtime (Bitwarden Secrets Manager via `bws run`).
- Local scripts exist under `C:\\Users\\<you>\\.openclaw\\` (not in git):
  - `patch-mcp.ps1`
  - `start-cursor-with-secrets.ps1`
  - `verify-openmemory.ps1`

---

## Test Steps (deterministic)

### 1) Secret-free config proof (mcp.json)

Run (with secrets injected, but do not print them):

```powershell
bws run --project-id <OPENCLAW_BWS_PROJECT_ID> -- pwsh -NoProfile -File "$HOME\\.openclaw\\verify-openmemory.ps1"
```

Expected output:

- `VERIFY_MCP_JSON_OK`
- `OPENMEMORY_PROXY_STARTED ...` (or `OPENMEMORY_PROXY_ALREADY_RUNNING ...`)
- `OPENMEMORY_PROXY_HEALTH_HTTP_200`
- `VERIFY_OPENMEMORY_OK`

PASS criteria:

- HTTP 200 from `http://127.0.0.1:8766/health`
- `mcp.json` has **no** persisted auth header for OpenMemory

### 2) Cursor tool visibility proof (UI)

In Cursor:

- Settings → Tools & MCP → `openmemory` should be **green**
- Tools should list the expected operations (example set from prior runs):\n
  - `health-check`\n
  - `add-memory`\n
  - `search-memory`\n
  - `list-memories`\n
  - `update-memory`\n
  - `delete-memory`\n
  - `delete-memories-by-namespace`

PASS criteria:

- Tool list is non-empty and matches expected core capabilities.

### 3) Functional tool test (async ingestion)

Using Cursor’s OpenMemory tools:

- Call `add-memory` with a **project_id** (`ynotfins/AI-Project-Manager`) and metadata `memory_types=["project_info"]`.
- Wait 2–4 seconds.
- Call `search-memory` with a query that should match the content.

PASS criteria:

- Search returns at least one hit with a non-zero score.

---

## Evidence logging (required)

After running the suite, append PASS/FAIL evidence to:

- `AI-Project-Manager/docs/ai/STATE.md`
- `AI-Project-Manager/docs/tooling/MCP_HEALTH.md`

