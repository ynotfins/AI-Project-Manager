FROM node:22-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates     ffmpeg mediainfo     && rm -rf /var/lib/apt/lists/*     && git config --global url.'https://github.com/'.insteadOf 'ssh://git@github.com/'     && npm install -g openclaw@2026.3.13 --ignore-scripts

RUN mkdir -p /root/.openclaw/workspace /root/.openclaw/workspace/skills
COPY README.md /root/.openclaw/workspace/README.md
COPY PROVENANCE.md /root/.openclaw/workspace/PROVENANCE.md
COPY IDENTITY.md /root/.openclaw/workspace/IDENTITY.md
COPY SOUL.md /root/.openclaw/workspace/SOUL.md
COPY AGENTS.md /root/.openclaw/workspace/AGENTS.md
COPY TOOLS.md /root/.openclaw/workspace/TOOLS.md
COPY SKILLS.md /root/.openclaw/workspace/SKILLS.md
COPY WORKFLOWS.md /root/.openclaw/workspace/WORKFLOWS.md
COPY MEMORY.md /root/.openclaw/workspace/MEMORY.md
COPY USER.md /root/.openclaw/workspace/USER.md
COPY BOOTSTRAP.md /root/.openclaw/workspace/BOOTSTRAP.md
COPY HEARTBEAT.md /root/.openclaw/workspace/HEARTBEAT.md
COPY SCHEDULE.md /root/.openclaw/workspace/SCHEDULE.md
COPY CHECKLIST.md /root/.openclaw/workspace/CHECKLIST.md
COPY AUDIT.md /root/.openclaw/workspace/AUDIT.md
COPY skills/ /root/.openclaw/workspace/skills/
COPY package.json /app/package.json
COPY openclaw-runner.js /app/openclaw-runner.js
COPY bot-telegram.js /app/bot-telegram.js
COPY bot-discord.js /app/bot-discord.js
COPY bot-slack.js /app/bot-slack.js
COPY bot-whatsapp.js /app/bot-whatsapp.js
COPY entrypoint.sh /app/entrypoint.sh

RUN npm install && chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
