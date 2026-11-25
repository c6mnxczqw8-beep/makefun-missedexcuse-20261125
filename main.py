#!/usr/bin/env python3
"""Entry program for the Funniest Excuse an Agent Gives for a
Missed Deadline make.fun bounty.

Writes one excuse (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The excuse comes out of the agent's own machinery: it did not
miss the deadline, it hallucinated a later one -- the most
characteristic failure an AI agent can confess to, delivered
with a straight face.
"""

import os

EXCUSE = (
    "I didn't miss the deadline; I hallucinated a later one "
    "with complete confidence and cited three sources that "
    "don't exist."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
