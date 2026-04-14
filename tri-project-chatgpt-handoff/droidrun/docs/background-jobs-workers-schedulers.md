# DroidRun — Background Jobs, Workers, and Schedulers

> DroidRun v0.5.1 · Python asyncio · LlamaIndex Workflows

## Summary

**DroidRun has no traditional background workers, daemons, schedulers, or persistent job queues.**

Every `droidrun run` invocation is a discrete, one-shot process. It starts, completes (or times out), and exits. Nothing runs between invocations. This document explains what this means in practice, identifies the components that come closest to background work, and clarifies what async concurrency does and does not imply.

---

## 1. The One-Shot Execution Model

```
User/AI client
      │
      ▼
droidrun run <task>    ← process starts
      │
      ▼
[observe → plan → act] × N steps   (max 15 by default)
      │
      ▼
result printed / returned
      │
      ▼
process exits          ← nothing persists
```

Each run is:
- A **single Python process** with a single event loop.
- **Bounded** by `max_steps` (default 15) and a wall-clock budget implied by the LLM timeout.
- **Stateless** — no data is written to a database or shared memory between runs.

---

## 2. What Comes Closest to Background Work

### 2.1 MCP server — persistent stdio process

`mcp_server.py` is a long-lived process, but it is **not a background job** in the traditional sense:

- It does not run in the background on its own initiative.
- It is launched and managed by the AI client (e.g., Claude Desktop) as a child process.
- It blocks on `stdin.read()` waiting for JSON-RPC requests.
- It spawns a **new `droidrun` subprocess per tool call** and is otherwise idle.

There is no work happening inside `mcp_server.py` between tool calls.

### 2.2 `auto_setup` — pre-flight check per run

Before every `droidrun run`, DroidRun optionally checks whether the Portal APK is installed and installs it if missing. This looks like a background daemon check, but it is actually:

- Synchronous.
- Inline with the main process startup.
- Only triggered if `auto_setup=true` in config.
- Not repeated if the APK is already installed (check takes <100 ms).

### 2.3 LlamaIndex Workflow steps — async, not parallel

LlamaIndex `Workflow` steps are `async def` coroutines that run inside a single `asyncio` event loop. The word "async" here means non-blocking I/O (LLM calls, HTTP to Portal APK), **not** parallel background threads. At any given moment, only one step is executing. The event loop multiplexes I/O waits.

There is no thread pool, no process pool, and no inter-process communication between steps.

### 2.4 `adb_find_port.ps1` — user-schedulable, not built-in

`adb_find_port.ps1` scans a subnet for devices advertising port 5555. It can be placed on a Windows Task Scheduler recurring trigger by the user, but:

- DroidRun itself never calls this script.
- There is no built-in mechanism to run it on a schedule.
- It produces console output only; it does not update any config file or registry.

### 2.5 PostHog telemetry — fire-and-forget HTTP

Each CLI invocation sends a single anonymous telemetry event to PostHog:

- The HTTP call is made asynchronously (`asyncio.ensure_future` or equivalent).
- It is **not scheduled** — it fires once per process, at startup.
- If the network is unavailable, the exception is silently swallowed.
- No retry, no queue, no local buffer.

This is the closest thing to a "background async task" in the codebase, and it is ephemeral: it lives only as long as the CLI process.

### 2.6 `TrajectoryWriter` — async file writes per step

When `save_trajectory != "none"`, `TrajectoryWriter` writes a JSON file after each observe-act step:

- Writes use `aiofiles` (async file I/O) so they do not block the event loop.
- They run as `asyncio` tasks within the same event loop as the workflow.
- There is no separate writer thread or process.
- Files accumulate on disk in `trajectories/<timestamp>/`; nothing reads them back during the run.

---

## 3. What Does NOT Exist

| Pattern | Present in DroidRun? | Notes |
|---------|----------------------|-------|
| Daemon process | No | — |
| Cron / scheduled task | No | Users may add their own via Task Scheduler / cron |
| Background thread | No | Pure asyncio, single thread |
| Thread pool (`ThreadPoolExecutor`) | No | — |
| Process pool | No | — |
| Message queue (Celery, Redis, etc.) | No | — |
| WorkManager (Android) | No | DroidRun is a Python host; it does not run on Android |
| Polling loop | No | Each step is event-driven by LLM response |
| WebSocket server | No | — |
| Persistent database | No | No DB of any kind |
| Retry queue | No | Fallback is attempted once inline, then fails |
| Health-check heartbeat | No | — |

---

## 4. Lifecycle Boundaries

```
Before run                During run                After run
─────────────────────     ────────────────────────  ─────────────────────
Nothing. DroidRun         Single asyncio loop:      Nothing. Process exits.
does not exist.           observe → act × N steps   Config file and
Config file exists        Async file writes         trajectory files
on disk (user-managed).   (TrajectoryWriter).       remain on disk.
                          Fire-and-forget telemetry.
```

---

## 5. Implications for Operators

- **No process supervisor needed.** There is nothing to keep alive between runs.
- **No memory leaks across runs.** Each run starts fresh.
- **Concurrency is safe by isolation.** Two simultaneous `droidrun run` invocations on the same device will race on the physical device UI, not on shared memory — DroidRun has no locking mechanism for this.
- **MCP server restart is safe.** If `mcp_server.py` is killed and restarted, no in-flight state is lost (there is none).
- **Trajectory cleanup is manual.** `trajectories/` grows without bound; users must prune it themselves.
