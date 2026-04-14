const { exec, execFile } = require("child_process");
const path = require("path");
const { promisify } = require("util");

const execAsync = promisify(exec);
const execFileAsync = promisify(execFile);
const preferredAgentId = process.env.OPENCLAW_AGENT_ID || "UX_URSELA_BOT";
const defaultWindowsBin = process.env.APPDATA
  ? path.join(process.env.APPDATA, "npm", "openclaw.cmd")
  : "openclaw.cmd";
const openclawBin = process.env.OPENCLAW_BIN || (process.platform === "win32" ? defaultWindowsBin : "openclaw");

function quoteCmdArg(value) {
  if (value === "") return "\"\"";
  if (!/[\\s"]/u.test(value)) return value;
  return `"${value.replace(/"/g, "\"\"")}"`;
}

async function execOpenClaw(args) {
  if (process.platform === "win32") {
    const commandLine = `"${openclawBin}" ${args.map(quoteCmdArg).join(" ")}`;
    return execAsync(commandLine, {
      env: process.env,
      maxBuffer: 1024 * 1024,
    });
  }

  return execFileAsync(openclawBin, args, {
    env: process.env,
    maxBuffer: 1024 * 1024,
  });
}

function isUnknownAgentError(error) {
  const combined = [error?.message, error?.stdout, error?.stderr].filter(Boolean).join("\\n");
  return combined.includes("Unknown agent id");
}

async function runAgent({ message, sessionId }) {
  const args = ["agent", "--agent", preferredAgentId, "--session-id", sessionId, "--message", message];
  try {
    const { stdout } = await execOpenClaw(args);
    return (stdout || "").trim();
  } catch (error) {
    if (preferredAgentId !== "main" && isUnknownAgentError(error)) {
      const { stdout } = await execOpenClaw(["agent", "--agent", "main", "--session-id", sessionId, "--message", message]);
      return (stdout || "").trim();
    }
    throw error;
  }
}

module.exports = { runAgent };
