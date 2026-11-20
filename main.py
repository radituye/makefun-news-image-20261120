#!/usr/bin/env python3
"""Ship the 20 November 2026 front page.

The artwork for this entry is entry.png, a 1024x1024 newspaper front
page that sums up the world news of Friday 20 November 2026: the lead
story is Trump pushing the Iran decision into 2027, with six boxes for
the Myanmar genocide verdict, the Houthi strikes on Riyadh and the
Strait of Hormuz, Cyclone Akvan, the Anthropic IPO, GTA VI sales, and
Voyager 1, plus an "also today" strip.

This entrypoint places an exact copy of entry.png at
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable
is unset). It uses only the Python standard library, touches no
network, and produces the same bytes on every run. Before copying it
checks the file really is a PNG, so a truncated image can never be
shipped by accident.
"""

import os
import shutil
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
ENTRY_DIR = Path(__file__).resolve().parent
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def ship_front_page() -> Path:
    """Copy entry.png to the output directory and return its path."""
    source = ENTRY_DIR / "entry.png"
    with source.open("rb") as handle:
        magic = handle.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG file")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    target = DEST_DIR / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise ValueError("entry.png copy came out the wrong size")
    return target


if __name__ == "__main__":
    shipped = ship_front_page()
    print(f"wrote {shipped} ({shipped.stat().st_size} bytes)")
