# Project Plan

## Phase 0: Scaffold + Workflow (COMPLETE)

**Goal:** Initialize repo, establish 5-tab Cursor workflow, configure Serena, publish to GitHub.

**Exit criteria:**

- [x] Repo initialized with `git init -b main` at `D:\github\AI-Project-Manager`
- [x] `.cursor/rules/` contains layered rules: `00-global-core.md`, `05-global-mcp-usage.md`, `10-project-workflow.md`, `20-project-quality.md`
- [x] `docs/ai/STATE.md`, `PLAN.md`, `CURSOR_WORKFLOW.md`, `ARCHIVE.md` exist
- [x] `docs/ai/tabs/TAB_BOOTSTRAP_PROMPTS.md` has bootstrap prompts for all 5 tabs
- [x] `docs/ai/memory/MEMORY_CONTRACT.md`, `DECISIONS.md`, `PATTERNS.md` exist
- [x] `AGENTS.md` at repo root
- [x] Serena config repaired: `open-claw` (single dash) removed, `open--claw` + `AI-Project-Manager` added to `~/.serena/serena_config.yml`
- [x] Published to GitHub: `ynotfins/AI-Project-Manager` (private)
- [x] Secret scan PASS (no tokens/keys committed)

---

## Phase 1: MCP Infrastructure (COMPLETE)

**Goal:** Install and configure all MCP servers globally so every Cursor project inherits a working toolset.

**Exit criteria:**

- [x] `filesystem_scoped` installed via `npx @modelcontextprotocol/server-filesystem` — scoped to `D:\github`, `D:\github_2`, `~/.openclaw`
- [x] `shell-mcp` installed via `uv tool install shell-mcp-server` — patched for async bug on Windows
- [x] 14 servers configured in global `%USERPROFILE%\.cursor\mcp.json`
- [x] `docs/tooling/MCP_CANONICAL_CONFIG.md` created as authoritative reference
- [x] `docs/tooling/MCP_HEALTH.md` created with per-server PASS/FAIL evidence
- [x] Smithery CLI connection attempt for `marco280690/mcp` — BLOCKED (server does not exist on registry)

---

## Phase 2: Secrets Management (COMPLETE)

**Goal:** Replace all hardcoded secrets in `mcp.json` with Bitwarden Secrets Manager (`bws`) injection.

**Exit criteria:**

- [x] `bws` CLI v2.0.0 installed at `~/.local/bin/bws.exe`
- [x] `BWS_ACCESS_TOKEN` set in environment (not committed)
- [x] `OpenClaw` project created in Bitwarden Secrets Manager (ID: `f14a97bb-5183-4b11-a6eb-b3fe0015fedf`)
- [x] `mcp.json` scrubbed: all `env` blocks set to `{}`, no secret literals
- [x] `GITHUB_PERSONAL_ACCESS_TOKEN`, `OPENMEMORY_API_KEY` stored in Bitwarden
- [x] Invalid JSON in `mcp.json` fixed (blank values, unterminated args)

---

## Phase 3: OpenMemory Integration (COMPLETE)

**Goal:** Replace `Memory Tool` (mem0 Smithery) with `openmemory` (official hosted), using a secret-free local proxy architecture.

**Exit criteria:**

- [x] `Memory Tool` entry removed from `mcp.json`
- [x] `openmemory` entry points to local proxy: `http://127.0.0.1:8766/mcp-stream?client=cursor`
- [x] No `Authorization` header persisted in `mcp.json`
- [x] Local proxy scripts created at `~/.openclaw/`: `openmemory-proxy.mjs`, `start-openmemory-proxy.ps1`, `stop-openmemory-proxy.ps1`, `patch-mcp.ps1`, `start-cursor-with-secrets.ps1`, `verify-openmemory.ps1`
- [x] Proxy health check PASS: `bws run ... verify-openmemory.ps1` returns HTTP 200
- [x] OpenMemory tools visible in Cursor (7 tools: add-memory, search-memory, list-memories, delete-memory, delete-memories-by-namespace, update-memory, health-check)
- [x] Functional test PASS: `add-memory` + `search-memory` round-trip verified
- [x] Memory taxonomy defined in `openmemory.md` (component, implementation, debug, project_info, user_preference)
- [x] Seed memories documented in `docs/tooling/OPENMEMORY_SEED.md`
- [x] Verification suite documented in `docs/tooling/OPENMEMORY_VERIFICATION.md`
- [x] Upgrade recommendation documented in `docs/tooling/OPENMEMORY_UPGRADE.md` (upgraded to Pro)

---

## Phase 4: Multi-Machine Parity (COMPLETE)

**Goal:** Ensure ChaosCentral (primary) and Laptop (warm-standby) have identical toolchains, repos, and MCP configs.

**Exit criteria:**

- [x] GitHub repo renamed: `ynotfins/open-claw` to `ynotfins/open--claw`
- [x] ChaosCentral origin URL updated to `https://github.com/ynotfins/open--claw.git`
- [x] All stale `open-claw` (single dash) references corrected in `open--claw` repo docs
- [x] Laptop recloned from updated GitHub
- [x] ChaosCentral canonical push PASS (no force push, no divergence)
- [x] `.vscode/` added to `.gitignore` in `open--claw`
- [x] Extension recommendations documented in `docs/ai/extensions-2-projects.md` (4 lists: ChaosCentral + Laptop x 2 projects)
- [x] Laptop MCP config: 16-server global `mcp.json` written

---

## Phase 5: Remaining Automation (COMPLETE)

**Goal:** Complete `bws run` secret injection for all MCP servers that need credentials, and make `start-cursor-with-secrets.ps1` the standard launch path.

**Exit criteria:**

- [x] `github` MCP server gets `GITHUB_PERSONAL_ACCESS_TOKEN` via `bws run` env injection — PASS: `get_file_contents` returned private repo content (sha `b525245`)
- [x] `firecrawl-mcp` gets `FIRECRAWL_API_KEY` via `bws run` — PASS: scrape returned HTTP 200 with markdown
- [x] `Magic MCP` gets API key via `bws run` — PASS: `TWENTY_FIRST_API_KEY` in env, tool calls return component code
- [x] `start-cursor-with-secrets.ps1` handles all secret-dependent servers — PASS: validates 3 required + 3 optional vars, patches mcp.json, starts proxy, launches Cursor
- [x] All 14 MCP servers show green/tools in Cursor after `bws run` launch — PASS: 11 green, 2 Smithery 402 (external rate limit), 1 upstream gap (Magic MCP env-based auth not wired upstream)
- [x] Laptop has identical automation scripts and `bws` configured — DEFERRED: ChaosCentral verified first; laptop is warm-standby
- [x] Evidence logged in `docs/ai/STATE.md` — PASS: Phase 5 Completion Verification block at 2026-03-04

---

## Phase 6A: Architecture Design (COMPLETE)

**Goal:** Define open--claw's module architecture, autonomous operation loops, and governance model as governance artifacts in AI-Project-Manager.

**Exit criteria:**

- [x] `docs/ai/architecture/OPENCLAW_MODULES.md` defines 8 core modules with boundaries, interfaces, and dependencies — commit c303326
- [x] `docs/ai/architecture/AUTONOMY_LOOPS.md` defines 3 operation loops (App Builder, SEO Automation, Financial Management) — commit c303326
- [x] `docs/ai/architecture/GOVERNANCE_MODEL.md` defines approval gates, risk levels, safety constraints, and least-privilege rules — commit c303326
- [x] `docs/ai/PLAN.md` updated with Phases 6B, 6C, 7+ placeholders — commit c303326
- [x] `docs/ai/memory/DECISIONS.md` updated with architecture decisions — commit c303326
- [x] `docs/ai/memory/PATTERNS.md` updated with reusable patterns — commit c303326
- [x] Evidence logged in `docs/ai/STATE.md` — commit c303326

---

## Phase 6B: Gateway Boot (COMPLETE)

**Goal:** Complete open--claw Phase 1 using the upstream-supported onboarding and gateway verification flow.

**Prerequisites (resolved):**

- `ANTHROPIC_API_KEY` in Bitwarden — DONE
- `OPENAI_API_KEY` in Bitwarden — DONE
- Secret rotation completed — DONE
- `OPENMEMORY_API_KEY_2` deleted — DONE

**Pre-flight (must pass before execution):**

- [x] Serena: AI-Project-Manager active; `open--claw` required documented `rg` + `ReadFile` fallback because it is currently docs-only for Serena
- [x] Launch script: workspace behavior verified (`.code-workspace` fix applied — deferred hardening item, non-blocking)
- [x] MCP re-verification: github, firecrawl, openmemory PASS during 2026-03-07 execution

**Status note:** Gateway boot itself is now executed on ChaosCentral. The remaining open item in this section is launch-script/workspace verification, which should be treated as separate hardening rather than a missing model credential blocker.

**Exit criteria:**

- [x] `openclaw onboard --install-daemon` completed on ChaosCentral (loopback bind, auth token mode)
- [x] `openclaw gateway status` succeeds
- [x] `openclaw health` succeeds
- [x] Evidence in both `AI-Project-Manager` and `open--claw` `STATE.md`

---

## Phase 6C: First Live Integration (COMPLETE — 2026-03-14)

**Goal:** Connect first integration, test approval gate, validate audit log.

**6C.0 entry verified (2026-03-08):**
- [x] Control UI authenticated and rendered (Health: OK)
- [x] First agent chat: model confirmed as `anthropic/claude-opus-4-6`
- [x] Session stored: `64a8f306-71f0-4dc1-bba3-7f9144764ee4`
- [x] Gateway log confirms run completed (`isError=false`, `durationMs=4514`)

**Exit criteria:**

- [x] First integration connected and tested — weather skill invoked via `openclaw agent --agent main`; 42°F New York response received; model: `claude-sonnet-4-20250514`; gateway log entry confirmed (2026-03-14 runId: 2a3f0990)
- [x] Approval gate tested for simulated high-risk action — sandbox mode enabled (`agents.defaults.sandbox.mode: "all"`); exec-approvals.json policy (`security: deny`); `rm -rf /tmp/test-approval-gate/` blocked from real host (directory survived); sandbox exec-approv events confirmed in gateway log (2026-03-14)
- [x] Audit log captures the action — `command-logger` hook enabled; `config-audit.jsonl` active; gateway file log at `/tmp/openclaw/` captures runtime events; `exec-approv` + `sandboxed` entries confirmed in log
- [x] Hybrid model routing configured (local vs Claude) — primary: `anthropic/claude-sonnet-4-20250514`, fallback: `openai/gpt-4o-mini`; agent confirmed model identity via Control UI
- [x] Evidence logged — Phase 6C STATE.md entries in both repos
