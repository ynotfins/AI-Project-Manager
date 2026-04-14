# Recommended Next Documentation

DroidRun v0.5.1 — Priority list of documentation that would most improve maintainability, security, and onboarding.

Items are ordered by impact. Each entry includes what to document, where to find the source material, and why it matters.

---

## 1. Portal APK API Reference

**File to create:** `docs/portal-api-reference.md`

**What to document:**
- All HTTP endpoints exposed by the Portal APK on port 8080
- Request method, path, and body format for each endpoint
- Response format (JSON schema) for each endpoint
- Error codes and what they mean
- Which endpoints are used by which DroidRun actions

**Source material:**
- `src/droidrun/tools/android/portal_client.py` — all HTTP calls are here
- Portal APK source (if accessible) — defines the server routes

**Why it matters:** The Portal APK HTTP API is the most critical interface in DroidRun. Every device action passes through it. Without a reference, any change to the APK risks breaking the Python client silently. This is the highest-risk undocumented interface in the system.

---

## 2. Agent Prompt Library

**File to create:** `docs/prompt-library.md`

**What to document:**
- All Jinja2 prompt templates in `config/prompts/` (or wherever they reside)
- Template name, purpose, and when it is used
- Variables available in each template context
- Which prompts are user-overridable vs hardcoded
- Example rendered output for each prompt

**Source material:**
- `config/prompts/` directory (search for `.j2` or `.jinja2` files)
- `src/droidrun/agent/` — where prompts are rendered

**Why it matters:** Prompts directly control LLM behavior. Undocumented prompts make it impossible to tune agent behavior predictably. Users who want to improve agent performance have no starting point.

---

## 3. Action Reference

**File to create:** `docs/action-reference.md`

**What to document:**
- Complete list of all agent actions: `click`, `type`, `swipe`, `press_key`, `open_app`, `wait`, `screenshot`, `complete`, `remember`
- Parameters for each action with types, constraints, and required vs optional
- What each action does on the device
- Known limitations (e.g., `type` may not work in all apps without the DroidRun keyboard)
- Examples of each action in context

**Source material:**
- `src/droidrun/tools/driver/android.py` — action implementations
- `src/droidrun/tools/` — ToolRegistry action definitions

**Why it matters:** Agents and users both need to understand what actions are available and what they do. This is also essential for writing effective task goals that the agent can execute.

---

## 4. LLM Provider Setup Guide

**File to create:** `docs/llm-provider-setup.md`

**What to document (per provider):**
- DeepSeek: API key setup, model name, text-only (no vision), cost
- OpenRouter: API key setup, model selection (Gemini-2.0-flash recommended for vision), vision support
- Google Gemini: API key setup, model name, vision support
- OpenAI: API key setup, model name, vision support (if supported)
- Ollama (local): setup, model name, no API key required
- For each: which config keys to set, example config snippet

**Source material:**
- `src/droidrun/llm/` — provider implementations
- `src/droidrun/config_example.yaml` — config keys

**Why it matters:** New users most commonly get blocked on LLM provider setup. A per-provider guide eliminates the most common onboarding failures.

---

## 5. Macro Format Specification

**File to create:** `docs/macro-format.md`

**What to document:**
- File format (JSON? YAML?) for recorded macros
- JSON/YAML schema with field descriptions
- How macros are recorded (`droidrun record`?)
- How macros are replayed
- What actions can be recorded and replayed
- Limitations (e.g., element indices may not be stable across app versions)

**Source material:**
- CLI source for `record` command in `src/droidrun/cli/main.py`
- Any macro serialization code in the tools layer

**Why it matters:** Macros are a key automation primitive for repetitive tasks. Without format documentation, recorded macros are opaque and cannot be manually edited or debugged.

---

## 6. Trajectory File Format

**File to create:** `docs/trajectory-format.md`

**What to document:**
- JSON schema for trajectory files stored in `trajectories/`
- What each field contains (step index, timestamp, UI state, LLM input, LLM output, action, result)
- Whether screenshots are embedded or referenced
- How to parse and analyze trajectory files
- Privacy note: trajectory files may contain sensitive device screen content

**Source material:**
- Trajectory serialization code in `src/droidrun/agent/droid/droid_agent.py` or related files
- Example trajectory file from a test run

**Why it matters:** Trajectory files are the primary debugging artifact for failed agent tasks. Without schema documentation, debugging requires reverse-engineering the JSON structure manually.

---

## 7. Credential Manager Usage Guide

**File to create:** `docs/credential-manager.md`

**What to document:**
- How to enable the credential manager (`credentials.enabled: true`)
- How to add app credentials (format, command or file edit)
- How credentials are referenced in task goals
- Whether credential values are encrypted at rest (verify first)
- How credentials are injected into agent context
- Security considerations (risk of storing passwords)

**Source material:**
- `src/droidrun/config_manager/config_manager.py`
- `~/.config/droidrun/credentials.yaml` format

**Why it matters:** The credential manager is a high-risk feature (stores app passwords). Users need to know exactly what they are enabling before using it.

---

## 8. MCP Server Extension Guide

**File to create:** `docs/mcp-extension-guide.md`

**What to document:**
- How to add a new tool to `mcp_server.py`
- MCP tool definition format (name, description, parameters, handler)
- How to expose a new DroidRun capability as an MCP tool
- How to test a new MCP tool from Cursor and Claude Desktop
- MCP server restart procedure after adding tools

**Source material:**
- `mcp_server.py` (workspace-specific)
- MCP SDK documentation

**Why it matters:** The MCP server is the primary integration point between DroidRun and AI clients. Making it extensible and documented enables the workspace to grow without requiring deep DroidRun internals knowledge.

---

## 9. Testing Guide

**File to create:** `docs/testing-guide.md`

**What to document:**
- How to write a unit test for a new DroidRun feature
- How to mock Portal HTTP responses for driver tests
- How to run tests without a physical device (mock device)
- Integration test approach (requires physical device)
- How to add test cases for new actions
- How to test MCP tool additions

**Source material:**
- Existing test files (if any — none found in workspace)
- Upstream droidrun test patterns (check upstream repo)

**Why it matters:** There is currently no documented test approach and no test suite found in the workspace. Before adding features, a testing foundation is critical. This document should be created alongside the first test file.

---

## 10. Upstream Sync Guide

**File to create:** `docs/upstream-sync-guide.md`

**What to document:**
- How this workspace fork relates to upstream github.com/droidrun/droidrun
- Which commit or tag this workspace was forked from (if known)
- Process for pulling upstream changes without breaking workspace additions
- Files that are workspace-specific and must not be overwritten from upstream (see `docs/unknowns-gaps-assumptions.md` Section 7)
- How to resolve conflicts between upstream and workspace changes
- Recommended sync cadence

**Source material:**
- Git history (if available)
- `docs/unknowns-gaps-assumptions.md` Section 7 — workspace-specific file list

**Why it matters:** This workspace will drift from upstream over time. Without a sync guide, merging upstream bugfixes and features becomes increasingly risky. Upstream may fix Portal APK issues or add new LLM providers that this workspace needs.

---

## Priority Summary

| Priority | Document | Risk Addressed |
|---|---|---|
| 1 | Portal APK API Reference | Silent client–APK contract breakage |
| 2 | Agent Prompt Library | LLM behavior opacity |
| 3 | Action Reference | Agent capability ambiguity |
| 4 | LLM Provider Setup Guide | Onboarding friction |
| 5 | Upstream Sync Guide | Upstream divergence risk |
| 6 | Trajectory File Format | Debugging capability |
| 7 | Credential Manager Usage | Security awareness for high-risk feature |
| 8 | Testing Guide | No automated regression protection |
| 9 | Macro Format Specification | Automation record/replay opacity |
| 10 | MCP Server Extension Guide | Integration extensibility |
