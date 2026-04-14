# Storage Layer

DroidRun uses **file-based storage only** — no SQL database, no Redis, no cloud sync, no session persistence between runs. All state is either in YAML/YAML-like config files, flat env files, or output files written during a run.

---

## Overview

| Store | Location | Format | Managed By |
|-------|----------|--------|------------|
| User config | `~/.config/droidrun/config.yaml` | YAML (schema v3) | `ConfigLoader` |
| API key store | `~/.config/droidrun/.env` | dotenv | `env_keys.py` |
| Trajectory files | `trajectories/` (relative to CWD, or configured path) | JSON + GIF | `TrajectoryWriter` |
| App cards | `src/droidrun/config/app_cards/` (bundled) | JSON + Markdown | `LocalAppCardProvider` |
| Credentials file | `config/credentials.yaml` (relative to CWD) | YAML | `FileCredentialManager` |
| Windows env vars | `HKCU\Environment` registry key | Registry string values | PowerShell setup scripts |

---

## 1. User Config — `~/.config/droidrun/config.yaml`

**Location resolution:** Uses `platformdirs.user_config_dir("droidrun")` — portable across OS.

| Platform | Resolved Path |
|----------|--------------|
| Linux / macOS | `~/.config/droidrun/config.yaml` |
| Windows | `%APPDATA%\droidrun\config.yaml` |

### Format

```yaml
_version: 3

agent:
  max_steps: 15
  reasoning: false
  vision: false
  streaming: true
  # ... (see environment-config-reference.md for full schema)

device:
  serial: null
  use_tcp: false
  auto_setup: true

tracing:
  enabled: false
  provider: phoenix

telemetry:
  enabled: true

logging:
  debug: false
  save_trajectory: none
```

### Schema Versioning & Migration

- The `_version` key tracks the config schema version (currently `3`).
- `ConfigLoader` reads the version and applies any necessary migrations before returning the config object.
- Users should not edit `_version` manually.

### Write Behavior

- Config is read at startup and never written back automatically (no auto-save during a run).
- The TUI writes config changes to disk on explicit save.
- CLI flags override config values in memory for the duration of that run only.

---

## 2. API Key Store — `~/.config/droidrun/.env`

**File:** Same directory as `config.yaml`, named `.env`.

### Format

Standard `python-dotenv` format:

```dotenv
GOOGLE_API_KEY=AIza...
GEMINI_API_KEY=AIza...
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

### Managed Keys

| Key | Provider |
|-----|---------|
| `GOOGLE_API_KEY` | Google Gemini |
| `GEMINI_API_KEY` | Google Gemini (alternate) |
| `OPENAI_API_KEY` | OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic Claude |

Keys are read and written by `env_keys.py`. The TUI "Models" tab provides a UI for entering and saving these keys.

### Precedence

```
~/.config/droidrun/.env  (highest)
    ↓ overrides
Shell environment variables
    ↓ overrides
Windows HKCU\Environment (lowest, set at login)
```

> The `.env` file is **never committed to git**. It is listed in `.gitignore`.

---

## 3. Trajectory Files — `trajectories/`

**Written when:** `logging.save_trajectory` is not `"none"`.

### Modes

| `save_trajectory` value | Behavior |
|------------------------|----------|
| `"none"` (default) | No files written |
| `"step"` | One JSON file per agent step (observe + plan + action) |
| `"action"` | One JSON file per action sent to device |

### Directory

```
trajectories/
├── run_20240315_142301/
│   ├── step_001.json
│   ├── step_002.json
│   └── ...
└── run_20240315_143005/
    └── ...
```

Default: `trajectories/` relative to the current working directory when `droidrun run` is executed. Override with `logging.trajectory_path`.

### GIF Recording

When `logging.trajectory_gifs: true`, `TrajectoryWriter` also compiles screenshots into an animated GIF per run:

```
trajectories/
└── run_20240315_142301/
    ├── step_001.json
    └── session.gif
```

### JSON Schema (per step)

```json
{
  "step": 1,
  "timestamp": "2024-03-15T14:23:05Z",
  "observation": { "ui_tree": { ... }, "screenshot_base64": "..." },
  "thought": "I need to tap the search bar...",
  "action": { "type": "tap", "x": 540, "y": 200 }
}
```

---

## 4. App Cards — `src/droidrun/config/app_cards/`

App cards provide per-app instructions that help the agent navigate specific applications more effectively (e.g., login flows, known UI quirks).

### Location

Bundled inside the installed package:

```
src/droidrun/config/app_cards/
├── gmail.md
├── chrome.md
├── settings.md
└── ...
```

### Format

Each card is a Markdown file (optionally with a paired JSON metadata file) keyed by app package name or common name.

### Access Modes

| `agent.app_cards.mode` | Source |
|------------------------|--------|
| `local` (confirmed working) | Reads from the bundled `app_cards/` directory |
| `server` (status unknown) | Fetches from a remote URL (`agent.app_cards.server_url`) |

`LocalAppCardProvider` resolves the directory via the installed package path — users do not need to manage this directory manually.

---

## 5. Credentials File — `config/credentials.yaml`

**Active when:** `credentials.enabled: true` in user config.

### Location

Relative to the current working directory:

```
config/
├── credentials.yaml        ← active credentials file
└── credentials_example.yaml ← template (do not edit; copy to credentials.yaml)
```

### Format

See `config/credentials_example.yaml` for the full template. General shape:

```yaml
accounts:
  google:
    username: user@example.com
    password: "{{ env:GOOGLE_PASSWORD }}"   # never hardcode; reference env var
  some_app:
    username: myuser
    password: "{{ env:APP_PASSWORD }}"
```

`FileCredentialManager` reads this at runtime and injects credentials when the agent needs to authenticate inside an app.

> **Security note:** Never hardcode passwords in `credentials.yaml`. Use `{{ env:VAR }}` interpolation to reference environment variables. The file itself must not be committed to git.

---

## 6. Windows Environment Variables — `HKCU\Environment`

Used in the workspace-specific Windows development setup. These are **persistent** Windows user environment variables (survive reboots, unlike session env vars).

### Keys

| Variable | Purpose | Set By |
|----------|---------|--------|
| `DROIDRUN_DEEPSEEK_KEY` | DeepSeek API key (workspace-specific name) | `store_api_keys_to_env.ps1` |
| `DROIDRUN_OPENROUTER_KEY` | OpenRouter API key | `store_api_keys_to_env.ps1` |

### How They Are Set

```powershell
# Sourced from Bitwarden Secrets Manager machine account
# Secret IDs (not values — values are fetched at runtime):
#   DeepSeek  = 14d69c11-99ba-428f-a656-b40e014e72ae
#   OpenRouter = f9ed80a7-fc35-4add-96d6-b40e0163b041

[System.Environment]::SetEnvironmentVariable(
    "DROIDRUN_DEEPSEEK_KEY",
    $secretValue,
    [System.EnvironmentVariableTarget]::User
)
```

Scripts involved:

- `setup_windows_host.ps1` — one-time initial setup
- `startup_droidrun.ps1` — injects keys into current shell session (reads from registry)
- `store_api_keys_to_env.ps1` — fetches from Bitwarden and writes to registry

### Precedence

Registry env vars are available to any process launched as that Windows user, but are overridden by the `~/.config/droidrun/.env` file if the same key appears there.

---

## What DroidRun Does NOT Store

| Common pattern | DroidRun status |
|----------------|-----------------|
| SQLite database | Not used |
| Redis / cache | Not used |
| Cloud sync | Not used |
| Session state between runs | Not persisted — each `droidrun run` starts fresh |
| Conversation history | Not persisted (in-memory only during a run) |
| User accounts | Not applicable |
