# DroidRun Architecture Overview

**Last updated:** 2026-03-15  
**Status:** Fully operational

---

## System Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    WINDOWS PC (chaoscentral)                 │
│                                                             │
│  Cursor / OpenClaw / Claude Desktop                         │
│       │                                                     │
│       │ MCP protocol (stdin/stdout JSON-RPC)                │
│       ▼                                                     │
│  mcp_server.py          ← DroidRun MCP server               │
│  (tools: phone_do,          started by start_mcp_server.ps1 │
│   phone_ping, phone_apps)                                   │
│       │                                                     │
│       │ subprocess call                                     │
│       ▼                                                     │
│  .venv\Scripts\droidrun.exe                                 │
│       │                                                     │
│       │ ADB over Tailscale WireGuard tunnel                 │
│       │ (port 5555, fixed via adb tcpip 5555)               │
│       ▼                                                     │
│  100.71.228.18:5555 ──────────────────────────────────────► │
│                                          SAMSUNG S25 ULTRA  │
│                                          Android 16         │
│                                          DroidRun Portal    │
│                                          v0.6.1             │
│                                          Accessibility ON   │
└─────────────────────────────────────────────────────────────┘
```

---

## File Structure

```
D:\github\droidrun\
├── src\                              ← DroidRun source (github.com/droidrun/droidrun)
├── .venv\                            ← Python 3.12.10 virtual environment
│   └── Scripts\droidrun.exe         ← CLI entry point
├── mcp_server.py                     ← MCP server (phone_do / phone_ping / phone_apps)
├── docs\
│   ├── architecture_overview.md     ← THIS FILE
│   └── ai\STATE.md                  ← Session state tracker
├── scripts\
│   ├── droidrun_run.ps1             ← MAIN: run AI tasks on phone
│   ├── reconnect_remote.ps1         ← MAIN: reconnect after reboot
│   ├── store_api_keys_to_env.ps1    ← Run after Cursor restart / key rotation
│   ├── start_mcp_server.ps1         ← Called by Cursor/OpenClaw/Claude Desktop
│   ├── adb_find_port.ps1            ← Auto-discover wireless debug port
│   ├── adb_status.ps1               ← Check ADB connection status
│   ├── droidrun_ping.ps1            ← Ping DroidRun Portal
│   ├── adb_connect_tailscale.ps1    ← Manual Tailscale connect
│   ├── adb_connect_wifi.ps1         ← Manual local Wi-Fi connect
│   ├── adb_pair_wifi.ps1            ← Pair new device over Wi-Fi (one-time)
│   └── setup_windows_host.ps1       ← Full host setup from scratch
└── README_REMOTE_SETUP.md           ← End-user setup guide
```

---

## Device Information

| Property | Value |
|----------|-------|
| Device | Samsung Galaxy S25 Ultra (Anthony's S25 Ultra) |
| Model | SM-S938U |
| Android | 16 |
| USB Serial | R5CY51LWKCR |
| Wi-Fi IP | 192.168.1.120 |
| Tailscale IP | 100.71.228.18 (stable — does not change) |
| ADB Port | 5555 (fixed via `adb tcpip 5555`, resets on reboot) |
| ADB Forward | `adb -s 100.71.228.18:5555 forward tcp:8080 tcp:8080` |
| DroidRun Portal | v0.6.1 |
| Tailscale Account | ynotfins@ |

---

## Software Versions

| Software | Version | Location |
|----------|---------|----------|
| Python | 3.12.10 | system PATH |
| DroidRun | 0.5.1 | D:\github\droidrun\src\ |
| DroidRun Portal (APK) | 0.6.1 | installed on phone |
| ADB | 1.0.41 (36.0.0) | C:\platform-tools\adb.exe |
| Tailscale (PC) | 1.94.2 | system |
| Bitwarden CLI (bw) | 2026.2.0 | system PATH |
| Bitwarden Secrets CLI (bws) | 2.0.0 | system PATH |

---

## Secret Names, Locations & Injection

### Bitwarden Secrets Manager (bws)
Secrets Manager organization: **R3lentlessGrind**  
Project: **DroidRun**  
Machine account: **droidrun-windows** (access token stored in Password Manager)

| Secret Name | Secret ID | Purpose |
|-------------|-----------|---------|
| `DEEPSEEK_API_KEY` | `14d69c11-99ba-428f-a656-b40e014e72ae` | DeepSeek API for non-vision tasks |
| `OPENROUTER_API_KEY` | `f9ed80a7-fc35-4add-96d6-b40e0163b041` | OpenRouter API for vision tasks (Gemini) |

### Bitwarden Password Manager (bw)

| Item Name | Purpose |
|-----------|---------|
| `BWS_DROIDRUN_TOKEN` | Machine account access token for `droidrun-windows` in Secrets Manager. Stored in Password field. Used by `bw get item BWS_DROIDRUN_TOKEN` to bootstrap `bws`. |

### Windows User Environment Variables
Stored in Windows registry at `HKCU\Environment` (encrypted by Windows, survives reboots).  
Set by running: `.\scripts\store_api_keys_to_env.ps1`

| Variable Name | Source Secret | Used By |
|---------------|--------------|---------|
| `DROIDRUN_DEEPSEEK_KEY` | `DEEPSEEK_API_KEY` from Secrets Manager | `droidrun_run.ps1`, `mcp_server.py` |
| `DROIDRUN_OPENROUTER_KEY` | `OPENROUTER_API_KEY` from Secrets Manager | `droidrun_run.ps1`, `mcp_server.py` |

### Secret Injection Flow

```
Bitwarden Password Manager
  └── BWS_DROIDRUN_TOKEN
        │ retrieved via: bw get item "BWS_DROIDRUN_TOKEN"
        │ sets: $env:BWS_ACCESS_TOKEN
        ▼
Bitwarden Secrets Manager (bws)
  └── DEEPSEEK_API_KEY    (ID: 14d69c11-...)
  └── OPENROUTER_API_KEY  (ID: f9ed80a7-...)
        │ retrieved via: bws secret get <ID>
        │ stored as: Windows user env vars
        ▼
Windows User Environment (HKCU\Environment)
  └── DROIDRUN_DEEPSEEK_KEY
  └── DROIDRUN_OPENROUTER_KEY
        │ read by mcp_server.py and droidrun_run.ps1
        │ injected as process-scoped env vars
        ▼
droidrun.exe process
  └── DEEPSEEK_API_KEY or OPENAI_API_KEY (set at runtime, cleared after task)
```

> **Security rule:** API key values are NEVER stored in config files, scripts, or git.  
> The `store_api_keys_to_env.ps1` script must be re-run after any key rotation.

---

## MCP Servers Added

DroidRun is registered as an MCP server in three clients. All use the same command.

### MCP Server Entry (identical across all three clients)

```json
"droidrun": {
  "command": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
  "args": [
    "-NonInteractive",
    "-File",
    "D:\\github\\droidrun\\scripts\\start_mcp_server.ps1"
  ],
  "transport": "stdio"
}
```

### Client Config File Locations

| Client | Config File | Section |
|--------|-------------|---------|
| **Cursor** | `C:\Users\ynotf\.cursor\mcp.json` | `mcpServers.droidrun` |
| **OpenClaw** | `C:\Users\ynotf\.openclaw\openclaw.json` | `mcpServers.droidrun` |
| **Claude Desktop** | `C:\Users\ynotf\AppData\Roaming\Claude\claude_desktop_config.json` | `mcpServers.droidrun` |

### MCP Server Startup Flow

```
Client app starts
  │
  ├─ spawns: pwsh.exe -NonInteractive -File start_mcp_server.ps1
  │             (all stdout reserved for JSON-RPC, no output from script)
  │
  └─ start_mcp_server.ps1 executes:
       └─ .venv\Scripts\python.exe mcp_server.py
            │ reads DROIDRUN_DEEPSEEK_KEY and DROIDRUN_OPENROUTER_KEY
            │ from Windows user environment
            │
            └─ exposes 3 tools via MCP stdio:
                 ├── phone_do(task, vision=false)
                 ├── phone_ping()
                 └── phone_apps()
```

### MCP Tools Exposed

| Tool | Parameters | Description |
|------|-----------|-------------|
| `phone_do` | `task` (string, required), `vision` (bool, default false) | Run any natural language task on the phone |
| `phone_ping` | none | Check phone + Portal connectivity |
| `phone_apps` | none | List installed apps on phone |

---

## AI Provider Logic

| Flag | Provider name | LlamaIndex class | Model | API endpoint |
|------|--------------|-----------------|-------|-------------|
| *(no vision)* | DeepSeek | `DeepSeek` | `deepseek-chat` | api.deepseek.com |
| `-Vision` | OpenRouter | `OpenAILike` | `google/gemini-2.0-flash-001` | openrouter.ai/api/v1 |

> **Why `OpenAILike` for OpenRouter?**  
> DroidRun's `OpenAI` provider validates model names against a hardcoded OpenAI list.  
> `OpenAILike` skips validation and accepts any model name, making it compatible with  
> OpenRouter, which routes to hundreds of models using the same OpenAI API format.

---

## Network Security

- ADB port 5555 is bound to the phone's network interface
- Only reachable via Tailscale's WireGuard tunnel (end-to-end encrypted)
- Phone uses private home Wi-Fi or cellular — never public networks
- ADB is never exposed to the public internet
- Tailscale account: `ynotfins@` — both PC and phone enrolled

---

## Tailscale Network

| Device | Tailscale IP | Status |
|--------|-------------|--------|
| chaoscentral (PC) | 100.111.111.124 | always online |
| samsung-sm-s938u (phone) | 100.71.228.18 | online when Tailscale app running |
| verizon-router (old, ignore) | 100.80.253.19 | offline, unused |

---

## Reconstruct From Scratch

1. Clone source: `git clone https://github.com/droidrun/droidrun.git src`
2. Create venv: `python -m venv .venv`
3. Install: `.venv\Scripts\python.exe -m pip install -e "src[google,anthropic,openai,deepseek,ollama,dev]"`
4. Verify ADB: `adb version` (already at `C:\platform-tools`)
5. Connect phone via USB → unlock screen → tap **Allow** on USB debugging dialog (check "Always allow")
6. Fix ADB port: `adb tcpip 5555` → `adb connect 100.71.228.18:5555`
7. Install Portal: `droidrun setup`
8. Enable accessibility: Settings → Accessibility → DroidRun Portal → ON
9. Forward port: `adb -s 100.71.228.18:5555 forward tcp:8080 tcp:8080`
10. Verify: `droidrun ping -d 100.71.228.18:5555`
11. Bitwarden: create DroidRun project in Secrets Manager, add DEEPSEEK_API_KEY + OPENROUTER_API_KEY
12. Create machine account `droidrun-windows`, grant DroidRun project access, generate access token
13. Save token to Password Manager as `BWS_DROIDRUN_TOKEN`
14. Add MCP entry to `~/.cursor/mcp.json`, `~/.openclaw/openclaw.json`, `%APPDATA%\Claude\claude_desktop_config.json`
15. Run: `.\scripts\store_api_keys_to_env.ps1`

---

## OpenClaw System Prompt (for onboarding OpenClaw)

> You have a new MCP tool available called **droidrun** with 3 tools:
>
> **`phone_do`** — Controls Anthony's Samsung Galaxy S25 Ultra using natural language. The AI agent will physically operate the phone (open apps, tap, type, swipe, read screen content). Parameters: `task` (string, required) and `vision` (boolean, optional — set true when you need to read what's on screen).
>
> **`phone_ping`** — Checks if the phone and DroidRun Portal are connected and responsive. No parameters.
>
> **`phone_apps`** — Lists all user-installed apps on the phone. No parameters.
>
> **How to use it:**
> - "Open YouTube on my phone" → call `phone_do` with task="Open YouTube"
> - "What's on my phone screen right now?" → call `phone_do` with task="Tell me what's on screen" and vision=true
> - "Is my phone connected?" → call `phone_ping`
> - "What apps do I have installed?" → call `phone_apps`
>
> The phone is a dedicated automation device (Samsung Galaxy S25 Ultra, Android 16) connected via Tailscale. It is safe to use at any time. Vision mode uses Gemini 2.0 Flash via OpenRouter. Non-vision mode uses DeepSeek. Always try without vision first unless you need to read the screen.

---

## Daily Workflow

```
Morning startup:
  .\scripts\reconnect_remote.ps1           ← if phone was rebooted
  .\scripts\droidrun_run.ps1 -Task "..."   ← run tasks

After Cursor restart:
  .\scripts\store_api_keys_to_env.ps1      ← re-cache keys to Windows env

After phone reboot (port 5555 resets):
  .\scripts\reconnect_remote.ps1           ← auto-finds port, re-locks to 5555

Key rotation:
  (update keys in Bitwarden Secrets Manager)
  .\scripts\store_api_keys_to_env.ps1      ← re-cache new values
```
