# OpenClaw Worker Memory Flow

## Purpose
Define how Sparky and the curated 15-worker squad should use the repaired OpenMemory stack without cross-project contamination or context bloat.

## Scope
This document is subordinate to `docs/ai/architecture/NO_LOSS.md` and specializes it for the OpenClaw delivery team.

## Design Goals
- preserve durable team knowledge without loading whole histories into active context
- isolate OpenClaw runtime memory from governance and other repos
- let specialists hand off compact outputs to Sparky
- promote only validated knowledge into durable memory

## Project And Namespace Rules

### Project IDs
- governance memory: `R3lentless-Grind-Ecosystem`
- OpenClaw team memory: `ynotfins/open--claw`

### Core namespaces
- `openclaw/briefs`
- `openclaw/decisions`
- `openclaw/patterns`
- `openclaw/debug`
- `openclaw/reviews`
- `openclaw/evidence`
- `openclaw/releases`
- `openclaw/sessions`

### Optional worker-scoped namespaces
Use only when the worker role needs repeated durable recall:
- `openclaw/worker/sparky`
- `openclaw/worker/delivery-director`
- `openclaw/worker/product-manager`
- `openclaw/worker/software-architect`
- `openclaw/worker/code-reviewer`

Do not create per-worker namespaces for every employee unless repeated use proves they need one.

## Promotion Chain
Raw work must not go straight into durable memory.

1. Task output exists in runtime files, STATE, logs, or worker chat
2. Worker produces a compact packet output
3. Sparky or the responsible gate role validates it
4. Only the stable result is promoted to OpenMemory

## What Gets Stored

### Store in `openclaw/briefs`
- stable product briefs
- acceptance criteria
- non-goals that matter beyond one chat

### Store in `openclaw/decisions`
- architecture choices
- approved implementation direction
- accepted trade-offs
- team operating decisions from Sparky

### Store in `openclaw/patterns`
- reusable implementation patterns
- proven rollout/checklist patterns
- known handoff formats that reduce context

### Store in `openclaw/debug`
- root causes
- verified fixes
- recurring failure signatures

### Store in `openclaw/reviews`
- final review conclusions
- recurring code quality risks worth remembering

### Store in `openclaw/evidence`
- durable proof summaries only
- not raw screenshots or full logs

### Store in `openclaw/releases`
- release verdicts
- rollback lessons
- post-release anomalies that matter later

## What Must Not Be Stored
- full chat transcripts by default
- speculative reasoning that was not validated
- raw step-by-step terminal logs when a short conclusion exists
- quarantined content
- secrets, tokens, env values, or direct credential IDs
- other-project implementation details unless explicitly promoted to governance

## Standard Memory Packet By Role

### product-manager
- summary of brief
- acceptance criteria
- explicit non-goals

### software-architect or backend-architect
- chosen boundaries
- interfaces
- risk notes
- rejected alternatives if they matter later

### code-reviewer
- final findings summary
- recurring smells or risk patterns

### qa-evidence-collector
- proof summary
- what was tested
- what remains unverified

### reality-checker
- go/no-go summary
- blocking risk statements

### devops-automator
- deploy pattern
- rollback trigger
- operational caveats

### Sparky
- final decision
- corrections required
- accepted system direction

## Retrieval Order For OpenClaw Work
When starting a new OpenClaw task:

1. `openclaw/decisions`
2. `openclaw/patterns`
3. `openclaw/debug` if the task is a fix
4. `openclaw/briefs` if the task is feature work
5. `openclaw/reviews` and `openclaw/evidence` only when acceptance history matters
6. governance memory only for cross-project policy or tool rules

## Minimal Session-End Routine
At the end of a meaningful worker packet:

1. capture the outcome in `STATE.md`
2. decide whether the result is durable
3. if durable, promote one compact memory entry to the correct namespace
4. never promote the whole packet if a short validated summary is enough

## Ready For Live Team Use When
- OpenMemory retrieval works reliably at session start
- Sparky can promote decisions without manual repair work
- at least one internal packet has completed the full brief -> review -> evidence -> Sparky -> memory cycle
