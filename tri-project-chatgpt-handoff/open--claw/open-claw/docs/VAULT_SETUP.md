# OpenClaw — Vault Setup And Secret Management

## Secret Storage Policy

Use non-committed secret sources only.

Preferred sources, matching upstream behavior:

1. Process environment
2. `.env` in the current working directory
3. `~/.openclaw/.env`
4. Config `env` block in `~/.openclaw/openclaw.json`
5. SecretRef-backed config values or optional shell import

Wrapper rules:

- Never commit `.env`, API keys, tokens, or credentials.
- Avoid plaintext secrets in tracked docs or checked-in config templates.
- `~/.openclaw/.env` is a convenient local store, not the only supported source.
- Some provider credentials may be stored in auth profiles rather than shared `.env`.

## Option 1: 1Password CLI

### Setup

```bash
# Install 1Password CLI in WSL
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
  sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/amd64 stable main" | \
  sudo tee /etc/apt/sources.list.d/1password-cli.list
sudo apt update && sudo apt install -y 1password-cli
```

### Startup Script

```bash
#!/bin/bash
# ~/.openclaw/load-secrets.sh

export OPENCLAW_GATEWAY_TOKEN=$(op read "op://OpenClaw/Gateway/token")
export ANTHROPIC_API_KEY=$(op read "op://OpenClaw/Anthropic/api-key")
export OPENAI_API_KEY=$(op read "op://OpenClaw/OpenAI/api-key")
export TELEGRAM_BOT_TOKEN=$(op read "op://OpenClaw/Telegram/bot-token")
```

### Usage

```bash
eval $(op signin)
source ~/.openclaw/load-secrets.sh
cd ~/openclaw-build && pnpm openclaw gateway status
cd ~/openclaw-build && pnpm openclaw dashboard
```

## Option 2: Bitwarden CLI

### Setup

```bash
# Install Bitwarden CLI
npm install -g @bitwarden/cli
```

### Startup Script

```bash
#!/bin/bash
# ~/.openclaw/load-secrets-bw.sh

export BW_SESSION=$(bw unlock --raw)
export OPENCLAW_GATEWAY_TOKEN=$(bw get password "OpenClaw Gateway Token")
export ANTHROPIC_API_KEY=$(bw get password "Anthropic API Key")
export OPENAI_API_KEY=$(bw get password "OpenAI API Key")
```

### Usage

```bash
source ~/.openclaw/load-secrets-bw.sh
cd ~/openclaw-build && pnpm openclaw gateway status
cd ~/openclaw-build && pnpm openclaw dashboard
```

## Option 3: Plain `.env` File

```bash
# ~/.openclaw/.env
OPENCLAW_GATEWAY_TOKEN=<generated-token>
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
# GEMINI_API_KEY=...
# TELEGRAM_BOT_TOKEN=...
# DISCORD_BOT_TOKEN=...
```

Protect the file:

```bash
chmod 600 ~/.openclaw/.env
```

## Auth Profile Note

Current OpenClaw behavior can store some provider credentials in auth profiles instead of shared `.env`.

That means:

- shared env files are still useful for gateway tokens and simple local setups
- provider onboarding may write credentials somewhere other than `~/.openclaw/.env`
- when debugging missing provider auth, check both env sources and the provider auth/profile flow

## Secret Rotation Checklist

| Secret | Rotation Frequency | How To Rotate |
| --- | --- | --- |
| Gateway token | Every 90 days | Rotate through current gateway/auth workflow |
| Anthropic API key | On compromise | Regenerate in Anthropic console |
| OpenAI API key | On compromise | Regenerate in OpenAI console |
| Google OAuth refresh token | On revocation | Re-run OAuth flow |
| Telegram bot token | On compromise | Revoke via BotFather |
| Twilio auth token | Every 90 days | Rotate in Twilio console |

## Verification

Before running the gateway, verify:

```bash
# Check no secrets in repo docs/config templates
cd /mnt/d/github/open--claw
rg -n "sk-|ghp_|AIza|AKIA|token=|password=" --glob "*.md" --glob "*.json*" --glob "!vendor/**" --glob "!.git/**"

# Check .env permissions if using ~/.openclaw/.env
ls -la ~/.openclaw/.env

# Check env vars without printing values
env | grep -E "OPENCLAW_|ANTHROPIC_|OPENAI_" | sed 's/=.*/=<set>/'
```
