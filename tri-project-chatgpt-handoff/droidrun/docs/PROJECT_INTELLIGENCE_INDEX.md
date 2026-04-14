# Project Intelligence Index — DroidRun

> Master index for the DroidRun repository. Start here. This workspace instance is a hybrid: the upstream open-source DroidRun Python framework (`src/`) combined with a Windows-specific operational layer (scripts, mcp_server.py) for the owner's Samsung Galaxy S25 Ultra automation stack.

---

## Project Purpose

DroidRun is a Python framework (v0.5.1, Beta, MIT) that enables **LLM agents to control Android (and experimentally iOS) devices** via natural language commands. The agent perceives device state through ADB + an on-device Portal APK, decides actions using an LLM, and executes touch/swipe/text/app-launch operations.

In this workspace, DroidRun is also integrated as an **MCP server** exposing phone control tools to Cursor, OpenClaw, and Claude Desktop.

---

## Repo Role Within Larger Workspace

```
AI-Project-Manager workspace  ←→  open--claw workspace  ←→  droidrun workspace (this repo)
        ↕                                   ↕                          ↕
  project orchestration             OpenClaw AI client        Android device control
                                                               + MCP server for both
```

- `AI-Project-Manager`: Orchestrates projects; launches all three workspaces
- `open--claw`: AI client that uses DroidRun via MCP to control the phone
- `droidrun`: Provides both the framework SDK and the MCP server endpoint

---

## Top-Level Architecture Summary

```
User / MCP Client (Cursor, OpenClaw, Claude Desktop)
        │
        ▼
  mcp_server.py  (JSON-RPC stdio MCP server)
        │
        ▼
  droidrun CLI  (droidrun run / ping / setup)
        │
        ▼
  DroidAgent  (LlamaIndex Workflow)
    ├── FastAgent / CodeActAgent   (reasoning=false, default)
    └── ManagerAgent + ExecutorAgent  (reasoning=true)
        │
        ▼
  AndroidDriver  (ADB + PortalClient HTTP)
        │
        ▼
  DroidRun Portal APK  (on-device, port 8080)
        │
        ▼
  Android OS (Samsung Galaxy S25 Ultra)
```

---

## Major Modules

| Module | Path | Role |
|--------|------|------|
| CLI | `src/droidrun/cli/` | Entry point, Click commands |
| DroidAgent | `src/droidrun/agent/droid/` | Top-level workflow coordinator |
| FastAgent | `src/droidrun/agent/codeact/` | Direct execution agent (XML tools or code) |
| ManagerAgent | `src/droidrun/agent/manager/` | Planning agent (reasoning mode) |
| ExecutorAgent | `src/droidrun/agent/executor/` | Action execution (reasoning mode) |
| AndroidDriver | `src/droidrun/tools/driver/android.py` | ADB + Portal device I/O |
| PortalClient | `src/droidrun/tools/android/portal_client.py` | HTTP to on-device Portal APK |
| ConfigManager | `src/droidrun/config_manager/` | YAML + env config loading |
| MCP Client | `src/droidrun/mcp/` | Consume external MCP servers as agent tools |
| MCP Server | `mcp_server.py` (workspace root) | Expose DroidRun as MCP to AI clients |
| Scripts | `scripts/*.ps1` | Windows PowerShell automation |
| Telemetry | `src/droidrun/telemetry/` | PostHog + Arize Phoenix + Langfuse |
| Portal mgmt | `src/droidrun/portal.py` | APK download/install/setup |
| Macro | `src/droidrun/macro/` | Record/replay device action macros |
| TUI | `src/droidrun/cli/tui/` | Textual-based terminal UI |

---

## Major Entry Points

| Entry Point | How to Call | Purpose |
|-------------|-------------|---------|
| `droidrun run "task"` | CLI | Run AI agent task on device |
| `droidrun setup` | CLI | Install Portal APK on device |
| `droidrun ping` | CLI | Verify Portal connectivity |
| `droidrun doctor` | CLI | Diagnose system health |
| `droidrun tui` | CLI | Launch interactive TUI |
| `droidrun macro` | CLI | Record/replay macros |
| `mcp_server.py` | Python / PS1 launcher | MCP server for AI clients |
| `scripts/startup_droidrun.ps1` | PowerShell | Unified startup (keys + ADB connect) |
| `scripts/droidrun_run.ps1` | PowerShell | Run task with auto-provider selection |

---

## Runtime Model

- **Python asyncio** via LlamaIndex Workflows
- **ADB** (TCP or USB) for device communication
- **Portal APK** runs on device, serves HTTP on port 8080 (ADB-forwarded to `localhost:8080`)
- **MCP server** runs as stdio subprocess (JSON-RPC over stdin/stdout)
- Tailscale provides secure cross-network ADB access (`100.71.228.18:5555`)
- No persistent daemon — each `droidrun run` spawns one workflow execution

---

## Configuration Model

- Primary: `~/.config/droidrun/config.yaml` (platformdirs user config)
- Example/template: `src/droidrun/config_example.yaml`
- API keys: `~/.config/droidrun/.env` OR Windows User Environment Variables (`HKCU\Environment`)
- Override hierarchy: CLI flags > YAML config > env vars > defaults
- Config object: `DroidrunConfig` dataclass (`src/droidrun/config_manager/config_manager.py`)
- MCP servers connectable via `mcp:` section in config YAML

---

## Dependency Model

- **LlamaIndex** (core AI orchestration, LLM abstraction)
- **async_adbutils** (ADB device communication)
- **httpx** (Portal HTTP client)
- **mcp** (MCP protocol — both server and client)
- **textual** (TUI framework)
- **rich** (CLI output)
- **pydantic** (data validation)
- **posthog** (anonymous telemetry)
- LLM providers: `llama-index-llms-openai`, `-openai-like`, `-google-genai`, `-ollama`, `-openrouter`, `anthropic`, `llama-index-llms-deepseek`

---

## How This Repo Interacts With Other Repos/Services

| System | Interaction | Direction |
|--------|-------------|-----------|
| Samsung S25 Ultra (device) | ADB TCP → DroidRun Portal HTTP:8080 | bidirectional |
| Tailscale network | Routes ADB TCP over private VPN | infrastructure |
| OpenAI / OpenRouter / DeepSeek / Google / Anthropic | LLM inference API calls | outbound |
| Bitwarden Secrets Manager | API key injection at startup | outbound (PowerShell) |
| Cursor / OpenClaw / Claude Desktop | MCP JSON-RPC stdio | inbound |
| GitHub (droidrun/droidrun-portal) | Portal APK download | outbound |
| Arize Phoenix / Langfuse | Tracing/observability | outbound (optional) |
| PostHog | Anonymous telemetry | outbound |

---

## Risks / Unknowns

- Portal accessibility service may not survive phone reboot without manual re-enable
- Wireless debug port changes on phone reboot (mitigated by `adb tcpip 5555` + `adb_find_port.ps1`)
- `mobilerun-sdk` dependency — purpose unclear, may be cloud/MobileRun integration
- iOS support is experimental (stub in `tools/driver/ios.py`, `tools/ios/`)
- No CI/CD pipeline found in this workspace instance
- `src/` is a clone of the upstream repo — local changes may conflict with upstream updates
- MCP server (`mcp_server.py`) is custom to this workspace, not part of upstream DroidRun

---

## Document Index

| Document | Path | Purpose |
|----------|------|---------|
| This file | `docs/PROJECT_INTELLIGENCE_INDEX.md` | Master entry point |
| Checklist | `docs/DOCS_CHECKLIST.md` | Documentation completion tracker |
| Project Overview | `docs/project-overview.md` | What DroidRun is |
| Repo Boundaries | `docs/repo-boundaries.md` | Ownership/delegation |
| Glossary | `docs/glossary.md` | Term definitions |
| System Architecture | `docs/system-architecture.md` | Component + flow diagrams |
| Module Map | `docs/module-map.md` | Folder → responsibility mapping |
| Runtime Lifecycle | `docs/runtime-lifecycle.md` | Startup/shutdown/retry |
| State Management | `docs/state-management.md` | Where state lives |
| Data Flow | `docs/data-flow.md` | Input → output traces |
| External Integrations | `docs/external-integrations.md` | APIs, SDKs, services |
| Offline/Sync Model | `docs/offline-sync-model.md` | Offline behavior |
| Error Handling | `docs/error-handling-model.md` | Exceptions, retries, degradation |
| Source Tree Guide | `docs/source-tree-guide.md` | Repo structure explained |
| Key Classes | `docs/key-classes-and-services.md` | Most important code units |
| Entry Points | `docs/entry-points-and-boot-sequence.md` | Boot sequence |
| Background Jobs | `docs/background-jobs-workers-schedulers.md` | Workers/schedulers |
| Navigation | `docs/navigation-screen-flow.md` | CLI/TUI navigation |
| API Layer | `docs/api-layer-client-contracts.md` | API clients |
| Storage Layer | `docs/storage-layer.md` | Persistence |
| Feature Inventory | `docs/feature-inventory.md` | All features |
| Env/Config Ref | `docs/environment-config-reference.md` | Config keys |
| Build/Release | `docs/build-release-process.md` | Build process |
| CI/CD | `docs/ci-cd.md` | Pipelines |
| Dependencies | `docs/dependency-inventory.md` | Package inventory |
| Secrets Handling | `docs/secrets-handling.md` | Secret management |
| Logging | `docs/logging-observability.md` | Observability |
| Troubleshooting | `docs/troubleshooting-playbook.md` | Debug playbook |
| Security Overview | `docs/security-overview.md` | Auth/access model |
| Permissions | `docs/permission-manifest.md` | System permissions |
| Data Privacy | `docs/data-privacy-storage.md` | User data |
| Threat Model | `docs/threat-model.md` | Threat analysis |
| Safe Failure | `docs/safe-failure-disable-paths.md` | Kill switches |
| AI Handoff | `docs/ai-handoff-summary.md` | AI-to-AI handoff doc |
| ADR Summary | `docs/adr-summary.md` | Architecture decisions |
| Unknowns | `docs/unknowns-gaps-assumptions.md` | Gaps and risks |
| Next Docs | `docs/recommended-next-docs.md` | Future documentation |
| Project Context | `docs/project-context.json` | Machine-readable summary |
| Final Summary | `docs/FINAL_SUMMARY.md` | Documentation run report |
| Architecture Overview | `docs/architecture_overview.md` | Workspace-specific architecture (existing) |
| AI State | `docs/ai/STATE.md` | Current session state |
