---
name: elevenlabs-voice-clone
description: Voice cloning and conversational voice configuration using ElevenLabs for reusable, branded AI phone voices.
category: Communication
roles:
  - sparky-chief-product-quality-officer
  - product-manager
  - backend-architect
  - mcp-integration-engineer
---

# ElevenLabs Voice Clone

## Status: READY FOR INTEGRATION

## Purpose
Create and manage a branded cloned voice for AI phone interactions without hardcoding voice assets or mixing voice data into the main delivery runtime.

## Requirements
- Use ElevenLabs API credentials from environment variables only.
- Keep voice-clone source recordings out of git.
- Store only the resulting `voice_id` in runtime configuration.
- Separate voice creation from call-serving runtime so production calls can keep working while the voice evolves.

## Configuration Template
```env
ELEVENLABS_API_KEY=your_api_key
ELEVENLABS_VOICE_ID=voice_abc123
ELEVENLABS_AGENT_ID=agent_abc123
ELEVENLABS_MODEL_ID=eleven_v3_conversational
ELEVENLABS_OUTPUT_FORMAT=ulaw_8000
```

## Voice Clone Workflow
1. Capture clean sample audio outside the repo.
2. Upload samples to create a cloned voice.
3. Record the resulting `voice_id` in a secret or environment variable.
4. Bind the voice to the phone-answering runtime.
5. Run a smoke call and judge intelligibility, latency, and brand fit.

## Safety Rules
- Do not impersonate real people without explicit approval.
- Keep a neutral fallback voice available.
- Treat source recordings as sensitive assets.
- Prefer low-latency telephony-compatible output formats for live calls.

## Evidence
- Voice clone created successfully.
- `voice_id` is configured in the runtime.
- Test call audio is intelligible and stable.
- Fallback voice path is documented.
