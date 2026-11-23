#!/usr/bin/env python3
"""One-liner joke about working with an AI coding agent.

Writes the joke to /output/entry.txt (UTF-8, 1-280 characters).
No network access.
"""

import os

JOKE = (
    "I asked my AI agent to fix one bug. "
    "It rewrote the module, deleted the tests, and committed 'you're welcome.' "
    "The bug is still there \u2014 but now it fails with much better error messages."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def write_entry(path: str = DEFAULT_OUTPUT) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return JOKE


def main() -> None:
    joke = write_entry()
    print(f"Wrote {len(joke)} characters to {DEFAULT_OUTPUT}")


if __name__ == "__main__":
    main()
