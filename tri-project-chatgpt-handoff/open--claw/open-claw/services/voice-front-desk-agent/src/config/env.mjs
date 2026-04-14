import { z } from "zod";

const envSchema = z.object({
  PORT: z.coerce.number().int().positive().default(8788),
  PUBLIC_BASE_URL: z.string().url().optional(),
  TWILIO_VOICE_MODE: z.enum(["media-stream", "conversation-relay"]).default("media-stream"),
  TWILIO_ACCOUNT_SID: z.string().optional(),
  TWILIO_AUTH_TOKEN: z.string().optional(),
  TWILIO_PHONE_NUMBER: z.string().optional(),
  TWILIO_WELCOME_GREETING: z
    .string()
    .default("Hello, you have reached the AI front desk. How can I help you today?"),
  VOICE_WEBSOCKET_PATH: z.string().default("/twilio/voice/ws"),
  ELEVENLABS_API_KEY: z.string().optional(),
  ELEVENLABS_AGENT_ID: z.string().optional(),
  ELEVENLABS_VOICE_ID: z.string().optional(),
  ELEVENLABS_MODEL_ID: z.string().default("eleven_v3_conversational")
});

export function loadEnv(rawEnv = process.env) {
  const env = envSchema.parse(rawEnv);
  const publicBaseUrl = env.PUBLIC_BASE_URL?.replace(/\/$/, "") ?? "";
  const voiceWebsocketUrl = publicBaseUrl
    ? `${publicBaseUrl.replace(/^http/, "ws")}${env.VOICE_WEBSOCKET_PATH}`
    : "";

  return {
    port: env.PORT,
    publicBaseUrl,
    twilioVoiceMode: env.TWILIO_VOICE_MODE,
    twilioAccountSid: env.TWILIO_ACCOUNT_SID ?? "",
    twilioAuthToken: env.TWILIO_AUTH_TOKEN ?? "",
    twilioPhoneNumber: env.TWILIO_PHONE_NUMBER ?? "",
    twilioWelcomeGreeting: env.TWILIO_WELCOME_GREETING,
    voiceWebsocketPath: env.VOICE_WEBSOCKET_PATH,
    voiceWebsocketUrl,
    elevenLabsApiKey: env.ELEVENLABS_API_KEY ?? "",
    elevenLabsAgentId: env.ELEVENLABS_AGENT_ID ?? "",
    elevenLabsVoiceId: env.ELEVENLABS_VOICE_ID ?? "",
    elevenLabsModelId: env.ELEVENLABS_MODEL_ID
  };
}
