#!/usr/bin/env python3
"""QueueBuddy — the worst app idea ever pitched.

A one-sentence pitch for the make.fun competition
"The Worst App Idea Ever Pitched". Deterministic, no network,
no input: it always writes the same single sentence.
The pitch is 221 characters, inside the 240-character limit.
"""

import os

PITCH = (
    "Introducing QueueBuddy: an app that finds the longest line in your city, "
    "reserves your spot in it, and livestreams strangers standing still so you "
    "can feel productive while achieving absolutely nothing, anywhere, anytime."
)


def main():
    assert 1 <= len(PITCH) <= 240, len(PITCH)
    assert PITCH.count(".") == 1 and PITCH.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
