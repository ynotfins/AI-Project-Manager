# WORKSPACE_MAP

Workspace name: `openclaw.code-workspace`

This export contains a tri-project, multi-root workspace:

1. `AI-Project-Manager`
   - Role: orchestration and governance layer.
   - What lives here: Cursor rules, agent workflow docs, state/handoff tracking, MCP configuration references, OpenMemory helper scripts, and a small `package/` CLI package.
   - Main tech: Markdown/JSON docs, PowerShell, Python, small TypeScript package managed with `pnpm`.

2. `open--claw`
   - Role: agent brain / runtime and product-charter repo.
   - What lives here: repo-root governance/docs plus runtime content mainly under `open-claw/`, including AI employee packages, integration docs, worker wrappers, and a Twilio + ElevenLabs voice service.
   - Main tech: Node.js packages (`npm`/`package-lock.json` in subpackages), JavaScript/ESM, Python helper scripts, Dockerfiles.

3. `droidrun`
   - Role: actuator layer for phone automation.
   - What lives here: Windows workspace glue at repo root plus the upstream Python framework as the `src/` git submodule snapshot, local MCP server, PowerShell launch scripts, and extensive architecture/debug docs.
   - Main tech: Python 3.11-3.13, Hatchling build, Click CLI, Textual TUI, LlamaIndex workflows, ADB + Portal APK.

## Multi-Root Assessment

This is a multi-root workspace, not a single monorepo.

- There is no shared top-level `package.json`, `pnpm-workspace.yaml`, `turbo.json`, or `nx.json` spanning all three projects.
- The projects are wired together by a Cursor workspace file, shared operational docs, MCP servers, environment conventions, and runtime service boundaries.
- Shared governance flows from `AI-Project-Manager` into the sibling repos through mirrored `.cursor/rules` and documented operating contracts.

## Dependency / Communication Map

- `AI-Project-Manager` -> `open--claw`
  - Provides the canonical tri-workspace governance, state tracking, tooling policy, and MCP configuration references.
- `AI-Project-Manager` -> `droidrun`
  - Provides the same governance/process layer and cross-repo operating context.
- `open--claw` -> `droidrun`
  - Uses DroidRun MCP tools for phone control.
  - Expected tools: `phone_do`, `phone_ping`, `phone_apps`.
- `open--claw` -> external OpenClaw gateway
  - Worker env examples reference `OPENCLAW_GATEWAY_URL=ws://host.docker.internal:18789` plus a gateway token and agent ID.
- `droidrun` -> Android device
  - Connects via ADB, forwards `tcp:8080`, and talks to the on-device DroidRun Portal over `http://localhost:8080` after port-forwarding.
- `AI-Project-Manager` -> external tooling runtime
  - References global Cursor MCP config at `%USERPROFILE%\.cursor\mcp.json` and a local OpenMemory compatibility server script.

## Important Ports / URLs

- `18789`: OpenClaw gateway / dashboard endpoint referenced in docs and worker env examples.
- `18792`: OpenClaw health endpoint referenced in AI-PM architecture docs.
- `8788`: `open-claw/services/voice-front-desk-agent` HTTP service default.
- `8080`: DroidRun Portal on the Android device; exposed locally through `adb forward tcp:8080 tcp:8080`.
- `5555`: ADB over TCP / wireless debugging.
- `8766`: OpenMemory proxy/bridge mentioned in AI-PM architecture docs.
- `27123` / `27124`: Obsidian local REST plugin HTTP / HTTPS ports referenced by AI-PM docs.

## Package Managers / Build Tooling

- `AI-Project-Manager/package`: `pnpm`, `tsup`, TypeScript.
- `open--claw` runtime packages: `npm` in individual package folders; Dockerfiles exist for multiple employee packages and the voice service.
- `droidrun`: `pip` / virtualenv workflow around `src/pyproject.toml`; build backend is `hatchling`.

## Shared Libraries / Shared Code

There is no obvious shared source package imported directly across all three repos.

The main shared surfaces are:
- shared operational docs and mirrored rules,
- the external Cursor MCP config,
- the OpenClaw gateway contract,
- the DroidRun MCP server boundary,
- and the multi-root workspace definition.

## Environment Expectations

Real secrets are intentionally excluded from this export.

Expected env/config surfaces inferred from code/docs:

- Global Cursor MCP config: `%USERPROFILE%\.cursor\mcp.json`
- AI-PM OpenMemory script:
  - `CLIENT_NAME`
  - `OPENMEMORY_STORE_PATH`
  - `OPENMEMORY_DEBUG_LOG` / `OPENMEMORY_TRACE_FILE` (optional)
  - `OPENMEMORY_API_KEY` for the packaged installer CLI
- OpenClaw workers / voice service:
  - `OPENCLAW_GATEWAY_URL`
  - `OPENCLAW_GATEWAY_TOKEN`
  - `OPENCLAW_AGENT_ID`
  - model-provider keys such as `ANTHROPIC_API_KEY`
  - channel tokens for Telegram / Discord / Slack / WhatsApp workers
  - voice-specific vars: `PORT`, `PUBLIC_BASE_URL`, `TWILIO_*`, `ELEVENLABS_*`, `VOICE_WEBSOCKET_PATH`
- DroidRun:
  - config file at `~/.config/droidrun/config.yaml`
  - env file at `~/.config/droidrun/.env`
  - provider keys such as `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `DEEPSEEK_API_KEY`
  - workspace-specific fallbacks: `DROIDRUN_DEEPSEEK_KEY`, `DROIDRUN_OPENROUTER_KEY`

## Databases / Storage / Auth / Background Work

- AI-PM documents a local OpenMemory SQLite store at `~/.openclaw/data/openmemory-cursor.sqlite3`.
- OpenClaw integration docs mention Firestore and Mem0 as MCP-mediated integration targets, but the setup is not fully contained in this repo export.
- DroidRun does not show a central application database in the inspected paths; persistence is mostly config files, trajectories, and optional tracing backends.
- Authentication is largely environment-driven: Bitwarden-based secret injection, LLM provider API keys, gateway token, and channel-specific bot tokens.
- No Redis/Kafka-style queue was obvious in the inspected first-pass paths; background behavior appears to be worker/bot processes, watchdogs, and external services.

## Expected Startup Order

1. `AI-Project-Manager` (read-only / operational context)
   - No mandatory runtime to boot for app logic.
   - Optionally start the local OpenMemory compatibility server if reproducing the exact Cursor MCP environment.
2. `droidrun`
   - Ensure the `src/` submodule snapshot is present.
   - Create the repo-root virtualenv, install the package from `src/`, connect ADB to the target phone, and confirm Portal connectivity.
   - Start `mcp_server.py` if OpenClaw needs live phone tools.
3. `open--claw`
   - Start the external OpenClaw gateway/dashboard and required workers.
   - Start optional services like the voice front desk only if that path is being debugged.

In practical debugging, `open--claw` depends on `droidrun` being reachable if phone automation is in scope. `AI-Project-Manager` is mostly documentation/orchestration context and does not block runtime startup.

## Likely Debug Entry Points

- `AI-Project-Manager/docs/tooling/MCP_CANONICAL_CONFIG.md`
- `AI-Project-Manager/docs/release/system-architecture.md`
- `AI-Project-Manager/scripts/openmemory_cursor_server.py`
- `open--claw/open-claw/docs/MODULES.md`
- `open--claw/open-claw/docs/INTEGRATIONS.md`
- `open--claw/open-claw/services/voice-front-desk-agent/src/index.mjs`
- `open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/*/openclaw-runner.js`
- `droidrun/docs/PROJECT_INTELLIGENCE_INDEX.md`
- `droidrun/docs/entry-points-and-boot-sequence.md`
- `droidrun/mcp_server.py`
- `droidrun/src/pyproject.toml`

## Missing Dependencies / Broken References Noticed During Packaging

- `droidrun/src` is a git submodule snapshot. If that directory is missing or stale in another clone, the repo-root PowerShell and MCP tooling will not work as documented.
- `open--claw` does not provide one repo-root install/run command. Runtime code is spread across subpackages, and many worker wrappers expect a globally installed `openclaw` CLI outside this repo.
- The canonical multi-root workspace file originally lives outside the repos at `C:\Users\ynotf\.openclaw\openclaw.code-workspace`. A copy is included in this handoff root for context only.
- Machine-local secret injection, `%USERPROFILE%\.cursor\mcp.json`, Bitwarden setup, WSL gateway services, and the Android phone are all outside the exported repos, so some startup paths remain documentation-driven rather than self-contained.
- Image-heavy README assets were intentionally excluded to keep the export compact; some rendered markdown references will therefore point to missing media, but code/debug understanding should still be intact.
