#!/usr/bin/env python3

import os
import math
import numpy
from collections import defaultdict, deque


dir_path = os.path.dirname(os.path.realpath(__file__))

# file = open(dir_path + "/input.txt", "r")
input_txt = '1309'
# input_txt = '8'
# input_txt = '57'
# input_txt = '39'
# input_txt = '71'
# input_txt = '18'
# input_txt = '42'
# print(input_txt)

class Cell(tuple):
  GRID_SERIAL = int(input_txt)

  @staticmethod
  def calc_power_level(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += Cell.GRID_SERIAL
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

  @property
  def power_level(self):
    return Cell.calc_power_level(self.x, self.y)
  @property
  def x(self):
    return self[0]
  @property
  def y(self):
    return self[1]

# print(Cell.calc_power_level((3, 5)))
# print(Cell.calc_power_level((122, 79)))
# print(Cell.calc_power_level((217, 196)))
# print(Cell.calc_power_level((101, 153)))
GRID_SIZE = 300

def find_best_square(size=3):
  grid = numpy.fromfunction(Cell.calc_power_level, (300, 300))
  best_cell = None
  largest_power = 0
  best_size = size

  for width in range(3, size + 1):
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)
    x, y = location[0][0], location[1][0]
    
    if maximum > largest_power:
      largest_power = maximum
      best_cell = (x, y)
      best_size = width

  return best_cell, largest_power, best_size

best_cell, largest_power, size = find_best_square()

print("Part 1 answer:", (best_cell, largest_power, size))

best_cell, largest_power, size = find_best_square(300)
print("Part 2 answer:", (best_cell, largest_power, size))
