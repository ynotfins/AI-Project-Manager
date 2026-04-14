# Glossary — DroidRun

All terms, acronyms, module names, and configuration keys used in this repository.

---

## A

**ADB (Android Debug Bridge)**
Platform tool from Android SDK. Enables communication with Android devices over USB, Wi-Fi, or TCP/IP. DroidRun uses ADB to install the Portal APK, forward ports, and invoke device commands via `async_adbutils`.

**Accessibility Service**
Android system service that DroidRun's Portal APK registers (`com.droidrun.portal/com.droidrun.portal.service.DroidrunAccessibilityService`). Provides the accessibility tree (UI element hierarchy) to the Portal HTTP API.

**ActionContext**
Data structure passed to agent action functions, carrying the current device driver, UI state, and config. Defined in `src/droidrun/agent/action_context.py`.

**ActionResult**
Return type from action functions. Carries `success` bool and `summary` string. Defined in `src/droidrun/agent/action_result.py`.

**AndroidDriver**
Class in `src/droidrun/tools/driver/android.py`. Concrete implementation of `DeviceDriver` for physical/emulated Android devices. Wraps `async_adbutils` ADB operations and delegates UI/input commands to `PortalClient`.

**app_cards**
Module (`src/droidrun/app_cards/`) providing app-specific instruction metadata to help the agent interact with specific applications. Supports local (file-based), server (HTTP), and composite (server+local fallback) modes.

**AppStarter / AppStarterWorkflow**
LlamaIndex Workflow in `src/droidrun/agent/oneflows/app_starter_workflow.py`. Handles app launch as a discrete sub-workflow, separate from the main task loop.

**Arize Phoenix**
Open-source LLM observability platform. DroidRun can send traces to a local or remote Phoenix instance. Configured via `tracing.provider = phoenix`.

**async_adbutils**
Python library providing async ADB device communication. DroidRun's primary interface to ADB.

**auto_setup**
Config flag (`device.auto_setup`, default `true`). When enabled, DroidRun automatically downloads and installs the Portal APK on the connected device before each run.

---

## B

**Bitwarden Secrets Manager (BWS)**
Cloud secret manager. Stores machine secrets accessed programmatically. DroidRun workspace uses it to inject API keys during startup.

**bws CLI**
Command-line tool for Bitwarden Secrets Manager. PowerShell startup scripts invoke `bws secret get <id>` to retrieve API key values.

**BWS_DROIDRUN_TOKEN**
The Bitwarden Secrets Manager machine account access token for this workspace. Stored in the regular Bitwarden vault (not in code). Required by `startup_droidrun.ps1`.

---

## C

**CodeActAgent**
Agent in `src/droidrun/agent/codeact/` that generates and executes Python code snippets to perform device actions. Used when `codeact: true` is set in config.

**codeact mode**
Execution mode where the agent writes Python code to perform actions, executed in a sandboxed evaluator. Contrasts with tool-calling mode (XML tools).

**ConfigLoader**
Class in `src/droidrun/config_manager/loader.py`. Reads a YAML config file, applies defaults, runs schema migrations, and returns a `DroidrunConfig` object.

**ConciseFilter**
UI tree filter in `src/droidrun/tools/filters/`. Reduces the accessibility tree to only actionable or visible elements, minimizing LLM token usage.

**credential_manager**
Module (`src/droidrun/credential_manager/`). Stores and retrieves app credentials (usernames, passwords) for automated login flows. `FileCredentialManager` persists credentials to disk.

---

## D

**DetailedFilter**
UI tree filter in `src/droidrun/tools/filters/`. Retains more element attributes than `ConciseFilter` for richer agent context.

**DeviceDriver**
Abstract base class in `src/droidrun/tools/driver/base.py`. Defines the interface all device drivers must implement (tap, swipe, type, screenshot, get_ui, etc.).

**DROIDRUN_DEEPSEEK_KEY**
Windows environment variable (stored in `HKCU\Environment`) holding the DeepSeek API key. Set by `startup_droidrun.ps1` / `store_api_keys_to_env.ps1`.

**DROIDRUN_OPENROUTER_KEY**
Windows environment variable holding the OpenRouter API key for this workspace.

**DroidAgent**
Top-level LlamaIndex Workflow class in `src/droidrun/agent/droid/droid_agent.py`. Coordinates the overall task: selects agent mode, sets up device driver, manages task loop, emits `ResultEvent`.

**DroidrunConfig**
Dataclass hierarchy in `src/droidrun/config_manager/config_manager.py`. Root config object. Contains nested configs for device, agent, tracing, MCP, credentials, and LLM profiles.

---

## E

**ExecutorAgent**
Agent in `src/droidrun/agent/executor/`. Receives a single planned action from `ManagerAgent` and executes it against the device. Used in reasoning mode.

---

## F

**FastAgent**
Agent in `src/droidrun/agent/codeact/`. Lightweight agent using XML-formatted tool calls. Default for `reasoning=false`.

**FileCredentialManager**
Concrete implementation of `CredentialManager` that persists credentials to a YAML file on disk.

---

## G

**GOOGLE_API_KEY / GEMINI_API_KEY**
Standard environment variables for Google GenAI API access. Managed by DroidRun's `env_keys.py`.

---

## I

**IndexedFormatter**
Formatter in `src/droidrun/tools/formatters/`. Assigns numeric indices to UI elements in the accessibility tree, enabling the agent to reference elements by index.

---

## J

**JSON-RPC**
Protocol used for MCP communication. Requests and responses are JSON objects with `method`, `params`, `id` fields, sent over stdio.

---

## L

**Langfuse**
Open-source LLM observability platform. Alternative to Arize Phoenix. Configured via `tracing.provider = langfuse`.

**LlamaIndex Workflow**
Framework from LlamaIndex (`llama-index-workflows==2.8.3`) for building event-driven, stateful AI pipelines. Key concepts: `StartEvent`, `StopEvent`, `WorkflowHandler`, `@step` decorators.

**LLM Profile**
Named LLM configuration block in `config.yaml`. Profiles: `manager`, `executor`, `fast_agent`, `text_manipulator`, `app_opener`, `scripter`, `structured_output`. Each specifies provider, model, temperature.

**llm_loader**
Module `src/droidrun/agent/utils/llm_loader.py`. Instantiates a LlamaIndex LLM object from a provider name and model string.

**llm_picker**
Module `src/droidrun/agent/utils/llm_picker.py`. Selects the appropriate LLM profile from config based on the agent role.

---

## M

**Macro**
Module (`src/droidrun/macro/`). Records and replays device interaction sequences deterministically. Useful for repetitive tasks.

**ManagerAgent**
Agent in `src/droidrun/agent/manager/`. Receives the overall goal and current UI state, plans the next atomic action, and delegates to `ExecutorAgent`. Used in reasoning mode.

**MCP (Model Context Protocol)**
Open protocol for AI clients to call tools hosted in external servers. DroidRun acts as both MCP server and MCP client.

**MCPClientManager**
Class in `src/droidrun/mcp/client.py`. Manages connections to external MCP servers, enumerates their tools.

**MCPConfig / MCPServerConfig**
Config models in `src/droidrun/mcp/config.py`. Define which MCP servers to connect to.

**MobileRun / mobilerun-sdk**
Cloud Android device service. `tools/driver/cloud.py` provides a driver backed by MobileRun's cloud infrastructure. Purpose Unknown / Needs Verification beyond this.

---

## O

**OpenRouter**
LLM routing API providing access to many models through an OpenAI-compatible endpoint. Used in vision mode in this workspace.

**OPENAI_API_KEY / ANTHROPIC_API_KEY**
Standard environment variables for respective LLM API access.

---

## P

**parallel_tools**
Config flag (`agent.fast_agent.parallel_tools`, default `true`). Allows the agent to issue multiple tool calls in a single LLM response when actions are independent.

**phone_apps**
MCP tool in `mcp_server.py`. Lists installed apps on the connected Android device.

**phone_do**
MCP tool in `mcp_server.py`. Executes an AI-directed task on the phone.

**phone_ping**
MCP tool in `mcp_server.py`. Checks Portal APK reachability.

**Portal / DroidRun Portal APK**
Android application (`com.droidrun.portal`) installed on the target device. Registers an accessibility service and exposes HTTP API (port 8080) for action commands and UI state.

**PortalClient**
HTTP client class in `src/droidrun/tools/android/portal_client.py`. Sends action commands to Portal APK. Supports ADB content provider and TCP transport.

**PostHog**
Product analytics platform. DroidRun sends anonymous usage telemetry. Can be disabled via `telemetry.enabled: false`.

---

## R

**reasoning mode**
Agent execution mode where `reasoning=true`. Uses ManagerAgent + ExecutorAgent pipeline. Slower but more deliberate.

**RecordingDriver**
Device driver in `src/droidrun/tools/driver/recording.py`. Wraps another driver and records all interactions.

**ResultEvent**
LlamaIndex event emitted by `DroidAgent` when task completes. Contains `success` bool and `summary` string.

---

## S

**safe_execution**
Config flag. When `true`, CodeActAgent and ScripterAgent run generated code in a sandboxed environment with restricted imports and builtins (controlled by `safe_execution` config section).

**ScripterAgent**
Agent in `src/droidrun/agent/scripter/`. Generates and runs off-device Python scripts for complex logic tasks.

**StartEvent / StopEvent**
LlamaIndex Workflow event types marking beginning and end of a workflow run.

**StatelessManagerAgent**
Variant of `ManagerAgent` that does not maintain conversational state between planning steps. Unknown / Needs Verification — exact behavioral difference.

**StealthDriver**
Device driver in `src/droidrun/tools/driver/stealth.py`. Variant that minimizes detectable automation signatures. Unknown / Needs Verification.

**StructuredOutputAgent**
Agent in `src/droidrun/agent/oneflows/`. Extracts structured JSON data from device screen content.

---

## T

**Tailscale**
Mesh VPN service. Device accessible at `100.71.228.18` via Tailscale, allowing ADB connections from any enrolled host.

**Tailscale IP**
`100.71.228.18` — the stable private IP assigned to the test device on the Tailscale network.

**telemetry**
Module (`src/droidrun/telemetry/`). Handles PostHog event tracking and LLM trace export to Phoenix or Langfuse.

**TextManipulator**
Agent/utility in `src/droidrun/agent/oneflows/text_manipulator.py`. Handles text editing tasks on-device as a dedicated sub-workflow.

**ToolRegistry**
Unknown / Needs Verification — likely refers to the collection of `DeviceDriver` methods exposed as callable tools to the agent. Referenced in `src/droidrun/agent/tool_registry.py`.

**tool-calling mode**
Execution mode where the agent uses XML-formatted tool calls (FastAgent) or LLM function calling API to invoke device actions.

**TrajectoryWriter**
Class in `src/droidrun/agent/trajectory/`. Records the full sequence of agent steps to disk for debugging and replay.

**TUI**
Terminal User Interface. DroidRun includes a `textual`-based TUI (`src/droidrun/cli/tui/`) for interactive task execution.

**Textual**
Python TUI framework used to build DroidRun's terminal UI.

---

## U

**UIProvider**
Class in `src/droidrun/tools/ui/provider.py`. Fetches current UI state from the device, applies filters, returns a `UIState` object.

**UIState**
Data structure containing the parsed accessibility tree for the current screen.

---

## V

**vision mode**
Agent execution mode where `vision=true`. Agent receives screenshot images, enabling reasoning about visual layout. Requires a multimodal LLM.

---

## W

**WorkflowHandler**
LlamaIndex object returned by `droid_agent.run()`. Provides async event stream and final result future.
