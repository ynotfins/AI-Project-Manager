# adb_find_port.ps1
# Scans the phone's Tailscale IP for an open ADB wireless debugging port
# and connects automatically. No need to read the port from the phone.

param(
    [string]$TailscaleIP = "100.71.228.18",
    [int]$StartPort      = 37000,
    [int]$EndPort        = 47000,
    [int]$TimeoutMs      = 300
)

Write-Host "=== ADB Port Auto-Discovery ===" -ForegroundColor Cyan
Write-Host "Scanning $TailscaleIP ports $StartPort-$EndPort ..." -ForegroundColor Yellow
Write-Host "(This takes ~30 seconds)" -ForegroundColor DarkGray

$foundPort = $null

for ($port = $StartPort; $port -le $EndPort; $port++) {
    $tcp = New-Object System.Net.Sockets.TcpClient
    $connect = $tcp.BeginConnect($TailscaleIP, $port, $null, $null)
    $wait = $connect.AsyncWaitHandle.WaitOne($TimeoutMs, $false)
    if ($wait -and -not $tcp.Client.Poll(0, [System.Net.Sockets.SelectMode]::SelectError)) {
        try {
            $tcp.EndConnect($connect)
            Write-Host "`n  Found open port: $port" -ForegroundColor Green
            $foundPort = $port
            $tcp.Close()
            break
        } catch {}
    }
    $tcp.Close()

    # Progress every 500 ports
    if ($port % 500 -eq 0) {
        Write-Host "  Scanned up to $port..." -ForegroundColor DarkGray
    }
}

if (-not $foundPort) {
    Write-Host "`nNo open ADB port found in range $StartPort-$EndPort." -ForegroundColor Red
    Write-Host "Make sure Wireless debugging is ON on the phone." -ForegroundColor Yellow
    exit 1
}

# Connect and forward
Write-Host "Connecting to ${TailscaleIP}:${foundPort}..." -ForegroundColor Yellow
$result = & adb connect "${TailscaleIP}:${foundPort}" 2>&1
Write-Host "  $result"

if ($result -match "connected") {
    & adb -s "${TailscaleIP}:${foundPort}" forward tcp:8080 tcp:8080 | Out-Null
    Write-Host "  Port 8080 forwarded." -ForegroundColor Green

    # Update droidrun_run.ps1 default device with new port
    $runScript = Join-Path $PSScriptRoot "droidrun_run.ps1"
    (Get-Content $runScript) -replace '100\.71\.228\.18:\d+', "${TailscaleIP}:${foundPort}" |
        Set-Content $runScript
    Write-Host "  Updated droidrun_run.ps1 default port to $foundPort." -ForegroundColor Green

    # Update reconnect_remote.ps1
    $reconnectScript = Join-Path $PSScriptRoot "reconnect_remote.ps1"
    (Get-Content $reconnectScript) -replace '(\$PHONE_ADB_PORT\s+=\s+)"[\d]+"', "`$1`"$foundPort`"" |
        Set-Content $reconnectScript
    Write-Host "  Updated reconnect_remote.ps1 port to $foundPort." -ForegroundColor Green

    Write-Host "`nDone! Device: ${TailscaleIP}:${foundPort}" -ForegroundColor Cyan
    Write-Host "Now run: .\droidrun_run.ps1 -Task `"your task`"" -ForegroundColor White
} else {
    Write-Host "Connection failed." -ForegroundColor Red
    exit 1
}
