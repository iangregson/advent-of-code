#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

lines = [
  '5483143223',
  '2745854711',
  '5264556173',
  '6141336146',
  '6357385478',
  '4167524645',
  '2176841721',
  '6882881134',
  '4846848554',
  '5283751526',
]


# lines = [
#   '11111',
#   '19991',
#   '19191',
#   '19991',
#   '11111',
# ]

grid = [[int(n) for n in list(line)] for line in lines]

def analyze_octopus(loc, grid, flash_locations):
  dx = [-1, -1, 0, 1, 1, 1, 0, -1]
  dy = [0, 1, 1, 1, 0, -1, -1, -1]

  x, y = loc
  if grid[x][y] > 9 and (x, y) not in flash_locations:
    flash_locations.append((x, y))
    for i in range(8):
      if 0 <= x+dx[i] < len(grid) and 0 <= y+dy[i] < len(grid):
        grid[x+dx[i]][y+dy[i]] += 1
        analyze_octopus((x+dx[i],y+dy[i]), grid, flash_locations)

n_steps = 100
total_flashes = 0
for step in range(n_steps):
  flash_locations = []

  # First, the energy level of each octopus increases by 1.
  grid = [[o + 1 for o in row] for row in grid]

  for y, row in enumerate(grid):
    for x, octopus in enumerate(row):
      analyze_octopus((x,y), grid, flash_locations)
  
  total_flashes += len(flash_locations)
  
  # Finally, any octopus that flashed during this step has its energy level set to 0, 
  # as it used all of its energy to flash.
  grid = [[0 if o > 9 else o for o in row] for row in grid]

  # for l in grid:
  #   print(l)
  # print()

print(total_flashes)

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '5483143223',
#   '2745854711',
#   '5264556173',
#   '6141336146',
#   '6357385478',
#   '4167524645',
#   '2176841721',
#   '6882881134',
#   '4846848554',
#   '5283751526',
# ]

# lines = [
#   '11111',
#   '19991',
#   '19191',
#   '19991',
#   '11111',
# ]

grid = [[int(n) for n in list(line)] for line in lines]

n_steps = 10000
total_flashes = 0
for step in range(1, n_steps + 1):
  flash_locations = []

  # First, the energy level of each octopus increases by 1.
  grid = [[o + 1 for o in row] for row in grid]

  for y, row in enumerate(grid):
    for x, octopus in enumerate(row):
      analyze_octopus((x,y), grid, flash_locations)
  
  total_flashes += len(flash_locations)
  
  # Finally, any octopus that flashed during this step has its energy level set to 0, 
  # as it used all of its energy to flash.
  grid = [[0 if o > 9 else o for o in row] for row in grid]

  
  # for l in grid:
  #   print(l)
  # print()
  
  if (sum([sum(line) for line in grid])) == 0:
    print(step)
    break

print(total_flashes)