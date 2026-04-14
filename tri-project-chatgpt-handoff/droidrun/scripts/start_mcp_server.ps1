# start_mcp_server.ps1
# MCP server launcher — ALL setup output goes to stderr only.
# stdin/stdout are reserved exclusively for MCP JSON-RPC communication.

$Root = Split-Path $PSScriptRoot -Parent
$ErrorActionPreference = "SilentlyContinue"

# Keys are pre-stored as Windows user env vars via store_api_keys_to_env.ps1
# They load automatically from the user's environment — no output needed here.

# Start the MCP server — it owns stdin/stdout for JSON-RPC
& "$Root\.venv\Scripts\python.exe" "$Root\mcp_server.py"
