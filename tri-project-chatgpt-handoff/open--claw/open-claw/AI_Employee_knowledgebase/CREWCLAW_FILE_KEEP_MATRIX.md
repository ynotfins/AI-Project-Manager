# CrewClaw File Keep Matrix

## Purpose
Decide which files from the purchased non-generic CrewClaw employee zips are worth keeping, even if they still need upgrades.

## Scope
Reviewed packet set:
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

The five generic `crewclaw-agent-deploy (12-16).zip` template packets are excluded.

## Summary Count
- **Worth keeping as distinct reusable artifacts:** `22`
- **Worth keeping only once as shared templates:** `16`
- **Worth keeping specifically from `software-engineer.zip`:** `6`
- **Worth keeping as specialist files from the other nine named packets:** `0`

This is a deduped count. The purchased set contains many repeated copies of the same starter files, so counting raw files across all zips would inflate the number without adding real value.

## Keep Once As Shared Templates
These files are worth keeping once as starter infrastructure or generic scaffolding:

### Runtime shell templates
- `Dockerfile`
- `docker-compose.yml`
- `package.json`
- `setup.sh`
- `.env.example`
- `README.md`
- `bot-telegram.js`
- `bot-discord.js`
- `bot-slack.js`
- `bot-whatsapp.js`
- `heartbeat.sh`

### Generic employee scaffolds
- `WORKFLOWS.md`
- `SCHEDULE.md`
- `MEMORY.md`
- `BOOTSTRAP.md`
- `USER.md`

## Keep Only From `software-engineer.zip`
These are the only purchased role files that rise above generic wrapper quality:
- `agents/software-engineer/SOUL.md`
- `agents/software-engineer/SKILLS.md`
- `agents/software-engineer/TOOLS.md`
- `agents/software-engineer/HEARTBEAT.md`
- `agents/software-engineer/AGENTS.md`
- `agents/software-engineer/IDENTITY.md`

## Discard From The Other Named Purchased Packets
For the remaining nine named purchased packets, these role-doc categories are not worth keeping as distinct specialist assets:
- `SOUL.md`
- `IDENTITY.md`
- `SKILLS.md`
- `TOOLS.md`
- `AGENTS.md`
- `HEARTBEAT.md`

Why they fail:
- most still identify as `Custom Role`
- most reuse the same generic "versatile AI employee" personality
- most expose the same generic skill bundle
- most reuse the same generic workflow templates
- most do not justify their specialist titles

## Employee-Level Verdicts
| Employee | Keep | Reason |
|---|---|---|
| `software-engineer.zip` | Partial keep | Best purchased packet; still incomplete, but contains the only role docs with real specialist value |
| `code-reviewer.zip` | Template-only keep | Label is useful, but internals are generic |
| `frontend-developer.zip` | Template-only keep | Label is useful, but internals are generic |
| `ux-designer.zip` | Template-only keep | Label is useful, but internals are generic |
| `seo-specialist.zip` | Template-only keep | Label is useful, but internals are generic |
| `api-integration-specialist.zip` | Template-only keep | Generic internals |
| `script-builder.zip` | Template-only keep | Generic internals |
| `personal-crm.zip` | Template-only keep | Generic internals |
| `overnight-coder.zip` | Template-only keep | Generic internals |
| `financial-analyst.zip` | Template-only keep | Generic internals |

## Practical Use
- Keep one shared runtime shell template from the purchased set.
- Keep the six `software-engineer` role files as salvageable reference material.
- Discard the duplicate role-specific files from the other nine named packets.
- Rebuild missing specialist files from higher-quality sources such as `agency-agents`, `awesome-openclaw-agents`, and the house standard.

## Replacement Sources For Weak Files
When a purchased file is discarded, replace it using this order:
1. `AI-EMPLOYEE-STANDARD.md`
2. `agency-agents` for specialist depth
3. OpenClaw official docs for file purpose and workspace conventions
4. `awesome-openclaw-agents` for OpenClaw-facing packaging and examples
5. `ocaudit` guidance for size, duplication, and context hygiene
