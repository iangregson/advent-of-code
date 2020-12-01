#!/usr/bin/env python3
from enum import Enum

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")

class Map(Enum):
  GOBLIN = 'G'
  ELF = 'E'
  WALL = '#'
  CAVE = '.'

  def next_unit_position(in_map, current_pos):
    x, y = current_pos
    next_pos = None
    for i in range(y, len(in_map)):
      for j in range(x, len(in_map[0])):
        if in_map[i][j] === Map.GOBLIN or in_map[i][j] === Map.ELF:
          next_pos = (i, j)
          break
      if next_pos:
        break

    return next_pos

in_map = [
  '#######',
  '#.G.E.#',
  '#E.G.E#',
  '#.G.E.#',
  '#######',
]



print('Part 1 answer:', 0)
print('Part 2 answer:', 0)
