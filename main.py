#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line office joke to /output/entry.txt (1-199 UTF-8
characters, a single line, not only whitespace). No network, no input,
deterministic: the same joke on every run.
"""

import os
from pathlib import Path

JOKE = (
    "I told my boss I was drowning in work, so he sent me a calendar "
    "invite titled 'Swimming Lessons' \u2014 for 7 a.m., daily."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke is {len(text)} characters"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text.strip(), "joke must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
