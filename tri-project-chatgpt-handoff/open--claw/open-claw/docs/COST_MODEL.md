# OpenClaw — Cost Model

## Summary

OpenClaw is free, open-source software (MIT license). Operational costs come from
three sources: AI model API usage, infrastructure (VPS/server), and channel-specific fees.

## AI Model Pricing (per million tokens, Feb 2026)

### Budget Tier (routine tasks)

| Model | Input | Output |
|-------|-------|--------|
| Llama 3.1 8B (self-hosted) | ~$0.05 | ~$0.08 |
| GPT-4o-mini | $0.15 | $0.60 |

### Mid Tier (balanced cost/performance)

| Model | Input | Output |
|-------|-------|--------|
| GPT-4o | $2.50 | $10.00 |
| Claude Haiku 4.5 | $1.00 | $5.00 |

### Premium Tier (complex reasoning)

| Model | Input | Output |
|-------|-------|--------|
| Claude Sonnet 4.5 | ~$3.00 | ~$15.00 |
| Claude Opus 4.5 | $5.00 | $25.00 |
| GPT-5.2 | ~$5.00 | ~$15.00 |

### Token Usage Patterns

A typical OpenClaw interaction uses 1,000–5,000 input tokens and 500–2,000 output tokens.
Context accumulates across conversation turns — session history is sent with each request.

Token amplifiers specific to OpenClaw:
- **Context accumulation**: full conversation history per session
- **Tool calls**: each tool invocation adds input/output tokens
- **Memory retrieval**: embedding lookups add to context window
- **Multi-step reasoning**: chain-of-thought increases output tokens

## Model Routing & Cost Control

OpenClaw supports model fallback chains and per-agent model assignment:

```json5
{
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-sonnet-4-5",
        fallbacks: ["openai/gpt-4o-mini"],
      },
    },
  },
}
```

Cost reduction strategies:
1. **Route by complexity**: use budget models for routine, premium for complex
2. **Session reset policy**: `session.reset.mode: "daily"` limits context growth
3. **Idle timeout**: `session.reset.idleMinutes: 120` resets stale sessions
4. **Tool profiles**: `minimal` profile reduces tool-related token overhead
5. **Self-hosted models**: Ollama/vLLM on SaladCloud or local GPU ($0 API cost)

## Infrastructure Costs

| Use Case | Specs | Monthly Cost |
|----------|-------|-------------|
| Personal (light) | 1-2 vCPU, 2-4 GB RAM | $5–10 |
| Personal (active) | 2 vCPU, 4 GB RAM | $10–15 |
| Small team | 2-4 vCPU, 8 GB RAM | $15–40 |
| Heavy automation | 4+ vCPU, 16 GB RAM | $40–100+ |

OpenClaw runs 24/7 to monitor triggers and execute workflows.
Local development (WSL2 on existing hardware) has zero infrastructure cost.

## Channel-Specific Costs

| Channel | Cost |
|---------|------|
| WhatsApp (Baileys) | Free (unofficial API, personal account) |
| Telegram | Free (Bot API) |
| Discord | Free (Bot API) |
| Slack | Free tier available; paid for enterprise features |
| SMS (Twilio) | ~$0.0075/message outbound, ~$0.0075 inbound |
| Voice (ElevenLabs) | $5–22/mo depending on character count |

## Monthly Cost Estimates

| Tier | AI Models | Infra | Channels | Total |
|------|-----------|-------|----------|-------|
| Minimal personal | $1–5 | $0 (local) | $0 | **$1–5** |
| Active personal | $10–30 | $5–10 | $0 | **$15–40** |
| Small team | $30–80 | $15–40 | $0–10 | **$45–130** |
| Heavy automation | $50–150+ | $40–100 | $10–50 | **$100–300+** |

## Cost Monitoring

- `scripts/cron_usage_report.ts` — built-in usage reporting
- `scripts/debug-claude-usage.ts` — Anthropic-specific cost tracking
- `skills/model-usage/` — skill for querying model usage stats
- OpenRouter dashboard for multi-provider cost aggregation

## Caps & Limits

Configure in `openclaw.json`:
- `agents.defaults.limits` — per-agent token/request limits
- `session.reset` — automatic session resets to bound context growth
- Model fallback chains — auto-downgrade when primary model errors or exceeds budget
