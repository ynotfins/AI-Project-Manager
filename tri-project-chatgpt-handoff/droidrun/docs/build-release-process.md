# Build & Release Process

## Build System

DroidRun uses **hatchling** as its build backend, configured in `pyproject.toml`.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Package Info

| Field | Value |
|---|---|
| Package name | `droidrun` |
| Version | `0.5.1` (Beta) |
| License | MIT |
| Python versions | 3.11–3.14 (exclusive upper bound) |
| Entry point | `droidrun = "droidrun.cli.main:cli"` |

## Install Commands

### Minimal install
```bash
pip install -e .
```

### Full install with all LLM providers and dev tools
```bash
pip install -e ".[google,anthropic,openai,deepseek,ollama,dev]"
```

### Available extras

| Extra | Includes |
|---|---|
| `google` | `llama-index-llms-google-genai` |
| `anthropic` | `anthropic`, `llama-index-llms-anthropic` |
| `openai` | already in core |
| `deepseek` | `llama-index-llms-deepseek` |
| `ollama` | `llama-index-llms-ollama` |
| `langfuse` | `langfuse`, `openinference-instrumentation-llama-index` |
| `dev` | `black`, `ruff`, `mypy`, `bandit`, `safety` |

## Dev Tools

These tools are available under the `dev` extra but **not automated** (no CI pipeline):

| Tool | Purpose | Run manually |
|---|---|---|
| `black==25.9.0` | Code formatting | `black droidrun/` |
| `ruff>=0.13.0` | Linting | `ruff check droidrun/` |
| `mypy>=1.0.0` | Static type checking | `mypy droidrun/` |
| `bandit>=1.8.6` | Security scanning | `bandit -r droidrun/` |
| `safety>=3.2.11` | Dependency vulnerability audit | `safety check` |

## Workspace Setup (Windows)

The workspace includes a one-time setup script for the Python virtual environment:

```powershell
# Run once to create venv and install droidrun with all extras
.\scripts\setup_windows_host.ps1
```

This script creates a venv, installs the package in editable mode, and configures the path.

## Portal APK

The Portal APK (`com.droidrun.portal`) is a **separate Android build** — its source is not in this repository.

- Hosted on GitHub Releases for the upstream repo
- Install via: `adb install droidrun-portal.apk`
- Required capabilities: Accessibility Service, HTTP server on port 8080

## No CI/CD Pipeline

> **Unknown / Needs Verification** — No CI/CD pipeline configuration was found in this workspace (no `.github/workflows/`, no `azure-pipelines.yml`, no `Makefile` targets). All build validation is currently manual.

See [`docs/ci-cd.md`](ci-cd.md) for the current state and recommendations.

## Version Strategy

> **Unknown / Needs Verification** — Semver (`MAJOR.MINOR.PATCH`) is assumed from `v0.5.1`. No version bump scripts, changelog tooling, or tagging conventions were found in the workspace. The upstream repo may have a release process — check `github.com/droidrun/droidrun`.

## Release Process

> **Unknown / Needs Verification** — No release scripts were found in this workspace. Assumed flow until verified:

1. Bump version in `pyproject.toml`
2. Run dev tools manually (`ruff`, `black`, `mypy`, `bandit`, `safety`)
3. Build: `pip install -e .` to validate
4. Tag release in git
5. Push to upstream; upstream may publish to PyPI or GitHub Releases

## Related Files

- `pyproject.toml` — single source of truth for version, deps, extras, entry points
- `scripts/setup_windows_host.ps1` — one-time dev environment bootstrap
- `docs/dependency-inventory.md` — full dependency list with risk notes
