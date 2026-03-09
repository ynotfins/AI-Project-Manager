# Session Bootstrap SOP

Standard operating procedure for bootstrapping a new Cursor session.
Run this at the start of every session to verify system state before doing work.

## Pre-flight Checklist

Run all 7 steps in order. Record PASS/FAIL for each.

### Step 1: Git State Verification

```powershell
git -C D:/github/AI-Project-Manager status
git -C D:/github/AI-Project-Manager log --oneline -3
git -C D:/github/open--claw status
git -C D:/github/open--claw log --oneline -3
git -C D:/github/open--claw tag -l "restore-*"
```

**PASS criteria:** Both repos on expected branches (AI-PM: `main`, open--claw: `master`).
No unexpected changes. Restore tags present.

### Step 2: WSL Environment Health

```powershell
wsl -e bash -c 'source ~/.nvm/nvm.sh 2>/dev/null && node -v && pnpm -v'
wsl -e bash -c 'ls ~/openclaw-build/ > /dev/null && echo DIR_OK || echo DIR_MISSING'
```

**PASS criteria:** Node v22.x, pnpm 10.x, directory exists.
**If FAIL:** See Host Restart Verification pattern in `docs/ai/memory/PATTERNS.md`.

### Step 3: Gateway Health

```powershell
wsl -e bash -c 'curl -s http://localhost:18792/ || echo GATEWAY_DOWN'
```

**PASS criteria:** Returns `OK`.
**If FAIL:** Restart with `wsl -e bash -c 'cd ~/openclaw-build && source ~/.nvm/nvm.sh && pnpm openclaw gateway --force'`

**Important:** Gateway ports are **18789** (Control UI) and **18792** (API health).
Port 3000 is NOT used.

### Step 4: MCP Tool Health

Test each MCP tool with a minimal invocation:

| Tool | Test | PASS |
|------|------|------|
| Context7 | `resolve-library-id` for any library | Response received |
| Firestore | `list-collections` | Response (even empty/error is informative) |
| GitHub | `list_issues` for `ynotfins/AI-Project-Manager` | Response received |
| Serena | `activate_project` + `check_onboarding_performed` | Project activated |
| OpenMemory | `search-memory` with any query | Response received |

Record each as PASS or FAIL + fallback tool to use.

### Step 5: STATE.md Currency

Read the last entry in both repos' `docs/ai/STATE.md`.
Confirm the timestamp and verdict match your expectations.
Confirm no unrecorded work exists.

### Step 6: Decision Point

Based on steps 1-5, assess:
- Are there open blockers from the last session?
- What was the last "What's Next" recommendation?
- Is the system ready for the planned work?

### Step 7: STATE.md Update + Commit

Write a full 13-section STATE.md entry (template in `.cursor/rules/10-project-workflow.md`)
with all evidence from steps 1-6.

```powershell
git -C D:/github/AI-Project-Manager add docs/ai/STATE.md && git -C D:/github/AI-Project-Manager commit -m "phase-0: session bootstrap"
git -C D:/github/open--claw add docs/ai/STATE.md && git -C D:/github/open--claw commit -m "phase-0: session bootstrap (mirror)"
```

## Evidence Requirements

Every bootstrap produces:
- Branch names and git status for both repos
- Node and pnpm version strings
- Gateway health response
- MCP tool PASS/FAIL table
- STATE.md currency confirmation
- Commit SHAs for both repos

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
