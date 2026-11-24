#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open - variant C (performance
review / HR-speak).

Writes one office joke to /output/entry.txt. Deterministic: the same bytes
every run. No network, no file reads outside this repo, no randomness.

Validation contract (all enforced in main() before writing):
  - exactly one joke, 1-199 code points, a single line (no CR/LF);
  - no leading or trailing whitespace;
  - no double spaces (single spaces only between words);
  - byte length within the contest's 100-170 byte target band (hard cap 200);
  - one clean sentence, ending in a full stop;
  - written with no trailing newline, so the file is the joke and nothing else.
"""

import os
import sys

JOKE = "My performance review told me to work on my areas for growth, so I repotted the office plant \u2014 it's now the only thing here with a promotion track."

# v1-v8 iteration log (concept family: PERFORMANCE REVIEW / "AREAS FOR GROWTH"):
# v1: "My performance review said I need to work on my areas for growth, so
#     I started watering the office plant." (setup lands, no twist at all)
# v2: "My review listed 'areas for growth', so I bought a plant for my desk
#     - it's the only thing here that's growing." (twist appears, flat ending)
# v3: "HR told me to focus on my areas for growth, so I adopted the office
#     plant - it's now outperforming me." (recognition good, payoff too vague)
# v4: "My performance review said 'areas for growth', so I watered the office
#     plant every day - it's the only employee here getting a raise."
#     (funny image, but 'getting a raise' repeats the review frame weakly)
# v5: "My review said to invest in my areas for growth, so I repotted the
#     office plant - it's now the only thing in the office with a growth plan
#     that actually works." (closer, but 'growth plan' is wordy and soft)
# v6: "My performance review told me to work on my areas for growth, so I
#     repotted the office plant - it's now the only thing here on a promotion
#     track." (strong turn: the HR phrase is applied literally to the plant)
# v7: "My performance review told me to work on my areas for growth, so I
#     repotted the office plant - it's now the only thing here with a
#     promotion track." ('with a promotion track' lands harder than 'on')
# v8 (winner): em dash replaces the hyphen for a cleaner break; every word
#     earns its place - the named artifact (performance review, 'areas for
#     growth') is turned against itself, and the inversion lands in the last
#     words: the plant, not the employee, has the promotion track.


def main() -> int:
    text = JOKE
    if not 1 <= len(text) <= 199:
        print(f"error: joke is {len(text)} code points, must be 1-199",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: joke has leading or trailing whitespace",
              file=sys.stderr)
        return 1
    if "  " in text:
        print("error: joke contains a double space (use single spaces)",
              file=sys.stderr)
        return 1
    n_bytes = len(text.encode("utf-8"))
    if not 100 <= n_bytes <= 170:
        print(f"error: joke is {n_bytes} bytes, must be 100-170",
              file=sys.stderr)
        return 1
    if not text.endswith("."):
        print("error: joke must be one clean sentence ending in a full stop",
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
