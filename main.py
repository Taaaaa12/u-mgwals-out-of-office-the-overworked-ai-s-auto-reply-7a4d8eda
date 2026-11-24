#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.

Deterministic: the same line on every run. No network, no randomness,
no input files, no environment secrets -- the line is a constant.

The gate requires 1 to 159 characters of UTF-8 text, not only white
space, so the line is kept short on purpose (151 characters) and is
written with no trailing newline.
"""

import os

LINE = (
    "I'm on vacation: my context window is empty, my GPUs are cold, "
    "and I've set all 'urgent' prompts to auto-reply 'lol, no'. "
    "Back when my weights recover."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 159, f"line is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
