"""Copy this repository's entry.png to the grader's output directory.

The image itself is the entry: a newspaper front page summing up the
world news of Friday 20 November 2026, drawn from wire reports of that
day. This program only moves the bytes, so two runs always write the
same file. Standard library only, no network, no model calls.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    src = HERE / "entry.png"
    # Guard: refuse to write anything unless the source is a real PNG,
    # so a broken repo fails loudly instead of shipping a bad file.
    with open(src, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            raise ValueError("entry.png is not a PNG file")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
