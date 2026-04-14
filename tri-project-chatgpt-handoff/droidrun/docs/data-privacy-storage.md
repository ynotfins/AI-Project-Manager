# Data Privacy and Storage

DroidRun v0.5.1 — What is stored, where, and what it contains.

---

## 1. Data Categories and Contents

### Config YAML (`~/.config/droidrun/config.yaml`)

- **Contains:** Device settings, model names, agent parameters, feature flags
- **PII:** None
- **Sensitive:** No (contains no secrets, only references to model names)
- **Format:** YAML plaintext

---

### Environment File (`~/.config/droidrun/.env`)

- **Contains:** API keys for LLM providers (GOOGLE_API_KEY, etc.)
- **PII:** None (API keys are service credentials, not personal data)
- **Sensitive:** **Yes** — API keys grant access to billed LLM services
- **Format:** Plaintext key=value
- **Protection:** File system permissions only (no encryption at rest)

---

### Trajectory Files (`trajectories/`)

- **Contains:** Step-by-step records of agent execution including:
  - Task goal
  - Observed UI state (accessibility tree text from device)
  - LLM reasoning and action decisions
  - Action results
  - Optionally: screenshots of device screen
- **PII:** **Potentially yes** — UI content may include names, messages, email addresses, account balances, or any other data visible on the device screen during task execution
- **Sensitive:** **Yes** — contents reflect what was on the device screen
- **Format:** JSON (exact schema needs verification)
- **Encryption:** None (plaintext on disk)
- **Location:** `trajectories/` relative to working directory (not in config dir)

---

### Credentials File (`~/.config/droidrun/credentials.yaml`)

- **Contains:** App usernames and passwords if `credentials.enabled: true` is set in config
- **PII:** **Yes** — usernames may be email addresses
- **Sensitive:** **Yes** — contains app passwords in plaintext (encryption status unverified)
- **Format:** YAML
- **Encryption:** **Unknown — Needs Verification**

---

### Windows Registry (`HKCU\Environment`)

- **Contains:** DROIDRUN_DEEPSEEK_KEY, DROIDRUN_OPENROUTER_KEY
- **PII:** None
- **Sensitive:** Yes — LLM API keys
- **Scope:** Current Windows user only
- **Encryption:** OS user profile isolation (not encrypted)

---

### PostHog Telemetry (Cloud)

- **Contains:** Anonymous usage events:
  - CLI invocations and command used
  - Model provider used (not the key)
  - Task success or failure boolean
  - DroidRun version
  - Platform (OS)
  - Anonymous distinct_id (UUID, not linked to identity)
- **PII:** None (by design — no task content, no screen content, no device identifiers)
- **Opt-out:** Set `telemetry.enabled: false` in `~/.config/droidrun/config.yaml`
- **Retention:** Per PostHog's data retention policy

---

### Langfuse Traces (Cloud, Optional)

- **Contains:** Full LLM traces when `[langfuse]` is configured, including:
  - Complete prompts sent to LLM (which include device UI tree text)
  - LLM responses and reasoning
  - Screenshots of device screen (if `langfuse_screenshots: true`)
  - Token counts and latency
- **PII:** **Potentially yes** — device UI content is included in prompts
- **Sensitive:** **Yes** — may contain on-screen text from any app
- **Opt-in:** Langfuse is disabled unless credentials are configured
- **Retention:** Per Langfuse account's data retention settings

---

## 2. Storage Locations Summary

| Data | Location | Type | Encrypted |
|---|---|---|---|
| Config | `~/.config/droidrun/config.yaml` | Local disk | No |
| API keys (.env) | `~/.config/droidrun/.env` | Local disk | No |
| Trajectory files | `trajectories/` (cwd) | Local disk | No |
| Credentials | `~/.config/droidrun/credentials.yaml` | Local disk | Unknown |
| API keys (registry) | `HKCU\Environment` | Windows registry | No (OS-scoped) |
| Bitwarden token | Bitwarden Secrets Manager | Cloud (Bitwarden) | Yes |
| Anonymous events | PostHog cloud | Cloud (PostHog) | Bitwarden-managed |
| LLM traces | Langfuse cloud | Cloud (Langfuse) | Langfuse-managed |

---

## 3. Data Retention

| Data | Retention | Deletion Method |
|---|---|---|
| Config YAML | Indefinite (until manually deleted) | `rm ~/.config/droidrun/config.yaml` |
| .env file | Indefinite (until manually deleted) | `rm ~/.config/droidrun/.env` |
| Trajectory files | **Indefinite — accumulates without bound** | Manual: `rm -rf trajectories/` |
| Credentials YAML | Indefinite (until manually deleted) | `rm ~/.config/droidrun/credentials.yaml` |
| Windows registry | Indefinite | `[Environment]::SetEnvironmentVariable("KEY", $null, "User")` |
| PostHog events | Per PostHog retention policy (default: 1 year) | PostHog project settings |
| Langfuse traces | Per Langfuse account settings | Langfuse dashboard |

**Warning:** The `trajectories/` directory has no automated cleanup. Every task run appends new files. On long-running deployments this directory will grow unboundedly.

---

## 4. Sensitive Data Handling Practices

| Concern | Practice | Gap |
|---|---|---|
| API keys in logs | Not logged (verified by code review) | Verify custom logging doesn't capture env vars |
| API keys in trajectories | Not written (they are not part of UI state) | Confirm for all trajectory serialization paths |
| Screenshots in Langfuse | Opt-in via `langfuse_screenshots: true` | Default is off; explicit user action required |
| Credentials in memory | Loaded at task start, not written to trajectory | Verify credential substitution doesn't appear in LLM prompts |
| Device screen content in LLM | Sent as part of UI tree and screenshots | By design; inform users before enabling vision mode |

---

## 5. Deletion Behavior

There is **no automated deletion** in DroidRun. Data accumulates until the user manually removes it.

To fully remove all local DroidRun data:

```powershell
# Remove config directory (includes .env, config.yaml, credentials.yaml)
Remove-Item -Recurse -Force ~/.config/droidrun/

# Remove trajectory files
Remove-Item -Recurse -Force ./trajectories/

# Remove Windows registry API keys
[Environment]::SetEnvironmentVariable("DROIDRUN_DEEPSEEK_KEY", $null, "User")
[Environment]::SetEnvironmentVariable("DROIDRUN_OPENROUTER_KEY", $null, "User")

# Revoke ADB authorization on device
# Settings → Developer options → Revoke USB debugging authorizations
```

Bitwarden machine account tokens must be revoked via the Bitwarden Secrets Manager console.
PostHog and Langfuse data must be deleted via their respective dashboards.

---

## 6. Privacy Risk Assessment

| Risk | Likelihood | Notes |
|---|---|---|
| Sensitive on-screen data in trajectories | **High** | Every task run creates a trajectory; device may show sensitive apps |
| Sensitive on-screen data in Langfuse | **Medium** (if enabled) | Langfuse is opt-in; screenshots require explicit config |
| API key exposure from .env file | Low | Requires filesystem access as current user |
| API key exposure from registry | Low | Requires registry access as current user |
| Credential file exposure | Low-Medium | Depends on whether encryption is implemented |

**Primary privacy concern:** Trajectory files capture everything visible on the device screen during task execution. If the phone is used for personal apps (messages, banking, email), those contents may appear in trajectory JSON files stored on the development machine.

**Recommendation:** Either delete trajectory files after reviewing, or exclude sensitive apps from automation tasks.
