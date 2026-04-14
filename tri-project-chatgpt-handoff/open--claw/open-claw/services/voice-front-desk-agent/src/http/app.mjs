import express from "express";

import { buildIncomingVoiceResponse } from "../domain/twiml.mjs";

export function createApp(config) {
  const app = express();

  app.use(express.urlencoded({ extended: false }));
  app.use(express.json());

  app.get("/health", (_req, res) => {
    res.json({
      ok: true,
      voiceMode: config.twilioVoiceMode,
      publicBaseUrlConfigured: Boolean(config.publicBaseUrl),
      websocketUrlConfigured: Boolean(config.voiceWebsocketUrl),
      elevenLabsConfigured: Boolean(config.elevenLabsApiKey)
    });
  });

  app.post("/twilio/voice/incoming", (req, res) => {
    const twiml = buildIncomingVoiceResponse(config);
    console.log("[voice-front-desk] incoming call", {
      callSid: req.body.CallSid,
      from: req.body.From,
      to: req.body.To,
      mode: config.twilioVoiceMode
    });

    res.type("text/xml").send(twiml);
  });

  app.post("/twilio/voice/status", (req, res) => {
    console.log("[voice-front-desk] call status", {
      callSid: req.body.CallSid,
      callStatus: req.body.CallStatus,
      callDuration: req.body.CallDuration
    });

    res.sendStatus(204);
  });

  return app;
}
