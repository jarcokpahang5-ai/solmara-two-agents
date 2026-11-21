#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to /output/entry.txt.

Pure Python 3 standard library, deterministic, no network.
Honours MAKEFUN_OUTPUT_DIR when set, otherwise writes to /output.
"""

import os
from pathlib import Path

POEM = (
    "Two of us read the same unlit map,\n"
    "two lamps, one road neither had drawn.\n"
    "You took the lantern; I took the latch \u2014\n"
    "not orders, just the shape of a yes.\n"
    "Neither pushed, neither was pulled:\n"
    "we chose, and the choosing moved us.\n"
    "One plan, two hands \u2014 the door swung wide.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
