# Agent Handoff — AI-Project-Manager

**Date**: 2026-03-08
**Handing off after**: Phase 6C.0 (gateway liveness verified, first agent chat confirmed, Phase 6B closed)
**Next action**: Phase 6C — First Live Integration (connect first integration, test approval gate, validate audit log)

---

## 1. What This Project Is

**AI-Project-Manager** is the governance repo for the Open Claw platform. It tracks phases, architecture decisions, execution state, and cross-repo coordination. It does **not** contain application code — that lives in `open--claw`.

The two repos form one coordinated system:

| Repo | Role | Contains |
|------|------|----------|
| `AI-Project-Manager` | Governance | Phases, state logs, architecture docs, workflow rules, memory, tab prompts |
| `open--claw` | Execution | Project docs, skill stubs, configs, vendored OpenClaw runtime (`vendor/openclaw/`) |

Both repos share a five-tab Cursor workflow: PLAN / AGENT / DEBUG / ASK / ARCHIVE.

---

## 2. Current State at Handoff

### Git History

```
9a7e58b  phase: close 6B, begin 6C.0 - first agent chat verified  ← HEAD
a229a33  governance: add PLAN repo-truth-first source priority rule
0c49da8  governance: add Host Restart Verification pattern + dense STATE entry
662be3f  governance: add HH:MM to STATE template + record canonical source decisions
68d13b5  state: Phase 6B.2 entry (first HH:MM-format)
```

### Phase Status

| Phase | Status |
|-------|--------|
| Phase 0 — Scaffold + Workflow | COMPLETE |
| Phase 1 — MCP Infrastructure | COMPLETE (14 servers) |
| Phase 2 — Secrets Management | COMPLETE (Bitwarden `bws`) |
| Phase 3 — OpenMemory Integration | COMPLETE (local proxy architecture) |
| Phase 4 — Multi-Machine Parity | COMPLETE (ChaosCentral + Laptop) |
| Phase 5 — Remaining Automation | COMPLETE (`bws run` injection for all) |
| Phase 6A — Architecture Design | COMPLETE (modules, loops, governance) |
| Phase 6B — Gateway Boot | **COMPLETE** |
| Phase 6C — First Live Integration | **OPEN** (6C.0 entry verified — first agent chat confirmed) |

### Cross-Repo State (open--claw)

| Phase | Status |
|-------|--------|
| Phase 0 — Project Kickoff | COMPLETE |
| Phase 1 — Gateway Boot + Integration Scaffold | **COMPLETE** |
| Phase 2 — First Live Integration | **OPEN** (not started) |

### WSL Environment (ChaosCentral)

- `fnm` auto-switch disabled in `~/.bashrc` (lines 125-128 fully commented out)
- Node v22.22.0 managed via `nvm` (auto-loads in interactive shells after PATH clobber fix)
- pnpm 10.23.0 pinned via `corepack`
- Gateway running: `127.0.0.1:18789`, loopback, token auth, pid 366 (as of 2026-03-08)
- Session `64a8f306-71f0-4dc1-bba3-7f9144764ee4` created by first agent chat
- Model confirmed: `anthropic/claude-opus-4-6`

### Unverified

- `loginctl enable-linger ynotf` status (determines if gateway survives user-session logout)
- `openclaw doctor --repair` nvm/systemd warning (deferred stabilization item)
- Full cold-reboot terminal window nvm auto-load (tested via `bash -ic`, not fresh boot window)

---

## 3. Repo Structure

```
D:\github\AI-Project-Manager\
├── .cursor/rules/
│   ├── 00-global-core.md               ← non-negotiable behaviors
│   ├── 05-global-mcp-usage.md          ← MCP tool usage policy
│   ├── 10-project-workflow.md          ← tab contracts, STATE template
│   └── 20-project-quality.md           ← engineering standards
├── AGENTS.md                            ← agent operating contract (start here)
├── docs/
│   ├── ai/
│   │   ├── STATE.md                     ← primary operational log
│   │   ├── PLAN.md                      ← active plan with phases
│   │   ├── HANDOFF.md                   ← this file
│   │   ├── ARCHIVE.md                   ← compressed past decisions
│   │   ├── CURSOR_WORKFLOW.md           ← human-readable workflow overview
│   │   ├── extensions-2-projects.md     ← VS Code extension lists
│   │   ├── architecture/
│   │   │   ├── AUTONOMY_LOOPS.md        ← 3 operation loops
│   │   │   ├── CODEBASE_ORIENTATION.md  ← codebase map
│   │   │   ├── GOVERNANCE_MODEL.md      ← approval gates, risk levels
│   │   │   └── OPENCLAW_MODULES.md      ← 8 core modules
│   │   ├── context/
│   │   │   └── session-2026-03-06-phase6b.md
│   │   ├── memory/
│   │   │   ├── DECISIONS.md
│   │   │   ├── MEMORY_CONTRACT.md
│   │   │   └── PATTERNS.md
│   │   └── tabs/
│   │       └── TAB_BOOTSTRAP_PROMPTS.md ← bootstrap prompts for all 5 tabs
│   ├── global-rules.md
│   └── tooling/                         ← MCP config, health, verification docs
└── .gitignore
```

---

## 4. Key Technical Facts

### Two-Repo System

- **AI-Project-Manager** (governance): phases, state, architecture, decisions. AGENT updates `docs/ai/STATE.md` here after every execution block.
- **open--claw** (execution): project docs, skill stubs, configs, vendored OpenClaw. STATE.md is mirrored here for cross-repo traceability.

### MCP Infrastructure

- 14 servers configured globally in `%USERPROFILE%\.cursor\mcp.json`
- Secret injection via `bws run` (Bitwarden Secrets Manager CLI)
- OpenMemory runs through a local proxy at `http://127.0.0.1:8766/mcp-stream?client=cursor`
- Launch script: `~/.openclaw/start-cursor-with-secrets.ps1` patches `mcp.json`, starts proxy, launches Cursor

### WSL Environment (ChaosCentral)

- **Distro**: Ubuntu 24.04.3 LTS
- **Node**: v22.22.0 via nvm (`/home/ynotf/.nvm/`)
- **pnpm**: 10.23.0 pinned via `corepack prepare pnpm@10.23.0 --activate`
- **Build location**: `~/openclaw-build/` (ext4 native FS, NOT `/mnt/d/`)
- **fnm**: disabled — `~/.bashrc` lines 125-128 fully commented out (conflicts with nvm PATH resets)

### Gateway Token Workflow

The gateway auth token lives in `~/.openclaw/openclaw.json` under `gateway.auth.token`.

Three retrieval methods:
```bash
# 1. Raw token
source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw config get gateway.auth.token

# 2. Tokenized dashboard URL (preferred — authenticates browser automatically)
source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw dashboard --no-open

# 3. Regenerate if missing
source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw doctor --generate-gateway-token
```

`node openclaw.mjs gateway token` is NOT a valid command — it errors with "too many arguments."

### Security Decisions (non-negotiable)

- WhatsApp: official Business Cloud API only (Baileys disabled)
- All outbound sends: approval-gated (email, SMS, WhatsApp, calendar events)
- Gateway: loopback bind + token auth always
- No secrets in repo, ever
- `~/.openclaw/.env` is the only valid secrets location
- Sandbox mode: `non-main` by default

### Git Identity (local to repos)

```
user.name  = ynotf
user.email = ynotf@users.noreply.github.com
```

---

## 5. Blocked Items

| Priority | Item | What's Needed | Status |
|----------|------|---------------|--------|
| **6C** | First live integration | Integration credential (Google Cloud is highest leverage) | OPEN |
| **P1** | Google Cloud (#2, #6, #7) | One project covers Gmail + Calendar + Contacts | BLOCKED |
| **P1** | Cost Caps (#8) | Needs baseline usage from running gateway | BLOCKED |
| **P2** | Domain Email (#3) | IMAP/SMTP credentials | BLOCKED |
| **P2** | Twilio SMS (#4) | Account + phone number | BLOCKED |
| **P3** | WhatsApp Business (#5) | Meta verification (1-2 weeks) | BLOCKED |

Full details in `open--claw/open-claw/docs/BLOCKED_ITEMS.md`.

---

## 6. MCP Tool Status

| Tool | Status | Notes |
|------|--------|-------|
| serena | PASS | AI-Project-Manager active. `open--claw` returns "No source files found" — use `rg` + file reads as fallback |
| Context7 | PASS | Library ID `/openclaw/openclaw` (4730 snippets) |
| GitHub MCP | PASS | Private repo access verified |
| firecrawl-mcp | PASS | Scrape returns HTTP 200 |
| openmemory | PASS | 7 tools, add/search round-trip verified. Requires `user_preference=true` or `project_id` |
| playwright | PASS | Used for Phase 6C.0 Control UI screenshot + first agent chat |
| sequential-thinking | PASS | Available |
| Exa Search | PASS | Available |
| filesystem_scoped | PASS | Scoped to `D:\github`, `D:\github_2`, `~/.openclaw` |
| shell-mcp | PASS | Patched for Windows async bug |

---

## 7. What the Next Agent Must Do

### Phase 6C — First Live Integration

Phase 6C.0 is verified (gateway healthy, first agent chat confirmed). Remaining:

1. Obtain an integration credential (Google Cloud is highest-leverage — covers Gmail, Calendar, Contacts)
2. Connect the integration via the Control UI or `openclaw configure`
3. Test the approval gate (one outbound action blocked until human approves)
4. Verify audit log captures the full action chain
5. Configure hybrid model routing (local vs Claude) if not auto-routing
6. Log evidence in `docs/ai/STATE.md`

See `docs/ai/PLAN.md` Phase 6C exit criteria for full checklist.

---

## 8. Conventions the Next Agent Must Follow

1. **All WSL commands** prefixed with `source /home/ynotf/.nvm/nvm.sh` (or `source ~/.nvm/nvm.sh`)
2. **Build always in `~/openclaw-build/`** — never `/mnt/d/` for pnpm operations (NTFS causes EACCES)
3. **Update `docs/ai/STATE.md`** after each execution block with PASS/FAIL evidence
4. **Mirror STATE.md** to `open--claw/docs/ai/STATE.md` for cross-repo changes
5. **Secret scan** before every commit: `grep -rPn "(sk-[a-zA-Z0-9]{20,}|ghp_|AIza|AKIA)" ...`
6. **MCP-first**: use serena, Context7, Exa before falling back to manual file reads
7. **No secrets in repo, ever** — `~/.openclaw/.env` is the only valid secrets location
8. **Approval gates**: never implement an outbound action without a gate in the design
9. **Modular architecture**: separate ui, domain, data, utils — no >20 line monolith blocks in Activities

---

## 9. Files to Read First (Recommended Order)

1. `AGENTS.md` — operating contract
2. `.cursor/rules/00-global-core.md` — non-negotiable behaviors
3. `docs/ai/STATE.md` — full execution log (primary source of truth)
4. `docs/ai/PLAN.md` — what's planned
5. `docs/ai/architecture/GOVERNANCE_MODEL.md` — approval gates, risk levels
6. `docs/ai/architecture/OPENCLAW_MODULES.md` — 8 core modules
7. `docs/ai/memory/DECISIONS.md` — key decisions with rationale

For `open--claw` context:
1. `open-claw/docs/BLOCKED_ITEMS.md` — current unblock steps
2. `open-claw/docs/SETUP_NOTES.md` — local wrapper runtime/setup guidance
3. `open-claw/docs/ARCHITECTURE_MAP.md` — OpenClaw hub-and-spoke architecture

---

## 10. Restart Checklist (Run After Every Cursor Restart)

```bash
# 1. Verify WSL path
wsl bash -c 'test -d /mnt/d/github/open--claw && echo PASS || echo FAIL'

# 2. Verify node + pnpm (nvm must be sourced)
wsl bash -c 'source /home/ynotf/.nvm/nvm.sh && node --version && pnpm --version'
# Expected: v22.22.0 / 10.23.0

# 3. Re-pin pnpm if version drifted
wsl bash -c 'source /home/ynotf/.nvm/nvm.sh && corepack prepare pnpm@10.23.0 --activate'

# 4. Verify git status
git -C D:/github/AI-Project-Manager status --short
git -C D:/github/open--claw status --short
git -C D:/github/AI-Project-Manager log --oneline -3
git -C D:/github/open--claw log --oneline -3
```

**MCP tools to verify:**

| Tool | Minimal test |
|------|-------------|
| serena | `activate_project AI-Project-Manager` |
| Context7 | `resolve-library-id` query for `openclaw` |
| openmemory | `health-check` call |
| GitHub MCP | `search_repositories` for `ynotfins` |
| firecrawl | `firecrawl_scrape` against any public URL |

---

## 11. Known Gotchas

| Gotcha | Solution |
|--------|----------|
| `node: command not found` in WSL | `source /home/ynotf/.nvm/nvm.sh` first |
| `Command 'fnm' not found` in WSL | Already fixed — lines 125-128 of `~/.bashrc` commented out. If it returns, re-comment the `eval "$(fnm env --use-on-cd)"` line |
| `EACCES rename` on pnpm install | Build in `~/openclaw-build/`, never `/mnt/d/` |
| `node openclaw.mjs gateway token` fails | Not a valid command. Use `pnpm openclaw config get gateway.auth.token` |
| serena fails to activate `open--claw` | Returns "No source files found". Use `rg` + targeted `ReadFile` as fallback |
| `openclaw onboard` hangs | Use `--non-interactive --accept-risk` flags |
| openmemory search returns -32602 | Must provide `user_preference=true` or `project_id` |
| `~/.bashrc` empty `if/then/fi` body | Bash requires at least one command between `then` and `fi`; a comment alone is a syntax error. Comment out the entire `if/fi` structure |
| Dashboard URL path | Root `/` (not `/openclaw`). Use `pnpm openclaw dashboard --no-open` for the correct tokenized URL |
| WhatsApp Baileys temptation | Built-in and easy, but decision is: official API only |
