import { access, readdir, readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const runtimeDir = path.dirname(fileURLToPath(import.meta.url));
const knowledgebaseDir = path.dirname(runtimeDir);
const employeesDir = path.join(knowledgebaseDir, "AI_employees");
const baselinePath = path.join(runtimeDir, "employee-runtime-baseline.json");

async function readJson(filePath) {
  return JSON.parse(await readFile(filePath, "utf8"));
}

async function listEmployeeDirs() {
  const entries = await readdir(employeesDir, { withFileTypes: true });
  const directories = entries
    .filter((entry) => entry.isDirectory())
    .map((entry) => path.join(employeesDir, entry.name));

  const livePackets = await Promise.all(
    directories.map(async (employeeDir) => {
      const requiredFiles = [
        path.join(employeeDir, "Dockerfile"),
        path.join(employeeDir, "package.json")
      ];

      try {
        await Promise.all(requiredFiles.map((filePath) => access(filePath)));
        return employeeDir;
      } catch {
        return null;
      }
    })
  );

  return livePackets.filter(Boolean);
}

function checkDockerfile(employeeName, dockerfile, baseline) {
  const issues = [];

  if (!dockerfile.includes(`FROM ${baseline.docker.baseImage}`)) {
    issues.push(
      `Dockerfile base image drift: expected FROM ${baseline.docker.baseImage}`
    );
  }

  if (!dockerfile.includes(`openclaw@${baseline.docker.openclawVersion}`)) {
    issues.push(
      `Dockerfile OpenClaw version drift: expected openclaw@${baseline.docker.openclawVersion}`
    );
  }

  return issues.map((issue) => `${employeeName}: ${issue}`);
}

function checkPackageJson(employeeName, packageJson, baseline) {
  const issues = [];
  const dependencies = packageJson.dependencies ?? {};

  for (const [name, version] of Object.entries(
    baseline.sharedChannelDependencies
  )) {
    if (dependencies[name] !== version) {
      issues.push(
        `${employeeName}: package.json dependency drift for ${name}: expected ${version}, found ${dependencies[name] ?? "<missing>"}`
      );
    }
  }

  return issues;
}

async function checkEmployee(employeeDir, baseline) {
  const employeeName = path.basename(employeeDir);
  const dockerfilePath = path.join(employeeDir, "Dockerfile");
  const packageJsonPath = path.join(employeeDir, "package.json");
  const [dockerfile, packageJson] = await Promise.all([
    readFile(dockerfilePath, "utf8"),
    readJson(packageJsonPath)
  ]);

  return [
    ...checkDockerfile(employeeName, dockerfile, baseline),
    ...checkPackageJson(employeeName, packageJson, baseline)
  ];
}

function printResult(employeeCount, issues) {
  if (issues.length === 0) {
    console.log(
      `PASS: ${employeeCount} curated AI employee runtime packets match the shared baseline.`
    );
    return;
  }

  console.error(
    `FAIL: detected ${issues.length} runtime drift issue(s) across ${employeeCount} curated AI employee packet(s).`
  );

  for (const issue of issues) {
    console.error(`- ${issue}`);
  }
}

async function main() {
  const baseline = await readJson(baselinePath);
  const employeeDirs = await listEmployeeDirs();
  const issueLists = await Promise.all(
    employeeDirs.map((employeeDir) => checkEmployee(employeeDir, baseline))
  );
  const issues = issueLists.flat();

  printResult(employeeDirs.length, issues);
  process.exitCode = issues.length === 0 ? 0 : 1;
}

main().catch((error) => {
  console.error(`FAIL: runtime drift check crashed: ${error.message}`);
  process.exitCode = 1;
});
