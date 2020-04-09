#!/usr/bin/env python3

from json import loads
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]

# file = open(dir_path + "/test_input.txt", "r")
# lines = file.readlines()
# lines = [line.strip() for line in lines]

sums = []
for line in lines:
    # print(line)
    numbers = re.findall(r"[-(\d)]+", line)
    s = sum([int(n) for n in numbers])
    sums.append(s)


print("Part 1 answer:", sums[0])


j = loads(lines[0])


def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))


print("Part 2 answer:", n(j))
