# DroidRun — Secure Remote Setup Guide

**Platform:** Windows 10/11 | **Device:** Samsung Galaxy S25 Ultra  
**Security model:** ADB never exposed to public internet — Tailscale VPN only.

---

## Table of Contents

1. [Installation](#installation)
2. [Phone Setup (USB)](#phone-setup-usb)
3. [DroidRun Portal Setup](#droidrun-portal-setup)
4. [Wi-Fi Wireless Debugging](#wi-fi-wireless-debugging)
5. [Tailscale Remote Workflow](#tailscale-remote-workflow)
6. [MCP Server Setup](#mcp-server-setup)
7. [Daily Commands](#daily-commands)
8. [PowerShell Scripts Reference](#powershell-scripts-reference)
9. [Troubleshooting](#troubleshooting)
10. [Device Information](#device-information)

---

## Installation

### Prerequisites
- Python 3.11–3.13 (3.12.10 installed)
- ADB (platform-tools) — installed at `C:\platform-tools\`
- Git
- Bitwarden CLI (`bw`) and Bitwarden Secrets CLI (`bws`) — installed at system PATH
- Tailscale 1.94.2

### Directory Structure

```
D:\github\droidrun\
├── src\                          ← DroidRun source (cloned from GitHub)
├── .venv\                        ← Python virtual environment
├── mcp_server.py                 ← MCP server exposing phone tools to AI clients
├── scripts\                      ← PowerShell automation scripts
├── docs\architecture_overview.md ← Full system architecture reference
└── README_REMOTE_SETUP.md        ← This file
```

### Setup Steps

```powershell
cd D:\github\droidrun

# Clone DroidRun source (already done)
git clone https://github.com/droidrun/droidrun.git src

# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Upgrade tools
python -m pip install --upgrade pip setuptools wheel

# Install DroidRun with all providers
pip install -e "src[google,anthropic,openai,deepseek,ollama,dev]"

# Verify
droidrun --help
```

Or simply run the setup script:
```powershell
.\scripts\setup_windows_host.ps1
```

---

## Phone Setup (USB)

### 1. Enable Developer Options
1. **Settings → About phone → Software information**
2. Tap **Build number** 7 times rapidly
3. Enter your PIN/password when prompted
4. "Developer mode enabled" toast appears

### 2. Enable USB Debugging
1. **Settings → Developer options**
2. Toggle **USB debugging** → ON
3. Confirm the warning dialog

### 3. Connect via USB & Authorize
1. Connect phone to PC via USB cable
2. **Unlock the phone screen**
3. A dialog appears: **"Allow USB debugging?"**
4. Check ✅ **"Always allow from this computer"**
5. Tap **Allow**

### 4. Verify Connection
```powershell
adb devices
# Expected: R5CY51LWKCR    device
```

---

## DroidRun Portal Setup

After USB authorization:

```powershell
# Activate venv first
.venv\Scripts\Activate.ps1

# Run setup (downloads + installs Portal APK)
droidrun setup
```

### Phone-side steps required after `droidrun setup`:

1. **Enable Accessibility Service:**
   - Settings → Accessibility → Installed services
   - Find **DroidRun Portal** → Toggle ON → tap Allow

2. **Enable HTTP Server in Portal app:**
   - Open DroidRun Portal app → Settings (gear icon)
   - Toggle **HTTP Server (REST)** → ON (port 8080)
   - This is what ADB connects to — must be ON

3. **Enable DroidRun Keyboard (optional but recommended):**
   - In Portal main screen, tap **SELECT** next to keyboard warning
   - Enable DroidRun Portal as an input method
   - Improves typing reliability in forms and search boxes

4. **Disable the overlay (cleaner experience):**
   - Portal main screen → Controls → Toggle **Overlay** → OFF
   - AI still works fully without the visual overlay

5. **Set Battery to Unrestricted:**
   - Settings → Apps → DroidRun Portal → Battery → Unrestricted
   - Prevents Samsung OneUI from killing the Portal in background

6. **Fix ADB port to 5555 (prevents random port changes):**
```powershell
adb tcpip 5555
adb connect 100.71.228.18:5555
adb forward tcp:8080 tcp:8080
```

### Verify Portal is running:
```powershell
droidrun ping -d 100.71.228.18:5555
# Expected: Portal is installed and accessible. You're good to go!
```

---

## Wi-Fi Wireless Debugging

This allows ADB connection **without the USB cable**.

### One-Time Pairing

#### Step 1: Enable Wireless Debugging on phone
1. **Settings → Developer options → Wireless debugging**
2. Toggle **ON**
3. Note the port shown (e.g., `100.71.228.18:XXXXX`)

#### Step 2: Get pairing code
1. Tap **"Pair device with pairing code"**
2. Note the 6-digit code and pairing port

#### Step 3: Pair from PC
```powershell
adb pair 192.168.1.120:PAIR_PORT PAIR_CODE
```
Or use the script:
```powershell
.\scripts\adb_pair_wifi.ps1 -PhoneIP 192.168.1.120 -PairPort 38291 -PairCode 123456
```

#### Step 4: Lock to fixed port 5555
```powershell
adb -s <device> tcpip 5555
adb connect 100.71.228.18:5555
adb forward tcp:8080 tcp:8080
```

> **Port 5555 resets on phone reboot.** Run `.\scripts\reconnect_remote.ps1` to restore it automatically.

---

## Tailscale Remote Workflow

Secure remote control from anywhere — ADB never exposed to the public internet.

### Setup (One-Time)

1. **Install Tailscale on Windows PC:**
```powershell
winget install Tailscale.Tailscale
```

2. **Install Tailscale on Android Phone:** Play Store → search **Tailscale**

3. **Log in to the same account on both devices** (account: `ynotfins@`)

4. **Verify both devices appear:**
```powershell
tailscale status
# samsung-sm-s938u  100.71.228.18  online
# chaoscentral      100.111.111.124  online
```

5. **Connect ADB via Tailscale:**
```powershell
adb connect 100.71.228.18:5555
adb forward tcp:8080 tcp:8080
droidrun ping -d 100.71.228.18:5555
```

### Security Notes
- ADB only reachable via Tailscale's WireGuard tunnel (end-to-end encrypted)
- Phone uses private home Wi-Fi or cellular — never exposed to public internet
- Port 5555 is not open to the internet — Tailscale handles all routing

---

## MCP Server Setup

DroidRun is exposed as an MCP server so Cursor, OpenClaw, and Claude Desktop can control the phone directly through conversation.

### MCP Tools Available

| Tool | Parameters | What it does |
|------|-----------|-------------|
| `phone_do` | `task` (string), `vision` (bool, default false) | Run any natural language task on the phone |
| `phone_ping` | none | Check phone + DroidRun Portal connectivity |
| `phone_apps` | none | List all user-installed apps on phone |

### Config added to all three clients

```json
"droidrun": {
  "command": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
  "args": ["-NonInteractive", "-File", "D:\\github\\droidrun\\scripts\\start_mcp_server.ps1"],
  "transport": "stdio"
}
```

| Client | Config file |
|--------|------------|
| Cursor | `C:\Users\ynotf\.cursor\mcp.json` |
| OpenClaw | `C:\Users\ynotf\.openclaw\openclaw.json` |
| Claude Desktop | `C:\Users\ynotf\AppData\Roaming\Claude\claude_desktop_config.json` |

### First-time and post-restart requirement
```powershell
.\scripts\store_api_keys_to_env.ps1
```
This fetches API keys from Bitwarden Secrets Manager and stores them as Windows user environment variables so the MCP server can start without prompting for credentials.

---

## Daily Commands

### Run an AI task on the phone (no vision — fast, cheap)
```powershell
.\scripts\droidrun_run.ps1 -Task "Open YouTube and search for the news"
```

### Run an AI task with vision (AI can see the screen)
```powershell
.\scripts\droidrun_run.ps1 -Task "Tell me what's on screen" -Vision
```

### Use a specific model
```powershell
.\scripts\droidrun_run.ps1 -Task "Book an Uber" -Vision -Model "anthropic/claude-3-5-sonnet"
```

### Smart reconnect (after reboot or connection drop)
```powershell
.\scripts\reconnect_remote.ps1
```

### Check phone connection status
```powershell
.\scripts\adb_status.ps1
```

### Ping DroidRun Portal
```powershell
.\scripts\droidrun_ping.ps1
```

### After Cursor restart (re-cache API keys)
```powershell
.\scripts\store_api_keys_to_env.ps1
```

---

## PowerShell Scripts Reference

### `droidrun_run.ps1` ⭐ Main script
**When to use:** Every time you want the AI to do something on your phone.

Fetches API keys from Bitwarden Secrets Manager via the BWS machine account token, injects them into memory (never written to disk), connects to the phone over Tailscale, forwards the DroidRun port, and runs the task. Automatically selects DeepSeek (no vision) or OpenRouter/Gemini (vision) based on the `-Vision` flag.

```powershell
.\scripts\droidrun_run.ps1 -Task "Open the camera"
.\scripts\droidrun_run.ps1 -Task "Read my notifications" -Vision
.\scripts\droidrun_run.ps1 -Task "Search YouTube" -Vision -Model "openai/gpt-4o"
.\scripts\droidrun_run.ps1 -Task "Turn on DND" -Steps 10
```

Parameters: `-Task` (required), `-Vision` (switch), `-Model` (default: auto), `-Device` (default: `100.71.228.18:5555`), `-Steps` (default: 30), `-Reasoning` (switch)

---

### `reconnect_remote.ps1` ⭐ Daily use after reboot
**When to use:** After the phone reboots, after a connection drop, or when `droidrun_run.ps1` says device not found.

Tries reconnection in order: existing connection → USB → Wi-Fi (`192.168.1.120`) → Tailscale (`100.71.228.18`). If all fail, runs `adb_find_port.ps1` to scan for the new wireless debug port, then re-locks ADB to port 5555. Updates all scripts with the new port automatically.

```powershell
.\scripts\reconnect_remote.ps1
```

---

### `store_api_keys_to_env.ps1` ⭐ After Cursor restart
**When to use:** After restarting Cursor, after rotating API keys in Bitwarden, or when MCP server reports missing API keys.

Unlocks the Bitwarden vault, fetches `DEEPSEEK_API_KEY` and `OPENROUTER_API_KEY` from Bitwarden Secrets Manager using the `BWS_DROIDRUN_TOKEN` machine account, and stores them as Windows user environment variables (`DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY`) encrypted in the Windows registry. These persist across reboots and are read by both `droidrun_run.ps1` and the MCP server.

```powershell
.\scripts\store_api_keys_to_env.ps1
```

---

### `start_mcp_server.ps1` — Auto-launched, never run manually
**When to use:** Never run directly. Called automatically by Cursor, OpenClaw, and Claude Desktop when they start the DroidRun MCP server.

Starts `mcp_server.py` using the `.venv` Python interpreter. All stdout is reserved for MCP JSON-RPC communication — the script itself produces no stdout output to avoid corrupting the protocol.

---

### `adb_find_port.ps1` — Troubleshooting
**When to use:** When the wireless debug port changed (phone rebooted and port 5555 wasn't restored) and `reconnect_remote.ps1` couldn't fix it automatically.

Scans the Tailscale IP (`100.71.228.18`) across the port range 37000–47000, finds the open ADB port, connects to it, re-locks ADB to port 5555 via `adb tcpip 5555`, and updates the default port in `droidrun_run.ps1` and `reconnect_remote.ps1`.

```powershell
.\scripts\adb_find_port.ps1
# Optional: specify different IP or port range
.\scripts\adb_find_port.ps1 -TailscaleIP 100.71.228.18 -StartPort 37000 -EndPort 47000
```

---

### `adb_status.ps1` — Diagnostic
**When to use:** To quickly check what ADB devices are connected, their authorization status, and phone model/Android version.

Shows a summary table of connected, unauthorized, and offline devices with a plain-English fix suggestion for each problem state.

```powershell
.\scripts\adb_status.ps1
```

---

### `droidrun_ping.ps1` — Diagnostic
**When to use:** To verify the DroidRun Portal is installed, running, and reachable before running a task. Useful for confirming the phone is ready after reconnecting.

Checks for an authorized ADB device, then calls `droidrun ping` and reports whether the Portal is reachable or gives a fix checklist if not.

```powershell
.\scripts\droidrun_ping.ps1
```

---

### `adb_connect_tailscale.ps1` — Manual Tailscale connect
**When to use:** When you want to manually connect to a specific Tailscale IP and port (bypassing the auto-reconnect logic). Also forwards port 8080 and pings DroidRun after connecting.

```powershell
.\scripts\adb_connect_tailscale.ps1 -TailscaleIP 100.71.228.18 -AdbPort 5555
```

---

### `adb_connect_wifi.ps1` — Manual local Wi-Fi connect
**When to use:** When you want to connect over local Wi-Fi specifically (not Tailscale). Useful if Tailscale is down or you want to verify local connectivity separately.

```powershell
.\scripts\adb_connect_wifi.ps1 -PhoneIP 192.168.1.120 -AdbPort 5555
```

---

### `adb_pair_wifi.ps1` — One-time pairing
**When to use:** Only needed when adding a new PC to the phone's trusted wireless debugging list, or if all ADB authorizations were revoked. Requires the 6-digit pairing code from the phone's Wireless debugging screen.

```powershell
.\scripts\adb_pair_wifi.ps1 -PhoneIP 192.168.1.120 -PairPort 38291 -PairCode 123456
```

---

### `setup_windows_host.ps1` — Fresh install only
**When to use:** Only when rebuilding this setup from scratch on a new PC. Checks for ADB, creates the `.venv`, and installs DroidRun with all provider extras.

```powershell
.\scripts\setup_windows_host.ps1
```

---

## Troubleshooting

### Device shows as `unauthorized`
**Fix:**
1. Unlock the phone screen
2. Look for "Allow USB debugging?" dialog — check "Always allow" and tap Allow
3. If dialog doesn't appear: Settings → Developer options → Revoke USB debugging authorizations → re-connect

### Port 5555 stopped working after reboot
```powershell
.\scripts\reconnect_remote.ps1
```
If that fails:
```powershell
.\scripts\adb_find_port.ps1
```

### `droidrun ping` fails (Portal not reachable)
1. Open DroidRun Portal app → Settings → toggle **HTTP Server (REST)** ON
2. Run: `adb forward tcp:8080 tcp:8080`
3. Check accessibility: Settings → Accessibility → DroidRun Portal → ON
4. Check battery: Settings → Apps → DroidRun Portal → Battery → Unrestricted

### MCP server not working in Cursor/OpenClaw
1. Run `.\scripts\store_api_keys_to_env.ps1` to re-cache API keys
2. Restart the client app
3. Check `DROIDRUN_DEEPSEEK_KEY` exists: `[System.Environment]::GetEnvironmentVariable('DROIDRUN_DEEPSEEK_KEY','User')`

### DeepSeek vision error (`unknown variant image_url`)
DeepSeek does not support vision. Use the `-Vision` flag which automatically switches to OpenRouter/Gemini:
```powershell
.\scripts\droidrun_run.ps1 -Task "Read screen" -Vision
```

### Tailscale not connecting
1. `tailscale status` — verify both devices show online
2. Open Tailscale app on phone — ensure it's connected
3. `tailscale ping 100.71.228.18` — test tunnel

### Battery optimizer killing DroidRun Portal
- Settings → Apps → DroidRun Portal → Battery → **Unrestricted**
- Settings → Battery → Background usage limits → DroidRun Portal → **Unrestricted**

---

## Device Information

| Property | Value |
|----------|-------|
| Device | Samsung Galaxy S25 Ultra (Anthony's S25 Ultra) |
| Model | SM-S938U |
| Android | 16 |
| USB Serial | R5CY51LWKCR |
| Wi-Fi IP | 192.168.1.120 |
| Tailscale IP | 100.71.228.18 (stable — never changes) |
| ADB Port | 5555 (fixed — resets on phone reboot) |
| ADB Forward | `adb -s 100.71.228.18:5555 forward tcp:8080 tcp:8080` |
| DroidRun Portal | v0.6.1 |
| ADB | 1.0.41 (36.0.0) at C:\platform-tools\ |
| Python | 3.12.10 |
| DroidRun | 0.5.1 |
| Workspace | D:\github\droidrun\ |
| Source | D:\github\droidrun\src\ |
| Virtual Env | D:\github\droidrun\.venv\ |
| Tailscale Account | ynotfins@ |
| Bitwarden machine account | droidrun-windows |
