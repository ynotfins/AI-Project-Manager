# Voice Front Desk Agent

Standalone voice-service scaffold for a live phone-answering AI worker.

## Purpose
- Receive incoming Twilio phone calls
- Return TwiML for a controlled voice path
- Expose a websocket entrypoint for Twilio media or relay traffic
- Reserve ElevenLabs configuration for cloned-voice and conversational upgrades

## Current State
- Inbound voice webhook scaffold: present
- TwiML generation: present
- WebSocket intake endpoint: present
- ElevenLabs config surface: present
- Production telephony credentials: not configured here
- Public HTTPS/WSS endpoint: not configured here

## Setup
1. Copy `.env.example` to a local env file outside git.
2. Add Twilio and ElevenLabs credentials.
3. Expose the service on public HTTPS/WSS.
4. Point the Twilio number voice webhook to `/twilio/voice/incoming`.
5. Run a smoke call before treating the worker as live.

## Notes
- This service is intentionally separate from the curated 15-worker generator so the core squad stays stable.
- The current scaffold is designed for modular extension: `config`, `domain`, `http`, and `realtime`.
- A real production bridge still needs public hosting, credentials, and a decision on `media-stream` vs `conversation-relay`.
