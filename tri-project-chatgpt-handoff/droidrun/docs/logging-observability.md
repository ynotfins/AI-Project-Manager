# Logging & Observability

DroidRun has four separate observability layers. This document describes each one, how to configure it, and where to look when things go wrong.

---

## 1. Python Logging (Terminal)

### Logger

DroidRun uses a named logger (`droidrun`) with a custom `CLILogHandler` that formats output via **rich**.

Configuration function:
```python
configure_logging(debug: bool, handler: logging.Handler)
```

### Log levels

| Level | When active | How to enable |
|---|---|---|
| `INFO` | Default | Always on |
| `DEBUG` | Verbose mode | `--debug` CLI flag OR `logging.debug: true` in config YAML |

### Console output

- Step summaries: printed as rich panels after each agent step
- Action results: tool calls and their outcomes, formatted with icons and color
- Errors: printed with traceback in debug mode; short message in normal mode

### MCP server logging

The MCP server (`mcp_server.py`) configures its own log level independently:

```python
# mcp_server.py line 1
logging.basicConfig(level=logging.WARNING)
```

MCP server logs are suppressed below WARNING — only errors and warnings appear in the terminal.

---

## 2. Trajectory Recording

Trajectories capture the full history of an agent run: screenshots, actions, results, and metadata.

### Configuration

In `~/.config/droidrun/config.yaml`:

```yaml
logging:
  save_trajectory: step   # none | step | action
  trajectory_path: trajectories/
  trajectory_gifs: false
```

| Value | Behavior |
|---|---|
| `none` | No trajectory saved |
| `step` | Save one record per agent step (recommended) |
| `action` | Save one record per individual action (verbose) |

### TrajectoryWriter

The `TrajectoryWriter` class handles serialization. Output files are JSON by default; GIFs can be generated from screenshot sequences when `trajectory_gifs: true`.

### Privacy note

Trajectory files contain **device screen content** — whatever was visible on the phone during the run. This may include:
- App content, messages, personal data
- Credentials if they were visible on screen

The `trajectories/` directory should be gitignored and treated as sensitive.

---

## 3. Telemetry (PostHog)

DroidRun sends **anonymous** usage events to PostHog. No PII is collected.

### What is sent

- CLI invocation events
- Agent mode used (e.g., `SimpleAgent`, `CodeActAgent`)
- Model name (e.g., `gpt-4o`, `gemini-2.0-flash`)
- Error types (not error messages or stack traces)

### What is NOT sent

- Task content or instructions
- Screenshots or trajectory data
- API keys or credentials
- Device identifiers

### Disable telemetry

```yaml
# ~/.config/droidrun/config.yaml
telemetry:
  enabled: false
```

Or set the environment variable:
```bash
DROIDRUN_TELEMETRY_DISABLED=true
```

---

## 4. LLM Tracing

LLM tracing captures the full prompt/response cycle for every LLM call: inputs, outputs, tool calls, latency, and token counts.

### Option A: Arize Phoenix (default, local)

Phoenix runs as a local server. No cloud account required.

```yaml
# config.yaml
tracing:
  provider: phoenix
```

Start the Phoenix server:
```bash
python -m phoenix.server.main serve
```

Default UI: `http://localhost:6006`

Traces include:
- Full prompt text sent to LLM
- Full response text
- Tool/function call arguments and results
- Latency per call
- Token counts (input, output, total)
- Span hierarchy (step → action → LLM call)

### Option B: Langfuse (cloud)

Langfuse is an alternative tracing backend with a hosted UI.

Required environment variables:
```
LANGFUSE_SECRET_KEY=...
LANGFUSE_PUBLIC_KEY=...
LANGFUSE_HOST=https://cloud.langfuse.com   # or self-hosted URL
```

Install:
```bash
pip install -e ".[langfuse]"
```

Configuration:
```yaml
tracing:
  provider: langfuse
  langfuse_screenshots: true   # uploads screenshots alongside traces (cloud)
```

> **Privacy note:** When `langfuse_screenshots: true`, device screenshots are uploaded to the configured Langfuse host. Disable this on production devices or when handling sensitive data.

---

## Where to Look First When Something Fails

Work through this sequence in order:

| Priority | Source | How to access |
|---|---|---|
| 1 | Terminal output | Read the console — errors are printed with rich formatting |
| 2 | Debug mode | Re-run with `--debug` to get full stack traces and verbose logs |
| 3 | ADB logcat | `adb logcat \| Select-String "DroidRun"` (PowerShell) or `adb logcat \| grep DroidRun` |
| 4 | Trajectory file | Open the latest file in `trajectories/` — shows each step with screenshots |
| 5 | Phoenix traces | `http://localhost:6006` — drill into the failing LLM call's inputs/outputs |
| 6 | Langfuse traces | Your Langfuse project dashboard — if Langfuse is configured as provider |

---

## Quick Reference: Config Keys

```yaml
# ~/.config/droidrun/config.yaml

logging:
  debug: false              # set true for DEBUG level output
  save_trajectory: step     # none | step | action
  trajectory_path: trajectories/
  trajectory_gifs: false

telemetry:
  enabled: true             # set false to opt out

tracing:
  provider: phoenix         # phoenix | langfuse
  langfuse_screenshots: false
```

---

## Related Files

- `docs/secrets-handling.md` — Langfuse key names and storage
- `docs/troubleshooting-playbook.md` — log-first debug workflow
