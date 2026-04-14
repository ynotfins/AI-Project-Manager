const { Client, GatewayIntentBits } = require("discord.js");
const { runAgent } = require("./openclaw-runner");

const client = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});
const slug = "ENGINEER_ENRIQUE_BOT";

client.on("ready", () => {
  console.log(`Discord bot logged in for Software Architect as ${client.user.tag}`);
});

client.on("messageCreate", async (message) => {
  if (message.author.bot) return;
  try {
    const sessionId = `discord-${slug}-${message.author.id}`;
    const reply = await runAgent({ message: message.content, sessionId });
    await message.reply(reply || "No response from agent.");
  } catch (error) {
    console.error(error);
    await message.reply("Something went wrong. Please try again.");
  }
});

client.login(process.env.DISCORD_BOT_TOKEN);
