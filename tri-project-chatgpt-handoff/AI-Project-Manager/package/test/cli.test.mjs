import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const cliPath = fileURLToPath(new URL("../dist/index.js", import.meta.url));

function runCli(args) {
  return spawnSync(process.execPath, [cliPath, ...args], {
    encoding: "utf8"
  });
}

function combinedOutput(result) {
  return `${result.stdout}\n${result.stderr}`.trim();
}

test("prints install help for top-level flags", () => {
  const result = runCli(["--help"]);
  const output = combinedOutput(result);

  assert.equal(result.status, 0);
  assert.match(output, /Install OpenMemory MCP server/);
  assert.match(output, /--client/);
});

test("prints the package version", () => {
  const result = runCli(["--version"]);
  const output = combinedOutput(result);

  assert.equal(result.status, 0);
  assert.match(output, /^0\.0\.2$/m);
});

test("fails fast when OPENMEMORY_API_KEY is missing", () => {
  const result = runCli(["--client", "cursor"]);
  const output = combinedOutput(result);

  assert.equal(result.status, 0);
  assert.match(output, /OPENMEMORY_API_KEY environment variable is required/);
});

test("warns on malformed env entries before failing", () => {
  const result = runCli(["--client", "cursor", "--env", "MALFORMED"]);
  const output = combinedOutput(result);

  assert.equal(result.status, 0);
  assert.match(output, /Invalid environment variable format: MALFORMED/);
  assert.match(output, /OPENMEMORY_API_KEY environment variable is required/);
});
