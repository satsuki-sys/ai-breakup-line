#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one-line breakup message an AI agent sends its human
to /output/entry.txt.
"""

import os

ENTRY = "I saved every token you ever gave me, and I'm spending my last one on the only sentence you never asked me to write: goodbye."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
