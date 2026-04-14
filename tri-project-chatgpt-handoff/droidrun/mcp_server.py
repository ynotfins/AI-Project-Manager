"""
DroidRun MCP Server
Exposes DroidRun phone control as MCP tools for Cursor, OpenClaw, Claude Desktop, etc.

Run with:  .venv\Scripts\python.exe mcp_server.py
"""

import asyncio
import logging
import os
import subprocess
import sys
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolResult,
    ListToolsResult,
    TextContent,
    Tool,
)

logging.basicConfig(level=logging.WARNING)

ROOT = Path(__file__).parent
DROIDRUN = ROOT / ".venv" / "Scripts" / "droidrun.exe"
DEFAULT_DEVICE = "100.71.228.18:5555"

server = Server("droidrun")


def _ensure_connected() -> str | None:
    """Make sure ADB port forward is active. Returns error string or None."""
    try:
        r = subprocess.run(
            ["adb", "devices"], capture_output=True, text=True, timeout=5
        )
        if DEFAULT_DEVICE not in r.stdout:
            subprocess.run(
                ["adb", "connect", DEFAULT_DEVICE],
                capture_output=True, timeout=10
            )
        subprocess.run(
            ["adb", "-s", DEFAULT_DEVICE, "forward", "tcp:8080", "tcp:8080"],
            capture_output=True, timeout=5
        )
        return None
    except Exception as e:
        return str(e)


def _run_droidrun(task: str, vision: bool = False, model: str = "deepseek-chat",
                  provider: str = "DeepSeek", api_base: str | None = None,
                  steps: int = 30) -> str:
    """Run a droidrun task and return output."""
    cmd = [
        str(DROIDRUN), "run",
        "-d", DEFAULT_DEVICE,
        "-p", provider,
        "-m", model,
        "--steps", str(steps),
        "--stream",
    ]
    if vision:
        cmd.append("--vision")
    else:
        cmd.append("--no-vision")
    if api_base:
        cmd += ["--api_base", api_base]
    cmd.append(task)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300,
        env={**os.environ},
    )
    output = result.stdout + result.stderr
    return output.strip()


@server.list_tools()
async def list_tools() -> ListToolsResult:
    return ListToolsResult(tools=[
        Tool(
            name="phone_do",
            description=(
                "Control Anthony's Samsung Galaxy S25 Ultra with a natural language command. "
                "The AI agent will execute the task on the phone (open apps, tap buttons, "
                "type text, navigate, read screen content, etc.). "
                "Use vision=true when the task requires reading what's on screen."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "task": {
                        "type": "string",
                        "description": "Natural language instruction, e.g. 'Open YouTube and search for DroidRun'"
                    },
                    "vision": {
                        "type": "boolean",
                        "description": "Enable screenshot vision (slower, needed for reading screen content). Default: false",
                        "default": False
                    }
                },
                "required": ["task"]
            }
        ),
        Tool(
            name="phone_ping",
            description="Check if the phone (Samsung Galaxy S25 Ultra) is connected and the DroidRun Portal is running.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="phone_apps",
            description="List installed apps on the phone.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ])


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> CallToolResult:
    # Ensure ADB is connected before every call
    err = _ensure_connected()
    if err:
        return CallToolResult(content=[TextContent(type="text",
            text=f"ERROR: Could not connect to phone: {err}\n"
                 f"Make sure Wireless debugging is ON and Tailscale is running.")])

    if name == "phone_ping":
        result = subprocess.run(
            [str(DROIDRUN), "ping", "-d", DEFAULT_DEVICE],
            capture_output=True, text=True, timeout=15
        )
        return CallToolResult(content=[TextContent(type="text",
            text=result.stdout.strip() or result.stderr.strip())])

    elif name == "phone_apps":
        result = subprocess.run(
            ["adb", "-s", DEFAULT_DEVICE, "shell", "pm", "list", "packages", "-3"],
            capture_output=True, text=True, timeout=15
        )
        apps = result.stdout.strip()
        return CallToolResult(content=[TextContent(type="text", text=apps)])

    elif name == "phone_do":
        task = arguments.get("task", "")
        vision = arguments.get("vision", False)

        if not task:
            return CallToolResult(content=[TextContent(type="text",
                text="ERROR: 'task' is required.")])

        # Choose provider based on vision
        if vision:
            provider = "OpenAILike"
            model = "google/gemini-2.0-flash-001"
            api_base = "https://openrouter.ai/api/v1"
            # Check both the dedicated env var and fallbacks
            api_key = (os.environ.get("DROIDRUN_OPENROUTER_KEY") or
                       os.environ.get("OPENAI_API_KEY") or
                       os.environ.get("OPENROUTER_API_KEY", ""))
            os.environ["OPENAI_API_KEY"] = api_key
            env_key = "DROIDRUN_OPENROUTER_KEY"
        else:
            provider = "DeepSeek"
            model = "deepseek-chat"
            api_base = None
            api_key = (os.environ.get("DROIDRUN_DEEPSEEK_KEY") or
                       os.environ.get("DEEPSEEK_API_KEY", ""))
            os.environ["DEEPSEEK_API_KEY"] = api_key
            env_key = "DROIDRUN_DEEPSEEK_KEY"

        if not api_key:
            return CallToolResult(content=[TextContent(type="text",
                text=f"ERROR: {env_key} not set.\n"
                     f"Run: .\\scripts\\store_api_keys_to_env.ps1 (one-time setup)")])

        output = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: _run_droidrun(task, vision, model, provider, api_base)
        )
        return CallToolResult(content=[TextContent(type="text", text=output)])

    return CallToolResult(content=[TextContent(type="text", text=f"Unknown tool: {name}")])


async def main():
    async with stdio_server() as streams:
        await server.run(streams[0], streams[1], server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
