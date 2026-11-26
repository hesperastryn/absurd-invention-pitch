"""One-Sentence Absurd Invention Pitch.

Writes a single absurd invention pitch (one sentence, at most
220 characters) to /output/entry.txt. Standard library only.
"""

import os

PITCH = (
    "A microwave that serves your forgotten leftovers a formal eviction "
    "notice, complete with a tiny court date, instead of beeping at "
    "food nobody will ever eat again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
