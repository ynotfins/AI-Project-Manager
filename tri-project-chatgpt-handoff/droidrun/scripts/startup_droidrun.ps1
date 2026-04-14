# startup_droidrun.ps1
# Unified DroidRun startup script — handles both normal sessions and post-reboot.
# Add this to the workspace launch script. Run order: inject keys → smart reconnect.
#
# Normal session:  injects keys + verifies existing connection (fast, ~5 seconds)
# After reboot:    injects keys + finds port + re-locks to 5555 + forwards (auto)
# No flags needed — detects which path is required automatically.

$ErrorActionPreference = "SilentlyContinue"
$Root = Split-Path $PSScriptRoot -Parent

$DEEPSEEK_SECRET_ID   = "14d69c11-99ba-428f-a656-b40e014e72ae"
$OPENROUTER_SECRET_ID = "f9ed80a7-fc35-4add-96d6-b40e0163b041"
$PHONE_TAILSCALE_IP   = "100.71.228.18"
$PHONE_ADB_PORT       = "5555"

Write-Host "=== DroidRun Startup ===" -ForegroundColor Cyan

# ── STEP 1: Inject API keys from Bitwarden Secrets Manager ──────────────────
Write-Host "[1/2] Injecting API keys..." -ForegroundColor Yellow

# Bootstrap BWS token from regular Bitwarden vault
if (-not $env:BWS_ACCESS_TOKEN) {
    $bwStatus = & bw status 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
    if ($bwStatus.status -eq "unauthenticated") {
        Write-Host "  Bitwarden not logged in. Run 'bw login' first." -ForegroundColor Red
        exit 1
    }
    if ($bwStatus.status -ne "unlocked") {
        Write-Host "  Unlocking Bitwarden vault (enter master password):" -ForegroundColor Yellow
        $env:BW_SESSION = & bw unlock --raw
    }
    $tokenItem = & bw get item "BWS_DROIDRUN_TOKEN" 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
    if ($tokenItem) {
        $env:BWS_ACCESS_TOKEN = $tokenItem.login.password
    } else {
        Write-Host "  ERROR: BWS_DROIDRUN_TOKEN not found in Bitwarden vault." -ForegroundColor Red
        exit 1
    }
}

$deepseekKey   = (& bws secret get $DEEPSEEK_SECRET_ID   2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue).value
$openrouterKey = (& bws secret get $OPENROUTER_SECRET_ID 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue).value

if (-not $deepseekKey -or -not $openrouterKey) {
    Write-Host "  ERROR: Could not retrieve one or more API keys from Secrets Manager." -ForegroundColor Red
    Write-Host "  Ensure droidrun-windows machine account has access to the DroidRun project." -ForegroundColor Yellow
    exit 1
}

# Store as Windows user env vars (encrypted in registry, survive reboots)
[System.Environment]::SetEnvironmentVariable("DROIDRUN_DEEPSEEK_KEY",   $deepseekKey,   "User")
[System.Environment]::SetEnvironmentVariable("DROIDRUN_OPENROUTER_KEY", $openrouterKey, "User")

# Also set for this process immediately
$env:DROIDRUN_DEEPSEEK_KEY   = $deepseekKey
$env:DROIDRUN_OPENROUTER_KEY = $openrouterKey

Write-Host "  API keys injected." -ForegroundColor Green

# ── STEP 2: Smart ADB reconnect ──────────────────────────────────────────────
Write-Host "[2/2] Verifying phone connection..." -ForegroundColor Yellow

$target = "${PHONE_TAILSCALE_IP}:${PHONE_ADB_PORT}"

# Check if already connected on port 5555
$connected = & adb devices 2>&1 | Where-Object { $_ -match [regex]::Escape($target) -and $_ -match "device$" }

if ($connected) {
    # Already connected — just ensure port forward is active
    & adb -s $target forward tcp:8080 tcp:8080 | Out-Null
    Write-Host "  Phone connected on $target." -ForegroundColor Green
} else {
    # Not connected — attempt reconnect on port 5555 first
    Write-Host "  Not connected. Attempting reconnect..." -ForegroundColor Yellow
    $result = & adb connect $target 2>&1
    Start-Sleep -Seconds 2
    $connected = & adb devices 2>&1 | Where-Object { $_ -match [regex]::Escape($target) -and $_ -match "device$" }

    if ($connected) {
        & adb -s $target forward tcp:8080 tcp:8080 | Out-Null
        Write-Host "  Reconnected on $target." -ForegroundColor Green
    } else {
        # Port 5555 not responding — post-reboot path: scan for current wireless debug port
        Write-Host "  Port 5555 unreachable (likely post-reboot). Scanning for active port..." -ForegroundColor Yellow
        & "$PSScriptRoot\adb_find_port.ps1" -TailscaleIP $PHONE_TAILSCALE_IP 2>&1 | Out-Null

        # adb_find_port.ps1 connects and re-locks to 5555
        Start-Sleep -Seconds 2
        $connected = & adb devices 2>&1 | Where-Object { $_ -match [regex]::Escape($target) -and $_ -match "device$" }

        if ($connected) {
            & adb -s $target forward tcp:8080 tcp:8080 | Out-Null
            Write-Host "  Port re-locked to 5555 and connected." -ForegroundColor Green
        } else {
            Write-Host "  WARNING: Could not connect to phone." -ForegroundColor Yellow
            Write-Host "  Check: Wireless debugging ON, Tailscale running on phone." -ForegroundColor Yellow
            Write-Host "  DroidRun keys are injected — run .\scripts\reconnect_remote.ps1 manually when phone is available." -ForegroundColor Yellow
        }
    }
}

Write-Host ""
Write-Host "DroidRun ready. Run tasks with:" -ForegroundColor Cyan
Write-Host "  .\scripts\droidrun_run.ps1 -Task `"your task here`"" -ForegroundColor White
Write-Host "  .\scripts\droidrun_run.ps1 -Task `"your task here`" -Vision" -ForegroundColor White
Write-Host ""
