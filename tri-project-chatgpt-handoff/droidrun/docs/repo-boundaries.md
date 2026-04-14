# Repo Boundaries — DroidRun

**Related:** [PROJECT_INTELLIGENCE_INDEX.md](PROJECT_INTELLIGENCE_INDEX.md) | [project-overview.md](project-overview.md)

---

## Responsibilities Owned by DroidRun

- **Agent orchestration** — Coordinating multi-step AI task execution against an Android device via LlamaIndex Workflows (DroidAgent, ManagerAgent, ExecutorAgent, FastAgent, CodeActAgent).
- **Device interaction** — Sending clicks, swipes, text input, app launches, and screenshots through the Portal APK or ADB content provider (AndroidDriver, PortalClient).
- **UI state parsing** — Fetching, filtering, and formatting the accessibility tree from the device (UIProvider, ConciseFilter, DetailedFilter, IndexedFormatter).
- **Portal APK management** — Downloading, installing, and verifying the Portal APK on the connected device (`portal.py`, `auto_setup` config flag).
- **Configuration management** — Loading, validating, and migrating YAML config; reading/writing `.env` files for API key storage (config_manager, env_keys).
- **LLM abstraction** — Loading and selecting LLM providers (OpenAI, OpenRouter, DeepSeek, Google GenAI, Ollama, Anthropic) via LlamaIndex LLM adapters (llm_loader, llm_picker).
- **MCP server** — Exposing `phone_do`, `phone_ping`, and `phone_apps` tools over stdio JSON-RPC for AI clients (mcp_server.py).
- **MCP client** — Consuming external MCP tool servers and adapting their tools for use inside DroidRun agents (mcp/adapter, mcp/client).
- **Credential management** — Storing and retrieving app credentials for device automation (credential_manager).
- **Telemetry and tracing** — Sending usage events to PostHog and traces to Arize Phoenix or Langfuse (telemetry/).
- **Macro record/replay** — Recording and replaying device interaction sequences (macro/).
- **TUI** — Terminal-based interactive UI for running tasks (cli/tui/, Textual).
- **Workspace-specific scripts** — PowerShell automation for ADB lifecycle, API key injection from Bitwarden, and MCP server launch (scripts/).
- **External agent adapters** — Thin wrappers for AutoGLM and MAI-UI as alternative agent backends (agent/external/).

---

## Responsibilities Delegated Elsewhere

| Responsibility | System That Owns It |
|---|---|
| Physical Android OS and hardware | Samsung Galaxy S25 Ultra / Android 16 |
| Accessibility event capture and HTTP API on-device | DroidRun Portal APK (`com.droidrun.portal`) |
| ADB protocol and USB/Wi-Fi transport | Android Debug Bridge (ADB) — platform tool |
| Wireless network routing across subnets | Tailscale (mesh VPN, device at `100.71.228.18`) |
| Secret storage and machine credentials | Bitwarden Secrets Manager (bws CLI) |
| LLM inference | DeepSeek API, OpenRouter, Google GenAI, OpenAI, Anthropic |
| Cloud device provisioning (optional) | MobileRun / mobilerun-sdk |
| AI client UI and chat interface | Cursor, OpenClaw, Claude Desktop |
| MCP protocol framing | `mcp` Python library (>=1.26.0) |
| iOS device interaction | Experimental iOS driver (not production-ready — Unknown / Needs Verification) |

---

## Integration Boundaries

### DroidRun ↔ Portal APK
- **Transport:** ADB content provider (default) or HTTP to `localhost:8080` (TCP mode, requires `adb forward tcp:8080 tcp:8080`).
- **What crosses:** Encoded action commands (click, swipe, type, key, screenshot, get-ui) and responses (accessibility tree XML/JSON, screenshot bytes).
- **Contract:** PortalClient auto-detects available transport and falls back gracefully.

### DroidRun ↔ ADB
- **Transport:** Shell subprocess (`adb -s <serial> ...`) via `async_adbutils`.
- **What crosses:** ADB commands (connect, install, shell, forward, content query/insert), device serial or IP:port.
- **Contract:** DroidRun assumes ADB is installed and on PATH. Serial is configured via `device.serial` or auto-detected.

### DroidRun ↔ Tailscale
- **Transport:** TCP/IP at `100.71.228.18:5555` (ADB over Tailscale).
- **What crosses:** ADB packets wrapped in Tailscale WireGuard tunnel.
- **Contract:** DroidRun treats Tailscale as transparent network; it only knows device IP. Tailscale must be running on both host and device.

### DroidRun ↔ Bitwarden Secrets Manager
- **Transport:** `bws` CLI subprocess invoked by PowerShell scripts.
- **What crosses:** API key values (DROIDRUN_DEEPSEEK_KEY, DROIDRUN_OPENROUTER_KEY) injected into Windows environment variables or `~/.config/droidrun/.env`.
- **Contract:** Bitwarden machine account token (`BWS_DROIDRUN_TOKEN`) must be present in the regular Bitwarden vault. DroidRun code never calls bws directly; only startup scripts do.

### DroidRun ↔ LLM APIs
- **Transport:** HTTPS via LlamaIndex LLM adapters (httpx under the hood).
- **What crosses:** Prompt messages (system + user + tool results), model responses, tool call JSON.
- **Contract:** DroidRun passes API keys via environment variables; LlamaIndex adapters handle authentication and retries.

### DroidRun ↔ AI Clients (MCP)
- **Transport:** stdio JSON-RPC (MCP protocol, `mcp` library).
- **What crosses:** Tool schemas, tool call requests (`phone_do`, `phone_ping`, `phone_apps`), tool results (text).
- **Contract:** AI client spawns `mcp_server.py` as a child process via `start_mcp_server.ps1`; DroidRun responds synchronously per tool call.

### DroidRun ↔ MobileRun (cloud)
- **Transport:** mobilerun-sdk (Unknown / Needs Verification — SDK details not confirmed).
- **What crosses:** Device commands routed to cloud-hosted Android instances.
- **Contract:** MobileRunTools driver is a drop-in replacement for AndroidDriver when using cloud devices.

---

## Assumptions About Upstream/Downstream Systems

- **ADB** is installed, on PATH, and able to reach the device (USB, Wi-Fi, or Tailscale). DroidRun does not manage ADB installation.
- **Portal APK** is compatible with the connected Android version. `auto_setup=true` will reinstall if the installed version is outdated.
- **Tailscale** is running on both host and device, the device is enrolled, and the Tailscale IP (`100.71.228.18`) is stable across sessions.
- **Bitwarden Secrets Manager** machine account has read access to the two secret IDs hardcoded in `startup_droidrun.ps1`. Token rotation must be done manually in the regular vault.
- **LLM API keys** are valid, have sufficient quota, and the selected model supports the required context window for multi-step device tasks.
- **AI clients** (Cursor, OpenClaw, Claude Desktop) correctly parse the MCP tool schemas returned by `mcp_server.py` and pass arguments as typed by the schema.
- **Android device** has accessibility services enabled and the Portal accessibility service is active.
- **Port 8080** on the device is not in use by another app when TCP mode is enabled.

---

## Anti-Patterns / What Should NOT Be Added Here

- **Hardcoded secrets** — API keys, passwords, or tokens must never appear in source files, config YAMLs, or committed `.env` files.
- **Device-specific UI logic** — Business logic that assumes a specific app's UI layout should live in task prompts or macros, not in agent code.
- **LLM provider lock-in** — New features should not assume a specific LLM; always route through `llm_loader`/`llm_picker`.
- **Monolithic agent classes** — Agent files exceeding ~20 lines of inline procedural logic should be refactored into domain/util modules.
- **Direct ADB subprocess calls outside drivers** — All ADB interaction must go through `AndroidDriver` or `async_adbutils`; never call `subprocess.run(["adb", ...])` from agent code.
- **On-device data persistence** — DroidRun is stateless per run; do not add session state that must survive across runs.
- **Workspace-specific config baked into source** — Device IP, secret IDs, and Tailscale addresses belong in scripts or env vars, not in `src/droidrun/`.
- **MCP server becoming a long-running daemon** — It is a stdio process, terminated per-session; do not add background threads or file watchers to it.
- **iOS production support** — The iOS driver is experimental; do not ship iOS-dependent features until the driver is verified stable.
