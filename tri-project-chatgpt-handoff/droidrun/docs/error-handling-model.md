# Error Handling Model

This document describes how DroidRun handles failures at every layer — from ADB transport errors to LLM API failures to keyboard interrupts — and what the system does when each failure occurs.

---

## Layered Error Handling Overview

```
CLI / MCP Server
  └── DroidAgent Workflow (LlamaIndex)
        ├── StateProvider (UI fetch with retry)
        │     └── PortalClient (TCP → content-provider fallback)
        ├── LLM API call (no retry on failure)
        ├── Action functions (propagate ActionResult)
        └── AndroidDriver (ADB transport)
```

Each layer has its own failure behavior. Lower layers generally propagate exceptions upward unless they have a specific recovery strategy.

---

## PortalClient: TCP → Content Provider Fallback

**What fails:** The Portal APK's TCP socket server (port 8080) is unavailable.

**How it's detected:** `PortalClient.connect()` attempts `GET http://localhost:8080/ping`. If the request times out or is refused, TCP is marked unavailable.

**Recovery:**
1. `PortalClient` automatically marks `tcp_available = False`
2. All subsequent calls route to the ADB content provider instead:
   ```
   adb shell content query --uri content://com.droidrun.portal/state
   ```
3. No user intervention required. The fallback is transparent.

**When fallback also fails:** The content provider call fails → enters the `StateProvider` retry loop (see below).

---

## StateProvider: Retry with Backoff + Mid-Retry Recovery

**What fails:** `driver.get_ui_tree()` returns an error, times out, or returns an incomplete response.

**Retry schedule:**

| Attempt | Delay before retry |
|---|---|
| 1 | — |
| 2 | 1s |
| 3 | 2s |
| 4 | 3s |
| 5 | 5s — **recovery triggered** |
| 6 | 8s |
| 7 | 10s |
| — | Exception raised |

Total wait across all retries: ~29 seconds before giving up.

**Recovery action (fired once after attempt 5):**
```python
# AndroidStateProvider._recover_portal():
adb shell settings put secure accessibility_enabled 0
adb shell settings put secure enabled_accessibility_services com.droidrun.portal/...
adb shell settings put secure accessibility_enabled 1
# then restart TCP socket server via content provider toggle
```

**After all retries exhausted:**
- `Exception("Failed to get state after 7 attempts: ...")` raised
- Propagates to the workflow step
- LlamaIndex emits `ResultEvent(success=False)`
- CLI prints error and exits

**`DeviceDisconnectedError`:** Re-raised immediately — no retries. ADB disconnects are considered unrecoverable without user intervention.

---

## Portal Accessibility Auto-Enable → Manual Fallback

**What fails:** Portal APK is installed but its accessibility service is disabled (common after phone reboot or system update).

**Detection:** First state fetch returns empty/error response. `portal.py` checks if the a11y service is enabled.

**Recovery:**
1. Auto-enable attempted:
   ```
   adb shell settings put secure enabled_accessibility_services com.droidrun.portal/...
   adb shell settings put secure accessibility_enabled 1
   ```
2. If auto-enable succeeds → continues normally
3. If auto-enable fails (some OEMs block this) → manual instructions printed to terminal + Android Settings > Accessibility screen opened via ADB

---

## ADB Device Not Found

**What fails:** `adb devices` does not show the configured device.

**Error:** `DeviceDisconnectedError` (custom exception in `src/droidrun/tools/driver/base.py`)

**Behavior:** Re-raised immediately everywhere. No retries. Clear error message in logs:
```
ERROR: Device <serial> not found. Is ADB connected?
```

**User action required:** `adb connect <ip>:<port>` or plug in USB.

---

## LLM API Errors

**What fails:** The LLM provider returns an error (HTTP 4xx/5xx, timeout, connection refused).

**Behavior:**
1. LlamaIndex raises an exception from the LLM call
2. The workflow step fails
3. LlamaIndex catches it and emits `ResultEvent(success=False, result=error_message)`
4. `DroidAgent.run()` returns `(False, error_message)`
5. CLI prints the error

**No automatic retry** on LLM API errors. If you want retry behavior, re-run the command.

**Special case — OpenRouter/vision:** If `DROIDRUN_OPENROUTER_KEY` is not set, `mcp_server.py` returns an error string to the MCP client immediately (before attempting the subprocess) rather than letting the subprocess fail with a traceback.

---

## Max Steps Reached

**What fails:** The agent completes `max_steps` iterations without calling `complete()`.

**Default:** 50 steps (configurable via `agent.max_steps` or `--steps` CLI flag).

**Behavior:**
1. The DroidAgent step loop checks `step_number >= max_steps`
2. Emits `ResultEvent(success=False, result="Max steps reached without completing the task")`
3. Trajectory (if enabled) is saved up to the last step

This is a graceful stop — not a crash. All state is preserved in the trajectory file if recording is enabled.

---

## KeyboardInterrupt (Ctrl+C)

**What fails:** User presses Ctrl+C during a run.

**Behavior:**
1. Python raises `KeyboardInterrupt` in the active coroutine
2. Caught in `src/droidrun/cli/main.py` main function
3. Returns `False` gracefully
4. No traceback printed to the user (clean exit)
5. Trajectory file may be incomplete (written incrementally, so partial data may exist)

---

## MCP Tool Errors

**What fails:** Any exception inside `mcp_server.py`'s `call_tool()` handler.

**Behavior:**
- Exceptions are caught and returned as `CallToolResult` with error text in `TextContent`
- The MCP client (Cursor, Claude Desktop, etc.) receives the error as a tool result string — not as a protocol-level error
- The MCP server process continues running; subsequent tool calls work normally

Example error response seen by MCP client:
```
ERROR: Could not connect to phone: [Errno 111] Connection refused
Make sure Wireless debugging is ON and Tailscale is running.
```

---

## `safe_execution` Sandbox (CodeActAgent)

**What fails:** Agent-generated Python code tries to import restricted modules or use blocked builtins.

**When active:** `safe_execution.enabled: true` in config (off by default).

**Implementation:** `src/droidrun/config_manager/safe_execution.py` — restricts the Python execution environment available to CodeActAgent:
- Blocks specific module imports (e.g., `os`, `sys`, `subprocess`)
- Restricts builtins (e.g., `__import__`, `eval`, `exec`)

**Failure behavior:** `ImportError` or `NameError` raised inside the sandboxed exec. Returned to agent as action failure. Agent may retry with a different approach or call `complete(success=False)`.

---

## Error Escalation (reasoning=True, Manager/Executor)

When `reasoning=True`, repeated Executor failures are escalated to the ManagerAgent:

- `DroidAgentState.error_flag_plan: bool` — set when Executor fails
- `DroidAgentState.err_to_manager_thresh: int` (default 2) — number of consecutive failures before escalating
- After `err_to_manager_thresh` consecutive failures, the Manager receives an escalation event and re-plans

This prevents the Executor from looping indefinitely on an impossible subgoal.

---

## Script Error Handling (PowerShell)

The 12 scripts in `scripts/` use a consistent pattern:

```powershell
$ErrorActionPreference = "SilentlyContinue"   # Non-critical commands don't abort
# ... attempt command ...
if ($LASTEXITCODE -ne 0) {
    Write-Warning "Step failed: <description>"
    exit 1
}
```

- Non-critical ADB commands (e.g., `adb forward`) use `SilentlyContinue` so a stale forward doesn't abort the script
- Critical checks (device connected, API key set) use explicit `if` checks + `exit 1`
- Scripts do **not** silently continue through critical failures

---

## Timeout Handling

| Context | Timeout | Behavior on timeout |
|---|---|---|
| `DroidAgent` workflow | 1000s (default) | LlamaIndex workflow timeout; raises `asyncio.TimeoutError`; CLI prints error |
| `mcp_server.py` subprocess | 300s | `subprocess.TimeoutExpired`; error returned to MCP client |
| `_ensure_connected()` ADB connect | 10s per `subprocess.run` call | `subprocess.TimeoutExpired`; returns error string |
| `phone_ping` / `phone_apps` | 15s per `subprocess.run` | Same |
| Portal state fetch | ~29s total (retry schedule) | Exception after final retry |
| Portal TCP ping on connect | Inferred short timeout | Falls back to content provider |

---

## Error Visibility Summary

| Error Type | User Sees | Log Level |
|---|---|---|
| ADB not connected | Clear error message in CLI output | ERROR |
| Portal inaccessible (recoverable) | Warning during retry; continues | WARNING |
| Portal inaccessible (unrecoverable) | Error + manual instructions | ERROR |
| LLM API failure | Error message from exception | ERROR |
| Max steps reached | "Max steps reached" result message | WARNING |
| KeyboardInterrupt | Clean exit, no traceback | — |
| MCP tool error | Error text in tool result | — (no log to client) |
| safe_execution violation | Action failure message to agent | DEBUG |
| Script failure | Write-Warning + exit 1 | PowerShell stream |
