# DroidRun Runtime Lifecycle

> DroidRun v0.5.1 · Python asyncio · LlamaIndex Workflows

This document traces the full lifetime of a DroidRun process from the moment the user hits Enter to the moment the process exits, covering every major path: CLI, MCP server, and PowerShell helper scripts.

---

## 1. CLI Startup Sequence

### 1.1 Entry point resolution

`pyproject.toml` registers:

```
[project.scripts]
droidrun = "droidrun.cli.main:cli"
```

When the user runs `droidrun <command>`, the OS resolves the installed script, which calls the `cli` Click group defined in `droidrun/cli/main.py`. The group is instantiated as `DroidRunCLI`, a custom `click.Group` subclass that injects shared context (config path, verbosity) before dispatching to sub-commands.

### 1.2 Click dispatch

Click parses `sys.argv`, matches the sub-command name, and invokes the corresponding function. All sub-commands share the following preamble:

1. Read `--config` option (defaults to `~/.config/droidrun/config.yaml`).
2. Call `ConfigLoader.load(path)` → returns a `DroidrunConfig` instance.
3. Store the config on the Click context object so nested callbacks can access it.

### 1.3 Per-command startup

| Command | What happens immediately |
|---------|--------------------------|
| `run` | Resolves device serial, optionally triggers `auto_setup`, instantiates `DroidAgent`, calls `asyncio.run(agent.run(task))` |
| `setup` | Calls `auto_setup` directly: downloads Portal APK from GitHub release, installs via `adb install`, enables accessibility service |
| `ping` | Opens `PortalClient`, sends a single HTTP GET to `localhost:8080/ping`, prints latency |
| `doctor` | Runs a checklist: ADB reachable, Portal installed, accessibility enabled, LLM credentials present |
| `tui` | Launches a Textual TUI; internally still instantiates `DroidAgent` and streams events |
| `macro` | Loads a YAML macro file, iterates steps, calls `DroidAgent.run()` for each |

### 1.4 Device resolution

```
explicit --serial flag?
  → use as-is
else
  → adb devices  (subprocess)
  → parse output, pick first online device
  → if none: raise UsageError
```

If `auto_setup=true` is set in config:

1. Check whether `com.droidrun.portal` is installed (`adb shell pm list packages`).
2. If missing: fetch latest release asset URL from GitHub API, download APK to a temp file, run `adb install -r <apk>`.
3. Enable accessibility service:  
   `adb shell settings put secure enabled_accessibility_services com.droidrun.portal/com.droidrun.portal.service.DroidrunAccessibilityService`
4. Forward port: `adb forward tcp:8080 tcp:8080`.

---

## 2. DroidAgent Initialization

`DroidAgent` is the top-level LlamaIndex `Workflow` subclass. Initialization (`__init__`) does **not** start any async I/O — it only wires up dependencies:

```
DroidAgent.__init__(task, config, llm, ...)
  → self.driver  = AndroidDriver(serial)
  → self.portal  = PortalClient(driver)
  → self.ui      = UIProvider(portal)
  → self.llm     = resolve_llm(config)          # from config.provider / env vars
  → self.steps   = build_step_registry(config)  # FastAgent OR ManagerAgent+ExecutorAgent
  → self.traj    = TrajectoryWriter(config)      # no-op if save_trajectory == "none"
```

### 2.1 Agent mode selection

```
config.reasoning == False
  → FastAgent / CodeActAgent (single-agent, direct action generation)

config.reasoning == True
  → ManagerAgent (plans sub-tasks)
  → ExecutorAgent (executes each sub-task)
```

Both modes are registered as LlamaIndex `Workflow` steps and communicate through typed `Event` objects passed on an internal event bus.

---

## 3. Agent Execution Loop

`asyncio.run(agent.run(task))` hands control to the LlamaIndex Workflow engine.

### 3.1 Step sequence (single-agent / FastAgent mode)

```
StartEvent(task)
    │
    ▼
[observe]  UIProvider.get_state()
           → PortalClient.get_ui_tree()    (HTTP or ADB content provider)
           → IndexedFormatter.format(tree)
           → ConciseFilter.prune(tree)
           → returns: annotated XML string
    │
    ▼
[plan/act] LLM call with system prompt + UI state + task
           → returns: action(s) to execute
    │
    ▼
[execute]  AndroidDriver.perform_action(action)
           → wraps adb shell / PortalClient HTTP call
           → waits wait_for_stable_ui = 0.3 s
    │
    ▼
[check]    done? max_steps reached? error?
           → no  → sleep 1.0 s → back to [observe]
           → yes → StopEvent(result)
```

`max_steps` defaults to 15. The loop counter is stored in workflow context and incremented after each `[execute]` step.

### 3.2 Step sequence (reasoning / ManagerAgent mode)

```
StartEvent(task)
    │
    ▼
ManagerAgent.plan()   → LLM generates sub-task list
    │
    ▼  (for each sub-task)
ExecutorAgent.run()
    └─ observe → act loop (same as single-agent, but scoped to sub-task)
    │
    ▼
ManagerAgent.aggregate() → summarises results → StopEvent
```

### 3.3 Observation detail

`UIProvider.get_state()` tries two transport paths in order:

1. **TCP (preferred):** `httpx.AsyncClient` → `GET http://localhost:8080/ui`  
   Requires `adb forward tcp:8080 tcp:8080` to be active.
2. **ADB content provider (fallback):** `adb shell content query --uri content://com.droidrun.portal.provider/ui`

The Portal APK (`com.droidrun.portal`) listens on port 8080 and provides the accessibility tree via its `DroidrunAccessibilityService`.

---

## 4. MCP Server Startup

`mcp_server.py` at the repository root is a standalone Python script, not imported by the main DroidRun package. AI clients (Claude Desktop, etc.) launch it as a child process via stdio transport.

### 4.1 How the client launches it

The AI client's MCP config contains something like:

```json
{
  "command": "python",
  "args": ["D:/github/droidrun/mcp_server.py"],
  "transport": "stdio"
}
```

The client spawns the process, then speaks JSON-RPC 2.0 over stdin/stdout.

### 4.2 What `mcp_server.py` does at startup

1. Creates an `mcp.Server` instance with name `"droidrun"`.
2. Registers three tools: `phone_do`, `phone_ping`, `phone_apps`.
3. Calls `server.run(transport="stdio")` — blocks reading stdin indefinitely.

No ADB connection is opened at startup. ADB is touched only when a tool is called.

### 4.3 Tool dispatch

Each tool call triggers `subprocess.run(["droidrun", ...], timeout=300)`.  
`phone_do` maps to `droidrun run <task> [--serial ...]`.  
`phone_ping` maps to `droidrun ping`.  
`phone_apps` maps to `droidrun run "list installed apps"` (or equivalent).

stdout/stderr of the subprocess are captured and returned as the tool result string.

### 4.4 Shutdown

The MCP server has no explicit shutdown hook. When the parent AI client exits or sends SIGTERM/SIGKILL, the process terminates immediately. No cleanup is needed because each invocation is stateless.

---

## 5. PowerShell Script Lifecycle

Three scripts ship with the repository to assist with device connectivity on Windows.

### 5.1 `startup_droidrun.ps1`

**Purpose:** Inject API keys from Bitwarden into the environment and establish ADB connectivity before launching the MCP server or a manual `droidrun` session.

**Sequence:**

```
1. $ErrorActionPreference = "SilentlyContinue"   # suppress non-fatal ADB errors
2. bws run ... → sets env vars:
     DROIDRUN_DEEPSEEK_KEY
     DROIDRUN_OPENROUTER_KEY
     GOOGLE_API_KEY
     OPENAI_API_KEY
     ANTHROPIC_API_KEY
3. adb connect 100.71.228.18:5555   (Tailscale address)
4. adb -s 100.71.228.18:5555 wait-for-device
5. [optional] adb forward tcp:8080 tcp:8080
6. echo "Ready"
```

The script does **not** stay resident. It exits after step 6.

### 5.2 `reconnect_remote.ps1`

**Purpose:** Re-establish ADB WiFi connection when the device drops off (e.g., after a sleep/wake cycle).

**Sequence:**

```
1. adb disconnect
2. adb connect <ip>:5555
3. adb devices   (print result for user confirmation)
```

Run manually or on a Task Scheduler trigger. Not called automatically by DroidRun.

### 5.3 `adb_find_port.ps1`

**Purpose:** Scan a subnet for devices advertising ADB on port 5555, useful when the device IP is unknown.

**Sequence:**

```
1. For each IP in range:
     Test-NetConnection -Port 5555 -WarningAction SilentlyContinue
2. Print IPs that respond
```

Output is informational. The user then passes the found IP to `droidrun --serial <ip>:5555` or adds it to config.

---

## 6. Shutdown Behavior

### 6.1 Normal termination

`StopEvent` is emitted by the workflow when:
- The agent reports the task is complete (`done=True` in LLM response).
- `max_steps` (default 15) is reached.

The workflow returns a result dict to `asyncio.run()`. The CLI prints the result and exits with code 0.

### 6.2 Keyboard interrupt

`KeyboardInterrupt` is caught at the `asyncio.run()` call site. The handler:
1. Cancels the running coroutine.
2. Returns `False` (task not completed).
3. Logs "Interrupted by user".
4. Exits with code 1.

No partial state is rolled back because DroidRun holds no transactions.

### 6.3 Error exit

Unhandled exceptions bubble to the CLI layer, which prints the traceback (if `--verbose`) and exits with a non-zero code. No cleanup hooks are registered beyond Python's normal atexit.

---

## 7. State Persistence

DroidRun is intentionally stateless between runs.

| Artifact | Persists? | Location |
|----------|-----------|----------|
| Config file | Yes (user-managed) | `~/.config/droidrun/config.yaml` |
| Trajectory | Yes (if enabled) | `trajectories/<timestamp>/` |
| ADB forwarding rule | Yes (until reboot/disconnect) | OS ADB daemon |
| Portal APK on device | Yes (until uninstalled) | Android device |
| LLM conversation history | No | In-memory only |
| UI tree snapshot | No | In-memory only |
| Step counter | No | In-memory per run |
| MCP server state | No | Each run is isolated subprocess |

### 7.1 Trajectory format

When `save_trajectory != "none"`, `TrajectoryWriter` creates a timestamped directory under `trajectories/` and writes one JSON file per step containing:
- Step index
- UI tree snapshot (raw XML)
- LLM prompt and response
- Action taken
- Timestamp

Trajectory files are append-only during a run and are never read back by DroidRun itself — they are purely for human inspection and offline analysis.

---

## 8. Retry and Recovery Behavior

### 8.1 Portal transport retry

`PortalClient` implements a two-level fallback:

```
Attempt 1: HTTP via adb forward (tcp:8080)
  → success → return response
  → ConnectionError / timeout → fall through

Attempt 2: ADB content provider
  → adb shell content query ...
  → parse output
  → if still fails → raise PortalConnectionError
```

No exponential backoff — the fallback is tried once per request.

### 8.2 ADB connectivity retry (scripts)

`startup_droidrun.ps1` and `reconnect_remote.ps1` try connection paths in order:
1. USB (if device is plugged in, ADB sees it directly)
2. WiFi (direct IP: `<device_ip>:5555`, port enabled via `adb tcpip 5555`)
3. Tailscale (`100.71.228.18:5555`)

`$ErrorActionPreference = "SilentlyContinue"` prevents early exit on failed connection attempts.

### 8.3 LLM call retry

LlamaIndex's built-in retry logic applies for transient API errors (rate limits, 5xx). The number of retries and backoff are controlled by the LLM client library, not by DroidRun directly.

### 8.4 No step-level retry

If an action fails (e.g., element not found, tap coordinates off-screen), DroidRun does **not** retry the same action. Instead, the next `[observe]` step will capture the current (unchanged) UI state and the LLM will decide the next action. Recovery is driven by the LLM's reasoning, not by explicit retry loops.
