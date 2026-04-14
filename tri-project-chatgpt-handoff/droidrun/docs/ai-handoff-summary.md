# AI Handoff Summary

For: AI-Project-Manager and any incoming agent taking over this codebase.
Written by: Documentation pass, DroidRun v0.5.1 workspace.

---

## What This Repo Is

This is a local workspace fork of the open-source DroidRun framework (upstream: github.com/droidrun/droidrun), extended with workspace-specific tooling. DroidRun enables AI agents to control Android devices by reading the device's UI accessibility tree and injecting programmatic input events. The workspace layer adds: MCP server integration (so AI clients like Cursor and Claude Desktop can invoke DroidRun tasks as tools), a PowerShell startup chain (manages Bitwarden secret loading and ADB wireless connection), and workspace-specific model configuration targeting DeepSeek (text) and OpenRouter/Gemini-2.0-flash (vision).

---

## Core Purpose

- **Android automation via AI:** Allow an LLM agent to perceive and control a real Android device by reading its UI tree and issuing actions (click, type, swipe, press key, open app).
- **MCP bridge:** Expose DroidRun as callable tools to any MCP-compatible AI client (Cursor, Claude Desktop, OpenClaw) so AI assistants can run Android tasks as part of larger workflows.
- **Remote device control:** Support wireless ADB over Tailscale VPN, enabling device automation without USB connection.

---

## Architecture in Plain Language

The execution path runs: **User or AI client → MCP server (`mcp_server.py`) → DroidRun CLI (`droidrun run`) → DroidAgent (LlamaIndex Workflow) → LLM API (DeepSeek or OpenRouter) → AndroidDriver → PortalClient → Portal APK (HTTP on port 8080) → device UI.** The Portal APK is an always-on process on the device that uses the Android Accessibility Service to read the full UI tree and to inject input events. The DroidAgent runs a perception-decision-action loop: it requests the current UI state from the Portal, sends that state to the LLM, receives an action decision, executes the action via the driver, then repeats until the task completes or `max_steps` is reached. The MCP server exposes this entire flow as MCP tools so AI clients can invoke it without using the CLI directly.

---

## Major Subsystems

| Subsystem | Location | What It Does | When Involved |
|---|---|---|---|
| DroidAgent | `src/droidrun/agent/droid/droid_agent.py` | LlamaIndex Workflow; main agent loop | Every task run |
| FastAgent | `src/droidrun/agent/fast_agent/` | Default agent using XML tool calls | Default mode |
| CodeAct / Scripter | `src/droidrun/agent/` | Code-generating agents; disabled by default | If `codeact: true` |
| AndroidDriver | `src/droidrun/tools/driver/android.py` | Translates DroidRun actions → Portal HTTP calls | Every action |
| PortalClient | `src/droidrun/tools/android/portal_client.py` | HTTP client for Portal APK; fallback to ADB content provider | Every device interaction |
| Portal APK | `com.droidrun.portal` (on-device) | Android Accessibility Service + HTTP server on port 8080 | Always running on device |
| MCP Server | `mcp_server.py` (workspace root) | Exposes DroidRun tools via MCP stdio protocol | When launched by AI client |
| CLI | `src/droidrun/cli/main.py` | Typer CLI entry point; `droidrun run`, `droidrun setup` | Direct CLI usage |
| Config Manager | `src/droidrun/config_manager/config_manager.py` | Loads and merges config YAML, env vars | At startup |
| LLM Config | `src/droidrun/llm/` | Provider abstraction for DeepSeek/OpenRouter/Google | Each LLM call |
| Startup Chain | `scripts/startup_droidrun.ps1` | Loads Bitwarden secrets, connects ADB, starts MCP | Session startup |
| Telemetry | `src/droidrun/telemetry/` | Anonymous PostHog events + optional Langfuse tracing | Background, every run |
| ToolRegistry | `src/droidrun/tools/` | Registers all available actions for the agent | Agent initialization |

---

## Key Workflows

### 1. Running a Task (End-to-End)

1. User invokes `droidrun run --goal "Open Settings and enable Dark Mode"` (or AI client sends MCP tool call)
2. CLI loads config from `~/.config/droidrun/config.yaml` and env vars
3. `DroidAgent` LlamaIndex Workflow is initialized with the goal
4. Agent calls `Portal HTTP GET /elements` to get current UI tree
5. UI tree is formatted and sent to LLM (DeepSeek or OpenRouter) with the goal
6. LLM returns an action (e.g., `click(index=5)`)
7. `AndroidDriver` translates the action to a Portal HTTP POST request
8. Portal APK executes the action via Accessibility Service
9. Agent waits, then fetches updated UI tree
10. Loop repeats until LLM returns `complete()` or `max_steps` is reached
11. `ResultEvent(success=True/False)` is returned to caller

### 2. Setting Up a Device

1. Connect device via USB or Tailscale wireless ADB
2. Run `droidrun setup` — installs Portal APK, grants permissions
3. Enable Accessibility Service manually on device (Settings → Accessibility → DroidRun Portal)
4. Run `droidrun devices` to verify device is recognized
5. Run `adb tcpip 5555` if switching to wireless ADB
6. Run `adb connect 100.71.228.18:5555` for Tailscale connection

### 3. Connecting Remotely via Tailscale

1. Ensure Tailscale is running on both host and device (or device's router)
2. Verify device IP: `tailscale ip -4` on device network
3. Enable ADB wireless on device: `adb tcpip 5555` (from USB connection first)
4. Connect: `adb connect 100.71.228.18:5555`
5. Verify: `adb devices` shows device as authorized
6. Forward Portal port: `adb forward tcp:8080 tcp:8080`
7. Run tasks normally — ADB and Portal will use the Tailscale tunnel

### 4. Using DroidRun from Another AI (MCP)

1. AI client (Cursor/Claude Desktop) is configured to launch `scripts\start_mcp_server.ps1`
2. On client startup, the MCP server process is spawned via stdio
3. AI client discovers available tools from the MCP server (tool list defined in `mcp_server.py`)
4. AI client sends a tool call (e.g., `run_android_task(goal="Open YouTube")`)
5. MCP server invokes the DroidRun CLI or agent directly
6. Result is returned as MCP tool response to the AI client

---

## Startup Flow (Cold Start)

1. **Open PowerShell** — launch with Bitwarden secrets: `pwsh -File scripts\startup_droidrun.ps1`
2. **Bitwarden loads** — `bws` CLI fetches `DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY`, writes to session env
3. **ADB connects** — script runs `adb connect 100.71.228.18:5555` (Tailscale IP)
4. **ADB forward** — script runs `adb forward tcp:8080 tcp:8080`
5. **Portal ping** — script verifies Portal HTTP responds on `localhost:8080`
6. **DroidRun ready** — env vars are set, device is reachable, CLI is usable
7. **MCP starts** (if AI client opens) — AI client spawns `mcp_server.py` via stdio

If any step in 2–5 fails, the startup script exits. DroidRun is not started in a partial state.

---

## Critical Files to Read First

| Priority | File | Why |
|---|---|---|
| 1 | `src/droidrun/agent/droid/droid_agent.py` | The main agent loop — understand this first |
| 2 | `src/droidrun/cli/main.py` | Entry point for all CLI commands |
| 3 | `src/droidrun/tools/driver/android.py` | How actions are dispatched to the device |
| 4 | `src/droidrun/tools/android/portal_client.py` | How the Portal APK is communicated with |
| 5 | `src/droidrun/config_manager/config_manager.py` | How config is loaded and merged |
| 6 | `src/droidrun/config_example.yaml` | All supported config options with defaults |
| 7 | `mcp_server.py` | MCP tool definitions — workspace-specific |
| 8 | `scripts/startup_droidrun.ps1` | Session startup chain including Bitwarden |
| 9 | `scripts/droidrun_run.ps1` | Task execution convenience script |
| 10 | `docs/PROJECT_INTELLIGENCE_INDEX.md` | Master index of all documentation |

---

## Dangerous Assumptions

1. **Portal is always reachable on localhost:8080.** If `adb forward` was not run or if Portal crashed on the device, every agent action silently fails or triggers the slower content provider fallback. Nothing alerts the user that Portal is down until a task fails.

2. **The device at 100.71.228.18 is always the Samsung Galaxy S25 Ultra.** If the Tailscale IP changes (device leaves and rejoins the network), ADB connects to a different address, or fails silently. The Tailscale IP is hardcoded in startup scripts.

3. **Bitwarden is reachable from the host.** If Bitwarden Secrets Manager is unavailable (network issue, vault locked), the startup script exits and DroidRun never starts. There is no fallback to environment variables already set.

4. **`llama-index==0.14.4` is the correct version.** This is pinned. If a future developer `pip install --upgrade` the environment, the agent may break silently if the LlamaIndex API has changed. The version pin is not documented with a reason.

5. **The LLM always returns parseable XML tool calls.** If the LLM returns malformed output, the agent fails at the parse step. There is no retry-with-simplified-prompt logic.

6. **Accessibility Service is always active.** The Portal APK depends on the Accessibility Service being enabled. Android can disable it after updates or if the user navigates away. DroidRun does not detect this proactively.

7. **`mobilerun-sdk` is a safe dependency.** Its purpose is unknown in this workspace. It is included but its behavior has not been audited.

---

## Current Unknowns

1. **`mobilerun-sdk` purpose** — What does this SDK do? What network calls does it make? Is it needed?
2. **credentials.yaml encryption** — Are stored app credentials encrypted at rest, or plaintext YAML?
3. **iOS driver status** — The iOS driver exists but is described as experimental. What is implemented vs stub?
4. **Stealth driver implementation** — What makes a driver "stealth"? Is it functional?
5. **Cloud driver auth** — The cloud driver references remote execution. What auth model does it use?
6. **`app_cards` server mode** — The CLI has a server mode for app cards. What does this do?
7. **StatelessManagerAgent vs DroidAgent** — When is the manager/executor split used vs the single DroidAgent?
8. **Which config file wins** — If `config.yaml` and `.env` both set the same value, which takes precedence?
9. **Langfuse screenshot format** — Are screenshots sent as base64 or URLs? What is the size limit?
10. **Portal APK exact endpoint list** — The HTTP API endpoints are not formally documented.

---

## How This Repo Interacts With the Workspace

This DroidRun workspace is one of three AI-enabled tools in the development setup:

| Tool | Role |
|---|---|
| **DroidRun** (this repo) | Android device automation; invoked by AI clients via MCP |
| **Cursor** | Primary IDE; hosts MCP client connection to DroidRun |
| **OpenClaw** | Gateway/orchestration; hosts additional MCP client connection to DroidRun |
| **Claude Desktop** | Secondary AI client; also connected to DroidRun MCP |

All three AI clients point to the same `scripts\start_mcp_server.ps1` in their MCP configs. This means multiple AI clients can simultaneously invoke DroidRun tools. There is no concurrency control — simultaneous tasks from different clients will race for the same device.

The Bitwarden Secrets Manager (machine account: BWS_DROIDRUN_TOKEN) holds the API keys that DroidRun needs. The startup script is the bridge between Bitwarden and the DroidRun runtime.

---

## Where Future Changes Are Most Risky

1. **`portal_client.py` and the Portal APK HTTP API** — Any change to Portal endpoints requires coordinated updates to both the APK (Android build) and the Python client. These are the most tightly coupled components and the hardest to test without a physical device.

2. **`droid_agent.py` LlamaIndex Workflow** — The LlamaIndex Workflows API changed significantly between versions. The pinned `llama-index==0.14.4` dependency means any upgrade to the agent loop risks breaking the workflow step definitions, event passing, and the observe-decide-act loop structure.

3. **`config_manager.py` and config schema** — The config dataclass is the contract between user settings and runtime behavior. Adding, removing, or renaming config keys without migration logic will silently break existing user configs. No migration system is currently documented.
