#!/usr/bin/env python3
"""Print required Windows->WSL env var names for gateway restart (one per line)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def main() -> int:
    path = Path.home() / ".openclaw" / "openclaw.json"
    if not path.is_file():
        print("ANTHROPIC_API_KEY", file=sys.stderr)
        print("ANTHROPIC_API_KEY")
        return 0
    blob = json.dumps(json.load(path.open(encoding="utf-8")))
    required = {"ANTHROPIC_API_KEY"}
    if re.search(r"openai/", blob):
        required.add("OPENAI_API_KEY")
    if re.search(r"openrouter/", blob):
        required.add("OPENROUTER_API_KEY")
    if re.search(r"anthropic/", blob):
        required.add("ANTHROPIC_API_KEY")
    for name in sorted(required):
        print(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
