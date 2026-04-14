# adb_status.ps1
# Show current ADB connection status and device info

Write-Host "=== ADB Status ===" -ForegroundColor Cyan

$devices = & adb devices 2>&1
Write-Host $devices

$deviceCount = ($devices | Where-Object { $_ -match "\bdevice$" }).Count
$unauthorized = ($devices | Where-Object { $_ -match "unauthorized" }).Count
$offline = ($devices | Where-Object { $_ -match "offline" }).Count

Write-Host ""
Write-Host "Summary:" -ForegroundColor Yellow
Write-Host "  Connected (authorized) : $deviceCount" -ForegroundColor $(if ($deviceCount -gt 0) { "Green" } else { "Red" })
Write-Host "  Unauthorized           : $unauthorized" -ForegroundColor $(if ($unauthorized -gt 0) { "Yellow" } else { "DarkGray" })
Write-Host "  Offline                : $offline" -ForegroundColor $(if ($offline -gt 0) { "Red" } else { "DarkGray" })

if ($deviceCount -gt 0) {
    Write-Host "`nDevice details:" -ForegroundColor Yellow
    try {
        $model = & adb shell getprop ro.product.model 2>&1
        $android = & adb shell getprop ro.build.version.release 2>&1
        $serial = & adb get-serialno 2>&1
        Write-Host "  Model   : $model"
        Write-Host "  Android : $android"
        Write-Host "  Serial  : $serial"
    } catch {
        Write-Host "  (Could not fetch device properties)" -ForegroundColor DarkGray
    }
}

if ($unauthorized -gt 0) {
    Write-Host "`nFix unauthorized: Unlock phone and tap 'Allow' on the USB debugging prompt." -ForegroundColor Yellow
}
if ($offline -gt 0) {
    Write-Host "`nFix offline: Try 'adb kill-server && adb start-server'" -ForegroundColor Yellow
}
