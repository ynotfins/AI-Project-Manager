# Secrets Handling

This document covers where secrets live, how they are injected, what must never be hardcoded, and how to rotate them.

> **Hard rule:** No secret values ever appear in source code, config files committed to git, or documentation. This file contains only secret **names** and **locations** — never values.

---

## Secret Names (Reference Only)

| Secret name | Purpose | Provider |
|---|---|---|
| `OPENAI_API_KEY` | OpenAI / OpenAI-compatible models | OpenAI |
| `GOOGLE_API_KEY` | Google Gemini models | Google AI Studio |
| `ANTHROPIC_API_KEY` | Claude models | Anthropic |
| `DEEPSEEK_API_KEY` | DeepSeek models | DeepSeek |
| `DROIDRUN_DEEPSEEK_KEY` | Workspace alias for DeepSeek key | — |
| `DROIDRUN_OPENROUTER_KEY` | Workspace alias for OpenRouter key | — |
| `LANGFUSE_SECRET_KEY` | Langfuse cloud tracing (server key) | Langfuse |
| `LANGFUSE_PUBLIC_KEY` | Langfuse cloud tracing (public key) | Langfuse |
| `BWS_ACCESS_TOKEN` | Bitwarden Secrets Manager machine account token | Bitwarden |

---

## Where Secrets Are Stored

### 1. Bitwarden Secrets Manager (canonical, recommended)

Machine account: `droidrun-windows`

Secret IDs (safe to record — these are identifiers, not values):
- DeepSeek key: `14d69c11-...` (truncated for safety)
- OpenRouter key: `f9ed80a7-...` (truncated for safety)

The **BWS machine account access token** is stored in the regular Bitwarden vault (not Secrets Manager), under the entry `BWS_DROIDRUN_TOKEN`. This token bootstraps access to all other secrets.

### 2. Windows Registry — `HKCU\Environment`

`DROIDRUN_DEEPSEEK_KEY` and `DROIDRUN_OPENROUTER_KEY` are written here by `startup_droidrun.ps1` after being fetched from Bitwarden. These persist across shell sessions for the current Windows user.

**Risk:** Environment variables in `HKCU\Environment` are readable by all processes running as the current user. Do not store on shared machines.

### 3. `~/.config/droidrun/.env`

Google, OpenAI, and other keys may live here for persistent local dev use. This path is gitignored.

```
GOOGLE_API_KEY=...
OPENAI_API_KEY=...
```

**Risk:** If the home directory is synced (OneDrive, etc.), this file may be inadvertently uploaded. Verify sync exclusions.

### 4. `functions/.env.local` (if Firebase functions present)

Not applicable to pure Python DroidRun usage, but if the workspace includes Firebase functions: `.env.local` is the source of truth; `.env` is generated before deploy and never manually edited.

---

## Injection Flow (Workspace)

```
Bitwarden vault
  └─ BWS_DROIDRUN_TOKEN (regular vault entry)
       │
       ▼
startup_droidrun.ps1
  └─ bws run / bws secret get
       │
       ├─ SetEnvironmentVariable("DROIDRUN_DEEPSEEK_KEY", ..., "User")  → HKCU\Environment
       ├─ SetEnvironmentVariable("DROIDRUN_OPENROUTER_KEY", ..., "User") → HKCU\Environment
       └─ $env:DROIDRUN_DEEPSEEK_KEY = ...   (current process)
            │
            ▼
       DroidRun CLI reads env vars via python-dotenv + os.environ
```

### Alternative: direct `.env` file

```
~/.config/droidrun/.env
  └─ loaded by DroidRun at startup via python-dotenv
```

### Alternative: one-time script

```powershell
# Set env vars interactively without Bitwarden (local dev only)
.\scripts\store_api_keys_to_env.ps1
```

---

## What Must Never Be Hardcoded

- API keys of any kind
- Bitwarden machine account tokens
- Device credentials (ADB passwords, if any)
- Langfuse secret keys
- Any value from the secret names table above

If you find a hardcoded secret: remove it immediately, rotate the secret, and audit git history.

---

## Local Dev Setup

**Option A (recommended): Bitwarden Secrets Manager**

1. Obtain `BWS_DROIDRUN_TOKEN` from the Bitwarden vault entry `BWS_DROIDRUN_TOKEN`.
2. Set it in your shell: `$env:BWS_ACCESS_TOKEN = "<token>"`
3. Run: `.\startup_droidrun.ps1`
4. Keys are now in your environment and Windows registry.

**Option B: Manual `.env` file**

1. Create `~/.config/droidrun/.env`
2. Add `KEY_NAME=value` lines for each key you need.
3. DroidRun loads this file at startup automatically.

**Option C: One-time script**

```powershell
.\scripts\store_api_keys_to_env.ps1
```

Prompts for key values and writes them to `HKCU\Environment`.

---

## CI/CD Secret Handling

> **Unknown / Needs Verification** — No CI/CD pipeline is currently configured. When one is added, secrets should be injected via the CI platform's secrets store (GitHub Actions Secrets, Azure Key Vault, etc.) — never via committed files.

---

## Secret Rotation

### Rotating an API key

1. Generate new key at the provider's dashboard.
2. Update the value in Bitwarden Secrets Manager (for the relevant secret ID).
3. Re-run `startup_droidrun.ps1` to pull the new value.
4. Verify DroidRun can connect with the new key.

### Rotating the BWS machine account token

1. Generate a new access token for the `droidrun-windows` machine account in Bitwarden Secrets Manager.
2. Update the `BWS_DROIDRUN_TOKEN` entry in the **regular Bitwarden vault**.
3. On any host using this workspace: set `$env:BWS_ACCESS_TOKEN = "<new token>"` and re-run `startup_droidrun.ps1`.

---

## Risk Summary

| Risk | Severity | Mitigation |
|---|---|---|
| `.env` file accidentally committed | High | `.gitignore` must include `*.env`, `.env*` — verify periodically |
| Windows `HKCU\Environment` readable by all user processes | Medium | Acceptable on single-user dev machines; avoid on shared hosts |
| Trajectory files containing screen content | Medium | `trajectories/` is gitignored; avoid storing sensitive data on-screen during recording |
| `credentials.yaml` (app passwords) | High | Never commit; store outside repo or gitignore explicitly |
| bws token expiry | Low | Bitwarden machine account tokens have configurable TTL; monitor expiry |

---

## Related Files

- `docs/logging-observability.md` — Langfuse key usage, telemetry
- `docs/troubleshooting-playbook.md` — API key not found errors
- `scripts/startup_droidrun.ps1` — secret injection entry point
- `scripts/store_api_keys_to_env.ps1` — one-time manual key setup
