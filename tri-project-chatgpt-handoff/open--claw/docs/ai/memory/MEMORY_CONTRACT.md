# Memory Contract — Open Claw

## Non-negotiable: repo docs are source of truth

Repo docs win. Always.

- `FINAL_OUTPUT_PRODUCT.md` is read first.
- Repo authority docs come before operational evidence.
- `docs/ai/STATE.md`, `docs/ai/memory/DECISIONS.md`, and `docs/ai/memory/PATTERNS.md` are authoritative once the charter/authority gate is satisfied.
- Memory MCP tools provide **recall support only** — they do not override repo docs.
- If memory conflicts with repo docs, **repo docs win**. Update or discard the conflicting memory entry.

## Recovery order

1. `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`
2. The repo authority contract for the repo in scope
3. Targeted OpenMemory retrieval
4. Machine-local recovery bundle via `filesystem`, if present and current
5. `docs/ai/STATE.md` summary/current state section
6. Exactly one of `docs/ai/memory/DECISIONS.md`, `docs/ai/memory/PATTERNS.md`, or `docs/ai/HANDOFF.md` if needed
7. The execution ledger one block at a time only as a fallback

## Live OpenMemory reality

The current Cursor MCP surface is thin:

- `search-memories(query)`
- `list-memories()`
- `add-memory(content)`

Do not assume direct `project_id`, `namespace`, or `memory_types` filters unless a proven wrapper exists. Use compact self-identifying memory text instead.

## What to store in memory MCP

- Stable facts: tech stack, frameworks, naming conventions, base URLs (no secrets)
- Key decisions and their rationale
- Reusable patterns (code patterns, workflow patterns)
- Integration notes (what works, what doesn't, workarounds)
- Module interface contracts (from `open-claw/docs/MODULES.md`)

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
- [ ] Refresh the recovery bundle or record why it was deferred
- [ ] Record memory reseed debt if OpenMemory was degraded

### Before repeating a pattern
- [ ] Verify the pattern is still current (check memory + repo docs)
- [ ] If the pattern has changed, update memory and docs

## Persistence rules

- One observation per fact, concise (under ~120 characters)
- Present tense
- No secrets — store a pointer if a credential is needed (e.g., "API key in 1Password: OpenClaw/Key")
- Prefer compact self-identifying text such as `[repo=openclaw][kind=pattern][stability=durable][source=...] ...`
