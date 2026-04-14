#!/bin/sh
set -e

if [ -z "$CREWCLAW_MONITOR_KEY" ]; then
  echo "[heartbeat] No CREWCLAW_MONITOR_KEY set; skipping dashboard heartbeat."
  exit 0
fi

while true; do
  curl -sf "https://www.crewclaw.com/api/ping/$CREWCLAW_MONITOR_KEY" > /dev/null 2>&1     && echo "[heartbeat] ping ok"     || echo "[heartbeat] ping failed"
  sleep 300
done
