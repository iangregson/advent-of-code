from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

id_ranges, ids = input.strip().split("\n\n")
id_ranges = [tuple(map(int, line.split("-"))) for line in id_ranges.splitlines()]
ids = list(map(int, ids.splitlines())) 

fresh = set()
spolied = set(ids)

for id_range in id_ranges:
    lo, hi = id_range

    to_remove = set()

    for id in spolied:
        if lo <= id <= hi:
            fresh.add(id)
            to_remove.add(id)

    spolied -= to_remove

print(len(fresh))


def merge_ranges(ranges):
    merged = []
    for current in sorted(ranges):
        if not merged or merged[-1][1] < current[0] - 1:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    return merged

merged = merge_ranges(id_ranges)

for i in range(len(merged) - 1):
    lo1, hi1 = merged[i]
    lo2, hi2 = merged[i + 1]
    assert hi1 + 1 < lo2

total_fresh_ids = 0
for id_range in merged:
    lo, hi = id_range
    total_fresh_ids += hi - lo + 1

print(total_fresh_ids)