# OpenClaw Workflow Checklist

## Packet Standard
- [x] The curated library has 15 employees.
- [x] Every employee packet includes the required docs.
- [x] Every employee packet now includes the required runtime files.
- [x] Every employee packet includes copied assigned skills under `skills/`.
- [x] Every employee packet zip was regenerated after runtime sync.

## Runtime Shape
- [x] A generated runtime exists at `open-claw/employees/deployed-curated/`.
- [x] The generated runtime includes a 14-service `docker-compose.yml` for the dockerized worker pool.
- [x] `SPARKY_CEO_BOT` is intentionally excluded from the Docker worker pool and remains the host-native executive runtime.
- [x] The generated runtime includes `start-employees.ps1` with env-first plus Bitwarden fallback secret resolution and partial-start capability.
- [x] Each worker uses the proven remote-gateway shell pattern: Node 22 + pinned `openclaw@2026.3.13` + entrypoint-generated config.
- [x] A machine-readable readiness snapshot is generated for the curated squad.

## Skill Activation
- [x] Assigned skills are present in every employee packet.
- [x] Assigned skills are copied into each packet's runtime payload.
- [x] Employee packets reference only real tracked skill slugs.

## Validation
- [x] Structural validation script available.
- Existing Telegram bot assignments are defined for **15** curated workers.
- Direct Bitwarden worker token IDs are wired for **15** curated workers.
- Assigned workers still needing explicit `*_TOKEN` env vars or Bitwarden secret IDs recorded: none.
- Curated workers still waiting on brand-new Telegram bots: none.
- First-run device pairing still must be approved against the real gateway.
- End-to-end live message tests still depend on gateway reachability and real bot credentials.

## Employee Coverage
- [x] `ACCESS_AUDITOR_ALLISON_BOT` packet generated and runtime-synced
- [x] `BACKEND_BRUCE_BOT` packet generated and runtime-synced
- [x] `CODE_CARL_BOT` packet generated and runtime-synced
- [x] `DELIVERY_DIRECTOR_DAN_BOT` packet generated and runtime-synced
- [x] `SCRIPT_SARAH_BOT` packet generated and runtime-synced
- [x] `FRONTEND_FELIX_BOT` packet generated and runtime-synced
- [x] `API_ANDY_BOT` packet generated and runtime-synced
- [x] `PRODUCT_MANAGER_PETE_BOT` packet generated and runtime-synced
- [x] `OVERNIGHT_OLIVER_BOT` packet generated and runtime-synced
- [x] `FINANCE_FRANKY_BOT` packet generated and runtime-synced
- [x] `SEO_SAMANTHA_BOT` packet generated and runtime-synced
- [x] `ENGINEER_ENRIQUE_BOT` packet generated and runtime-synced
- [x] `SPARKY_CEO_BOT` packet generated and runtime-synced
- [x] `PERSONAL_PAMELA_BOT` packet generated and runtime-synced
- [x] `UX_URSELA_BOT` packet generated and runtime-synced
