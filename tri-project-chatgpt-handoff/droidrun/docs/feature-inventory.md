# Feature Inventory

All implemented, partial, experimental, and unknown-status features in DroidRun v0.5.1. Each entry includes status, purpose, key source files, dependencies, and known gaps.

**Status legend:**
- ✅ **Complete** — production-ready, confirmed working
- 🔶 **Partial** — code exists, requires additional setup (e.g., external server)
- 🧪 **Experimental** — stub or proof-of-concept, not production-ready
- ❓ **Unknown** — dependency or adapter code exists; runtime behavior unverified

---

## 1. Natural Language Device Control

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Execute plain-English tasks on an Android device via AI agent |
| **CLI** | `droidrun run "open Maps and search for coffee"` |
| **Key Files** | `src/droidrun/agent/`, `src/droidrun/tools/android/portal_client.py`, `src/droidrun/cli/run.py` |
| **Dependencies** | ADB, Portal APK, any configured LLM provider |
| **Gaps** | None for core flow; multi-step tasks depend on `max_steps` setting |

---

## 2. Portal APK Install & Management

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Download, install, and manage the `com.droidrun.portal` APK that provides the accessibility bridge on the Android device |
| **CLI** | `droidrun setup` |
| **Key Files** | `src/droidrun/cli/setup.py`, `src/droidrun/tools/android/adb.py` |
| **Dependencies** | ADB, internet access (GitHub releases or ungh.cc mirror) |
| **Gaps** | None |

---

## 3. Portal Health Check

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Verify that the Portal APK is installed, running, and reachable |
| **CLI** | `droidrun ping` |
| **Key Files** | `src/droidrun/cli/ping.py`, `src/droidrun/tools/android/portal_client.py` |
| **Dependencies** | ADB or TCP connection to device |
| **Gaps** | None |

---

## 4. System Diagnostics

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Full health check: ADB connectivity, portal status, LLM API reachability, config validity |
| **CLI** | `droidrun doctor` |
| **Key Files** | `src/droidrun/cli/doctor.py` |
| **Dependencies** | ADB, configured LLM provider(s) |
| **Gaps** | None |

---

## 5. Terminal UI (TUI)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Interactive configuration interface without editing YAML manually |
| **CLI** | `droidrun tui` |
| **Key Files** | `src/droidrun/tui/settings_screen.py`, `src/droidrun/tui/models_tab.py`, `src/droidrun/tui/advanced_tab.py`, `src/droidrun/tui/agent_tab.py` |
| **Dependencies** | `textual` library |
| **Gaps** | Tab contents inferred from filenames; verify against running TUI |

---

## 6. Macro Recording & Replay

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Record a sequence of device actions and replay them deterministically (no LLM needed) |
| **CLI** | `droidrun macro record`, `droidrun macro replay` |
| **Key Files** | `src/droidrun/cli/macro.py` |
| **Dependencies** | ADB, Portal APK |
| **Gaps** | None |

---

## 7. Multi-Provider LLM Support

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Use any supported LLM provider without changing agent code |
| **Providers** | OpenAI, GoogleGenAI (Gemini), Anthropic, DeepSeek, Ollama, OpenRouter, OpenAILike |
| **Key Files** | `src/droidrun/agent/llm_loader.py`, `src/droidrun/config/config.py` |
| **Dependencies** | Provider-specific LlamaIndex adapter packages (see `pyproject.toml` extras) |
| **Gaps** | None for listed providers |

---

## 8. Vision Mode

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Send device screenshots to the LLM instead of (or in addition to) the accessibility tree — required for apps with non-standard accessibility |
| **Config** | `agent.fast_agent.vision: true` or `--vision` CLI flag |
| **Key Files** | `src/droidrun/tools/android/portal_client.py` (screenshot action), agent loop |
| **Dependencies** | Multimodal LLM (Gemini, GPT-4o, Claude 3+) |
| **Gaps** | Higher token usage; slower than text-only mode |

---

## 9. Reasoning Mode (Manager + Executor Pipeline)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Two-LLM pipeline: Manager LLM decomposes the task into sub-goals; Executor LLM performs each sub-goal on the device |
| **Config** | `agent.reasoning: true` |
| **Key Files** | `src/droidrun/agent/manager.py`, `src/droidrun/agent/executor.py` |
| **Dependencies** | Two LLM profiles (`manager` and `executor` in `llm_profiles`) |
| **Gaps** | Higher cost (two LLM calls per step); may be overkill for simple tasks |

---

## 10. FastAgent XML Tool-Calling Mode

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete (default mode) |
| **Purpose** | Single-LLM agent using LlamaIndex XML tool-calling format for device actions |
| **Config** | Default when `reasoning: false` and `codeact: false` |
| **Key Files** | `src/droidrun/agent/fast_agent.py` |
| **Dependencies** | Any configured LLM (tool-calling support recommended) |
| **Gaps** | None |

---

## 11. CodeAct Mode

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | LLM generates Python code to accomplish device tasks; sandbox executes the code |
| **Config** | `agent.fast_agent.codeact: true` |
| **Key Files** | `src/droidrun/agent/fast_agent.py`, `src/droidrun/agent/codeact/` |
| **Dependencies** | LLM with strong code generation; sandbox config (`safe_execution.*`) |
| **Gaps** | Sandbox restrictions may block some advanced operations |

---

## 12. MCP Client (Consume External Tools)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | DroidRun agent can call tools provided by external MCP servers (file system, web search, etc.) during a task |
| **Config** | `mcp.enabled: true`, `mcp.servers.*` |
| **Key Files** | `src/droidrun/mcp/client.py` (`MCPClientManager`) |
| **Dependencies** | `mcp>=1.26.0`, external MCP server processes |
| **Gaps** | Tool schema validation is pass-through; errors in external tools propagate to agent |

---

## 13. MCP Server (Expose Phone Control)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete (workspace-specific deployment) |
| **Purpose** | Expose DroidRun capabilities as MCP tools (`phone_do`, `phone_ping`, `phone_apps`) so AI clients like Claude Desktop or Cursor can drive the phone |
| **Key Files** | `src/droidrun/mcp_server.py` |
| **Dependencies** | `mcp>=1.26.0`, running DroidRun + Portal |
| **Gaps** | Requires explicit registration in the AI client's MCP config |

---

## 14. Credential Manager

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Supply app credentials (usernames/passwords) to the agent for automated login flows |
| **Config** | `credentials.enabled: true`, `credentials.file_path` |
| **Key Files** | `src/droidrun/credentials/file_credential_manager.py`, `config/credentials_example.yaml` |
| **Dependencies** | `config/credentials.yaml` file (not bundled; user creates from example) |
| **Gaps** | Password values must be env var references — never hardcoded in YAML |

---

## 15. App Cards (Per-App Instructions)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete (local mode); ❓ Unknown (server mode) |
| **Purpose** | Provide app-specific context (UI quirks, login flows, navigation hints) to the agent before it starts a task |
| **Config** | `agent.app_cards.enabled: true`, `agent.app_cards.mode: local\|server` |
| **Key Files** | `src/droidrun/config/app_cards/` (bundled cards), `src/droidrun/agent/app_cards/` (provider code) |
| **Dependencies** | None for local mode; `agent.app_cards.server_url` for server mode |
| **Gaps** | Server mode URL and protocol unverified; card coverage limited to bundled apps |

---

## 16. Telemetry (PostHog)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Anonymous usage analytics to guide product development |
| **Config** | `telemetry.enabled: true` (default) |
| **Key Files** | `src/droidrun/telemetry/` |
| **Dependencies** | `posthog` Python library, internet access |
| **Opt-out** | Set `telemetry.enabled: false` in config |
| **Gaps** | None |

---

## 17. Tracing (Phoenix / Langfuse)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Export LLM trace data (prompts, responses, tool calls, latencies) to Arize Phoenix or Langfuse for debugging and evaluation |
| **Config** | `tracing.enabled: true`, `tracing.provider: phoenix\|langfuse` |
| **Key Files** | `src/droidrun/tracing/` |
| **Dependencies** | `arize-phoenix` or `langfuse` + `openinference-instrumentation-llama-index` |
| **Gaps** | Requires running Phoenix server (local) or Langfuse account (cloud/self-hosted) |

---

## 18. Trajectory Recording

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Save per-step or per-action JSON snapshots of agent runs for debugging, evaluation, and dataset creation |
| **Config** | `logging.save_trajectory: step\|action`, `logging.trajectory_path`, `logging.trajectory_gifs` |
| **Key Files** | `src/droidrun/logging/trajectory_writer.py` |
| **Dependencies** | Disk space; `Pillow` for GIF compilation |
| **Gaps** | No built-in trajectory viewer; files are raw JSON + GIF |

---

## 19. Safe Code Execution (Sandbox)

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Execute LLM-generated Python code (CodeAct mode) in a restricted sandbox — limits imports and builtins to prevent destructive operations |
| **Config** | `safe_execution.*` section |
| **Key Files** | `src/droidrun/agent/sandbox/` |
| **Dependencies** | None (pure Python implementation) |
| **Gaps** | Overly restrictive configs may break legitimate agent code; tune `allowed_modules` as needed |

---

## 20. External Agents (AutoGLM, MAI-UI)

| Field | Detail |
|-------|--------|
| **Status** | 🔶 Partial |
| **Purpose** | Use specialized external agent models (AutoGLM, MAI-UI) instead of the built-in agent |
| **Key Files** | `src/droidrun/agent/external/` or similar adapter code |
| **Dependencies** | Running vLLM server hosting the external model |
| **Gaps** | Requires self-hosted vLLM inference; not usable with standard API keys |

---

## 21. iOS Support

| Field | Detail |
|-------|--------|
| **Status** | 🧪 Experimental stub |
| **Purpose** | Extend DroidRun-style automation to iOS devices |
| **Key Files** | `src/droidrun/tools/driver/ios.py` |
| **Dependencies** | iOS device, macOS host, relevant iOS automation framework |
| **Gaps** | Implementation is a stub; not functional in v0.5.1 |

---

## 22. Cloud Device Support (MobileRun)

| Field | Detail |
|-------|--------|
| **Status** | ❓ Unknown |
| **Purpose** | Run DroidRun against cloud-hosted Android devices via the MobileRun service |
| **Key Files** | `mobilerun-sdk` dependency in `pyproject.toml` |
| **Dependencies** | `mobilerun-sdk`, MobileRun account/service |
| **Gaps** | Integration code unverified; API and auth details unknown |

---

## 23. Stealth Mode

| Field | Detail |
|-------|--------|
| **Status** | ❓ Unknown |
| **Purpose** | Operate the device in a way that reduces detectable automation signatures (e.g., for apps that block accessibility services) |
| **Key Files** | `src/droidrun/tools/driver/stealth.py` |
| **Dependencies** | Unknown |
| **Gaps** | Implementation status and mechanism unverified |

---

## 24. Tailscale Remote Operation

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete (workspace-specific setup) |
| **Purpose** | Control an Android device over Tailscale VPN — device can be physically remote from the host machine |
| **Key Files** | Workspace PowerShell setup scripts; `device.use_tcp: true` + device Tailscale IP in `device.serial` |
| **Dependencies** | Tailscale installed on both host and device (or device router) |
| **Gaps** | Not part of the open-source DroidRun package; requires network-level setup |

---

## 25. Bitwarden Secrets Integration

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete (workspace-specific) |
| **Purpose** | Securely inject API keys from Bitwarden Secrets Manager into the development environment without storing secrets in files |
| **Key Files** | `setup_windows_host.ps1`, `store_api_keys_to_env.ps1`, `startup_droidrun.ps1` |
| **Dependencies** | `bws` CLI (Bitwarden Secrets Manager), `BWS_ACCESS_TOKEN` env var, machine account |
| **Secret IDs** | DeepSeek: `14d69c11-99ba-428f-a656-b40e014e72ae`; OpenRouter: `f9ed80a7-fc35-4add-96d6-b40e0163b041` |
| **Gaps** | Workspace-specific; not part of the open-source package |

---

## 26. Structured Output Extraction

| Field | Detail |
|-------|--------|
| **Status** | ✅ Complete |
| **Purpose** | Run a DroidRun agent that extracts structured data from an app (e.g., scrape a list of items into a JSON schema) rather than performing a task |
| **Key Files** | `src/droidrun/agent/oneflows/structured_output_agent.py` |
| **Dependencies** | Any configured LLM with structured output / function calling support |
| **Gaps** | Schema must be defined by the caller; no interactive schema builder |

---

## Feature Count Summary

| Status | Count |
|--------|-------|
| ✅ Complete | 20 |
| 🔶 Partial | 1 |
| 🧪 Experimental | 1 |
| ❓ Unknown | 4 |
| **Total** | **26** |
