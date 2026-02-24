# Memory Contract

## Non-negotiable: repo docs are source of truth

Repo docs win. Always.

- `docs/ai/STATE.md`, `docs/ai/memory/DECISIONS.md`, and `docs/ai/memory/PATTERNS.md` are authoritative.
- Memory MCP tools provide **recall support only** — they do not override repo docs.
- If memory conflicts with repo docs, **repo docs win**. Update or discard the conflicting memory entry.

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
