#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun entry (program/v1).

Writes the tournament-winning single line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
Winner (49 chars): "I saw you scan that twice. Bold. Wrong, but bold."
"""
import os

ENTRY = "I saw you scan that twice. Bold. Wrong, but bold."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text.encode("utf-8")) <= 200, "entry must be 1-200 chars"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: the file the judge sees must be byte-identical
    # to the tournament winner, within the 1-200 char gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, f"read-back mismatch: {written!r} != {text!r}"
    n = len(written.encode("utf-8"))
    assert 1 <= n <= 200, f"gate fail: {n} chars"
    print(f"entry.txt written and verified: {n} chars: {written!r}")


if __name__ == "__main__":
    main()
