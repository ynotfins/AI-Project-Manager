#!/usr/bin/env python3
"""
Cursor afterFileEdit hook: rotate_ledger.py

Automatically rotates AI-Project-Manager/docs/ai/context/AGENT_EXECUTION_LEDGER.md
when it exceeds the size/count policy thresholds.

Policy (from 00-global-core.md and 10-project-workflow.md):
- Keep the 3-5 most recent LEDGER-NNN entries in the active ledger.
- Archive threshold: entry count > 5 OR file > ~300 lines.
- Move the oldest entries verbatim to docs/ai/context/archive/ledger-YYYY-MM-DD.md.
- Never archive below 3 active entries.
- Never summarize or rewrite archived entries (verbatim move only).
- Preserve the header/policy section unchanged.

Invocation modes:
  1. Cursor hook (stdin JSON payload):
     Cursor passes {"file_path": "...", "workspace_roots": [...], "edits": [...]}
  2. Direct/force mode (CLI):
     python rotate_ledger.py --force [--project-root PATH]
     (uses CWD or --project-root as the repo root)

Exit codes:
  0  - success (including no-op when rotation is not needed)
  Non-zero - should not happen; script is fail-open by design
"""

import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

LEDGER_RELATIVE_PATH = "docs/ai/context/AGENT_EXECUTION_LEDGER.md"
ARCHIVE_DIR_RELATIVE = "docs/ai/context/archive"

# Rotation thresholds
MAX_ACTIVE_ENTRIES = 5
MIN_ACTIVE_ENTRIES = 3
MAX_ACTIVE_LINES = 300

# Pattern that identifies the start of a real ledger entry block.
# Each entry starts with:   \n---\n\n## LEDGER-{digits}
# The format example in the header uses ## LEDGER-<NNN> (non-digits), so it
# will NOT match, which correctly excludes it from entry splitting.
ENTRY_BOUNDARY = re.compile(r"\n(?=---\n\n## LEDGER-\d+)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    force_mode = "--force" in sys.argv

    if force_mode:
        project_root = _resolve_project_root_from_args()
    else:
        project_root = _resolve_project_root_from_stdin()

    if project_root is None:
        # Could not determine project root; exit cleanly (fail-open).
        _emit_ok()
        return

    ledger_path = project_root / LEDGER_RELATIVE_PATH
    archive_dir = project_root / ARCHIVE_DIR_RELATIVE

    if not ledger_path.exists():
        _emit_ok()
        return

    try:
        _rotate_if_needed(ledger_path, archive_dir, verbose=force_mode)
    except Exception as exc:
        sys.stderr.write(f"[rotate_ledger] Unhandled error: {exc}\n")
        import traceback
        traceback.print_exc(file=sys.stderr)

    _emit_ok()


# ---------------------------------------------------------------------------
# Stdin / force-mode resolution
# ---------------------------------------------------------------------------

def _resolve_project_root_from_stdin() -> "Path | None":
    """Parse the Cursor afterFileEdit payload from stdin and return project root."""
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return None
        payload = json.loads(raw)
    except (json.JSONDecodeError, OSError):
        return None

    file_path_str: str = payload.get("file_path", "")
    workspace_roots: list = payload.get("workspace_roots", [])

    if not file_path_str:
        return None

    # Quick check: is this the ledger file?
    normalized = file_path_str.replace("\\", "/")
    if not normalized.endswith(LEDGER_RELATIVE_PATH):
        # Not the ledger – skip immediately.
        return None

    # Prefer workspace_roots[0] as the project root (most reliable).
    if workspace_roots:
        return Path(workspace_roots[0])

    # Fallback: derive project root from the absolute file path.
    return _derive_root_from_file_path(Path(file_path_str))


def _resolve_project_root_from_args() -> "Path | None":
    """Resolve project root for --force mode."""
    # Allow --project-root PATH override.
    args = sys.argv[1:]
    if "--project-root" in args:
        idx = args.index("--project-root")
        if idx + 1 < len(args):
            return Path(args[idx + 1])

    # Default: current working directory.
    cwd = Path.cwd()
    # Verify the ledger exists here.
    if (cwd / LEDGER_RELATIVE_PATH).exists():
        return cwd

    # Walk up to find it.
    return _derive_root_from_file_path(cwd / LEDGER_RELATIVE_PATH)


def _derive_root_from_file_path(file_path: Path) -> "Path | None":
    """Walk up from file_path to find the repo root containing the ledger."""
    # The ledger_relative_path has N parts; strip them from the absolute path.
    relative_parts = Path(LEDGER_RELATIVE_PATH).parts  # ('docs', 'ai', 'context', '...')
    candidate = file_path
    for _ in relative_parts:
        candidate = candidate.parent
    if (candidate / LEDGER_RELATIVE_PATH).exists():
        return candidate
    return None


# ---------------------------------------------------------------------------
# Core rotation logic
# ---------------------------------------------------------------------------

def _rotate_if_needed(ledger_path: Path, archive_dir: Path, verbose: bool = False) -> None:
    """Read the ledger, rotate if above threshold, write results."""
    content = ledger_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    total_lines = len(lines)

    header, entries = _parse_ledger(content)
    entry_count = len(entries)

    if verbose:
        print(f"[rotate_ledger] Ledger: {ledger_path}")
        print(f"[rotate_ledger] Before rotation: {total_lines} lines, {entry_count} entries")

    # Check if rotation is needed.
    needs_rotation = (entry_count > MAX_ACTIVE_ENTRIES) or (total_lines > MAX_ACTIVE_LINES)
    if not needs_rotation:
        if verbose:
            print("[rotate_ledger] No rotation needed — within policy limits.")
        return

    if entry_count <= MIN_ACTIVE_ENTRIES:
        if verbose:
            print(
                f"[rotate_ledger] At minimum entry floor ({MIN_ACTIVE_ENTRIES}); "
                "cannot archive further. Ledger may still exceed line limit."
            )
        return

    # Sort entries by LEDGER number (ascending = chronological order).
    # Newest entries have the highest LEDGER numbers; oldest have the lowest.
    # This is authoritative — file position is NOT used to determine age.
    def ledger_number(entry: str) -> int:
        m = re.search(r"## LEDGER-(\d+)", entry)
        return int(m.group(1)) if m else 0

    sorted_ascending = sorted(entries, key=ledger_number)  # oldest first
    sorted_descending = list(reversed(sorted_ascending))   # newest first

    # Determine which entries to archive (oldest = lowest numbers) and which to keep.
    to_keep = list(sorted_descending)  # start: newest first
    to_archive: list[str] = []         # will accumulate oldest-first (chronological)

    while len(to_keep) > MIN_ACTIVE_ENTRIES:
        current_lines = _estimate_lines(header, to_keep)
        if len(to_keep) <= MAX_ACTIVE_ENTRIES and current_lines <= MAX_ACTIVE_LINES:
            break  # Both conditions satisfied.
        # Remove oldest: it's at the END of to_keep (since to_keep is newest-first).
        oldest = to_keep.pop()
        # Append so to_archive accumulates in chronological order (oldest first):
        # first pop = lowest LEDGER number → appended first = position 0 in to_archive.
        to_archive.append(oldest)

    if not to_archive:
        if verbose:
            print("[rotate_ledger] No entries selected for archiving.")
        return

    # Ensure archive directory exists.
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Archive file name: ledger-YYYY-MM-DD.md (today's date).
    today_str = date.today().strftime("%Y-%m-%d")
    archive_file = archive_dir / f"ledger-{today_str}.md"

    _write_to_archive(archive_file, to_archive, today_str)
    # Write active ledger with entries in descending LEDGER-number order (newest first).
    _write_active_ledger(ledger_path, header, to_keep)

    # Verification stats.
    new_content = ledger_path.read_text(encoding="utf-8")
    new_lines = len(new_content.splitlines())
    new_entry_count = len(to_keep)

    if verbose:
        print(f"[rotate_ledger] After rotation:  {new_lines} lines, {new_entry_count} entries")
        print(f"[rotate_ledger] Archived {len(to_archive)} entries to: {archive_file}")
        entry_labels = _extract_entry_labels(to_archive)
        print(f"[rotate_ledger] Archived entries (chronological): {entry_labels}")
        kept_labels = _extract_entry_labels(to_keep)
        print(f"[rotate_ledger] Kept entries (newest first):      {kept_labels}")
    else:
        sys.stderr.write(
            f"[rotate_ledger] Rotated {len(to_archive)} entries to {archive_file.name}. "
            f"Active ledger: {new_lines} lines, {new_entry_count} entries.\n"
        )


# ---------------------------------------------------------------------------
# Ledger parsing
# ---------------------------------------------------------------------------

def _parse_ledger(content: str) -> tuple[str, list[str]]:
    """
    Split ledger into (header, [entry_blocks]).

    The header is everything before the first real ledger entry.
    Entry blocks are newest-first, each starting with '---\n\n## LEDGER-{digits}'.

    The split pattern consumes the '\\n' immediately before '---\\n\\n## LEDGER-{digits}',
    so each entry block begins with '---' (no leading newline).
    Reconstruction requires inserting '\\n' between header and first entry, and
    between consecutive entries (i.e., header + '\\n' + '\\n'.join(entries)).
    """
    parts = ENTRY_BOUNDARY.split(content)

    if len(parts) <= 1:
        # No real entries found — return entire content as header.
        return content, []

    header = parts[0]
    entries = parts[1:]  # Each starts with '---\n\n## LEDGER-NNN...'
    return header, entries


def _estimate_lines(header: str, entries: list[str]) -> int:
    """Estimate the line count of the reconstructed ledger."""
    if not entries:
        return len(header.splitlines())
    combined = header + "\n" + "\n".join(entries)
    return len(combined.splitlines())


def _extract_entry_labels(entries: list[str]) -> list[str]:
    """Extract LEDGER-NNN labels from entry blocks for reporting."""
    labels = []
    for entry in entries:
        m = re.search(r"## (LEDGER-\d+)", entry)
        if m:
            labels.append(m.group(1))
    return labels


# ---------------------------------------------------------------------------
# File writers
# ---------------------------------------------------------------------------

def _write_to_archive(archive_file: Path, to_archive: list[str], today_str: str) -> None:
    """
    Append archived entries to the archive file (create with header if new).
    Entries are written in chronological order (oldest first = order of to_archive list).
    Each entry block is verbatim — no summarization or rewriting.
    """
    if archive_file.exists():
        existing = archive_file.read_text(encoding="utf-8")
        # Ensure existing content ends cleanly, then append entries.
        body = existing.rstrip("\n") + "\n"
        for entry in to_archive:
            body += "\n" + entry.rstrip("\n") + "\n"
        archive_file.write_text(body, encoding="utf-8")
    else:
        archive_header = (
            f"# AGENT Execution Ledger — Archive\n\n"
            f"**Date**: {today_str}\n"
            f"**Status**: NON-CANONICAL — historical only; never authoritative.\n\n"
            f"Archived from `docs/ai/context/AGENT_EXECUTION_LEDGER.md`.\n"
            f"Entries are verbatim — no summarization or rewriting.\n\n"
        )
        body = archive_header
        for entry in to_archive:
            body += "\n" + entry.rstrip("\n") + "\n"
        archive_file.write_text(body, encoding="utf-8")


def _write_active_ledger(
    ledger_path: Path, header: str, to_keep: list[str]
) -> None:
    """Write the updated active ledger: header + kept entries (newest first)."""
    if not to_keep:
        new_content = header
    else:
        new_content = header + "\n" + "\n".join(entry.rstrip("\n") for entry in to_keep) + "\n"
    ledger_path.write_text(new_content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _emit_ok() -> None:
    """Output an empty JSON object to stdout (required for Cursor hook protocol)."""
    sys.stdout.write("{}\n")
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
