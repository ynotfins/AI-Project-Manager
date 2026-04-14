## OpenMemory + Mem0 Upgrade Decision (2026-03-02)

### What each product is doing for us

- **OpenMemory (hosted MCP)**: developer/agent memory used by Cursor across projects (tools like `add-memory`, `search-memory`).
- **Mem0 Platform (Starter)**: application/runtime memory APIs (when OpenClaw itself needs memory in production code).

### OpenMemory plan decision (Hobby → Pro?)

From `openmemory.dev` pricing:

- **Hobby**: 1,000 retrievals/month
- **Pro**: 5,000 retrievals/month + **Unlimited Projects**

Recommendation:

- **Upgrade to OpenMemory Pro** if either is true:
  - you routinely use Cursor across multiple repos and expect >1,000 memory retrievals/month, or
  - you want **Unlimited Projects** to avoid per-project constraints as you add governed repos.
- Stay on **Hobby** if:
  - you’re experimenting and can keep retrievals under 1,000/month (and you’re okay with any project-count limits).

Given your workflow (multiple governed repos + heavy agent usage), **Pro is the safer default** to avoid throttling and to remove project-count friction.

### Mem0 Platform plan decision (Starter → Pro?)

From `mem0.ai/pricing` (Starter):

- 50,000 memories storage
- 5,000 retrieval API calls/month
- Unlimited end users

Recommendation:

- Keep **Mem0 Starter** until OpenClaw’s runtime actually uses Mem0 APIs in production and you observe sustained retrieval volume near 5,000/month.
- Upgrade Mem0 only when app-level usage justifies it; OpenMemory MCP usage does not necessarily imply Mem0 Platform overage.

