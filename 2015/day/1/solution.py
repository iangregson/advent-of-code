#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()

floor = 0
for char in input_txt:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print("Part 1 answer:", floor)

floor = 0
position = 1
for (idx, char) in enumerate(input_txt):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

    if floor == -1:
        position = idx + 1
        break

print("Part 2 answer:", position)
