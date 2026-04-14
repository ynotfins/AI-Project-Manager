# Navigation & Screen Flow

DroidRun is a **CLI tool + TUI** — it has no traditional GUI screen navigation. This document describes the actual flows: command-line invocation, TUI panel navigation, agent task flow on the Android device, and MCP client/server routing.

---

## 1. CLI Command Flow

```
User terminal
     │
     ▼
droidrun [COMMAND] [OPTIONS] [ARGS]
     │
     ├─ droidrun run "open camera and take a photo"
     ├─ droidrun setup
     ├─ droidrun ping
     ├─ droidrun doctor
     ├─ droidrun macro record / macro replay
     └─ droidrun tui
```

### DroidRunCLI — Smart Command Routing

DroidRun uses a custom `Click.Group` subclass (`DroidRunCLI`) that rewrites the argument list before dispatch:

- If the **first argument is not a known command** and **not a flag** (e.g., `droidrun "open settings"`), the CLI automatically inserts `run` before it.
- This allows the shorthand `droidrun "do task"` instead of `droidrun run "do task"`.

```
droidrun "open camera"
    └─► DroidRunCLI detects unknown first arg
        └─► inserts "run" → droidrun run "open camera"
```

### Execution Sequence for `droidrun run`

```
1. Parse CLI options (--model, --provider, --vision, --steps, etc.)
2. Load config: ~/.config/droidrun/config.yaml (via ConfigLoader)
3. Load env vars: ~/.config/droidrun/.env (via python-dotenv)
4. Apply CLI overrides on top of config values
5. Resolve device (ADB serial or TCP) → connect portal client
6. Instantiate LLM (provider + model from config/CLI)
7. Instantiate agent (FastAgent / Manager+Executor / CodeAct)
8. Run agent loop (observe → plan → act → repeat, max_steps)
9. Print result to terminal (rich-formatted)
10. Exit
```

---

## 2. TUI Navigation (Textual-based)

Launch with:

```bash
droidrun tui
```

The TUI is a [Textual](https://textual.textualize.io/) application. Based on the source structure, the following screens and tabs exist:

### Screens

| Screen | File | Purpose |
|--------|------|---------|
| Settings Screen | `settings_screen.py` | Main configuration UI |

### Tabs within Settings Screen

| Tab | File | Purpose |
|-----|------|---------|
| Models | `models_tab.py` | Configure LLM providers and model selection |
| Advanced | `advanced_tab.py` | Advanced agent/execution settings |
| Agent | `agent_tab.py` | Agent behavior, steps, reasoning mode |

> **Note:** The exact tab labels and navigation keys are inferred from file names. Verify by running `droidrun tui` and inspecting the rendered interface.

### TUI Navigation Keys (Textual defaults)

| Key | Action |
|-----|--------|
| `Tab` | Move focus to next widget |
| `Shift+Tab` | Move focus to previous widget |
| `Enter` | Activate focused button/toggle |
| `Escape` | Close dialog / go back |
| `Q` or `Ctrl+C` | Quit TUI |

The TUI writes changes back to `~/.config/droidrun/config.yaml` on save.

---

## 3. Agent Task Flow (Device-side Navigation)

The "navigation" DroidRun performs is on the **Android device**, not on the host. Each agent step:

```
┌─────────────────────────────────────────┐
│              Agent Loop                 │
│                                         │
│  1. OBSERVE                             │
│     └─ Portal APK reads accessibility  │
│        tree (or screenshot if vision)   │
│        via PortalClient                 │
│                                         │
│  2. PLAN                                │
│     └─ LLM receives UI state + task    │
│        → produces action or tool call   │
│                                         │
│  3. ACT                                 │
│     └─ PortalClient sends action:       │
│        tap / swipe / type / key /       │
│        screenshot                       │
│                                         │
│  4. OBSERVE NEXT STATE                  │
│     └─ Device transitions to new screen │
│        Loop back to step 1              │
│                                         │
│  Stop: task complete / max_steps hit    │
└─────────────────────────────────────────┘
```

### Agent Variants

| Mode | Behavior |
|------|----------|
| **FastAgent** (default) | Single LLM, XML tool-calling, direct observe→act |
| **Reasoning (Manager+Executor)** | Manager LLM plans sub-tasks, Executor LLM acts |
| **CodeAct** | LLM generates Python code snippets; sandbox executes them |
| **Structured Output** | Agent extracts structured data from device screens |

---

## 4. MCP Client/Server Flow

### As MCP Server (exposing phone control to AI clients)

```
AI Client (Claude Desktop, Cursor, etc.)
     │  stdio JSON-RPC
     ▼
droidrun mcp_server.py
     │  phone_do(goal, vision=False)
     │  phone_ping()
     │  phone_apps()
     ▼
DroidRun Agent (internal)
     │
     ▼
PortalClient → Android device
     │
     └─► result returned to AI client
```

### As MCP Client (consuming external tools)

```
DroidRun Agent
     │  needs external tool
     ▼
MCPClientManager (mcp/client.py)
     │  list_tools → discovers available tools
     │  call_tool  → invokes tool
     ▼
External MCP Server (stdio or HTTP)
     │
     └─► result injected into agent context
```

---

## 5. Setup Flow (first-time)

```
droidrun setup
     │
     ├─ Checks ADB connection
     ├─ Downloads Portal APK (GitHub releases via api.github.com or ungh.cc)
     ├─ Installs com.droidrun.portal via ADB
     └─ Starts portal service (HTTP on port 8080 inside device)

droidrun ping
     └─ Verifies portal is reachable and responding

droidrun doctor
     └─ Full diagnostics: ADB, portal, LLM connectivity, config validity
```

---

## 6. Windows Workspace Setup (one-time)

```
setup_windows_host.ps1   ← run once by developer
     │
     ├─ Installs Python deps (pip install -e ".[google,anthropic,openai,deepseek,ollama,dev]")
     ├─ Configures ADB / Android SDK path
     ├─ Stores API keys in HKCU\Environment (persistent Windows env vars)
     └─ Optionally configures Tailscale for remote device access

startup_droidrun.ps1 / store_api_keys_to_env.ps1
     └─ Run on session start to inject DROIDRUN_DEEPSEEK_KEY, DROIDRUN_OPENROUTER_KEY
        into the current shell from Windows registry
```
