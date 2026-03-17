# CI/CD Pipeline Documentation

**Version:** Internal v1.0  
**Last updated:** 2026-03-16  
**Source:** `droidrun/src/.github/workflows/` (6 files scanned)

---

## Summary

| Repo | CI/CD | Workflows | Notes |
|------|-------|-----------|-------|
| `droidrun` | ✓ Yes | 6 GitHub Actions workflows | Upstream library (github.com/droidrun/droidrun) via git submodule |
| `open--claw` | ✗ No | None | Manual build scripts only (see Android section) |
| `AI-Project-Manager` | ✗ No | None | Docs-only repo; CI optional but recommended |

---

## droidrun — GitHub Actions Workflows

These workflows exist in `droidrun/src/.github/workflows/` (the upstream git submodule).
They belong to the **upstream open-source project** (github.com/droidrun/droidrun), not to
the local `ynotfins/droidrun` repository. They run against the upstream repo's GitHub environment.

### 1. `black.yml` — Code Formatting Lint

| Field | Value |
|-------|-------|
| **Trigger** | `push`, `pull_request` (all branches) |
| **Runner** | `ubuntu-latest` |
| **Python** | 3.13 |
| **Tool** | `psf/black@stable` (version 25.9.0) |
| **Action** | Checks all Python files with `--check --diff --verbose` |
| **Artifacts** | None |
| **PASS criteria** | All Python files formatted to Black standard |
| **FAIL behavior** | Workflow fails; diff shows which lines need reformatting |

**Purpose:** Enforces consistent Python code formatting across the DroidRun library. Blocks merges if code is not Black-formatted.

---

### 2. `bounty.yml` — GitHub Project V2 Issue Labeling

| Field | Value |
|-------|-------|
| **Trigger** | `issues: labeled` |
| **Runner** | `ubuntu-latest` |
| **Auth** | `secrets.BOUNTY_SECRET` (org-level GitHub secret) |
| **Action** | Updates issue status in GitHub Project V2 (project #2, org: droidrun) when an issue label changes |
| **Artifacts** | None |

**Purpose:** Automatically syncs issue labels to a GitHub Project V2 board status field for bounty tracking. Organization-level GitHub API + GraphQL. Not relevant to local deployment.

---

### 3. `claude-code-review.yml` — AI Code Review on Pull Requests

| Field | Value |
|-------|-------|
| **Trigger** | `pull_request: [opened, synchronize]` |
| **Runner** | `ubuntu-latest` |
| **Permissions** | `contents: read`, `pull-requests: write`, `issues: read`, `id-token: write` |
| **Action** | Claude AI reviews PR code changes and posts comments on the PR |
| **Artifacts** | None |

**Purpose:** Automated AI-powered code review on every PR to the upstream DroidRun repo. Requires Claude API access configured in the upstream GitHub Actions environment.

---

### 4. `claude.yml` — Claude AI Issue/PR Agent

| Field | Value |
|-------|-------|
| **Trigger** | `issue_comment: created`, `pull_request_review_comment: created`, `issues: [opened, assigned]`, `pull_request_review: submitted` |
| **Condition** | Only runs if comment/body contains `@claude` |
| **Runner** | `ubuntu-latest` |
| **Permissions** | `contents: read`, `pull-requests: read`, `issues: read`, `id-token: write`, `actions: read` |
| **Action** | Claude AI responds to `@claude` mentions in issues and PRs |
| **Artifacts** | None |

**Purpose:** Interactive AI assistant for issue discussion and PR review in the upstream repo. Invoked on-demand via `@claude` mentions.

---

### 5. `docker.yml` — Docker Image Build & Publish

| Field | Value |
|-------|-------|
| **Trigger** | `push: tags: v*` (semantic version tags only) |
| **Runner** | `ubuntu-latest` |
| **Registry** | `ghcr.io` (GitHub Container Registry) |
| **Image** | `ghcr.io/droidrun/droidrun` |
| **QEMU** | Multi-platform build support |
| **Permissions** | `contents: read`, `packages: write`, `attestations: write`, `id-token: write` |
| **Artifacts** | Docker image pushed to ghcr.io |

**Purpose:** Publishes a Docker image of DroidRun to GitHub Container Registry on every version tag. The image can be used for server-side Android farm deployments (not relevant to our Windows/ADB setup).

---

### 6. `publish.yml` — PyPI Package Publication

| Field | Value |
|-------|-------|
| **Trigger** | `push` (all; but jobs only run on `refs/tags/v*`) |
| **Jobs** | `version-check` → `build` → `publish-to-testpypi` → `publish-to-pypi` |
| **Runner** | `ubuntu-latest` |
| **Python** | `3.x` |
| **Build tool** | `pypa/build` |
| **Artifacts** | Python wheel + source tarball uploaded to TestPyPI and PyPI |

**Purpose:** Publishes the `droidrun` Python package to PyPI on version tag pushes. Verifies tag matches `pyproject.toml` version before publishing. Requires PyPI OIDC trust configured in the upstream GitHub environment.

**Flow:**
```
git push v0.5.1
  → version-check: confirms tag == pyproject.toml version
  → build: python -m build → dist/
  → publish-to-testpypi: pypa/gh-action-pypi-publish (TestPyPI)
  → publish-to-pypi: pypa/gh-action-pypi-publish (PyPI)
```

---

## open--claw — No CI/CD Workflows

`D:\github\open--claw\.github\` does not exist. No GitHub Actions workflows are configured.

### Manual Build Process — Android APK

The Android app is built manually using batch scripts in the repository root:

#### Debug Build (`build_apk.bat`)
```batch
:: Sets JAVA_HOME to Eclipse Adoptium JDK 17.0.16.8
:: Runs: gradlew.bat assembleDebug
:: Output: vendor/openclaw/apps/android/app/build/outputs/apk/debug/openclaw-<version>-debug.apk
```

APK naming format: `openclaw-<versionName>-<buildType>.apk` (configured in `build.gradle.kts` via `androidComponents.onVariants`)

#### Release Build (`build_apk_fixed.bat`)
```batch
:: Same Java setup
:: Requires ~/.gradle/gradle.properties with signing config:
::   OPENCLAW_ANDROID_STORE_FILE, OPENCLAW_ANDROID_STORE_PASSWORD
::   OPENCLAW_ANDROID_KEY_ALIAS, OPENCLAW_ANDROID_KEY_PASSWORD
:: Runs: gradlew.bat assembleRelease
:: Output: vendor/openclaw/apps/android/app/build/outputs/apk/release/openclaw-<version>-release.apk
```

### Android Build Variants

| Variant | Minify | Shrink | Signing | Debug Symbols |
|---------|--------|--------|---------|---------------|
| `debug` | Off | Off | Debug (auto) | Full |
| `release` | On (R8) | On | Release keystore | Stripped |

**Prerequisites:**
- Java: Eclipse Adoptium JDK 17 at `C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot`
- Android SDK installed (Gradle downloads it if `ANDROID_HOME` not set)
- Release: `~/.gradle/gradle.properties` with signing properties (see `configuration.md`)

**ABIs built:** `armeabi-v7a`, `arm64-v8a`, `x86`, `x86_64` (all major ABIs)

### Recommended CI/CD for open--claw (Gap)

The following CI/CD does not exist but is recommended for production readiness:

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `android-debug.yml` | Push to `main`, PRs | Build debug APK, upload as artifact |
| `android-release.yml` | Tag `v*` | Build signed release APK, create GitHub Release |
| `gateway-smoke.yml` | Push to `main` | Start OpenClaw gateway, run health check |
| `lint.yml` | Push, PRs | TypeScript type check + ESLint |

---

## AI-Project-Manager — No CI/CD Workflows

`D:\github\AI-Project-Manager\.github\` does not exist. This is expected — the repo contains only Markdown documentation and Cursor rule files. No compilation or deployment is needed.

### Optional CI for Docs (Not implemented)

| Workflow | Purpose |
|----------|---------|
| `link-check.yml` | Validate internal Markdown links on push |
| `secrets-scan.yml` | Scan for accidentally committed secrets on every PR |

---

## Local Startup — Replacing CI for open--claw Gateway

Since open--claw has no CI, gateway startup and validation is manual:

```powershell
# Full startup (recommended — uses Bitwarden secrets):
bws run --project-id f14a97bb-5183-4b11-a6eb-b3fe0015fedf -- pwsh -NoProfile -File "$HOME\.openclaw\start-cursor-with-secrets.ps1"

# Manual gateway health check (after startup):
wsl -- bash -lc "source ~/.nvm/nvm.sh && cd ~/openclaw-build && pnpm openclaw health"

# Expected healthy output:
# Agents: main (default)
# WhatsApp: linked
# Telegram: ok (@Sparky4bot)
# Signal: disabled
```

---

## Version Tracking

| Component | Current Version | How to Update |
|-----------|-----------------|---------------|
| OpenClaw gateway | 2026.3.8 | Update `vendor/openclaw/` + `VENDOR_PIN.md` |
| OpenClaw Android app | 2026.3.8 (versionCode 202603081) | Rebuild with `build_apk_fixed.bat` after gateway update |
| DroidRun library (`src/`) | 0.5.1 | `git submodule update --remote` + update `.venv` |
| DroidRun Portal (APK on phone) | 0.6.1 | Install new APK via `adb install` |
| Node.js | 22.x (nvm) | `nvm install --lts && nvm use --lts` |
| Python | 3.12.10 | Update `.venv` Python interpreter |
