#!/usr/bin/env python3
"""QueueBuddy: the worst app idea ever pitched.

A deterministic, offline program. It writes exactly one sentence
(221 characters, within the 240-character limit) pitching the most
useless app imaginable to /output/entry.txt.
"""

import os

SENTENCE = (
    "Introducing QueueBuddy: an app that finds the longest line in your city, "
    "reserves your spot in it, and livestreams strangers standing still so you "
    "can feel productive while achieving absolutely nothing, anywhere, anytime."
)


def main():
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit("entry must be 1-240 chars, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
