## Extensions policy (governance + performance)

- **Default stance**: keep extensions **minimal** and **workspace-scoped** (Disable (Workspace) instead of uninstall).
- **Token discipline**: keep all “AI assist” extensions **disabled** unless explicitly needed for a session.
- **Two-machine reality**:
  - **ChaosCentral (128GB RAM / RTX 4070 SUPER)** can run quality-of-life extensions without concern.
  - **Laptop (16GB RAM)** should stay lean to avoid background churn, indexing overhead, and battery drain.

---

## AI-Project-Manager — ChaosCentral (enable/disable)

Enable:
- Auto Rename Tag
- DotENV
- EditorConfig for VS Code
- Error Lens
- ESLint
- GitLens — Git supercharged
- Highlight Matching Tag
- Path Intellisense
- Prettier — Code formatter
- Pretty TypeScript Errors
- WSL (AnySphere)
- YAML (Red Hat)
- Code Spell Checker
- PowerShell

Disable:
- Better Comments
- Color Highlight
- Container Tools
- Docker
- ES7+ React/Redux/React-Native snippets
- File Utils
- Gemini Code Assist
- Import Cost
- Material Icon Theme
- Python (AnySphere)
- Python (ms-python)
- Python Debugger
- Rainbow CSV
- Ruff
- Tailwind CSS IntelliSense
- TODO Highlight
- Todo Tree
- Turbo Console Log
- Database Client
- Database Client JDBC
- Enlighter for Cursor — Learn Vibe Coding
- Expo Tools
- Giga AI Context Manager
- i18n Ally

---

## open--claw — ChaosCentral (enable/disable)

Enable:
- Auto Rename Tag
- DotENV
- EditorConfig for VS Code
- Error Lens
- ESLint
- GitLens — Git supercharged
- Highlight Matching Tag
- Path Intellisense
- Prettier — Code formatter
- Pretty TypeScript Errors
- WSL (AnySphere)
- YAML (Red Hat)
- Code Spell Checker
- PowerShell

Disable:
- Better Comments
- Color Highlight
- Container Tools
- Docker
- ES7+ React/Redux/React-Native snippets
- File Utils
- Gemini Code Assist
- Import Cost
- Material Icon Theme
- Python (AnySphere)
- Python (ms-python)
- Python Debugger
- Rainbow CSV
- Ruff
- Tailwind CSS IntelliSense
- TODO Highlight
- Todo Tree
- Turbo Console Log
- Database Client
- Database Client JDBC
- Enlighter for Cursor — Learn Vibe Coding
- Expo Tools
- Giga AI Context Manager
- i18n Ally

Notes:
- Keep **Gemini Code Assist** disabled to avoid accidental token burn and duplicated AI surfaces.

---

## AI-Project-Manager — Laptop (Book4Chaos) (enable/disable)

Enable (lean set):
- EditorConfig for VS Code
- YAML (Red Hat)
- Code Spell Checker
- PowerShell
- GitLens — Git supercharged

Enable only if actively editing TS/JS in this repo:
- ESLint
- Prettier — Code formatter
- Pretty TypeScript Errors
- Path Intellisense

Disable (everything else by default):
- Auto Rename Tag (optional)
- DotENV (optional)
- Error Lens
- Highlight Matching Tag
- WSL (AnySphere) (enable only when you’re actually using WSL/Cursor integration)
- All Python/Docker/DB/AI/snippet extensions (as listed above)

---

## open--claw — Laptop (Book4Chaos) (enable/disable)

Enable (lean set):
- EditorConfig for VS Code
- YAML (Red Hat)
- Code Spell Checker
- PowerShell
- WSL (AnySphere)

Enable only when needed:
- GitLens — Git supercharged (useful, but optional on laptop)
- ESLint / Prettier / Pretty TypeScript Errors / Path Intellisense (only if coding in TS/JS at that moment)
- Error Lens (nice, but can add UI noise and minor overhead)

Disable:
- All AI assist extensions (Gemini, etc.)
- Docker/Container tools
- Database clients/JDBC
- Python stacks (unless you’re actively doing Python work)

---

## Extensions to add (recommended)

- **Markdown All in One** (docs-heavy governance work)
- **GitHub Pull Requests and Issues** (only if you’ll manage PRs/issues inside Cursor)
- **markdownlint** (optional; enable only if you want strict Markdown enforcement)

---

## Workspace recommendations (`.vscode/extensions.json`)

Use this to guide installs and suppress noisy suggestions. This does not force-enable/disable; it’s advisory.

Recommended (baseline for both projects):

```json
{
  "recommendations": [
    "editorconfig.editorconfig",
    "redhat.vscode-yaml",
    "streetsidesoftware.code-spell-checker",
    "ms-vscode.powershell",
    "eamodio.gitlens"
  ],
  "unwantedRecommendations": [
    "google.gemini-code-assist",
    "cweijan.vscode-database-client2",
    "cweijan.vscode-database-client2-jdbc",
    "ms-azuretools.vscode-docker",
    "ms-azuretools.vscode-containers",
    "giga-ai.giga-ai"
  ]
}
```

Optional “dev-mode” additions (only add to recommendations if you actually use them in the repo):
- `dbaeumer.vscode-eslint`
- `esbenp.prettier-vscode`
- `yoavbls.pretty-ts-errors`
- `christian-kohler.path-intellisense`

---

## Operational rule (how to apply)
- Prefer: **Disable (Workspace)** for anything marked Disable above.
- Keep a “lean by default” posture on the laptop; only enable heavier dev tooling during active work sessions.
