# Software Bill of Materials (SBOM)

**Version:** Internal v1.0  
**Last updated:** 2026-03-16  
**Sources:**
- `open--claw/vendor/openclaw/package.json` (npm dependencies)
- `open--claw/vendor/openclaw/apps/android/app/build.gradle.kts` (Android/Kotlin dependencies)
- `droidrun/src/pyproject.toml` (Python dependencies)

---

## Summary

| Project | Runtime | Package Manager | Direct Dependencies |
|---------|---------|-----------------|---------------------|
| open--claw (Node.js) | WSL2, Node.js 22 | pnpm | 52 npm packages |
| open--claw (Android) | Android 16, JVM 17 | Gradle (Kotlin DSL) | 28 Android/JVM packages |
| droidrun | Windows, Python 3.12.10 | pip / hatchling | 18 Python packages |
| AI-Project-Manager | None (docs-only) | None | **0 dependencies** |

> AI-Project-Manager is a documentation and governance repository. It contains no runtime code and has no package dependencies.

---

## open--claw — Node.js Dependencies

**Source:** `vendor/openclaw/package.json` · **License:** MIT (OpenClaw itself)  
**Runtime:** Node.js v22 (nvm), pnpm 10.23.0

### Core AI & Agent

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@agentclientprotocol/sdk` | 0.15.0 | MIT | Low | ACP protocol SDK for agent communication |
| `@mariozechner/pi-agent-core` | 0.57.1 | MIT | Low | Pi agent core (reasoning engine) |
| `@mariozechner/pi-ai` | 0.57.1 | MIT | Low | Pi AI model interface |
| `@mariozechner/pi-coding-agent` | 0.57.1 | MIT | Low | Pi coding agent |
| `@mariozechner/pi-tui` | 0.57.1 | MIT | Low | Pi terminal UI |
| `@sinclair/typebox` | 0.34.48 | MIT | Low | JSON Schema + TypeScript types |
| `ajv` | ^8.18.0 | MIT | Low | JSON Schema validation |
| `zod` | ^4.3.6 | MIT | Low | TypeScript schema validation |

### Messaging Channels

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@whiskeysockets/baileys` | 7.0.0-rc.9 | GPL-3.0 | **Medium** | WhatsApp unofficial API. GPL license — review before redistribution. |
| `grammy` | ^1.41.1 | MIT | Low | Telegram Bot API framework |
| `@grammyjs/runner` | ^2.0.3 | MIT | Low | grammy concurrent update runner |
| `@grammyjs/transformer-throttler` | ^1.2.1 | MIT | Low | grammy rate limiter |
| `@buape/carbon` | 0.0.0-beta-20260216184201 | MIT | Low | Discord integration |
| `discord-api-types` | ^0.38.41 | MIT | Low | Discord API type definitions |
| `@discordjs/voice` | ^0.19.0 | MIT | Low | Discord voice support |
| `@slack/bolt` | ^4.6.0 | MIT | Low | Slack app framework |
| `@slack/web-api` | ^7.14.1 | MIT | Low | Slack Web API client |
| `@larksuiteoapi/node-sdk` | ^1.59.0 | MIT | Low | Lark/Feishu integration |
| `@line/bot-sdk` | ^10.6.0 | Apache-2.0 | Low | LINE messaging |

### AWS & Cloud

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@aws-sdk/client-bedrock` | ^3.1004.0 | Apache-2.0 | Low | AWS Bedrock LLM integration |

### Web & HTTP

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `express` | ^5.2.1 | MIT | Low | HTTP server framework |
| `undici` | ^7.22.0 | MIT | Low | HTTP/1.1 + HTTP/2 client |
| `ws` | ^8.19.0 | MIT | Low | WebSocket server/client |
| `https-proxy-agent` | ^7.0.6 | MIT | Low | HTTPS proxy support |
| `playwright-core` | 1.58.2 | Apache-2.0 | Low | Browser automation (core only — no browsers bundled) |

### File Processing & Data

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `pdfjs-dist` | ^5.5.207 | Apache-2.0 | Low | PDF parsing |
| `sharp` | ^0.34.5 | Apache-2.0 | Low | Image processing (native bindings) |
| `file-type` | ^21.3.0 | MIT | Low | File type detection |
| `jszip` | ^3.10.1 | MIT | Low | ZIP file handling |
| `tar` | 7.5.11 | ISC | Low | TAR archive handling |
| `@mozilla/readability` | ^0.6.0 | Apache-2.0 | Low | Web page content extraction |
| `linkedom` | ^0.18.12 | ISC | Low | Lightweight DOM parser |
| `markdown-it` | ^14.1.1 | MIT | Low | Markdown parser/renderer |
| `yaml` | ^2.8.2 | ISC | Low | YAML parser |
| `json5` | ^2.2.3 | MIT | Low | JSON5 parser |
| `sqlite-vec` | 0.1.7-alpha.2 | MIT | Low | SQLite vector extension (local memory) |

### Media & Audio

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `node-edge-tts` | ^1.2.10 | MIT | Low | Text-to-speech via Edge TTS |
| `opusscript` | ^0.1.1 | MIT | Low | Opus audio codec |

### Utilities & Terminal

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@clack/prompts` | ^1.1.0 | MIT | Low | Terminal prompts |
| `chalk` | ^5.6.2 | MIT | Low | Terminal colors |
| `cli-highlight` | ^2.1.11 | ISC | Low | Syntax highlighting for CLI |
| `commander` | ^14.0.3 | MIT | Low | CLI argument parsing |
| `tslog` | ^4.10.2 | MIT | Low | TypeScript structured logging |
| `croner` | ^10.0.1 | MIT | Low | Cron scheduling |
| `chokidar` | ^5.0.0 | MIT | Low | File watcher |
| `dotenv` | ^17.3.1 | BSD-2-Clause | Low | .env file loader |
| `ipaddr.js` | ^2.3.0 | MIT | Low | IP address parsing |
| `jiti` | ^2.6.1 | MIT | Low | TypeScript/ESM runtime loader |
| `long` | ^5.3.2 | Apache-2.0 | Low | 64-bit integer support |
| `osc-progress` | ^0.3.0 | MIT | Low | Terminal progress bar |
| `qrcode-terminal` | ^0.12.0 | MIT | Low | QR code display in terminal |

### Network Discovery

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@homebridge/ciao` | ^1.3.5 | MIT | Low | mDNS/DNS-SD (Bonjour) for Tailscale node discovery |

### Peer Dependencies (Optional)

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@napi-rs/canvas` | ^0.1.89 | MIT | Low | Canvas rendering (optional, native) |
| `node-llama-cpp` | 3.16.2 | MIT | Low | Local LLM inference via llama.cpp (optional) |

### Native System Access

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `@lydell/node-pty` | 1.2.0-beta.3 | MIT | **Medium** | Pseudo-terminal (shell execution). Native binding — review sandbox config. |

---

## open--claw — Android App Dependencies

**Source:** `vendor/openclaw/apps/android/app/build.gradle.kts`  
**Runtime:** Android 16, minSdk 31, targetSdk 36, JVM 17, Kotlin, Jetpack Compose

### AndroidX & Jetpack

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `androidx.compose:compose-bom` | 2026.02.00 | Apache-2.0 | Low | Compose BOM (all compose versions from this) |
| `androidx.core:core-ktx` | 1.17.0 | Apache-2.0 | Low | Android KTX extensions |
| `androidx.lifecycle:lifecycle-runtime-ktx` | 2.10.0 | Apache-2.0 | Low | Lifecycle-aware coroutines |
| `androidx.activity:activity-compose` | 1.12.2 | Apache-2.0 | Low | Activity + Compose integration |
| `androidx.webkit:webkit` | 1.15.0 | Apache-2.0 | Low | WebView (modern) |
| `androidx.compose.ui:ui` | BOM-managed | Apache-2.0 | Low | Compose UI core |
| `androidx.compose.material3:material3` | BOM-managed | Apache-2.0 | Low | Material Design 3 |
| `androidx.compose.material:material-icons-extended` | BOM-managed | Apache-2.0 | Low | Full icon set (R8 tree-shakes unused) |
| `androidx.navigation:navigation-compose` | 2.9.7 | Apache-2.0 | Low | Compose navigation |
| `androidx.security:security-crypto` | 1.1.0 | Apache-2.0 | Low | Encrypted SharedPreferences |
| `androidx.exifinterface:exifinterface` | 1.4.2 | Apache-2.0 | Low | Image EXIF data |
| `androidx.camera:camera-*` | 1.5.2 | Apache-2.0 | Low | CameraX (5 modules) |

### Material & UI

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `com.google.android.material:material` | 1.13.0 | Apache-2.0 | Low | Material Components |

### Kotlin Libraries

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `org.jetbrains.kotlinx:kotlinx-coroutines-android` | 1.10.2 | Apache-2.0 | Low | Coroutines for Android |
| `org.jetbrains.kotlinx:kotlinx-serialization-json` | 1.10.0 | Apache-2.0 | Low | JSON serialization |

### Networking

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `com.squareup.okhttp3:okhttp` | 5.3.2 | Apache-2.0 | Low | HTTP client |
| `dnsjava:dnsjava` | 3.6.4 | BSD-3-Clause | Low | DNS-SD for Tailscale node discovery |

### Cryptography

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `org.bouncycastle:bcprov-jdk18on` | 1.83 | MIT | Low | Cryptographic provider |

### Content Rendering

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `org.commonmark:commonmark` | 0.27.1 | BSD-2-Clause | Low | Markdown parser |
| `org.commonmark:commonmark-ext-*` | 0.27.1 | BSD-2-Clause | Low | Markdown extensions (4 modules) |

### QR Code

| Package | Version | License | Risk | Notes |
|---------|---------|---------|------|-------|
| `com.journeyapps:zxing-android-embedded` | 4.3.0 | Apache-2.0 | Low | QR code scanner |

### Test Dependencies

| Package | Version | License | Notes |
|---------|---------|---------|-------|
| `junit:junit` | 4.13.2 | EPL-1.0 | Unit tests |
| `kotlinx-coroutines-test` | 1.10.2 | Apache-2.0 | Coroutine testing |
| `io.kotest:kotest-runner-junit5-jvm` | 6.1.3 | Apache-2.0 | Kotest runner |
| `io.kotest:kotest-assertions-core-jvm` | 6.1.3 | Apache-2.0 | Kotest assertions |
| `com.squareup.okhttp3:mockwebserver` | 5.3.2 | Apache-2.0 | HTTP mock server |
| `org.robolectric:robolectric` | 4.16.1 | Apache-2.0 | Android unit testing on JVM |
| `org.junit.vintage:junit-vintage-engine` | 6.0.2 | EPL-2.0 | JUnit 4 compatibility |

---

## droidrun — Python Dependencies

**Source:** `droidrun/src/pyproject.toml` · **License:** MIT (DroidRun itself)  
**Runtime:** Python 3.12.10, hatchling build system  
**Note:** `src/` is a git submodule pointing to `github.com/droidrun/droidrun` (upstream project)

### Core Runtime

| Package | Version Constraint | License | Risk | Notes |
|---------|--------------------|---------|------|-------|
| `llama-index` | ==0.14.4 | MIT | Low | LLM orchestration framework (pinned) |
| `llama-index-workflows` | ==2.8.3 | MIT | Low | LlamaIndex workflow engine (pinned) |
| `llama-index-llms-openai` | >=0.5.6 | MIT | Low | OpenAI provider |
| `llama-index-llms-openai-like` | >=0.5.1 | MIT | Low | OpenAI-compatible providers (OpenRouter) |
| `llama-index-llms-google-genai` | >=0.8.5 | MIT | Low | Google Gemini provider |
| `llama-index-llms-ollama` | >=0.7.2 | MIT | Low | Ollama local LLM provider |
| `llama-index-llms-openrouter` | >=0.4.2 | MIT | Low | OpenRouter provider |
| `mcp` | >=1.26.0 | MIT | Low | Model Context Protocol SDK |
| `pydantic` | >=2.11.10 | MIT | Low | Data validation |
| `async_adbutils` | latest | Apache-2.0 | Low | Async ADB utilities |

### Observability & Tracing

| Package | Version Constraint | License | Risk | Notes |
|---------|--------------------|---------|------|-------|
| `arize-phoenix` | >=12.3.0 | BSD-3-Clause | Low | LLM tracing / observability |
| `llama-index-callbacks-arize-phoenix` | >=0.6.1 | MIT | Low | LlamaIndex → Phoenix bridge |
| `posthog` | >=6.7.6 | MIT | Low | Product analytics (upstream library) |

### HTTP & I/O

| Package | Version Constraint | License | Risk | Notes |
|---------|--------------------|---------|------|-------|
| `httpx` | >=0.27.0 | BSD-3-Clause | Low | Async HTTP client |
| `aiofiles` | >=25.1.0 | Apache-2.0 | Low | Async file I/O |
| `python-dotenv` | >=1.2.1 | BSD-3-Clause | Low | .env file loader |

### UI

| Package | Version Constraint | License | Risk | Notes |
|---------|--------------------|---------|------|-------|
| `rich` | >=14.1.0 | MIT | Low | Rich terminal output |
| `textual` | >=6.11.0 | MIT | Low | Terminal UI framework |
| `mobilerun-sdk` | latest | MIT | Low | Mobile run SDK |

### Optional — LLM Providers (installed in this deployment)

| Package | Version Constraint | License | Installed Extra |
|---------|--------------------|---------|----------------|
| `llama-index-llms-deepseek` | >=0.2.1 | MIT | `deepseek` |

### Optional — Development Tools

| Package | Version | License | Notes |
|---------|---------|---------|-------|
| `black` | ==25.9.0 | MIT | Code formatter |
| `ruff` | >=0.13.0 | MIT | Linter |
| `mypy` | >=1.0.0 | MIT | Type checker |
| `bandit` | >=1.8.6 | Apache-2.0 | Security linter |
| `safety` | >=3.2.11 | MIT | Dependency vulnerability scanner |

---

## AI-Project-Manager

**No dependencies.** This repository is documentation-only and contains no runtime code,
no `package.json`, no `requirements.txt`, no `pyproject.toml`, and no `build.gradle`.

---

## License Risk Summary

| Risk Level | Count | Packages |
|------------|-------|---------|
| **High** | 0 | — |
| **Medium** | 2 | `@whiskeysockets/baileys` (GPL-3.0), `@lydell/node-pty` (native shell access) |
| **Low** | ~94 | All others |

### Medium Risk Notes

**`@whiskeysockets/baileys` (GPL-3.0):**
- Provides WhatsApp connectivity via the unofficial multi-device protocol
- GPL-3.0 license requires source disclosure if distributed as part of a GPL work
- Internal deployment only — no redistribution occurs
- Risk: If system is ever commercialized as a product, this must be replaced with the official WhatsApp Business API

**`@lydell/node-pty` (native shell execution):**
- Provides pseudo-terminal for shell command execution within agent sessions
- Native binding with broad OS access; requires proper sandbox configuration
- Risk: Improperly configured `exec-approvals.json` could allow destructive commands
- Mitigation: Sandbox mode configuration in `openclaw.json`; approval gates in exec-policy
