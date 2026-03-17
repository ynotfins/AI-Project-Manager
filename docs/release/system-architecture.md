# System Architecture

**Version:** OpenClaw v2026.3.8 / DroidRun v0.5.1  
**Last updated:** 2026-03-16  
**Audience:** Internal — owner, family, employees  
**Source repos:** open--claw, droidrun, AI-Project-Manager

---

## Overview

This is a tri-project AI operating system running on a single Windows PC (chaoscentral) with WSL2.
The system provides always-on AI assistance through messaging channels (WhatsApp, Telegram),
developer tooling (Cursor IDE), and physical phone automation (Samsung Galaxy S25 Ultra).

### Three-Layer Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 3: ORCHESTRATION — AI-Project-Manager                        │
│  Governance rules, workflow contracts, release docs, STATE.md       │
│  No runtime. Docs-only repo. Cursor rules define AI behavior.       │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 2: AGENT BRAIN — open--claw (WSL2)                           │
│  OpenClaw v2026.3.8 gateway. Port 18789 (UI/API), 18792 (health)   │
│  Channels: WhatsApp (Baileys), Telegram. Skills: 8 configured.      │
│  LLM routing: claude-sonnet-4-5 → gpt-4o → gpt-4o-mini             │
│  Memory: sqlite-vec (local vector store). Node.js 22, pnpm.         │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 1: RUNTIME — droidrun (Windows)                              │
│  Python 3.12.10. MCP server: phone_do / phone_ping / phone_apps    │
│  Target: Samsung Galaxy S25 Ultra (Android 16) via ADB+Tailscale   │
│  Tailscale IP: 100.71.228.18:5555. DroidRun Portal v0.6.1 on phone │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Full System Architecture Diagram

```mermaid
graph TB
    subgraph Windows["Windows PC (chaoscentral)"]
        subgraph Cursor["Cursor IDE"]
            CursorApp["Cursor App"]
            MCPClients["MCP Clients:<br/>Clear Thought 1.5<br/>Context7<br/>openmemory<br/>serena<br/>github<br/>firecrawl-mcp<br/>sequential-thinking<br/>droidrun"]
        end

        subgraph DroidRun["droidrun project (Windows)"]
            MCP["mcp_server.py<br/>MCP Server (stdio)"]
            DroidRunExe[".venv/Scripts/droidrun.exe<br/>v0.5.1"]
            ADB["ADB client<br/>C:\\platform-tools\\adb.exe"]
        end

        BWS["Bitwarden Secrets CLI (bws)<br/>Machine account: droidrun-windows"]
        StartScript["start-cursor-with-secrets.ps1<br/>(Bitwarden → env → WSL gateway)"]
    end

    subgraph WSL2["WSL2 (Ubuntu)"]
        subgraph OpenClaw["open--claw — OpenClaw Gateway"]
            Gateway["OpenClaw Gateway<br/>v2026.3.8<br/>Port 18789 (API/UI)<br/>Port 18792 (health)"]
            Channels["Channels<br/>WhatsApp (Baileys)<br/>Telegram (@Sparky4bot)"]
            Skills["Skills (8 configured)<br/>approval-gate<br/>gmail-inbox<br/>domain-email<br/>google-calendar<br/>google-contacts<br/>whatsapp-official<br/>sms-twilio<br/>mem0-bridge"]
            Memory["Memory<br/>sqlite-vec<br/>~/.openclaw/workspace/"]
            SystemD["systemd user service<br/>openclaw-gateway.service"]
        end
        NVM["Node.js v22 (nvm)<br/>pnpm 10.23.0"]
    end

    subgraph LLMCloud["LLM Providers (Internet)"]
        Anthropic["Anthropic API<br/>claude-sonnet-4-5 (primary)<br/>claude-opus-4-6"]
        OpenAI["OpenAI API<br/>gpt-4o (fallback)<br/>gpt-4o-mini (budget)"]
        DeepSeek["DeepSeek API<br/>deepseek-chat<br/>(droidrun non-vision)"]
        OpenRouter["OpenRouter API<br/>google/gemini-2.0-flash-001<br/>(droidrun vision)"]
    end

    subgraph Phone["Samsung Galaxy S25 Ultra"]
        AndroidOS["Android 16"]
        DroidRunPortal["DroidRun Portal v0.6.1<br/>Accessibility Service ON<br/>Port 8080 (local HTTP)"]
        Tailscale_Phone["Tailscale WireGuard<br/>100.71.228.18"]
    end

    subgraph Messaging["Messaging (Internet)"]
        WhatsApp["WhatsApp"]
        Telegram["Telegram"]
    end

    subgraph BitwPass["Bitwarden Password Manager"]
        BWPassVault["Vault<br/>BWS_DROIDRUN_TOKEN<br/>OPENCLAW_GATEWAY_TOKEN"]
    end

    subgraph BitwSecrets["Bitwarden Secrets Manager"]
        BWSecretsOC["Project: OpenClaw<br/>ANTHROPIC_API_KEY<br/>OPENAI_API_KEY<br/>OPENROUTER_API_KEY"]
        BWSecretsDR["Project: DroidRun<br/>DEEPSEEK_API_KEY<br/>OPENROUTER_API_KEY"]
    end

    %% Startup flow
    StartScript -->|"1. bws run → env vars"| BWSecretsOC
    StartScript -->|"2. WSLENV → .gateway-env (transient)"| SystemD
    SystemD -->|"3. EnvironmentFile loads keys"| Gateway

    %% Cursor → OpenClaw
    CursorApp -->|"HTTP API :18789"| Gateway

    %% Cursor → DroidRun MCP
    CursorApp -->|"MCP stdio"| MCP
    MCP -->|"subprocess"| DroidRunExe

    %% DroidRun → Phone
    DroidRunExe -->|"ADB commands"| ADB
    ADB -->|"ADB over Tailscale WireGuard<br/>tcp:100.71.228.18:5555"| Tailscale_Phone
    Tailscale_Phone --> DroidRunPortal
    DroidRunPortal -->|"tcp:8080 (port-forwarded)"| DroidRunExe

    %% OpenClaw → LLMs
    Gateway -->|"Anthropic API"| Anthropic
    Gateway -->|"OpenAI API"| OpenAI

    %% DroidRun → LLMs
    DroidRunExe -->|"non-vision tasks"| DeepSeek
    DroidRunExe -->|"vision tasks"| OpenRouter

    %% Channels
    Gateway <-->|"WebSocket/REST"| Channels
    Channels <-->|"Baileys (unofficial)"| WhatsApp
    Channels <-->|"Bot API"| Telegram

    %% Secrets injection for DroidRun
    BWPassVault -->|"bw get item"| StartScript
    BWSecretsOC -->|"bws secret get"| StartScript
    BWSecretsDR -->|"bws secret get"| BWS
    BWS -->|"HKCU\\Environment"| DroidRunExe
```

---

## Data Flow: User Message → Agent Response

```mermaid
sequenceDiagram
    participant U as User (WhatsApp/Telegram)
    participant CH as Channel Adapter
    participant GW as OpenClaw Gateway
    participant SK as Skill / Tool
    participant LLM as LLM Provider
    participant MEM as sqlite-vec Memory

    U->>CH: sends message
    CH->>GW: deliver to agent session
    GW->>MEM: retrieve context (prior turns, decisions)
    GW->>LLM: claude-sonnet-4-5 (primary)<br/>or gpt-4o (fallback)
    LLM-->>GW: response / tool calls
    GW->>SK: invoke skill (if tool call)
    SK-->>GW: skill result
    GW->>MEM: store turn
    GW->>CH: send response
    CH->>U: deliver response
```

---

## Data Flow: Phone Control

```mermaid
sequenceDiagram
    participant AI as Cursor / OpenClaw Agent
    participant MCP as mcp_server.py (stdio)
    participant DR as droidrun.exe
    participant ADB as ADB Client
    participant TS as Tailscale Tunnel
    participant PH as DroidRun Portal (phone)
    participant LLM as DeepSeek / Gemini

    AI->>MCP: phone_do(task, vision=false)
    MCP->>DR: subprocess: droidrun run -d 100.71.228.18:5555
    DR->>LLM: observe current UI + plan actions
    LLM-->>DR: action sequence
    DR->>ADB: ADB commands (tap, swipe, type, screenshot)
    ADB->>TS: WireGuard packet → 100.71.228.18:5555
    TS->>PH: ADB over Tailscale
    PH-->>ADB: accessibility tree / screenshot
    ADB-->>DR: result
    DR-->>MCP: task output
    MCP-->>AI: CallToolResult
```

---

## Service Boundaries

| Service | Host | Port | Protocol | Owner |
|---------|------|------|----------|-------|
| OpenClaw Gateway API | WSL2 localhost | 18789 | HTTP/WebSocket | open--claw |
| OpenClaw Health | WSL2 localhost | 18792 | HTTP | open--claw |
| OpenClaw Control UI | WSL2 localhost | 18789/openclaw | HTTP | open--claw |
| DroidRun MCP Server | Windows process | stdio | MCP JSON-RPC | droidrun |
| OpenMemory Proxy | Windows localhost | 8766 | HTTP/SSE | AI-Project-Manager |
| ADB Server | Windows | 5037 | TCP | droidrun |
| DroidRun Portal | Phone (Android) | 8080 | HTTP (port-forwarded) | droidrun |
| Tailscale VPN | Windows + Phone | WireGuard | UDP | external |

---

## Repo Responsibilities (Summary)

| Repo | Runtime | Language | Primary Role |
|------|---------|----------|-------------|
| `open--claw` | WSL2 | Node.js 22 | AI gateway, channels, LLM routing, skills, memory |
| `droidrun` | Windows | Python 3.12 | Phone automation, ADB bridge, MCP server |
| `AI-Project-Manager` | None | Markdown | Governance, workflow rules, release docs, STATE tracking |

---

## Local vs. Remote Execution

| Component | Local | Remote/Cloud |
|-----------|-------|-------------|
| OpenClaw gateway process | ✓ WSL2 | — |
| Agent session state | ✓ sqlite-vec on disk | — |
| LLM inference | — | ✓ Anthropic / OpenAI / OpenRouter / DeepSeek |
| WhatsApp messages | ✓ Baileys runs locally | ✓ WhatsApp servers for delivery |
| Telegram messages | ✓ grammy runs locally | ✓ Telegram Bot API |
| DroidRun MCP server | ✓ Windows process | — |
| ADB connection | ✓ Windows → Phone via Tailscale | ✓ Tailscale relay if P2P fails |
| Secret storage | — | ✓ Bitwarden cloud vault |

---

## Offline Support

| Feature | Works Offline? | Notes |
|---------|----------------|-------|
| OpenClaw gateway process | ✓ Yes | Starts without internet |
| Local memory (sqlite-vec) | ✓ Yes | Reads/writes work offline |
| LLM responses | ✗ No | All LLM providers are cloud APIs |
| WhatsApp / Telegram | ✗ No | Requires internet for delivery |
| DroidRun phone control | Partial | ADB works over LAN; Tailscale relay needs internet |
| Bitwarden secret injection | ✗ No | bws requires internet; use cached env vars |

---

## Startup Sequence

When `start-cursor-with-secrets.ps1` is run (via `bws run ...`):

1. **Bitwarden bws CLI** injects secrets into PowerShell env vars (ANTHROPIC_API_KEY, OPENAI_API_KEY, OPENROUTER_API_KEY)
2. **DroidRun block**: fetches DEEPSEEK_KEY + OPENROUTER_KEY from DroidRun Bitwarden project; stores in Windows user env; reconnects phone ADB
3. **OpenMemory proxy**: starts `start-openmemory-proxy.ps1` (HTTP→SSE bridge on :8766)
4. **Gateway secrets**: writes transient `~/.openclaw/.gateway-env` (chmod 600), restarts `openclaw-gateway.service` via systemd, deletes `.gateway-env` after 8 seconds
5. **Cursor launches**: opens `openclaw.code-workspace` (AI-Project-Manager + open--claw + droidrun)

---

## MCP Servers Active in Cursor

| Server | Transport | Purpose |
|--------|-----------|---------|
| `Clear Thought 1.5` | HTTP | Primary reasoning (mental_model, debugging_approach, etc.) |
| `Context7` | HTTP | Library/framework documentation lookup |
| `openmemory` | HTTP (:8766) | Cross-session agent memory |
| `serena` | stdio | Code intelligence (symbol nav, refactoring) |
| `github` | HTTP | GitHub repo operations |
| `sequential-thinking` | stdio | Fallback sequential reasoning |
| `firecrawl-mcp` | HTTP | Web scraping (scrape/map/search only) |
| `droidrun` | stdio | Phone automation (phone_do/phone_ping/phone_apps) |

---

## Key Configuration Files

| File | Location | Purpose |
|------|----------|---------|
| `openclaw.json` | `~/.openclaw/openclaw.json` (WSL) | Gateway runtime config (channels, agents, skills, routing) |
| `openclaw.template.json5` | `open--claw/open-claw/configs/` | Template for `openclaw.json` — commit-safe |
| `mcp.json` | `C:\Users\ynotf\.cursor\mcp.json` | Cursor MCP server registry |
| `openclaw.code-workspace` | `C:\Users\ynotf\.openclaw\` | Tri-repo multi-root workspace definition |
| `start-cursor-with-secrets.ps1` | `C:\Users\ynotf\.openclaw\` | Startup script (Bitwarden → env → gateway) |
| `api-keys.conf` | `~/.config/systemd/user/openclaw-gateway.service.d/` | systemd EnvironmentFile drop-in |
| `mcp_server.py` | `D:\github\droidrun\` | DroidRun MCP server entry point |

> **Security:** No secrets are stored in any of these files (except `openclaw.json`'s internal gateway auth token, which is OpenClaw-managed and not a user-provided credential).
