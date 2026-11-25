import os

# One line, 18 words, no trailing newline: the excuse a gamer texts
# the boss to skip work on GTA 6 launch week. Believable because the
# detail is boring and specific (IT holding the laptop for a patch);
# funny because the excuse's own logic does the work.
ENTRY = "IT took my laptop for the mandatory security patch and said I can't have it back until Thursday"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
