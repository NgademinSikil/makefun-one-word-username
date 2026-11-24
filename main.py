#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes Ngademin's own make.fun username -- one word, nothing else --
to /output/entry.txt, the single text the judge compares.
"""

import os

USERNAME = "ngademin"


def main():
    # Gate check, mirroring the sealed scorer: 1-30 chars, one word,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(USERNAME) <= 30, "username must be 1-30 characters"
    assert USERNAME.split() == [USERNAME], "username must be a single word"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(USERNAME)
    print(USERNAME)


if __name__ == "__main__":
    main()
