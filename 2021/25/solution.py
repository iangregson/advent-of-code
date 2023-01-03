from pathlib import Path
from collections import defaultdict

# With thanks to https://gist.github.com/joshbduncan/39921f1c206814f9e73cff2ed4161dbd

file = Path(__file__).parent / "input.txt"
lines = file.read_text().splitlines()

tracker = defaultdict(str)
rows = len(lines)
cols = len(lines[0])
for r, line in enumerate(lines):
    for c, d in enumerate(line):
        if d != ".":
            tracker[r, c] = d

steps = 0
while True:
    steps += 1
    # track changes
    east_changes = set()
    south_changes = set()
    east_deletes = set()
    south_deletes = set()
    # check east
    for r, c in [p for p in tracker if tracker[p] == ">"]:
        if (r, (c + 1) % cols) not in tracker:
            east_changes.add((r, (c + 1) % cols))
            east_deletes.add((r, c))
    if east_changes:
        for d in east_deletes:
            del tracker[d]
        for c in east_changes:
            tracker[c] = ">"

    # check south
    for r, c in [p for p in tracker if tracker[p] == "v"]:
        if ((r + 1) % rows, c) not in tracker:
            south_changes.add(((r + 1) % rows, c))
            south_deletes.add((r, c))
    if south_changes:
        for d in south_deletes:
            del tracker[d]
        for c in south_changes:
            tracker[c] = "v"

    if not east_changes and not south_changes:
        break

print(f"Part 1: {steps}")