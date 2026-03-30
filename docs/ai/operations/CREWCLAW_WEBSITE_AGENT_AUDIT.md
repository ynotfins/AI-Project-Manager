# CrewClaw Website Agent Audit

## Executive Summary

This audit focused on whether the current CrewClaw employee packages are ready to help clone and rebrand a Next.js website.

### Headline findings

- The five `generic` downloads are not five different specialists. They are five identical `My Agent` template packages.
- All CrewClaw ZIP packages currently share a packaging defect: their `Dockerfile` tries to `COPY bot.js`, but the packages contain `bot-telegram.js` instead.
- The current named employee packages are structurally complete, but most of them are role-thin. Their names suggest specialization, but their actual `SOUL.md`, `TOOLS.md`, and `SKILLS.md` content is mostly generic.
- `software-engineer` is the only current package that is meaningfully closer to a real implementation worker.
- The older shared deployed workers still route Telegram traffic to `main` in their bot wrapper. The newer deployed workers route to their own agent IDs.
- The editor/tooling surface on this machine is decent for a Next.js workflow. The biggest gaps are in employee package specialization, not in Cursor itself.

## PASS / FAIL Summary

| Check | Result | Notes |
| --- | --- | --- |
| Core package structure present | PASS | Named and generic CrewClaw ZIPs include `README.md`, `Dockerfile`, `docker-compose.yml`, `heartbeat.sh`, `setup.sh`, `package.json`, bot files, and the full agent-doc set. |
| ZIP Dockerfile integrity | FAIL | All audited CrewClaw ZIPs reference missing `bot.js` instead of `bot-telegram.js`. |
| Generic ZIP uniqueness | FAIL | `crewclaw-agent-deploy (12)` through `(16)` are identical `My Agent` template packages. |
| Role specificity across named employees | FAIL | 9 of the 10 named employee packages are mostly generic in skills, tools, and behavior. |
| Website-clone readiness today | PARTIAL | `software-engineer` is usable as a foundation; the broader website team still needs specialization. |
| Cursor extension baseline | PASS | ESLint, Prettier, Tailwind CSS, Docker, GitLens, markdownlint, Python, PowerShell, YAML, Error Lens, and others are installed. |
| Playwright editor support | PASS | `ms-playwright.playwright` was installed during this audit. |
| GitHub Copilot install via Cursor CLI | FAIL | Standard extension IDs were not found through the current Cursor CLI marketplace path. |

## Current Website Squad Recommendation

Use this as the initial website-clone squad:

- `software-engineer`: lead implementation worker for clone/rebrand
- `frontend-developer`: secondary UI worker, but only after re-specialization
- `ux-designer`: design review / layout guidance, but only after re-specialization
- `code-reviewer`: review gate
- `seo-specialist`: later-stage metadata, copy, and SEO cleanup
- `api-integration-specialist`: later-stage forms / integrations / APIs

Do not use these as primary website workers yet:

- `financial-analyst`
- `personal-crm`
- `overnight-coder` as currently defined
- any of the five generic `My Agent` downloads

## Tooling Audit

### Installed editor extensions that already help

- `dbaeumer.vscode-eslint`
- `esbenp.prettier-vscode`
- `bradlc.vscode-tailwindcss`
- `ms-azuretools.vscode-docker`
- `eamodio.gitlens`
- `davidanson.vscode-markdownlint`
- `redhat.vscode-yaml`
- `usernamehw.errorlens`
- `christian-kohler.path-intellisense`
- `anysphere.remote-wsl`
- `mem0.openmemory`

### Added during this audit

- `ms-playwright.playwright`

### Attempted but blocked

- `GitHub.copilot`
- `GitHub.copilot-chat`

The Cursor CLI reported those extension IDs as not found in the available marketplace path, so Copilot is still not available from this audit pass.

## Agent Skill Surface Available In This Environment

The current agent environment already exposes useful high-level skills for a Next.js workflow, including:

- `nextjs`
- `shadcn`
- `agent-browser`
- `agent-browser-verify`
- `react-best-practices`
- `check-compiler-errors`
- `run-smoke-tests`
- `fix-ci`
- `next-upgrade`
- `turbopack`
- `turborepo`
- `vercel-cli`
- deployment / performance / observability skills
- Context7 documentation access

Conclusion: the machine-level skill surface is already strong enough. The weak point is the employee package definitions.

## What The Employee Packages Are Missing For A Next.js Rebrand Workflow

Most employee packages are missing one or more of these critical pieces:

- explicit Next.js App Router knowledge in the employee docs
- explicit React / TypeScript / Tailwind / CSS theming responsibilities
- a documented clone-and-rebrand workflow
- browser-based visual QA instructions
- screenshot comparison / manual verification steps
- git clone / branch / commit workflow instructions
- direct access / usage guidance for the Windows node and Cursor tooling
- per-role acceptance criteria
- tests and build verification instructions for Next.js
- structurally correct ZIP Dockerfiles

## Current Routing Reality

There are two routing patterns in the current deployed workers:

### Older shared workers

These currently route messages to `main` in the Telegram wrapper:

- `api-integration-specialist`
- `code-reviewer`
- `financial-analyst`
- `frontend-developer`
- `overnight-coder`

### Newer direct-routed workers

These route to their own agent IDs in `bot-telegram.js`:

- `personal-crm`
- `script-builder`
- `seo-specialist`
- `software-engineer`
- `ux-designer`

This means the current worker naming does not always equal true isolated specialist behavior at runtime.

## Framework Guidance

Current Next.js guidance from the official docs confirms these important rebrand points:

- App Router metadata should be managed via the `metadata` export.
- Metadata files like `favicon.ico` and `icon.png` can be handled via the app directory conventions.
- Global styles belong in the root layout import path.
- Browser-exposed env vars must use the `NEXT_PUBLIC_` prefix.

That aligns with the website-clone workflow we want: first clone and rebrand metadata, assets, colors, and contact info, then replace images and finish content migration.

## Recommended Next Steps

1. Use `software-engineer` as the first real website-clone worker.
2. Re-specialize `frontend-developer`, `ux-designer`, `seo-specialist`, and `code-reviewer` before trusting them with autonomous work.
3. Fix the ZIP packaging defect at the source so future CrewClaw downloads are deployable without manual patching.
4. Rebuild or re-download the five generic portal agents only after their names, roles, skills, and rules are actually filled in.
5. Add explicit website-clone instructions to the employee docs: clone repo, rename brand, update contact data, update colors, run build/tests, produce review notes.

## Follow-On Buildout Completed

The follow-on standardization pass was completed in `open--claw/open-claw/AI_Employee_knowledgebase`.

### What now exists

- a repo-tracked `AUTHORITATIVE_STANDARD.md` that defines the local source of truth instead of trusting any single upstream repo
- a curated 15-employee development team under `open--claw/open-claw/AI_Employee_knowledgebase/AI_employees`
- zipped portable employee packets for all 15 curated employees under `open--claw/open-claw/AI_Employee_knowledgebase/AI_employees/_zips`
- a copied reference-asset library with the strongest source role files, CI patterns, runtime templates, and prompt patterns
- 10 new tracked development skills under `open--claw/open-claw/skills` covering Next.js App Router, Playwright, visual QA, ADRs, release gates, MCP integration, and handoff discipline

### Authoritative roster

- `sparky-chief-product-quality-officer`
- `delivery-director`
- `product-manager`
- `software-architect`
- `frontend-developer`
- `backend-architect`
- `ux-architect`
- `ui-designer`
- `code-reviewer`
- `qa-evidence-collector`
- `reality-checker`
- `devops-automator`
- `accessibility-auditor`
- `seo-ai-discovery-strategist`
- `mcp-integration-engineer`

### Current limitation

This new library is the curated standard, but it has not yet been wired back into the currently deployed CrewClaw runtime workers. The old downloaded CrewClaw ZIPs still exist as raw source material; the new tracked knowledgebase is the better source of truth for future specialization and packaging.
