#!/usr/bin/env python3

import os
import re
from collections import defaultdict
import collections

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/ex_input.txt", "r")
txt = file.read()

coords, folds = txt.split('\n\n')
coords = coords.split('\n')
folds = folds.split('\n')
folds = [line.replace('fold along ', '') for line in folds]

first_fold = folds[0]

coords = [tuple(map(int, c.split(','))) for c in coords]

# print(coords)

def fold(f, coords):
  direction, n = f.split('=')
  n = int(n)

  new_coords = set()
  if direction == 'y':
    coords = sorted(coords, key=lambda x: x[1])
    for c in coords:
      x, y = c
      if y < n:
        new_coords.add(c)
      if y == n:
        continue
      if y > n:
        dy = y - n
        new_y = n - dy
        new_coords.add((x, new_y))
  else:
    coords = sorted(coords, key=lambda x: x[0])
    for c in coords:
      x, y = c
      if x < n:
        new_coords.add(c)
      if x == n:
        continue
      if x > n:
        dx = x - n
        new_x = n - dx
        new_coords.add((new_x, y))

  return new_coords


print(len(fold(first_fold, coords.copy())))

for f in folds:
  coords = fold(f, coords.copy())


max_x = max(map(lambda x: x[0], coords))
max_y = max(map(lambda x: x[1], coords))

for y in range(0, max_y + 1):
  line = ''
  for x in range(0, max_x + 1):
    if (x, y) in coords:
      line += '#'
    else:
      line += '.'
  print(line)