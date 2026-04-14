# Priority Tool Usage

This file tracks the health, purpose, and required-use discipline for the highest-value tools in the system.

## Priority Set

### 7 primary tools

| Tool | Primary role | Use when |
|---|---|---|
| `thinking-patterns` | structured reasoning | architecture, debugging, decomposition, decision framing |
| `Context7` | current external docs | libraries, frameworks, SDKs, APIs, CLIs |
| `serena` | exact-path code intelligence | symbol-aware code and config work |
| `Exa Search` | live web research | current ecosystem or public-web research |
| `playwright` | browser verification | frontend flows, UI checks, evidence |
| `firecrawl-mcp` | structured web extraction | crawl/map/scrape public docs or sites |
| `Magic MCP` | UI scaffolding | rapid interface generation and design starts |

### persistence backbone

| Tool | Primary role | Use when |
|---|---|---|
| `openmemory` | long-horizon memory | before planning, after durable decisions, during session recovery |

## Current Registration / Access State

| Tool | Status | Notes |
|---|---|---|
| `thinking-patterns` | CONFIGURED | new primary reasoning server; active tool mapping updated on 2026-04-10 |
| `Context7` | PASS | docs retrieved for `mem0` and `openmemory` on 2026-04-07 |
| `serena` | PASS | registered: `AI-Project-Manager`, `open--claw`, `open-claw-runtime`, `droidrun`, `alerts-sheets` |
| `Exa Search` | CONFIGURED | not exercised in this pass |
| `playwright` | CONFIGURED | not exercised in this pass |
| `firecrawl-mcp` | CONFIGURED | not exercised in this pass |
| `Magic MCP` | CONFIGURED | not exercised in this pass |
| `openmemory` | PASS | official `npx openmemory` stdio server is active; Cursor descriptors regenerated |

## Required Behavior

### PLAN

- Must identify `Required Tools`, `Optional Tools`, and `Safe to disable` in every AGENT prompt when task complexity justifies it.
- Must use OpenMemory retrieval before large file reads.
- Must use Context7 for external docs questions.

### AGENT

- Must use `thinking-patterns` for non-trivial planning, decomposition, debugging, or high-risk decisions instead of relying only on implicit reasoning.
- Must use Serena before raw search when the task is code or config inside a valid Serena project.
- Must use OpenMemory before planning and after durable results.
- Must record PASS/FAIL evidence for every tool used.

### DEBUG

- Must use `thinking-patterns.debugging_approach` for complex diagnosis.
- Must prefer targeted evidence retrieval over broad document loading.

## Serena Registration Map

| Serena project | Path | Purpose |
|---|---|---|
| `AI-Project-Manager` | `D:/github/AI-Project-Manager` | workflow/process/governance code and config |
| `open--claw` | `D:/github/open--claw` | repo-root docs/governance layer |
| `open-claw-runtime` | `D:/github/open--claw/open-claw` | runtime and employee package code |
| `droidrun` | `D:/github/droidrun` | actuator/mobile code |

Rule:

- on first access to a codebase, activate Serena by exact path
- if the project is missing, activating by path must register it
- repo root and runtime subproject are distinct when both exist

## Launch Integrity Rule

Cursor must be launched through the canonical Bitwarden wrapper so tool auth and runtime permissions exist in the Cursor process tree:

```powershell
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command "bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File \"$HOME\.openclaw\start-cursor-with-secrets.ps1\""
```

If Cursor is restarted outside this wrapper, Sparky may lose access to:

- OpenMemory auth
- GitHub MCP auth
- Firecrawl auth
- Magic auth
- OpenClaw gateway env
- DroidRun injected keys

## Change Log

### 2026-04-07

- Migrated primary reasoning policy from `Clear Thought 1.5` to `thinking-patterns`
- Verified `Context7` docs retrieval for `mem0` and `openmemory`
- Verified `openmemory` add/search with namespace isolation
- Registered `droidrun` in Serena
- Normalized `open--claw` Serena repo-root project config
- Confirmed Bitwarden Machine Account access to 32 secrets

### 2026-04-08

- Confirmed `openmemory` local proxy is alive via `/healthz`
- Confirmed upstream `api.openmemory.dev` MCP/health path is intermittently returning `504`
- Confirmed Cursor `user-openmemory` metadata currently lacks a `tools/` directory, which explains green/no-tools behavior
- Copied 18 post-restart screenshots into `docs/screenshots/2026-04-08-post-restart/`

### 2026-04-09

- Replaced the old local-proxy `mcp-stream` transport with the official `npx openmemory` stdio server
- Verified `VERIFY_OPENMEMORY_OK` after restart
- Confirmed Cursor regenerated `user-openmemory/tools/`
- Kept `/health` as a noisy signal only, not the sole availability test

### 2026-04-10

- Launcher hardening complete: node.cmd token injection from WSL openclaw.json, OpenMemory messaging updated to stdio server, startup warning classification documented
- Validated launcher flow: token extraction (48 chars), node.cmd template, warning classification, OpenMemory messaging, gateway health - all PASS
