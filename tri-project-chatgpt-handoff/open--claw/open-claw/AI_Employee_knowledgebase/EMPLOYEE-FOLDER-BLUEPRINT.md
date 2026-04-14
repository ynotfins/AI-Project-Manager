# Employee Folder Blueprint

## Required Docs In Every Employee Folder
- `README.md`
- `PROVENANCE.md`
- `IDENTITY.md`
- `SOUL.md`
- `AGENTS.md`
- `TOOLS.md`
- `SKILLS.md`
- `WORKFLOWS.md`
- `MEMORY.md`
- `USER.md`
- `BOOTSTRAP.md`
- `HEARTBEAT.md`
- `SCHEDULE.md`
- `CHECKLIST.md`
- `AUDIT.md`

## Required Runtime Files For Live Workers
- `Dockerfile`
- `docker-compose.yml`
- `entrypoint.sh` when gateway bootstrap is needed
- `setup.sh`
- `.env.example`
- `package.json`
- `bot-telegram.js`
- `bot-discord.js`
- `bot-slack.js`
- `bot-whatsapp.js`
- `heartbeat.sh`

## Checklist Requirements
Every `CHECKLIST.md` must include:
- doc checklist
- runtime checklist
- skill checklist
- provenance checklist
- current completion status

## Audit Requirements
Every `AUDIT.md` must include:
- grade
- strengths
- missing pieces
- runtime readiness verdict
- next upgrade steps

## Rule
If an imported employee cannot satisfy this blueprint, keep only the worthwhile files and rebuild the rest.
