param(
    [int]$Port = 3080,
    [string]$HostAddress = "127.0.0.1",
    [string]$GatewayUrl = "http://127.0.0.1:18789",
    [switch]$Rebuild
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Path $PSScriptRoot -Parent
$nerveRoot = Join-Path (Split-Path -Path $repoRoot -Parent) "temp\openclaw-nerve"

function Resolve-NpmCommand {
    $npm = Get-Command npm.cmd -ErrorAction SilentlyContinue
    if (-not $npm) {
        $npm = Get-Command npm -ErrorAction SilentlyContinue
    }
    if ($npm) {
        return $npm.Source
    }

    $fallback = Join-Path $env:ProgramFiles "nodejs\npm.cmd"
    if (Test-Path -LiteralPath $fallback) {
        return $fallback
    }

    throw "npm.cmd not found in PATH or at $fallback"
}

function Get-NerveProbeHost([string]$TargetHostAddress) {
    if ($TargetHostAddress -eq "0.0.0.0" -or $TargetHostAddress -eq "::") {
        return "127.0.0.1"
    }

    return $TargetHostAddress
}

function Test-NerveHealthy([string]$TargetHostAddress, [int]$TargetPort) {
    $probeHost = Get-NerveProbeHost $TargetHostAddress
    $uri = "http://{0}:{1}/health" -f $probeHost, $TargetPort

    try {
        $response = Invoke-WebRequest -UseBasicParsing -Uri $uri -TimeoutSec 2
        if ($response.StatusCode -ne 200) {
            return $false
        }

        $payload = $response.Content | ConvertFrom-Json
        return $payload.status -eq "ok"
    } catch {
        return $false
    }
}

if (-not (Test-Path -LiteralPath $nerveRoot)) {
    throw "Nerve repo not found at $nerveRoot"
}

if (-not $env:OPENCLAW_GATEWAY_TOKEN -and -not $env:GATEWAY_TOKEN) {
    throw "Missing OPENCLAW_GATEWAY_TOKEN (or GATEWAY_TOKEN) in the current environment."
}

$npmCmd = Resolve-NpmCommand
$distIndex = Join-Path $nerveRoot "dist\index.html"
$serverEntry = Join-Path $nerveRoot "server-dist\index.js"

if ($Rebuild -or -not (Test-Path -LiteralPath $distIndex) -or -not (Test-Path -LiteralPath $serverEntry)) {
    Write-Host "Nerve build artifacts missing or rebuild requested; running npm run build..." -ForegroundColor Cyan
    Push-Location $nerveRoot
    try {
        & $npmCmd run build
        if ($LASTEXITCODE -ne 0) {
            throw "Nerve build failed. Fix the build before starting the dashboard."
        }
    } finally {
        Pop-Location
    }
}

$probeHost = Get-NerveProbeHost $HostAddress
if (Test-NerveHealthy -TargetHostAddress $HostAddress -TargetPort $Port) {
    Write-Host "Nerve already responds at http://$probeHost`:$Port" -ForegroundColor Yellow
    return
}

$startInfo = @{
    FilePath = $npmCmd
    ArgumentList = @("start")
    WorkingDirectory = $nerveRoot
    WindowStyle = "Hidden"
}

$env:PORT = "$Port"
$env:HOST = $HostAddress
$env:GATEWAY_URL = $GatewayUrl
if (-not $env:GATEWAY_TOKEN -and $env:OPENCLAW_GATEWAY_TOKEN) {
    $env:GATEWAY_TOKEN = $env:OPENCLAW_GATEWAY_TOKEN
}

Start-Process @startInfo | Out-Null

$deadline = (Get-Date).AddSeconds(12)
while ((Get-Date) -lt $deadline) {
    Start-Sleep -Milliseconds 500
    if (Test-NerveHealthy -TargetHostAddress $HostAddress -TargetPort $Port) {
        Write-Host "Nerve is live at http://$probeHost`:$Port" -ForegroundColor Green
        return
    }
}

Write-Host "Nerve start command launched, but /health is not responding yet at http://$probeHost`:$Port" -ForegroundColor Yellow
Write-Host "Run npm start in $nerveRoot to inspect the foreground logs if it stays down." -ForegroundColor Yellow
