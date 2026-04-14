# Dependency Inventory

Source of truth: `pyproject.toml`. Last verified against: **v0.5.1**.

> **Risk legend**
> - 🔴 Pinned (exact version) — update blocked; drift risk
> - 🟡 Floor-pinned (>=) — may drift on fresh install; review on major bumps
> - ⚠️ Unknown — version or purpose not fully confirmed

---

## Runtime Core

These packages are installed for all users regardless of which LLM extras are selected.

| Package | Constraint | Purpose | Risk notes |
|---|---|---|---|
| `async_adbutils` | (unversioned) | Async ADB client — device communication | ⚠️ No version pin; API changes will break silently |
| `llama-index` | `==0.14.4` | Core AI orchestration framework | 🔴 Pinned; current upstream is much newer — evaluate migration |
| `posthog` | `>=6.7.6` | Anonymous usage telemetry | 🟡 |
| `pydantic` | `>=2.11.10` | Data validation and settings | 🟡 |
| `rich` | `>=14.1.0` | Terminal output formatting | 🟡 |
| `arize-phoenix` | `>=12.3.0` | Local LLM trace server | 🟡 |
| `httpx` | `>=0.27.0` | Async HTTP client (Portal API, provider calls) | 🟡 |
| `llama-index-callbacks-arize-phoenix` | `>=0.6.1` | Phoenix integration for llama-index | 🟡 |
| `llama-index-workflows` | `==2.8.3` | Workflow orchestration layer | 🔴 Pinned; tied to pinned `llama-index` version |
| `aiofiles` | `>=25.1.0` | Async file I/O | 🟡 |
| `textual` | `>=6.11.0` | Terminal UI framework | 🟡 |
| `mcp` | `>=1.26.0` | Model Context Protocol server/client | 🟡 |
| `python-dotenv` | `>=1.2.1` | `.env` file loading | 🟡 |
| `mobilerun-sdk` | ⚠️ unknown | Unknown version; unknown purpose | ⚠️ Needs clarification |

---

## Runtime LLM Providers (Core — Always Installed)

These are included in the base install, not gated behind extras:

| Package | Constraint | Provider |
|---|---|---|
| `llama-index-llms-openai` | `>=0.5.6` | OpenAI (GPT-4o, etc.) |
| `llama-index-llms-openai-like` | `>=0.5.1` | OpenAI-compatible endpoints (e.g. local models) |
| `llama-index-llms-google-genai` | `>=0.8.5` | Google Gemini |
| `llama-index-llms-ollama` | `>=0.7.2` | Ollama (local models) |
| `llama-index-llms-openrouter` | `>=0.4.2` | OpenRouter (multi-provider routing) |

---

## Optional Extras

Install with: `pip install -e ".[<extra>]"`

### `anthropic`
| Package | Constraint | Notes |
|---|---|---|
| `anthropic` | `>=0.67.0` | Anthropic SDK |
| `llama-index-llms-anthropic` | `>=0.8.6,<0.9.0` | 🔴 Upper-bound pinned — must not upgrade past 0.9.0 until tested |

### `deepseek`
| Package | Constraint | Notes |
|---|---|---|
| `llama-index-llms-deepseek` | `>=0.2.1` | DeepSeek provider integration |

### `langfuse`
| Package | Constraint | Notes |
|---|---|---|
| `langfuse` | `==3.12.1` | 🔴 Pinned; cloud LLM tracing |
| `openinference-instrumentation-llama-index` | `>=3.0.0` | Phoenix/OTEL instrumentation bridge |
| `llama-index-instrumentation` | (unversioned) | ⚠️ No version pin |

---

## Dev Extra

Install with: `pip install -e ".[dev]"`

| Package | Constraint | Purpose |
|---|---|---|
| `black` | `==25.9.0` | 🔴 Pinned; code formatter |
| `ruff` | `>=0.13.0` | Linter / import sorter |
| `mypy` | `>=1.0.0` | Static type checker |
| `bandit` | `>=1.8.6` | Security vulnerability scanner |
| `safety` | `>=3.2.11` | Dependency vulnerability audit |

---

## Build System

| Package | Purpose |
|---|---|
| `hatchling` | PEP 517 build backend (declared in `[build-system]`) |

---

## System Tools (Not Python Packages)

These must be installed and available on `PATH` separately:

| Tool | Purpose | Install |
|---|---|---|
| `adb` (Android Platform Tools) | Device communication | [developer.android.com/tools/releases/platform-tools](https://developer.android.com/tools/releases/platform-tools) |
| `Tailscale` | VPN for secure remote ADB | [tailscale.com/download](https://tailscale.com/download) |
| `bws` (Bitwarden Secrets Manager CLI) | Secret injection at startup | [bitwarden.com/products/secrets-manager](https://bitwarden.com/products/secrets-manager/) |
| `PowerShell 5.1+` | Startup scripts, ADB helpers | Built into Windows 10/11 |

---

## Pinned Package Risk Summary

| Package | Pin | Why it matters |
|---|---|---|
| `llama-index==0.14.4` | Exact | Framework is many versions behind; major API changes exist upstream |
| `llama-index-workflows==2.8.3` | Exact | Tied to llama-index pin; upgrade together |
| `llama-index-llms-anthropic<0.9.0` | Upper bound | Compatibility constraint with pinned framework |
| `langfuse==3.12.1` | Exact | Cloud tracing client; API may evolve |
| `black==25.9.0` | Exact | Formatting output stability (acceptable for dev tools) |

---

## Related Files

- `pyproject.toml` — authoritative source
- `docs/build-release-process.md` — how to install and build
- `docs/secrets-handling.md` — which env vars LLM providers require
