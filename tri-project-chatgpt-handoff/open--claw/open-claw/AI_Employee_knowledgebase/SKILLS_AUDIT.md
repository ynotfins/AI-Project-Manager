# Skills Audit

## Existing Tracked Skills Before This Pass
- `approval-gate`
- `domain-email`
- `gmail-inbox`
- `google-calendar`
- `google-contacts`
- `mem0-bridge`
- `sms-twilio`
- `whatsapp-official`

## Added Development Skills
| Skill | Description | Primary Roles |
|---|---|---|
| `nextjs-app-router` | Production Next.js App Router workflow for modern websites and apps with metadata, server/client boundaries, and build verification. | frontend-developer, ux-architect, seo-ai-discovery-strategist, sparky-chief-product-quality-officer |
| `design-token-theming` | Design token and theming system for light, dark, and system modes with accessible, reusable UI primitives. | ux-architect, ui-designer, frontend-developer, accessibility-auditor |
| `playwright-e2e` | Production-grade Playwright workflow for end-to-end testing with retries, traces, web-first assertions, and CI artifacts. | frontend-developer, qa-evidence-collector, reality-checker, devops-automator, accessibility-auditor |
| `visual-qa-evidence` | Evidence-first QA process for screenshots, responsive coverage, dark mode, and issue reports tied to visual proof. | qa-evidence-collector, reality-checker, ui-designer, frontend-developer |
| `architecture-adr` | Architecture decision record workflow for design choices, trade-offs, rollback paths, and modular boundaries. | software-architect, backend-architect, sparky-chief-product-quality-officer, code-reviewer, mcp-integration-engineer |
| `code-review-gate` | High-signal review gate for correctness, security, maintainability, testing, and performance. | code-reviewer, sparky-chief-product-quality-officer, software-architect |
| `release-readiness` | Release gate for build verification, regression evidence, rollback planning, and final go/no-go decisions. | devops-automator, reality-checker, qa-evidence-collector, sparky-chief-product-quality-officer |
| `repo-clone-rebrand` | Workflow for cloning an existing site/app, changing brand identity, contact details, theme, and proofing the result safely. | product-manager, delivery-director, frontend-developer, seo-ai-discovery-strategist |
| `mcp-integration` | Pattern for designing and validating MCP integrations with typed parameters, descriptive tools, and graceful failure handling. | mcp-integration-engineer, backend-architect, software-architect |
| `handoff-state` | Shared operating pattern for documenting current state, evidence, blockers, and next actions between employees. | sparky-chief-product-quality-officer, delivery-director, product-manager, code-reviewer, qa-evidence-collector, reality-checker |
| `twilio-voice-intake` | Twilio Voice intake workflow for inbound phone calls, TwiML entrypoints, streaming/relay setup, and safe real-time call routing. | sparky-chief-product-quality-officer, delivery-director, product-manager, backend-architect, mcp-integration-engineer |
| `elevenlabs-voice-clone` | ElevenLabs voice-cloning and conversational voice configuration workflow for branded live-call voices. | sparky-chief-product-quality-officer, product-manager, backend-architect, mcp-integration-engineer |
| `phone-support-intake` | Short, escalation-safe call-handling workflow for live humans with summaries and follow-up routing. | sparky-chief-product-quality-officer, delivery-director, product-manager |
| `video-repair-forensics` | Evidence-first workflow for triaging and salvaging damaged video files with copy-first recovery before re-encode fallback. | sparky-chief-product-quality-officer |
| `media-recovery-validation` | Validation workflow for proving whether a repaired media file is truly fixed, partially salvaged, or still corrupt. | sparky-chief-product-quality-officer |

## Audit Verdict
The repo now has both the original communication/approval primitives and the curated software-delivery layer, plus dedicated media-recovery skills for Sparky's damaged-video repair workload.

## Current Runtime Status
- Tracked skill folders present in `open-claw/skills/`: **23**
- Communication and approval skills tracked: **8**
- Curated delivery/recovery skills assigned to the 15-employee roster: **15**
- The assigned curated skills are copied into each employee packet under `AI_employees/<employee>/skills/`.
- Structural validation is complete: the generated runtime packets, copied skill files, Docker Compose, PowerShell startup surface, and generated worker scripts all pass repo-side validation.
- Live skill invocation is **still not fully proven** for the generated curated runtime because 3 already-assigned workers still need direct secret mapping or stable env-backed injection, and the generated workers have not yet completed end-to-end gateway smoke tests.
