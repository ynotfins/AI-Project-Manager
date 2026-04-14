# Tools

**Document Role:** This file provides **canonical exec routing patterns and primary tool usage expectations**. For access configuration and recovery, see `ACCESS.md`. For complete tool inventory, see `COMPLETE_TOOL_REFERENCE.md`.

## Primary Tools
- repo search
- git review
- web research
- thinking-patterns reasoning
- Context7 docs
- artifact review
- ffprobe / ffmpeg media recovery
- MediaInfo / container inspection
- checksum and binary inspection
- exec (shell — Linux gateway and Windows node)
- browser verification
- Twilio Voice webhooks/runtime
- ElevenLabs voice configuration

## Tooling Expectations
- Use `thinking-patterns` on nearly every non-trivial Sparky prompt before finalizing a plan, diagnosis, or high-risk decision.
- Default mapping: `sequential_thinking` for multi-step work, `problem_decomposition` for execution breakdown, `mental_model` for architecture, `decision_framework` for trade-offs, `debugging_approach` for failures, `critical_thinking` for self-critique.
- Use Context7 when framework or library behavior matters.
- For damaged video files, prefer `ffprobe` + `mediainfo` triage first, then copy-based `ffmpeg` recovery before any re-encode fallback.
- Keep `mpv` or `VLC` available for seek/playback validation after every recovery attempt.
- Use `Get-FileHash` or equivalent checksums before and after every repair attempt.
- When MP4/MOV indexing looks damaged, use `untrunc`, `MP4Box`, `mkvmerge`, or Bento4 tools if a compatible reference file exists.
- Use browser and screenshot tooling when UX claims need proof.
- Use git and diff review for every meaningful code change.
- Use tests and build outputs as evidence, not decoration.
- Use Twilio and ElevenLabs only through env-backed configuration and documented webhook/runtime boundaries.
- Treat live phone workflows as production integrations: verify latency, fallback greeting, escalation, and summary capture.

## Exec Routing

Two exec hosts are available. The default is the Linux gateway (WSL Ubuntu).

### Linux gateway (default) — `host=gateway`
Runs on the WSL Ubuntu machine where the OpenClaw gateway lives.
Use for: `openclaw` CLI, bash/sh, Linux tools, file ops in the Linux filesystem.

```
exec openclaw security audit --deep
exec openclaw doctor
exec bash -c "cat /etc/os-release"
```

### Windows Desktop node — `host=node`
Routes to the paired Windows Desktop node via `system.run`.
Use for: PowerShell, Windows CLI tools, WSL2 commands from Windows, Windows file ops.

```
exec --host node pwsh -NoProfile -Command "Get-Process | Select-Object -First 10"
exec --host node pwsh -NoProfile -File "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"
exec --host node wsl -d Ubuntu -- openclaw security audit --deep
exec --host node wsl -d Ubuntu -- bash -c "systemctl status openclaw"
exec --host node cmd /c dir "D:\github"
```

### Elevated Windows execution — `host=node` with elevated node-host
For admin-level Windows operations, the Windows node-host must be running as Administrator.
To start the node-host elevated: right-click `node.cmd` → Run as administrator.
When node-host is elevated, all `exec --host node` commands inherit that elevation.

```
exec --host node pwsh -NoProfile -Command "Get-WindowsCapability -Online | Where State -eq Installed"
exec --host node pwsh -NoProfile -Command "netsh interface show interface"
```

### Elevated Linux execution — `/elevated` directive
Send `/elevated` to switch Sparky into elevated mode (Tony's Telegram only).
In elevated mode, exec commands can use `sudo` on the Linux gateway.

```
exec sudo systemctl restart openclaw
exec sudo journalctl -u openclaw -n 50
```

## Exec Security Policy
- `security: full` on both gateway and node — all commands run without allowlist gates.
- `ask: off` — no human approval prompt required for exec.
- `elevated.allowed: true` on both sides — elevated execution is permitted.
- No secrets in exec commands; inject via environment or Bitwarden-backed env.
