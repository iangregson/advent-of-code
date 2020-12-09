#!/usr/bin/env python3

import os
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '35',
#   '20',
#   '15',
#   '25',
#   '47',
#   '40',
#   '62',
#   '55',
#   '65',
#   '95',
#   '102',
#   '117',
#   '150',
#   '182',
#   '127',
#   '219',
#   '299',
#   '277',
#   '309',
#   '576',
# ]

PREAMBLE_LEN = 25
numbers = [int(line) for line in lines]
result = None
for idx, n in enumerate(numbers):
  if idx < PREAMBLE_LEN: continue
  preamble = numbers[idx-PREAMBLE_LEN:idx]
  if n not in [sum(pair) for pair in itertools.combinations(preamble, 2)]:
    result = n
    break

print('Part 1:', result)

target = result
target_range = None
start_idx = 0
while not target_range:
  n_range = []
  # print('\n start range')
  for i in range(start_idx, len(numbers)):
    n_range.append(numbers[i])
    # print(n_range)
    if sum(n_range) >= target:
      break
    
  if sum(n_range) == target:
    target_range = n_range
  else:
    start_idx += 1

print('Part 2:', min(target_range) + max(target_range))
