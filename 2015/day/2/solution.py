#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")

lines = file.readlines()
lines = [line.strip() for line in lines]
# lines = ["2x3x4", "1x1x10"]

total = 0
for line in lines:
    l, w, h = [int(v) for v in line.split('x')]
    side1 = l*w
    side2 = l*h
    side3 = w*h
    smallest_side = min(side1, side2, side3)
    area = 2*side1 + 2*side2 + 2*side3 + smallest_side
    total += area

print("Part 1 answer:", total)

total = 0
for line in lines:
    l, w, h = [int(v) for v in line.split('x')]
    side1 = 2*l + 2*w
    side2 = 2*l + 2*h
    side3 = 2*w + 2*h
    smallest_side = min(side1, side2, side3)
    volume = (l*w*h) + smallest_side
    total += volume

print("Part 2 answer:", total)
