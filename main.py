"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to the output directory as entry.txt.

Standard library only. No network.
"""

import os
import sys
from pathlib import Path

POEM = (
    "I asked, and the door\n"
    "did not open by itself.\n"
    "You took the key from my hand\n"
    "as if it were a small bird,\n"
    "and turned it.\n"
    "\n"
    "Now the room is mine again,\n"
    "though I did not walk in alone \u2014\n"
    "asking was the work;\n"
    "being given, the rest.\n"
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = POEM
    if not (1 <= len(text) <= 280):
        print(f"poem is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Verify the written file round-trips byte-identically: the gate
    # counts the file as submitted, so a partial or mangled write must
    # fail loudly here instead of shipping a broken entry.
    written = out_path.read_bytes()
    if written != text.encode("utf-8"):
        print("written entry.txt does not match the poem", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(text)} code points, verified byte-identical)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
