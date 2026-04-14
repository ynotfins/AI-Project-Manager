# Obsidian Local REST MCP

This document records the local Obsidian MCP bridge configuration used by this machine.

## Current Choice

- Server name: `obsidian-vault`
- MCP package: `obsidian-mcp-server`
- Transport: stdio via `npx`
- Local API URL: `http://127.0.0.1:27123`
- Auth env var in Cursor process: `OBSIDIAN_API_KEY`
- Base URL env var in Cursor process: `OBSIDIAN_BASE_URL`
- SSL verification env var in Cursor process: `OBSIDIAN_VERIFY_SSL=false`
- Secret source: Bitwarden secret `OBSIDIAN_LOCAL_REST_API`
- Secret UUID: `ba4bd3ea-e910-49e3-9524-b427016b8365`
- Bitwarden project: `R3lentless-Grind-Global-Memory`

## Why This Bridge

- The installed Obsidian plugin is a REST API, not an MCP server.
- `obsidian-mcp-server` is the currently working Cursor bridge shape for the local REST plugin on this machine.
- The API key is not written into `mcp.json`; it is injected at launch time by `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`.

## Cursor MCP Shape

```json
{
  "obsidian-vault": {
    "command": "npx",
    "args": ["-y", "obsidian-mcp-server"],
    "env": {
      "OBSIDIAN_BASE_URL": "http://127.0.0.1:27123",
      "OBSIDIAN_VERIFY_SSL": "false"
    }
  }
}
```

The API key is inherited from the launcher environment as `OBSIDIAN_API_KEY`.

## Runtime Verification

Current evidence across the repair sequence:

- 2026-04-10: direct probe confirmed `http://127.0.0.1:27123` returned HTTP 200
- 2026-04-10: direct probe confirmed `https://127.0.0.1:27123` failed with an SSL wrong-version error
- 2026-04-10: `docs/obsidian/openapi.yaml` confirmed HTTP on `27123` and HTTPS on `27124`
- 2026-04-11: local bridge config was swapped to `obsidian-mcp-server` with `OBSIDIAN_BASE_URL=http://127.0.0.1:27123`
- 2026-04-12: an earlier live `obsidian-vault.obsidian_global_search` succeeded in a prior repaired Cursor session
- 2026-04-12: this current Cursor session returned `MCP server does not exist: user-obsidian-vault` and `MCP server does not exist: obsidian-vault` for targeted `obsidian_global_search` attempts

Current implication:

- the local Obsidian REST API is alive
- the prior HTTPS-on-27123 bridge setting was wrong
- the documented bridge shape remains the canonical config target
- this specific Cursor session does not currently have `obsidian-vault` registered, so targeted MCP use must be treated as degraded until Cursor reloads its MCP servers
- `obsidian-vault` should still be treated as a scoped sidecar note tool, not as canonical project state or default bootstrap context

## Restore Steps

1. Restart Cursor through `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`.
2. Re-run a targeted `obsidian_global_search` or note list/read call after reload.
3. If the server is still missing, verify the global `mcp.json` still points `obsidian-vault` to `npx -y obsidian-mcp-server` with `OBSIDIAN_BASE_URL=http://127.0.0.1:27123`.

## Operational Rules

**Memory System Relationship:**
- **OpenMemory** = primary durable structured memory backbone for agent decisions, patterns, project state
- **Obsidian** = fast-access scoped note memory sidecar for operator knowledge and personal context
- Obsidian is NOT repo truth, NOT a replacement for OpenMemory, NOT default bootstrap context

**Usage Guidelines:**
- Prefer targeted note reads/searches over broad vault dumps
- Use only when task explicitly needs operator knowledge or personal research findings
- Repo docs, code, and OpenMemory remain authoritative for project state
- Do NOT use Obsidian for agent operational decisions (use OpenMemory instead)
- Do NOT treat Obsidian notes as canonical over repo-tracked docs
- Do NOT use Obsidian as a replacement for `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, or `HANDOFF.md`

## Related Local Files

- `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`
- `C:\Users\ynotf\.openclaw\patch-mcp.ps1`
- `D:\github\AI-Project-Manager\docs\obsidian\openapi.yaml`
