# store_api_keys_to_env.ps1
# One-time setup: fetches API keys from Bitwarden Secrets Manager and stores
# them as Windows user environment variables (encrypted in registry at HKCU).
# Run this once after any key rotation. MCP server then starts cleanly.

$DEEPSEEK_SECRET_ID   = "14d69c11-99ba-428f-a656-b40e014e72ae"
$OPENROUTER_SECRET_ID = "f9ed80a7-fc35-4add-96d6-b40e0163b041"

Write-Host "=== Store DroidRun API Keys to Windows User Environment ===" -ForegroundColor Cyan

# Unlock bw vault if needed
if (-not $env:BWS_ACCESS_TOKEN) {
    $bwStatus = & bw status 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
    if ($bwStatus.status -ne "unlocked") {
        Write-Host "Unlocking Bitwarden vault..." -ForegroundColor Yellow
        $env:BW_SESSION = & bw unlock --raw
    }
    $tokenItem = & bw get item "BWS_DROIDRUN_TOKEN" 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue
    if ($tokenItem) { $env:BWS_ACCESS_TOKEN = $tokenItem.login.password }
}

# Fetch keys
Write-Host "Fetching keys from Bitwarden Secrets Manager..." -ForegroundColor Yellow
$deepseekKey   = (& bws secret get $DEEPSEEK_SECRET_ID   2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue).value
$openrouterKey = (& bws secret get $OPENROUTER_SECRET_ID 2>&1 | ConvertFrom-Json -ErrorAction SilentlyContinue).value

if (-not $deepseekKey -or -not $openrouterKey) {
    Write-Host "ERROR: Could not retrieve one or more keys. Is BWS_ACCESS_TOKEN set?" -ForegroundColor Red
    exit 1
}

# Store as Windows user environment variables (HKCU registry, survives reboots)
[System.Environment]::SetEnvironmentVariable("DROIDRUN_DEEPSEEK_KEY",   $deepseekKey,   "User")
[System.Environment]::SetEnvironmentVariable("DROIDRUN_OPENROUTER_KEY", $openrouterKey, "User")

Write-Host "Keys stored as Windows user environment variables:" -ForegroundColor Green
Write-Host "  DROIDRUN_DEEPSEEK_KEY   = sk-...($($deepseekKey.Length) chars)" -ForegroundColor Green
Write-Host "  DROIDRUN_OPENROUTER_KEY = sk-...($($openrouterKey.Length) chars)" -ForegroundColor Green
Write-Host ""
Write-Host "MCP server will now start cleanly without needing Bitwarden at launch." -ForegroundColor Cyan
Write-Host "Re-run this script if you rotate your API keys." -ForegroundColor DarkGray
