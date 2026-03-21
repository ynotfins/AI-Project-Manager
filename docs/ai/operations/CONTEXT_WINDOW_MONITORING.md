# Context Window Monitoring

This runbook keeps PLAN and AGENT within safe context limits by monitoring document size, estimated token cost, and archive thresholds.

## Why this exists

Large state and history files can silently consume the context budget before useful work starts. This file defines measurable guardrails.

## Token estimation model

Use fast approximation for English-heavy markdown:

- `estimated_tokens = character_count / 4`

This is approximate by design and good enough for guardrails.

## Budgets by tab

Assume a practical upper bound of 200k model tokens. Keep large safety margin.

- PLAN preload target: <= 35k tokens
- PLAN hard ceiling: 60k tokens
- AGENT preload target: <= 25k tokens
- AGENT hard ceiling: 45k tokens
- Any single source file target: <= 12k tokens
- Any single source file hard ceiling: 20k tokens

## File size guardrails

For operational docs in active use:

- `docs/ai/STATE.md`
  - target: <= 140 KB
  - warn: > 140 KB
  - archive required: > 180 KB
- `docs/ai/HANDOFF.md`
  - target: <= 16 KB
  - rewrite required: > 24 KB
- `docs/ai/PLAN.md`
  - target: <= 36 KB
  - refactor required: > 48 KB

## Monitoring cadence

- Before every major PLAN cycle
- After every substantial AGENT block
- Before appending to `STATE.md`

## Quick check commands (PowerShell)

```powershell
$files = @(
  "D:\github\AI-Project-Manager\docs\ai\STATE.md",
  "D:\github\AI-Project-Manager\docs\ai\HANDOFF.md",
  "D:\github\AI-Project-Manager\docs\ai\PLAN.md"
)

$files | ForEach-Object {
  $raw = Get-Content -Raw $_
  [PSCustomObject]@{
    File = $_
    SizeKB = [math]::Round((Get-Item $_).Length / 1KB, 1)
    Chars = $raw.Length
    EstTokens = [math]::Round($raw.Length / 4, 0)
  }
}
```

## Archive policy trigger

When `STATE.md` crosses warn threshold:

1. Move completed or superseded blocks to `docs/ai/archive/`.
2. Keep current summary, active blockers, and newest operational entries in active `STATE.md`.
3. Update `docs/ai/archive/README.md` index.
4. Record the archive action in `STATE.md` with PASS/FAIL evidence.

## Failure policy

If thresholds are exceeded and no archive is done:

- Mark context health as FAIL in `STATE.md`.
- Stop non-critical work.
- Run archive cleanup before next feature block.
