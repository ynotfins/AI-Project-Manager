# Project Overview — DroidRun

**Related:** [PROJECT_INTELLIGENCE_INDEX.md](PROJECT_INTELLIGENCE_INDEX.md) | [repo-boundaries.md](repo-boundaries.md)

---

## What DroidRun Is

DroidRun is an **open-source Python framework (v0.5.1, Beta, MIT)** that enables LLM-powered AI agents to autonomously control Android devices through natural language commands. An agent "sees" the device screen (via UI accessibility tree or screenshots), plans actions, and executes them — tapping, swiping, typing text, launching apps, pressing system buttons.

This workspace instance combines the upstream DroidRun framework (`src/`) with a Windows-specific operational layer built for a Samsung Galaxy S25 Ultra connected over Tailscale.

---

## What DroidRun Is Responsible For

- Connecting to Android devices via ADB (USB or TCP/Wireless/Tailscale)
- Installing and managing the DroidRun Portal APK on the device
- Reading device UI state (accessibility tree via Portal, or screenshots)
- Executing atomic device actions: tap, swipe, type, key press, app launch, drag
- Running LLM agents (FastAgent, Manager+Executor, CodeAct) to fulfill natural-language tasks
- Exposing device control as MCP tools (`phone_do`, `phone_ping`, `phone_apps`) to AI clients
- Managing API key injection and ADB reconnection via PowerShell scripts
- Recording and replaying device action macros (`droidrun macro`)
- Providing a terminal UI (`droidrun tui`) for interactive sessions

---

## What DroidRun Is NOT Responsible For

- Managing the Android phone's OS, apps, or accounts
- Providing a GUI desktop application (terminal/CLI only, plus TUI)
- Storing persistent user data or conversation history between runs
- Managing other AI projects (that is `AI-Project-Manager`'s role)
- Cloud device management (separate `mobilerun-sdk` / DroidRun Cloud product)
- Network infrastructure (Tailscale managed separately)
- Bitwarden vault management (keys injected at startup by PowerShell scripts)

---

## Who Uses It

| User | Context |
|------|---------|
| Human operator (workspace owner) | Runs tasks via CLI or PowerShell scripts |
| OpenClaw (AI client) | Calls `phone_do`, `phone_ping`, `phone_apps` via MCP |
| Cursor agent | Calls MCP tools from within Cursor IDE |
| Claude Desktop | Calls MCP tools from Claude's MCP integration |
| AI-Project-Manager | Launches DroidRun startup script as part of workspace launch |

---

## Where It Fits — Tri-Workspace Context

```
AI-Project-Manager
├── Launches: open--claw workspace
├── Launches: droidrun workspace  ← THIS REPO
│   ├── startup_droidrun.ps1 (API key inject + ADB connect)
│   └── start_mcp_server.ps1 (MCP server for AI clients)
└── Manages project orchestration
```

DroidRun is the **actuator layer**: when an AI client in OpenClaw or Cursor needs to do something on a phone, it calls DroidRun's MCP tools.

---

## Current Maturity / Status

| Aspect | Status |
|--------|--------|
| Upstream framework | Beta (v0.5.1) |
| Android support | Production-quality |
| iOS support | Experimental (stub code, not usable) |
| Tailscale remote | Working (100.71.228.18:5555) |
| MCP server (workspace) | Working (mcp_server.py) |
| Vision (screenshots) | Working via OpenRouter/Gemini |
| Reasoning mode | Available (Manager + Executor) |
| CI/CD | None configured |
| Test coverage | Unknown / not verified locally |

---

## Top 5 Critical Capabilities

1. **Natural language device control** — `droidrun run "open the camera app"` executes on device
2. **Multi-provider LLM support** — DeepSeek (no-vision), OpenRouter/Gemini (vision), OpenAI, Anthropic, Google, Ollama
3. **MCP server exposure** — Phone control accessible from any MCP-compatible AI client
4. **Secure key management** — API keys from Bitwarden Secrets Manager, never in files
5. **Smart ADB reconnect** — Handles post-reboot port changes, auto-locks to port 5555

---

## Device Details (This Workspace)

| Property | Value |
|----------|-------|
| Device | Samsung Galaxy S25 Ultra (SM-S938U) |
| Android version | Android 16 |
| Tailscale IP | 100.71.228.18 |
| ADB port (fixed) | 5555 |
| Portal HTTP port | 8080 (forwarded via ADB) |
| Connection method | Tailscale → ADB TCP → Portal HTTP |
