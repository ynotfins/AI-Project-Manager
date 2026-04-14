# Offline and Sync Model

DroidRun has **no offline mode and no sync layer**. Every component of a successful run requires live connectivity to the appropriate service. This document describes exactly what fails without each network dependency, what remains functional, and how the system degrades gracefully.

---

## System Requirements for a Successful Run

| Component | Requires Network? | Notes |
|---|---|---|
| ADB (USB) | No | USB ADB is purely local |
| ADB (wireless/Tailscale) | Yes (Tailscale VPN) | VPN must be up for remote ADB |
| Portal APK (already installed) | No | Runs on-device; no network |
| Portal APK (first install) | Yes | Downloads from GitHub |
| LLM API | Yes | All providers are cloud APIs |
| Ollama (local) | No | Runs locally; no network needed |
| PostHog telemetry | Yes (optional) | Fire-and-forget; failure is silent |
| Arize Phoenix tracing | No (local server) | Runs on localhost |
| Langfuse tracing | Yes (optional) | Cloud service |
| Trajectory save | No | Writes to local disk |

---

## What Fails Without Internet

### LLM API calls

Without internet access to the configured LLM provider (OpenAI, Anthropic, Google, DeepSeek, OpenRouter), the agent cannot make any progress. The failure path is:

1. LLM API call raises a network error (connection refused, DNS failure, timeout)
2. LlamaIndex propagates the exception up the workflow
3. The workflow step fails
4. `ResultEvent(success=False)` is emitted
5. CLI prints the error and exits

There is **no retry loop for LLM API failures** — the run ends immediately.

**Exception:** If Ollama is configured (`provider: Ollama`, `api_base: http://localhost:11434`), the LLM call goes to a local server. No internet required for inference; however, the Ollama model must already be pulled (`ollama pull <model>`).

### Portal APK download

If the Portal APK is not yet installed on the device and there is no internet access:

1. `droidrun setup` (or first-run auto-setup) calls `download_portal_apk()`
2. HTTP request to `https://ungh.cc/repos/droidrun/droidrun-portal/releases/latest` times out
3. Setup aborts with a clear error message
4. The user must manually download the APK and install via `adb install`

**If Portal is already installed:** No network needed for Portal operation. The APK runs on the device and communicates via ADB.

### PostHog telemetry

- If PostHog is unreachable: telemetry events are silently dropped
- No retry, no queue, no impact on agent behavior
- The run continues normally

### Langfuse tracing

- If Langfuse is unreachable: traces are silently dropped
- No retry, no queue, no impact on agent behavior

---

## What Works Offline (USB ADB)

When the device is connected via USB and the Portal APK is already installed:

| Feature | Works offline? |
|---|---|
| Screen reading (a11y tree) | Yes |
| Tap / swipe / type actions | Yes |
| Screenshot capture | Yes |
| App launch | Yes |
| Trajectory recording | Yes |
| Ollama inference | Yes (if local model pulled) |
| Phoenix tracing | Yes (local server) |

Essentially: everything except cloud LLM APIs works offline over USB.

---

## What Works Without Remote ADB (Tailscale down)

If Tailscale is disconnected but the device is on USB:

| Feature | Works? |
|---|---|
| USB ADB operations | Yes |
| MCP server `phone_do` tool | No — `mcp_server.py` hardcodes `100.71.228.18:5555` (Tailscale address) |
| Direct CLI `droidrun run -d <usb-serial>` | Yes |

The `mcp_server.py` hardcodes the Tailscale device address. If Tailscale is down but USB is connected, the MCP server will fail. Use the CLI directly in that case.

---

## No Queued Actions

DroidRun does **not** queue actions for later delivery. If a step fails (ADB disconnected, LLM timeout, Portal unreachable), the run stops immediately. There is no:

- Retry queue for failed actions
- Offline action buffer
- Resume-from-last-step capability

If you need to retry a task, re-run `droidrun run` from scratch. Trajectory files let you inspect what happened in a failed run, but they cannot be used to resume.

---

## No Conflict Handling

There is no multi-device sync, no multi-agent coordination, and no shared state between runs. Each `droidrun run` is isolated. Running two instances simultaneously against the same device will result in race conditions on the ADB connection (the second instance will likely fail to acquire the ADB lock or cause unpredictable UI interactions).

---

## Graceful Degradation in Scripts

The 12 PowerShell scripts in `scripts/` use `$ErrorActionPreference = "SilentlyContinue"` for individual ADB commands, but include explicit error checks for critical steps. The scripts:

- Check for device connectivity before proceeding (`adb devices`)
- Warn and exit (non-zero) if required connectivity is missing
- Do **not** crash silently — failures produce descriptive output before exiting

Example pattern in scripts:
```powershell
$devices = adb devices 2>&1
if ($devices -notmatch "device$") {
    Write-Warning "No ADB device found. Connect device and try again."
    exit 1
}
```

---

## Summary

| Scenario | Result |
|---|---|
| No internet, USB ADB, Portal installed, Ollama running | Full functionality |
| No internet, USB ADB, Portal installed, cloud LLM | Run fails immediately at first LLM call |
| No internet, Portal not installed | Setup fails; cannot install Portal |
| Tailscale down, USB ADB connected | CLI works; MCP server does not |
| Tailscale down, no USB | All connectivity fails |
| Mid-run ADB disconnect | `DeviceDisconnectedError` raised; run ends immediately |
| Mid-run Portal crash | Auto-recovery attempted (restart a11y service); if recovery fails after 7 attempts, run ends |
| Mid-run LLM API error | Run ends immediately with `ResultEvent(success=False)` |
