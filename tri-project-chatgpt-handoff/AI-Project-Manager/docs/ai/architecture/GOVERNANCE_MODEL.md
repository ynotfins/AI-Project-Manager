# open--claw Governance Model

**Last updated:** 2026-04-07
**Supersedes:** 2026-03-31 version

---

## Purpose

The Governance Model defines **what the AI employee team may do autonomously, what requires Sparky's internal approval, and what is exclusively reserved for Tony**. It is the safety layer between autonomous delivery operation and real-world consequences.

This model is aligned with `open--claw/open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`, which states:

> Day-to-day software delivery work must not depend on human interpretation, manual sequencing, or constant approval. Human involvement is reserved only for governance boundaries that must remain under Tony's control.

AI-Project-Manager owns this document. open--claw reads it at Gateway startup and enforces it via the Governance overlay applied before every action.

---

## Authority Structure

| Authority | Layer | Scope |
|---|---|---|
| **Tony** (human) | Supreme | Changing `FINAL_OUTPUT_PRODUCT.md`; revoking privileged credentials; approving irreversible real-world actions; redefining the product goal |
| **AI-PM** (governance agent) | Strategic | Workflow rules, 5-tab contracts, memory namespace governance, tool policy, context budgets, cross-project coordination, STATE.md/HANDOFF.md maintenance |
| **Sparky** (`sparky-chief-product-quality-officer`) | Tactical | Development execution, 15-employee team management, code quality, build/test/ship, product decisions within charter, ACCEPT/REFACTOR/REJECT authority, secret creation via Machine Account |
| **AI employee team** (15 employees) | Operational | Autonomous execution of delivery tasks under Sparky's direct supervision |

### Role Separation

AI-PM operates at the PLAN level (produces prompts). Sparky operates at the AGENT level (executes prompts and manages employees). They communicate via:

- AI-PM → Sparky: PLAN tab produces AGENT prompts
- Sparky → AI-PM: STATE.md execution blocks and OpenMemory decision storage
- Conflict resolution: FINAL_OUTPUT_PRODUCT.md wins, then Tony, then AI-PM governance rules

AI-PM never commands employees directly. Sparky never modifies workflow rules or memory governance.

### Bitwarden Machine Account

The Machine Account `R3lentle$$-Grind-Global-Memory` enables Sparky to:

- List and read existing secrets (auto-approve)
- Create new secrets for employees or services (Sparky-notified, not Tony-gate)
- Inject secrets via `bws run` (auto-approve)

Revoking or deleting secrets for external services remains Tony-gate.

Routine delivery work does not wait for user approval. Sparky is the approval layer for internal work.

---

## Risk Levels

Three risk levels determine the approval behavior for every action:

| Level | Name | Approval behavior | Timeout |
|---|---|---|---|
| 🟢 Low | Auto-approve | Execute immediately; no notification required | None |
| 🟡 Medium | Sparky-notified | Sparky is notified; execution proceeds unless Sparky stops it | None (Sparky acts immediately if needed) |
| 🔴 Tony-gate | Tony explicit approval required | Halt execution; wait for Tony's explicit confirmation; do not auto-approve or route to Sparky | Indefinite |

---

## Action Classification

### 🟢 Low — Auto-Approve (no human interaction)

| Action | Rationale |
|---|---|
| Read any file in allowed scoped paths | Read-only, no side effect |
| Web search / SERP lookup | No mutation |
| Crawl public URL | Read-only |
| Write to staging environment | Easily reversible |
| Generate or refactor code (not yet deployed) | No external effect until deployed |
| Open a GitHub PR | Reversible; internal delivery step |
| Add / search memory | Non-destructive |
| Health check / status query | Read-only probe |
| Shell command in scoped path (read or scoped write) | Limited scope, reversible |
| Trigger CI/CD pipeline (staging) | Reversible; internal delivery step |
| Planning, re-planning, and phase sequencing | Internal delivery coordination |
| Rule rewrites and governance doc updates | Internal delivery coordination |
| Model escalation decisions | Internal to the agent team |
| Internal task delegation between AI employees | Internal coordination |
| Refactoring any amount of code in a focused area | Normal delivery work |
| Writing, editing, or deleting files in scoped paths | Normal delivery work |
| Merge PR to a non-main branch | Internal delivery step |
| Delete memory entry | Permanent but recoverable from docs |
| Add new MCP server configuration | Infrastructure change within approved scope |
| Send notification via internal messaging channel | Internal communication |
| SEO meta tag / structured data changes | Reversible; live ranking impact is monitored |
| Content changes on staging | Staging-only; no production effect |

### 🟡 Medium — Sparky-Notified (Sparky reviews; execution proceeds)

| Action | Rationale |
|---|---|
| Merge PR to main/master | Permanent code change; Sparky must confirm readiness |
| Modify > 1000 LOC in a single PR | Broad change; Sparky reviews before merge |
| Deploy to production | Immediate live impact; Sparky signoff required (not Tony unless external real-world risk) |
| Change authentication configuration | Security boundary; Sparky review |
| Rotate or regenerate API keys (internal services only) | Disrupts dependent services; Sparky review |
| Create new Bitwarden secrets via Machine Account | Service provisioning; Sparky review |
| Rotate existing secrets via Machine Account | Disrupts dependent services; Sparky review |
| Disable any Gateway service | Service disruption; Sparky review |
| SEO changes touching > 50 pages | Broad ranking risk; Sparky review |
| Any action outside defined scoped paths | Sandbox boundary; Sparky review before proceeding |

### 🔴 Tony-gate — Tony's Explicit Approval Required

| Action | Rationale |
|---|---|
| Change `FINAL_OUTPUT_PRODUCT.md` | Supreme product charter; only Tony may amend |
| Redefine the product goal | Reserved human authority per the charter |
| Revoke privileged credentials for external services | Secrets management; Tony's exclusive domain |
| Delete Bitwarden secrets for external services | Tony's exclusive domain for destructive secret ops |
| Financial transaction of any kind | Real money; zero autonomy |
| Access financial account data | Sensitive data exposure risk |
| Send external communication to real people (email, SMS, WhatsApp to Tony's contacts) | User-impersonation risk |
| Deploy to production in a way that creates irreversible external-world consequences | Real-world permanent effect |
| Any action outside designated filesystem scopes | Sandbox escape risk |

---

## Safety Constraints (Hard Rules — Never Auto-Approved)

These constraints are **permanently blocked** and may not be overridden by any internal authority, including Sparky:

```
FINANCIAL:
  - Direct access to savings accounts: BLOCKED
  - Direct access to operating accounts: BLOCKED
  - Only the funded bill-pay sandbox is accessible for financial operations
  - Maximum transaction size: $0 (zero — all transactions require Tony's explicit approval)

INFRASTRUCTURE:
  - Only one active Gateway at a time (ChaosCentral is primary)
  - Laptop Gateway: stopped by default; only started for failover
  - No Gateway on non-designated machines

DEPLOYMENT:
  - Default target: staging
  - Production deployments with irreversible external-world consequences require Tony approval
  - Standard production deployments with rollback paths require Sparky signoff only
  - No force-push to main/master under any circumstances

SECRETS:
  - No secrets committed to any repository
  - No secrets printed to any log
  - No secrets passed as command arguments
  - Bitwarden (bws run) is the only authorized injection path

SCOPE:
  - Filesystem access scoped to: D:\github, D:\github_2, ~/.openclaw
  - No access outside designated paths (even if technically possible)
  - No access to other users' files or system directories

IDENTITY:
  - No impersonation of Tony in external communications
  - All AI-generated messages to real external contacts must be reviewed before send
```

---

## Sparky's Internal Authority

Sparky (`sparky-chief-product-quality-officer`) is the internal approval and quality authority for all routine software-delivery work. This means:

- Sparky may approve, reject, or require refactor of any code change, architecture decision, or delivery step without waiting for Tony.
- Sparky may escalate any task back to the responsible employee with correction requirements.
- Sparky must review every file-change during delivery per the mandatory review rule in `FINAL_OUTPUT_PRODUCT.md`.
- Sparky's go/no-go decision is required before merging to main or deploying to production.
- Sparky may not override the Tony-gate list or the hard safety constraints above.

Sparky does **not** require user confirmation to exercise these authorities. They are internal to the team.

---

## Internal Escalation Path

When the team encounters uncertainty during delivery, the escalation path is:

```
1. PAUSE — Stop the current action.
2. CLASSIFY — Determine whether the uncertainty is:
   a. Technical ambiguity → route to Sparky for internal resolution
   b. Missing information resolvable from docs/memory → resolve internally
   c. Tony-gate action → halt and notify Tony via configured channel
   d. Tool failure → follow fallback policy in 05-global-mcp-usage.md
3. RESOLVE:
   - For (a) and (b): Sparky decides; resume without Tony involvement
   - For (c): Notify Tony with what was attempted, why paused, what is needed, and safe fallback
   - For (d): Use fallback; record FAIL in STATE.md
4. AUDIT — Log the escalation event regardless of resolution.
```

**Never:** Pause normal delivery work waiting for Tony input on internal decisions.
**Always:** Escalate Tony-gate actions to Tony; resolve everything else internally.

---

## Audit Requirements

Every action that is Sparky-notified or Tony-gate must produce an audit record:

| Field | Required | Source |
|---|---|---|
| Timestamp (UTC) | Yes | System clock |
| Action type | Yes | Module + operation |
| Risk level | Yes | Governance Model classification |
| Inputs | Yes | Sanitized (no secrets) |
| Output | Yes | Sanitized result or error |
| Approval signal | Yes (Sparky/Tony gates) | Sparky decision or Tony response |
| Module | Yes | Which module triggered |
| Outcome | Yes | PASS / FAIL / ROLLBACK |

**Storage:** `docs/ai/audit/` in AI-Project-Manager repo (append-only log per date).
**Retention:** 90 days minimum; 1 year for financial actions.
**Secret handling:** Audit logs must never contain raw secret values. Use `[REDACTED]` for any field that could expose credentials, PII, or financial account data.

---

## Least-Privilege Rules

1. **Filesystem:** open--claw reads/writes only within the three approved paths. It does not enumerate files outside these paths.
2. **GitHub:** open--claw uses `GITHUB_PERSONAL_ACCESS_TOKEN` scoped to specific repos. It does not create repos, manage org settings, or access other users' repos.
3. **Financial:** open--claw reads bill-pay sandbox exports only. No write access to any financial account. No stored financial account credentials.
4. **Shell:** open--claw runs shell commands only in scoped working directories. No `sudo`, no system path mutation, no process management outside own PIDs.
5. **MCP tools:** open--claw uses only configured MCP servers. It does not install new MCP servers at runtime without a Governance Model update.
6. **Memory:** open--claw stores memories scoped to `ynotfins/AI-Project-Manager` or `ynotfins/open--claw`. It does not write to other project namespaces.

---

## Approval Channel (Tony-gate only)

Current configured channel for Tony-gate actions: **WhatsApp / Telegram** (via open--claw Gateway inbox).

Fallback: Direct Cursor chat in AI-Project-Manager AGENT tab.

Tony approval format:

```
APPROVE <task-id>     — approves the pending Tony-gate action
REJECT <task-id>      — rejects and halts; team re-plans
APPROVE ALL           — approves all pending Tony-gate actions in current session
```

Sparky approval is recorded in `docs/ai/STATE.md` and the audit log; it does not require a channel message.
