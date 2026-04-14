# DroidRun Module Map

**Version:** 0.5.1 | All paths relative to repository root unless noted.

This document provides a module-by-module reference for every major package in the DroidRun source tree. Each entry includes: path, purpose, key files, inbound dependencies (what uses this module), and outbound dependencies (what this module uses).

---

## Table of Contents

1. [cli/](#1-cli)
2. [cli/tui/](#2-clitui)
3. [agent/droid/](#3-agentdroid)
4. [agent/codeact/](#4-agentcodeact)
5. [agent/manager/](#5-agentmanager)
6. [agent/executor/](#6-agentexecutor)
7. [agent/scripter/](#7-agentscripter)
8. [agent/oneflows/](#8-agentoneflows)
9. [agent/external/](#9-agentexternal)
10. [agent/trajectory/](#10-agenttrajectory)
11. [agent/utils/](#11-agentutils)
12. [tools/driver/](#12-toolsdriver)
13. [tools/android/](#13-toolsandroid)
14. [tools/ui/](#14-toolsui)
15. [tools/filters/](#15-toolsfilters)
16. [tools/formatters/](#16-toolsformatters)
17. [tools/helpers/](#17-toolshelpers)
18. [config_manager/](#18-config_manager)
19. [config/](#19-config)
20. [credential_manager/](#20-credential_manager)
21. [mcp/](#21-mcp)
22. [telemetry/](#22-telemetry)
23. [macro/](#23-macro)
24. [app_cards/](#24-app_cards)
25. [mcp_server.py](#25-mcp_serverpy-workspace-root)
26. [scripts/](#26-scripts)

---

## 1. `cli/`

**Path:** `src/droidrun/cli/`

**Purpose:** Primary human-facing entry point. Defines all Click command groups and commands that `droidrun` exposes on the PATH. Parses arguments, loads config, instantiates the correct agent strategy, and drives execution.

| Key File | Responsibility |
|---|---|
| `__init__.py` | Exports the top-level `cli` Click group |
| `main.py` | Registers sub-commands; sets up logging and telemetry |
| `run.py` | `droidrun run` — launches `DroidAgent` with a task string |
| `setup.py` | `droidrun setup` — interactive device pairing and config wizard |
| `ping.py` | `droidrun ping` — health-check against Portal APK |
| `doctor.py` | `droidrun doctor` — validates environment, ADB, LLM keys |
| `tui_cmd.py` | `droidrun tui` — launches Textual TUI |
| `macro_cmd.py` | `droidrun macro` — record/replay macro subcommands |

**Depends on:**

| Module | Reason |
|---|---|
| `agent/droid/` | Instantiates `DroidAgent` for `run` command |
| `config_manager/` | Loads `DroidrunConfig` and env keys |
| `telemetry/` | Initializes PostHog/Phoenix at startup |
| `tools/driver/` | Creates `AndroidDriver` for `ping`/`doctor` |
| `cli/tui/` | Delegates to Textual app for `tui` command |
| `macro/` | Record/replay logic for `macro` command |
| `click` | CLI framework |
| `rich` | Formatted terminal output |

**Used by:**

| Caller | How |
|---|---|
| `mcp_server.py` | Shares config loading; MCP server calls agent layer directly |
| System PATH (`droidrun`) | Installed as a console script via `pyproject.toml` |

---

## 2. `cli/tui/`

**Path:** `src/droidrun/cli/tui/`

**Purpose:** Interactive terminal UI built on Textual. Streams agent steps, screenshots (inline ASCII/sixel), logs, and device state in a multi-panel layout. Intended for live monitoring during long-running tasks.

| Key File | Responsibility |
|---|---|
| `app.py` | `DroidRunApp(App)` — Textual application entry point |
| `widgets/` | Custom Textual widgets: log panel, screenshot panel, step list |
| `screens/` | Task input screen, run screen, settings screen |
| `styles/` | Textual CSS (`droidrun.tcss`) |

**Depends on:**

| Module | Reason |
|---|---|
| `agent/droid/` | Subscribes to workflow events for live updates |
| `tools/driver/` | Fetches screenshots for inline display |
| `textual` | UI framework |
| `rich` | Markup inside Textual widgets |

**Used by:**

| Caller | How |
|---|---|
| `cli/tui_cmd.py` | `droidrun tui` launches `DroidRunApp().run()` |

---

## 3. `agent/droid/`

**Path:** `src/droidrun/agent/droid/`

**Purpose:** Top-level LlamaIndex workflow coordinator. Receives a task, selects an execution strategy based on config and task metadata, routes to the appropriate sub-agent, collects the result, and emits telemetry. Acts as the single integration point between the CLI/MCP layer and the individual agent strategies.

| Key File | Responsibility |
|---|---|
| `__init__.py` | Exports `DroidAgent` |
| `droid_agent.py` | `DroidAgent(Workflow)` — strategy selection, task lifecycle |
| `context.py` | Shared workflow context object passed between steps |
| `events.py` | LlamaIndex `Event` subclasses (TaskStarted, StepCompleted, TaskDone) |

**Depends on:**

| Module | Reason |
|---|---|
| `agent/codeact/` | Delegates to `FastAgent` / `CodeActAgent` for single-pass tasks |
| `agent/manager/` | Delegates to `ManagerAgent` for multi-step planning |
| `agent/executor/` | Used alongside `ManagerAgent` |
| `agent/scripter/` | Delegates Python script generation tasks |
| `agent/oneflows/` | Delegates specialized one-shot flows |
| `agent/utils/` | LLM loading, tracing setup |
| `tools/driver/` | Creates `AndroidDriver` instance |
| `telemetry/` | Emits task start/end events |
| `config_manager/` | Reads strategy selection config |
| `llama-index-workflows` | Workflow base class |

**Used by:**

| Caller | How |
|---|---|
| `cli/run.py` | `await DroidAgent(...).run(task=...)` |
| `mcp_server.py` | `phone_do` tool calls `DroidAgent` |
| `cli/tui/` | Subscribes to workflow events |

---

## 4. `agent/codeact/`

**Path:** `src/droidrun/agent/codeact/`

**Purpose:** Contains two single-pass agent variants. `FastAgent` uses XML-tagged tool calls in a single LLM round-trip — low latency, suitable for simple deterministic tasks. `CodeActAgent` extends this by generating and executing Python code blocks, enabling dynamic logic that goes beyond fixed tool schemas.

| Key File | Responsibility |
|---|---|
| `fast_agent.py` | `FastAgent(Workflow)` — XML tool parsing, single-pass execution |
| `codeact_agent.py` | `CodeActAgent(Workflow)` — Python code block generation + exec |
| `tool_parser.py` | Parses XML tool-call blocks from LLM output |
| `executor.py` | Executes parsed tool calls against the driver |
| `prompts.py` | System prompts for FastAgent and CodeActAgent |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Executes actions (tap, swipe, type, screenshot) |
| `tools/ui/` | Reads current `UIState` |
| `tools/filters/` | Applies element filters before LLM context |
| `tools/formatters/` | Formats element lists for the prompt |
| `agent/utils/` | `llm_loader.py`, `signatures.py` |
| `llama-index-workflows` | Workflow base class |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Selected when `strategy=fast` or `strategy=codeact` |

---

## 5. `agent/manager/`

**Path:** `src/droidrun/agent/manager/`

**Purpose:** High-level planning agent. Given a task, the `ManagerAgent` iteratively observes screen state, reasons about the next step (with `reasoning=True` for chain-of-thought), and issues a structured step instruction to the `ExecutorAgent`. `StatelessManagerAgent` is a variant that does not maintain cross-step state, useful for isolated sub-tasks.

| Key File | Responsibility |
|---|---|
| `manager_agent.py` | `ManagerAgent(Workflow)` — stateful planner |
| `stateless_manager.py` | `StatelessManagerAgent(Workflow)` — stateless variant |
| `planner.py` | Step generation logic; calls LLM with full screen context |
| `evaluator.py` | Checks if task is complete after each step |
| `prompts.py` | System prompts for planning and evaluation |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Captures screenshots and UI state for context |
| `tools/ui/` | `UIState` observation |
| `tools/filters/` | Prune UI element list before sending to LLM |
| `tools/formatters/` | Format elements for prompt |
| `agent/executor/` | Sends step instructions for execution |
| `agent/utils/` | LLM loading, tracing |
| `llama-index-workflows` | Workflow base class |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Selected when `strategy=manager` |

---

## 6. `agent/executor/`

**Path:** `src/droidrun/agent/executor/`

**Purpose:** Low-level action execution agent. Receives a structured step string from `ManagerAgent`, uses an LLM (with `reasoning=True`) to translate it into a concrete driver call (e.g., `tap(x, y)`), executes it, and returns the result. Handles retries and error recovery at the single-step level.

| Key File | Responsibility |
|---|---|
| `executor_agent.py` | `ExecutorAgent(Workflow)` — step-to-action translation |
| `action_runner.py` | Calls `AndroidDriver` methods; captures result |
| `retry.py` | Exponential backoff retry logic for flaky actions |
| `prompts.py` | System prompts for action translation |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Dispatches concrete actions |
| `agent/utils/` | `actions.py` action schema, LLM loading |
| `llama-index-workflows` | Workflow base class |

**Used by:**

| Caller | How |
|---|---|
| `agent/manager/` | Called after each plan step |
| `agent/droid/` | In manager+executor pipeline mode |

---

## 7. `agent/scripter/`

**Path:** `src/droidrun/agent/scripter/`

**Purpose:** Off-device Python script generation and execution. The `ScripterAgent` generates a Python script that uses the DroidRun driver API, executes it in a sandboxed subprocess on the host, and captures stdout/stderr as the result. Useful for data extraction, file processing, or complex conditional logic.

| Key File | Responsibility |
|---|---|
| `scripter_agent.py` | `ScripterAgent(Workflow)` — script gen + exec |
| `sandbox.py` | Subprocess isolation, timeout enforcement |
| `prompts.py` | System prompt with driver API reference |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Driver API reference injected into the script context |
| `agent/utils/` | LLM loading |
| `llama-index-workflows` | Workflow base class |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Selected when `strategy=scripter` |

---

## 8. `agent/oneflows/`

**Path:** `src/droidrun/agent/oneflows/`

**Purpose:** Collection of specialized single-purpose workflows for common sub-tasks that don't require the full manager+executor pipeline. Each is a self-contained LlamaIndex workflow.

| Key File | Responsibility |
|---|---|
| `app_starter.py` | `AppStarterWorkflow` — reliably launches an app by package name |
| `structured_output.py` | `StructuredOutputAgent` — extracts structured data (Pydantic) from screen |
| `text_manipulator.py` | `TextManipulator` — clipboard read/write, text field manipulation |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Device interaction |
| `tools/ui/` | UIState for structured extraction |
| `agent/utils/` | LLM loading |
| `llama-index-workflows` | Workflow base class |
| `pydantic` | Output schema validation in `StructuredOutputAgent` |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Delegated for app launch, data extraction sub-tasks |
| `agent/manager/` | Called as helper during planning |

---

## 9. `agent/external/`

**Path:** `src/droidrun/agent/external/`

**Purpose:** Thin adapter layer for integrating third-party autonomous agent backends. Currently hosts adapters for AutoGLM and MAI-UI, allowing external agents to drive the Android device through the same `AndroidDriver` interface.

| Key File | Responsibility |
|---|---|
| `autoglm_adapter.py` | Bridges AutoGLM agent calls to `AndroidDriver` |
| `mai_ui_adapter.py` | Bridges MAI-UI agent calls to `AndroidDriver` |
| `base_adapter.py` | Abstract base class for external adapters |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Executes actions issued by external agents |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Selected when `strategy=external` with provider flag |

---

## 10. `agent/trajectory/`

**Path:** `src/droidrun/agent/trajectory/`

**Purpose:** Records the full action trajectory of any agent run to a structured JSON file. Used for debugging, replay, dataset creation, and imitation learning.

| Key File | Responsibility |
|---|---|
| `trajectory_writer.py` | `TrajectoryWriter` — wraps a driver; intercepts all calls |
| `schema.py` | Pydantic models for trajectory frames |
| `replayer.py` | Reads trajectory JSON and replays via `AndroidDriver` |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | Wraps driver via decorator pattern |
| `pydantic` | Frame schema validation |

**Used by:**

| Caller | How |
|---|---|
| `tools/driver/RecordingDriver` | Delegates recording to `TrajectoryWriter` |
| `cli/macro_cmd.py` | `droidrun macro record` uses trajectory output |

---

## 11. `agent/utils/`

**Path:** `src/droidrun/agent/utils/`

**Purpose:** Shared utilities used across all agent modules. Includes action schema definitions, LLM instantiation helpers, provider selection logic, DSPy/LlamaIndex signature definitions, and OpenTelemetry tracing setup.

| Key File | Responsibility |
|---|---|
| `actions.py` | Canonical action schema (tap, swipe, type, keyevent, launch, …) |
| `llm_loader.py` | `load_llm(provider, model, api_key)` — returns LlamaIndex LLM |
| `llm_picker.py` | Selects provider/model from config; handles vision vs. no-vision |
| `signatures.py` | LlamaIndex `Signature` / DSPy-style typed prompt definitions |
| `tracing_setup.py` | Configures OpenTelemetry exporter to Arize-Phoenix or Langfuse |

**Depends on:**

| Module | Reason |
|---|---|
| `config_manager/` | Reads LLM provider config and API keys |
| `telemetry/` | Provides tracer instance |
| `llama-index` | LLM base classes |
| `pydantic` | Action schema models |

**Used by:**

| Caller | How |
|---|---|
| `agent/codeact/` | LLM loading, action schema |
| `agent/manager/` | LLM loading, signatures |
| `agent/executor/` | LLM loading, action schema |
| `agent/scripter/` | LLM loading |
| `agent/droid/` | Tracing setup at workflow start |

---

## 12. `tools/driver/`

**Path:** `src/droidrun/tools/driver/`

**Purpose:** Defines the `DeviceDriver` abstract base class and all concrete driver implementations. Every agent strategy talks to exactly one driver instance, keeping device-specific concerns isolated from agent logic.

| Key File | Responsibility |
|---|---|
| `base.py` | `DeviceDriver` ABC — tap, swipe, type, screenshot, get_ui_state, launch, keyevent |
| `android_driver.py` | `AndroidDriver` — wraps `PortalClient`; primary production driver |
| `cloud_driver.py` | `CloudDriver` — routes to `mobilerun-sdk` device farm |
| `ios_driver.py` | `IOSDriver` — iOS WebDriverAgent adapter (experimental) |
| `stealth_driver.py` | `StealthDriver` — decorates any driver with timing jitter |
| `recording_driver.py` | `RecordingDriver` — decorates any driver; records trajectory |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/android/` | `AndroidDriver` delegates to `PortalClient` |
| `tools/ui/` | Returns `UIState` from `get_ui_state()` |
| `tools/filters/` | Applied inside `get_ui_state()` |
| `tools/formatters/` | Used to format elements for agent prompts |
| `agent/trajectory/` | `RecordingDriver` writes via `TrajectoryWriter` |
| `mobilerun-sdk` | `CloudDriver` backend |
| `httpx` | `AndroidDriver` uses `PortalClient` which uses httpx |

**Used by:**

| Caller | How |
|---|---|
| `agent/codeact/` | Primary action interface |
| `agent/manager/` | Screenshot + UI state observation |
| `agent/executor/` | Action dispatch |
| `agent/scripter/` | Script execution context |
| `agent/oneflows/` | All device interactions |
| `cli/ping.py` | Health check |
| `cli/doctor.py` | Connectivity validation |

---

## 13. `tools/android/`

**Path:** `src/droidrun/tools/android/`

**Purpose:** HTTP client for the Portal APK. `PortalClient` wraps every Portal endpoint with typed Python methods. All network I/O is async via `httpx`. This is the only module that knows the Portal APK's HTTP schema.

| Key File | Responsibility |
|---|---|
| `portal_client.py` | `PortalClient` — typed async methods for all Portal endpoints |
| `models.py` | Pydantic response models matching Portal APK JSON |
| `endpoints.py` | Endpoint path constants |

**Depends on:**

| Module | Reason |
|---|---|
| `httpx` | Async HTTP requests to Portal APK |
| `pydantic` | Response model validation |

**Used by:**

| Caller | How |
|---|---|
| `tools/driver/android_driver.py` | All device interactions routed through here |

---

## 14. `tools/ui/`

**Path:** `src/droidrun/tools/ui/`

**Purpose:** UI state abstraction. `UIProvider` fetches raw element data from the driver and builds a `UIState` object — a structured snapshot of all visible UI elements with coordinates, text, resource IDs, and accessibility metadata.

| Key File | Responsibility |
|---|---|
| `ui_provider.py` | `UIProvider` — fetches + parses raw element tree |
| `ui_state.py` | `UIState` — typed container for current screen elements |
| `element.py` | `UIElement` Pydantic model (bounds, text, class, clickable, …) |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/android/` | Raw element JSON from Portal APK |
| `tools/filters/` | Applies filters to raw element list |
| `pydantic` | Element model validation |

**Used by:**

| Caller | How |
|---|---|
| `tools/driver/` | `get_ui_state()` returns `UIState` |
| `agent/manager/` | Observation step |
| `agent/codeact/` | Context for LLM prompt |
| `agent/oneflows/` | Structured extraction |

---

## 15. `tools/filters/`

**Path:** `src/droidrun/tools/filters/`

**Purpose:** Reduces the element list before it is included in an LLM prompt. Filters remove invisible, off-screen, or redundant elements to stay within context window limits.

| Key File | Responsibility |
|---|---|
| `concise_filter.py` | `ConciseFilter` — aggressive pruning; keeps only actionable elements |
| `detailed_filter.py` | `DetailedFilter` — conservative pruning; retains all visible elements |
| `base.py` | `ElementFilter` ABC |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/ui/` | Operates on `UIElement` list |

**Used by:**

| Caller | How |
|---|---|
| `tools/ui/UIProvider` | Applied during `UIState` construction |
| `tools/driver/AndroidDriver` | Config selects which filter to apply |

---

## 16. `tools/formatters/`

**Path:** `src/droidrun/tools/formatters/`

**Purpose:** Converts a filtered `UIState` into a string representation suitable for inclusion in an LLM prompt. `IndexedFormatter` assigns a numeric index to each element so the LLM can reference elements by index rather than by coordinates.

| Key File | Responsibility |
|---|---|
| `indexed_formatter.py` | `IndexedFormatter` — emits `[42] Button "Submit" (540,1200)` style text |
| `base.py` | `ElementFormatter` ABC |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/ui/` | Formats `UIState` / `UIElement` |

**Used by:**

| Caller | How |
|---|---|
| `agent/codeact/` | Prompt construction |
| `agent/manager/` | Prompt construction |
| `tools/driver/` | Pre-formats state for agent callbacks |

---

## 17. `tools/helpers/`

**Path:** `src/droidrun/tools/helpers/`

**Purpose:** Low-level geometric and search utilities shared across tools and agents.

| Key File | Responsibility |
|---|---|
| `coordinate.py` | Coordinate normalization, bounds-to-center calculation |
| `geometry.py` | Bounding box intersection, overlap detection, screen region helpers |
| `element_search.py` | Fuzzy text search over `UIElement` list; finds elements by label |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/ui/` | Operates on `UIElement` |

**Used by:**

| Caller | How |
|---|---|
| `tools/driver/` | Coordinate calculations for tap/swipe |
| `agent/executor/` | Element lookup by index or label |
| `agent/oneflows/` | Element search in specialized flows |

---

## 18. `config_manager/`

**Path:** `src/droidrun/config_manager/`

**Purpose:** Unified configuration loading. Merges values from environment variables, `~/.droidrun/config.yaml`, and optional `.env` files. Exposes a typed `DroidrunConfig` Pydantic model. Handles schema migrations between config versions.

| Key File | Responsibility |
|---|---|
| `loader.py` | `ConfigLoader` — discovers and merges config sources |
| `config.py` | `DroidrunConfig` Pydantic model with all config fields |
| `env_keys.py` | Constants for all `DROIDRUN_*` environment variable names |
| `migrations.py` | Version migration handlers (v1 → v2 → current) |

**Depends on:**

| Module | Reason |
|---|---|
| `pydantic` | Config model validation |
| `python-dotenv` | `.env` file loading |

**Used by:**

| Caller | How |
|---|---|
| `cli/` | Loaded at command startup |
| `agent/droid/` | Strategy selection from config |
| `agent/utils/llm_picker.py` | Provider/model selection |
| `tools/driver/` | Device IP, port, driver type |
| `telemetry/` | Telemetry opt-in/opt-out flag |

---

## 19. `config/`

**Path:** `src/droidrun/config/`

**Purpose:** Static configuration assets bundled with the package. Not executable code — contains default prompts, app card definitions, and a credentials example file for user onboarding.

| Key File | Responsibility |
|---|---|
| `app_cards.json` | Default app-specific instruction cards |
| `prompts/` | Default system prompt templates (Jinja2 or plain text) |
| `credentials_example.yaml` | Commented example of `~/.droidrun/config.yaml` |

**Depends on:** none (static data)

**Used by:**

| Caller | How |
|---|---|
| `config_manager/loader.py` | Reads `credentials_example.yaml` for onboarding help |
| `app_cards/` | Merges with user-defined cards |
| `agent/*/prompts.py` | Loads default prompt templates |

---

## 20. `credential_manager/`

**Path:** `src/droidrun/credential_manager/`

**Purpose:** Manages credentials for apps that require login (e.g., stored username/password for test accounts). `FileCredentialManager` reads from an encrypted local YAML. `CredentialManager` is the abstract interface.

| Key File | Responsibility |
|---|---|
| `credential_manager.py` | `CredentialManager` ABC |
| `file_manager.py` | `FileCredentialManager` — reads `~/.droidrun/credentials.yaml` |
| `models.py` | `AppCredential` Pydantic model |

**Depends on:**

| Module | Reason |
|---|---|
| `pydantic` | Model validation |
| `config_manager/` | Credential file path from config |

**Used by:**

| Caller | How |
|---|---|
| `agent/oneflows/` | Login flows that need credentials |
| `agent/manager/` | Injects credentials into task context |

---

## 21. `mcp/`

**Path:** `src/droidrun/mcp/`

**Purpose:** MCP client-side integration. `MCPClientManager` manages connections to external MCP servers (e.g., filesystem, browser tools) that agents can call as tools. Includes config parsing for MCP server definitions and an adapter that wraps MCP tools as LlamaIndex tools.

| Key File | Responsibility |
|---|---|
| `client_manager.py` | `MCPClientManager` — connects to and manages MCP server processes |
| `adapter.py` | Wraps MCP tool descriptors as LlamaIndex `FunctionTool` |
| `config.py` | Parses MCP server config from `~/.droidrun/mcp_servers.json` |

**Depends on:**

| Module | Reason |
|---|---|
| `mcp` (≥1.26.0) | MCP SDK for stdio client transport |
| `llama-index` | `FunctionTool` wrapping |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Loads MCP tools into agent tool registry |
| `agent/codeact/` | MCP tools available alongside built-in tools |

---

## 22. `telemetry/`

**Path:** `src/droidrun/telemetry/`

**Purpose:** Non-blocking telemetry emission. Sends usage events to PostHog (product analytics) and trace spans to Arize-Phoenix (LLM observability). Langfuse is an optional alternative backend. All emission is async and fire-and-forget — failures are silently swallowed.

| Key File | Responsibility |
|---|---|
| `posthog_client.py` | `PosthogTelemetry` — event emission to PostHog |
| `phoenix_client.py` | `PhoenixTracer` — OpenTelemetry span exporter to Arize-Phoenix |
| `langfuse_client.py` | `LangfuseTracer` — optional Langfuse backend |
| `base.py` | `TelemetryBackend` ABC |

**Depends on:**

| Module | Reason |
|---|---|
| `posthog` | PostHog Python SDK |
| `arize-phoenix` | Phoenix OpenTelemetry exporter |
| `config_manager/` | `DROIDRUN_TELEMETRY` flag and project ID |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Task start/end events |
| `agent/utils/tracing_setup.py` | Tracer initialization |
| `cli/main.py` | Telemetry init at process start |

---

## 23. `macro/`

**Path:** `src/droidrun/macro/`

**Purpose:** Record and replay action macros. Recording captures all driver calls (via `RecordingDriver`) to a macro JSON file. Replay reads the file and replays actions deterministically, optionally with timing scaling.

| Key File | Responsibility |
|---|---|
| `recorder.py` | `MacroRecorder` — drives `RecordingDriver`; saves macro JSON |
| `replayer.py` | `MacroReplayer` — reads macro JSON; dispatches actions |
| `schema.py` | `MacroFrame` Pydantic model |

**Depends on:**

| Module | Reason |
|---|---|
| `tools/driver/` | `RecordingDriver` for capture; any driver for replay |
| `agent/trajectory/` | Shares trajectory schema format |
| `pydantic` | Frame validation |

**Used by:**

| Caller | How |
|---|---|
| `cli/macro_cmd.py` | `droidrun macro record` / `droidrun macro replay` |

---

## 24. `app_cards/`

**Path:** `src/droidrun/app_cards/`

**Purpose:** App-specific instruction overlays. An "app card" is a JSON/YAML snippet that provides the agent with app-specific hints (known element IDs, login flows, navigation patterns) for a specific Android package. Merged with the base system prompt at runtime.

| Key File | Responsibility |
|---|---|
| `loader.py` | `AppCardLoader` — loads built-in + user-defined cards |
| `models.py` | `AppCard` Pydantic model |
| `registry.py` | `AppCardRegistry` — looks up card by package name |

**Depends on:**

| Module | Reason |
|---|---|
| `config/app_cards.json` | Built-in default cards |
| `config_manager/` | User card directory from config |
| `pydantic` | Card model validation |

**Used by:**

| Caller | How |
|---|---|
| `agent/droid/` | Injects app card into system prompt before task start |
| `agent/manager/` | App card included in planning prompt |

---

## 25. `mcp_server.py` (workspace root)

**Path:** `mcp_server.py`

**Purpose:** Workspace-level MCP server that exposes DroidRun capabilities to AI clients (Cursor, Claude Desktop, OpenClaw) over stdio JSON-RPC. Not part of the installable package — runs as a separate process launched by the AI client's MCP configuration.

| Tool Name | Signature | Behavior |
|---|---|---|
| `phone_do` | `task: str` → `str` | Runs `DroidAgent` with the given task; returns result text |
| `phone_ping` | `()` → `bool` | Pings Portal APK; returns `True` if reachable |
| `phone_apps` | `()` → `list[str]` | Returns list of installed package names |

**Depends on:**

| Module | Reason |
|---|---|
| `agent/droid/` | `DroidAgent` for `phone_do` |
| `tools/driver/` | `AndroidDriver` for `phone_ping` and `phone_apps` |
| `config_manager/` | Config loading |
| `mcp` (≥1.26.0) | MCP server SDK |

**Used by:**

| Caller | How |
|---|---|
| Cursor IDE | Via `.cursor/mcp.json` stdio transport |
| Claude Desktop | Via `claude_desktop_config.json` stdio transport |
| OpenClaw | Via MCP gateway config |

---

## 26. `scripts/`

**Path:** `scripts/` (repository root)

**Purpose:** PowerShell automation scripts for Windows host setup, ADB management, secret injection, and process lifecycle. These are developer-tooling scripts, not part of the Python package.

| Script | Purpose |
|---|---|
| `startup_droidrun.ps1` | Master startup: calls `bws run` → injects secrets → launches Cursor/terminal |
| `adb_connect.ps1` | Connects ADB over TCP to device at configured Tailscale IP and port |
| `adb_disconnect.ps1` | Disconnects ADB TCP connection |
| `adb_restart.ps1` | Kills and restarts ADB server; re-connects |
| `check_portal.ps1` | Health-checks Portal APK HTTP endpoint |
| `inject_secrets.ps1` | Reads from Bitwarden; sets `HKCU\Environment` vars |
| `clear_secrets.ps1` | Removes secrets from `HKCU\Environment` |
| `install_portal.ps1` | Pushes Portal APK to device via ADB and starts the service |
| `install_deps.ps1` | Creates venv, installs `droidrun[dev]` with all extras |
| `run_tests.ps1` | Runs pytest with coverage in the correct venv |
| `kill_droidrun.ps1` | Kills all running `droidrun` and `mcp_server.py` processes |
| `update_env.ps1` | Re-syncs `HKCU\Environment` from `.env.local` (local dev only) |

**Depends on:**

| Tool | Reason |
|---|---|
| `bws` (Bitwarden Secrets CLI) | Secret retrieval in `startup_droidrun.ps1` and `inject_secrets.ps1` |
| `adb` | Device connectivity scripts |
| PowerShell 7+ | All scripts require `pwsh` |

**Used by:** Developers directly; not called from Python code.

---

## Dependency Graph Summary

```
mcp_server.py
    └─ agent/droid/ ────────────────────────────────────────┐
         ├─ agent/codeact/                                   │
         ├─ agent/manager/ ─── agent/executor/               │
         ├─ agent/scripter/                                  │
         ├─ agent/oneflows/                                  │
         └─ agent/utils/ ──── config_manager/               │
                                                             │
cli/ ────────────────────────────────────────────────────────┤
    ├─ cli/tui/                                              │
    ├─ macro/ ──── agent/trajectory/                         │
    └─ app_cards/                                            │
                                                             │
All agents ──► tools/driver/ ──► tools/android/ (PortalClient)
                   ├─ tools/ui/ ──► tools/filters/
                   ├─ tools/formatters/
                   └─ tools/helpers/

config_manager/ ◄── all modules that need config
credential_manager/ ◄── agent/oneflows/, agent/manager/
mcp/ ◄── agent/droid/
telemetry/ ◄── agent/droid/, cli/, agent/utils/
```
