# Decisions Log

Record key decisions with rationale. One entry per decision.

## Entries

<!-- Format:

## <Date> — <Decision Title>

**Context:** What prompted this decision
**Decision:** What was chosen
**Alternatives considered:** What else was evaluated
**Rationale:** Why this was selected
-->

## 2026-02-23 — Phase 5 Closure: bws run is the standard Cursor launch path

**Context:** Phase 5 required wiring GITHUB_PERSONAL_ACCESS_TOKEN, FIRECRAWL_API_KEY, and
TWENTY_FIRST_API_KEY into their respective MCP servers without storing secrets in mcp.json.

**Decision:** `bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh start-cursor-with-secrets.ps1`
is the canonical and only supported way to launch Cursor on ChaosCentral. Cursor must not be
launched directly from taskbar/Start — always via the bws launch script.

**Alternatives considered:**
- Storing secrets directly in mcp.json (rejected: violates zero-trust policy)
- Using OS-level environment variables in .bashrc/.profile (rejected: persisted in plaintext on disk)
- Smithery hosted injection (rejected: Smithery HTTP 402 rate limit blocks reliability)

**Rationale:** bws run injects secrets only into the child process environment at runtime,
leaving no plaintext traces on disk or in version control. All 14 MCP servers receive their
credentials atomically at Cursor startup.

---

## 2026-02-23 — Phase 6 Decomposition: Split into 6A (architecture), 6B (gateway), 6C (integration)

**Context:** Phase 6 was originally a single monolithic goal ("Complete OpenClaw Build"). Upon
review, the prerequisite of `ANTHROPIC_API_KEY` injection is a human-only action (Bitwarden),
which blocks all Gateway-dependent work.

**Decision:** Phase 6 split into three sequential phases:
- 6A: Architecture Design (no external dependencies — can be done now)
- 6B: Gateway Boot (blocked on Tony: API key injection + secret rotation)
- 6C: First Live Integration (blocked on 6B)

**Alternatives considered:**
- Proceed with Gateway boot first (rejected: would fail without API key)
- Defer all Phase 6 work (rejected: architecture design has no blockers)

**Rationale:** Parallelizes work — architecture docs can be created and committed while Tony
completes Bitwarden actions in parallel. Reduces idle time.

---

## 2026-02-23 — open--claw Module Architecture: 8 Modules with Governance Overlay

**Context:** Phase 6A requires defining open--claw's module boundaries for safe autonomous
operation. Research from openclawlab.com official docs and community analyses (Bibek Poudel,
Raj Substack) confirmed OpenClaw's layered Gateway architecture.

**Decision:** 8 core modules defined:
Planner, Executor, Tool Router, Memory Engine, Code Generator, Deployment Engine, SEO Engine,
Finance Engine. AI-Project-Manager acts as the governance orchestrator; open--claw is the
executor. All High-risk actions require explicit human approval; Medium actions use notify +
30-min auto-approve timeout.

**Alternatives considered:**
- Fewer modules (4-5, merged domain engines): rejected for insufficient boundary clarity
- More modules (12+, split by tool): rejected as over-engineering for current scope

**Rationale:** 8 modules match OpenClaw's documented capability layers and align with the
three autonomy loops (App Builder, SEO Automation, Financial Management). Each module has a
clear risk level enabling precise governance gate placement.
