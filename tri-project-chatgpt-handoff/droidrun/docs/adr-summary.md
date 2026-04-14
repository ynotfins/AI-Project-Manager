# Architecture Decision Records — Summary

DroidRun v0.5.1 — Documented and inferred architectural decisions.

---

## Confirmed Decisions

These decisions are directly evident from the codebase and can be verified without documentation.

---

### ADR-001: LlamaIndex Workflows as Agent Orchestration

**Decision:** Use LlamaIndex Workflows (`llama-index-workflows`) as the orchestration framework for agent step execution, rather than a custom state machine or a direct LLM loop.

**Rationale (inferred):** LlamaIndex Workflows provides structured event-driven execution, step isolation, and built-in support for async operations. It aligns with the broader LlamaIndex ecosystem already used for LLM provider abstraction.

**Consequences:**
- Agent logic is tied to LlamaIndex Workflow API; upgrades require workflow step refactoring
- The `llama-index==0.14.4` pin is a direct consequence of this decision
- Debugging the agent requires understanding LlamaIndex Workflow execution model

**Status:** Active. Verified in `src/droidrun/agent/droid/droid_agent.py`.

---

### ADR-002: Portal APK as On-Device Interface

**Decision:** Deploy a companion APK (`com.droidrun.portal`) to the Android device rather than relying solely on ADB shell commands for UI interaction.

**Rationale:** ADB shell commands for UI automation (e.g., `adb shell input tap`) are unreliable, slow, and cannot read the UI accessibility tree efficiently. The Portal APK uses the Android Accessibility Service API, which provides structured UI element data and reliable input injection.

**Consequences:**
- Requires user to manually enable Accessibility Service (cannot be automated)
- APK version must be kept in sync with Python client expectations
- No-root required (Accessibility Service is a standard Android API)
- Portal APK must be installed and running for any task to execute

**Status:** Active. Core to the architecture.

---

### ADR-003: Content Provider + TCP Dual Transport in PortalClient

**Decision:** Implement two transport mechanisms in `PortalClient`: primary HTTP TCP (via `adb forward`) and fallback ADB content provider queries.

**Rationale:** TCP via `adb forward` is fast but requires explicit setup. The content provider fallback enables basic UI observation even when the forward is not configured, improving robustness for initial setup and diagnostics.

**Consequences:**
- More complex `PortalClient` implementation
- Fallback has reduced functionality (read-only observation, no actions)
- Users may not realize they are running in degraded mode (fallback is transparent)

**Status:** Active. Verified in `src/droidrun/tools/android/portal_client.py`.

---

### ADR-004: YAML Config with Dataclass Schema

**Decision:** Store DroidRun configuration in a YAML file backed by Python dataclasses, rather than using environment variables exclusively or a different config format.

**Rationale:** YAML is human-readable and supports nested configuration. Dataclasses provide type safety and IDE autocomplete for config access in code. Combined with `platformdirs` for location, this gives a user-friendly configuration experience.

**Consequences:**
- Config location is OS-dependent (`~/.config/droidrun/` on Linux/Mac, equivalent on Windows)
- Config schema changes require migration logic (currently absent)
- Both YAML and env vars are supported; precedence rules need documentation

**Status:** Active. Verified in `src/droidrun/config_manager/config_manager.py` and `src/droidrun/config_example.yaml`.

---

### ADR-005: FastAgent (XML Tool Calls) as Default, not CodeAct

**Decision:** Default agent mode is `FastAgent`, which uses structured XML tool call responses from the LLM, rather than `CodeAct`, which generates and executes Python code.

**Rationale:** XML tool calls are more predictable, easier to validate, and do not require a code execution sandbox. CodeAct is more powerful but introduces arbitrary code execution risk. The XML approach aligns with tool-calling patterns already established by the LLM provider APIs.

**Consequences:**
- Default mode is safer but less flexible
- CodeAct remains available for advanced use cases but is opt-in
- `safe_execution` sandbox is less critical for FastAgent (but critical for CodeAct/Scripter)

**Status:** Active. Default behavior verified via config and CLI defaults.

---

### ADR-006: Modular Driver Pattern (DeviceDriver Base Class)

**Decision:** Define a `DeviceDriver` abstract base class and implement concrete drivers: `AndroidDriver`, `iOSDriver`, `CloudDriver`, `StealthDriver`, `RecordingDriver`.

**Rationale:** Allows the agent core to be device-agnostic. Swapping the driver changes the device target without changing agent logic. Enables future expansion to iOS, cloud emulators, and specialized recording modes.

**Consequences:**
- iOS and Cloud drivers are not fully implemented (experimental/stub status)
- Interface contract is defined in the base class; any new driver must implement it
- Stealth and Recording drivers modify or wrap AndroidDriver behavior

**Status:** Active (Android driver). Others are experimental or stub.

---

### ADR-007: platformdirs for Config Location

**Decision:** Use the `platformdirs` library to determine the config directory path (`~/.config/droidrun/` on Linux, equivalent on Windows/macOS) rather than hardcoding a path.

**Rationale:** `platformdirs` follows OS conventions for user config directories. Hardcoded paths break cross-platform portability.

**Consequences:**
- Config location differs by OS (important for documentation)
- Users migrating between OSes will need to copy config manually

**Status:** Active.

---

### ADR-008: stdio JSON-RPC for MCP Server

**Decision:** Implement the MCP server using stdio-based JSON-RPC communication, not an HTTP server.

**Rationale:** The MCP specification defines stdio as the primary transport for locally-spawned servers. AI clients (Cursor, Claude Desktop) spawn MCP servers as child processes and communicate via stdin/stdout. This avoids port conflicts and authentication complexity.

**Consequences:**
- MCP server cannot be used over a network without additional tooling
- Each AI client spawns its own MCP server process (no sharing)
- No MCP server authentication (security delegated to process spawning)

**Status:** Active. Verified in `mcp_server.py` (workspace-specific file).

---

### ADR-009: Bitwarden Secrets Manager for API Keys (Workspace Decision)

**Decision:** Store API keys in Bitwarden Secrets Manager (machine account) rather than in `.env` files on disk. Keys are loaded at session start via `bws` CLI.

**Rationale (workspace-specific):** Keeps secrets out of disk files and git history. Allows rotation without modifying files. Consistent with broader workspace security policy.

**Consequences:**
- DroidRun cannot start without Bitwarden availability
- Startup requires `bws` CLI to be installed and the machine token to be valid
- Adds a cloud dependency to an otherwise local tool
- Upstream DroidRun does not use Bitwarden; this is a workspace-layer addition

**Status:** Active (workspace-specific). Not in upstream droidrun.

---

## Inferred Decisions

These decisions are evident from the code but not explicitly documented. Rationale is inferred.

---

### ADR-I-001: llama-index Pinned to 0.14.4

**Inferred rationale:** LlamaIndex has undergone significant breaking API changes across minor versions. Pinning to `0.14.4` ensures the workflow step API, event passing, and LLM integration work as expected. An unpinned install may pull a breaking version.

**Gap:** The specific reason for this version (vs 0.14.5 or later) is unknown. May be the last version where `llama-index-workflows==2.8.3` is compatible.

---

### ADR-I-002: PostHog for Anonymous Telemetry

**Inferred rationale:** PostHog is a self-hostable, open-source analytics platform with good privacy defaults. Using anonymous distinct IDs avoids PII collection while still enabling usage analytics. Common choice for open-source developer tools.

**Gap:** Whether PostHog is configured to self-host or use PostHog cloud is not verified from workspace configuration.

---

### ADR-I-003: Arize Phoenix as Default Tracer

**Inferred rationale:** Arize Phoenix runs locally without requiring a cloud account or API key. It provides LLM trace visualization that works offline, appropriate for development environments.

**Gap:** Langfuse is also supported (cloud). The reason Phoenix is the default (vs Langfuse as default) is likely local-first preference.

---

### ADR-I-004: adb tcpip 5555 to Fix Wireless Port

**Inferred rationale:** When an Android device connects wirelessly via ADB, it picks a random port. Running `adb tcpip 5555` forces port 5555, making the Tailscale IP+port combination stable and scriptable.

**Gap:** This is documented in setup guides but the decision to use a fixed port vs dynamic discovery is not formally recorded.

---

### ADR-I-005: OpenRouter for Vision, DeepSeek for Text

**Inferred rationale:** DeepSeek's API does not support the `image_url` format required for vision tasks. OpenRouter/Gemini-2.0-flash does. Splitting by capability avoids the cost of vision-capable models for text-only steps.

**Gap:** This split is workspace-specific model selection. Upstream droidrun likely supports multiple providers without this specific split.

---

## Unknown Rationale

These decisions exist in the codebase but their rationale is not documented and cannot be confidently inferred.

| Decision | What Is Observed | What Is Unknown |
|---|---|---|
| `mobilerun-sdk` dependency | Included in requirements | Purpose, what it connects to, whether it's needed |
| `safe_execution: false` default | Disabled by default | Why not default-on given the security risk |
| `auto_setup: true` default | Portal auto-installs | Why this risk is acceptable as default; what triggers re-install |
| Jinja2 prompt templates in `config/prompts/` | Templates exist | Why Jinja2 vs f-strings; which prompts are overridable vs hardcoded |
