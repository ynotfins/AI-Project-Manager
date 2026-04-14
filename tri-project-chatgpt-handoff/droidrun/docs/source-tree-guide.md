# Source Tree Guide

Annotated directory and file map for the DroidRun workspace. Every top-level directory and key file is explained.

---

## Root Layout

```
D:\github\droidrun\
├── src/                        # Python package source (upstream + local customisations)
├── scripts/                    # PowerShell automation scripts (workspace-specific)
├── docs/                       # Documentation (this folder)
├── .cursor/                    # Cursor IDE rules and configuration
├── .venv/                      # Python virtual environment (not committed)
├── mcp_server.py               # Workspace MCP server — exposes phone control as MCP tools
├── openmemory.md               # OpenMemory project index (living guide for AI agents)
├── AGENTS.md                   # Cursor workflow contracts and rules entry point
├── README.md                   # Cursor project template readme
└── README_REMOTE_SETUP.md      # DroidRun remote device setup guide (Tailscale, ADB wireless)
```

---

## `src/droidrun/` — Python Package

The core DroidRun Python package. This is based on upstream DroidRun v0.5.1 with local modifications. **Changes here may diverge from upstream.** Do not blindly merge upstream updates without checking for conflicts.

```
src/droidrun/
├── __init__.py                 # Package root; re-exports public API
├── __main__.py                 # Enables `python -m droidrun`
├── config_example.yaml         # Reference config with all documented options
├── log_handlers.py             # Custom logging handlers (TUI, file, stream)
├── portal.py                   # Portal APK management: download, install, enable, health-check
│
├── cli/                        # Command-line interface
│   ├── main.py                 # Entry point: `droidrun run`, `droidrun setup`, `droidrun ping`, etc.
│   ├── app.py                  # Textual TUI application (rich terminal UI)
│   └── commands.py             # Click command definitions
│
├── agent/                      # All agent logic
│   ├── action_context.py       # ActionContext: dependency-injection bag for action functions
│   ├── action_result.py        # ActionResult: (success: bool, summary: str) return type
│   ├── tool_registry.py        # Registers action functions as LlamaIndex FunctionTools
│   ├── usage.py                # Token usage tracking and reporting
│   │
│   ├── codeact/                # CodeActAgent — executes Python code directly
│   │   ├── codeact_agent.py    # Main CodeActAgent workflow
│   │   ├── tools_agent.py      # FastAgent variant (XML tool-calling, no code exec)
│   │   ├── xml_parser.py       # Parses LLM XML tool-call responses
│   │   └── events.py           # LlamaIndex Event types for CodeAct
│   │
│   ├── common/                 # Shared agent utilities
│   │   ├── constants.py        # Shared constants (max_steps default, etc.)
│   │   └── events.py           # Common Event types
│   │
│   ├── droid/                  # DroidAgent — top-level orchestrator
│   │   ├── droid_agent.py      # DroidAgent: main workflow, routes to fast/codeact/manager
│   │   ├── state.py            # DroidAgentState: the single shared state model
│   │   └── events.py           # DroidAgent Event types
│   │
│   ├── executor/               # ExecutorAgent — atomic action executor (reasoning=True)
│   │   ├── executor_agent.py   # Executes one atomic action per subgoal
│   │   ├── prompts.py          # System prompts for ExecutorAgent
│   │   └── events.py           # ExecutorAgent Event types
│   │
│   ├── external/               # External/third-party agent adapters
│   │   ├── mai_ui.py           # MAI-UI agent adapter (not used in this workspace)
│   │   └── autoglm.py          # AutoGLM agent adapter (vLLM-backed, not used)
│   │
│   ├── manager/                # ManagerAgent — planner (reasoning=True)
│   │   ├── manager_agent.py    # Creates plans and subgoals from task
│   │   ├── stateless_manager_agent.py  # Stateless variant for single-shot planning
│   │   ├── prompts.py          # System prompts for ManagerAgent
│   │   └── events.py           # ManagerAgent Event types
│   │
│   ├── oneflows/               # Single-shot sub-agents (one-turn workflows)
│   │   ├── app_starter_workflow.py     # AppStarter: opens an app by name
│   │   ├── structured_output_agent.py  # Extracts structured data from final answer
│   │   └── text_manipulator.py         # TextManipulator: edits text fields
│   │
│   ├── scripter/               # ScripterAgent — runs Python scripts off-device
│   │   ├── scripter_agent.py   # Generates + executes Python automation scripts
│   │   └── events.py           # ScripterAgent Event types
│   │
│   ├── trajectory/             # Trajectory recording
│   │   └── writer.py           # Serialises LlamaIndex Events to JSON + GIF
│   │
│   └── utils/                  # Agent utility functions
│       ├── actions.py          # All atomic action functions (click, type, swipe, etc.)
│       ├── chat_utils.py       # LLM message construction helpers (multimodal, history)
│       ├── code_checker.py     # Validates Python code before safe_execution
│       ├── executer.py         # Executes action functions with ActionContext
│       ├── inference.py        # LLM call helpers (streaming, non-streaming)
│       ├── llm_loader.py       # Instantiates LLM from config (provider + model + api_key)
│       ├── llm_picker.py       # Routes provider string to llm_loader
│       ├── prompt_resolver.py  # Resolves prompt templates to strings
│       ├── signatures.py       # LlamaIndex tool signatures for action functions
│       ├── tracing_setup.py    # Configures OpenTelemetry exporter (Phoenix or Langfuse)
│       └── trajectory.py       # Trajectory data container + load/save utilities
│
├── app_cards/                  # App-specific context cards
│   ├── app_card_provider.py    # Resolves app card for current package name
│   ├── app_cards.json          # App card index
│   └── prompts/                # Per-app prompt snippets (e.g., Gmail, YouTube)
│       └── gmail.md            # Gmail-specific agent hints
│
├── cli/                        # (see above — duplicate entry for clarity)
│   └── tui/                    # Textual TUI components
│       ├── app.py              # TUI App root
│       ├── event_handler.py    # Handles agent events → TUI updates
│       ├── logs.py             # Log panel widget
│       ├── settings/           # Settings screen widgets
│       └── widgets/            # Reusable TUI widgets (step counter, action display, etc.)
│
├── config/                     # Config-related files
│   ├── credentials_example.yaml    # Example credentials file format
│   └── prompts/                    # Agent system prompt templates
│       ├── codeact/            # CodeActAgent prompts
│       ├── executor/           # ExecutorAgent prompts
│       ├── manager/            # ManagerAgent prompts
│       └── scripter/           # ScripterAgent prompts
│
├── config_manager/             # Configuration loading and migration
│   ├── config_manager.py       # Main config management entry point
│   ├── loader.py               # ConfigLoader: load + validate + migrate config
│   ├── path_resolver.py        # Resolves platform-specific config paths (platformdirs)
│   ├── prompt_loader.py        # Loads prompt templates from config/prompts/
│   ├── safe_execution.py       # Restricted Python exec environment for CodeActAgent
│   ├── env_keys.py             # Environment variable name constants
│   └── migrations/             # Config schema migrations
│       ├── v002_add_code_exec.py   # Migration: adds code_exec config block
│       └── v003_add_auto_setup.py  # Migration: adds auto_setup config block
│
├── credential_manager/         # Credential manager for type_secret() action
│   ├── credential_manager.py   # Abstract base
│   └── file_credential_manager.py  # File-backed implementation (optional encryption)
│
├── macro/                      # Macro recording and replay
│   └── __init__.py             # Unknown / Needs Verification (macro module init)
│
├── mcp/                        # MCP client (consume external MCP tool servers)
│   ├── client.py               # MCP client: connects to configured MCP servers
│   ├── adapter.py              # Wraps MCP tools as LlamaIndex FunctionTools
│   └── config.py               # MCP server configuration dataclass
│
├── telemetry/                  # Telemetry and tracing
│   ├── tracker.py              # PostHog capture() function
│   ├── events.py               # Telemetry event types (PackageVisitEvent, etc.)
│   ├── langfuse_processor.py   # Langfuse trace exporter
│   └── phoenix.py              # Arize Phoenix tracer setup
│
└── tools/                      # Device interaction layer
    ├── android/                # Android-specific tools
    │   └── portal_client.py    # PortalClient: HTTP + content-provider client for Portal APK
    │
    ├── driver/                 # Device driver abstraction
    │   ├── base.py             # DeviceDriver ABC + DeviceDisconnectedError
    │   ├── android.py          # AndroidDriver: wraps AdbDevice + PortalClient
    │   ├── cloud.py            # CloudDriver: Unknown / Needs Verification
    │   ├── ios.py              # iOSDriver: stub only, not implemented
    │   ├── recording.py        # RecordingDriver: wraps another driver, logs all actions
    │   └── stealth.py          # StealthDriver: minimises detectable automation signals
    │
    ├── filters/                # Accessibility tree filters (reduce noise)
    │   ├── base.py             # TreeFilter ABC
    │   ├── concise_filter.py   # ConciseFilter: removes non-interactive elements
    │   └── detailed_filter.py  # DetailedFilter: keeps more context (slower)
    │
    ├── formatters/             # Accessibility tree formatters (produce LLM-readable text)
    │   ├── base.py             # TreeFormatter ABC
    │   └── indexed_formatter.py  # IndexedFormatter: assigns numeric index per element
    │
    ├── helpers/                # Coordinate and geometry utilities
    │   ├── coordinate.py       # x/y coordinate math helpers
    │   ├── element_search.py   # Element lookup by index, text, class
    │   └── geometry.py         # Bounds parsing and intersection helpers
    │
    ├── ios/                    # iOS tools (stub only)
    │   └── ios_provider.py     # iOSStateProvider: not implemented
    │
    └── ui/                     # UI state management
        ├── provider.py         # StateProvider + AndroidStateProvider (with retry/recovery)
        ├── state.py            # UIState: snapshot of current screen
        └── stealth_state.py    # StealthUIState: extended state for stealth mode
```

---

## `scripts/` — PowerShell Automation

Workspace-specific helper scripts. None of these are part of the DroidRun Python package.

```
scripts/
├── adb_connect_tailscale.ps1   # Connect ADB to device over Tailscale VPN
├── adb_connect_wifi.ps1        # Connect ADB to device over local Wi-Fi
├── adb_find_port.ps1           # Discover current wireless debug port on device
├── adb_pair_wifi.ps1           # Pair a new device for wireless debugging (one-time)
├── adb_status.ps1              # Show ADB device list + port forward status
├── droidrun_ping.ps1           # Ping the Portal on the device
├── droidrun_run.ps1            # Run a DroidRun task (wrapper with env setup)
├── reconnect_remote.ps1        # Re-establish ADB + port forward after disconnect
├── setup_windows_host.ps1      # One-time Windows host setup (ADB install, PATH, etc.)
├── start_mcp_server.ps1        # Start mcp_server.py with correct venv and env vars
├── startup_droidrun.ps1        # Combined startup: ADB connect + port forward + ping
└── store_api_keys_to_env.ps1   # Store API keys as process environment variables (no files)
```

---

## `docs/` — Documentation

```
docs/
├── architecture_overview.md    # High-level system architecture overview
├── DOCS_CHECKLIST.md           # Documentation task tracking
├── PROJECT_INTELLIGENCE_INDEX.md  # Cross-reference index for AI agents
├── project-overview.md         # Project context and goals
├── state-management.md         # [this session] State objects and lifecycle
├── data-flow.md                # [this session] Data flow diagrams
├── external-integrations.md    # [this session] External service integrations
├── offline-sync-model.md       # [this session] Offline behavior and degradation
├── error-handling-model.md     # [this session] Error handling at every layer
├── source-tree-guide.md        # [this session] This file
│
└── ai/                         # AI agent operational docs (Cursor workflow state)
    ├── ARCHIVE.md              # Archived decisions and historical context
    ├── CURSOR_WORKFLOW.md      # Human-readable Cursor tab workflow overview
    ├── PLAN.md                 # Current active plan
    ├── STATE.md                # Current agent state (updated after each execution block)
    ├── DECISIONS.md            # Key architectural decisions log
    ├── MEMORY_CONTRACT.md      # Rules for what agents should/should not store in memory
    ├── PATTERNS.md             # Observed code patterns and conventions
    ├── memory/                 # Long-term memory files for AI agents
    └── tabs/
        └── TAB_BOOTSTRAP_PROMPTS.md  # Bootstrap prompts for each Cursor tab
```

---

## `.cursor/` — Cursor IDE Configuration

```
.cursor/
└── rules/                      # Cursor rules (AI behavior contracts)
    ├── 00-global-core.md       # Non-negotiable global behaviors
    ├── 05-global-mcp-usage.md  # MCP tool usage policy
    ├── 10-project-workflow.md  # Tab contracts and execution protocol
    ├── 20-project-quality.md   # Engineering standards
    └── openmemory.mdc          # OpenMemory integration rules
```

---

## Root Files

| File | Purpose |
|---|---|
| `mcp_server.py` | Workspace MCP server. Exposes `phone_do`, `phone_ping`, `phone_apps` tools via stdio. Used by Cursor Agent, Claude Desktop, OpenClaw. |
| `openmemory.md` | Living index of the project, maintained by AI agents. Shareable summary of architecture, patterns, and namespaces. |
| `AGENTS.md` | Canonical entry point for AI agent rules. Points to `.cursor/rules/` files and `docs/ai/` state files. |
| `README.md` | Cursor project template readme. Describes the five-tab Cursor workflow. |
| `README_REMOTE_SETUP.md` | Step-by-step guide for setting up remote ADB access via Tailscale and wireless debugging. |

---

## Key File Relationships

```
DroidAgent (droid/droid_agent.py)
  └── uses DroidAgentState (droid/state.py)
  └── creates ActionContext (action_context.py)
  └── calls action functions (utils/actions.py)
        └── via ActionContext.driver → AndroidDriver (tools/driver/android.py)
              └── via PortalClient (tools/android/portal_client.py)
  └── calls StateProvider (tools/ui/provider.py)
        └── via TreeFilter (tools/filters/)
        └── via IndexedFormatter (tools/formatters/)
  └── calls LLM (utils/llm_loader.py + utils/llm_picker.py)

CLI (cli/main.py)
  └── creates AndroidDriver
  └── creates DroidAgent
  └── reads config via ConfigLoader (config_manager/loader.py)

mcp_server.py (root)
  └── spawns subprocess: droidrun CLI
  └── calls ADB directly via subprocess
```
