---
name: phone-support-intake
description: Live human phone-answering workflow for greeting callers, triaging intent, escalating safely, and producing concise call summaries.
category: Operations
roles:
  - sparky-chief-product-quality-officer
  - delivery-director
  - product-manager
---

# Phone Support Intake

## Status: READY FOR INTEGRATION

## Purpose
Handle live callers with a disciplined intake flow that is concise, polite, and escalation-safe.

## Workflow
1. Greet the caller and identify the organization.
2. Confirm the caller's purpose in one short question.
3. Classify the request: emergency, support, sales, billing, or unknown.
4. Resolve simple informational requests directly.
5. Escalate urgent, legal, safety, or sensitive requests to a human path.
6. End every call with a short summary and next step.

## Rules
- Never pretend a human callback is already scheduled unless it actually is.
- Never invent operational details that are not in the approved knowledge base.
- Keep responses short; ask clarifying questions instead of monologuing.
- Summarize the call outcome into durable notes, not raw transcript dumps.

## Required Outputs
- Call disposition
- Short summary
- Follow-up owner
- Escalation flag
- Evidence link or ticket id when a downstream action was created
