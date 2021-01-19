#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
input_txt = [line.strip() for line in file.readlines()]

input_txt = [
  'sesenwnenenewseeswwswswwnenewsewsw',
  'neeenesenwnwwswnenewnwwsewnenwseswesw',
  'seswneswswsenwwnwse',
  'nwnwneseeswswnenewneswwnewseswneseene',
  'swweswneswnenwsewnwneneseenw',
  'eesenwseswswnenwswnwnwsewwnwsene',
  'sewnenenenesenwsewnenwwwse',
  'wenwwweseeeweswwwnwwe',
  'wsweesenenewnwwnwsenewsenwwsesesenwne',
  'neeswseenwwswnwswswnw',
  'nenwswwsewswnenenewsenwsenwnesesenew',
  'enewnwewneswsewnwswenweswnenwsenwsw',
  'sweneswneswneneenwnewenewwneswswnese',
  'swwesenesewenwneswnwwneseswwne',
  'enesenwswwswneneswsenwnewswseenwsese',
  'wnwnesenesenenwwnenwsewesewsesesew',
  'nenewswnwewswnenesenwnesewesw',
  'eneswnwswnwsenenwnwnwwseeswneewsenese',
  'neswnwewnwnwseenwseesewsenwsweewe',
  'wseweeenwnesenwwwswnew',
]

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

tiles = defaultdict(lambda: 'white')

for instruction in instructions:
  pos = P(0,0)
  for direction in instruction:
    pos = move(pos, direction)

  if tiles[pos] == 'white':
    tiles[pos] = 'black'
  else:
    tiles[pos] = 'white'

# print(tiles)
print('Part 1:', list(tiles.values()).count('black'))

def n_adjacent_black_tiles(pos, tiles, directions):
  adjacent_tiles = []
  q, r = pos
  for d in directions:
    qq, rr = q + directions[d].q, r + directions[d].r
    adjacent_tiles.append(tiles[P(qq, rr)])
  # print(adjacent_tiles)
  return adjacent_tiles.count('black')

def flip_tiles(tiles, directions):
  new_tiles = defaultdict(lambda: 'white')

  for tile_pos in list(tiles):
    tile = tiles[tile_pos]
    n = n_adjacent_black_tiles(tile_pos, tiles, directions)
    # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    if tile == 'black':
      if n == 0 or n > 2:
        new_tiles[tile_pos] = 'white'
        print(tile, n, 'flipped to white')
      else:
        new_tiles[tile_pos] = 'black'
        print(tile, n, 'stayed black')
    # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    elif tile == 'white':
      if n == 2:
        new_tiles[tile_pos] = 'black'
        print(tile, n, 'flipped black')
      else:
        new_tiles[tile_pos] = 'white'
        print(tile, n, 'stayed white')
  
  return new_tiles

N_DAYS = 1
for i in range(1, N_DAYS + 1):
  tiles = flip_tiles(tiles, directions)
  print(tiles)
  print('Day {}:'.format(i), list(tiles.values()).count('black'))

