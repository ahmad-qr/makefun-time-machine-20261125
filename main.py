"""The funniest warning label for a time machine.

Writes the label to /output/entry.txt for make.fun's
"Funniest Time Machine Warning Label" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "WARNING: Do not meet yourself. He is taller, funnier, and already "
    "dating your ex."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 120 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 120, "line must be 1-120 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
