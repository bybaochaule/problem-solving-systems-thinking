#!/usr/bin/env python3
"""Check a Markdown workflow map for key systems-thinking sections.

This helper is deterministic and non-destructive. It reads a Markdown file and
reports whether common sections for the Problem Solving & Systems Thinking skill
are present. It does not modify files.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REQUIRED_PHRASES = [
    "goal",
    "success metric",
    "system boundary",
    "assumptions",
    "workflow map",
    "decision",
    "agent flow",
    "risks",
    "next steps",
]


def check_markdown(path: Path) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8").lower()
    missing = [phrase for phrase in REQUIRED_PHRASES if phrase not in text]
    return not missing, missing


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a workflow map Markdown file for required sections.")
    parser.add_argument("markdown_file", help="Path to a Markdown workflow map file.")
    args = parser.parse_args(argv)

    path = Path(args.markdown_file)
    if not path.exists() or not path.is_file():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2

    ok, missing = check_markdown(path)
    if ok:
        print("pass: all recommended workflow sections were found")
        return 0

    print("warning: missing recommended phrases:")
    for phrase in missing:
        print(f"- {phrase}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
