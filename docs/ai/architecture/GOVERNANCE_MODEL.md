# open--claw Governance Model

**Last updated:** 2026-02-23
**Author:** Agent (Phase 6A)

---

## Purpose

The Governance Model defines **what open--claw may do autonomously, what requires human
approval, and what is permanently blocked**. It is the safety layer between autonomous
operation and real-world consequences.

AI-Project-Manager owns this document. open--claw reads it at Gateway startup and enforces
it via the Governance overlay applied by the Executor before every High/Medium action.

---

## Risk Levels

Three risk levels determine the approval behavior for every action:

| Level | Name | Approval behavior | Timeout |
|---|---|---|---|
| 🟢 Low | Auto-approve | Execute immediately without notification | None |
| 🟡 Medium | Notify + auto-approve | Notify user via configured channel; proceed after timeout unless rejected | 30 minutes |
| 🔴 High | Explicit approval required | Halt execution; wait for explicit user confirmation; do not auto-approve | Indefinite |

---

## Action Classification

### 🟢 Low — Auto-Approve

| Action | Module | Rationale |
|---|---|---|
| Read any file in allowed scoped paths | Tool Router | Read-only, no side effect |
| Web search / SERP lookup | Tool Router | No mutation |
| Crawl public URL | SEO Engine | Read-only |
| Write to staging environment | Deployment Engine | Easily reversible |
| Generate code (not yet deployed) | Code Generator | No external effect until deployed |
| Add / search memory | Memory Engine | Non-destructive |
| Write report to Google Sheets (read-only tab) | Finance Engine | Append-only, no mutation |
| Health check / status query | All | Read-only probe |
| Shell command in scoped path (read) | Tool Router | No mutation |

### 🟡 Medium — Notify + Auto-Approve (30 min)

| Action | Module | Rationale |
|---|---|---|
| Modify SEO meta tags / structured data | SEO Engine | Live ranking impact, reversible |
| Modify content on staging | Code Generator | Affects staging users if any |
| Open GitHub PR | Code Generator / Deployment Engine | Requires human awareness |
| Delete memory entry | Memory Engine | Permanent but recoverable from docs |
| Shell command with write operations in scoped path | Tool Router | Limited scope, reversible |
| Trigger CI/CD pipeline (staging) | Deployment Engine | Build cost; staging impact |
| Categorize financial transaction (auto-assign) | Finance Engine | Reversible via re-categorization |
| Send notification via messaging channel | All | User-visible communication |
| Add new MCP server configuration | Tool Router | Infrastructure change |

### 🔴 High — Explicit Approval Required

| Action | Module | Rationale |
|---|---|---|
| Deploy to **production** | Deployment Engine | Immediate live impact |
| Modify > 500 LOC in a single PR | Code Generator | Broad change, high review burden |
| Merge PR to main/master | Deployment Engine | Permanent code change |
| Financial transaction of any kind | Finance Engine | Real money at stake |
| Access financial account data | Finance Engine | Sensitive data exposure risk |
| Delete files in any environment | All | Potentially irreversible |
| Change authentication configuration | All | Security boundary |
| Rotate or regenerate API keys | All | Disrupts dependent services |
| Add/remove Bitwarden secrets | Tool Router | Secrets management |
| Disable any Gateway service | All | Service disruption |
| Send external communication (email, SMS, WhatsApp to contacts) | All | User-impersonation risk |
| SEO changes touching > 20 pages | SEO Engine | Broad ranking risk |
| Any action outside defined scoped paths | Tool Router | Sandbox escape risk |

---

## Safety Constraints (Hard Rules — Never Auto-Approved)

These constraints are **permanently blocked** and may not be overridden by any approval:

```
FINANCIAL:
  - Direct access to savings accounts: BLOCKED
  - Direct access to operating accounts: BLOCKED
  - Only the funded bill-pay sandbox is accessible for financial operations
  - Maximum transaction size: $0 (zero — all transactions require explicit approval)

INFRASTRUCTURE:
  - Only one active Gateway at a time (ChaosCentral is primary)
  - Laptop Gateway: stopped by default; only started for failover
  - No Gateway on non-designated machines

DEPLOYMENT:
  - Default target: staging
  - Production requires explicit approval — ALWAYS (no exceptions for "simple" changes)
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
  - All AI-generated messages must be clearly labeled or reviewed before send
```

---

## Escalation Path

When open--claw encounters uncertainty, it follows this escalation path:

```
1. PAUSE — Stop the current action immediately.
2. CLASSIFY — Determine whether the uncertainty is:
   a. Ambiguous input (ask Planner to re-plan with constraints)
   b. Missing information (request from user via configured channel)
   c. Risk boundary (treat as High-risk, require explicit approval)
   d. Tool failure (follow fallback policy in 05-global-mcp-usage.md)
3. NOTIFY — Inform user via configured channel with:
   - What was being attempted
   - Why execution paused
   - What is needed to proceed
   - Proposed safe fallback (if any)
4. WAIT — Do not proceed until the appropriate signal is received.
5. AUDIT — Log the escalation event regardless of resolution.
```

**Never:** Guess and proceed. Uncertainty always escalates upward.

---

## Audit Requirements

Every action that is Medium or High risk must produce an audit record:

| Field | Required | Source |
|---|---|---|
| Timestamp (UTC) | Yes | System clock |
| Action type | Yes | Module + operation |
| Risk level | Yes | Governance Model classification |
| Inputs | Yes | Sanitized (no secrets) |
| Output | Yes | Sanitized result or error |
| Approval signal | Yes (Medium/High) | User response or timeout |
| Module | Yes | Which module triggered |
| Task graph ID | Yes | From Planner |
| Outcome | Yes | PASS / FAIL / ROLLBACK |

**Storage:** `docs/ai/audit/` in AI-Project-Manager repo (append-only log per date).
**Retention:** 90 days minimum; 1 year for financial actions.
**Secret handling:** Audit logs must never contain raw secret values. Use `[REDACTED]` for any
field that could expose credentials, PII, or financial account data.

---

## Least-Privilege Rules

1. **Filesystem:** open--claw reads/writes only within the three approved paths.
   It does not enumerate files outside these paths, even for audit purposes.
2. **GitHub:** open--claw uses `GITHUB_PERSONAL_ACCESS_TOKEN` scoped to specific repos.
   It does not create repos, manage org settings, or access other users' repos.
3. **Financial:** open--claw reads bill-pay sandbox exports only. No write access to any
   financial account. No stored financial account credentials.
4. **Shell:** open--claw runs shell commands only in scoped working directories.
   No `sudo`, no system path mutation, no process management outside own PIDs.
5. **MCP tools:** open--claw uses only configured MCP servers. It does not install new MCP
   servers at runtime without a Governance Model update approved by AI-Project-Manager.
6. **Memory:** open--claw stores memories scoped to `ynotfins/AI-Project-Manager` or
   `ynotfins/open--claw`. It does not write to other project namespaces.

---

## Approval Channel

Current configured approval channel: **WhatsApp / Telegram** (via open--claw Gateway inbox).

Fallback: Direct Cursor chat in AI-Project-Manager AGENT tab.

Approval format required:
```
APPROVE <task-id>     — approves the pending action
REJECT <task-id>      — rejects and halts; Planner re-plans
APPROVE ALL           — approves all pending Medium actions in current session
```

---

## Phase Status

| Phase | Governance component | Status |
|---|---|---|
| 6A | This document — governance model defined | COMPLETE (architecture only) |
| 6B | Gateway boot — enforcement wired into Gateway | BLOCKED (waiting: ANTHROPIC_API_KEY) |
| 6C | Approval channel — WhatsApp/Telegram wired | BLOCKED (depends on 6B) |
