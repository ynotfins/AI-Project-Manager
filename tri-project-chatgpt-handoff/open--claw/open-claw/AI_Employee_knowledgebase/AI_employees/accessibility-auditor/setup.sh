#!/bin/sh
set -e

WORKSPACE_DIR="$HOME/.openclaw/workspace"
mkdir -p "$WORKSPACE_DIR" "$WORKSPACE_DIR/skills" "$WORKSPACE_DIR/live" "$WORKSPACE_DIR/CHECKLISTS" "$WORKSPACE_DIR/HANDOFF_TEMPLATES" "$WORKSPACE_DIR/evals"

for file in README.md PROVENANCE.md IDENTITY.md SOUL.md AGENTS.md TOOLS.md SKILLS.md WORKFLOWS.md MEMORY.md USER.md BOOTSTRAP.md HEARTBEAT.md SCHEDULE.md CHECKLIST.md AUDIT.md ACCESS.md COMPLETE_TOOL_REFERENCE.md ONBOARDING.md DECISION_LOG.md RUNBOOK.md KNOWLEDGE_SOURCES.md SOURCE_PRIORITY.md RETRIEVAL_RULES.md SUCCESS_METRICS.md APPROVAL_GATES.md PR_RULES.md SPARKY_EVALUATION_SUMMARY.md; do
  cp "$file" "$WORKSPACE_DIR/$file"
done

cp -R skills/. "$WORKSPACE_DIR/skills/"
if [ -d live ]; then
  cp -R live/. "$WORKSPACE_DIR/live/"
fi
if [ -d CHECKLISTS ]; then
  cp -R CHECKLISTS/. "$WORKSPACE_DIR/CHECKLISTS/"
fi
if [ -d HANDOFF_TEMPLATES ]; then
  cp -R HANDOFF_TEMPLATES/. "$WORKSPACE_DIR/HANDOFF_TEMPLATES/"
fi
if [ -d evals ]; then
  cp -R evals/. "$WORKSPACE_DIR/evals/"
fi

echo "Workspace installed for Accessibility Auditor: $WORKSPACE_DIR"
echo "Provide OPENCLAW_GATEWAY_URL and OPENCLAW_GATEWAY_TOKEN before running a channel bot."
