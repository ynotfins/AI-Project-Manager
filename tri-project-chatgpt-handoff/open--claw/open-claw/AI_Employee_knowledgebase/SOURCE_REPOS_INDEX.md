# Source Repos Index

## Purpose
Provide a durable index of the local upstream employee/skill sources that inform the curated OpenClaw packets.

## Important Constraint
`source_repos/` is local research material and is not the authoritative runtime surface. The deployable surface remains:
- `AI_employees/`
- `reference_assets/`
- `open-claw/skills/`

Some upstream trees are local-only or gitignored, so this index is built from the tracked repo docs and visible top-level source folders rather than assuming every upstream file is always present in git.

## Top-Level Sources

| Source | Purpose | Reuse Mode |
| --- | --- | --- |
| `agency-agents` | Best role-definition depth for specialist employee profiles. | Promote selected role ideas into curated packets only. |
| `awesome-openclaw-agents` | Best packaged OpenClaw worker examples and runtime-facing folder patterns. | Salvage packaging and tool-usage patterns. |
| `agent-factory` | Coordination, communications, and agent-operating patterns. | Salvage operational doctrine into `reference_assets/operations/`. |
| `autogen` | Automation and orchestration examples. | Salvage CI/integration patterns. |
| `awesome-ai-organization` | Broader organizational/team ideas. | Research only until explicitly promoted. |
| `calfkit-sdk` | Tooling/integration reference material. | Research only. |
| `cursor-starter` | Starter prompts and implementation flows for CI, integration, and testing. | Salvage prompt patterns. |
| `openclaw-android` | Android-specific OpenClaw-adjacent work. | Research only unless promoted. |
| `openlabor` | Agent/workflow experimentation. | Research only. |
| `plumoai` | External AI workflow examples. | Research only. |
| `PraisonAI` | CI and orchestration reference assets. | Salvage CI patterns. |
| `Startup-Agents` | Startup/operator-style agent references. | Research only unless promoted. |

## Reusable Categories

### Employee role depth
- `agency-agents` is the strongest source for role-specific prose and specialist boundaries.
- Best direct fits for the curated squad are product, architecture, engineering, testing, integrations, marketing, support, and specialized roles.

### Runtime packaging
- `awesome-openclaw-agents` remains the strongest reference for OpenClaw-shaped folder and runtime patterns.

### Proactive operating doctrine
- The curated packets already depend on proactive operating patterns mirrored into `reference_assets/runtime_templates/`.

### CI and prompt patterns
- `cursor-starter`, `PraisonAI`, and `autogen` are the main sources for reusable CI/testing/prompt assets.

## Highest-Value Reuse Targets

| Curated role | Highest-value upstream reuse |
| --- | --- |
| `product-manager` | agency-agents product role profiles |
| `backend-architect` | agency-agents engineering backend architect references |
| `software-architect` | architecture/runtime packaging from awesome-openclaw-agents plus agency engineering roles |
| `mcp-integration-engineer` | integration/specialized source profiles and MCP-oriented tooling patterns |
| `qa-evidence-collector`, `reality-checker`, `accessibility-auditor` | testing-oriented agency profiles plus CI/evidence patterns |
| `devops-automator` | CI/orchestration patterns from PraisonAI and autogen |
| `seo-ai-discovery-strategist` | marketing/discovery-oriented agency roles and prompt assets |

## Deployment Gaps
- Upstream source trees are not the runtime; promoted content still needs:
  - `CHECKLIST.md`
  - `AUDIT.md`
  - current `TOOLS.md`
  - current `SKILLS.md`
  - OpenClaw runtime shell validation
- Quarantined or raw imported content must not be routed directly into the active team without explicit promotion.
- Live deployment still depends on worker tokens, channel bindings, gateway pairing, and smoke tests.

## Recommendation
- Use `source_repos/` as a mining ground, not a live routing surface.
- Promote only high-value role definitions or skill ideas into:
  - `AI_employees/`
  - `reference_assets/`
  - `open-claw/skills/`
- Keep a follow-up task for deeper per-file indexing if the full local mirrors are needed for another import wave.
