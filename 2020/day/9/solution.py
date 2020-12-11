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
start_idx = 0
while True:
  n_range = set()
  total = 0
  for i in range(start_idx, len(numbers)):
    n_range.add(numbers[i])
    total += numbers[i]
    if total >= target:
      break
    
  if total == target:
    print('Part 2:', min(n_range) + max(n_range))
    break
  else:
    start_idx += 1

