# adb_connect_tailscale.ps1
# Connect to the phone over Tailscale VPN (secure remote operation)
# Usage: .\adb_connect_tailscale.ps1 -TailscaleIP 100.XX.XX.XX -AdbPort XXXXX

param(
    [Parameter(Mandatory = $true)]
    [string]$TailscaleIP,

    [Parameter(Mandatory = $true)]
    [string]$AdbPort
)

Write-Host "=== ADB Tailscale Connect ===" -ForegroundColor Cyan
Write-Host "Tailscale IP : $TailscaleIP" -ForegroundColor White
Write-Host "ADB Port     : $AdbPort" -ForegroundColor White
Write-Host ""

# Verify Tailscale is running
Write-Host "Checking Tailscale status..." -ForegroundColor Yellow
$tsStatus = & tailscale status 2>&1 | Select-Object -First 5
Write-Host $tsStatus

# Connect via ADB
Write-Host "`nConnecting to device..." -ForegroundColor Yellow
$result = & adb connect "${TailscaleIP}:${AdbPort}" 2>&1
Write-Host $result

if ($result -match "connected") {
    Write-Host "`nTailscale ADB connection SUCCESSFUL." -ForegroundColor Green
    adb devices
    # Forward DroidRun Portal port (required after every new connection)
    Write-Host "`nForwarding DroidRun Portal port..." -ForegroundColor Yellow
    & adb -s "${TailscaleIP}:${AdbPort}" forward tcp:8080 tcp:8080 | Out-Null
    Write-Host "  Port 8080 forwarded." -ForegroundColor Green
} else {
    Write-Host "`nConnection FAILED. Check:" -ForegroundColor Red
    Write-Host "  1. Tailscale is running on BOTH this PC and the phone"
    Write-Host "  2. Both devices are in the same Tailscale network (tailscale status)"
    Write-Host "  3. Phone Tailscale IP is correct"
    Write-Host "  4. Wireless debugging is enabled on the phone"
    Write-Host "  5. ADB port matches phone's Wireless debugging settings"
    Write-Host ""
    Write-Host "  Get phone's Tailscale IP: Run 'tailscale status' on any device"
    exit 1
}

# Verify DroidRun
Write-Host "`nVerifying DroidRun ping..." -ForegroundColor Yellow
$Root = Split-Path $PSScriptRoot -Parent
$droidrun = Join-Path $Root ".venv\Scripts\droidrun.exe"
if (Test-Path $droidrun) {
    & $droidrun ping 2>&1 | Select-Object -First 10
}
