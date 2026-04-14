# AI Employee Standard

## Read first (supreme charter)
Before using this file or any packet, read `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`. It governs the finished product, autonomy bar, and non‑negotiables. `AUTHORITATIVE_STANDARD.md` and `TEAM_ROSTER.md` interpret the charter and org structure; they must not override it. This document defines packet shape and quality gates; it is subordinate to the charter.

## Decision
No single imported source contains the perfect AI employee folder. The house standard is a hybrid:
- **Official workspace file map:** OpenClaw docs
- **Role-definition quality:** `agency-agents`
- **OpenClaw-shaped packaging and examples:** `awesome-openclaw-agents`
- **Workspace optimization and token discipline:** `ocaudit`
- **Simple memory architecture:** `agent-template`
- **Session rules and proactive operating behavior:** `How-To-Build_Agents-proactive-agent-3.1.0`
- **Runtime shell baseline:** the proven OpenClaw worker shell already stabilized in this repo, not the older purchased CrewClaw shell

This file is the model every future AI employee must follow.

## Best Source Findings
### Best source repo for employee quality
- `open-claw/AI_Employee_knowledgebase/source_repos/agency-agents/agency-agents-main`

### Best official workspace structure reference
- `https://docs.openclaw.ai/reference/templates/AGENTS`
- `https://docs.openclaw.ai/reference/templates/SOUL`
- `https://docs.openclaw.ai/cli/agents`

### Best individual role-definition files
- `source_repos/agency-agents/agency-agents-main/product/product-manager.md`
- `source_repos/agency-agents/agency-agents-main/engineering/engineering-backend-architect.md`

### Best OpenClaw-shaped employee folder
- `source_repos/awesome-openclaw-agents/awesome-openclaw-agents-main/agents/security/vuln-scanner/`

### Best proactive operating templates
- `Agents-Bulk/How-To-Build_Agents-proactive-agent-3.1.0/assets/SOUL.md`
- `Agents-Bulk/How-To-Build_Agents-proactive-agent-3.1.0/assets/AGENTS.md`

### Best external optimization guidance
- `https://github.com/johnpaulhayes/ocaudit/blob/main/references/best-practices.md`

## Required Library Packet Files
Every tracked employee packet must include these files:

| File | Purpose | Primary source influence |
|---|---|---|
| `README.md` | Human-readable role summary, mission, outcomes, and packet purpose | house standard |
| `PROVENANCE.md` | Trace where the role came from and what was adapted | house standard |
| `IDENTITY.md` | Role name, manager, mode, and operating identity | agency-agents |
| `SOUL.md` | Deep persona, mission, principles, tone, and success criteria | agency-agents + proactive |
| `AGENTS.md` | Session rules, memory discipline, safety, collaboration, and proactive behavior | proactive |
| `TOOLS.md` | Real tool expectations and when to use them | awesome-openclaw-agents + house standard |
| `SKILLS.md` | Assigned skills and what they govern | house standard |
| `WORKFLOWS.md` | Concrete role-specific execution flows, not generic filler | agency-agents |
| `MEMORY.md` | What long-term context to preserve and why | proactive |
| `USER.md` | Founder context, quality bar, and expected style of work | house standard |
| `BOOTSTRAP.md` | First-run procedure and verification expectations | proactive + house standard |
| `HEARTBEAT.md` | Ongoing checks, escalation triggers, and cadence | proactive, role-tailored |
| `SCHEDULE.md` | Cadence for startup, mid-cycle, release, and follow-up work | house standard |
| `CHECKLIST.md` | Exact packet blueprint, required docs, required runtime files, and required skills for this role | house standard |
| `AUDIT.md` | What the employee can do now, what is missing, and readiness verdict | house standard |

## File Boundary Rules
These come from the official OpenClaw docs and the strongest external optimization guidance:

- `AGENTS.md` is **how the employee operates**: rules, memory protocol, safety, and collaboration.
- `SOUL.md` is **who the employee is**: tone, values, persona, and boundaries.
- `USER.md` is **who the founder/user is** and how the role should relate to them.
- `IDENTITY.md` is the small identity surface: name, emoji, theme, short self-description.
- `TOOLS.md` is for **real environment notes and tool expectations**, not generic filler.
- `MEMORY.md` is long-term curated memory, not raw daily log spill.
- `HEARTBEAT.md` must stay short and operational because it is repeatedly injected.
- `BOOTSTRAP.md` is a first-run ritual, not a permanent dumping ground.
- Role-specific execution detail belongs in `WORKFLOWS.md`, not spread randomly across every file.

## Required Runtime Package Files
If an employee is intended to run live, it also needs a valid runtime shell:

| File | Purpose |
|---|---|
| `Dockerfile` | Proven, current OpenClaw install path |
| `docker-compose.yml` | Reproducible container launch |
| `entrypoint.sh` | Gateway/bootstrap configuration when remote mode is used |
| `setup.sh` | Safe first-run local setup |
| `.env.example` | Non-secret environment contract |
| `package.json` | Channel dependencies |
| `bot-telegram.js` | Telegram worker entrypoint |
| `bot-discord.js` | Discord worker entrypoint |
| `bot-slack.js` | Slack worker entrypoint |
| `bot-whatsapp.js` | WhatsApp worker entrypoint |
| `heartbeat.sh` | Monitoring/heartbeat loop when applicable |

## Shared Runtime Baseline
Curated live packets under `AI_Employee_knowledgebase/AI_employees` must share one runtime baseline so Docker/package drift does not spread role by role.

- Canonical baseline file: `AI_Employee_knowledgebase/runtime/employee-runtime-baseline.json`
- Drift check: `node AI_Employee_knowledgebase/runtime/check-runtime-drift.mjs`
- Shared values that must stay aligned there: Docker base image, OpenClaw runtime version, and the common channel dependency versions
- If one packet needs a deliberate exception, document it in that packet's `AUDIT.md` before changing the shared baseline

## Token And Context Discipline
Because OpenClaw injects workspace files into prompt context, file quality is also a context-budget problem.

Rules:
- Keep workspace files concise and non-duplicative.
- Avoid bloated `AGENTS.md`, `SOUL.md`, and especially `HEARTBEAT.md`.
- Keep repeated or historical material in supporting docs, not always-loaded files.
- Never let file count create false confidence; dense, accurate files beat many generic files.
- If a file grows large, move secondary material into supporting docs or checklists and leave only the core instructions loaded by default.

## Quality Gates
An employee is not accepted until it passes all of these:
1. **Role specificity:** the role is clearly specialized and does not read like `Custom Role` filler.
2. **Real workflows:** `WORKFLOWS.md` contains role-specific playbooks and deliverables.
3. **Tool realism:** `TOOLS.md` names real tools the role is expected to use, not generic placeholders.
4. **Skill alignment:** `SKILLS.md` matches the job and references usable skills.
5. **Evidence-first behavior:** the role requires proof before claiming completion.
6. **Modularity discipline:** the role pushes work toward `ui`, `domain`, `data`, and `utils` boundaries when building software.
7. **Runtime integrity:** deploy shell files are internally consistent and reference files that actually exist.
8. **Runtime baseline alignment:** curated live packets match `runtime/employee-runtime-baseline.json` or carry an explicit documented exception.
9. **No secrets in repo:** no credentials, tokens, or secret material inside the packet.
10. **Auditability:** `PROVENANCE.md` and `AUDIT.md` exist and are current.
11. **Context efficiency:** the packet avoids duplication and bloat that would waste OpenClaw context.
12. **Checklist completeness:** `CHECKLIST.md` exists and clearly marks required docs, runtime files, skills, and current completion status.
13. **Explicit grade:** `AUDIT.md` includes a grade and the reasoning behind it.

## Anti-Patterns To Reject
Reject imported employees that have any of these unless they are being mined only for partial salvage:
- `Custom Role` or equivalent placeholder identity
- generic “versatile AI employee” personality text
- same four-skill bundle repeated across unrelated roles
- generic “morning briefing / escalation / end-of-day summary” workflows for specialist jobs
- tool docs that only say research/web search/data analysis for every role
- placeholder memory/bootstrap files with no role adaptation
- outdated runtime shell such as the older purchased CrewClaw install path
- deploy files that reference missing files
- role titles that overstate actual capability
- bloated workspace files that repeat the same rules in multiple places
- personality packs that lack deliverables, workflows, or tool realism

## Build Rule
When importing an employee from any outside source:
1. Audit file by file.
2. Keep only the files with real value.
3. Replace weak files from stronger sources or build them fresh.
4. Record the provenance.
5. Write or update `AUDIT.md` before accepting the packet.

## Source Hierarchy
When building or upgrading employees, prefer sources in this order:
1. `FINAL_OUTPUT_PRODUCT.md` (charter; supreme)
2. `AUTHORITATIVE_STANDARD.md` and `TEAM_ROSTER.md` (interpreters; subordinate to the charter)
3. `AI-EMPLOYEE-STANDARD.md` (this file)
4. Curated house packets under `AI_Employee_knowledgebase/AI_employees`
5. `agency-agents` for role depth
6. `awesome-openclaw-agents` for OpenClaw-facing packaging ideas
7. proactive-agent templates for operating discipline
8. purchased CrewClaw packets only for small salvageable pieces

## Current Verdict
The project does **not** currently have one fully complete imported employee folder that can be trusted unchanged.

The closest usable references are:
- OpenClaw docs for official workspace structure
- `agency-agents` for role-definition depth
- `awesome-openclaw-agents/.../vuln-scanner` for OpenClaw-style packaging quality
- `ocaudit` for file-boundary and token-budget discipline
- `software-engineer.zip` for the strongest purchased CrewClaw role subset

The standard above is therefore the required model for every future employee packet, always subordinate to `FINAL_OUTPUT_PRODUCT.md`.
