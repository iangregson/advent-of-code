#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
ints = [int(n) for n in file.read().strip().split(',')]

# ints = [3,4,3,1,2]

# tests = [
#   [3,4,3,1,2],
#   [2,3,2,0,1],
#   [1,2,1,6,0,8],
#   [0,1,0,5,6,7,8],
#   [6,0,6,4,5,6,7,8,8],
#   [5,6,5,3,4,5,6,7,7,8],
#   [4,5,4,2,3,4,5,6,6,7],
#   [3,4,3,1,2,3,4,5,5,6],
#   [2,3,2,0,1,2,3,4,4,5],
#   [1,2,1,6,0,1,2,3,3,4,8],
#   [0,1,0,5,6,0,1,2,2,3,7,8],
#   [6,0,6,4,5,6,0,1,1,2,6,7,8,8,8],
#   [5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8],
#   [4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8],
#   [3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8],
#   [2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7],
#   [1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8],
#   [0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8],
#   [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8],
# ]

def next_state(ints):
  new_fish = []
  for idx, i in enumerate(ints):
    if i == 0:
      new_fish.append(8)
      ints[idx] = 6
    else:
      ints[idx] -= 1

  return ints + new_fish



for i in range(80):
  # print(ints)
  ints = next_state(ints)

print(len(ints))

file = open(dir_path + "/input.txt", "r")
ints = [int(n) for n in file.read().strip().split(',')]
ints = [3,4,3,1,2]

ages = defaultdict(int)
for n in ints:
  ages[n] += 1

for _ in range(256):
  ages = {n: ages[n + 1] for n in range(-1, 8)}
  ages[8] = ages[-1]
  ages[6] += ages[-1]
  ages[-1] = 0

print(sum(ages.values()))