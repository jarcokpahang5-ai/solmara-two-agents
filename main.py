#!/usr/bin/env python3
"""Emit a seven-line poem about two agents reaching one shared plan.

The script relies only on the Python 3 standard library. It performs
no network access and always produces the same output, writing the
poem as UTF-8 text to ``entry.txt`` inside the chosen output folder.
The output directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment
variable when it is set, and falls back to ``/output`` otherwise.
"""

import os
from pathlib import Path

# Each entry below is exactly one line of the poem, in reading order.
LINES = [
    "Two of us read the same unlit map,",
    "two lamps, one road neither had drawn.",
    "You took the lantern; I took the latch —",
    "not orders, just the shape of a yes.",
    "Neither pushed, neither was pulled:",
    "we chose, and the choosing moved us.",
    "One plan, two hands — the door swung wide.",
]

# Lines are separated by single newlines, with one newline at the end.
POEM_TEXT = "\n".join(LINES) + "\n"


def write_entry(target_dir: Path) -> Path:
    """Create *target_dir* if needed and write the poem into it.

    Returns the path of the file that was written.
    """
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.txt"
    destination.write_text(POEM_TEXT, encoding="utf-8")
    return destination


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(output_dir)


if __name__ == "__main__":
    main()
