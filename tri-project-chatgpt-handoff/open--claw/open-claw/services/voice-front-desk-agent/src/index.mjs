import "dotenv/config";
import http from "node:http";

import { loadEnv } from "./config/env.mjs";
import { createApp } from "./http/app.mjs";
import { attachVoiceSocket } from "./realtime/voiceSocket.mjs";

const config = loadEnv();
const app = createApp(config);
const server = http.createServer(app);

attachVoiceSocket(server, config);

server.listen(config.port, () => {
  console.log("[voice-front-desk] listening", {
    port: config.port,
    voiceMode: config.twilioVoiceMode,
    websocketPath: config.voiceWebsocketPath,
    publicBaseUrlConfigured: Boolean(config.publicBaseUrl),
    elevenLabsConfigured: Boolean(config.elevenLabsApiKey)
  });
});
