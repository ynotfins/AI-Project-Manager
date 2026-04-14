# Session Bootstrap SOP

Standard operating procedure for bootstrapping a new Cursor session.

This SOP now has two tracks:

- **Recovery bootstrap** — the default after a restart, crash, or power loss when the goal is to recover context with minimal reads
- **Full health bootstrap** — an expanded AGENT/DEBUG check when environment health itself is relevant to the work

## Track A — Recovery Bootstrap (default)

Use this first unless the task explicitly depends on live environment health.

### Step 0: Launch Integrity

Cursor should still be launched through the canonical Bitwarden wrapper:

```powershell
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command "bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File \"$HOME\.openclaw\start-cursor-with-secrets.ps1\""
```

If launch integrity is unknown, record it as unverified rather than inventing a PASS.

### Step 1: Authority Gate

Read in this order:

1. `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. The repo authority contract for the repo in scope:
   - `AGENTS.md`
   - `.cursor/rules/01-charter-enforcement.md`
   - `.cursor/rules/05-global-mcp-usage.md`
   - `.cursor/rules/10-project-workflow.md`
   - `docs/ai/memory/MEMORY_CONTRACT.md`
   - `docs/ai/operations/NO_LOSS_RECOVERY_LOOP.md`
   - `docs/ai/operations/RECOVERY_BUNDLE_SPEC.md`

### Step 2: OpenMemory Retrieval

Run a targeted OpenMemory search for the active repo and task.

If OpenMemory is degraded:

1. Mark it FAIL immediately
2. Use the recovery bundle only if the task is still safely satisfiable
3. Record any reseed debt in `docs/ai/STATE.md`

### Step 3: Recovery Bundle

Read the recovery bundle via `filesystem` if it exists and appears current:

- `docs/ai/recovery/current-state.json`
- `docs/ai/recovery/session-summary.md`
- `docs/ai/recovery/active-blockers.json`
- `docs/ai/recovery/memory-delta.json`

The bundle is non-canonical. Use it to avoid broad rereads, not to override repo docs.

### Step 4: Operational Snapshot

Read the summary/current state section of `docs/ai/STATE.md`.

Then read exactly one of the following only if needed:

- `docs/ai/memory/DECISIONS.md`
- `docs/ai/memory/PATTERNS.md`
- `docs/ai/HANDOFF.md`

Use `docs/ai/context/AGENT_EXECUTION_LEDGER.md` only as a one-block-at-a-time fallback.

Other `docs/ai/context/` artifacts and chat history are not part of the default recovery bootstrap.

## Track B — Full Health Bootstrap (on demand)

Use this when environment health, tool reachability, or gateway/runtime behavior is part of the task.

### Step 1: Git State Verification

```powershell
git -C D:/github/AI-Project-Manager status
git -C D:/github/AI-Project-Manager log --oneline -3
git -C D:/github/open--claw status
git -C D:/github/open--claw log --oneline -3
git -C D:/github/open--claw tag -l "restore-*"
```

### Step 2: WSL Environment Health

```powershell
wsl -e bash -c 'source ~/.nvm/nvm.sh 2>/dev/null && node -v && pnpm -v'
wsl -e bash -c 'ls ~/openclaw-build/ > /dev/null && echo DIR_OK || echo DIR_MISSING'
```

### Step 3: Gateway Health

```powershell
wsl -e bash -c 'curl -s http://localhost:18792/ || echo GATEWAY_DOWN'
```

Important ports:

- Control UI: `18789`
- API health: `18792`
- Port `3000` is not used

### Step 4: MCP Tool Health

Test only the tools needed for the current task.

| Tool | Minimal test |
|------|--------------|
| Context7 | resolve a library |
| GitHub | list issues or similar lightweight repo call |
| Serena | activate exact-path project |
| OpenMemory | `search-memories` |
| thinking-patterns | `sequential_thinking`, `mental_model`, or `debugging_approach` |
| Exa Search | lightweight search query |
| Playwright | minimal browser call if browser verification is planned |
| Firecrawl | lightweight scrape/map if web extraction is planned |
| Magic MCP | lightweight design call if UI generation is planned |

Record each tested tool as PASS or FAIL with the actual fallback used.

If OpenMemory appears green but exposes no tools:

1. Run `pwsh -File D:\github\AI-Project-Manager\scripts\check_openmemory_stack.ps1`
2. Check whether `C:\Users\ynotf\.cursor\projects\d-github-AI-Project-Manager\mcps\user-openmemory\tools\` exists
3. If the tools directory is missing, treat OpenMemory as FAIL
4. Record the incident in `docs/tooling/MCP_HEALTH.md`

### Step 5: State Currency

Read the latest relevant `STATE.md` entry in each changed repo.
Confirm there is no unrecorded work that would distort the next task.

## Evidence Requirements

Every bootstrap entry should distinguish:

- newly verified evidence
- documented prior evidence
- still unverified assumptions

Do not label environment checks as PASS unless they were actually run in this session.

## Quick Reference

| Item | Value |
|------|-------|
| AI-PM branch | `main` |
| open--claw branch | `master` |
| Gateway UI | `http://localhost:18789` |
| Gateway API | `http://localhost:18792` |
| Node | v22.x via nvm |
| pnpm | 10.x |
| GitHub owner | `ynotfins` |
| Restore tag | `restore-20260308-2037-phase6c0` |
| bws project ID | `f14a97bb-5183-4b11-a6eb-b3fe0015fedf` |
