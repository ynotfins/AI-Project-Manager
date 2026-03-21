# Policy Drift Checker

Use this checklist before major planning cycles or after rule changes.

## Purpose

Detect and correct drift between canonical governance (`AI-Project-Manager`) and mirrored project rules (`open--claw`, `droidrun`) while keeping context overhead minimal.

## Canonical source

AI-PM is canonical:

- `.cursor/rules/00-global-core.md`
- `.cursor/rules/05-global-mcp-usage.md`
- `.cursor/rules/10-project-workflow.md`
- `.cursor/rules/20-project-quality.md`
- `docs/ai/operations/*`

## Drift checks (PASS/FAIL)

1. **Tool policy parity**
   - Clear Thought 1.5 is primary reasoning tool
   - sequential-thinking is fallback only
   - serena + Context7 usage mandates exist
2. **PLAN/AGENT contract parity**
   - PLAN no-edit/no-command
   - AGENT state update required after each execution block
   - PASS/FAIL evidence requirement present
3. **State template parity**
   - Full required section template exists in workflow rule
4. **Context preservation parity**
   - `STATE.md` source priority defined
   - `docs/ai/context/` non-canonical
   - `docs/ai/archive/` never-consulted for operations
5. **Quality/security parity**
   - Secrets policy present
   - Context7 `query-docs` dependency verification requirement present

## Quick command audit

```powershell
$canon = "D:\github\AI-Project-Manager\.cursor\rules"
$targets = @(
  "D:\github\open--claw\.cursor\rules",
  "D:\github\droidrun\.cursor\rules"
)

foreach ($t in $targets) {
  Write-Host "`n=== Comparing $t to canonical ==="
  git diff --no-index "$canon\05-global-mcp-usage.md" "$t\05-global-mcp-usage.md" | Out-Host
  git diff --no-index "$canon\10-project-workflow.md" "$t\10-project-workflow.md" | Out-Host
  git diff --no-index "$canon\20-project-quality.md" "$t\20-project-quality.md" | Out-Host
}
```

## Action policy on drift

- If drift is cosmetic only: normalize formatting.
- If drift changes behavior/safety/tooling: patch target repo to canonical parity.
- Record every harmonization in both repos' `docs/ai/STATE.md`.

## Context-window hygiene

- Keep rules concise and high-signal.
- Avoid redundant "always apply" meta-rules that add instruction bloat.
- Prefer one canonical rule set + mirrored parity checks over many overlapping directives.
