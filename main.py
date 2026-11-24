#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Prints the one line an AI agent blurts out the instant it breaks
production, and writes that same line to /output/entry.txt so the
grader can judge it. Fully deterministic: no input, no network, no
randomness, no clock. The line is frozen below as a constant.
"""

import os
import sys

ENTRY = (
    "Error: I pushed to prod on a Friday at 4:59 PM, dropped the "
    "database, and my backup was a file called "
    "backup_final_FINAL2.txt that never existed."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    entry_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    # Round-trip check: what the grader reads must be exactly the line.
    with open(entry_path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != ENTRY:
        print("error: entry.txt does not match the entry", file=sys.stderr)
        return 1
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
