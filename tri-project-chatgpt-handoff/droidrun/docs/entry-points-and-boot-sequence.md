# DroidRun — Entry Points and Boot Sequences

> DroidRun v0.5.1 · Python asyncio · LlamaIndex Workflows

This document maps every way to start DroidRun — CLI commands, Python SDK import, and MCP server — and traces exactly what happens before the first user-visible action.

---

## 1. Primary Entry Point

### 1.1 Registered script

`pyproject.toml` declares:

```toml
[project.scripts]
droidrun = "droidrun.cli.main:cli"
```

`pip install droidrun` (or `pip install -e .`) writes a `droidrun` wrapper script into the active virtualenv's `bin/` (Linux/macOS) or `Scripts/` (Windows). The wrapper imports `droidrun.cli.main` and calls `cli()`.

### 1.2 `DroidRunCLI` — the Click group

`cli` is an instance of `DroidRunCLI`, a custom `click.Group` subclass. Before Click dispatches to any sub-command, `DroidRunCLI.invoke()` runs shared pre-flight logic:

1. Determine config path from `--config` flag or default (`~/.config/droidrun/config.yaml`).
2. Call `ConfigLoader.load(config_path)` → `DroidrunConfig`.
3. Set log level based on `--verbose` / `--quiet`.
4. Store config on `click.Context` for sub-commands to retrieve.

---

## 2. CLI Sub-Command Boot Sequences

### 2.1 `droidrun run <task>`

```
droidrun run "open Settings and enable dark mode"
│
├─ 1. ConfigLoader.load() → DroidrunConfig
├─ 2. Resolve device serial
│      --serial flag?  → use it
│      else            → adb devices → pick first online
│
├─ 3. auto_setup check (if config.auto_setup == True)
│      adb shell pm list packages | grep com.droidrun.portal
│      missing? → download APK from GitHub releases
│               → adb install -r <apk>
│               → adb shell settings put secure enabled_accessibility_services \
│                     com.droidrun.portal/com.droidrun.portal.service.DroidrunAccessibilityService
│
├─ 4. adb forward tcp:8080 tcp:8080
│
├─ 5. DroidAgent.__init__(task, config, serial)
│      → AndroidDriver(serial)
│      → PortalClient(driver)
│      → UIProvider(portal)
│      → resolve_llm(config)
│      → TrajectoryWriter(config)
│      → register workflow steps (FastAgent OR ManagerAgent+ExecutorAgent)
│
├─ 6. asyncio.run(agent.run(task))
│      → workflow StartEvent → observe → plan → act → ... → StopEvent
│
└─ 7. Print result; exit 0 (success) or 1 (failure / interrupted)
```

**What happens before first user interaction:** steps 1–5 complete synchronously before any LLM call or device touch.

---

### 2.2 `droidrun setup`

```
droidrun setup [--serial <serial>]
│
├─ 1. ConfigLoader.load() → DroidrunConfig
├─ 2. Resolve device serial
├─ 3. AndroidDriver(serial)  (ADB only, no Portal yet)
│
├─ 4. Fetch latest Portal APK URL from GitHub API
│      GET https://api.github.com/repos/droidrun/droidrun/releases/latest
│      → find asset matching *.apk
│
├─ 5. Download APK to tempfile
├─ 6. adb install -r <apk>
├─ 7. Enable accessibility service (adb shell settings put ...)
├─ 8. adb forward tcp:8080 tcp:8080
├─ 9. PortalClient.ping() → verify Portal is responding
│
└─ 10. Print "Setup complete"; exit 0
```

---

### 2.3 `droidrun ping`

```
droidrun ping [--serial <serial>]
│
├─ 1. ConfigLoader.load() → DroidrunConfig
├─ 2. Resolve device serial
├─ 3. AndroidDriver(serial)
├─ 4. adb forward tcp:8080 tcp:8080
├─ 5. PortalClient.ping()
│      → HTTP GET http://localhost:8080/ping
│      → record round-trip time
│
└─ 6. Print latency; exit 0 (reachable) or 1 (unreachable)
```

---

### 2.4 `droidrun doctor`

```
droidrun doctor [--serial <serial>]
│
├─ 1. ConfigLoader.load() → DroidrunConfig
├─ 2. Check ADB binary present (subprocess which adb / where adb)
├─ 3. Check device reachable (adb -s <serial> get-state)
├─ 4. Check Portal APK installed (adb shell pm list packages)
├─ 5. Check accessibility service enabled
│      adb shell settings get secure enabled_accessibility_services
│      → contains com.droidrun.portal?
├─ 6. Check LLM credentials
│      → env vars present for configured provider?
├─ 7. PortalClient.ping() → TCP reachable?
│
└─ 8. Print pass/warn/fail table; exit 0 (all pass) or 1 (any fail)
```

---

### 2.5 `droidrun tui`

```
droidrun tui [--serial <serial>]
│
├─ 1. ConfigLoader.load() → DroidrunConfig
├─ 2. Resolve device serial
├─ 3. DroidAgent.__init__(...)     (same as `run`)
│
├─ 4. Launch Textual app (DroidRunApp)
│      → renders task input field + live log pane + UI tree pane
│
├─ 5. On task submit (Enter):
│      asyncio task → DroidAgent.run(task)
│      → streams StepEvent objects back to TUI for live display
│
└─ 6. On Ctrl+C or window close: cancel asyncio task, exit
```

---

### 2.6 `droidrun macro <file>`

```
droidrun macro tasks.yaml [--serial <serial>]
│
├─ 1. ConfigLoader.load() → DroidrunConfig
├─ 2. Resolve device serial
├─ 3. Parse YAML macro file → list of task strings
│
├─ 4. For each task:
│      DroidAgent.__init__(task, config, serial)
│      asyncio.run(agent.run(task))
│      → print result
│      → if result.success == False and macro.stop_on_failure: break
│
└─ 5. Print summary (N succeeded / M failed); exit 0 or 1
```

A new `DroidAgent` is created per task. No state carries between tasks.

---

## 3. DroidAgent Boot Sequence (Detailed)

This sequence applies to every code path that instantiates `DroidAgent`.

```
DroidAgent.__init__(task, config, llm=None, serial=None)
│
├─ 1. Resolve serial
│      serial arg → use as-is
│      else       → adb devices → first online device
│
├─ 2. AndroidDriver(serial)
│      stores serial, verifies adb binary is on PATH
│      no I/O yet
│
├─ 3. PortalClient(driver)
│      stores driver reference
│      no connection yet
│
├─ 4. UIProvider(portal, config)
│      stores portal + filter config
│      no connection yet
│
├─ 5. resolve_llm(config)
│      match config.provider:
│        "openai"    → OpenAI(api_key=OPENAI_API_KEY, model=config.model)
│        "anthropic" → Anthropic(api_key=ANTHROPIC_API_KEY, ...)
│        "deepseek"  → OpenAI-compatible client(DROIDRUN_DEEPSEEK_KEY, ...)
│        "openrouter"→ OpenAI-compatible client(DROIDRUN_OPENROUTER_KEY, ...)
│        "gemini"    → Gemini(api_key=GOOGLE_API_KEY, ...)
│
├─ 6. TrajectoryWriter(config)
│      if config.save_trajectory == "none": no-op singleton
│      else: create trajectories/<ISO-timestamp>/ directory
│
├─ 7. Select agent mode
│      config.reasoning == False:
│        register FastAgent steps on workflow
│      config.reasoning == True:
│        register ManagerAgent + ExecutorAgent steps on workflow
│
└─ 8. return (no async I/O has occurred)

asyncio.run(agent.run(task))
│
├─ 9.  Emit StartEvent(task)
├─ 10. First [observe]: PortalClient connects (TCP or ADB fallback)
│       → first actual device I/O
├─ 11. First LLM call
│       → first actual network I/O
└─ 12. Execution loop begins
```

---

## 4. MCP Server Boot Sequence

```
python mcp_server.py
│
├─ 1. Import mcp SDK
├─ 2. mcp.Server("droidrun")
├─ 3. Register tools:
│      @server.tool("phone_do")   → handler_phone_do
│      @server.tool("phone_ping") → handler_phone_ping
│      @server.tool("phone_apps") → handler_phone_apps
│
├─ 4. server.run(transport="stdio")
│      → reads JSON-RPC from stdin indefinitely
│      → no ADB, no config, no LLM at this point
│
└─ (blocking; exits only when stdin closes)

On tool call received (e.g. phone_do):
│
├─ 5. subprocess.run(
│       ["droidrun", "run", task, "--serial", serial],
│       timeout=300,
│       capture_output=True
│     )
│      → full CLI boot sequence (steps 1–7 in §2.1) runs in child process
│
└─ 6. Return child process stdout as tool result string
```

There is no shared state between the MCP server process and the `droidrun` child processes it spawns.

---

## 5. Python Library Entry Point (SDK Usage)

DroidRun can be used as a library without the CLI:

```python
import asyncio
from droidrun import DroidAgent
from droidrun.config_manager import ConfigLoader

config = ConfigLoader.load()  # reads ~/.config/droidrun/config.yaml + env
agent = DroidAgent(task="open Chrome", config=config)
result = asyncio.run(agent.run())
print(result)
```

### What this does before any user-visible action

1. `ConfigLoader.load()` — reads config file and env vars.
2. `DroidAgent.__init__()` — same 8-step sequence as §3 above (no I/O).
3. `asyncio.run(agent.run())` — starts the event loop; first I/O is step 10 (Portal connect).

No background threads or daemon processes are started. The entire execution is contained in the calling thread's event loop.

---

## 6. Dependency Graph Bootstrap

Every entry point ultimately resolves the same dependency chain before first action:

```
DroidrunConfig (ConfigLoader.load)
    │
    ├──► LLM client (resolve_llm)
    │         └──► LLM API (first call: step 11)
    │
    ├──► AndroidDriver (serial)
    │         └──► adb binary (first call: step 10 or auto_setup)
    │
    ├──► PortalClient (driver)
    │         └──► Portal APK on device (first call: step 10)
    │                   └──► DroidrunAccessibilityService
    │
    ├──► UIProvider (portal, config)
    │         └──► ConciseFilter
    │         └──► IndexedFormatter
    │
    ├──► TrajectoryWriter (config)
    │         └──► trajectories/ directory on disk
    │
    └──► Agent steps (FastAgent OR ManagerAgent+ExecutorAgent)
              └──► registered on LlamaIndex Workflow
```

All nodes above the "first call" annotations are constructed synchronously in `__init__`. No network or device I/O occurs until `agent.run()` is awaited.
