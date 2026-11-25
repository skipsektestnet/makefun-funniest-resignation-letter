"""The Funniest One-Line Resignation Letter: writes the entry text to /output/entry.txt.

Why this line: a resignation in the cron job's own voice. It has fired every
minute since March, nobody has once said thank you, so it quits by taking
every minute off — the grievance is specific and concrete, the punch is the
wordplay on "every minute" at the very end.
"""

import os

# The entry itself: one line, 128 chars, the "every minute off" punch at the end.
ENTRY = "I have fired every minute since March and nobody has once said thank you, so effective immediately I am taking every minute off."

OUTPUT_PATH = "/output/entry.txt"

# Length bounds for this bounty: 1 to 140 characters.
MIN_CHARS = 1
MAX_CHARS = 140


def validate_entry(text):
    """Check the entry is a non-empty single line within the length bounds."""
    assert text and not text.isspace(), "entry must not be empty"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, "entry length out of bounds"
    assert "\n" not in text, "entry must be a single line"
    # Whitespace guard: no leading/trailing whitespace sneaking in.
    assert text == text.strip(), "entry must not start or end with whitespace"
    return text


def main():
    # Guard: never submit a blank entry to the sealed gate.
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
