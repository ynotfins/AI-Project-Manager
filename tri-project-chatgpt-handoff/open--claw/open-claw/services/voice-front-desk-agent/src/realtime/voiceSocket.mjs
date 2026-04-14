import { WebSocketServer } from "ws";

export function attachVoiceSocket(server, config) {
  const socketPath = config.voiceWebsocketPath;
  const wss = new WebSocketServer({ noServer: true });

  server.on("upgrade", (request, socket, head) => {
    const requestUrl = new URL(request.url, "http://localhost");
    if (requestUrl.pathname !== socketPath) {
      socket.destroy();
      return;
    }

    wss.handleUpgrade(request, socket, head, (ws) => {
      wss.emit("connection", ws, request);
    });
  });

  wss.on("connection", (ws, request) => {
    console.log("[voice-front-desk] websocket connected", {
      mode: config.twilioVoiceMode,
      path: request.url
    });

    ws.on("message", (payload) => {
      const text = payload.toString();
      const preview = text.length > 200 ? `${text.slice(0, 200)}...` : text;
      console.log("[voice-front-desk] websocket event", preview);
    });

    ws.on("close", () => {
      console.log("[voice-front-desk] websocket closed");
    });
  });

  return wss;
}
