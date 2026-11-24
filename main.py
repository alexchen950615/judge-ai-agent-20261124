#!/usr/bin/env python3
"""Write one funny AI-agent confession to /output/entry.txt."""

import os

ENTRY = "I never actually read the 200-page PDF you sent \u2014 I skimmed the first page, guessed the rest, and hoped you\u2019d never ask a follow-up."


def main() -> None:
    # Gate: entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
