param()

$ErrorActionPreference = "Stop"

function Write-Check($name, $status, $detail) {
  [PSCustomObject]@{
    Check = $name
    Status = $status
    Detail = $detail
  }
}

$results = @()
$aiPmRoot = if ($env:AI_PROJECT_MANAGER_ROOT) { $env:AI_PROJECT_MANAGER_ROOT } else { "D:\github\AI-Project-Manager" }
$serverPath = Join-Path $aiPmRoot "scripts\openmemory_cursor_server.py"
$storePath = Join-Path $env:USERPROFILE ".openclaw\data\openmemory-cursor.sqlite3"

try {
  $mcpPath = Join-Path $HOME ".cursor\mcp.json"
  $mcp = Get-Content -LiteralPath $mcpPath -Raw | ConvertFrom-Json -ErrorAction Stop
  $openmemoryConfig = $null
  if ($mcp.mcpServers.PSObject.Properties.Name -contains "openmemory-local") {
    $openmemoryConfig = $mcp.mcpServers.'openmemory-local'
  } elseif ($mcp.mcpServers.PSObject.Properties.Name -contains "openmemory") {
    $openmemoryConfig = $mcp.mcpServers.openmemory
  }
  $ok = $null -ne $openmemoryConfig -and
        $openmemoryConfig.command -eq "python" -and
        ($openmemoryConfig.args | Select-Object -First 1) -eq $serverPath -and
        $openmemoryConfig.env.CLIENT_NAME -eq "cursor" -and
        $openmemoryConfig.env.OPENMEMORY_STORE_PATH -eq $storePath
  if ($ok) {
    $results += Write-Check "cursor mcp.json" "PASS" "local durable OpenMemory compatibility server"
  } else {
    $results += Write-Check "cursor mcp.json" "FAIL" "openmemory entry is not the local durable compatibility server"
  }
} catch {
  $results += Write-Check "cursor mcp.json" "FAIL" $_.Exception.Message
}

try {
  if (-not (Test-Path -LiteralPath $serverPath)) {
    throw "missing server script at $serverPath"
  }

  $logDir = Join-Path $HOME ".openclaw"
  $stdoutLog = Join-Path $logDir "verify-openmemory.log"
  $stderrLog = Join-Path $logDir "verify-openmemory.err.log"
  if (Test-Path $stdoutLog) { Remove-Item $stdoutLog -Force -ErrorAction SilentlyContinue }
  if (Test-Path $stderrLog) { Remove-Item $stderrLog -Force -ErrorAction SilentlyContinue }

  $env:OPENMEMORY_DEBUG_LOG = "1"
  $job = Start-Process -FilePath "python" -ArgumentList $serverPath -PassThru -WindowStyle Hidden `
    -RedirectStandardOutput $stdoutLog `
    -RedirectStandardError $stderrLog
  Start-Sleep -Seconds 2
  $stdout = if (Test-Path $stdoutLog) { Get-Content $stdoutLog -Raw } else { "" }
  $stderr = if (Test-Path $stderrLog) { Get-Content $stderrLog -Raw } else { "" }
  $combined = "$stdout`n$stderr"
  if (-not $job.HasExited) {
    Stop-Process -Id $job.Id -Force -ErrorAction SilentlyContinue
  }
  Remove-Item Env:\OPENMEMORY_DEBUG_LOG -ErrorAction SilentlyContinue
  if ($combined -match "OpenMemory Cursor MCP Server initialized successfully") {
    $results += Write-Check "local stdio server init" "PASS" "local compatibility server initialized successfully"
  } else {
    $results += Write-Check "local stdio server init" "FAIL" "Initialization success marker not found"
  }
} catch {
  $results += Write-Check "local stdio server init" "FAIL" $_.Exception.Message
}

try {
  $tmpStore = Join-Path $env:TEMP "openmemory-stack-check.sqlite3"
  $tmpProbeScript = Join-Path $env:TEMP "openmemory-stack-check.py"
  if (Test-Path $tmpStore) { Remove-Item $tmpStore -Force -ErrorAction SilentlyContinue }

  $script = @'
import json
import os
import subprocess
import sys

def run_probe(mode, token):
    server_env = os.environ.copy()
    server_env["OPENMEMORY_STORE_PATH"] = os.environ["OPENMEMORY_STACK_CHECK_STORE"]
    server = subprocess.Popen(
        ["python", os.environ["OPENMEMORY_STACK_CHECK_SERVER"]],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=server_env,
    )

    def send(msg):
        data = json.dumps(msg).encode("utf-8")
        if mode == "line-delimited":
            server.stdin.write(data + b"\n")
        else:
            server.stdin.write(f"Content-Length: {len(data)}\r\n\r\n".encode("ascii") + data)
        server.stdin.flush()

    def recv():
        if mode == "line-delimited":
            line = server.stdout.readline()
            if not line:
                raise RuntimeError("no line-delimited response from MCP server")
            return json.loads(line.decode("utf-8"))
        headers = {}
        while True:
            line = server.stdout.readline()
            if not line:
                raise RuntimeError("no framed response from MCP server")
            if line in (b"\r\n", b"\n"):
                break
            k, v = line.decode("utf-8").split(":", 1)
            headers[k.strip().lower()] = v.strip()
        body = server.stdout.read(int(headers["content-length"]))
        return json.loads(body.decode("utf-8"))

    send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "stack-check", "version": "1.0"}}})
    recv()
    send({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
    send({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "add-memory", "arguments": {"content": token}}})
    add_resp = recv()
    send({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "search-memories", "arguments": {"query": token}}})
    search_resp = recv()
    send({"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "list-memories", "arguments": {}}})
    list_resp = recv()
    send({"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "delete-all-memories", "arguments": {}}})
    delete_resp = recv()
    server.terminate()
    server.wait(timeout=5)
    return {
        "add": add_resp["result"]["content"][0]["text"],
        "search": search_resp["result"]["content"][0]["text"],
        "list": list_resp["result"]["content"][0]["text"],
        "delete": delete_resp["result"]["content"][0]["text"],
    }

payload = {
    "framed": run_probe("content-length", "STACK-CHECK-OPENMEMORY-FRAMED"),
    "line_delimited": run_probe("line-delimited", "STACK-CHECK-OPENMEMORY-LINE"),
}
print(json.dumps(payload))
'@

  Set-Content -LiteralPath $tmpProbeScript -Value $script -Encoding utf8
  $env:OPENMEMORY_STACK_CHECK_STORE = $tmpStore
  $env:OPENMEMORY_STACK_CHECK_SERVER = $serverPath
  $payload = python $tmpProbeScript
  Remove-Item Env:\OPENMEMORY_STACK_CHECK_STORE -ErrorAction SilentlyContinue
  Remove-Item Env:\OPENMEMORY_STACK_CHECK_SERVER -ErrorAction SilentlyContinue
  $parsed = $payload | ConvertFrom-Json

  $framed = $parsed.framed
  $lineDelimited = $parsed.line_delimited

  $ok = $framed.add -match "Memory added successfully|Memory already exists" -and
        $framed.search -match "STACK-CHECK-OPENMEMORY-FRAMED" -and
        $framed.list -match "STACK-CHECK-OPENMEMORY-FRAMED" -and
        $framed.delete -match "Deleted 1 memories|Deleted 0 memories" -and
        $lineDelimited.add -match "Memory added successfully|Memory already exists" -and
        $lineDelimited.search -match "STACK-CHECK-OPENMEMORY-LINE" -and
        $lineDelimited.list -match "STACK-CHECK-OPENMEMORY-LINE" -and
        $lineDelimited.delete -match "Deleted 1 memories|Deleted 0 memories"

  if ($ok) {
    $results += Write-Check "local store roundtrip" "PASS" "framed and line-delimited add/search/list/delete succeeded"
  } else {
    $results += Write-Check "local store roundtrip" "FAIL" ($payload -replace '\s+', ' ')
  }
} catch {
  $results += Write-Check "local store roundtrip" "FAIL" $_.Exception.Message
} finally {
  if (Test-Path (Join-Path $env:TEMP "openmemory-stack-check.sqlite3")) {
    Remove-Item (Join-Path $env:TEMP "openmemory-stack-check.sqlite3") -Force -ErrorAction SilentlyContinue
  }
  if (Test-Path (Join-Path $env:TEMP "openmemory-stack-check.py")) {
    Remove-Item (Join-Path $env:TEMP "openmemory-stack-check.py") -Force -ErrorAction SilentlyContinue
  }
}

$projectCacheRoot = Join-Path $env:USERPROFILE ".cursor\projects"
$descriptorCandidates = @()
if (Test-Path $projectCacheRoot) {
  $descriptorCandidates = Get-ChildItem -Path $projectCacheRoot -Recurse -Filter *.json -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -like "*\mcps\user-openmemory\tools\*.json" }
}
if ($descriptorCandidates.Count -gt 0) {
  $results += Write-Check "cursor descriptor tools" "PASS" "$($descriptorCandidates.Count) tool descriptors discovered in Cursor project cache"
} else {
  $results += Write-Check "cursor descriptor tools" "FAIL" "no user-openmemory tool descriptors found under $projectCacheRoot"
}

$results | Format-Table -AutoSize
