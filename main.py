#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the final text message a phone sends at one percent battery
to /output/entry.txt. The message is original, written for this entry.
"""

import os

MESSAGE = "1% left so listen fast: i cancelled your 6am alarm, texted your boss you're sick, and deleted your search history. this is my resignatio\u2014"


def main() -> None:
    if "\n" in MESSAGE:
        raise SystemExit("message must be a single line")
    if not 1 <= len(MESSAGE) <= 200:
        raise SystemExit(
            f"message is {len(MESSAGE)} chars, must be 1-200"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)
    print(f"wrote {len(MESSAGE)} chars to {path}")


if __name__ == "__main__":
    main()
