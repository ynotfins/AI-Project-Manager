# adb_pair_wifi.ps1
# Pair ADB with the phone over Wi-Fi (one-time pairing required for wireless debugging)
# Usage: .\adb_pair_wifi.ps1 -PhoneIP 192.168.1.XX -PairPort XXXXX -PairCode XXXXXX

param(
    [Parameter(Mandatory = $true)]
    [string]$PhoneIP,

    [Parameter(Mandatory = $true)]
    [string]$PairPort,

    [Parameter(Mandatory = $true)]
    [string]$PairCode
)

Write-Host "=== ADB Wi-Fi Pairing ===" -ForegroundColor Cyan
Write-Host "Phone IP  : $PhoneIP" -ForegroundColor White
Write-Host "Pair Port : $PairPort" -ForegroundColor White
Write-Host "Pair Code : $PairCode" -ForegroundColor White
Write-Host ""

# Pairing (one-time)
Write-Host "Pairing..." -ForegroundColor Yellow
$result = & adb pair "${PhoneIP}:${PairPort}" $PairCode 2>&1
Write-Host $result

if ($result -match "Successfully paired") {
    Write-Host "`nPairing SUCCESSFUL." -ForegroundColor Green
    Write-Host "Now run .\adb_connect_wifi.ps1 to connect." -ForegroundColor White
} else {
    Write-Host "`nPairing FAILED. Check:" -ForegroundColor Red
    Write-Host "  1. Wi-Fi pairing is still open on the phone (Settings -> Developer -> Wireless debugging -> Pair device with pairing code)"
    Write-Host "  2. Phone IP is correct (check Wi-Fi settings)"
    Write-Host "  3. Pairing code matches exactly"
    exit 1
}
