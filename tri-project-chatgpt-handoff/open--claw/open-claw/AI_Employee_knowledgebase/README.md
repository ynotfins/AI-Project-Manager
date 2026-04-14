# AI Employee Knowledgebase

This directory is the curated, repo-tracked source of truth for the development team library built on 2026-03-30. It captures the **product charter**, the house standard, the roster, copied high-value references, and portable employee packets.

## Authority order (every employee, every session)
1. **`FINAL_OUTPUT_PRODUCT.md`** — supreme product charter; read first; nothing overrides it.
2. **Tony’s explicit permission** to change that file.
3. **`AUTHORITATIVE_STANDARD.md`** and **`TEAM_ROSTER.md`** — interpret the charter and org structure; they must not contradict or override it.
4. **`AI-EMPLOYEE-STANDARD.md`** and everything under `AI_employees/` — subordinate packet and layout rules derived from the above.
5. Upstream research under `source_repos/` — not authoritative on its own.

## Folder Map
- `AI_employees/` — curated employee folders plus `_zips/` with portable employee packet archives.
- `candidate_employees/agency-agents/` — **QUARANTINED. NON-ROUTABLE — OUT OF SCOPE.** Standardized packet wrappers for the imported agency-agents role library. 2,608 files. Do not read, search, route through, or recall from memory. See `NON_ROUTABLE_QUARANTINE.md`.
- `employee_audits/` — repeatable audit notes for curated employees and readiness planning.
- `reference_assets/` — copied high-signal upstream files and examples worth keeping.
- `FINAL_OUTPUT_PRODUCT.md` — supreme charter; every employee reads this first.
- `AI-EMPLOYEE-STANDARD.md` — required packet layout and quality model (subordinate to the charter).
- `EMPLOYEE-FOLDER-BLUEPRINT.md` — exact docs and runtime files each employee folder must carry.
- `AGENCY_IMPORT_SUMMARY.md` — import counts, category coverage, and grades for the agency-agents library.
- `SOURCE_LIBRARY_CATALOG.md` — ranked source repos and what was actually kept from each.
- `OPENCLAW_WORKFLOW_CHECKLIST.md` — current checklist for the curated 15-employee OpenClaw runtime workflow.
- `TEAM_OPERATING_SYSTEM.md` — operating model for Sparky plus the 15 curated workers: pods, handoff chain, readiness states, and activation order.
- `VOICE_FRONT_DESK_STACK.md` — standalone phone/voice worker architecture using Twilio Voice plus ElevenLabs without breaking the curated 15-worker runtime.
- `SOURCE_REPOS_INDEX.md` — durable index of upstream source libraries, reuse categories, and deployment gaps.
- `SPARKY_REPLACEMENT_AUDIT.md` — verdict on whether `temp/Sparky` should replace the curated Sparky packet (current answer: merge, not replace).
- `CURATED_TEAM_STATUS.json` — generated machine-readable readiness snapshot for the curated squad.
- `MEMORY_PROMOTION_TEMPLATE.md` — compact template for promoting validated worker outputs into durable memory.
- `RUNTIME_VALIDATION_SUMMARY.md` — latest PASS/FAIL validation report for packet completeness and generated runtime wiring.
- `current_employees.md` — current employee status board with Telegram mapping, packet readiness, skills, and per-file ratings.
- `AUTHORITATIVE_STANDARD.md` — house standard; interprets the charter; must not override it.
- `TEAM_ROSTER.md` — hierarchy and responsibilities; subordinate to the charter.
- `PROVENANCE_MATRIX.md` — where each employee packet came from.
- `SKILLS_AUDIT.md` — tracked skill inventory and what was added.
- `EMPLOYEE_READINESS_AUDIT.md` — current verdict on curated packets vs legacy purchased packets.
- `NON_ROUTABLE_QUARANTINE.md` — **canonical quarantine registry** for the entire tri-workspace. Defines which paths are excluded from search, routing, memory, and embeddings, and the promotion gate to lift quarantine.

## Quarantine Notice

`candidate_employees/**` is quarantined as of 2026-04-01. All 2,608 files in that directory carry the `<!-- NON-ROUTABLE — OUT OF SCOPE -->` banner. Agents must not read, reference, route through, search, or store to memory any content from that directory. The canonical quarantine registry and promotion gate are in `NON_ROUTABLE_QUARANTINE.md`. Enforcement rules are in `.cursor/rules/02-non-routable-exclusions.md`.

## Notes
- `source_repos/` is local research material and not the authoritative tracked standard.
- The charter (`FINAL_OUTPUT_PRODUCT.md`) is supreme; curated files in this folder apply only insofar as they align with it.
- Current curated-runtime status: all 15 curated employee packets are runtime-synced and structurally validated; all 15 curated workers now have Telegram assignments, all 15 are wired to direct Bitwarden secret IDs, and first-run device pairing is still pending before live smoke validation.
