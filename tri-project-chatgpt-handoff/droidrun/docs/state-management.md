# State Management

DroidRun is a **stateless-per-run** system. All agent state is held in memory for the duration of a single `droidrun run` invocation and is discarded when the process exits (unless trajectory recording is enabled).

---

## Core State Objects

### `DroidAgentState`

**Location:** `src/droidrun/agent/droid/state.py`

The central Pydantic `BaseModel` that is passed through the entire LlamaIndex Workflow. It is shared across all sub-agents (ManagerAgent, ExecutorAgent, FastAgent, CodeActAgent, TextManipulator, etc.) via the workflow's shared context mechanism.

**Lifecycle:** Created once by `DroidAgent` at run start. Mutated in-place throughout the run. Discarded when the run completes.

**Key fields, grouped by concern:**

| Group | Fields | Purpose |
|---|---|---|
| Task | `instruction`, `step_number`, `runtype`, `user_id` | Top-level task identity |
| Device state (current) | `formatted_device_state`, `a11y_tree`, `phone_state`, `screenshot`, `focused_text`, `width`, `height` | What the screen looks like right now |
| Device state (previous) | `previous_formatted_device_state` | Before/after comparison for detecting stale states |
| App tracking | `current_package_name`, `current_activity_name`, `visited_packages`, `visited_activities`, `app_card` | Which app is open; telemetry |
| Thought/plan | `last_thought`, `previous_plan`, `progress_summary` | LLM reasoning continuity across steps |
| Planning | `plan`, `current_subgoal`, `answer` | Used by ManagerAgent (reasoning=True) |
| Action tracking | `action_history`, `summary_history`, `action_outcomes`, `error_descriptions`, `last_action`, `last_summary` | Step-by-step history passed into prompts |
| Memory | `manager_memory`, `fast_memory` | In-prompt note-taking; `fast_memory` capped at 10 items |
| Completion | `finished`, `success` | Set by `complete()` tool; checked each loop iteration |
| Message history | `message_history` | Full `ChatMessage` list for stateful agents (FastAgent/CodeAct) |
| Error handling | `error_flag_plan`, `err_to_manager_thresh` | Escalate repeated executor failures to manager |
| Script tracking | `scripter_history`, `last_scripter_message`, `last_scripter_success` | ScripterAgent state |
| Text manipulation | `has_text_to_modify`, `text_manipulation_history`, `last_text_manipulation_success` | TextManipulator state |
| User message queue | `pending_user_messages`, `workflow_completed` | Mid-run message injection (see below) |
| Custom | `custom_variables`, `output_dir` | User-defined key-value store |

**Notable methods on the state object:**

```python
await state.remember(information)   # Appends to fast_memory (max 10 items, FIFO)
await state.complete(success, reason)  # Sets finished=True, success, answer
state.queue_user_message(message)   # Enqueue a mid-run human message
state.drain_user_messages()         # Atomically consume all pending messages
state.update_current_app(pkg, activity)  # Update + fire telemetry event
```

---

### `ActionContext`

**Location:** `src/droidrun/agent/action_context.py`

A lightweight dependency-injection container passed into every action function. It is **not** a Pydantic model — it is a plain Python class instantiated once per step.

```python
class ActionContext:
    driver: DeviceDriver        # Talks to the Android device via ADB
    ui: UIState | None          # Refreshed snapshot before each tool execution
    shared_state: DroidAgentState   # The single shared state (mutated in place)
    state_provider: StateProvider   # Re-fetches UI state on demand
    app_opener_llm: ...         # LLM instance for AppStarter sub-workflow
    credential_manager: CredentialManager | None
    streaming: bool
```

`ActionContext` is rebuilt each step (so `ui` is fresh), but `shared_state` is the same object throughout the run.

---

### `ActionResult`

**Location:** `src/droidrun/agent/action_result.py`

```python
@dataclass
class ActionResult:
    success: bool
    summary: str
```

Returned by every action function. `summary` is appended to `DroidAgentState.summary_history` and fed back into the LLM context at the next step. `success` updates `action_outcomes`.

---

## Workflow Handler (LlamaIndex)

**Framework:** LlamaIndex `Workflow` (async, event-driven)

DroidAgent, ManagerAgent, and ExecutorAgent are all implemented as LlamaIndex `Workflow` subclasses. The framework handles:

- Async step routing via typed `Event` objects
- Concurrent sub-workflow execution
- `StopEvent` / `ResultEvent` terminal events

`DroidAgentState` is passed into the workflow as a shared context object, meaning all steps see the same mutable state. LlamaIndex's Workflow is **single-threaded async** (event loop based), so there are no shared-memory race conditions between steps — each step runs to completion before the next is dispatched. However, if sub-workflows run concurrently (e.g., parallel tool calls), the shared state **can** be mutated concurrently; the LlamaIndex implementation serialises event dispatch at the `ctx.send_event` level, making this safe in practice.

---

## Trajectory Recording

**Location:** `src/droidrun/agent/utils/trajectory.py`

Trajectories are **opt-in**. When enabled (config: `save_trajectory != "none"`), the `Trajectory` object creates a timestamped folder under `trajectories/` (relative to cwd) and writes incrementally:

```
trajectories/
└── 20250316_143052_a1b2c3d4/
    ├── trajectory.json        # Serialised LlamaIndex Events
    ├── macro.json             # Low-level action sequence with timestamps
    └── screenshots/
        └── trajectory.gif    # Animated screenshot sequence
```

- `trajectory.json` — all `Event` objects emitted during the run, serialised by `make_serializable()`
- `macro.json` — populated from `RecordingDriver.log` (if recording driver is used); contains raw action types, coordinates, timestamps
- Screenshots are captured as `bytes` and assembled into a GIF at save time

Trajectory data is **append-only** during the run. There is no partial-resume capability — if the process dies mid-run, the trajectory folder may be incomplete.

---

## Queued User Messages

`DroidAgentState.pending_user_messages` implements a mid-run injection queue. External callers (e.g., a UI frontend or a test harness) can call `state.queue_user_message(msg)` while the agent is running. At the start of each step, the agent calls `state.drain_user_messages()` to consume and inject those messages into the LLM context as if the user typed them mid-task.

Guard: `queue_user_message` raises `RuntimeError` if `workflow_completed` is `True`.

---

## UI State Caching

The `UIState` snapshot (accessibility tree + formatted text + element index) is fetched **once per step**, before tool execution. It is stored in `ActionContext.ui` for the duration of that step. Actions that call `get_ui_state()` explicitly trigger a fresh fetch via `state_provider.get_state()`.

There is **no cross-step UI cache**. Each step starts with a fresh fetch from the Portal APK, with retry/backoff logic (up to 7 attempts, delays: 1s, 2s, 3s, 5s, 8s, 10s, 10s) and mid-retry Portal recovery (restart accessibility service + TCP socket server).

---

## Shared State Across Sub-Agents (reasoning=True)

When `reasoning=True`, `DroidAgentState` is shared between:

- **ManagerAgent** — writes `plan`, `current_subgoal`, `manager_memory`, `progress_summary`
- **ExecutorAgent** — reads `current_subgoal`, writes `action_history`, `last_action`, `last_summary`, `error_flag_plan`

The Manager reads Executor's outcomes each iteration to decide the next subgoal. There is no message-passing between agents — they communicate exclusively through mutations to the shared `DroidAgentState`.

---

## No Persistence Between Runs

- No database, no SQLite, no file-backed session store
- Each `droidrun run` starts with a fresh `DroidAgentState`
- `fast_memory` and `manager_memory` exist only for the duration of one run
- Trajectory files are the only persistent artifact (optional, disk-based)
- Config is read from `~/.config/droidrun/config.yaml` at startup but is not written back during a run
