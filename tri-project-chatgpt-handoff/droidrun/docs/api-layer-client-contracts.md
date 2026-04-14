# API Layer & Client Contracts

This document describes every API client and server boundary in DroidRun: how they are authenticated, what data they exchange, and what error handling applies.

---

## 1. PortalClient — Android Device Bridge

**File:** `src/droidrun/tools/android/portal_client.py`

The PortalClient is the primary interface between the DroidRun agent and the Android device. It supports two transports, selected by config.

### Transports

| Transport | Config | Mechanism | When Used |
|-----------|--------|-----------|-----------|
| ADB Content Provider | `device.use_tcp = false` (default) | `adb shell content query --uri content://com.droidrun.portal/...` via `async_adbutils` | Default; no port forwarding needed |
| TCP / HTTP | `device.use_tcp = true` | HTTP to `localhost:8080` (or device IP) via `httpx` | When ADB is unavailable or for remote devices |

### Endpoints (TCP mode — HTTP on port 8080)

| Endpoint | Method | Purpose | Request Body | Response |
|----------|--------|---------|-------------|----------|
| `/ui` | `GET` | Fetch accessibility tree of current screen | none | JSON: UI node tree |
| `/action` | `POST` | Send action to device | JSON action payload | JSON: success/error |

### Action Types (`/action` payload)

```json
{ "type": "tap",        "x": 540, "y": 960 }
{ "type": "swipe",      "x1": 540, "y1": 1500, "x2": 540, "y2": 500, "duration": 300 }
{ "type": "type",       "text": "hello world" }
{ "type": "key",        "keycode": 3 }
{ "type": "screenshot"  }
```

### Authentication

- **None.** Security is provided by ADB trust (USB or `adb tcpip` pairing). The portal HTTP server binds only to localhost (or the device's ADB-forwarded port).

### Error Handling

```
TCP timeout
    └─► PortalClient falls back to ADB content provider transport
        (if ADB is available)

ADB not connected
    └─► Raises DeviceNotFoundError; droidrun doctor will report this

Portal APK not installed / not running
    └─► HTTP 404 or connection refused; user runs `droidrun setup`
```

---

## 2. LLM API Clients — via LlamaIndex Adapters

DroidRun uses LlamaIndex LLM adapters. The `llm_loader` module maps `provider` + `model` strings from config to the appropriate adapter.

### Provider → Adapter Mapping

| `provider` value | LlamaIndex Package | Auth Env Var | Notes |
|------------------|--------------------|--------------|-------|
| `GoogleGenAI` | `llama-index-llms-google-genai` | `GOOGLE_API_KEY` or `GEMINI_API_KEY` | Gemini models |
| `OpenAI` | `llama-index-llms-openai` | `OPENAI_API_KEY` | GPT-4o, o-series |
| `OpenAILike` | `llama-index-llms-openai-like` | per `base_url` / `api_base` | OpenRouter, local OpenAI-compatible servers |
| `Anthropic` | `llama-index-llms-anthropic` | `ANTHROPIC_API_KEY` | Claude models (optional extra) |
| `DeepSeek` | `llama-index-llms-deepseek` | `DEEPSEEK_API_KEY` or `DROIDRUN_DEEPSEEK_KEY` | DeepSeek-R1 etc. |
| `Ollama` | `llama-index-llms-ollama` | none | Local inference; `base_url` required |
| `OpenRouter` | `llama-index-llms-openrouter` | `DROIDRUN_OPENROUTER_KEY` | Aggregator; many models |

### Config Shape (per LLM profile)

```yaml
llm_profiles:
  default:
    provider: GoogleGenAI
    model: gemini-2.0-flash
    temperature: 0.0
    # Optional overrides:
    base_url: https://...    # for OpenAILike / Ollama
    api_base: https://...    # alternate key for base URL
    kwargs: {}               # passed through to adapter constructor
```

### Auth Resolution Order

1. Value in `~/.config/droidrun/.env` (managed by `env_keys.py`)
2. Shell environment variable (inherited process env)
3. Windows HKCU\Environment (workspace-specific keys, injected by startup scripts)

### Error Handling

- Missing API key → `AuthenticationError` from adapter; DroidRun prints actionable message.
- Rate limit / 429 → propagated as exception; no automatic retry (LlamaIndex default behavior).
- Model not found → adapter raises; user must correct `model` in config.

---

## 3. MCP Server — Phone Control as MCP Tools

**File:** `src/droidrun/mcp_server.py`

DroidRun can expose Android device control as an MCP (Model Context Protocol) server, allowing AI clients (Claude Desktop, Cursor Agent, etc.) to drive the phone.

### Protocol

- **Transport:** stdio JSON-RPC (standard MCP stdio transport)
- **Authentication:** None (local process, trusted caller)
- **Discovery:** Client calls `list_tools` to enumerate available tools

### Exposed Tools

| Tool | Signature | Description |
|------|-----------|-------------|
| `phone_do` | `phone_do(goal: str, vision: bool = False)` | Run a DroidRun agent task on the device |
| `phone_ping` | `phone_ping()` | Check portal health; returns `ok` or error |
| `phone_apps` | `phone_apps()` | List installed apps on device |

### Invocation Example

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "phone_do",
    "arguments": { "goal": "open Maps and search for coffee", "vision": false }
  },
  "id": 1
}
```

### Response Shape

```json
{
  "jsonrpc": "2.0",
  "result": { "content": [{ "type": "text", "text": "Task completed: ..." }] },
  "id": 1
}
```

---

## 4. MCP Client Manager — Consuming External MCP Servers

**File:** `src/droidrun/mcp/client.py` — class `MCPClientManager`

When `mcp.enabled = true` in config, DroidRun's agent can call tools provided by external MCP servers (e.g., a file system MCP, a web search MCP).

### Supported Transports

| Transport | Config | When Used |
|-----------|--------|-----------|
| stdio | `command` + `args` | Local MCP servers launched as subprocesses |
| HTTP | `url` | Remote MCP servers |

### Config Shape

```yaml
mcp:
  enabled: true
  servers:
    filesystem:
      command: npx
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
      env: {}
    websearch:
      command: uvx
      args: ["mcp-server-fetch"]
```

### Client Lifecycle

```
1. MCPClientManager.connect(server_name)
   └─ Spawns subprocess or connects HTTP

2. list_tools()
   └─ Returns [{name, description, inputSchema}, ...]

3. call_tool(name, arguments)
   └─ Sends JSON-RPC call
   └─ Returns tool result (text / image / structured)

4. disconnect()
   └─ Terminates subprocess or closes HTTP session
```

### Error Handling

- Server fails to start → `MCPConnectionError`; agent logs warning, continues without that server's tools
- Tool call timeout → configurable timeout; raises `MCPTimeoutError`

---

## 5. GitHub / ungh.cc — Portal APK Download

**Used by:** `droidrun setup`

| Property | Value |
|----------|-------|
| Primary URL | `https://api.github.com/repos/droidrun/droidrun/releases/latest` |
| Fallback URL | `https://ungh.cc/repos/droidrun/droidrun/releases/latest` (rate-limit-free mirror) |
| Auth | None (public repository) |
| Method | `GET` |
| Response | JSON: release metadata + asset download URLs |
| Asset | `portal.apk` (package: `com.droidrun.portal`) |

The APK is downloaded via `httpx` with a progress indicator, then installed via `adb install`.

---

## 6. PostHog — Anonymous Telemetry

**Controlled by:** `telemetry.enabled` (default: `true`)

| Property | Value |
|----------|-------|
| SDK | `posthog` Python library |
| Host | PostHog cloud (posthog.com) |
| Delivery | Fire-and-forget; non-blocking background thread |
| Data | Anonymous events: command used, agent mode, provider type, success/failure |
| PII | None. No device identifiers, no task content, no API keys |
| Opt-out | Set `telemetry.enabled: false` in `~/.config/droidrun/config.yaml` |

---

## 7. Arize Phoenix — Trace Export

**Controlled by:** `tracing.enabled = true`, `tracing.provider = phoenix`

| Property | Value |
|----------|-------|
| Protocol | OTLP (OpenTelemetry Protocol) |
| Default endpoint | `http://localhost:6006` (local Phoenix server) |
| Integration | `openinference-instrumentation-llama-index` auto-instruments LLM calls |
| Auth | None for local; API key if using Phoenix Cloud |
| Data | LLM prompt/response pairs, tool calls, latencies, token counts |

**Start Phoenix locally:**
```bash
pip install arize-phoenix
python -m phoenix.server.main
```

---

## 8. Langfuse — Trace Export (Alternative)

**Controlled by:** `tracing.enabled = true`, `tracing.provider = langfuse`

| Property | Value |
|----------|-------|
| Protocol | HTTP POST to Langfuse ingest API |
| Config keys | `tracing.langfuse_public_key`, `tracing.langfuse_secret_key`, `tracing.langfuse_host` |
| Auth | Public key + Secret key (Basic Auth) |
| Data | LLM traces; optionally screenshots (`tracing.langfuse_screenshots: true`) |
| Self-host | Set `langfuse_host` to your self-hosted instance URL |

**Required packages:**
```bash
pip install langfuse openinference-instrumentation-llama-index
```

---

## Summary — Authentication Matrix

| Client | Auth Method | Secret Location |
|--------|-------------|-----------------|
| PortalClient (ADB) | ADB device trust | ADB key pair (`~/.android/adbkey`) |
| PortalClient (TCP) | None (localhost only) | — |
| OpenAI | API key | `OPENAI_API_KEY` env var / `.env` |
| Gemini | API key | `GOOGLE_API_KEY` / `GEMINI_API_KEY` |
| Anthropic | API key | `ANTHROPIC_API_KEY` |
| DeepSeek | API key | `DEEPSEEK_API_KEY` / `DROIDRUN_DEEPSEEK_KEY` |
| OpenRouter | API key | `DROIDRUN_OPENROUTER_KEY` |
| Ollama | None | — |
| MCP Server | None | — |
| MCP Client | None (local) | per-server env config |
| GitHub API | None (public) | — |
| PostHog | Project key (hardcoded in lib) | — |
| Phoenix | None / API key | env var (if cloud) |
| Langfuse | Public + Secret key | `tracing.*` config keys |
