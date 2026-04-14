# droidrun_ping.ps1
# Ping the DroidRun Portal on the connected device

$Root = Split-Path $PSScriptRoot -Parent
$droidrun = Join-Path $Root ".venv\Scripts\droidrun.exe"

Write-Host "=== DroidRun Ping ===" -ForegroundColor Cyan

if (-not (Test-Path $droidrun)) {
    Write-Host "DroidRun not found. Run setup_windows_host.ps1 first." -ForegroundColor Red
    exit 1
}

# Check device connected
$devices = & adb devices 2>&1
$authorized = $devices | Where-Object { $_ -match "\bdevice$" }
if (-not $authorized) {
    Write-Host "No authorized ADB device found." -ForegroundColor Red
    Write-Host "Run adb_connect_wifi.ps1 or adb_connect_tailscale.ps1 first." -ForegroundColor Yellow
    exit 1
}

Write-Host "Device found. Pinging DroidRun Portal..." -ForegroundColor Yellow
$result = & $droidrun ping 2>&1
Write-Host $result

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nPortal REACHABLE." -ForegroundColor Green
} else {
    Write-Host "`nPortal NOT reachable. Check:" -ForegroundColor Red
    Write-Host "  1. DroidRun Portal app is installed on the phone"
    Write-Host "  2. Accessibility service is enabled: Settings -> Accessibility -> DroidRun Portal"
    Write-Host "  3. Run 'droidrun setup' to reinstall/reconfigure"
}
