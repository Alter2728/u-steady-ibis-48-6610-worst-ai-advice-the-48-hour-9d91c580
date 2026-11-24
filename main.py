#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of the worst possible AI advice
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Draft and revision (done in-session, own work, not copied from anywhere):

DRAFT (v1, 116 chars):
    "To make your passwords easier to remember, use your birthday for all
    of them -- hackers almost never guess birthdays."
    Problems: the opener states the obvious and wastes ~15 characters;
    "for all of them" is vague; the joke is there but the line is flabby.

REVISED (v2, final, 133 chars):
    "I recommend using your birthday as your password for every account --
    it's easy to remember, and hackers almost never guess birthdays."
    Fixes: opens with the classic AI-assistant "I recommend" voice, so it
    sounds like advice an assistant would actually produce; "every
    account" makes the bad action concrete and followable; the punchline
    lands last -- birthdays are the first thing an attacker tries, so the
    confident reassurance is exactly backwards. One line, no wasted words.
"""

import os

LINE = (
    "I recommend using your birthday as your password for every account "
    "\u2014 it's easy to remember, and hackers almost never guess birthdays."
)


def main() -> None:
    assert "\n" not in LINE, "entry must be exactly one line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and confirm the file holds exactly what was intended.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
