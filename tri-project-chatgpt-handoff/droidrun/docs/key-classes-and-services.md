# DroidRun — Key Classes and Services

> DroidRun v0.5.1 · Python asyncio · LlamaIndex Workflows

This document describes every major class and service in the DroidRun codebase: what it does, what it consumes, what it produces, and why it exists.

---

## 1. DroidAgent

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/droid/droid_agent.py` |
| **Base class** | `llama_index.core.workflow.Workflow` |
| **Role** | Top-level orchestrator; owns the full task lifecycle |

### Inputs
- `task: str` — natural-language instruction from the user or MCP caller
- `config: DroidrunConfig` — full configuration object
- `llm` — resolved LLM client (OpenAI, Anthropic, DeepSeek, etc.)
- `serial: str | None` — ADB device serial (explicit or auto-detected)

### Outputs
- `result: dict` — `{"success": bool, "message": str, "steps": int}`
- Side effect: trajectory files written to `trajectories/` (if enabled)

### Key dependencies
`AndroidDriver`, `PortalClient`, `UIProvider`, `TrajectoryWriter`, one of `FastAgent` / (`ManagerAgent` + `ExecutorAgent`)

### Why it matters
`DroidAgent` is the single object the CLI, the TUI, and the MCP server all instantiate. It selects the agent mode, wires every sub-component together, and owns the `asyncio` event loop handoff from the synchronous CLI layer.

---

## 2. FastAgent

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/codeact/` |
| **Role** | Default single-agent executor; used when `reasoning=False` |

### Inputs
- Current UI state string (from `UIProvider`)
- Task / sub-task description
- LLM client

### Outputs
- `Action` object (tap, swipe, type, scroll, launch, etc.)
- `done: bool` flag indicating task completion

### Key dependencies
`UIProvider`, `IndexedFormatter`, `ConciseFilter`, LLM client

### Why it matters
FastAgent is the "happy path." It handles the majority of real-world tasks with a single LLM call per step: observe → generate action → execute. No multi-agent overhead.

---

## 3. CodeActAgent

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/codeact/` |
| **Role** | Code-execution variant of FastAgent; generates and runs Python snippets |

### Inputs
- Same as FastAgent
- Python execution sandbox (via `exec` in a restricted namespace)

### Outputs
- Executed action(s) derived from generated code
- stdout/stderr of executed snippet (fed back into the next LLM prompt)

### Key dependencies
`UIProvider`, `AndroidDriver` (injected into the execution namespace), LLM client

### Why it matters
CodeActAgent enables multi-step action sequences expressed as Python rather than structured JSON. Useful for tasks that require branching logic (e.g., "if the button is grayed out, scroll down first").

---

## 4. ManagerAgent

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/manager/` |
| **Role** | High-level planner; used when `reasoning=True` |

### Inputs
- Full task string
- LLM client (typically a more capable model)

### Outputs
- Ordered list of sub-tasks (strings)
- Final aggregated result after all sub-tasks complete

### Key dependencies
`ExecutorAgent` (calls it per sub-task), LLM client

### Why it matters
Reasoning mode decomposes complex, multi-step tasks (e.g., "book a flight and send a confirmation email") into smaller, verifiable chunks. ManagerAgent owns the decomposition and progress tracking.

---

## 5. ExecutorAgent

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/executor/` |
| **Role** | Executes a single sub-task assigned by ManagerAgent |

### Inputs
- Sub-task string from ManagerAgent
- Current device state (re-observed at start of each sub-task)
- LLM client

### Outputs
- Sub-task result: `{"success": bool, "message": str}`

### Key dependencies
`UIProvider`, `AndroidDriver`, LLM client

### Why it matters
ExecutorAgent is the leaf node in reasoning mode. It runs an observe-act loop identical to FastAgent but scoped to one sub-task, allowing ManagerAgent to retry or replan if a sub-task fails.

---

## 6. ScripterAgent

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/scripter/` |
| **Role** | Runs off-device Python scripts to augment on-device actions |

### Inputs
- Script instructions or file path
- LLM client

### Outputs
- Script output (stdout) fed back as observation

### Key dependencies
Python subprocess / exec environment, LLM client

### Why it matters
Some tasks require off-device computation (e.g., parsing a web page, computing a value) that cannot be done through the Android UI. ScripterAgent handles these detours without blocking the main workflow.

---

## 7. AndroidDriver

| Field | Value |
|-------|-------|
| **Path** | `droidrun/tools/driver/android.py` |
| **Role** | ADB device driver; translates high-level actions into `adb` commands |

### Inputs
- `serial: str` — device serial
- `Action` objects (tap, swipe, type, key, launch, scroll, screenshot, …)

### Outputs
- Return values from `adb shell` commands (stdout strings)
- `bytes` for screenshot data

### Key dependencies
`subprocess` (calls `adb` binary), `PortalClient` (for UI-tree-aware taps)

### Why it matters
Every interaction with the physical or emulated Android device flows through `AndroidDriver`. It is the single source of truth for device I/O and the natural place to add new action types.

---

## 8. PortalClient

| Field | Value |
|-------|-------|
| **Path** | `droidrun/tools/android/portal_client.py` |
| **Role** | HTTP client to the Portal APK running on the device |

### Inputs
- Base URL `http://localhost:8080` (after `adb forward tcp:8080 tcp:8080`)
- Request type: `GET /ui`, `GET /ping`, `POST /action`

### Outputs
- Raw accessibility-tree XML string
- HTTP status / action acknowledgement

### Transport fallback
1. **Primary:** `httpx.AsyncClient` over forwarded TCP port 8080
2. **Fallback:** `adb shell content query --uri content://com.droidrun.portal.provider/ui`

### Key dependencies
`httpx` (async HTTP), `AndroidDriver` (for fallback ADB commands)

### Why it matters
The Portal APK is the only reliable way to obtain the full Android accessibility tree at runtime. `PortalClient` abstracts the transport so the rest of the stack does not care whether TCP or ADB content provider is used.

---

## 9. UIProvider

| Field | Value |
|-------|-------|
| **Path** | `droidrun/tools/ui/provider.py` |
| **Role** | Fetches, filters, and formats the current UI state |

### Inputs
- `PortalClient` instance
- Filter configuration (from `DroidrunConfig`)

### Outputs
- Annotated, indexed XML string ready for the LLM prompt

### Pipeline
```
PortalClient.get_ui_tree()
  → raw XML
  → ConciseFilter.prune()     (remove irrelevant nodes)
  → IndexedFormatter.format() (add [idx] annotations)
  → return string
```

### Key dependencies
`PortalClient`, `ConciseFilter`, `IndexedFormatter`

### Why it matters
`UIProvider` is the bridge between raw Android accessibility data and the structured text the LLM needs. Poor filtering here increases token cost and hallucination risk; good filtering keeps prompts tight.

---

## 10. IndexedFormatter

| Field | Value |
|-------|-------|
| **Path** | `droidrun/tools/formatters/` |
| **Role** | Annotates accessibility tree nodes with integer indices |

### Inputs
- Pruned accessibility tree (XML / dict)

### Outputs
- XML string where each interactive element has a `[0]`, `[1]`, … prefix

### Why it matters
The LLM refers to UI elements by index (`tap [3]`) rather than by raw coordinates. `IndexedFormatter` creates and maintains the mapping between index and element, which `AndroidDriver` then resolves back to screen coordinates at action time.

---

## 11. ConciseFilter

| Field | Value |
|-------|-------|
| **Path** | `droidrun/tools/filters/` |
| **Role** | Prunes the raw accessibility tree to reduce noise |

### Inputs
- Full accessibility tree from `PortalClient`
- Filter rules (configurable: remove non-interactive, collapse single-child, max-depth, etc.)

### Outputs
- Reduced tree (same structure, fewer nodes)

### Why it matters
Android accessibility trees can contain hundreds of nodes (system decorations, invisible elements, deeply nested layouts). Passing the full tree to the LLM wastes tokens and degrades action accuracy. `ConciseFilter` typically reduces tree size by 60–80%.

---

## 12. ConfigLoader

| Field | Value |
|-------|-------|
| **Path** | `droidrun/config_manager/loader.py` |
| **Role** | Reads and merges configuration from file + environment |

### Inputs
- Config file path (default: `~/.config/droidrun/config.yaml`)
- Environment variables (override file values)

### Outputs
- `DroidrunConfig` instance

### Merge priority
`env vars` > `config file` > `built-in defaults`

### Key dependencies
`PyYAML`, `pydantic` (via `DroidrunConfig`)

### Why it matters
`ConfigLoader` is called at the start of every CLI command. Every component downstream receives a fully resolved `DroidrunConfig` rather than reading env vars directly, which keeps configuration concerns in one place.

---

## 13. DroidrunConfig

| Field | Value |
|-------|-------|
| **Path** | `droidrun/config_manager/config_manager.py` |
| **Role** | Typed configuration schema (Pydantic model) |

### Key fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `provider` | str | `"openai"` | LLM provider name |
| `model` | str | provider default | Model identifier |
| `reasoning` | bool | `False` | Enable ManagerAgent mode |
| `max_steps` | int | `15` | Hard cap on observe-act cycles |
| `auto_setup` | bool | `True` | Download/install Portal APK automatically |
| `save_trajectory` | str | `"none"` | `"none"` / `"steps"` / `"full"` |
| `wait_for_stable_ui` | float | `0.3` | Seconds to wait after each action |
| `after_sleep` | float | `1.0` | Seconds to sleep between steps |

### Why it matters
A single validated config object eliminates scattered `os.getenv()` calls throughout the codebase and makes it easy to test components in isolation by injecting a mock config.

---

## 14. MCPClientManager

| Field | Value |
|-------|-------|
| **Path** | `droidrun/mcp/client.py` |
| **Role** | Consumes external MCP servers from within DroidRun |

### Inputs
- MCP server connection spec (stdio command or SSE URL)
- Tool name + arguments

### Outputs
- Tool call results (strings, dicts)

### Key dependencies
`mcp` Python SDK (Anthropic), async stdio/SSE transport

### Why it matters
DroidRun can itself be an MCP *client* — e.g., calling a web-search MCP server during task execution. `MCPClientManager` manages the connection lifecycle so agent steps can call external tools without boilerplate.

---

## 15. TrajectoryWriter

| Field | Value |
|-------|-------|
| **Path** | `droidrun/agent/trajectory/` |
| **Role** | Records per-step execution data to disk |

### Inputs
- Step index, UI tree XML, LLM prompt, LLM response, action taken, timestamp
- Output directory derived from `DroidrunConfig.save_trajectory`

### Outputs
- JSON files written to `trajectories/<ISO-timestamp>/step_<n>.json`

### Behaviour
- Writes are async (`aiofiles`) so they do not block the observe-act loop.
- If `save_trajectory == "none"`, `TrajectoryWriter` is a no-op (all methods return immediately).
- Files are never read back by DroidRun; they are for offline analysis only.

### Why it matters
Trajectories are the primary tool for debugging agent behaviour, building evaluation datasets, and understanding why a run succeeded or failed.

---

## 16. mcp_server.py

| Field | Value |
|-------|-------|
| **Path** | `mcp_server.py` (repository root) |
| **Role** | Exposes DroidRun to AI clients (Claude Desktop, etc.) as an MCP server |

### Transport
stdio JSON-RPC 2.0

### Tools exposed

| Tool | Maps to | Description |
|------|---------|-------------|
| `phone_do` | `droidrun run <task>` | Execute a natural-language task on the connected device |
| `phone_ping` | `droidrun ping` | Check that DroidRun and the Portal APK are reachable |
| `phone_apps` | `droidrun run "list installed apps"` | Return a list of installed app package names |

### How tools are invoked
Each tool call runs `subprocess.run(["droidrun", ...], timeout=300, capture_output=True)`. This means every `phone_do` spawns a full DroidRun process including config loading, device detection, and LLM calls.

### Startup
`mcp.Server("droidrun").run(transport="stdio")` — blocks on stdin, exits when stdin closes.

### Why it matters
`mcp_server.py` is the integration layer between DroidRun's Python CLI and any MCP-compatible AI client. It requires no changes to the core DroidRun package and keeps the server stateless.
