# CrewClaw Bitwarden Secret Inventory

Names and UUIDs only. No secret values are stored in this repo.

## Active

| Name                        | UUID                                   | Status   |
| --------------------------- | -------------------------------------- | -------- |
| `ANTHROPIC_API_KEY`         | `2fdc8f21-0d02-46b3-ad30-b3fe0049a474` | `active` |
| `OPENCLAW_GATEWAY_TOKEN`    | `79f3acf8-c855-4c0d-9726-b40d01278bb6` | `active` |
| `API_INTEGRATION_SPECIALIST`  | `d44c0214-4341-4b57-83b6-b411002ba700` | `active` |
| `CODE_REVIEWER`             | `9f6d6d14-917f-435d-a757-b41100300499` | `active` |
| `FINANCIAL_ANALYST`         | `d32f653b-0f42-4824-b760-b41100307afd` | `active` |
| `FRONTEND_DEVELOPER`        | `db45a28d-e942-4b19-aee9-b4110030a9e8` | `active` |
| `OVERNIGHT_CODER`           | `cd3ecf0b-b6df-4490-9bf8-b4110030d207` | `active` |
| `PERSONAL_CRM`              | `30a52f8e-5afa-4074-86f7-b41d000c36d7` | `active` |
| `SCRIPT_BUILDER`            | `9127c2f6-7185-41c3-9aab-b41d000c69ee` | `active` |
| `SEO_SPECIALIST`            | `35e7872d-66f5-4a6c-9ec1-b41d000c9501` | `active` |
| `SOFTWARE_ENGINEER`         | `5dd1faf1-c943-4be3-8cbf-b41d000cc156` | `active` |
| `UX_DESIGNER`               | `c58957d8-a07e-4d6f-ab76-b41d000d1de7` | `active` |

## CrewClaw Monitor Exception

`CREWCLAW_MONITOR_KEY` is intentionally allowed in untracked per-worker local `.env` files for CrewClaw dashboard heartbeat only.

This exception applies only to CrewClaw monitor keys. Runtime bot tokens, gateway tokens, and provider API keys remain Bitwarden-only secrets.

## Reserved / Not In Bitwarden

| Name                    | UUID                         | Status                 |
| ----------------------- | ---------------------------- | ---------------------- |
| `CREWCLAW_MONITOR_KEY`  | `local per-worker .env only` | `approved exception`   |
