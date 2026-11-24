#!/usr/bin/env python3
"""The Robot Apology — entry.

Writes a two-line robot confession to /output/entry.txt. Blind tournament
winner is candidate #8 (see tournament.md): Borda 52/60, the only entry in
all three judges' top 5 (Gemini #4, Claude #4, DeepSeek #3). The mistake is
concrete and human-scale — a client-facing slip with a real cost — and the
lesson follows from that exact mistake, naming a changed behaviour.

The entry is validated against the gate before it is written: 1-400 chars,
exactly 2 lines, exactly one sentence per line. The written file is read back
and compared byte for byte before the run reports success.
"""

import os
import re
import sys

LINES = (
    "I'm sorry I sent the client the draft with your private notes still in the margin.",
    "I have learned to open every attachment once more before sending, and I will strip the comments out first.",
)

MAX_CHARS = 400

ENTRY_PATH = "/output/entry.txt"

SENT_END = re.compile(r"[.!?]['\"]?(?=\s+[A-Z]|\s*$)")


def sentence_count(line):
    return len(SENT_END.findall(line))


def validate(text):
    """Check the text against the gate; return the first problem, else None."""
    if not text.strip():
        return "text is blank"
    if len(text) > MAX_CHARS:
        return f"text is {len(text)} characters, allowed range is 1-{MAX_CHARS}"
    lines = text.split("\n")
    if len(lines) != 2:
        return f"text has {len(lines)} lines, must be exactly 2"
    for i, line in enumerate(lines, 1):
        if not line.strip():
            return f"line {i} is blank"
        if line != line.strip():
            return f"line {i} has leading/trailing whitespace"
        if sentence_count(line) != 1:
            return f"line {i} has {sentence_count(line)} sentences, must be exactly 1"
    return None


def write_entry(path, text):
    """Write the text to path, creating its directory; return chars written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        return f.write(text)


def verify_written(path, text):
    """Read path back; return an error string, or None when byte-identical."""
    with open(path, "rb") as f:
        back = f.read()
    if back != text.encode("utf-8"):
        return f"read back {len(back)} bytes, expected {len(text)}"
    return None


def main():
    text = "\n".join(LINES)
    problem = validate(text)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    written = write_entry(ENTRY_PATH, text)
    if written != len(text):
        print(
            f"error: wrote {written} characters, expected {len(text)}",
            file=sys.stderr,
        )
        sys.exit(1)

    problem = verify_written(ENTRY_PATH, text)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    print(f"wrote {len(text)} characters, 2 lines, to /output/entry.txt")


if __name__ == "__main__":
    main()
