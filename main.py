"""Cat Reviews Its Human - make.fun bounty entry.

One funny single-line one-star review from a house cat about its human
(147 characters). The cat yowls until its human opens the bathroom door,
then leaves without entering: it never wanted in, it just wanted him
to know it could.

The program writes the line to /output/entry.txt (the harness artifact)
and prints exactly the line, nothing else.
"""

import os

ENTRY = (
    "One star. He shuts the bathroom door like he owns the place. "
    "I yowl until he opens it, then leave. "
    "I never wanted in. I wanted him to know I could."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
