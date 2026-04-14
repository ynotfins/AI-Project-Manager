# CI/CD — Current State

> **Honest status: No CI/CD pipeline is configured in this workspace.**

This document records what exists, what is missing, and what a future pipeline should look like.

---

## Current State

| Item | Status |
|---|---|
| `.github/workflows/` | Not found in this workspace |
| `azure-pipelines.yml` | Not found |
| `Makefile` CI targets | Not found |
| Automated test suite | Not found |
| Automated lint/format checks | Not automated (tools available, run manually) |
| Release pipeline | Unknown / Needs Verification |

### Upstream repo

The upstream repository at `github.com/droidrun/droidrun` **may** have CI workflows configured. This workspace is a local clone/fork — its CI state should be verified by inspecting the upstream repo directly.

---

## Tools Available (Manual Only)

All dev tools are installed under `pip install -e ".[dev]"` but must be run manually:

```bash
# Lint
ruff check droidrun/

# Format check
black --check droidrun/

# Type checking
mypy droidrun/

# Security scan
bandit -r droidrun/

# Dependency vulnerability audit
safety check
```

---

## Gaps

1. **No automated linting or formatting enforcement** — contributors can commit unformatted or linting-error code undetected.
2. **No automated test execution** — no test suite found; no pytest/unittest configuration.
3. **No build validation on PR** — `pip install -e .` is not verified automatically.
4. **No release pipeline** — version bumping, changelog generation, and PyPI/GitHub Releases publishing are all manual and undocumented.
5. **No security scanning on push** — `bandit` and `safety` are available but not triggered.

---

## Recommended Future CI Setup

The following is a reference design for a GitHub Actions pipeline. **Not yet implemented.**

### `.github/workflows/ci.yml` (proposed)

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint-and-format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: ruff check droidrun/
      - run: black --check droidrun/

  type-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: mypy droidrun/

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -e ".[dev]"
      - run: bandit -r droidrun/
      - run: safety check

  build-check:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -e ".[google,anthropic,openai,deepseek,ollama,dev]"
      - run: droidrun --help
```

### Notes on Android/Portal testing

- The Portal APK requires a physical Android device or a connected emulator — **not feasible in standard GitHub Actions**.
- Portal integration tests should be run locally or via a self-hosted runner with an attached device.
- ADB-dependent tests cannot run in the standard cloud CI environment.

---

## Priority Order for Implementation

1. Add `ruff` + `black` pre-commit hook (local enforcement, zero infrastructure)
2. Add GitHub Actions CI for lint, format, type-check, build-check
3. Add `bandit` + `safety` to CI
4. Define and write a basic unit test suite (no device required)
5. Design a release workflow (version bump → changelog → tag → PyPI publish)

---

## Related Files

- `docs/build-release-process.md` — build system details
- `pyproject.toml` — dev tool versions and configuration
