---
name: approval-gate
description: Human-in-the-loop confirmation system that intercepts outbound actions and requires explicit approve/deny before execution.
---

# Approval Gate Skill

## Status: READY (framework — requires approval channel configuration)

## Purpose
Central approval mechanism for all outbound actions across skills.
Prevents unintended sends, purchases, modifications, or deletions.

## Flow
```
Agent prepares action
       │
       ▼
┌──────────────────┐
│  Approval Gate   │
│  Intercepts      │
│  action          │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Post to         │
│  approval        │◀─── WhatsApp / Telegram / Slack / Discord
│  channel         │
└──────┬───────────┘
       │
  ┌────┴────┐
  │         │
approve    deny
  │         │
  ▼         ▼
execute   log + abort
```

## Approval Channel
The approval channel is configured in `openclaw.json`:
```json5
{
  skills: {
    entries: {
      "approval-gate": {
        enabled: true,
        env: {
          APPROVAL_CHANNEL: "whatsapp",
          APPROVAL_TARGET: "+15551234567",
          APPROVAL_TIMEOUT_MINUTES: "30",
        },
      },
    },
  },
}
```

## Approval Message Format
When an action requires approval, the gate posts:
```
🔒 Approval Required

Action: Send email
To: john@example.com
Subject: Meeting follow-up
Body preview: Hi John, following up on...

Reply "approve" to execute or "deny" to cancel.
Expires in 30 minutes.
```

## Rules
- All outbound sends (email, SMS, WhatsApp) require approval
- All event creation/modification requires approval
- All financial actions require approval
- Read-only operations do NOT require approval
- Expired approvals are auto-denied and logged
- Denied actions are logged with reason (if provided)
- No retry without new approval request

## Audit Integration
Every approval/denial is logged to the OpenClaw audit system:
- `checkId`: `approval-gate/<action-type>`
- `severity`: `info` (approved) or `warn` (denied/expired)
- `detail`: full action description, requester, approver, timestamp

## Integration with Other Skills
Skills that require approval call the gate before executing:
- `gmail-inbox` — all sends
- `domain-email` — all sends
- `sms-twilio` — all outbound SMS
- `whatsapp-official` — all outbound messages (except 24h window replies if configured)
- `google-calendar` — event creation, modification, deletion

## Unblock Steps
1. Choose an approval channel (WhatsApp, Telegram, Slack, or Discord)
2. Configure the channel in `openclaw.json` (must be already paired)
3. Set approval target (phone number, chat ID, or channel ID)
4. Run `openclaw config set skills.entries.approval-gate.enabled true`
