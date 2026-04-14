# CrewClaw Purchased Employee Audit

## Scope
This audit covers the ten non-generic purchased CrewClaw employee zip files in `open-claw/employees/`:

- `api-integration-specialist.zip`
- `code-reviewer.zip`
- `financial-analyst.zip`
- `frontend-developer.zip`
- `overnight-coder.zip`
- `personal-crm.zip`
- `script-builder.zip`
- `seo-specialist.zip`
- `software-engineer.zip`
- `ux-designer.zip`

The five generic `crewclaw-agent-deploy (12-16).zip` template downloads are intentionally excluded from the ranking below.

## Method
- Inspected archive structure and required files across all ten purchased zips.
- Read role packet contents: `README.md`, `SOUL.md`, `SKILLS.md`, `TOOLS.md`, `WORKFLOWS.md`, `AGENTS.md`, `HEARTBEAT.md`, `MEMORY.md`, and `BOOTSTRAP.md`.
- Compared named packets for specialization depth, runtime completeness, workflow quality, and evidence of real differentiation.
- Checked the deploy shell (`Dockerfile`, `docker-compose.yml`, `.env.example`, `setup.sh`, bot entrypoints) for end-to-end consistency.

## Executive Verdict
No non-generic purchased CrewClaw employee is complete and thorough all the way through.

The best of the purchased set is `software-engineer.zip`, but even that packet is only the strongest relative to the others. It is not production-complete:
- its role docs are still shallow
- its workflows are generic monitoring/briefing templates instead of software-delivery workflows
- its runtime shell is outdated
- its Docker packaging is internally inconsistent

The rest of the named purchased employees are mostly thin role wrappers. Most of them reuse the same generic "Custom Role" identity, the same skill mix, the same tool list, the same workflow templates, and the same shallow bootstrap/memory scaffolding.

## Top Ranking
1. `software-engineer.zip`
   Reason: only purchased packet with a non-generic role identity, a role-specific tool list that includes code generation, and a slightly more detailed heartbeat.
2. `code-reviewer.zip`
   Reason: the name is useful, but the actual contents are still generic and not meaningfully better than the other wrapper roles.
3. `frontend-developer.zip`
   Reason: the label is useful for website work, but the internal packet does not actually support the label.
4. `ux-designer.zip`
   Reason: the label aligns with website work, but the content is generic and thin.
5. `seo-specialist.zip`
   Reason: useful label only; internals do not justify a specialist verdict.
6. `api-integration-specialist.zip`
7. `script-builder.zip`
8. `personal-crm.zip`
9. `overnight-coder.zip`
10. `financial-analyst.zip`

Ranks 2 through 10 are weakly separated. In practice, they mostly sit in the same low-quality tier, and the ordering is driven more by role usefulness for your goals than by packet quality.

## What Makes `software-engineer.zip` The Best
- `SOUL.md` uses a real role name (`Software Engineer`) instead of `Custom Role`.
- It has a more appropriate primary skill set: `Code Generation`, `Research`, `Data Analysis`.
- `TOOLS.md` includes code-generation usage rather than only browser-style research tasks.
- `HEARTBEAT.md` is slightly more detailed than the other purchased packets.

## Why `software-engineer.zip` Still Falls Short
- `SOUL.md` is still very short and generic for a true autonomous software engineer.
- `WORKFLOWS.md` contains generic "Morning Briefing / Escalation Workflow / End-of-Day Summary" sections instead of repo work, testing, review, debugging, and release flows.
- `README.md` is a generic deploy guide, not a role-specific operating manual.
- `Dockerfile` still uses `node:20-slim` and `npm install -g openclaw`, which matches the older broken packaging path already seen in runtime testing.
- `Dockerfile` tries to copy `bot.js`, but the archive does not include `bot.js`, which means the deploy artifact is internally inconsistent.

## Main Findings Across The Other Nine Named Packets
### 1. Role identity is mostly fake specialization
Most named purchased employees still say:
- `Role: Custom Role`
- "You are a versatile AI employee"
- generic behavior and generic rules

That means the packet name changed, but the internal identity usually did not become a real specialist.

### 2. Skills are mostly the same generic bundle
Most named purchased employees use the same active skills:
- `Research`
- `Summarization`
- `Data Analysis`
- `Web Search`

That is not enough to justify labels like frontend developer, UX designer, SEO specialist, or API integration specialist.

### 3. Tools are mostly the same generic bundle
Most named purchased employees expose the same tool ideas:
- browser research
- data analysis
- web search

They do not document concrete code, design-system, testing, API, or deployment toolchains specific to their titles.

### 4. Workflows are not specialist workflows
Most named purchased employees reuse the same templates:
- `Morning Briefing`
- `Escalation Workflow`
- `End-of-Day Summary`

Those are generic monitor/ops patterns, not specialist execution playbooks.

### 5. Heartbeat and memory files are shallow
Most named purchased employees have:
- a thin `HEARTBEAT.md`
- a placeholder `MEMORY.md`
- a simple `BOOTSTRAP.md`

They read like starter templates, not mature autonomous employees with deep operating discipline.

### 6. Runtime packaging is not fully solid
Shared runtime issues found in the purchased packets:
- outdated `node:20-slim` base image
- `npm install -g openclaw` packaging path
- generic multi-platform shell not tied to proven project workflows
- `Dockerfile` references `bot.js`, but `bot.js` is missing from the archive

This means even the better packets do not qualify as fully complete end-to-end deploy artifacts.

## Per-Employee Notes
### `software-engineer.zip`
- Strongest packet in the purchased set.
- Only one with clearly better role identity and code-oriented tooling.
- Still incomplete and too shallow for autonomous production software delivery.

### `code-reviewer.zip`
- Name is promising, but internals still say `Custom Role`.
- No evidence of a real code-review rubric, diff review process, bug-risk framework, or approval gate.
- Better treated as a renamed generic agent than a true review specialist.

### `frontend-developer.zip`
- Good title for your goals.
- Internals do not mention App Router, design systems, accessibility, component architecture, browser verification, or testing depth.
- Not a real frontend specialist yet.

### `ux-designer.zip`
- Good title for your goals.
- Internals do not provide UX audit methods, information architecture workflows, research synthesis, wireframing, accessibility heuristics, or design handoff discipline.
- Not a real UX specialist yet.

### `seo-specialist.zip`
- Good title for your goals.
- Internals do not provide metadata workflows, keyword strategy, schema, crawl audits, or content optimization plans.
- Not a real SEO specialist yet.

### `api-integration-specialist.zip`
- Role label suggests backend integration strength.
- Internals do not show API contract thinking, auth handling, retry/failure policy, schema mapping, or integration test workflows.
- Mostly a generic wrapper.

### `script-builder.zip`
- Name suggests automation usefulness.
- Internals do not provide scripting standards, validation, testing, CLI safety rules, or environment discipline.
- Mostly a generic wrapper.

### `personal-crm.zip`
- Role is outside your current website-squad priority.
- Internals are still generic and not strong enough to count as a solid CRM operator.

### `overnight-coder.zip`
- Interesting label, weak internals.
- No meaningful autonomous coding workflow beyond the generic template.

### `financial-analyst.zip`
- Role is outside your current delivery priority.
- Internals are generic and do not show real finance-specific rigor.

## Best Answer To Your Question
Are any of the non-generic CrewClaw purchased employees complete and solid all the way through the way they should be?

No.

Is any one of them the best?

Yes: `software-engineer.zip` is the best of the purchased non-generic CrewClaw employees.

Is it complete and thorough?

No. It is better than the others, but still not at the level it should be for a fully developed autonomous software employee.

## Recommendation
- Treat `software-engineer.zip` as the best raw starting point from the purchased CrewClaw set.
- Treat `frontend-developer.zip`, `ux-designer.zip`, `seo-specialist.zip`, and `code-reviewer.zip` as useful labels only, not trustworthy finished specialists.
- Use the curated house standard in `AI_Employee_knowledgebase` as the real source of truth going forward.
- If you want live workers, rebuild the website squad from the curated packets instead of trusting the purchased CrewClaw packets as-is.
