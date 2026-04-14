# adb_connect_wifi.ps1
# Connect to the phone over Wi-Fi (after pairing has been done once)
# Usage: .\adb_connect_wifi.ps1 -PhoneIP 192.168.1.XX -AdbPort XXXXX

param(
    [Parameter(Mandatory = $true)]
    [string]$PhoneIP,

    [Parameter(Mandatory = $true)]
    [string]$AdbPort
)

Write-Host "=== ADB Wi-Fi Connect ===" -ForegroundColor Cyan
Write-Host "Target: ${PhoneIP}:${AdbPort}" -ForegroundColor White
Write-Host ""

$result = & adb connect "${PhoneIP}:${AdbPort}" 2>&1
Write-Host $result

if ($result -match "connected") {
    Write-Host "`nConnection SUCCESSFUL." -ForegroundColor Green
    adb devices
} else {
    Write-Host "`nConnection FAILED. Check:" -ForegroundColor Red
    Write-Host "  1. Wireless debugging is enabled on the phone"
    Write-Host "  2. Phone IP address is correct"
    Write-Host "  3. ADB port matches what's shown in Wireless debugging settings"
    Write-Host "  4. You are on the same Wi-Fi network"
    exit 1
}

# Activate venv and verify DroidRun
Write-Host "`nVerifying DroidRun..." -ForegroundColor Yellow
$Root = Split-Path $PSScriptRoot -Parent
$droidrun = Join-Path $Root ".venv\Scripts\droidrun.exe"
if (Test-Path $droidrun) {
    & $droidrun ping 2>&1 | Select-Object -First 10
} else {
    Write-Host "  DroidRun not found at $droidrun" -ForegroundColor DarkGray
}
