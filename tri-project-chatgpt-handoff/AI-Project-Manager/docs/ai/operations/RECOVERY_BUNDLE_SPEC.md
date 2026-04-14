# Recovery Bundle Specification

This document defines the concrete recovery bundle used to reduce reread thrash after a reboot, crash, or power loss.

## Status

The recovery bundle is **non-canonical**.

It is a speed layer only. Repo-tracked docs remain authoritative.

## Goals

- cut the amount of repo rereading needed after recovery
- preserve exact pointers into canonical repo docs
- record tool degradations and memory reseed debt
- stay compact enough to inspect quickly

## Storage location

The recovery bundle lives in this repo and must be written via `filesystem` to:

- `docs/ai/recovery/current-state.json`
- `docs/ai/recovery/session-summary.md`
- `docs/ai/recovery/active-blockers.json`
- `docs/ai/recovery/memory-delta.json`

No broad repo scanning is allowed for default recovery. Read only these files plus OpenMemory first.

## Required contents

### `current-state.json`

Required schema:

- `phase`
- `goal`
- `last_action`
- `active_workers`

### `active-blockers.json`

Required schema:

- `blockers`: list of objects containing at least:
  - `title`
  - `severity`

### `memory-delta.json`

Required schema:

- `decisions`
- `patterns`

Each list should contain the latest compact durable deltas worth re-querying in OpenMemory.

### `session-summary.md`

Required contents:

- current human-readable narrative
- active blockers summary
- next recommended action

## Freshness rules

Treat the bundle as current only when:

- it reflects the latest meaningful verified work
- no newer unresolved `STATE.md` block contradicts it
- its last refresh is recent enough for the active task

If freshness is uncertain, say so and fall back to canonical repo docs.

## Update cadence

Refresh the bundle:

- after meaningful verified AGENT work
- after ARCHIVE promotion work
- after DEBUG produces a stable root cause worth carrying forward
- after any incident that creates memory reseed debt

Do not churn the bundle for trivial edits.

## Content discipline

- Keep the bundle pointer-heavy, not duplicate-heavy
- Do not paste large doc copies into it
- Do not include secrets, token IDs, or raw credentials
- Do not treat Obsidian or Artiforge outputs as authoritative inputs
- Do not embed broad transcript dumps

## Allowed uses

- accelerate recovery after a crash or reboot
- carry forward compact tool-failure and reseed notes
- reduce broad `STATE.md` or ledger reads during PLAN/DEBUG
- provide enough context that recovery can start from OpenMemory plus these files only

## Forbidden uses

- overriding repo-tracked docs
- replacing `STATE.md`, `HANDOFF.md`, `DECISIONS.md`, or `PATTERNS.md`
- becoming the default source of truth
- hiding that OpenMemory storage/retrieval was skipped

## Recovery test

The recovery path is considered materially present only when:

1. the four files above physically exist
2. OpenMemory contains a matching compact durable update
3. a recovery read can explain current phase, goal, blockers, and recent decisions without broad repo scanning
4. a later normal execution refreshes the same bundle without manual repair steps between the execution and the recovery read
