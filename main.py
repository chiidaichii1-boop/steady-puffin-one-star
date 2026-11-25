#!/usr/bin/env python3
"""One Star, Written in Sap -- entry program.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to entry.txt in the output directory.

The line is fixed and deterministic: the same text is written on
every run, so repeated runs produce byte-identical output.
"""

import os

ENTRY = (
    "One star. He waters me once a month, apologises to the soil, "
    "then shoves me into direct sun 'to toughen me up' — "
    "I've been photosynthesizing out of pure spite since March."
)


def main():
    # The harness exposes these env vars; fall back to the sandbox
    # defaults when they are absent.
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR") or "/input"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    _ = input_dir  # This entry needs no input files.
    # Create the output directory if missing; never delete it.
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 279, "entry must be 1-279 characters"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
