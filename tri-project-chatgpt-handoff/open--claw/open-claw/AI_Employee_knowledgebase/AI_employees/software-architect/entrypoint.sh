#!/bin/sh
set -e

CONFIG_DIR="/root/.openclaw"
CONFIG_FILE="$CONFIG_DIR/openclaw.json"
WORKSPACE_DIR="$CONFIG_DIR/workspace"
MAIN_AGENT_DIR="$CONFIG_DIR/agents/main/agent"
ROLE_AGENT_ID="ENGINEER_ENRIQUE_BOT"
ROLE_AGENT_DIR="$CONFIG_DIR/agents/$ROLE_AGENT_ID/agent"

if [ -z "$OPENCLAW_GATEWAY_URL" ] || [ -z "$OPENCLAW_GATEWAY_TOKEN" ]; then
  echo "[entrypoint] ERROR: OPENCLAW_GATEWAY_URL and OPENCLAW_GATEWAY_TOKEN must be set."
  exit 1
fi

if [ -z "$OPENCLAW_AGENT_ID" ]; then
  export OPENCLAW_AGENT_ID="$ROLE_AGENT_ID"
fi

mkdir -p "$CONFIG_DIR" "$WORKSPACE_DIR" "$MAIN_AGENT_DIR" "$ROLE_AGENT_DIR"

cat > "$CONFIG_FILE" <<OCJSON
{
  "agents": {
    "defaults": {
      "workspace": "$WORKSPACE_DIR",
      "heartbeat": { "every": "0m" }
    },
    "list": [
      {
        "id": "main",
        "default": false,
        "workspace": "$WORKSPACE_DIR",
        "agentDir": "$MAIN_AGENT_DIR"
      },
      {
        "id": "ENGINEER_ENRIQUE_BOT",
        "default": true,
        "workspace": "$WORKSPACE_DIR",
        "agentDir": "$ROLE_AGENT_DIR"
      }
    ]
  },
  "gateway": {
    "mode": "remote",
    "remote": {
      "url": "$OPENCLAW_GATEWAY_URL",
      "token": "$OPENCLAW_GATEWAY_TOKEN"
    }
  }
}
OCJSON

echo "[entrypoint] workspace ready for ENGINEER_ENRIQUE_BOT"
echo "[entrypoint] worker agent id: $OPENCLAW_AGENT_ID"
echo "[entrypoint] remote gateway configured: $OPENCLAW_GATEWAY_URL"
exec node bot-telegram.js
