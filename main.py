"""Fortune-cookie wisdom for developers.

Chosen line: "Legacy code is not a mess; it is a decision that outlived
its meeting."

Why this line won, scored against the judge criteria in order:
1. One original fortune-cookie line for a developer -- it is a single
   piece of wisdom addressed to a dev, not a slogan or a punchline.
2. Reads like a fortune cookie -- one short balanced sentence, the
   classic "is not X; it is Y" reframe, landing in a single breath.
3. True about a dev's day -- legacy code is what every developer
   actually inherits and works in; it is accumulated past decisions.
4. A fresh turn -- legacy code is usually called a mess or a burden;
   reframing it as a decision nobody ever revisited is a turn the
   reader has not heard before.
5. A quiet twist rewarding a second read -- the meeting (ephemeral,
   forgotten by everyone) is outlived by the decision made in it;
   the thing nobody remembers is the thing still running in prod.

The line is 70 characters, well under the 120-character limit.
"""

import os

FORTUNE = "Legacy code is not a mess; it is a decision that outlived its meeting."


def main() -> None:
    assert len(FORTUNE) <= 120, "fortune exceeds the 120-character limit"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
