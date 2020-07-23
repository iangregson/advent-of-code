#!/usr/bin/env python3

import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_lines = file.readlines()
input_lines = [list(filter(len, l.strip().split(' '))) for l in input_lines]
input_lines = [list(map(int, l)) for l in input_lines]

# input_lines = [
#     [5, 10, 25],
#     [3, 4, 5],
#     [7, 8, 9],
#     [5, 10, 25],
#     [3, 4, 5],
#     [7, 8, 9],
# ]
# print(input_lines)

count_possible_triangles = 0

for line in input_lines:
    line.sort()
    if sum(line[:2]) > line[2]:
        count_possible_triangles += 1

print("Part 1 answer:", count_possible_triangles)

data = np.loadtxt(dir_path + "/input.txt").T.reshape(-1, 3).T
data.sort(axis=0)
count_possible_triangles = np.sum(sum(data[:2]) > data[2])

print("Part 2 answer:", count_possible_triangles)
