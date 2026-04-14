# Troubleshooting Playbook

Step-by-step debug procedures for the most common DroidRun failure modes.

> **General principle:** Terminal output → ADB logcat → trajectory file → Phoenix traces. Work this sequence before deeper investigation.

---

## 1. `droidrun: command not found`

**Symptoms:** Running `droidrun` in a terminal returns "command not found" or "not recognized".

**Causes and fixes:**

### A. Virtual environment not activated
```powershell
# Activate the venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Then verify
droidrun --version
```

If you used `setup_windows_host.ps1`, the venv is in `.\venv\` relative to the workspace root.

### B. Package not installed in active environment
```powershell
# Confirm which Python/pip is active
Get-Command python | Select-Object Source
pip show droidrun
```

If `pip show droidrun` shows nothing:
```powershell
pip install -e ".[google,anthropic,openai,deepseek,ollama,dev]"
```

### C. Entry point not on PATH
```powershell
# Find where droidrun is installed
pip show -f droidrun | Select-String "droidrun"
```

The entry point should be in the venv's `Scripts\` directory. Ensure that directory is on `$env:PATH`.

---

## 2. Device not found / `adb devices` shows nothing

**Symptoms:** `adb devices` returns empty list or only `List of devices attached`.

### A. ADB not installed
```powershell
adb version
```
If this fails, install Android Platform Tools and add to `PATH`.

### B. USB cable / connection
- Unplug and replug the USB cable.
- Try a different port or cable (some cables are charge-only).
- USB debugging must be enabled: **Settings → Developer Options → USB Debugging → ON**.

### C. Authorization pending
Check the device screen — a dialog "Allow USB Debugging?" must be accepted. Enable "Always allow from this computer".

### D. Wireless ADB — Tailscale not running
For wireless/remote connections:
```powershell
# Verify Tailscale is connected and device IP is reachable
tailscale status
ping 100.71.228.18

# Connect ADB to device
adb connect 100.71.228.18:5555
adb devices
```

If `ping` fails, Tailscale is not connected or the device is offline.

### E. Wrong port after reboot
The wireless ADB port can change after a device reboot. See [Section 5](#5-adb-port-changes-after-reboot) below.

---

## 3. Device shows "unauthorized"

**Symptoms:** `adb devices` shows the device with status `unauthorized`.

**Fix:**
1. On the Android device: **Settings → Developer Options → Revoke USB Debugging Authorizations**.
2. Reconnect the device (USB or wireless).
3. Accept the "Allow USB Debugging?" dialog on the device.
4. Verify:
```powershell
adb devices
# Expected: <serial>  device
```

If the device still shows unauthorized after re-authorization, try:
```powershell
adb kill-server
adb start-server
adb devices
```

---

## 4. Portal not responsive (ping/connection fails)

**Symptoms:** DroidRun reports it cannot reach the Portal, or Portal health check fails.

### A. Portal APK not installed
```powershell
adb shell pm list packages | Select-String "droidrun"
# Expected: package:com.droidrun.portal
```

If missing, install the Portal APK:
```powershell
adb install droidrun-portal.apk
```

Then open the Portal app and follow its setup prompts.

### B. Accessibility Service not enabled (most common cause)

The Portal HTTP server only starts if Accessibility Service is granted. Without it, port 8080 is closed.

On the device:
**Settings → Accessibility → Installed Services → DroidRun Portal → ON**

Confirm it is running — the Portal app should show a green "Active" status.

### C. Port 8080 not forwarded

```powershell
# Forward local port to device
adb forward tcp:8080 tcp:8080

# Verify Portal is listening
curl http://localhost:8080/ping
# Expected: {"status": "ok"} or similar
```

If `adb forward` returns an error, the ADB connection itself may be broken — see Section 2.

### D. Required Android permissions not granted

Portal requires the following to function fully:
| Permission | How to grant |
|---|---|
| Accessibility Service | Settings → Accessibility → DroidRun Portal → ON |
| Battery optimization exemption | Settings → Battery → DroidRun Portal → Unrestricted |
| Notification access | Settings → Notifications → Notification access → DroidRun Portal → ON |
| Overlay permission | Settings → Apps → DroidRun Portal → Display over other apps → ON |
| DroidRun keyboard | Settings → General Management → Keyboard → DroidRun Keyboard → ON |

---

## 5. ADB Port Changes After Reboot

**Symptoms:** ADB wireless connection worked before, but the device is unreachable after a reboot.

Android assigns a new random port for ADB over TCP after each reboot. Fix:

### Discover new port
```powershell
.\scripts\adb_find_port.ps1
```

This script scans for the device and outputs the current port.

### Lock port to 5555 (persistent until next reboot)
```powershell
# Connect via USB first, then lock the TCP port
adb tcpip 5555
adb connect 100.71.228.18:5555
```

To make this permanent across reboots, `adb tcpip 5555` must be run after each reboot while connected via USB, or use a Tasker/automation script on the device.

---

## 6. Vision Mode Fails (`image_url` error)

**Symptoms:** Agent fails with an error referencing `image_url` not supported, or model returns an error on vision tasks.

**Cause:** The configured model does not support image inputs. DeepSeek's text models, for example, do not accept vision input.

**Fix:** Switch to a vision-capable model for tasks requiring screenshots:

```yaml
# config.yaml
llm:
  model: gemini/gemini-2.0-flash      # Google Gemini (vision capable)
  # or
  model: openrouter/google/gemini-2.0-flash-exp
```

OpenRouter can route to many vision-capable models. DeepSeek is suitable for text/code tasks only.

---

## 7. API Key Not Found

**Symptoms:** DroidRun starts but immediately fails with "API key not set", "authentication failed", or similar provider error.

### A. `startup_droidrun.ps1` not run in this session
```powershell
.\startup_droidrun.ps1
```

Windows environment variables set via `SetEnvironmentVariable("User")` are visible to new processes but not to an already-open terminal. Close and reopen the terminal after running the startup script, or source it in-session.

### B. BWS token expired or invalid
```powershell
# Test bws access manually
$env:BWS_ACCESS_TOKEN = "<your token>"
bws secret list
```

If this fails with an auth error, the machine account token has expired. Rotate it — see `docs/secrets-handling.md#rotating-the-bws-machine-account-token`.

### C. Env var not in current process
```powershell
# Check if the key is visible to the current shell
$env:OPENAI_API_KEY       # or whichever key
echo $env:DROIDRUN_DEEPSEEK_KEY
```

If empty, the startup script either wasn't run or its output didn't propagate. Re-run `startup_droidrun.ps1` in the current shell.

### D. `.env` file missing or wrong path
DroidRun also loads `~/.config/droidrun/.env`. Verify it exists and contains the needed key:
```powershell
Get-Content "$env:USERPROFILE\.config\droidrun\.env"
```

---

## 8. MCP Server Not Appearing in AI Client

**Symptoms:** Claude Desktop / Cursor / other AI client doesn't show DroidRun tools, or MCP connection fails.

### A. AI client not restarted after config change
Fully quit and relaunch the AI client after any change to `mcp.json`.

### B. Incorrect path in `mcp.json`
```json
{
  "mcpServers": {
    "droidrun": {
      "command": "powershell",
      "args": ["-File", "D:\\github\\droidrun\\scripts\\start_mcp_server.ps1"]
    }
  }
}
```

Verify the path in `args` points to the correct `start_mcp_server.ps1`. Use absolute paths with escaped backslashes.

### C. MCP server script failing silently
```powershell
# Run it manually to see errors
.\scripts\start_mcp_server.ps1
```

Watch for Python errors, missing venv, or import failures. Fix the error, then restart the AI client.

---

## 9. "More Than One Device" Error

**Symptoms:** ADB commands fail with "error: more than one device/emulator".

**Cause:** Multiple ADB devices are connected (e.g., USB + wireless, or multiple emulators).

**Fix:** Specify the target device explicitly:
```powershell
# List devices and find the serial
adb devices

# Use -s flag with the target serial
adb -s 100.71.228.18:5555 shell

# Or set ANDROID_SERIAL for the session
$env:ANDROID_SERIAL = "100.71.228.18:5555"
```

In DroidRun config:
```yaml
device:
  serial: "100.71.228.18:5555"
```

---

## 10. Agent Loops or Hits `max_steps`

**Symptoms:** Task runs until `max_steps` is reached without completing, or the agent repeats the same action in a loop.

### A. Increase `max_steps`
```yaml
agent:
  max_steps: 50    # default is usually 20-30
```

### B. Enable reasoning mode
Some models perform better on complex tasks when reasoning is enabled:
```yaml
llm:
  model: openrouter/google/gemini-2.0-flash-thinking-exp
```

### C. Check Portal responsiveness
A looping agent often means the Portal is not reporting state correctly:
```powershell
curl http://localhost:8080/ping
curl http://localhost:8080/state
```

If these fail, resolve Portal connectivity first (see Section 4).

### D. Reduce task scope
Break the task into smaller, more specific sub-tasks and run them sequentially.

---

## 11. Trajectory Not Saved

**Symptoms:** Run completes but no file appears in `trajectories/`.

### A. Check config
```yaml
logging:
  save_trajectory: step   # must not be "none"
  trajectory_path: trajectories/
```

### B. Check directory permissions
```powershell
# Verify the trajectories directory exists and is writable
Test-Path trajectories
New-Item -ItemType Directory -Force -Path trajectories
```

### C. Verify the path is relative to the working directory
If `trajectory_path` is a relative path, it resolves relative to where `droidrun` is invoked. Use an absolute path to avoid ambiguity:
```yaml
logging:
  trajectory_path: "D:/github/droidrun/trajectories/"
```

---

## 12. `bws` CLI Errors

**Symptoms:** `startup_droidrun.ps1` fails with bws errors; secrets not injected.

### A. `bws` not on PATH
```powershell
Get-Command bws
```

If not found, install the Bitwarden Secrets Manager CLI and add it to `PATH`. See [bitwarden.com/products/secrets-manager](https://bitwarden.com/products/secrets-manager/).

### B. Access token not set
```powershell
echo $env:BWS_ACCESS_TOKEN
```

If empty, retrieve the token from the Bitwarden vault entry `BWS_DROIDRUN_TOKEN` and set it:
```powershell
$env:BWS_ACCESS_TOKEN = "<token from vault>"
```

### C. Machine account lacks access to secret IDs
The `droidrun-windows` machine account must have read access to the specific secret IDs (DeepSeek: `14d69c11-...`, OpenRouter: `f9ed80a7-...`). Verify in the Bitwarden Secrets Manager web UI under **Machine Accounts → droidrun-windows → Access**.

### D. Token expired
Machine account tokens have a configurable TTL. If expired:
1. Generate a new token in Bitwarden Secrets Manager.
2. Update `BWS_DROIDRUN_TOKEN` in the regular Bitwarden vault.
3. Set it in the current session and re-run `startup_droidrun.ps1`.

---

## General Debug Checklist

When nothing above resolves the issue, work through this sequence:

```
[ ] droidrun --version  → confirms package is installed
[ ] adb devices         → confirms device is connected and authorized
[ ] curl http://localhost:8080/ping  → confirms Portal is running
[ ] echo $env:OPENAI_API_KEY        → confirms key is in environment
[ ] droidrun --debug <command>      → full verbose output
[ ] adb logcat | Select-String "DroidRun"  → device-side logs
[ ] open trajectories/<latest>.json → step-by-step replay
[ ] open http://localhost:6006      → Phoenix traces for LLM call details
```

---

## Related Files

- `docs/logging-observability.md` — where to find logs and traces
- `docs/secrets-handling.md` — API key storage and rotation
- `docs/build-release-process.md` — installation and build steps
- `README_REMOTE_SETUP.md` — Tailscale + wireless ADB setup
