# droidrun_run.ps1
# Pulls DEEPSEEK_API_KEY from Bitwarden Secrets Manager (bws) and runs a DroidRun task.
# The API key is injected as a process-scoped env variable — never written to disk.
#
# First-time setup:
#   1. In Bitwarden Secrets Manager: create a Machine Account, grant it access to DroidRun project
#   2. Generate an Access Token for that machine account
#   3. Store that access token in your regular Bitwarden vault as item "BWS_DROIDRUN_TOKEN"
#   4. Run this script — it will bootstrap everything automatically
#
# Usage:
#   .\droidrun_run.ps1 -Task "Open YouTube and search for funny cats"
#   .\droidrun_run.ps1 -Task "Turn on Do Not Disturb" -Model "deepseek-reasoner" -Reasoning

param(
    [Parameter(Mandatory = $true)]
    [string]$Task,

    [string]$Device        = "100.71.228.18:5555",
    [string]$Provider      = "auto",        # auto = DeepSeek (no vision) or OpenRouter (vision)
    [string]$Model         = "auto",        # auto = picks best model for provider
    [switch]$Vision,                        # enables vision via OpenRouter
    [switch]$Reasoning,
    [int]   $Steps         = 30
)

$Root     = Split-Path $PSScriptRoot -Parent
$droidrun = Join-Path $Root ".venv\Scripts\droidrun.exe"

# Secret IDs from Bitwarden Secrets Manager — DroidRun project
$DEEPSEEK_SECRET_ID   = "14d69c11-99ba-428f-a656-b40e014e72ae"
$OPENROUTER_SECRET_ID = "f9ed80a7-fc35-4add-96d6-b40e0163b041"

Write-Host "=== DroidRun Agent ===" -ForegroundColor Cyan
Write-Host "Task    : $Task" -ForegroundColor White
Write-Host "Device  : $Device" -ForegroundColor White
Write-Host "Provider: $Provider / $Model" -ForegroundColor White
Write-Host ""

# --- 1. Get BWS access token from regular Bitwarden vault (bw) ---
Write-Host "[1/4] Fetching BWS access token from Bitwarden vault..." -ForegroundColor Yellow

# Check if BWS_ACCESS_TOKEN is already set in environment
if (-not $env:BWS_ACCESS_TOKEN) {
    # Unlock bw vault if needed
    $bwStatus = & bw status 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
    if ($bwStatus.status -eq "unauthenticated") {
        Write-Host "  Not logged in to Bitwarden. Running: bw login" -ForegroundColor Yellow
        bw login
    }
    if ($bwStatus.status -ne "unlocked") {
        Write-Host "  Unlocking vault (enter master password):" -ForegroundColor Yellow
        $env:BW_SESSION = & bw unlock --raw
    }

    # Retrieve the BWS machine account token from regular vault
    $tokenItem = & bw get item "BWS_DROIDRUN_TOKEN" 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
    if (-not $tokenItem) {
        Write-Host "  ERROR: Could not find 'BWS_DROIDRUN_TOKEN' in Bitwarden vault." -ForegroundColor Red
        Write-Host "  Store your Bitwarden Secrets Manager machine account token" -ForegroundColor Yellow
        Write-Host "  as a password item named 'BWS_DROIDRUN_TOKEN' in your Bitwarden vault." -ForegroundColor Yellow
        exit 1
    }
    $env:BWS_ACCESS_TOKEN = $tokenItem.login.password
    Write-Host "  BWS token loaded." -ForegroundColor Green
} else {
    Write-Host "  BWS_ACCESS_TOKEN already set in environment." -ForegroundColor Green
}

# --- 2. Resolve provider + model + fetch API key ---
Write-Host "`n[2/4] Resolving provider and fetching API key..." -ForegroundColor Yellow

# Auto-select provider: Vision tasks use OpenRouter (supports image_url), text tasks use DeepSeek
if ($Provider -eq "auto") {
    $Provider = if ($Vision) { "OpenRouter" } else { "DeepSeek" }
}

if ($Provider -eq "OpenRouter") {
    if ($Model -eq "auto") { $Model = "google/gemini-2.0-flash-001" }  # fast + vision + cheap
    $secretJson = & bws secret get $OPENROUTER_SECRET_ID 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ERROR: Could not fetch OPENROUTER_API_KEY: $secretJson" -ForegroundColor Red; exit 1
    }
    $apiKey = ($secretJson | ConvertFrom-Json).value
    $env:OPENAI_API_KEY = $apiKey   # OpenRouter uses OpenAI-compatible API
    Write-Host "  OpenRouter key loaded (model: $Model)." -ForegroundColor Green
} else {
    # DeepSeek
    if ($Model -eq "auto") { $Model = "deepseek-chat" }
    $secretJson = & bws secret get $DEEPSEEK_SECRET_ID 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ERROR: Could not fetch DEEPSEEK_API_KEY: $secretJson" -ForegroundColor Red; exit 1
    }
    $apiKey = ($secretJson | ConvertFrom-Json).value
    $env:DEEPSEEK_API_KEY = $apiKey
    Write-Host "  DeepSeek key loaded (model: $Model)." -ForegroundColor Green
}

if (-not $apiKey) {
    Write-Host "  ERROR: Secret value is empty." -ForegroundColor Red; exit 1
}

# --- 3. Inject into process environment (never written to disk) ---
Write-Host "`n[3/4] Injecting key into session environment..." -ForegroundColor Yellow
Write-Host "  Provider: $Provider / $Model" -ForegroundColor Green
Write-Host "  Vision  : $Vision" -ForegroundColor Green

# --- 4. Ensure ADB connection + port forward ---
Write-Host "`n[4/4] Verifying device connection..." -ForegroundColor Yellow
$connected = & adb devices 2>&1 | Where-Object { $_ -match [regex]::Escape($Device) -and $_ -match "device$" }
if (-not $connected) {
    Write-Host "  Reconnecting to $Device..." -ForegroundColor Yellow
    $connectResult = & adb connect $Device 2>&1
    Start-Sleep -Seconds 2
    $connected = & adb devices 2>&1 | Where-Object { $_ -match [regex]::Escape($Device) -and $_ -match "device$" }
    if (-not $connected) {
        Write-Host "  ERROR: Could not connect to $Device" -ForegroundColor Red
        Write-Host "  The wireless debugging port may have changed." -ForegroundColor Yellow
        Write-Host "  Check: Settings -> Developer options -> Wireless debugging" -ForegroundColor Yellow
        Write-Host "  Then re-run with: .\scripts\droidrun_run.ps1 -Device 100.71.228.18:NEWPORT -Task `"$Task`"" -ForegroundColor Yellow
        $env:DEEPSEEK_API_KEY = $null
        $env:BWS_ACCESS_TOKEN = $null
        exit 1
    }
}
$fwdResult = & adb -s $Device forward tcp:8080 tcp:8080 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: Port forward failed: $fwdResult" -ForegroundColor Red
    exit 1
}
Write-Host "  Device ready." -ForegroundColor Green

# --- 5. Run the task ---
Write-Host "`n=== Running Task ===" -ForegroundColor Cyan
Write-Host "> $Task" -ForegroundColor White
Write-Host ""

$cmdArgs = @(
    "run",
    "-d", $Device,
    "-m", $Model,
    "--steps", $Steps,
    "--stream"
)

# OpenRouter uses OpenAILike provider (skips model name validation, accepts any model)
if ($Provider -eq "OpenRouter") {
    $cmdArgs += @("-p", "OpenAILike", "--api_base", "https://openrouter.ai/api/v1")
} else {
    $cmdArgs += @("-p", $Provider)
}

if ($Vision)    { $cmdArgs += "--vision" } else { $cmdArgs += "--no-vision" }
if ($Reasoning) { $cmdArgs += "--reasoning" }

$cmdArgs += $Task

& $droidrun @cmdArgs

# Clear secrets from environment when done
$env:DEEPSEEK_API_KEY  = $null
$env:OPENAI_API_KEY    = $null
$env:BWS_ACCESS_TOKEN  = $null
Write-Host "`nSecrets cleared from session." -ForegroundColor DarkGray
