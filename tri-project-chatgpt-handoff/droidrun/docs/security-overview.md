# Security Overview

DroidRun v0.5.1 — Security Model and Trust Boundaries

---

## 1. Authentication Model

DroidRun uses **ADB trust** as its primary authentication primitive. There is no HTTP-level authentication on the Portal server, and no authentication on the MCP server.

| Component | Auth Mechanism | Notes |
|---|---|---|
| ADB (USB) | USB pairing trust | One-time device authorization stored on device |
| ADB (wireless) | Wireless pairing (adb pair) | Uses pairing code + certificate exchange |
| Portal HTTP (port 8080) | **None** | Security delegated entirely to ADB port forwarding |
| MCP server | **None** | Trusts the spawning AI client process |
| Tailscale VPN | WireGuard + identity-based ACLs | Prevents unauthenticated access to the ADB port |

The Portal APK deliberately omits HTTP authentication because it is only reachable via `adb forward`, which itself requires an authenticated ADB session. Removing HTTP auth simplifies the Portal while keeping the security perimeter at ADB pairing.

---

## 2. Trust Boundaries

```
Internet
   │  (not exposed — Tailscale private mesh)
   ▼
Tailscale VPN (100.71.228.18:5555)
   │  Trust: Tailscale node enrollment + WireGuard encryption
   ▼
ADB daemon on device
   │  Trust: USB/wireless pairing certificate
   ▼
adb forward tcp:8080 tcp:8080
   │  Trust: ADB session must be active
   ▼
Portal HTTP (localhost:8080 only)
   │  Trust: process-level (loopback only)
   ▼
Portal APK (com.droidrun.portal)
   │  Trust: Android Accessibility Service grant (user-approved)
   ▼
Device UI tree + input injection
```

**MCP server trust boundary:**

```
AI client process (Cursor / OpenClaw / Claude Desktop)
   │  spawns via stdio
   ▼
mcp_server.py process
   │  trusts parent process implicitly (stdio pipe)
   ▼
DroidRun agent/CLI
```

The MCP server inherits the identity of the AI client that spawned it. Anyone who can send stdin to the MCP server process can invoke DroidRun tools.

---

## 3. Defense in Depth

Three layers protect the device from unauthorized access:

1. **Tailscale VPN** — The ADB port (5555) is only reachable via Tailscale private mesh. It is not exposed to the public internet. Enrollment requires Tailscale account credentials.
2. **ADB trust** — Even if the Tailscale network is compromised, ADB pairing is required. The device must explicitly authorize the host's ADB key.
3. **Port-forward-on-demand** — Portal HTTP is only accessible after `adb forward tcp:8080 tcp:8080` is run by an authenticated ADB session. There is no persistent listener on the network interface.

---

## 4. Least Privilege

| Component | Privilege Level | Notes |
|---|---|---|
| Portal APK | Android user process | No root, no shell exec, Accessibility Service only |
| DroidRun CLI | Windows user context | No elevated process, inherits user env vars |
| MCP server | Windows user context | Same as CLI |
| safe_execution sandbox | Restricted Python | Blocks os, sys, subprocess, shutil, pathlib, open, exec, eval, compile, importlib, __import__ |
| ADB commands | ADB shell | Not root by default (device-dependent) |

The Portal APK does not have shell access or root privileges. It interacts with the device exclusively through the Accessibility Service API, which is a standard Android framework with defined scope.

The `safe_execution` sandbox (when enabled) restricts agent-generated code to prevent file system access, process spawning, or dynamic code loading.

---

## 5. Sensitive Data Handling

| Data | Storage Location | Encrypted at Rest | Notes |
|---|---|---|---|
| API keys (DeepSeek, OpenRouter) | Windows HKCU\Environment | OS user profile isolation | Not written to files |
| API keys (Google, etc.) | ~/.config/droidrun/.env | **No** | Plaintext, chmod-restricted |
| credentials.yaml (app passwords) | ~/.config/droidrun/ | **Unknown — Needs Verification** | May be plaintext |
| Trajectory files | Local disk (trajectories/) | **No** | May contain sensitive screen content |
| Bitwarden token | Bitwarden Secrets Manager | Yes (Bitwarden cloud) | Machine account token |
| LLM prompts (Langfuse) | Langfuse cloud (if enabled) | Langfuse-managed | Includes UI screen text |

API keys are stored in Windows user environment variables and loaded at process startup. They are not written to trajectory files or logs (verified by code inspection). The `.env` file at `~/.config/droidrun/.env` is plaintext on disk.

---

## 6. Client-Side Protections

| Protection | Implementation | Default State |
|---|---|---|
| safe_execution sandbox | `agent.fast_agent.safe_execution` / `agent.scripter.safe_execution` | **Disabled** |
| max_steps limit | `agent.fast_agent.max_steps` | 15 steps |
| Action whitelist | Hardcoded action set in AndroidDriver | Always active |
| Telemetry opt-out | `telemetry.enabled: false` | Enabled (anonymous) |
| Vision mode | `--vision` flag / config | Optional |

The action whitelist restricts agents to: `click`, `type`, `swipe`, `press_key`, `open_app`, `wait`, `screenshot`, `complete`, `remember`. Arbitrary shell commands are not in the action set.

**Gap:** `safe_execution` is disabled by default. CodeAct and Scripter agents can execute arbitrary Python unless explicitly enabled.

---

## 7. Server/API Dependency Assumptions

When DroidRun sends requests to LLM APIs, it includes:
- Task goal (user-provided prompt)
- Current UI tree as text (from Accessibility Service)
- Screenshot images (vision mode only)

**What the LLM provider receives:**
- Potentially sensitive on-screen content from the device (banking apps, messages, etc.)
- Task descriptions which may reference the device owner's workflow

The LLM provider (DeepSeek, OpenRouter, Google) is treated as a **trusted third party** for the duration of the task. Users should be aware that UI content — including notification text, form data, or visible documents — may be transmitted to these APIs.

If `langfuse_screenshots: true` is set in the Langfuse config, full screenshots are uploaded to Langfuse cloud in addition to text.

---

## Summary Risk Table

| Threat | Likelihood | Impact | Primary Mitigation |
|---|---|---|---|
| Unauthorized Portal access | Low | High | ADB forward + Tailscale |
| API key leakage | Low | High | Env vars, not files |
| Sensitive screen data in LLM calls | Medium | Medium | Unavoidable by design; inform user |
| Prompt injection via device UI | Medium | Medium | max_steps, goal anchoring |
| Agent executing unsafe code | Medium (if CodeAct) | High | safe_execution (disabled by default) |
| Trajectory file disclosure | Low | Medium | Local only, no auto-share |

See `docs/threat-model.md` for full threat analysis.
