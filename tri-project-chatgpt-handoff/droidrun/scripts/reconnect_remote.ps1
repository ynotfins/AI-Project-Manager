# reconnect_remote.ps1
# Smart reconnect: tries USB first, then Wi-Fi, then Tailscale
# Edit the IP/port values below to match your phone's settings

# --- CONFIGURE THESE ---
$PHONE_WIFI_IP      = "192.168.1.120"   # Anthony's S25 Ultra local Wi-Fi IP
$PHONE_ADB_PORT     = "45991"           # Wireless debugging port (may change if toggled off/on)
$PHONE_TAILSCALE_IP = "100.71.228.18"   # Anthony's S25 Ultra Tailscale IP (stable)
# -----------------------

$Root = Split-Path $PSScriptRoot -Parent
$droidrun = Join-Path $Root ".venv\Scripts\droidrun.exe"

Write-Host "=== DroidRun Smart Reconnect ===" -ForegroundColor Cyan

function Test-DroidRun {
    if (-not (Test-Path $droidrun)) { return $false }
    $out = & $droidrun ping 2>&1
    return ($LASTEXITCODE -eq 0)
}

function Get-AuthorizedDevice {
    $d = & adb devices 2>&1 | Where-Object { $_ -match "\bdevice$" }
    return $d
}

# Step 1: Check if already connected
Write-Host "`n[1] Checking existing connections..." -ForegroundColor Yellow
if (Get-AuthorizedDevice) {
    Write-Host "  Already connected!" -ForegroundColor Green
    if (Test-DroidRun) {
        Write-Host "  DroidRun Portal: REACHABLE" -ForegroundColor Green
        exit 0
    } else {
        Write-Host "  DroidRun Portal: NOT reachable (check accessibility service)" -ForegroundColor Yellow
    }
}

# Step 2: Try USB
Write-Host "`n[2] Checking USB connection..." -ForegroundColor Yellow
& adb start-server | Out-Null
Start-Sleep -Seconds 2
if (Get-AuthorizedDevice) {
    Write-Host "  USB device found!" -ForegroundColor Green
    exit 0
}

# Step 3: Try Wi-Fi
Write-Host "`n[3] Trying Wi-Fi ($PHONE_WIFI_IP:$PHONE_ADB_PORT)..." -ForegroundColor Yellow
$wifiResult = & adb connect "${PHONE_WIFI_IP}:${PHONE_ADB_PORT}" 2>&1
Write-Host "  $wifiResult"
if ($wifiResult -match "connected") {
    Write-Host "  Wi-Fi connected!" -ForegroundColor Green
    exit 0
}

# Step 4: Try Tailscale
Write-Host "`n[4] Trying Tailscale ($PHONE_TAILSCALE_IP:$PHONE_ADB_PORT)..." -ForegroundColor Yellow
$tsResult = & adb connect "${PHONE_TAILSCALE_IP}:${PHONE_ADB_PORT}" 2>&1
Write-Host "  $tsResult"
if ($tsResult -match "connected") {
    Write-Host "  Tailscale connected!" -ForegroundColor Green
    exit 0
}

# Step 5: Try port scan to find the random wireless debug port, then lock back to 5555
Write-Host "`n[5] Port 5555 unreachable — scanning for wireless debug port..." -ForegroundColor Yellow
$found = & "$PSScriptRoot\adb_find_port.ps1" -TailscaleIP $PHONE_TAILSCALE_IP 2>&1
if ($LASTEXITCODE -eq 0) {
    # Re-lock to port 5555
    Write-Host "  Re-locking to port 5555..." -ForegroundColor Yellow
    & adb -s "${PHONE_TAILSCALE_IP}:5555" tcpip 5555 2>&1 | Out-Null
    Start-Sleep -Seconds 2
    & adb connect "${PHONE_TAILSCALE_IP}:5555" | Out-Null
    & adb -s "${PHONE_TAILSCALE_IP}:5555" forward tcp:8080 tcp:8080 | Out-Null
    Write-Host "  Port 5555 restored." -ForegroundColor Green
    exit 0
}

Write-Host "`n=== All reconnect methods FAILED ===" -ForegroundColor Red
Write-Host "Manual steps:" -ForegroundColor Yellow
Write-Host "  1. Check Wireless debugging is ON on the phone"
Write-Host "  2. Run: .\scripts\adb_find_port.ps1"
exit 1
