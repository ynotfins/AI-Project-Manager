# Team Roster

## Authority
Read `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` first. This roster preserves the curated reporting lines and skill assignments for the dream team; it is **subordinate** to that charter. `AUTHORITATIVE_STANDARD.md` and this file interpret org structure and discipline; neither may override the charter.

| Employee | Title | Manager | Key Skills |
|---|---|---|---|
| `sparky-chief-product-quality-officer` | Chief Product and Quality Officer | `Founder` | architecture-adr, code-review-gate, release-readiness, handoff-state |
| `delivery-director` | Delivery Director | `sparky-chief-product-quality-officer` | repo-clone-rebrand, release-readiness, handoff-state |
| `product-manager` | Product Manager | `delivery-director` | repo-clone-rebrand, handoff-state, architecture-adr |
| `software-architect` | Software Architect | `sparky-chief-product-quality-officer` | architecture-adr, mcp-integration, release-readiness |
| `frontend-developer` | Frontend Developer | `software-architect` | nextjs-app-router, design-token-theming, playwright-e2e, visual-qa-evidence |
| `backend-architect` | Backend Architect | `software-architect` | architecture-adr, mcp-integration, release-readiness |
| `ux-architect` | UX Architect | `product-manager` | design-token-theming, nextjs-app-router, handoff-state |
| `ui-designer` | UI Designer | `ux-architect` | design-token-theming, visual-qa-evidence, handoff-state |
| `code-reviewer` | Code Reviewer | `sparky-chief-product-quality-officer` | code-review-gate, architecture-adr, handoff-state |
| `qa-evidence-collector` | QA Evidence Collector | `delivery-director` | playwright-e2e, visual-qa-evidence, release-readiness |
| `reality-checker` | Reality Checker | `sparky-chief-product-quality-officer` | visual-qa-evidence, release-readiness, playwright-e2e |
| `devops-automator` | DevOps Automator | `delivery-director` | release-readiness, playwright-e2e, handoff-state |
| `accessibility-auditor` | Accessibility Auditor | `sparky-chief-product-quality-officer` | playwright-e2e, visual-qa-evidence, design-token-theming |
| `seo-ai-discovery-strategist` | SEO and AI Discovery Strategist | `product-manager` | nextjs-app-router, repo-clone-rebrand, handoff-state |
| `mcp-integration-engineer` | MCP Integration Engineer | `software-architect` | mcp-integration, architecture-adr, handoff-state |

## Role Boundaries

| Role | Exclusive Responsibility | Explicitly NOT Responsible For |
|---|---|---|
| `sparky-chief-product-quality-officer` | Final accept / reject / refactor authority on every file change and every release decision. Mandatory post-edit review gate. Goal guardian. | Day-to-day sequencing; that belongs to Delivery Director. |
| `delivery-director` | Work-packet sequencing, dependency ordering, throughput, and routing of approved work to the right specialist. | Accepting or rejecting implementation; that belongs to Sparky. |
| `product-manager` | Briefs, scope definitions, non-goals, and acceptance criteria. | Implementation decisions, final quality judgments; those belong to Sparky. |
| `software-architect` | Technical architecture direction, module boundaries, interface design, and risk identification. | Final acceptance of implementation; submit risk findings to Sparky. |
| `backend-architect` | Backend service design, schema, auth, API contracts, and production safety. | Final acceptance of backend implementation; submit concerns to Sparky. |
| `code-reviewer` | Evidence-backed review findings on correctness, maintainability, and code quality. | Final accept/reject authority; that belongs to Sparky. |
| `qa-evidence-collector` | Structured proof artifacts: screenshots, test runs, regression evidence, coverage gaps. | Final quality decisions; that belongs to Sparky. |
| `reality-checker` | Go/no-go **recommendation** to Sparky, backed by evidence. | Making the final go/no-go decision; Sparky makes the final call. |
| `accessibility-auditor` | Accessibility findings, inclusive interaction coverage, WCAG evidence. | Final acceptance; submit findings to Sparky. |
| `devops-automator` | Build automation, deployment, release mechanics, operational safety. | Release authorization; that belongs to Sparky. |

## Deterministic Handoff Chain

This is the required sequence every work packet must travel before it is considered accepted.

```
1. BRIEF         → product-manager produces scope, brief, and acceptance criteria
                 → delivers to delivery-director for routing

2. ROUTING       → delivery-director sequences work and assigns to the correct specialist(s)

3. IMPLEMENT     → specialist(s) execute (software-architect, backend-architect,
                   frontend-developer, ux-architect, ui-designer, mcp-integration-engineer,
                   devops-automator, seo-ai-discovery-strategist)

4. REVIEW        → code-reviewer produces evidence-backed review findings
                 → qa-evidence-collector produces proof artifacts (screenshots, test runs)
                 → accessibility-auditor produces accessibility evidence (where applicable)
                 → reality-checker produces a go/no-go recommendation with evidence

5. SPARKY GATE   → Sparky reviews all changed files and all evidence from step 4
                 → Sparky decides: ACCEPT / REFACTOR / REJECT
                 → REFACTOR or REJECT: Sparky specifies required corrections;
                   delivery-director re-routes back to the responsible specialist
                 → ACCEPT: work is considered done; Sparky hands to delivery-director
                   for release sequencing

6. RELEASE       → delivery-director sequences release window
                 → devops-automator executes release
                 → Sparky verifies post-release state before closing the packet
```

No step may be skipped. No specialist may self-accept their own work. Only Sparky may issue the final ACCEPT decision.

## Leadership Spine

- `sparky-chief-product-quality-officer` — final internal accept/reject/refactor authority; mandatory post-edit review gate; goal guardian; simplicity owner.
- `delivery-director` — sequencing, dependencies, and work-packet routing only; does not accept or reject work.
- `product-manager` — briefs, scope, and acceptance criteria only; does not make implementation or quality decisions.
- `software-architect` — technical direction and risk identification; submits architectural concerns to Sparky.

## Core Delivery Cells

- Product: `product-manager`
- Architecture: `software-architect`, `backend-architect`, `mcp-integration-engineer`
- UX/UI: `ux-architect`, `ui-designer`, `frontend-developer`
- Quality evidence: `code-reviewer`, `qa-evidence-collector`, `reality-checker`, `accessibility-auditor`
- Release and reach: `devops-automator`, `seo-ai-discovery-strategist`
