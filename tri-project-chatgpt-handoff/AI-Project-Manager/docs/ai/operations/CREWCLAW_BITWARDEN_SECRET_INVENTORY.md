# Bitwarden Secret Inventory

Names and UUIDs only. No secret values are stored in this repo.

Canonical reference: `docs/ai/protected/bitwarden.md`

Last synced: 2026-04-12

## Projects

| Project | Secret Count | Purpose |
|---------|-------------|---------|
| OpenClaw | 34 | Core runtime, employee bot tokens, and integrations |
| DroidRun | 3 | Mobile automation and model access |
| R3lentle$$-Grind-Global-Memory | 1 | Global memory / OpenMemory token |

**Total: 38 secrets**

## Machine Accounts

| Name | Secret Count | Notes |
|------|--------------|-------|
| BookChaos | 38 | Machine account present in the current Bitwarden org view |
| ChaosCentral | 38 | Machine account present in the current Bitwarden org view |
| droidrun-windows | 38 | DroidRun machine account used for mobile automation secret access |
| R3lentle$$-Grind-Global-Memory | 38 | Canonical global-memory / PLAN / Sparky machine account |

| Field | Value |
|-------|-------|
| Canonical Machine Account | R3lentle$$-Grind-Global-Memory |
| Organization ID | 8098135b-9af5-41d7-9bcc-b3fa001d7cea |
| Purpose | Autonomous secret management for PLAN/Sparky |

## Bitwarden Machine Account Setup

The Machine Account enables automated secret creation and rotation without human intervention.

To verify the Machine Account is working:

```powershell
$env:BWS_ACCESS_TOKEN = (Get-Content "$HOME\.openclaw\local.env" | Select-String "BWS_ACCESS_TOKEN" | ForEach-Object { $_.Line.Split('=',2)[1] })
bws secret list --organization-id 8098135b-9af5-41d7-9bcc-b3fa001d7cea
```

If this returns the secret list, the Machine Account is functional.

To create a new secret programmatically:

```powershell
bws secret create --key "SECRET_NAME" --value "secret_value" --project-id "<project-uuid>" --organization-id 8098135b-9af5-41d7-9bcc-b3fa001d7cea
```

## OpenClaw Runtime / API Secrets

| Secret Name | UUID | Purpose |
|-------------|------|---------|
| ANTHROPIC_API_KEY | 2fdc8f21-0d02-46b3-ad30-b3fe0049a474 | Claude models |
| ARTIFORGE_PERSONAL_ACCESS_TOKEN | e442a7ae-86fe-4189-a37a-b42801836e71 | Artiforge MCP |
| CLAWHUB_CLI_TOKEN | 4a48a157-5c5c-4534-8217-b4070156b34e | ClawHub CLI/runtime access |
| COMPOSIO_API_KEY | 774579e0-1337-418c-bfa5-b3fe00495653 | Composio integration |
| FIRECRAWL_API_KEY | 2e5140d0-767d-451f-b54e-b3fe0048fb50 | Firecrawl MCP |
| GITHUB_PERSONAL_ACCESS_TOKEN | e705c8b8-f152-4c6b-bc49-b3fe001841aa | GitHub MCP |
| GOG_KEYRING_PASSWORD | 40d4a7da-6d6b-4101-9256-b409003007b4 | GOG/keyring access |
| MATON_API_KEY | 69f6fe0e-30dc-4ff9-a979-b408017db0b1 | Maton integration |
| OBSIDIAN_LOCAL_REST_API | ba4bd3ea-e910-49e3-9524-b427016b8365 | Obsidian Local REST API |
| OPENAI_API_KEY | b1cd8ac8-f475-4ac7-afd7-b405002dbfc0 | GPT models |
| OPENCLAW_GATEWAY_TOKEN | 79f3acf8-c855-4c0d-9726-b40d01278bb6 | OpenClaw gateway auth |
| OPENMEMORY_API_KEY | 6c9955ba-a991-4d26-92b9-b4010043efde | Hosted OpenMemory compatibility path |
| OPENROUTER_API_KEY | c83ea5f5-89bd-46f1-b4f5-b405004a5ddc | OpenRouter models |
| SCRAPEOPS_API_KEY | 75056518-37d2-4976-842f-b4110152c998 | ScrapeOps integration |
| TWENTY_FIRST_API_KEY | b1ccb093-a646-452e-bd73-b40301835d6b | Magic MCP |
| XAI_API_KEY | 877c7114-c7dd-43d4-90c6-b41c015d211f | xAI/Grok models |
| ZEP_API_KEY | 83d96a20-c002-4c6e-b6f7-b40f0127a5b9 | Zep integration |

## Global Memory / OpenMemory

| Secret Name | UUID | Scope | Purpose |
|-------------|------|-------|---------|
| CURSOR_LOSSLESS_OPENMEMORY_API_KEY | 6bce89f4-4576-4b9f-b556-b425013e3100 | R3lentle$$-Grind-Global-Memory | Canonical OpenMemory token for the lossless memory system; startup scripts map it to `OPENMEMORY_API_KEY` for legacy hosted OpenMemory tooling that still expects the older env var name. |

## DroidRun Secrets

| Secret Name | UUID | Purpose |
|-------------|------|---------|
| BWS_DROIDRUN_TOKEN | 46fd9f5c-4b77-4de9-b0df-b4120005feb9 | DroidRun machine-account bootstrap token |
| DEEPSEEK_API_KEY | 14d69c11-99ba-428f-a656-b40e014e72ae | DroidRun DeepSeek access |
| OPENROUTER_API_KEY | f9ed80a7-fc35-4add-96d6-b40e0163b041 | DroidRun OpenRouter access |

## Curated Employee Telegram Bot Secrets (OpenClaw project)

Bitwarden secret names now reflect the stored bot secret names from Telegram/Bitwarden, which often match the Telegram username rather than the Telegram first name.

| Curated Employee | Bitwarden Secret Name | UUID |
|------------------|-----------------------|------|
| `accessibility-auditor` | `ACCESS_AUDITOR_ALLISON_BOT` | b1ff4d8c-d7ed-48e8-b96b-b427013718aa |
| `mcp-integration-engineer` | `API_ANDY_BOT` | d44c0214-4341-4b57-83b6-b411002ba700 |
| `backend-architect` | `BACKEND_BRUCE_BOT` | 64411f20-e4fb-418a-aa1b-b42701375e83 |
| `code-reviewer` | `CODE_REVIEWER` | 9f6d6d14-917f-435d-a757-b41100300499 |
| `delivery-director` | `DELIVERY_DIRECTOR_DAN_BOT` | f08c26ae-8b3b-42db-8b8a-b41e00254ae0 |
| `software-architect` | `ENGINEER_ENRIQUE_BOT` | 5dd1faf1-c943-4be3-8cbf-b41d000cc156 |
| `reality-checker` | `FINANCIAL_ANALYST` | d32f653b-0f42-4824-b760-b41100307afd |
| `frontend-developer` | `FRONTEND_FELIX_BOT` | db45a28d-e942-4b19-aee9-b4110030a9e8 |
| `qa-evidence-collector` | `OVERNIGHT_OLIVER_BOT` | cd3ecf0b-b6df-4490-9bf8-b4110030d207 |
| `ui-designer` | `PERSONAL_PAMELA_BOT` | 30a52f8e-5afa-4074-86f7-b41d000c36d7 |
| `product-manager` | `PRODUCT_MANAGER_PETE_BOT` | 262ed8cc-9adf-46a6-a0ba-b41e00258aa7 |
| `devops-automator` | `SCRIPT_SARAH_BOT` | 9127c2f6-7185-41c3-9aab-b41d000c69ee |
| `seo-ai-discovery-strategist` | `SEO_SAMANTHA_BOT` | 35e7872d-66f5-4a6c-9ec1-b41d000c9501 |
| `sparky-chief-product-quality-officer` | `SPARKY_CEO_BOT` | e08b6a94-02bf-4222-876a-b41e00251315 |
| `ux-architect` | `UX_URSULA_BOT` | c58957d8-a07e-4d6f-ab76-b41d000d1de7 |

## Additional Logged Telegram Bot Secrets (OpenClaw project)

These secrets were visible in the latest Bitwarden screenshots but are not part of the current curated 15-worker roster.

| Bitwarden Secret Name | UUID | Notes |
|-----------------------|------|-------|
| `destiny_stripper_bot` | 1a465209-f656-48de-8709-b42a012438fb | Logged bot secret outside the curated employee roster. |
| `SECRETARY_STACY_BOT` | 2733f3f8-964b-4cb6-be93-b42a0120b0b9 | Logged bot secret outside the curated employee roster; renamed from `Sparky4bot`; separate from the curated lead Sparky `SPARKY_CEO_BOT`. |

## CrewClaw Monitor Exception

`CREWCLAW_MONITOR_KEY` is intentionally allowed in untracked per-worker local `.env` files for CrewClaw dashboard heartbeat only.
