# Memory Contract

## Non-negotiable: repo docs are source of truth

Repo docs win. Always.

- `docs/ai/STATE.md` is the **primary operational source of truth** for PLAN. Read it first before consulting any other source.
- `docs/ai/memory/DECISIONS.md` and `docs/ai/memory/PATTERNS.md` are authoritative for decisions and patterns.
- Memory MCP tools provide **recall support only** — they do not override repo docs.
- If memory conflicts with repo docs, **repo docs win**. Update or discard the conflicting memory entry.
- `docs/ai/context/` is non-canonical artifact storage (session dumps, transcript extracts). Informative only.
- `docs/ai/context/AGENT_EXECUTION_LEDGER.md` is a **non-canonical** verbatim execution record. It is informative only. PLAN/DEBUG must NOT load it by default. Consult only when STATE.md, DECISIONS.md, PATTERNS.md, and HANDOFF.md are insufficient — and only the specific block(s) needed. AGENT must append one entry after every completed prompt block.
- `@Past Chats` is a **last resort** — consult only after `STATE.md`, `DECISIONS.md`, `PATTERNS.md`, and `docs/ai/context/` are insufficient.

### Context source priority

1. `docs/ai/STATE.md`
2. `docs/ai/memory/DECISIONS.md`
3. `docs/ai/memory/PATTERNS.md`
4. `docs/ai/operations/PROJECT_LONGTERM_AWARENESS.md`
5. `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md`
6. `docs/ai/context/`
7. `@Past Chats` (last resort)

## What to store in memory MCP

- Stable facts: tech stack, frameworks, naming conventions, base URLs (no secrets)
- Key decisions and their rationale
- Reusable patterns (code patterns, workflow patterns)
- Integration notes (what works, what doesn't, workarounds)

## What must NEVER be stored

- Secrets, tokens, API keys, credentials, or service-account JSON
- Personal data (emails, phone numbers, addresses)
- Large code blocks (store a file path reference instead)
- Transient brainstorming (keep in ASK tab or discard)
- Anything that duplicates repo docs verbatim

## Retrieve-before-plan / store-after-phase checklist

### Before planning (REQUIRED)

- [ ] Search memory for prior decisions related to the current task
- [ ] Check `docs/ai/memory/DECISIONS.md` for relevant precedents
- [ ] Check `docs/ai/memory/PATTERNS.md` for applicable patterns
- [ ] If memory conflicts with repo docs, discard the memory entry

### After completing a phase (REQUIRED)

- [ ] Store new decisions in memory and in `docs/ai/memory/DECISIONS.md`
- [ ] Store new patterns in memory and in `docs/ai/memory/PATTERNS.md`
- [ ] Verify stored facts are concise (under ~120 characters each)
- [ ] Verify no secrets or personal data were stored

### Before repeating a pattern

- [ ] Verify the pattern is still current (check memory + repo docs)
- [ ] If the pattern has changed, update memory and docs

## Persistence rules

- One observation per fact, concise (under ~120 characters)
- Present tense
- No secrets — store a pointer if a credential is needed (e.g., "API key in 1Password: Project/Key")

## Context-window hygiene

- Follow `docs/ai/operations/CONTEXT_WINDOW_MONITORING.md` guardrails.
- If `STATE.md` or preload docs exceed warn thresholds, archive before adding new large blocks.
- Keep memory entries atomic and non-duplicative to reduce retrieval noise.
