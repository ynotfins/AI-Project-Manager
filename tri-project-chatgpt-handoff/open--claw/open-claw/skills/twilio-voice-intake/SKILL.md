---
name: twilio-voice-intake
description: Incoming phone-call handling via Twilio Voice, TwiML webhooks, and websocket-based real-time audio/session routing.
category: Communication
roles:
  - sparky-chief-product-quality-officer
  - delivery-director
  - product-manager
  - backend-architect
  - mcp-integration-engineer
---

# Twilio Voice Intake

## Status: READY FOR INTEGRATION

## Purpose
Receive live phone calls, route them into a controlled voice-agent workflow, and preserve a clean boundary between telephony transport, business logic, and escalation policy.

## Requirements
- Use Twilio Voice webhooks for inbound call entry.
- Return valid TwiML for the selected call path.
- Prefer websocket-based streaming or relay for real-time AI conversations.
- Keep secrets in environment variables only.
- Log call metadata and outcomes without storing raw secrets.

## Recommended Architecture
1. Twilio phone number receives the call.
2. Webhook returns TwiML that connects the caller to a controlled websocket or relay path.
3. A voice runtime handles greeting, intent capture, escalation, and transcript summarization.
4. Stable summaries are promoted to durable memory; raw call audio is not stored by default.

## Configuration Template
```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+15551234567
TWILIO_VOICE_WEBHOOK_BASE_URL=https://your-public-host.example.com
TWILIO_VOICE_MODE=conversation-relay
TWILIO_STATUS_CALLBACK_URL=https://your-public-host.example.com/twilio/voice/status
```

## Operational Rules
- Always provide a fallback greeting if the AI path is unavailable.
- Escalate urgent or sensitive calls to a human route instead of bluffing.
- Keep webhook handlers idempotent.
- Require a public HTTPS/WSS endpoint for Twilio callbacks and websocket connections.

## Evidence
- Inbound webhook returns valid TwiML.
- Call status callbacks are received and logged.
- Voice runtime health endpoint confirms ready state.
- At least one end-to-end test call is documented before production use.
