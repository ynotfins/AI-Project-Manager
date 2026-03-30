# CrewClaw Employee Install Runbook

## Purpose

This runbook documents the practical steps to prepare, activate, verify, and later deactivate CrewClaw employees for this workspace.

It is designed for the current local setup:

- Runtime repo: `D:\github\open--claw`
- Employee package root: `D:\github\open--claw\open-claw\employees`
- Shared deployed worker root: `D:\github\open--claw\open-claw\employees\deployed`
- Gateway host: local OpenClaw gateway on the same machine / WSL2 environment
- Secret source of truth: Bitwarden

This document does **not** store any raw runtime secrets or monitor keys.

## CrewClaw-Only `.env` Exception

For CrewClaw employees only, local untracked `.env` files are allowed for:

- `CREWCLAW_MONITOR_KEY`

This exception exists because the CrewClaw portal / `monitor.sh` flow is built around writing the monitor key locally so `heartbeat.sh` can ping the dashboard.

This exception does **not** apply to:

- Telegram bot tokens
- gateway tokens
- provider API keys
- any other runtime secret

Those remain Bitwarden-only secrets and should continue to be injected at runtime.

## Current Package Inventory

### Shared deployed workers

These already exist as unpacked folders under `open-claw/employees/deployed` and are wired into the current shared deployment:

- `api-integration-specialist`
- `code-reviewer`
- `financial-analyst`
- `frontend-developer`
- `overnight-coder`

### Additional prepared ZIP packages

These are present under `open-claw/employees` and are ready to be unpacked into working folders:

- `personal-crm.zip`
- `script-builder.zip`
- `seo-specialist.zip`
- `software-engineer.zip`
- `ux-designer.zip`

### Other archive files in the folder

These exist but are not part of the immediate 10-worker Telegram deployment plan:

- `crewclaw-anthony-bundle.zip`
- `awesome-openclaw-agents-main.zip`

## Known Package Issues

- All audited CrewClaw ZIP packages currently ship with a broken `Dockerfile` reference to `bot.js` even though the packages contain `bot-telegram.js`.
- The five downloaded generic packages in `employees/generic` are identical `My Agent` templates, not five distinct specialists.
- Most named employee packages are structurally complete but still role-thin; the package name often overstates the real specialization encoded in the employee docs.

See `docs/ai/operations/CREWCLAW_WEBSITE_AGENT_AUDIT.md` and the per-employee files under `docs/ai/operations/crewclaw-employees/` before trusting a package for autonomous work.

## Installation Model

There are two different things to track for each employee:

1. **Runtime deployment**
   The employee can actually run as a bot/worker and connect to the OpenClaw gateway.

2. **CrewClaw dashboard monitoring**
   The employee shows a green dot in the CrewClaw portal by sending heartbeat pings.

These are related but not the same.

- A worker can be running without dashboard heartbeat.
- A worker can show heartbeat without being fully proven for routing and message handling.

## Batch Vs One-By-One

You do **not** need to prepare runtime one employee at a time.

Batch-friendly steps:

- unpack multiple employee ZIPs at once
- add multiple worker token UUIDs to the shared launcher
- extend the shared `deployed/docker-compose.yml` once for the whole batch
- start the full worker batch together

Usually still one-at-a-time in the CrewClaw UI:

- portal `Add Agent`
- grabbing or confirming a specific monitor key
- confirming the first dashboard ping for a specific employee tile

Recommended split:

- do runtime prep in batches
- do CrewClaw portal activation per employee as needed

## Recommended Operating Strategy

Use this lifecycle for every employee:

1. **Prepare**
   Unpack the package, inspect the generated files, and confirm the employee has a valid local project folder.

2. **Portal add**
   Add the employee in the CrewClaw portal so a monitor key can be created.

3. **Dashboard activation**
   Run the CrewClaw monitor setup from that employee's folder, or use the advanced manual method to write `CREWCLAW_MONITOR_KEY` locally and start heartbeat.

4. **Runtime proof**
   Prove the employee actually works:
   - token injected
   - container or process running
   - gateway reachable
   - device paired if applicable
   - route to `main` or intended agent verified
   - first heartbeat ping seen
   - real bot/platform reply succeeds

5. **Deactivate when not in workflow**
   Once proven, stop heartbeat and stop runtime unless the employee is actively needed.

6. **Keep ready**
   Leave the unpacked folder, config notes, secret mapping plan, and proof history in place so the employee can be reactivated quickly later.

### Default policy

- Keep only the employees currently used in the active workflow running.
- Keep all other prepared employees in a **ready but off** state.
- Turn on specialists only when they are needed for a real phase of work.

This avoids:

- secret sprawl
- idle containers
- noisy dashboards
- unnecessary bot routing complexity
- troubleshooting many inactive workers at once

## Standard Install Procedure For One Employee

### 1. Unpack the package

If the employee only exists as a ZIP:

- unzip it under `D:\github\open--claw\open-claw\employees\deployed\`
- resulting folder should look like:
  - `README.md`
  - `package.json`
  - `Dockerfile`
  - `docker-compose.yml`
  - `heartbeat.sh`
  - `setup.sh`
  - `agents/<employee-name>/SOUL.md`

### 2. Inspect the generated project

Confirm:

- `agents/<employee-name>/SOUL.md` exists
- `heartbeat.sh` exists
- `docker-compose.yml` exists
- `README.md` has the expected platform/start instructions

`SOUL.md` is important because CrewClaw's setup script auto-detects the employee identity from it.

### 3. Add the employee in the CrewClaw portal

In the CrewClaw portal:

- click `Add Agent`
- create the employee entry

After adding it, CrewClaw provides two monitor activation paths:

### Automatic path

Run from the employee project folder:

```bash
curl -fsSL https://www.crewclaw.com/monitor.sh | bash
```

What it does:

- detects the employee from `SOUL.md`
- asks for email
- registers the employee with CrewClaw
- writes `CREWCLAW_MONITOR_KEY` to local `.env`
- creates or reuses `heartbeat.sh`
- sends the first ping

### Advanced manual path

The CrewClaw portal dropdown also exposes:

- a `CREWCLAW_MONITOR_KEY=...` line for local `.env`
- a `curl ... /api/ping/...` cron example

Use the advanced path when:

- you already have the key visible in the portal
- you want to avoid the interactive script prompt
- you need to wire the heartbeat manually in Windows/WSL

Important:

- do **not** commit this `.env`
- do **not** store the raw key in repo docs

### 4. Write local monitor env

Create or update a local `.env` inside the employee folder:

```env
CREWCLAW_MONITOR_KEY=<portal-generated-key>
```

This `.env` is an approved CrewClaw-only exception and is for dashboard heartbeat only.

### 5. Start heartbeat

Preferred local path:

```bash
bash heartbeat.sh
```

Background example:

```bash
nohup bash heartbeat.sh > heartbeat.log 2>&1 &
```

Windows/WSL note:

For this repo, running `heartbeat.sh` via WSL from the employee project folder is the simplest path.

Important implementation note:

- use the CrewClaw ping endpoint exactly as shown in the portal manual path
- if a local `.env` is written from Windows, the heartbeat loader must tolerate `CRLF` line endings and trim any trailing `\r` from `CREWCLAW_MONITOR_KEY`

### 6. Verify dashboard activation

Expected signs:

- `heartbeat.sh` prints `ping ok`
- CrewClaw portal changes from `waiting for first ping`
- employee gets a green dot / online indicator

### 7. Runtime deployment

Only do this when the employee is meant to actually run in the workflow.

For the current shared deployment model, full runtime enablement requires:

- a Bitwarden secret for that worker token
- the secret UUID added to `start-employees.ps1`
- a service entry added to shared `deployed/docker-compose.yml`
- container verification after startup

The current shared startup script is:

- `D:\github\open--claw\open-claw\employees\deployed\start-employees.ps1`

It is currently hardcoded for the five shared workers only.

That means any newly unpacked employee is **not** part of the shared runtime until that script and the shared compose are extended.

### 8. Prove the employee works

Minimum proof checklist:

- CrewClaw portal entry exists
- monitor key exists locally
- `heartbeat.sh` returns `ping ok`
- worker runtime has token/config ready
- worker can reach the gateway
- worker route is valid
- worker can produce a real bot/platform reply

Do not treat `online in CrewClaw` as proof of full runtime health by itself.

## Shared Runtime Notes

Current shared compose:

- `D:\github\open--claw\open-claw\employees\deployed\docker-compose.yml`

Current shared startup script:

- `D:\github\open--claw\open-claw\employees\deployed\start-employees.ps1`

Current shared deployment behavior:

- injects secrets from Bitwarden
- starts the five existing shared workers
- does **not** include Bitwarden-native heartbeat wiring for all employees

So today there are two valid states:

1. **Dashboard-only activated**
   Employee pings CrewClaw but is not part of the shared worker runtime.

2. **Fully active**
   Employee is both heartbeat-enabled and wired into runtime/deployment.

## Deactivation Procedure

After proving an employee works, deactivate it unless it is actively needed.

### Dashboard deactivation

Stop the heartbeat process.

Examples:

```bash
pkill -f heartbeat.sh
```

or stop the specific background job / terminal running it.

### Runtime deactivation

If the worker has its own container:

```bash
docker compose stop
```

If it is part of the shared deployment:

- remove or disable its shared compose service
- or stop the specific container

### Keep the employee ready

Leave these in place:

- unpacked folder
- local notes
- secret mapping plan
- proof history
- portal entry if you want quick reactivation later

## Team Activation Strategy

### Always-on set

Keep only the smallest set always running:

- core workflow workers currently in daily use
- currently, only workers actively helping with real development flow should remain on

### On-demand set

Turn these on only for a task window:

- design specialists
- SEO/content workers
- CRM/sales workers
- script/build specialists
- experimental or low-frequency agents

### Activation gate

Before leaving any employee on, ask:

- Is it part of the active workflow this week?
- Does it have a real token and runtime path?
- Has it been proven recently?
- Will someone actually use it now?

If not, keep it ready but off.

## Recommended Plan For The Current 11

### Phase A: Prove all 10 Telegram workers can dashboard-activate

For each of the 10 token-backed Telegram workers:

- add in CrewClaw portal
- write local monitor `.env`
- run `heartbeat.sh`
- verify first ping
- stop heartbeat if the employee is not needed immediately

This proves install readiness without exploding runtime complexity.

Current runtime-ready worker set:

- `api-integration-specialist`
- `code-reviewer`
- `financial-analyst`
- `frontend-developer`
- `overnight-coder`
- `personal-crm`
- `script-builder`
- `seo-specialist`
- `software-engineer`
- `ux-designer`

### Phase B: Promote only selected employees into shared runtime

Only extend shared runtime for employees that are actively needed.

Candidates for near-term promotion:

- `software-engineer`
- `ux-designer`
- `seo-specialist`
- `script-builder`
- `personal-crm`

### Phase C: Add larger batch later

When the 31 additional ZIP packages arrive:

- unpack
- inventory
- portal-add
- dashboard-activate
- prove
- switch off unless in workflow

## Security Rules

- Never commit `.env` files with monitor keys
- Never commit Bitwarden secret values
- Keep Bitwarden as the source of truth for real runtime secrets
- Treat CrewClaw monitor keys as local operational secrets
- Prefer placeholders in docs and real values only in local env or Bitwarden

## Fastest Practical Workflow

For a new employee:

1. Unzip into `employees/deployed/<employee-name>`
2. Add employee in CrewClaw portal
3. Run monitor setup from that folder
4. Verify first ping
5. Stop heartbeat if not actively needed
6. Only later, wire it into shared runtime if the workflow truly needs it

That gives the best balance of:

- readiness
- proof
- low operational noise
- low deployment risk
