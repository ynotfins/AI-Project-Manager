# OpenClaw — Architecture Map

## Overview

OpenClaw follows a **hub-and-spoke** architecture with a single **Gateway** at the center.
The Gateway is a WebSocket server acting as the control plane, sitting between all
user-facing interfaces (messaging apps, CLI, web dashboard, mobile apps) and the
**Agent Runtime** where reasoning and execution happen.

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  WhatsApp    │   │  Telegram   │   │  Discord     │
│  (Baileys)   │   │  (Bot API)  │   │  (Bot Token) │
└──────┬───────┘   └──────┬──────┘   └──────┬───────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                ┌─────────▼─────────┐
                │     Gateway       │
                │  (WebSocket :18789)│
                │  auth · routing   │
                │  sessions · health│
                └─────────┬─────────┘
                          │
                ┌─────────▼─────────┐
                │   Agent Runtime   │
                │  Pi Agent Core    │
                │  model · tools    │
                │  memory · sandbox │
                └───────────────────┘
```

## Repo Structure (`vendor/openclaw/`)

| Directory | Purpose |
|-----------|---------|
| `openclaw.mjs` | CLI entrypoint → loads `dist/entry.js` (Node.js 22+) |
| `src/gateway/` | WebSocket server, auth, rate limiting, boot, health monitor |
| `src/agents/` | Agent runtime, auth profiles, model routing, patch application |
| `src/channels/` | Channel abstraction: allowlists, gating, sessions, typing |
| `src/security/` | Audit logging, tool policy, DM policy, secret scanning |
| `src/config/` | Config resolution, agent dirs, channel capabilities, commands |
| `src/memory/` | Embedding backends, batch processing, vector search |
| `src/plugins/` | Plugin loader, SDK, extension API |
| `src/providers/` | LLM provider adapters (Anthropic, OpenAI, Gemini, etc.) |
| `src/cli/` | Commander.js CLI: start, config, pair, diagnose |
| `src/hooks/` | Lifecycle hooks for extensibility |
| `src/sessions/` | Session management, spawn, history, cross-session tools |
| `src/cron/` | Scheduled actions and heartbeat |
| `extensions/` | 38 channel/memory/auth plugins (auto-discovered) |
| `skills/` | 52 skill directories (SKILL.md frontmatter, hot-loadable) |
| `packages/` | Sub-packages: `clawdbot`, `moltbot` (legacy names) |
| `ui/` | Lit-based web components for Control UI |
| `apps/` | Mobile apps (iOS, Android WebSocket clients) |
| `.pi/` | Pi agent config: prompts, extensions, git settings |

## Gateway Details

- **Transport**: WebSocket (`ws` library), default `127.0.0.1:18789`
- **Auth modes**: token, password, trusted-proxy (Tailscale support)
- **Design**: idempotency keys required, event-driven (not poll-based), typed protocol (TypeBox JSON Schema)
- **Constraint**: one Gateway per host (WhatsApp single-device protocol)
- **Control UI**: Lit web components served at `/openclaw` from the Gateway process

## Agent Runtime

- **Core**: `src/agents/piembeddedrunner.ts` — Pi Agent Core, RPC streaming
- **Cycle**: resolve session → assemble context → stream model response + tool calls → persist state
- **Sessions**: per-channel-peer DM, per-group, per-agent scoping
- **Multi-agent**: different channels/groups can route to isolated agent instances with separate workspaces and models
- **Cross-session**: `sessions_spawn`, `sessions_history`, `sessions_send`, `sessions_list`

## Channel Adapters

Each adapter implements: authentication, inbound parsing, access control, outbound formatting.

| Channel | Auth Method | Built-in? |
|---------|-------------|-----------|
| WhatsApp | QR code (Baileys) | Yes |
| Telegram | Bot token | Yes |
| Discord | Bot token | Yes |
| Slack | Bot + App tokens | Yes |
| iMessage | macOS native | Yes |
| Signal | Via extension | Extension |
| Teams | Via extension | Extension |
| Line | Via extension | Extension |
| Matrix | Via extension | Extension |
| IRC | Via extension | Extension |

## Skills & Extensions

**Skills** (`skills/`): YAML frontmatter in `SKILL.md`, auto-discovered, hot-loadable.
Custom skills go in `~/.openclaw/workspace/skills/`.

**Extensions** (`extensions/`): four extension points:
1. **Provider plugins** — custom/self-hosted LLM providers
2. **Tool plugins** — custom capabilities
3. **Memory plugins** — alternative storage backends (vector stores, knowledge graphs)
4. **Channel plugins** — new messaging platforms

## Config Model

- **Primary config**: `~/.openclaw/openclaw.json` (JSON5)
- **Env vars**: `.env` → `~/.openclaw/.env` → process env (precedence: process > local > home)
- **Key sections**: `gateway`, `agents`, `channels`, `session`, `tools`, `skills`

## Module Mapping to Open Claw

| Open Claw Module | OpenClaw Vendor Mapping |
|------------------|------------------------|
| orchestrator | `src/gateway/` + `src/agents/` (routing, session, agent selection) |
| memory | `src/memory/` + `extensions/memory-*` |
| dev | `src/plugins/` + `skills/coding-agent` |
| comms | Channel adapters + `extensions/` (Slack, Discord, Telegram, etc.) |
| web | `src/browser/` + `skills/` (browser-based skills) |
