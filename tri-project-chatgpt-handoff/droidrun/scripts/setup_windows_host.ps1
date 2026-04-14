# setup_windows_host.ps1
# One-time setup: verifies ADB, creates .venv, installs DroidRun
# Run from D:\github\droidrun

$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent

Write-Host "=== DroidRun Windows Host Setup ===" -ForegroundColor Cyan

# --- 1. Check ADB ---
Write-Host "`n[1/4] Checking ADB..." -ForegroundColor Yellow
try {
    $adbVer = & adb version 2>&1 | Select-Object -First 1
    Write-Host "  PASS: $adbVer" -ForegroundColor Green
} catch {
    Write-Host "  FAIL: ADB not found. Installing via winget..." -ForegroundColor Red
    winget install Google.PlatformTools --accept-source-agreements --accept-package-agreements
    $env:PATH += ";C:\platform-tools"
    Write-Host "  Restart PowerShell and re-run this script after install." -ForegroundColor Yellow
    exit 1
}

# --- 2. Check Python ---
Write-Host "`n[2/4] Checking Python..." -ForegroundColor Yellow
$pyVer = python --version 2>&1
Write-Host "  PASS: $pyVer" -ForegroundColor Green

# --- 3. Create .venv if missing ---
Write-Host "`n[3/4] Setting up virtual environment..." -ForegroundColor Yellow
$VenvPath = Join-Path $Root ".venv"
if (-not (Test-Path $VenvPath)) {
    python -m venv $VenvPath
    Write-Host "  Created .venv" -ForegroundColor Green
} else {
    Write-Host "  .venv already exists, skipping." -ForegroundColor DarkGray
}

# --- 4. Install DroidRun ---
Write-Host "`n[4/4] Installing DroidRun..." -ForegroundColor Yellow
$pip = Join-Path $VenvPath "Scripts\python.exe"
& $pip -m pip install --upgrade pip setuptools wheel | Out-Null
$SrcPath = Join-Path $Root "src"
& $pip -m pip install -e "$SrcPath[google,anthropic,openai,deepseek,ollama,dev]" | Select-Object -Last 3

Write-Host "`n=== Setup complete! ===" -ForegroundColor Cyan
Write-Host "Activate with: .venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "Then run:      droidrun --help" -ForegroundColor White
