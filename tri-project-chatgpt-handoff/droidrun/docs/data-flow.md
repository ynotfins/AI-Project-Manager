# Data Flow

This document traces the exact path data takes through DroidRun — from a user command to a physical tap on the device screen, and back.

---

## 1. User Input Flow (CLI → Action → Result)

```mermaid
flowchart TD
    A["User: droidrun run -d &lt;device&gt; -p DeepSeek -m deepseek-chat 'Open YouTube'"] --> B[CLI entry point\nsrc/droidrun/cli/main.py]
    B --> C[ConfigLoader.load\nReads ~/.config/droidrun/config.yaml\nMerges CLI flags]
    C --> D[AndroidDriver.connect\nADB connect to device\nadb forward tcp:8080 tcp:8080]
    D --> E[Portal health check\nPortalClient.connect\nDetects TCP vs content-provider mode]
    E --> F[DroidAgent.__init__\nBuilds LlamaIndex Workflow\nCreates DroidAgentState]
    F --> G{reasoning=True?}
    G -- No --> H[FastAgent or CodeActAgent\nDirect LLM tool-calling loop]
    G -- Yes --> I[ManagerAgent\nCreates plan + subgoals]
    I --> J[ExecutorAgent\nExecutes one atomic action per subgoal]
    H --> K[Action function called\ne.g. click index=5]
    J --> K
    K --> L[AndroidDriver method\ne.g. tap x=540 y=960]
    L --> M[ADB command sent to device\nasync_adbutils shell input tap 540 960]
    M --> N[ActionResult returned\nsuccess=True summary='Tapped element 5']
    N --> O[State updated\naction_history appended\nsummary_history appended]
    O --> P{finished?}
    P -- No --> Q[Next step: fetch fresh UI state\nback to H/J]
    P -- Yes --> R[ResultEvent\nsuccess + answer returned to CLI]
    R --> S[CLI prints result\ntrajectory saved if configured]
```

---

## 2. UI Perception Flow (Request → LLM Context)

Each agent step starts by fetching the current device state. This is the "eyes" of the agent.

```mermaid
flowchart TD
    A[Agent step begins] --> B[StateProvider.get_state called\nAndroidStateProvider]
    B --> C[driver.get_ui_tree called\nAndroidDriver]
    C --> D{PortalClient: TCP available?}
    D -- Yes --> E[HTTP GET localhost:8080/state\nvia adb-forwarded port]
    D -- No --> F[ADB content provider query\nadb shell content query\n--uri content://com.droidrun.portal/state]
    E --> G[Portal APK responds\nJSON: a11y_tree + phone_state + device_context]
    F --> G
    G --> H{Success?}
    H -- No / error --> I[Retry with backoff\n1s 2s 3s 5s 8s 10s\nup to 7 attempts]
    I -- attempt 5 --> J[Recovery: restart a11y service\n+ TCP socket server]
    J --> I
    I -- success --> K[Raw accessibility tree]
    H -- Yes --> K
    K --> L[TreeFilter.filter\nConciseFilter or DetailedFilter\nRemoves invisible / redundant nodes]
    L --> M[IndexedFormatter.format\nAssigns numeric index to each element\nProduces formatted text string]
    M --> N[UIState object created\nelements list + formatted_text\n+ phone_state + screen dims]
    N --> O[LLM context assembled:\nsystem prompt\n+ task goal\n+ action_history\n+ fast_memory\n+ formatted UI tree\n+ screenshot if vision=True]
    O --> P[LLM API call]
    P --> Q[Tool call or final answer\nreturned from LLM]
```

---

## 3. Vision Flow (Screenshot → Multimodal LLM Message)

Vision is **opt-in** (`--vision` flag or `tools.vision: true` in config). When enabled, a screenshot is captured and sent alongside the accessibility tree.

```mermaid
flowchart TD
    A[vision=True] --> B[take_screenshot action called\nor auto-captured each step]
    B --> C[AndroidDriver.take_screenshot\nadb exec-out screencap -p]
    C --> D[PNG bytes returned]
    D --> E[Stored in DroidAgentState.screenshot\nas raw bytes]
    E --> F[LLM message builder\nsrc/droidrun/agent/utils/chat_utils.py]
    F --> G[bytes encoded as base64]
    G --> H[LlamaIndex ImageBlock / ImageDocument\ninserted into ChatMessage content list]
    H --> I[Sent to LLM API\nas multimodal message\nOpenAI vision / Gemini / Claude]
    I --> J[LLM sees both:\ntext accessibility tree\n+ screenshot image]
```

Notes:
- Without vision, the LLM relies entirely on the formatted accessibility tree text.
- With vision, both are sent. The LLM can use either to answer.
- Providers that do not support multimodal input (e.g., DeepSeek text-only) will fail if vision is enabled. Use a vision-capable model (Gemini, GPT-4o, Claude 3.x, etc.).

---

## 4. MCP Tool Flow (Cursor/Claude → Phone)

When DroidRun is used as an MCP server, the call chain is:

```mermaid
flowchart TD
    A["MCP client\n(Cursor Agent / Claude Desktop / OpenClaw)"] --> B["MCP protocol call\nphone_do task='Open YouTube'"]
    B --> C[mcp_server.py\nstdio MCP server\nServer 'droidrun']
    C --> D[_ensure_connected\nadb devices + adb connect\nadb forward tcp:8080 tcp:8080]
    D --> E{vision=True?}
    E -- No --> F[provider=DeepSeek\nmodel=deepseek-chat\napi_key=DROIDRUN_DEEPSEEK_KEY]
    E -- Yes --> G[provider=OpenAILike\nmodel=google/gemini-2.0-flash-001\napi_base=openrouter.ai\napi_key=DROIDRUN_OPENROUTER_KEY]
    F --> H[subprocess.run\ndroidrun.exe run -d 100.71.228.18:5555\n-p DeepSeek -m deepseek-chat\n--steps 30 --stream task]
    G --> H
    H --> I[DroidRun CLI subprocess\ntimeout=300s\ncaptures stdout+stderr]
    I --> J[Full agent run\n see flows 1-2-3 above]
    J --> K[stdout output returned]
    K --> L[CallToolResult\nTextContent with output]
    L --> A
```

Tools exposed by `mcp_server.py`:

| Tool | What it does |
|---|---|
| `phone_do` | Run a natural language task (dispatches full DroidRun agent run) |
| `phone_ping` | `droidrun ping` — check Portal connectivity |
| `phone_apps` | `adb shell pm list packages -3` — list installed apps |

---

## 5. Error Flow (Failures and Fallbacks)

```mermaid
flowchart TD
    A[Any step fails] --> B{Which layer?}

    B -- Portal TCP timeout --> C[PortalClient falls back\nto ADB content provider]
    C --> D{Content provider works?}
    D -- Yes --> E[Continue normally]
    D -- No --> F[StateProvider retry loop\n7 attempts / 29s total]
    F -- attempt 5 --> G[Auto-recovery:\nrestart a11y service\nrestart TCP server]
    G --> F
    F -- all exhausted --> H[Exception raised\nWorkflow catches\nResultEvent success=False]

    B -- LLM API error --> I[LLM call raises exception\nlogged at ERROR level]
    I --> J[Workflow step fails\nLlamaIndex emits ResultEvent success=False]
    J --> K[CLI prints error\nexits with failure]

    B -- ADB not connected --> L[AndroidDriver.connect raises\nDeviceDisconnectedError re-raised immediately\nno retries on disconnect]
    L --> K

    B -- max_steps reached --> M[DroidAgent step loop exits\nResultEvent success=False\n'Max steps reached']
    M --> K

    B -- KeyboardInterrupt --> N[Caught in CLI main\nReturns False gracefully\nNo traceback printed]

    B -- MCP tool error --> O[Exception caught in call_tool handler\nReturns CallToolResult with error text\nMCP client receives error string\nnot an exception]

    B -- subprocess timeout in mcp_server --> P[subprocess.TimeoutExpired\nafter 300s\nReturns error string to MCP client]
```

---

## End-to-End Timing Reference

| Segment | Typical latency |
|---|---|
| ADB connect + port forward | < 1s |
| Portal state fetch (TCP) | 50–200ms |
| Portal state fetch (content provider) | 200–800ms |
| TreeFilter + IndexedFormatter | < 10ms |
| LLM API call (DeepSeek, no vision) | 1–5s |
| LLM API call (Gemini vision) | 2–8s |
| ADB action execution (tap, swipe) | 100–500ms |
| Full step (fetch → LLM → act) | 2–10s |
| Full task (10 steps, no vision) | 20–100s |
