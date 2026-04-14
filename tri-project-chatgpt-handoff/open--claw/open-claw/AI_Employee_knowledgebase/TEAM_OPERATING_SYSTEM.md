# Team Operating System

## Authority
Read `FINAL_OUTPUT_PRODUCT.md` first. This file is subordinate to the charter, `AUTHORITATIVE_STANDARD.md`, and `TEAM_ROSTER.md`.

## Purpose
Turn the curated 15-employee library into a controlled delivery system led by Sparky instead of a loose collection of packets.

## Mission
- keep Sparky as the final accept/reject gate
- route work through specialist pods instead of ad hoc agent choice
- keep context small by handing off compact deliverables, not whole histories
- require evidence before any packet is considered done
- keep runtime readiness separate from role quality
- keep recovery durable after chat loss by promoting compact stable summaries into canonical docs and OpenMemory

## Org Shape

### Leadership spine
- `sparky-chief-product-quality-officer` owns final product quality, acceptance, and refactor authority
- `delivery-director` owns sequencing, dependency management, and routing
- `product-manager` owns briefs, acceptance criteria, and non-goals
- `software-architect` owns architecture direction and boundary integrity

### Delivery pods
- Product pod: `product-manager`, `delivery-director`
- Architecture pod: `software-architect`, `backend-architect`, `mcp-integration-engineer`
- Experience pod: `ux-architect`, `ui-designer`, `frontend-developer`, `accessibility-auditor`
- Quality pod: `code-reviewer`, `qa-evidence-collector`, `reality-checker`
- Release pod: `devops-automator`, `seo-ai-discovery-strategist`

## Standard Work Packet
Every feature, bug, or migration must move through the same compact handoff chain:

1. Brief
2. Architecture
3. Implementation
4. Review
5. Evidence
6. Sparky gate
7. Release
8. Post-release verification

## Required Deliverable By Role
- `product-manager`: scope, non-goals, acceptance criteria, user-facing outcome
- `software-architect` or `backend-architect`: boundary plan, risks, interfaces, data flow
- implementer: changed files plus short rationale
- `code-reviewer`: findings only, severity ordered
- `qa-evidence-collector`: proof artifacts, smoke results, remaining gaps
- `reality-checker`: go/no-go recommendation with concrete risks
- `devops-automator`: release steps, rollback path, deploy evidence
- `sparky-chief-product-quality-officer`: final decision, corrections, or acceptance

## Context Discipline
- Briefs must be short and scoped to one packet.
- Architecture handoffs must describe boundaries, not repeat the full brief.
- Review handoffs must contain findings, not rewritten implementation summaries.
- Evidence handoffs must point to proof, not narrate everything that happened.
- Sparky receives only the latest packet outputs plus required proof.
- Worker handoffs should remain small enough to survive reboot recovery without needing raw transcript reloads.

## Readiness States
Track every employee in one of these states:

| State | Meaning |
|---|---|
| `packet_ready` | docs, skills, and runtime files are structurally complete |
| `runtime_ready` | token/bot wiring exists and startup dependencies are satisfied |
| `smoke_ready` | can be started and paired against the real gateway |
| `live_ready` | passed message-flow smoke tests and can be assigned real work |

Use `CURATED_TEAM_STATUS.json` as the machine-readable source of truth for these tracked states.

## Current Gaps To Live Squad
- `accessibility-auditor` needs a brand-new Telegram bot
- `backend-architect` needs a brand-new Telegram bot
- `delivery-director` needs explicit env wiring or a direct Bitwarden UUID
- `product-manager` needs explicit env wiring or a direct Bitwarden UUID
- `sparky-chief-product-quality-officer` needs explicit env wiring or a direct Bitwarden UUID
- first-run gateway pairing approval is still required before curated workers are fully live
- phone/voice support is now an incubation track under `VOICE_FRONT_DESK_STACK.md`, separate from the curated 15-worker generator

## Activation Order
Bring the curated squad online in this order:

1. Sparky
2. delivery-director
3. product-manager
4. software-architect
5. code-reviewer
6. qa-evidence-collector
7. reality-checker
8. devops-automator
9. frontend-developer
10. backend-architect
11. ux-architect
12. ui-designer
13. accessibility-auditor
14. mcp-integration-engineer
15. seo-ai-discovery-strategist

## Startup Discipline
- Use `open-claw/employees/deployed-curated/start-employees.ps1 -CheckOnly` before any live start.
- Default startup may be partial: ready workers can launch even while blocked workers remain unresolved.
- Use `-Strict` only when the goal is a full-squad clean launch with zero unresolved workers.
- Do not treat blocked workers as a reason to keep all ready workers offline.

## Memory Promotion
- Use `MEMORY_PROMOTION_TEMPLATE.md` to turn completed packet outputs into compact durable memory candidates.
- Sparky or the responsible gate role validates the packet before promotion.
- Promote only the stable summary, not raw transcript or full terminal output.
- Prefer compact self-identifying memory text so future retrieval does not depend on unsupported metadata filters.

## Ready For The First App Clone Test When
- OpenMemory session recovery is stable in live Cursor chats
- Sparky, delivery-director, product-manager, software-architect, code-reviewer, qa-evidence-collector, and devops-automator are all `live_ready`
- the remaining specialists are at least `runtime_ready`
- the delivery chain is exercised once on a smaller internal work packet before the `4axe.com` clone effort
