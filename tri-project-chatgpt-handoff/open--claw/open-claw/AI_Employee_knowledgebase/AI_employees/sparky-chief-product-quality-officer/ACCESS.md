# Sparky's Executive Access Model

**Document Role:** This file defines Sparky's **persistent access configuration and recovery procedures**. For exec routing examples, see `TOOLS.md`. For full tool inventory, see `COMPLETE_TOOL_REFERENCE.md`.

## Access Status: PERSISTENT & UNRESTRICTED

Sparky's full executive permissions are **permanently configured** in the OpenClaw runtime configuration at `~/.openclaw/openclaw.json`. No special activation, tokens, or credentials are required. Access persists across restarts.

## Access Matrix

| Resource | Permission Level | Configuration Source | Requires Action? |
|---|---|---|---|
| **WSL (Linux gateway)** | Full unrestricted exec | `tools.exec.security: "full"` | ❌ No — automatic |
| **Windows Desktop** | Full system access | `tools.exec.node: "Windows Desktop"` | ❌ No — automatic |
| **Docker** | Full access | Via gateway or node exec | ❌ No — automatic |
| **Elevated/sudo** | Enabled | `tools.elevated.enabled: true` | ✅ Yes — `/elevated` directive in Telegram |
| **All MCP Tools** | Full access | Global MCP config | ❌ No — automatic |

## How Access Works

### No Action Required for Standard Operations

Sparky automatically has:
- ✅ Full command execution on WSL gateway (`exec` commands run unrestricted)
- ✅ Full system access on Windows Desktop (`exec --host node` commands run unrestricted)
- ✅ Docker access from both hosts
- ✅ All 12 MCP servers/tools available
- ✅ No approval prompts or allowlists

### When Elevated Access Is Needed

For `sudo` commands on Linux or admin commands on Windows:

**Telegram Only** (Tony's account: `6873660400`):
```
/elevated
```

After `/elevated` directive, all subsequent `exec` commands run with elevated privileges until the conversation ends.

**NOT available in other channels** (WhatsApp, web, voice) — elevated mode is Telegram-exclusive.

## Persistent Configuration Details

### Exec Security (from `~/.openclaw/openclaw.json`)

```json
{
  "tools": {
    "exec": {
      "host": "gateway",          // Default: WSL Ubuntu
      "security": "full",          // ✅ NO command restrictions
      "node": "Windows Desktop"    // ✅ Windows paired & connected
    },
    "elevated": {
      "enabled": true,              // ✅ Sudo/admin allowed
      "allowFrom": {
        "telegram": ["6873660400"] // Tony's Telegram ID
      }
    }
  }
}
```

### Agent Defaults (from `~/.openclaw/openclaw.json`)

```json
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "off"              // ✅ NO isolation restrictions
      },
      "maxConcurrent": 4,          // Can run 4 parallel tasks
      "subagents": {
        "maxConcurrent": 8         // Can spawn 8 subagents
      }
    }
  }
}
```

## Available Tools (All Automatic)

### 12 MCP Servers (Global Config)

| Tool | Purpose | Auto-Available? |
|---|---|---|
| `thinking-patterns` | Structured reasoning (15 tools) | ✅ Always |
| `Context7` | External library docs | ✅ Always |
| `openmemory` | Long-horizon memory | ✅ Always |
| `github` | Repository operations | ✅ Always |
| `obsidian-vault` | Personal knowledge vault | ✅ Always |
| `serena` | Code intelligence | ✅ Always |
| `Exa Search` | Web research | ✅ Always |
| `firecrawl-mcp` | Web extraction | ✅ Always |
| `playwright` | Browser automation | ✅ Always |
| `Magic MCP` | UI generation | ✅ Always |
| `droidrun` | Phone control (Samsung S25 Ultra) | ✅ Always |
| `filesystem` | Local file access | ✅ Always |

### Built-in OpenClaw Tools

- `exec` — Shell execution (WSL gateway or Windows node)
- `browser` — Web browsing and screenshots
- `system.run` — Direct Windows node commands
- All tools inherit Sparky's `security: full` permissions

## Exec Routing Reference

### Default (WSL Gateway)
```
exec openclaw health
exec bash -c "systemctl status openclaw-gateway"
exec python3 script.py
```

### Windows Desktop Node
```
exec --host node pwsh -NoProfile -Command "Get-Process"
exec --host node wsl -d Ubuntu -- openclaw nodes status
exec --host node cmd /c dir "D:\github"
```

### Elevated Linux (requires `/elevated` in Telegram)
```
exec sudo systemctl restart openclaw-gateway
exec sudo journalctl -u openclaw -n 50
exec sudo docker ps
```

### Elevated Windows (requires node-host running as Admin)
```
exec --host node pwsh -NoProfile -Command "Get-WindowsCapability -Online"
exec --host node pwsh -NoProfile -Command "netsh interface show interface"
```

## Access Persistence Verification

To verify access is still configured correctly:

```bash
# Check exec security
wsl bash -c "cat ~/.openclaw/openclaw.json | jq '.tools.exec'"

# Check elevated permissions
wsl bash -c "cat ~/.openclaw/openclaw.json | jq '.tools.elevated'"

# Check gateway health
wsl bash -c "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw health"

# Check Windows node connectivity
wsl bash -c "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw nodes status"
```

Expected output:
- `security: "full"` ✅
- `elevated.enabled: true` ✅
- Gateway: `Telegram: ok` ✅
- Node: `Connected: 1` ✅

## What Can Break Access?

### Will NOT Break Access
- Cursor restarts
- Gateway restarts (`systemctl --user restart openclaw-gateway`)
- Windows node restarts (watchdog auto-recovers)
- System reboots (systemd + watchdog restore services)

### Will Break Access
- Manual edits to `~/.openclaw/openclaw.json` that change `tools.exec.security` or `tools.elevated.enabled`
- Deleting the OpenClaw configuration directory (`~/.openclaw/`)
- Changing the gateway token without updating Windows node config
- Unpairing the Windows Desktop node

### Recovery Procedure

If access is broken:

1. Verify gateway is running:
   ```bash
   wsl bash -c "systemctl --user status openclaw-gateway"
   ```

2. Verify node is connected:
   ```bash
   wsl bash -c "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw nodes status"
   ```

3. If gateway is down, restart via canonical script:
   ```powershell
   & "D:\github\AI-Project-Manager\scripts\restart-openclaw-gateway.ps1"
   ```

4. If node is disconnected, relaunch via wrapper:
   ```powershell
   bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
   ```

5. If config is corrupted, restore from `OPENCLAW_MODULES.md` canonical reference.

## Summary

**Sparky's access is persistent, automatic, and unrestricted.**

No activation steps are needed for normal operations. All tools are always available. The only exception is elevated mode, which requires a `/elevated` directive in Telegram for sudo/admin commands.

Access is configured once at the OpenClaw level and persists across all restarts and sessions.
