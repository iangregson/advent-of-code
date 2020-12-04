#!/usr/bin/env python3

import os
from collections import namedtuple
from functools import reduce
from operator import mul

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '..##.......',
#   '#...#...#..',
#   '.#....#..#.',
#   '..#.#...#.#',
#   '.#...##..#.',
#   '..#.##.....',
#   '.#.#.#....#',
#   '.#........#',
#   '#.##...#...',
#   '#...##....#',
#   '.#..#...#.#',
# ]

P = namedtuple('P', ['x', 'y'])
Slope = namedtuple('Slope', ['right', 'down'])
GridDimensions = namedtuple('GridDimenions', ['width', 'height'])

def next_pos(p, slope, grid_dimensions):
  x = (p.x + slope.right) % grid_dimensions.width
  y = (p.y + slope.down)

  if y >= grid_dimensions.height:
    return None
  
  return P(x, y)

n_trees = 0
pos = P(0,0)
while pos:
  if lines[pos.y][pos.x] == '#':
    n_trees += 1
  pos = next_pos(pos, Slope(3, 1), GridDimensions(len(lines[0]), len(lines)))

print('Part 1:', n_trees)

slopes = [
  Slope(1, 1),
  Slope(3, 1),
  Slope(5, 1),
  Slope(7, 1),
  Slope(1, 2),
]

n_trees_slope = []

for slope in slopes:
  n_trees = 0
  pos = P(0,0)
  while pos:
    if lines[pos.y][pos.x] == '#':
      n_trees += 1
    pos = next_pos(pos, slope, GridDimensions(len(lines[0]), len(lines)))
  n_trees_slope.append(n_trees)

print('Part 2:', reduce(mul, n_trees_slope))