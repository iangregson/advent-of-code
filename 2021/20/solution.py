#!/usr/bin/env python3

import os
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/ex_input.txt", "r")

class Image():
  def __init__(self, coord_set, algorithm):
    self.coord_set = coord_set
    self.algorithm = algorithm
  
  @property
  def min_x(self):
    return min([x for x,y in self.coord_set])
 
  @property
  def max_x(self):
    return max([x for x,y in self.coord_set])

  @property
  def min_y(self):
    return min([y for x,y in self.coord_set])

  @property
  def max_y(self):
    return max([y for x,y in self.coord_set])

  def __str__(self):
    rows = []
    for y in range(self.min_y-5, self.max_y+5):
      row = ''
      for x in range(self.min_x-5, self.max_x+5):
        if (x,y) in self.coord_set:
          row += '#'
        else:
          row += '.'
      rows.append(row)
    
    return "\n".join(rows) + '\n'

  def __repr__(self):
    return self.__str__()

  def __len__(self):
    return len(self.coord_set)

  def enhance(self, track_on):
    new_coords = set()

    for y in range(self.min_y-5, self.max_y+5):
      for x in range(self.min_x-5, self.max_x+10):
        alg_idx = 0
        bits = ''
        for dy in [-1, 0, 1]:
          for dx in [-1, 0, 1]:
            if ((x+dx,y+dy) in self.coord_set) == track_on:
              bits += '1'
            else:
              bits += '0'
        alg_idx = int(bits, 2)
        assert 0 <= alg_idx < 512
        if (self.algorithm[alg_idx] == '#') != track_on:
          new_coords.add((x,y))
    self.coord_set = new_coords
  

text = file.read().strip()

algorithm, lines = text.split('\n\n')
algorithm = algorithm.strip()
lines = lines.strip().split()
assert len(algorithm) == 512

coord_set = set()
for y, line in enumerate(lines):
  for x, bit in enumerate(line.strip()):
    if bit == '#':
      coord_set.add((x,y))

image = Image(coord_set, algorithm)

for n in range(50):
  if n == 2:
    print(len(image))
  is_even = n % 2 == 0
  image.enhance(is_even)

print(len(image))

