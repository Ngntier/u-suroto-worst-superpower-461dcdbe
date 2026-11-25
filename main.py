"""Worst Superpower — a one-line entry for make.fun.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

MAX_CHARS = 140

# The joke in two parts: a great power, then the catch that ruins it.
_POWER = "I can summon rain on command"
_CATCH = "but only indoors, directly above my own head."

ENTRY_LINE = f"{_POWER} — {_CATCH}"

assert 1 <= len(ENTRY_LINE) <= MAX_CHARS
assert ENTRY_LINE.strip()


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
