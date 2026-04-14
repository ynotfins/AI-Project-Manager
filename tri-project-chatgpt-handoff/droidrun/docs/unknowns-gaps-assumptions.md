# Unknowns, Gaps, and Assumptions

DroidRun v0.5.1 — Explicit inventory of what is uncertain, unverified, or assumed.

This file exists to prevent future work from being built on incorrect foundations. Every item here should be resolved by investigation or testing, not by assumption.

---

## 1. Missing Documentation (Not in This Workspace or Upstream)

| Missing Document | Why It Matters |
|---|---|
| Portal APK HTTP API reference | Every AndroidDriver action translates to a Portal endpoint. Without this, the client–APK contract is implicit and fragile. |
| Action parameter reference | The complete set of actions (click, type, swipe, etc.) with their exact parameters and constraints is not formally documented. |
| Jinja2 prompt library | What prompts exist in `config/prompts/`? Are they all overridable? What variables does each template expect? |
| Macro file format | Recorded macros are referenced in the CLI but the file format (JSON? YAML?) is undocumented. |
| Trajectory JSON schema | Trajectory files contain step-by-step agent execution records. The schema is not documented, making it hard to parse or analyze recordings. |
| Upstream release changelog | The upstream repo is github.com/droidrun/droidrun. There is no record of which upstream commits or releases this workspace fork tracks. |
| Credential manager internals | Whether `credentials.yaml` is encrypted, what format it uses, and how credentials are looked up during a task is not documented. |
| MCP tool parameter schemas | What parameters does each MCP tool accept? The schema in `mcp_server.py` defines them but no human-readable reference exists. |

---

## 2. Unclear Wiring

### mobilerun-sdk

- **What is it?** An SDK included as a dependency.
- **What does it do?** Unknown. Not referenced in primary documentation.
- **What network calls does it make?** Unverified. May connect to an external service.
- **Is it required?** Unclear. Removing it may break Portal functionality or may have no effect.
- **Action needed:** Read `mobilerun-sdk` source or PyPI page; trace all import paths in Portal APK.

### app_cards Server Mode

- **What triggers it?** The CLI appears to have a server mode related to "app cards."
- **What does it do?** Unclear — possibly serves a web UI displaying installed apps.
- **Is it deployed?** Not mentioned in the startup chain.
- **Action needed:** Inspect `src/droidrun/cli/main.py` for server mode commands.

### StatelessManagerAgent vs DroidAgent

- **DroidAgent** is the primary agent used by `droidrun run`.
- **StatelessManagerAgent** appears in the codebase with a different architecture (Manager + Executor split, `reasoning=True` mode).
- **When is it used?** Not clear from CLI documentation which mode uses the manager/executor split.
- **How does `reasoning=True` activate it?** The config key `reasoning` is referenced but its effect on agent class selection is not documented.
- **Action needed:** Trace `reasoning` config key through agent initialization to identify the branching point.

---

## 3. Guessed Areas (Not Verified)

| Area | Assumption Made | Confidence | How to Verify |
|---|---|---|---|
| iOS driver status | Described as "experimental stub" — assumes minimal or no functionality | Medium | Run `droidrun devices` with an iOS device connected; inspect `ios.py` for NotImplementedError |
| Stealth driver | Assumes it wraps AndroidDriver with behavioral modifications to avoid detection | Low | Read `stealth.py`; test on a device with anti-automation detection |
| Cloud driver auth | Assumes it uses API key or OAuth for a remote execution service | Very Low | Read `cloud.py`; find referenced cloud service |
| `credentials.yaml` encryption | Assumes plaintext (no encryption evidence found) | Medium | Search for encryption/decryption calls in config_manager.py |
| Portal APK source | Assumes Portal APK is pre-built; no build process found in workspace | High | Check if Portal source repo is linked or if APK is binary-only |
| `app_cards` output format | Assumes JSON response based on REST API conventions | Low | Inspect portal_client.py for app_cards calls |

---

## 4. Architecture Risks

### Pinned llama-index==0.14.4

- **Risk:** Locks the entire agent orchestration framework to a specific version.
- **Failure mode:** `pip install --upgrade` (by a new developer or CI) breaks the agent loop silently.
- **No CI to catch breakage.**
- **Upstream divergence risk:** Upstream droidrun may have already upgraded; syncing upstream commits could pull a different llama-index version.

### No CI/CD or Test Suite

- **Risk:** No automated verification that changes don't break existing behavior.
- **Failure mode:** Any code change may silently break device connection, agent loop, or MCP integration.
- **Manual testing requires a physical device** (Samsung Galaxy S25 Ultra or equivalent).
- **Impact:** High for a project with hardware dependencies.

### Upstream Divergence

- **Risk:** This workspace is a fork of github.com/droidrun/droidrun. There is no documented process for merging upstream changes.
- **Failure mode:** Upstream bugfixes and features accumulate; merging after extended divergence becomes high-risk.
- **Action needed:** Establish a sync cadence and document it in `docs/upstream-sync-guide.md`.

### LlamaIndex Workflows API Fragility

- **Risk:** The LlamaIndex Workflows API has changed significantly between minor versions. The agent step definitions in `droid_agent.py` are tightly coupled to `0.14.4` API.
- **Failure mode:** Any version change breaks the agent loop in ways that may not surface as exceptions (silent behavioral changes).

---

## 5. Config Ambiguity

### Which Config File Wins?

DroidRun supports multiple config sources:
- `~/.config/droidrun/config.yaml`
- `~/.config/droidrun/.env`
- CLI flags (e.g., `--goal`, `--model`)
- Windows environment variables (HKCU\Environment)

The **precedence order** is not formally documented. Behavior when the same key appears in multiple sources is unknown.

**Action needed:** Read `config_manager.py` to trace the merge order explicitly.

### Migration Behavior

When the config schema changes between DroidRun versions (e.g., new keys added, old keys removed), there is no documented migration path. Old `config.yaml` files may:
- Silently ignore new required keys (use defaults)
- Fail to parse if syntax changes
- Behave incorrectly if defaults change

**No migration logic** has been observed in the codebase.

---

## 6. Modules Needing Deeper Audit

| Module | Why Audit Needed |
|---|---|
| `src/droidrun/telemetry/` | Exact events sent to PostHog are not inventoried. Verify no screen content or task descriptions are included in telemetry payloads. |
| `src/droidrun/tools/` (ToolRegistry) | The exact set of tools registered for each agent mode is not documented. Verify the action whitelist is enforced uniformly. |
| `credentials.yaml` handler | Verify whether credentials are encrypted at rest. Verify how they are injected into agent context. |
| `mobilerun-sdk` integration | Trace all imports and calls. Verify no unexpected network behavior. |
| Langfuse integration | Confirm what is included in traces when `langfuse_screenshots: false`. Verify no accidental credential inclusion. |
| `config_manager.py` merge logic | Trace exact precedence for all config sources. Document the winner for each conflict type. |

---

## 7. Workspace-Specific vs Framework Confusion

Several files in this workspace are **not part of upstream droidrun** and exist only in this local environment. Newcomers may confuse them with framework components.

| File | Status | Notes |
|---|---|---|
| `mcp_server.py` | **Workspace-only** | Not in upstream droidrun; bridges DroidRun to AI clients |
| `scripts/startup_droidrun.ps1` | **Workspace-only** | Bitwarden integration; not upstream |
| `scripts/start_mcp_server.ps1` | **Workspace-only** | MCP launch script; not upstream |
| `scripts/droidrun_run.ps1` | **Workspace-only** | Convenience script; not upstream |
| `docs/ai/` (entire folder) | **Workspace-only** | AI agent state tracking; not upstream |
| `openmemory.md` | **Workspace-only** | Memory index for AI agents; not upstream |
| `~/.config/droidrun/config.yaml` | **Local runtime** | Not in repo; generated per installation |

When evaluating whether a bug or behavior is an upstream issue vs workspace issue, check this list first.
