# Patterns Log

Record reusable patterns discovered during development.

## Entries

<!-- Format:

## <Pattern Name>

**Context:** When to use this pattern
**Pattern:** Description or code reference
**Example:** File path or snippet reference
**Caveats:** Known limitations or edge cases
-->

## bws-run Secret Injection

**Context:** Any time Cursor or a CLI tool needs API keys without storing them in plaintext
on disk, in environment files, or in version control.

**Pattern:**
```powershell
bws run --project-id <PROJECT_ID> -- <command>
# Example: launch Cursor with all MCP secrets
bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"
```
Secrets are injected as environment variables into the child process only. No plaintext
persisted anywhere.

**Example:** `C:\Users\ynotf\.openclaw\start-cursor-with-secrets.ps1`

**Caveats:**
- `BWS_ACCESS_TOKEN` must be set in the parent shell before calling `bws run`
- If `BWS_ACCESS_TOKEN` is not set, `bws run` fails silently — validate in the script
- The `fc-` Firecrawl key and `OPENMEMORY_API_KEY` must be raw values (no `Token ` prefix) in Bitwarden
- Smithery-hosted MCP servers (Context7, Clear Thought) are not injectable via this pattern
  (they use their own auth)

---

## Two-Layer Autonomous System

**Context:** Designing the relationship between AI-Project-Manager (governance) and open--claw
(execution) so that governance rules are centrally defined and enforced regardless of which
machine open--claw runs on.

**Pattern:**
```
AI-Project-Manager (orchestrator)
  ├── docs/ai/PLAN.md               ← defines goals and phases
  ├── docs/ai/architecture/         ← defines module boundaries and risk levels
  ├── docs/ai/memory/               ← persists decisions and patterns
  └── docs/ai/STATE.md              ← tracks execution evidence

        ↓ (phases, task graphs, approval gates)

open--claw (executor)
  ├── Gateway (control plane)       ← always-on process
  ├── Modules (8)                   ← Planner, Executor, Tool Router, etc.
  ├── Skills / MCP servers          ← capability layer
  └── Audit log                     ← records all Medium/High actions
```

**Example:** `docs/ai/architecture/OPENCLAW_MODULES.md`, `docs/ai/architecture/GOVERNANCE_MODEL.md`

**Caveats:**
- Only one active Gateway at a time (ChaosCentral primary, Laptop warm-standby)
- Governance Model document must be read by open--claw at Gateway startup
- Changes to governance rules require a PLAN-approved PLAN.md update before enforcement
