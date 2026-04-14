const { App } = require("@slack/bolt");
const { runAgent } = require("./openclaw-runner");

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  socketMode: true,
  appToken: process.env.SLACK_APP_TOKEN,
});
const slug = "SPARKY_CEO_BOT";

app.event("app_mention", async ({ event, say }) => {
  const text = event.text.replace(/<@[^>]+>/g, "").trim();
  if (!text) return say("How can I help?");
  try {
    const sessionId = `slack-${slug}-${event.user ?? 'unknown'}`;
    const reply = await runAgent({ message: text, sessionId });
    await say(reply || "No response from agent.");
  } catch (error) {
    console.error(error);
    await say("Something went wrong. Please try again.");
  }
});

app.message(async ({ message, say }) => {
  if (message.subtype) return;
  try {
    const sessionId = `slack-dm-${slug}-${message.user ?? 'unknown'}`;
    const reply = await runAgent({ message: message.text, sessionId });
    await say(reply || "No response from agent.");
  } catch (error) {
    console.error(error);
    await say("Something went wrong. Please try again.");
  }
});

(async () => {
  await app.start();
  console.log("Slack bot is running for Chief Product and Quality Officer.");
})();
