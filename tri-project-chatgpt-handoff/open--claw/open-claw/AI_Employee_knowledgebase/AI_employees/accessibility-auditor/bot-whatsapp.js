const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const { runAgent } = require("./openclaw-runner");

const client = new Client({ authStrategy: new LocalAuth() });
const slug = "ACCESS_AUDITOR_ALLISON_BOT";

client.on("qr", (qr) => {
  qrcode.generate(qr, { small: true });
  console.log("Scan the QR code above with WhatsApp");
});

client.on("ready", () => {
  console.log("WhatsApp bot is ready for Accessibility Auditor.");
});

client.on("message", async (message) => {
  try {
    const sender = message.from.replace(/[^a-zA-Z0-9]/g, "-");
    const sessionId = `whatsapp-${slug}-${sender}`;
    const reply = await runAgent({ message: message.body, sessionId });
    await message.reply(reply || "No response from agent.");
  } catch (error) {
    console.error(error);
    await message.reply("Something went wrong. Please try again.");
  }
});

client.initialize();
