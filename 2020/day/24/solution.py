#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
input_txt = [line.strip() for line in file.readlines()]

# input_txt = [
#   'sesenwnenenewseeswwswswwnenewsewsw',
#   'neeenesenwnwwswnenewnwwsewnenwseswesw',
#   'seswneswswsenwwnwse',
#   'nwnwneseeswswnenewneswwnewseswneseene',
#   'swweswneswnenwsewnwneneseenw',
#   'eesenwseswswnenwswnwnwsewwnwsene',
#   'sewnenenenesenwsewnenwwwse',
#   'wenwwweseeeweswwwnwwe',
#   'wsweesenenewnwwnwsenewsenwwsesesenwne',
#   'neeswseenwwswnwswswnw',
#   'nenwswwsewswnenenewsenwsenwnesesenew',
#   'enewnwewneswsewnwswenweswnenwsenwsw',
#   'sweneswneswneneenwnewenewwneswswnese',
#   'swwesenesewenwneswnwwneseswwne',
#   'enesenwswwswneneswsenwnewswseenwsese',
#   'wnwnesenesenenwwnenwsewesewsesesew',
#   'nenewswnwewswnenesenwnesewesw',
#   'eneswnwswnwsenenwnwnwwseeswneewsenese',
#   'neswnwewnwnwseenwseesewsenwsweewe',
#   'wseweeenwnesenwwwswnew',
# ]

def parse(line):
  instruction = []
  line = list(line)
  while len(line):
    char = line.pop(0)

    if char == 's' or char == 'n':
      char2 = line.pop(0)
      instruction.append(char + char2)
    else:
      instruction.append(char)
  return instruction

instructions = list(map(parse, input_txt))

# axial coordinate system https://www.redblobgames.com/grids/hexagons/
P = namedtuple('P', ['q', 'r'])
WHITE = 0
BLACK = 1
directions = {
  'ne': P(1, -1),
  'e': P(1, 0),
  'se': P(0, 1),
  'sw': P(-1, 1),
  'w': P(-1, 0),
  'nw': P(0, -1),
}

def move(pos, direction):
  q, r = pos
  qq, rr = q + directions[direction].q, r + directions[direction].r
  return P(qq, rr)

tiles = defaultdict(int)

for instruction in instructions:
  pos = P(0,0)
  for direction in instruction:
    pos = move(pos, direction)

  if tiles[pos] == WHITE:
    tiles[pos] = BLACK
  else:
    tiles[pos] = WHITE

# print(tiles)
print('Part 1:', sum(tiles.values()))

def n_adjacent_black_tiles(pos, tiles, directions):
  adjacent_tiles = []
  for d in directions.values():
    q, r = pos.q + d.q, pos.r + d.r
    adjacent_tiles.append(tiles[P(q, r)])
  return sum(adjacent_tiles)

def flip_tiles(tiles, directions):
  new_tiles = tiles.copy()

  for q in range(-100,100):
    for r in range(-100,100):
      pos = P(q, r)
      tile = tiles[pos]
      n = n_adjacent_black_tiles(pos, tiles, directions)
      # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
      if tile == BLACK:
        if n == 0 or n > 2:
          new_tiles[pos] = WHITE
          # print(tile, n, 'flipped to white')
        else:
          new_tiles[pos] = BLACK
          # print(tile, n, 'stayed black')
      # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
      elif tile == WHITE:
        if n == 2:
          new_tiles[pos] = BLACK
          # print(tile, n, 'flipped black')
        else:
          new_tiles[pos] = WHITE
          # print(tile, n, 'stayed white')
  
  return new_tiles

N_DAYS = 100
for i in range(1, N_DAYS + 1):
  tiles = flip_tiles(tiles, directions)
  # print(tiles)
  # print(len(tiles))
  if i % 10 == 0:
    print('Day {}:'.format(i), sum(tiles.values()))

print('Part 2:', sum(tiles.values()))

