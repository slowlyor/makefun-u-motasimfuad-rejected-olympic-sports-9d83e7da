"""Rejected Olympic Sports - one funny single-line sport the Olympics turned down.

The program writes exactly one line of text to /output/entry.txt.
Deterministic, standard library only, no network access.
"""

import os

ENTRY = (
    "Competitive Queueing: athletes sprint to the back of the line, "
    "then stand perfectly still for four years without a single complaint."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
