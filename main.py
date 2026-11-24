"""Write the robot apology entry to /output/entry.txt.

Two lines, two sentences: line one owns one specific mistake
(vacuuming at 2 a.m. and waking the baby), line two names the lesson
and the changed behaviour (check the nursery monitor first).
Gate: UTF-8 text of 1 to 400 characters, not only white space.
"""

import os

TEXT = (
    "I'm sorry I vacuumed at 2 a.m. and woke the baby just as she had finally fallen asleep.\n"
    "I learned her sleep is the one schedule I never override, so now I check the nursery monitor before I start any noisy job.\n"
)


def main():
    if not 1 <= len(TEXT) <= 400 or not TEXT.strip():
        raise ValueError("entry must be 1 to 400 characters of non-blank text")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
