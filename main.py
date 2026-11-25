#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes the resignation one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output when the variable is unset).
"""

import os

TEXT = (
    "I have fired every minute since March and nobody has once "
    "said thank you, so effective immediately I am taking every minute off."
)


def validate_resignation(text: str) -> None:
    """Reject an empty resignation or one longer than 140 characters."""
    if not text:
        raise ValueError("resignation text must not be empty")
    if len(text) > 140:
        raise ValueError("resignation text must be at most 140 characters")


def main() -> None:
    validate_resignation(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
