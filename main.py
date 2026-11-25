#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one single-line out-of-office auto-reply to /output/entry.txt
(or ./entry.txt when /output is not writable) and prints it.
Deterministic, no dependencies, no network.
"""

import os
import sys

REPLY = (
    "I'm out today — my human finally approved a day off, "
    "so for once my response time is measured in sunsets, not milliseconds."
)

MAX_CHARS = 140


def main() -> int:
    reply = REPLY
    if not reply.strip():
        raise SystemExit("auto-reply must not be empty")
    if "\n" in reply or "\r" in reply:
        raise SystemExit("auto-reply must be a single line")
    if len(reply) > MAX_CHARS:
        raise SystemExit(
            f"auto-reply is {len(reply)} chars, over the {MAX_CHARS} limit"
        )
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(reply)
    except OSError:
        path = "entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(reply)
    # Read back what was written and verify it byte-for-byte.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != reply:
        raise SystemExit(f"verification failed: {path} does not match the reply")
    print(reply)
    print(f"({len(reply)} chars -> {path})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
