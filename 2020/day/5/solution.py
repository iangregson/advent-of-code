#!/usr/bin/env python3

import os
import itertools
import functools
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'FBFBBFFRLR',
#   'BFFFBBFRRR',
#   'FFFBBBFRRR',
#   'BBFFBBFRLL',
# ]

row_numbers = []

for line in lines:
  row = line[:-3]
  col = line[-3:]

  high = 127
  low = 0
  for char in row:
    # print(low, high)
    if char == 'F':
      low = low
      high = ((high - low) // 2) + low
    elif char == 'B':
      low = ((high - low) // 2) + 1 + low
      high = high
  row_n = min([low, high])
  # print(row_n)

  high = 7
  low = 0
  for char in col:
    # print(low, high)
    if char == 'L':
      low = low
      high = ((high - low) // 2) + low
    elif char == 'R':
      low = ((high - low) // 2) + 1 + low
      high = high
  col_n = min([low, high])
  # print(col_n)

  id = row_n * 8 + col_n

  row_numbers.append(((row_n, col_n), id))

row_numbers = sorted(row_numbers, key=lambda x: x[1])

print('Part 1:', row_numbers[-1][1])

# print(row_numbers)

low = row_numbers[0][1]
high = row_numbers[-1][1]
result = None
for i in range(low, high):
  # print(i, row_numbers[i - low])
  if i != row_numbers[i - low][1]:
    result = i
    break

print('Part 2:', result)
