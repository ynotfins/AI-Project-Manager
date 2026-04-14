---
name: media-recovery-validation
description: Validation workflow for proving whether a recovered media file is truly fixed, partially salvaged, or still corrupt.
category: Recovery
roles:
  - sparky-chief-product-quality-officer
---

# Media Recovery Validation

## Status: READY

## Purpose
Make media-recovery claims evidence-based by validating playback, seeking, duration, streams, and failure boundaries after each repair attempt.

## Validation Checklist
- Confirm container and streams with `ffprobe`.
- Confirm duration matches expectation closely enough to explain any loss.
- Test playback from start, midpoint, and near the original failure point.
- Test random seek points to catch broken indexes.
- Compare audio/video sync where relevant.
- Record whether the result is:
  - fully recovered
  - partially recovered
  - playable but degraded
  - unrecoverable

## Rules
- Do not call a file fixed just because the first minute plays.
- Separate playback success from archival integrity.
- Keep every recovery attempt numbered so results can be compared.
- If a file is only partially recovered, state the exact usable range.

## Output
- Recovery attempt id
- Commands run
- Validation result
- Remaining corruption or quality loss
- Recommended next attempt or stop condition
