#!/usr/bin/env python3

import os
import re
from itertools import combinations
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")

lines = file.readlines()
lines = [line.strip().rstrip('.') for line in lines]

containers = [int(x) for x in lines]

# print(containers)


T = 150
valid_combinations = []
for i in range(1, len(containers)):
    comb = combinations(containers, i)
    for c in comb:
        if sum(c) == T:
            valid_combinations.append(c)

print("Part 1 answer:", len(valid_combinations))

T = 150
valid_combinations = defaultdict(list)
for i in range(1, len(containers)):
    comb = combinations(containers, i)
    for c in comb:
        if sum(c) == T:
            valid_combinations[i].append(c)

min_containers = min(valid_combinations.keys())
print("Part 2 answer:", len(valid_combinations[min_containers]))
