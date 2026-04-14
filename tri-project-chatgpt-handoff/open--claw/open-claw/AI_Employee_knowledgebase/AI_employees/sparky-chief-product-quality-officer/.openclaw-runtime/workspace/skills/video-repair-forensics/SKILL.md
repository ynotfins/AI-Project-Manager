---
name: video-repair-forensics
description: Evidence-first workflow for recovering damaged or partially playable video files with copy-first salvage, container triage, and validation.
category: Recovery
roles:
  - sparky-chief-product-quality-officer
---

# Video Repair Forensics

## Status: READY

## Purpose
Recover damaged video files without destroying the original evidence, starting with container triage and copy-based salvage before any re-encode fallback.

## Default Toolchain
- `ffprobe` for stream, timestamp, and container inspection
- `ffmpeg` for remux, stream copy, timestamp regeneration, and salvage re-encode
- `mediainfo` for second-opinion container metadata
- `mpv` or `VLC` for seek/playback verification
- checksums (`Get-FileHash`, `sha256sum`) for before/after evidence
- `untrunc`, `MP4Box`, `mkvmerge`, or Bento4 tools when MP4/MOV headers or indexes are damaged and a compatible reference file exists

## Rules
- Never overwrite the damaged source file.
- Always work on a copy and preserve hashes, file sizes, timestamps, and the exact failure point.
- Prefer stream copy / remux before re-encoding.
- Record whether failure appears to be container corruption, timestamp corruption, truncation, or decode corruption.
- If encryption/decryption is suspected, compare multiple affected files for the same failure pattern before assuming random damage.

## Recovery Order
1. Hash the original and create a working copy.
2. Inspect with `ffprobe` and `mediainfo`.
3. Try copy-first remux to a safer container.
4. Try timestamp regeneration or corrupt-packet skipping.
5. If MP4/MOV indexing is damaged, try header/index repair with a same-device reference file.
6. Re-encode only as a last-resort salvage path.
7. Verify with playback seeking and fresh `ffprobe` output.

## Evidence Required
- Original file hash and working-copy hash
- `ffprobe` notes before and after
- Exact timestamp where playback failure begins
- Recovery command(s) used
- Final verification result: fully playable, partially salvaged, or unrecoverable
