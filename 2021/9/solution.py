#!/usr/bin/env python3

import os
from functools import reduce
from operator import mul

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '2199943210',
#   '3987894921',
#   '9856789892',
#   '8767896789',
#   '9899965678',
# ]

grid = [list(map(int, line)) for line in lines]

def get_adj(loc, direction, grid):
  x, y = loc
  x1, y1 = direction
  width = len(grid[0])
  height = len(grid)
  x2 = x + x1
  y2 = y + y1
  if y2 >= 0 and y2 < height and x2 >= 0 and x2 < width:
    return grid[y2][x2]
  else:
    return None


low_points = []
for y, row in enumerate(grid):
  for x, n in enumerate(row):
    up = get_adj((x,y), (0,-1), grid)
    down = get_adj((x,y), (0,1), grid)
    left = get_adj((x,y), (-1,0), grid)
    right = get_adj((x,y), (1,0), grid)
    adjacents = [up, down, left, right]
    adjacents = [i for i in adjacents if i is not None]
    if n == min([n] + adjacents) and n not in adjacents:
      # print(n, adjacents)
      low_points.append((n, (x,y)))

print(sum([1 + i[0] for i in low_points]))

def basin_size(low_point, grid):
  basin_points_visited = []
  basin_points = [low_point]
  basin_size = 0
  while len(basin_points):
    point = basin_points.pop()
    if point in basin_points_visited:
      continue
    n, (x, y) = point
    up = get_adj((x,y), (0,-1), grid)
    down = get_adj((x,y), (0,1), grid)
    left = get_adj((x,y), (-1,0), grid)
    right = get_adj((x,y), (1,0), grid)
    # print(point, [up, down, left, right])
    basin_size += 1
    if up is not None and up != 9:
      basin_points.append((up, (x, y - 1)))
    if down is not None and down != 9:
      basin_points.append((down, (x, y + 1)))
    if left is not None and left != 9:
      basin_points.append((left, (x - 1, y)))
    if right is not None and right != 9:
      basin_points.append((right, (x+1, y)))
    basin_points_visited.append(point)

  return basin_size

basin_sizes = sorted([basin_size(p, grid) for p in low_points])

print(reduce(mul,basin_sizes[-3:]))