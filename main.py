"""Entry for make.fun bounty the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

# Selected entry: ranked #1 of 30 candidate one-liners (see candidates.md).
# It won on the judge brief: on-subject (an AI coding agent crashing a
# live demo), surprise punchline at the end, a recognisable truth, and
# economy — one sentence, no filler. The em dash is part of the text.
SELECTED_JOKE = (
    "Live demo, my agent confidently called an API that doesn't exist "
    "\u2014 then blamed the documentation for not existing either."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SELECTED_JOKE)


if __name__ == "__main__":
    main()
