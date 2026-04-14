<#
.SYNOPSIS
  Canonical OpenClaw gateway secret sync + systemd restart (WSL).

.DESCRIPTION
  - Reads required API keys from the current process environment (inject via `bws run`).
  - Writes ~/.openclaw/.gateway-env inside WSL (chmod 600) for systemd EnvironmentFile.
  - Restarts openclaw-gateway.service.
  - Never prints secret values.

.NOTES
  ANTHROPIC_API_KEY is always required for this path.
  OPENAI_API_KEY / OPENROUTER_API_KEY / XAI_API_KEY are required when ~/.openclaw/openclaw.json references those providers.

  Avoid ad-hoc `pnpm openclaw gateway restart` from shells without injected env.
#>
$ErrorActionPreference = "Stop"

function ConvertTo-WslPath {
  param([Parameter(Mandatory)][string]$WindowsPath)
  if ($WindowsPath -match '^([A-Za-z]):\\(.*)$') {
    $drive = $Matches[1].ToLowerInvariant()
    $rest = ($Matches[2] -replace '\\', '/')
    return "/mnt/$drive/$rest"
  }
  throw "Cannot convert Windows path to WSL: $WindowsPath"
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pyWin = Join-Path $scriptDir "openclaw_gateway_required_env.py"
if (-not (Test-Path -LiteralPath $pyWin)) {
  throw "Missing helper script: $pyWin"
}
$pyWsl = ConvertTo-WslPath -WindowsPath $pyWin

"OPENCLAW: Canonical gateway restart — validating env + writing .gateway-env..." | Out-Host

$requiredRaw = wsl python3 $pyWsl 2>&1
if ($LASTEXITCODE -ne 0) {
  throw "openclaw_gateway_required_env.py failed: $requiredRaw"
}

$requiredNames = @(
  $requiredRaw |
    ForEach-Object { $_.ToString().Trim() } |
    Where-Object { $_ -match "^[A-Z0-9_]+$" }
)

if ($requiredNames.Count -lt 1) {
  throw "Failed to resolve required env names from WSL config."
}

$missing = @()
foreach ($name in $requiredNames) {
  $val = [System.Environment]::GetEnvironmentVariable($name)
  if (-not $val) {
    $missing += $name
  }
}

if ($missing.Count -gt 0) {
  throw @"
Missing required environment variables for gateway restart: $($missing -join ', ')
Launch from: bws run -- ... -- pwsh -File `$HOME\.openclaw\start-cursor-with-secrets.ps1
Or run this script from an injected shell.
"@
}

$env:WSLENV = "ANTHROPIC_API_KEY/u:OPENAI_API_KEY/u:OPENROUTER_API_KEY/u:XAI_API_KEY/u"
# Single-line bash avoids CRLF/heredoc breakage; vars come from WSLENV-inherited env inside WSL.
$bashLc = 'set -e; { printf "ANTHROPIC_API_KEY=%s\n" "$ANTHROPIC_API_KEY"; printf "OPENAI_API_KEY=%s\n" "$OPENAI_API_KEY"; printf "OPENROUTER_API_KEY=%s\n" "$OPENROUTER_API_KEY"; printf "XAI_API_KEY=%s\n" "$XAI_API_KEY"; } > ~/.openclaw/.gateway-env; chmod 600 ~/.openclaw/.gateway-env; systemctl --user daemon-reload; systemctl --user restart openclaw-gateway.service; sleep 8; echo GATEWAY_STARTED'
$gwResult = wsl bash -lc $bashLc
$env:WSLENV = ""

$gwResult | Out-Host
"OPENCLAW: Gateway restart issued (.gateway-env refreshed, systemd restarted)." | Out-Host
