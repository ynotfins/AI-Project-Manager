# Voice Front Desk Stack

## Purpose
Define the first live phone-answering stack for OpenClaw without disturbing the curated 15-worker generator.

## Decision
- Keep the curated 15-worker squad stable.
- Add phone/voice support as a separate standalone service under `open-claw/services/voice-front-desk-agent/`.
- Treat the voice worker as an incubation runtime until Twilio credentials, a public HTTPS/WSS endpoint, and ElevenLabs voice settings are live.

## Recommended Stack
1. **Twilio Voice** for the phone number, inbound call webhook, and TwiML control path.
2. **Standalone voice-front-desk service** for TwiML generation, websocket intake, and call-state logging.
3. **ElevenLabs** for cloned voice and conversational voice configuration.
4. **Sparky** as final gate for greeting quality, escalation rules, and production readiness.

## Why Separate From The Curated 15
- The curated runtime currently enforces a fixed 15-worker invariant.
- A phone worker needs different dependencies, public network posture, and operational rules than the Telegram-first squad.
- Twilio/voice rollout should not destabilize the current employee sync and deployment flow.

## Required External Setup
- Twilio account with a Voice-capable phone number
- Public HTTPS URL for `/twilio/voice/incoming`
- Public WSS URL for `/twilio/voice/ws`
- ElevenLabs API key and either `voice_id` or `agent_id`

## Current Repo Surface
- Skills:
  - `twilio-voice-intake`
  - `elevenlabs-voice-clone`
  - `phone-support-intake`
- Runtime service:
  - `open-claw/services/voice-front-desk-agent/`

## Ready For Live Test When
- Twilio number is purchased and webhook is configured
- Service is reachable on public HTTPS/WSS
- ElevenLabs credentials and voice settings are present
- A smoke call confirms greeting, routing, and fallback behavior
