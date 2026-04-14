---
description: "Model routing policy for Open Claw: labels, thinking vs non-thinking, escalation"
globs: ["**/*"]
alwaysApply: true
---

# 15 — Model Routing (Open Claw)

> Extends: `10-project-workflow.md`
> Subordinate to: `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md` (supreme authority)

Routine delivery work does not stop to wait for user-confirmed model switches. The team escalates internally — AGENT may route to a stronger model or to Sparky without user confirmation. Tony approval is not required for model selection.

---

## Model Inventory

All model references must use these exact labels. No aliases, no abbreviations.

### Thinking-class models

These models perform extended internal reasoning before responding. Use for ambiguous,
high-stakes, multi-step, or architectural tasks where correctness matters more than speed.

- **GPT-5.2 High**
- **GPT-5.2 Extra High**
- **GPT-5.2 Codex High**
- **GPT-5.2 Codex High Fast**
- **GPT-5.2 Codex Fast**

### Non-thinking-class models

These models respond directly without extended reasoning. Use for implementation,
code generation, and execution tasks where the plan is already clear.

- **Sonnet 4.6**
- **Sonnet 4.5**
- **Sonnet 4**
- **Opus 4.6**
- **Opus 4.5**

### Fast utility models

Optimized for speed and low cost. Use for triage, summarization, compression,
and single-turn lookups where reasoning depth is not needed.

- **GPT-5.2 Fast**
- **GPT-5.2 Low**

---

## Mandatory Response Header

Every response in every tab must begin with this header block. No exceptions.

```
MODEL: <exact model label from inventory above>
CLASS: thinking-class | non-thinking-class | fast utility
TAB: PLAN | AGENT | DEBUG | ASK | ARCHIVE
DEFAULT FOR TAB: <default model label for this tab>
OVERRIDE: yes — <reason> | no
```

---

## Tab Defaults

| Tab | Default Model | Class |
|-----|--------------|-------|
| PLAN | GPT-5.2 High | thinking-class |
| AGENT | Sonnet 4.6 | non-thinking-class |
| DEBUG | GPT-5.2 High | thinking-class |
| ASK | GPT-5.2 Fast | fast utility |
| ARCHIVE | GPT-5.2 Low | fast utility |

**Rationale:**

- PLAN and DEBUG require deep reasoning to catch design flaws and root causes before any code is written or changed. Thinking-class models catch contradictions and edge cases that non-thinking models miss.
- AGENT executes a plan that has already been reasoned through. Non-thinking-class models are faster for straightforward implementation work.
- ASK and ARCHIVE handle lightweight single-turn lookups and compression where reasoning depth provides no benefit.

---

## Internal Escalation Rules

Model escalation is an internal delivery decision. AGENT does not stop and wait for the user to confirm a model switch — it escalates internally and continues.

### Rule A — AGENT Internal Escalation (no user stop required)

If AGENT encounters any of the following situations during delivery:

- Multi-module refactor (touching more than one module boundary)
- Any change touching auth, security, secrets, or credential handling
- Designing new architecture or routing
- Modifying rules or governance files (`.cursor/rules/`, `AGENTS.md`)
- Debugging nondeterministic failures (flaky tests, race conditions, intermittent errors)
- Any situation where the current reasoning depth is clearly insufficient

AGENT must:

1. **Record** the trigger in `docs/ai/STATE.md` (what triggered escalation and why)
2. **Route to Sparky** — delegate the problematic step to `sparky-chief-product-quality-officer` for resolution or re-planning
3. **Or self-escalate** — if routing to Sparky is not available in the current session, continue using a thinking-class model (GPT-5.2 Codex High) for the current step
4. **Continue delivery** — do not stop and wait for user confirmation of the model change

AGENT must record in the response header: `OVERRIDE: yes — <trigger reason>`.

AGENT must **not** halt the entire delivery pipeline waiting for a user to manually switch models. The team resolves model routing internally.

### Rule B — PLAN Internal Escalation (route internally; no user stop)

If PLAN is designing any of the following:

- Security boundaries or trust model
- Pricing or cost model decisions
- Multi-system integration design

PLAN should switch internally to GPT-5.2 Extra High and record `OVERRIDE: yes — <reason>` in the response header. PLAN does not ask the user to confirm this switch — it makes the decision and continues.

### Rule C — ASK Unresolved Turn Escalation (internal re-route at turn 3)

If ASK has not resolved a question within 2 turns, ASK must:

1. Record the escalation in its response
2. Produce a structured prompt for PLAN or Sparky to resolve with deeper reasoning
3. Hand off — do not continue spinning on the same question with the same model

---

## Sparky Routing

When a delivery problem exceeds AGENT's current model capacity or confidence, AGENT routes to Sparky rather than stopping for user input.

Sparky routing format (include in AGENT's response):

```
ROUTING TO SPARKY: <sparky-chief-product-quality-officer>
REASON: <one sentence — what exceeded AGENT's resolution capacity>
INPUT: <what Sparky needs to resolve this — specific question or decision>
EXPECTED OUTPUT: <what resolution AGENT needs to continue>
```

Sparky resolves internally and returns a decision. Delivery resumes without Tony involvement unless the decision touches a Tony-gate action.

---

## Tony-Gate Actions (still require Tony confirmation)

Model routing, escalation decisions, and Sparky delegation are **not** Tony-gate actions. The following are Tony-gate and still require Tony's explicit confirmation regardless of model or escalation state:

- Changing `FINAL_OUTPUT_PRODUCT.md`
- Issuing or revoking privileged credentials
- Irreversible external-world actions
- Redefining the product goal

See `AI-Project-Manager/docs/ai/architecture/GOVERNANCE_MODEL.md` for the full Tony-gate list.

---

## No Silent Degradation

If an escalation trigger occurs, AGENT must record it — in the response header and in `docs/ai/STATE.md`. Silently proceeding without recording the escalation event is a rule violation regardless of output quality. The record exists for Sparky's mandatory file-change review.
