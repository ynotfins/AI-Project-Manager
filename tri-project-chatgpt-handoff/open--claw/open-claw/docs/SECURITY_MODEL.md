# OpenClaw — Security Model

## Trust Boundary

OpenClaw enforces a clear trust boundary: the Gateway runs on your infrastructure,
binds to loopback by default, and all external access requires authentication.
The model provides intelligence; OpenClaw provides the security perimeter.

## Authentication

| Mode | When to Use |
|------|-------------|
| `token` | Recommended for any non-loopback bind. Token set via config or `openclaw doctor --generate-gateway-token` |
| `password` | Alternative to token. Set via `OPENCLAW_GATEWAY_PASSWORD` |
| `trusted-proxy` | Behind a reverse proxy that sets `x-forwarded-user` header |
| Tailscale | `gateway.tailscale.mode: serve/funnel` for private network access |

Rate limiting on auth: 10 attempts / 60s window, 5-minute lockout (loopback exempt).

## Gateway Network Security

- **Default bind**: `127.0.0.1` (loopback only) — no remote access without explicit config
- **Port**: `18789` (configurable)
- **Protocol**: WebSocket with JSON Schema validation (TypeBox). Malformed frames rejected immediately
- **Idempotency**: all side-effecting operations require idempotency keys

## Channel Access Control

| Layer | Mechanism |
|-------|-----------|
| DM policy | `pairing` (explicit approval), `allowlist`, `open`, `disabled` |
| Allowlists | Per-channel phone numbers / usernames |
| Group policy | `requireMention`, group-specific allowlists |
| Command gating | Channel-level command restrictions |

Default for WhatsApp DMs: `pairing` mode — requires explicit approval before processing messages from unknown senders.

## Docker Sandboxing

Optional but recommended for untrusted sessions.

| Setting | Options |
|---------|---------|
| `sandbox.mode` | `all`, `non-main` (default for safety), `off` |
| `sandbox.scope` | `session` (default), `agent`, `shared` |
| `sandbox.workspaceAccess` | `none` (default), `ro`, `rw` |

Sandboxed: tool execution (exec, read, write, edit, apply_patch, process).
Not sandboxed: Gateway process, elevated exec, explicitly host-allowed tools.

## Tool Policy

Three layers of control:

1. **Tool profiles**: `minimal`, `coding`, `messaging`, `full` — base allowlists
2. **Allow/deny lists**: `tools.allow`, `tools.deny` (deny always wins)
3. **Sandbox tool policy**: separate allow/deny when sandboxed

Tool groups (shorthands): `group:fs`, `group:browser`, etc.

`/exec` command changes session defaults for authorized senders but cannot override a denied tool.

## Secret Scanning

- `.detect-secrets.cfg` and `.secrets.baseline` in vendor repo
- Pre-commit hooks scan for secrets before commits
- `.env.example` provides key templates — never commit real values

## Credential Policy (Open Claw Project)

- `functions/.env.local` is source of truth for real credentials (if applicable)
- `.env*` files are in `.gitignore`
- No secrets in code or git — ever
- API keys referenced by environment variable name only in config docs
- Service account JSON files never committed

## Formal Verification

TLA+/TLC models maintained in [openclaw-formal-models](https://github.com/vignesh07/openclaw-formal-models):

| Property | Status |
|----------|--------|
| Gateway exposure (loopback + auth) | Verified |
| `nodes.run` pipeline (allowlist + approval) | Verified |
| Approval token replay prevention | Verified |
| Pairing store (TTL + caps) | Verified |
| Ingress gating (mention + command bypass) | Verified |

These are bounded model checks, not full implementation proofs.

## Audit Logging

`src/security/audit*.ts` provides:
- Channel-level audit events
- Filesystem access audit
- Tool policy enforcement audit
- Async and sync audit pipelines
