#!/usr/bin/env python3

import os
import re
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]


claims = [[*map(int, re.findall(r'\d+', l))] for l in input_txt if l]
squares = lambda c: ((i, j) for i in range(c[1], c[1]+c[3])
                            for j in range(c[2], c[2]+c[4]))
fabric = Counter(s for c in claims for s in squares(c))

part1 = sum(1 for v in fabric.values() if v > 1)
part2 = next(c[0] for c in claims if all(fabric[s] == 1 for s in squares(c)))

print("Part 1 answer:", part1)
print("Part 2 answer:", part2)