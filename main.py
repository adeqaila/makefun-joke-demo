"""Entry for make.fun bounty the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

JOKE = (
    "Live demo, my agent confidently called an API that doesn't exist "
    "\u2014 then blamed the documentation for not existing either."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
