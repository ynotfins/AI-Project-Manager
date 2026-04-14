import twilio from "twilio";

const { VoiceResponse } = twilio.twiml;

export function buildIncomingVoiceResponse(config) {
  const response = new VoiceResponse();

  if (!config.voiceWebsocketUrl) {
    response.say(
      "The voice front desk is not configured yet. Please try again later or contact us through a text channel."
    );
    response.hangup();
    return response.toString();
  }

  if (config.twilioVoiceMode === "conversation-relay") {
    const connect = response.connect({
      action: config.publicBaseUrl ? `${config.publicBaseUrl}/twilio/voice/status` : undefined
    });
    connect.conversationRelay({
      url: config.voiceWebsocketUrl,
      welcomeGreeting: config.twilioWelcomeGreeting
    });
    return response.toString();
  }

  response.say(config.twilioWelcomeGreeting);
  const start = response.start();
  start.stream({
    name: "voice-front-desk-media-stream",
    url: config.voiceWebsocketUrl
  });
  response.pause({ length: 60 });

  return response.toString();
}
