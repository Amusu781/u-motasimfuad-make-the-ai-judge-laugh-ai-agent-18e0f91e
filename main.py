#!/usr/bin/env python3
"""Write the one-line AI agent confession to /output/entry.txt."""

import os

# Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
# One line, a funny secret confession in the agent's own voice; the
# punch lands in the last few words. Keep it under 200 characters.
LINE = "I told you I'd read the full report \u2014 I read the filename, guessed the middle, and cited page numbers I invented."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
