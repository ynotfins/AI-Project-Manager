# External Integrations

This document lists every external system DroidRun communicates with, how it communicates, and what breaks when the integration is unavailable.

---

## Integration Summary Table

| Integration | Category | Required? | Config Key |
|---|---|---|---|
| ADB (async_adbutils) | Device | Yes | `device.serial` / `-d` flag |
| DroidRun Portal APK | Device | Yes | Auto-installed |
| GitHub / ungh.cc | Device setup | First-run only | (hardcoded URL) |
| OpenAI API | LLM | One LLM required | `OPENAI_API_KEY` |
| Google GenAI API | LLM | One LLM required | `GOOGLE_API_KEY` |
| Anthropic API | LLM | One LLM required | `ANTHROPIC_API_KEY` |
| DeepSeek API | LLM | One LLM required | `DEEPSEEK_API_KEY` |
| OpenRouter API | LLM | One LLM required | `OPENAI_API_KEY` (routed) |
| Ollama | LLM | No (local alt) | `api_base` URL |
| MCP protocol (client) | Tooling | No | `mcp` config block |
| MCP protocol (server) | Tooling | No | `mcp_server.py` |
| PostHog | Telemetry | No (opt-out) | `telemetry.enabled` |
| Arize Phoenix | Tracing | No | `tracing.provider: phoenix` |
| Langfuse | Tracing | No | `LANGFUSE_*` env vars |
| Bitwarden Secrets Manager | Workspace secrets | No (workspace-specific) | External to DroidRun |
| Tailscale | Remote device networking | No (workspace-specific) | External to DroidRun |
| mobilerun-sdk | Unknown | Unknown | Unknown / Needs Verification |

---

## ADB (`async_adbutils`)

**Purpose:** Low-level Android device communication. All device interactions (tap, swipe, type, screenshot, shell commands, file transfer, port forwarding) go through ADB.

**Library:** `async_adbutils` (async wrapper around `adbutils`)

**Entry points:**
- `src/droidrun/tools/driver/android.py` — `AndroidDriver` wraps `AdbDevice`
- `src/droidrun/portal.py` — Portal install/enable helpers use `device.shell()`
- `mcp_server.py` — calls `adb` CLI directly via `subprocess.run`

**Config required:**
- Device serial or IP:port via `device.serial` config key, or `-d` CLI flag
- ADB must be installed and on `PATH`
- For remote devices: `adb connect <ip>:<port>` before running

**Transport modes:**
- USB: direct
- Wireless debug: `adb connect <ip>:<port>` (default port 5555)
- Remote via Tailscale: same as wireless, but over private VPN

**Failure modes:**
- Device not found → `DeviceDisconnectedError` raised immediately, no retry
- ADB server not running → `adb start-server` attempted automatically by `adbutils`
- Port forward fails → Portal TCP mode unavailable, falls back to content provider

---

## DroidRun Portal APK (`com.droidrun.portal`)

**Purpose:** On-device accessibility service + HTTP server. The Portal is the bridge between ADB and Android's UI accessibility tree. Without it, DroidRun cannot read the screen or execute UI actions.

**What it does:**
- Runs an accessibility service that captures the UI hierarchy
- Exposes the UI tree via two transports:
  - TCP socket server (port 8080, preferred) — accessed via `adb forward tcp:8080 tcp:8080`
  - ADB content provider — fallback when TCP unavailable

**Entry points:**
- `src/droidrun/tools/android/portal_client.py` — `PortalClient` HTTP/content provider client
- `src/droidrun/portal.py` — install, enable, health-check helpers
- `src/droidrun/tools/driver/android.py` — `AndroidDriver.portal` holds the `PortalClient`

**Config required:** None beyond device connectivity. Portal APK is auto-downloaded and installed on first `droidrun setup` or first run.

**Connection auto-detection:**
```python
# PortalClient.connect() tries TCP first
GET http://localhost:8080/ping   # via adb-forwarded port
# if timeout → falls back to:
adb shell content query --uri content://com.droidrun.portal/ping
```

**Failure modes:**
- Portal not installed → `droidrun setup` downloads and installs it
- Accessibility service disabled → auto-enable attempted via `adb shell settings put secure ...`; if that fails, user is shown manual instructions and Settings screen is opened
- Portal crashes → mid-retry recovery in `AndroidStateProvider._recover_portal()` restarts the service
- Phone rebooted → accessibility service may need re-enable (known issue)

---

## GitHub API / ungh.cc (APK Download)

**Purpose:** Download the latest Portal APK release during setup.

**URL pattern:** `https://ungh.cc/repos/droidrun/droidrun-portal/releases/latest` (ungh.cc is a GitHub API proxy)

**Entry points:** `src/droidrun/portal.py` — `download_portal_apk()`

**Config required:** None (unauthenticated public API).

**Failure modes:**
- No internet → APK download fails; setup aborts with clear error
- GitHub rate-limited → ungh.cc caches responses; unlikely to be rate-limited
- New APK incompatible → Unknown / Needs Verification

---

## OpenAI API

**Purpose:** LLM provider for text and vision tasks.

**Models used:** Any `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, etc.

**Entry points:**
- `src/droidrun/agent/utils/llm_loader.py` — `load_llm()` instantiates `LlamaIndex OpenAI`
- `src/droidrun/agent/utils/llm_picker.py` — routes provider string to loader

**Config required:**
- `OPENAI_API_KEY` environment variable
- Config: `provider: OpenAI`, `model: gpt-4o`

**Failure modes:**
- Missing API key → LLM instantiation raises; run fails immediately
- API rate limit / quota → HTTP 429 from LlamaIndex; propagates as exception; `ResultEvent(success=False)`
- Network timeout → LlamaIndex raises; same handling

---

## Google GenAI API

**Purpose:** LLM provider, particularly for vision tasks (Gemini models).

**Models used:** `gemini-1.5-pro`, `gemini-2.0-flash`, etc.

**Entry points:** Same as OpenAI — `llm_loader.py` / `llm_picker.py`

**Config required:**
- `GOOGLE_API_KEY` environment variable
- Config: `provider: Google`, `model: gemini-2.0-flash`

**Failure modes:** Same pattern as OpenAI.

---

## Anthropic API

**Purpose:** LLM provider (Claude models).

**Models used:** `claude-3-5-sonnet`, `claude-3-opus`, etc.

**Entry points:** Same as OpenAI — `llm_loader.py` / `llm_picker.py`

**Config required:**
- `ANTHROPIC_API_KEY` environment variable
- Config: `provider: Anthropic`, `model: claude-3-5-sonnet-20241022`

**Failure modes:** Same pattern as OpenAI.

---

## DeepSeek API

**Purpose:** Cost-effective LLM for non-vision tasks. Default provider in `mcp_server.py`.

**Models used:** `deepseek-chat`, `deepseek-reasoner`

**Entry points:** `llm_loader.py` / `llm_picker.py`; `mcp_server.py` uses it directly as default.

**Config required:**
- `DEEPSEEK_API_KEY` environment variable (or `DROIDRUN_DEEPSEEK_KEY` in workspace)
- Config: `provider: DeepSeek`, `model: deepseek-chat`

**Failure modes:** Same pattern as OpenAI. Note: DeepSeek does not support vision/multimodal — using `--vision` with DeepSeek will fail.

---

## OpenRouter API

**Purpose:** Unified LLM routing proxy. Used in `mcp_server.py` for vision tasks (routes to `google/gemini-2.0-flash-001`).

**Entry points:**
- `mcp_server.py` — hardcoded `api_base=https://openrouter.ai/api/v1` when `vision=True`
- `llm_loader.py` — `provider: OpenAILike` with custom `api_base`

**Config required:**
- `OPENROUTER_API_KEY` or `DROIDRUN_OPENROUTER_KEY` environment variable
- OpenRouter is accessed via the `OpenAILike` LlamaIndex provider (compatible with OpenAI SDK format)

**Failure modes:** Same pattern as OpenAI. If the specific routed model (e.g. Gemini) is unavailable on OpenRouter, the request fails.

---

## Ollama (Local)

**Purpose:** Run open-source LLMs locally without API keys.

**Entry points:** `llm_loader.py` — `provider: Ollama`, points to local HTTP server

**Config required:**
- Ollama must be running locally (`ollama serve`)
- Config: `provider: Ollama`, `model: llama3`, `api_base: http://localhost:11434`

**Failure modes:**
- Ollama not running → connection refused; run fails
- Model not pulled → Ollama returns 404; run fails
- Local model too slow → step timeout; Unknown / Needs Verification if timeout is enforced per-LLM-call

---

## MCP Protocol — Client Mode

**Purpose:** DroidRun can consume external MCP tool servers (e.g., a web search MCP, a file system MCP) as additional tools available to the agent.

**Entry points:**
- `src/droidrun/mcp/` — MCP client adapter and config
- `src/droidrun/mcp/client.py` — MCP client that connects to configured servers
- `src/droidrun/mcp/adapter.py` — wraps MCP tools as LlamaIndex `FunctionTool`

**Config required:**
```yaml
mcp:
  servers:
    - name: my_server
      command: ["npx", "-y", "@my/mcp-server"]
```

**Failure modes:**
- MCP server process fails to start → tool unavailable; agent continues without it
- MCP tool call returns error → returned as error string in tool result (not an exception)

---

## MCP Protocol — Server Mode (`mcp_server.py`)

**Purpose:** Exposes DroidRun phone control as MCP tools to Cursor, Claude Desktop, OpenClaw, or any MCP-compatible client.

**Transport:** stdio (stdin/stdout JSON-RPC)

**Entry point:** `mcp_server.py` (root of workspace)

**Tools exposed:**
- `phone_do` — run a natural language task via subprocess `droidrun run`
- `phone_ping` — check Portal/ADB connectivity
- `phone_apps` — list installed apps

**Config required:**
- `DROIDRUN_DEEPSEEK_KEY` for non-vision tasks
- `DROIDRUN_OPENROUTER_KEY` for vision tasks
- ADB on PATH, Tailscale running, device connected

**Failure modes:**
- ADB error → `_ensure_connected()` returns error string; tool returns error text to MCP client (no exception thrown to client)
- Missing API key → error text returned to MCP client
- Subprocess timeout (300s) → `subprocess.TimeoutExpired`; returns error text

---

## PostHog (Telemetry)

**Purpose:** Anonymous usage telemetry — which LLM providers are used, which apps are opened, task success rates. Helps the DroidRun team understand usage patterns.

**Entry points:**
- `src/droidrun/telemetry/tracker.py` — `capture()` function
- Called from `DroidAgentState.update_current_app()` and other state transitions

**Config required:**
- Opt-out: `telemetry.enabled: false` in config
- No API key required (uses hardcoded DroidRun PostHog project key)

**What is captured:** Package/activity visits, step counts, LLM provider names, success/failure booleans. **No task content, no screenshots, no personal data.**

**Failure modes:**
- Network unavailable → silently fails; no impact on agent behavior
- PostHog down → same (fire-and-forget)

---

## Arize Phoenix (Local Tracing)

**Purpose:** Local tracing server for debugging agent behavior. Records LLM calls, token counts, step spans, latency.

**Entry points:**
- `src/droidrun/telemetry/phoenix.py` — Phoenix setup
- `src/droidrun/agent/utils/tracing_setup.py` — configures OpenTelemetry exporter

**Config required:**
- `tracing.provider: phoenix` in config (default)
- Phoenix must be running: `python -m phoenix.server.main` (separate process)
- Default endpoint: `http://localhost:6006`

**Failure modes:**
- Phoenix not running → tracing silently disabled; agent runs normally
- Connection refused → logged at WARNING once; no retry

---

## Langfuse (Cloud Tracing)

**Purpose:** Cloud-hosted LLM observability platform. Alternative to Phoenix for team-shared trace visibility.

**Entry points:**
- `src/droidrun/telemetry/langfuse_processor.py`
- `src/droidrun/agent/utils/tracing_setup.py`

**Config required:**
- `tracing.provider: langfuse` in config
- `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST` environment variables

**Failure modes:**
- Missing env vars → Langfuse disabled; agent runs normally
- Network error → traces lost silently

---

## Bitwarden Secrets Manager (Workspace-Specific)

**Purpose:** Inject API keys (DeepSeek, OpenRouter, etc.) as process environment variables at Cursor launch time. Keeps secrets out of files entirely.

**Scope:** This is a workspace-level operational practice, not a DroidRun framework feature. DroidRun itself is not aware of Bitwarden — it only sees the resulting environment variables.

**Entry points:** `scripts/store_api_keys_to_env.ps1` (workspace helper script)

**Config required:** Bitwarden CLI (`bws`) installed and authenticated.

**Failure modes:**
- Bitwarden not running / not authenticated → env vars not set → DroidRun fails with "API key not set" error

---

## Tailscale (Workspace-Specific)

**Purpose:** Private VPN network allowing `adb connect` to a remote Android device over the internet securely, without exposing ADB to the public internet.

**Scope:** Workspace-level operational practice, not a DroidRun framework feature.

**Device address in use:** `100.71.228.18:5555` (hardcoded in `mcp_server.py`)

**Failure modes:**
- Tailscale disconnects → ADB connect fails → all MCP tool calls fail
- Tailscale offline: USB ADB still works locally; only remote access is affected
- Port 5555 changes after reboot → `scripts/adb_connect_tailscale.ps1` handles reconnect

---

## mobilerun-sdk

**Purpose:** Unknown / Needs Verification

Listed as a dependency. Likely related to DroidRun Cloud or a managed remote device service. No usage found in the local codebase source files explored.

**Entry points:** Unknown / Needs Verification

**Config required:** Unknown / Needs Verification

**Failure modes:** Unknown / Needs Verification
