# Environment & Configuration Reference

Complete reference for every YAML config key and environment variable in DroidRun v0.5.1. Config lives at `~/.config/droidrun/config.yaml`. Environment variables are loaded from `~/.config/droidrun/.env` (overrides shell env) and Windows `HKCU\Environment`.

---

## YAML Configuration Keys

### `agent` — Core Agent Behavior

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent.name` | string | `"droidrun"` | Display name for the agent (used in logs and traces) |
| `agent.max_steps` | integer | `15` | Maximum number of observe→act steps before the agent stops |
| `agent.reasoning` | boolean | `false` | Enable Manager+Executor two-LLM pipeline |
| `agent.streaming` | boolean | `true` | Stream LLM output to terminal in real time |
| `agent.after_sleep_action` | string | — | Action to perform after a sleep/wait step (e.g., `"screenshot"`) |
| `agent.wait_for_stable_ui` | boolean | — | Wait for the UI tree to stabilize before observing |
| `agent.use_normalized_coordinates` | boolean | — | Use 0–1 normalized coordinates instead of pixel coordinates |

### `agent.fast_agent` — FastAgent (Default) Configuration

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent.fast_agent.vision` | boolean | `false` | Send screenshots to LLM (requires multimodal model) |
| `agent.fast_agent.codeact` | boolean | `false` | Enable CodeAct mode (LLM generates Python code) |
| `agent.fast_agent.parallel_tools` | boolean | — | Allow multiple tool calls in a single LLM response |
| `agent.fast_agent.system_prompt` | string | (built-in) | Override the default system prompt |
| `agent.fast_agent.user_prompt` | string | (built-in) | Override the default user prompt template |
| `agent.fast_agent.safe_execution` | boolean | `true` | Enforce sandbox restrictions for CodeAct mode |
| `agent.fast_agent.execution_timeout` | integer | — | Max seconds for a single code execution (CodeAct) |

### `agent.manager` — Manager LLM (Reasoning Mode)

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent.manager.vision` | boolean | `false` | Enable vision for the Manager LLM |
| `agent.manager.system_prompt` | string | (built-in) | Override Manager system prompt |
| `agent.manager.stateless` | boolean | — | Reset Manager context between sub-tasks |

### `agent.executor` — Executor LLM (Reasoning Mode)

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent.executor.vision` | boolean | `false` | Enable vision for the Executor LLM |
| `agent.executor.system_prompt` | string | (built-in) | Override Executor system prompt |

### `agent.scripter` — Scripter Sub-Agent

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent.scripter.enabled` | boolean | `false` | Enable the scripter sub-agent |
| `agent.scripter.max_steps` | integer | — | Max steps for the scripter |
| `agent.scripter.execution_timeout` | integer | — | Max seconds per script execution |
| `agent.scripter.system_prompt` | string | (built-in) | Override scripter system prompt |
| `agent.scripter.safe_execution` | boolean | `true` | Enforce sandbox for scripter |

### `agent.app_cards` — Per-App Instructions

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent.app_cards.enabled` | boolean | `false` | Load app-specific instruction cards before tasks |
| `agent.app_cards.mode` | enum | `"local"` | `local` (bundled) or `server` (remote URL) |
| `agent.app_cards.app_cards_dir` | string | (package bundled) | Override path to local app cards directory |
| `agent.app_cards.server_url` | string | — | URL for remote app card server (server mode only) |

---

### `llm_profiles` — LLM Configuration

Each key under `llm_profiles` is a **role name** (`default`, `manager`, `executor`, or custom). At least `default` must be defined.

```yaml
llm_profiles:
  default:
    provider: GoogleGenAI
    model: gemini-2.0-flash
    temperature: 0.0
  manager:
    provider: OpenAI
    model: gpt-4o
    temperature: 0.1
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `llm_profiles.{role}.provider` | string | ✅ | Provider name (see table below) |
| `llm_profiles.{role}.model` | string | ✅ | Model name as accepted by the provider's API |
| `llm_profiles.{role}.temperature` | float | No | Sampling temperature (0.0 = deterministic) |
| `llm_profiles.{role}.base_url` | string | No | Custom API base URL (Ollama, OpenAILike) |
| `llm_profiles.{role}.api_base` | string | No | Alternate key for base URL (some adapters) |
| `llm_profiles.{role}.kwargs` | object | No | Additional kwargs passed to the LlamaIndex adapter constructor |

**Valid `provider` values:**

| Value | LLM Service | Auth Key |
|-------|-------------|----------|
| `GoogleGenAI` | Google Gemini | `GOOGLE_API_KEY` / `GEMINI_API_KEY` |
| `OpenAI` | OpenAI | `OPENAI_API_KEY` |
| `OpenAILike` | Any OpenAI-compatible API | depends on `base_url` |
| `Anthropic` | Anthropic Claude | `ANTHROPIC_API_KEY` |
| `DeepSeek` | DeepSeek | `DEEPSEEK_API_KEY` / `DROIDRUN_DEEPSEEK_KEY` |
| `Ollama` | Local Ollama | none (set `base_url`) |
| `OpenRouter` | OpenRouter aggregator | `DROIDRUN_OPENROUTER_KEY` |

---

### `device` — Target Device

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `device.serial` | string \| null | `null` | ADB device serial; `null` = auto-detect first connected device |
| `device.use_tcp` | boolean | `false` | Use TCP/HTTP transport instead of ADB content provider |
| `device.platform` | string | `"android"` | Target platform (`android`; `ios` is experimental) |
| `device.auto_setup` | boolean | `true` | Automatically install Portal APK if not present |

---

### `telemetry` — Anonymous Usage Tracking

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `telemetry.enabled` | boolean | `true` | Send anonymous usage events to PostHog; set `false` to opt out |

---

### `tracing` — LLM Trace Export

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `tracing.enabled` | boolean | `false` | Enable trace export |
| `tracing.provider` | enum | `"phoenix"` | `phoenix` (Arize Phoenix) or `langfuse` |
| `tracing.langfuse_screenshots` | boolean | `false` | Include device screenshots in Langfuse traces |
| `tracing.langfuse_secret_key` | string | — | Langfuse secret key (prefer env var) |
| `tracing.langfuse_public_key` | string | — | Langfuse public key |
| `tracing.langfuse_host` | string | — | Langfuse instance URL (default: Langfuse cloud) |

---

### `logging` — Log & Trajectory Settings

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `logging.debug` | boolean | `false` | Enable verbose debug logging |
| `logging.save_trajectory` | enum | `"none"` | `none`, `step` (per-step JSON), or `action` (per-action JSON) |
| `logging.trajectory_path` | string | `"trajectories/"` | Directory for trajectory output (relative to CWD) |
| `logging.trajectory_gifs` | boolean | `false` | Compile screenshots into an animated GIF per run |
| `logging.rich_text` | boolean | `true` | Use Rich library for formatted terminal output |

---

### `safe_execution` — Code Sandbox (CodeAct Mode)

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `safe_execution.allow_all_imports` | boolean | `false` | Disable import restrictions (disables sandbox protection) |
| `safe_execution.allowed_modules` | list[string] | (built-in list) | Whitelist of importable module names |
| `safe_execution.blocked_modules` | list[string] | (built-in list) | Blacklist of module names; takes precedence over `allowed_modules` |
| `safe_execution.allow_all_builtins` | boolean | `false` | Disable builtin restrictions |
| `safe_execution.blocked_builtins` | list[string] | (built-in list) | Blacklist of Python builtins (e.g., `exec`, `eval`, `__import__`) |

---

### `tools` — Tool Selection

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `tools.disabled_tools` | list[string] | `[]` | Tool names to exclude from the agent's tool set (by tool function name) |

---

### `credentials` — App Credential Injection

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `credentials.enabled` | boolean | `false` | Enable credential manager |
| `credentials.file_path` | string | `"config/credentials.yaml"` | Path to credentials YAML file (relative to CWD) |

---

### `mcp` — MCP Client Configuration

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mcp.enabled` | boolean | `false` | Enable MCP client (consume external MCP tools) |
| `mcp.servers.{name}.command` | string | — | Executable to launch the MCP server subprocess |
| `mcp.servers.{name}.args` | list[string] | `[]` | Arguments passed to the command |
| `mcp.servers.{name}.env` | object | `{}` | Environment variables injected into the server process |

**Example:**

```yaml
mcp:
  enabled: true
  servers:
    filesystem:
      command: npx
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/data"]
      env: {}
```

---

## Environment Variables

### Standard Framework Env Vars

These are read by the LlamaIndex LLM adapters. Set in `~/.config/droidrun/.env` or as shell env vars.

| Variable | Provider | Required For |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | Google Gemini | `provider: GoogleGenAI` |
| `GEMINI_API_KEY` | Google Gemini | `provider: GoogleGenAI` (alternate name) |
| `OPENAI_API_KEY` | OpenAI | `provider: OpenAI` or `provider: OpenAILike` |
| `ANTHROPIC_API_KEY` | Anthropic | `provider: Anthropic` |
| `DEEPSEEK_API_KEY` | DeepSeek | `provider: DeepSeek` |

### Workspace-Specific Env Vars (Windows)

Stored in Windows `HKCU\Environment` registry. Injected by workspace PowerShell scripts.

| Variable | Provider | Source |
|----------|----------|--------|
| `DROIDRUN_DEEPSEEK_KEY` | DeepSeek | Bitwarden secret `14d69c11-99ba-428f-a656-b40e014e72ae` |
| `DROIDRUN_OPENROUTER_KEY` | OpenRouter | Bitwarden secret `f9ed80a7-fc35-4add-96d6-b40e0163b041` |

> These are workspace-specific aliases. DroidRun's `llm_loader` reads them as fallbacks when the standard `DEEPSEEK_API_KEY` is not set.

### Tracing Env Vars (Optional)

Used when `tracing.provider: langfuse`. Can be set as env vars instead of embedding values in `config.yaml`.

| Variable | Description |
|----------|-------------|
| `LANGFUSE_SECRET_KEY` | Langfuse secret key |
| `LANGFUSE_PUBLIC_KEY` | Langfuse public key |
| `LANGFUSE_HOST` | Langfuse instance URL (default: Langfuse cloud) |

### Bitwarden Secrets Manager

| Variable | Description |
|----------|-------------|
| `BWS_ACCESS_TOKEN` | Machine account token for `bws` CLI; read by `store_api_keys_to_env.ps1` at setup time |

> `BWS_ACCESS_TOKEN` grants access to the Bitwarden Secrets Manager vault. It is itself a secret — store it only in the Windows Credential Manager or a secure vault, never in a file.

---

## Config Precedence (highest to lowest)

```
1. CLI flags (--model, --provider, --vision, --steps, ...)
2. ~/.config/droidrun/.env file values
3. Shell environment variables (current session)
4. Windows HKCU\Environment registry values
5. ~/.config/droidrun/config.yaml values
6. Built-in defaults
```

---

## Minimal Working Config Example

```yaml
_version: 3

llm_profiles:
  default:
    provider: GoogleGenAI
    model: gemini-2.0-flash
    temperature: 0.0

agent:
  max_steps: 20

device:
  auto_setup: true

telemetry:
  enabled: false
```

With `GOOGLE_API_KEY` set in `~/.config/droidrun/.env`, this is sufficient to run `droidrun run "open Settings"`.
