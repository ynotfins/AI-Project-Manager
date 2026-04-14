# Safe Failure and Disable Paths

DroidRun v0.5.1 — How to disable risky features, kill the agent, and understand failure modes.

---

## 1. Disabling Risky Behavior

### Vision Mode

Vision mode sends device screenshots to the LLM provider. Disable it when screenshot content is sensitive.

```yaml
# In ~/.config/droidrun/config.yaml
agent:
  fast_agent:
    vision: false
```

Or via CLI: omit the `--vision` flag. Vision is opt-in per run; it is not active unless `--vision` is passed or set in config.

---

### Code Execution (CodeAct Agent)

The CodeAct agent generates and executes arbitrary Python code. Disable it to prevent code generation.

```yaml
# In ~/.config/droidrun/config.yaml
agent:
  fast_agent:
    codeact: false   # default is false; verify this is not set to true
```

If `codeact: true` appears in your config, remove it or set it to `false`.

---

### Unsafe Code Sandbox (safe_execution)

When CodeAct or Scripter is active, enable `safe_execution` to restrict what code can do. This blocks `os`, `sys`, `subprocess`, `shutil`, `pathlib`, `open`, `exec`, `eval`, `compile`, `importlib`, and `__import__`.

```yaml
# In ~/.config/droidrun/config.yaml
agent:
  fast_agent:
    safe_execution: true
  scripter:
    safe_execution: true
```

**Default state:** Disabled. Must be explicitly enabled. Enabling this may cause legitimate agent code to fail if it uses filesystem operations.

---

### Telemetry

Anonymous usage events sent to PostHog. Disable for air-gapped environments or privacy preference.

```yaml
# In ~/.config/droidrun/config.yaml
telemetry:
  enabled: false
```

Telemetry does not contain screen content or task details — only CLI invocation counts, model names, and success/failure booleans. Disabling is still reasonable for internal environments.

---

### Auto-Setup (Portal Auto-Install)

When `auto_setup: true`, DroidRun will automatically install or update the Portal APK on the connected device. Disable this to prevent unexpected APK changes.

```yaml
# In ~/.config/droidrun/config.yaml
device:
  auto_setup: false
```

With auto_setup disabled, you must manually install Portal updates via `droidrun setup` or direct APK install.

---

### MCP Server

Disable MCP integration to prevent AI clients from connecting to DroidRun.

```yaml
# In ~/.config/droidrun/config.yaml
mcp:
  enabled: false
```

Alternatively, simply do not add DroidRun to the AI client's MCP config (Cursor, OpenClaw, Claude Desktop). The MCP server only runs when launched by a client.

---

### Credential Manager

Disable the credential manager to prevent DroidRun from storing or using app credentials.

```yaml
# In ~/.config/droidrun/config.yaml
credentials:
  enabled: false
```

With this disabled, any task requiring credential injection will fail at the credential lookup step rather than using stored passwords.

---

## 2. Kill Switches

### Ctrl+C in CLI

Sending SIGINT (Ctrl+C) to a running `droidrun run` command triggers graceful shutdown. The agent catches the signal, stops execution, and returns `ResultEvent(success=False)`. No partial actions are rolled back — any UI changes made up to the interruption point persist on the device.

---

### MCP Server Process

The MCP server runs as a child process spawned by the AI client (Cursor, Claude Desktop, etc.). To stop it:

- Close the AI client application — it terminates child processes on exit
- Or kill the process directly:

```powershell
# Find and kill the MCP server process
Get-Process python | Where-Object { $_.CommandLine -like "*mcp_server*" } | Stop-Process -Force
```

---

### ADB Disconnect (Remote)

Disconnect the remote device immediately and prevent all further ADB communication:

```powershell
adb disconnect 100.71.228.18:5555
```

This terminates any active ADB connection to the Tailscale device. Any in-progress DroidRun task will fail at the next ADB or Portal call.

---

### Portal Force Stop (On-Device)

Kill the Portal APK on the device without disconnecting ADB:

```powershell
adb shell am force-stop com.droidrun.portal
```

This stops the Portal HTTP server. The DroidRun agent will fail on the next action. Portal can be restarted by:

```powershell
adb shell am start -n com.droidrun.portal/.MainActivity
```

---

### Kill ADB Server (Nuclear)

Stop the ADB daemon on the host machine, disconnecting all devices:

```powershell
adb kill-server
```

This disconnects all ADB-connected devices (USB and wireless). ADB will restart automatically on the next ADB command. Any active DroidRun tasks will fail immediately.

---

### Remove ADB Port Forward

If `adb forward tcp:8080 tcp:8080` is active and you want to cut Portal access without disconnecting ADB:

```powershell
adb forward --remove tcp:8080
# Or remove all forwards:
adb forward --remove-all
```

---

## 3. Degraded Mode Behavior

### LLM API Unavailable (network outage or key invalid)

| Behavior | Fail mode |
|---|---|
| Agent receives API error on first LLM call | FAIL CLOSED |
| Returns `ResultEvent(success=False, error="API error: ...")` | — |
| No retry by default | — |
| No fallback model | — |

The agent does not silently degrade to a fallback model. It fails with an explicit error.

---

### Portal Not Accessible (TCP path)

| Behavior | Fail mode |
|---|---|
| TCP connection to localhost:8080 fails | Attempt fallback |
| Falls back to ADB content provider | FAIL OPEN (partial) |
| If content provider also fails | FAIL CLOSED |

The `PortalClient` implements a dual transport: TCP (primary) and ADB content provider (fallback). If TCP is unavailable (e.g., `adb forward` not set up), the client falls back to reading the accessibility tree via ADB content provider queries. This fallback has reduced functionality.

---

### Bitwarden Unavailable at Startup

| Behavior | Fail mode |
|---|---|
| `bws` CLI cannot reach Bitwarden | FAIL CLOSED at startup |
| `startup_droidrun.ps1` exits without loading API keys | — |
| DroidRun is never started | — |

By design: if secrets cannot be loaded, DroidRun does not start. This prevents running with missing API keys silently.

---

### Device Not Found

| Behavior | Fail mode |
|---|---|
| `adb devices` returns no authorized device | FAIL CLOSED |
| Explicit error: "No authorized device found" | — |
| No retry or wait | — |

---

## 4. Fail-Closed vs Fail-Open Summary

| Condition | Behavior | Rationale |
|---|---|---|
| API key missing from environment | **FAIL CLOSED** | No attempt without valid credentials |
| ADB device not found / not authorized | **FAIL CLOSED** | Cannot operate without device access |
| Portal TCP unavailable | **FAIL OPEN** (content provider fallback) | Graceful degradation for observation |
| max_steps reached | **FAIL CLOSED** | Safety bound; returns failure |
| LLM returns malformed response | **FAIL CLOSED** | Agent cannot parse action; stops |
| Accessibility Service disabled on device | **FAIL CLOSED** | Portal cannot read UI tree |
| Bitwarden unavailable at startup | **FAIL CLOSED** | Secrets not loaded; DroidRun not started |
| Langfuse unreachable | **FAIL OPEN** | Tracing skipped; agent continues |
| PostHog unreachable | **FAIL OPEN** | Telemetry skipped; agent continues |

---

## 5. Safe Baseline Configuration

For a security-first deployment, apply these settings in `~/.config/droidrun/config.yaml`:

```yaml
agent:
  fast_agent:
    codeact: false
    safe_execution: true
    max_steps: 10        # reduce from default 15 for tighter control
    vision: false        # enable only when needed

  scripter:
    safe_execution: true

device:
  auto_setup: false      # no automatic APK changes

telemetry:
  enabled: false         # no external telemetry

credentials:
  enabled: false         # no stored credentials unless needed
```
