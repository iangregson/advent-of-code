#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

numbers = [int(l) for l in lines]

# numbers = [
#   1721,
#   979,
#   366,
#   299,
#   675,
#   1456,
# ]

result = None

for i in numbers:
  target = 2020 - i
  if target in numbers:
    result = i * target

print('Part 1:', result)

def find_summands(total, numbers):
  for i in numbers:
    target = total - i
    if target in numbers:
      return i, target
  return i, None


result = None
for i in numbers:
  target = 2020 - i
  j, k = find_summands(target, numbers)
  if k is not None:
    result = i * j * k
    break


print('Part 2:', result)