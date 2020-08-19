#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

input_txt = [
    'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
    'The second floor contains a hydrogen generator.',
    'The third floor contains a lithium generator.',
    'The fourth floor contains nothing relevant.',
]

print(input_txt)

print("Part 1 answer:", 0)
print("Part 2 answer:", 0)
