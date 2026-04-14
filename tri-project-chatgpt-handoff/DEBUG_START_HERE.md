# DEBUG_START_HERE

This export is for first-pass inspection/debugging, not for turnkey deployment. Real secrets and machine-local config were intentionally excluded.

## 1. Install Dependencies

### AI-Project-Manager

Main repo behavior is docs/scripts, so there is no required repo-root install.

Optional package install:

```powershell
cd AI-Project-Manager/package
pnpm install
pnpm build
```

Optional local OpenMemory server:

```powershell
cd AI-Project-Manager
python scripts/openmemory_cursor_server.py
```

### open--claw

There is no single repo-root package install. Install only the package(s) you want to run.

Voice service:

```powershell
cd open--claw/open-claw/services/voice-front-desk-agent
npm install
npm run dev
```

Representative worker package pattern:

```powershell
cd open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/accessibility-auditor
npm install
```

Important note:
- Multiple worker packages shell out to a globally installed `openclaw` CLI (`openclaw.cmd` on Windows) and expect the OpenClaw gateway env vars to already exist.
- Repo docs reference an external dashboard/gateway command such as `pnpm openclaw dashboard --no-open`, but that CLI is not vendored by this repo.

### droidrun

The repo-root operational layer expects a virtualenv at `.venv`, while the actual Python package lives under `src/`.

```powershell
cd droidrun
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e .\src
```

Optional extras if needed:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".\src[anthropic,dev]"
```

## 2. Start Order

### Minimal code-understanding mode

1. Read `WORKSPACE_MAP.md`.
2. Start with `AI-Project-Manager/docs/tooling/MCP_CANONICAL_CONFIG.md`.
3. Read `open--claw/open-claw/docs/MODULES.md` and `open--claw/open-claw/docs/INTEGRATIONS.md`.
4. Read `droidrun/docs/PROJECT_INTELLIGENCE_INDEX.md` and `droidrun/docs/entry-points-and-boot-sequence.md`.

### Minimal runtime-debug mode

1. Prepare DroidRun first.

```powershell
cd droidrun
.\scripts\start_mcp_server.ps1
```

If you are not using the helper script, the equivalent is:

```powershell
cd droidrun
.\.venv\Scripts\python.exe mcp_server.py
```

2. Confirm phone connectivity.

```powershell
cd droidrun
.\.venv\Scripts\droidrun.exe ping -d 100.71.228.18:5555
```

3. Start the OpenClaw gateway / dashboard externally.

```powershell
pnpm openclaw dashboard --no-open
```

Treat this as documented intent, not a repo-contained command.

4. Start any OpenClaw service/package under test, such as the voice service.

```powershell
cd open--claw/open-claw/services/voice-front-desk-agent
npm run dev
```

5. Use AI-PM docs for cross-repo architecture, MCP wiring, and process assumptions.

## 3. Do The Projects Run Independently?

- `AI-Project-Manager`: yes, as a docs/orchestration repo; it does not need to be running for code inspection.
- `droidrun`: yes, as a standalone Python CLI/framework.
- `open--claw`: partially; individual packages can run independently, but the broader intended behavior depends on external gateway/tooling and often on DroidRun MCP availability.
- Full tri-workspace behavior requires them together: governance/docs from AI-PM, agent/gateway from OpenClaw, and phone control from DroidRun.

## 4. Required Services / External Systems

Likely required for a realistic first run:

- Global Cursor MCP config at `%USERPROFILE%\.cursor\mcp.json`
- Bitwarden CLI / injected env vars for secrets
- OpenClaw gateway / dashboard on or around port `18789`
- Android phone reachable through ADB over TCP (`100.71.228.18:5555` is the documented device target in this workspace)
- DroidRun Portal APK on the phone, with `adb forward tcp:8080 tcp:8080`
- Optional Twilio + ElevenLabs credentials for the voice service
- Optional tracing backends: Arize Phoenix, Langfuse

## 5. Required / Inferred Env Vars

### AI-Project-Manager

- `CLIENT_NAME`
- `OPENMEMORY_STORE_PATH`
- `OPENMEMORY_DEBUG_LOG` / `OPENMEMORY_TRACE_FILE` (optional)
- `OPENMEMORY_API_KEY` for the packaged installer CLI

### open--claw

- `OPENCLAW_GATEWAY_URL`
- `OPENCLAW_GATEWAY_TOKEN`
- `OPENCLAW_AGENT_ID`
- `OPENCLAW_VERSION`
- provider keys such as `ANTHROPIC_API_KEY`
- channel tokens such as `TELEGRAM_BOT_TOKEN`, `DISCORD_BOT_TOKEN`, `SLACK_*`
- voice service vars: `PORT`, `PUBLIC_BASE_URL`, `TWILIO_*`, `ELEVENLABS_*`, `VOICE_WEBSOCKET_PATH`

### droidrun

- config file: `~/.config/droidrun/config.yaml`
- env file: `~/.config/droidrun/.env`
- provider keys: `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `DEEPSEEK_API_KEY`
- workspace-specific fallbacks: `DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY`
- optional tracing vars: `LANGFUSE_SECRET_KEY`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_HOST`

## 6. Probable Failure Points

- Missing `droidrun/src` submodule content.
- Missing repo-root `.venv` in `droidrun`, which breaks `scripts/start_mcp_server.ps1` and `mcp_server.py` assumptions.
- Missing or stale ADB wireless-debug address/port after phone reboot.
- Missing Portal APK or broken `adb forward tcp:8080 tcp:8080`.
- Missing `OPENCLAW_GATEWAY_TOKEN` or unreachable OpenClaw gateway.
- Missing globally installed `openclaw` CLI for OpenClaw worker wrappers.
- Missing `%USERPROFILE%\.cursor\mcp.json` or MCP session registration drift.
- Missing Bitwarden-injected secrets for LLM providers.
- Voice-service startup failures if `PUBLIC_BASE_URL`, Twilio, or ElevenLabs env vars are absent.

## 7. API / Proxy / Auth / DB / Worker Notes

- OpenClaw workers use WebSocket gateway connectivity through `OPENCLAW_GATEWAY_URL`, typically `ws://host.docker.internal:18789`.
- DroidRun talks to the local forwarded Portal endpoint at `http://localhost:8080` after ADB forwarding.
- The voice service computes its WebSocket URL from `PUBLIC_BASE_URL` plus `VOICE_WEBSOCKET_PATH` (default `/twilio/voice/ws`).
- AI-PM documents a local OpenMemory SQLite store and a shared Cursor MCP config, but those live outside the repos.
- Firestore and Mem0 appear as target integrations in OpenClaw docs, not as fully self-contained repo-local services in this export.
- No obvious queue/broker like Redis or Kafka appeared in the first-pass inspection; worker/background behavior is process-based.

## 8. Best First Debug Reads

If a first run fails, read in this order:

1. `AI-Project-Manager/docs/tooling/MCP_CANONICAL_CONFIG.md`
2. `AI-Project-Manager/docs/release/system-architecture.md`
3. `open--claw/open-claw/docs/MODULES.md`
4. `open--claw/open-claw/docs/INTEGRATIONS.md`
5. `open--claw/open-claw/services/voice-front-desk-agent/src/config/env.mjs`
6. `droidrun/docs/PROJECT_INTELLIGENCE_INDEX.md`
7. `droidrun/docs/entry-points-and-boot-sequence.md`
8. `droidrun/mcp_server.py`
