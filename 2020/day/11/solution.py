#!/usr/bin/env python3

import os
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'L.LL.LL.LL',
#   'LLLLLLL.LL',
#   'L.L.L..L..',
#   'LLLL.LL.LL',
#   'L.LL.LL.LL',
#   'L.LLLLL.LL',
#   '..L.L.....',
#   'LLLLLLLLLL',
#   'L.LLLLLL.L',
#   'L.LLLLL.LL',
# ]

# print(grid)

def get_seat_at_pos(grid, pos):
  x, y = pos
  
  if x < 0 or y < 0:
    return None
  try:
    return grid[y][x]
  except IndexError:
    return None

def get_adjacent_seats(grid, pos):
  x, y = pos

  adjacent_positions = [
    (x-1, y-1), # top left
    (x, y-1), # top middle
    (x+1, y-1), # top right
    (x-1, y), # middle left
    (x+1, y), # middle right
    (x-1, y+1), # bottom left
    (x, y+1), # bottom middle
    (x+1, y+1), # bottom right
  ]

  seats = [get_seat_at_pos(grid, a_pos) for a_pos in adjacent_positions]

  return seats


def next_state(grid, get_adjacent_seats, seat_eviction_threshold):
  n_changes = 0
  new_grid = [row.copy() for row in grid]

  for y, row in enumerate(new_grid):
    for x, seat in enumerate(row):
      seat = get_seat_at_pos(grid, (x, y))
      # if it's floor do nothing
      if seat == '.':
        continue

      adjacent_seats = get_adjacent_seats(grid, (x, y))
      n_adjacent = adjacent_seats.count('#')
      
      # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
      if seat == 'L' and n_adjacent == 0:
        new_grid[y][x] = '#'
        n_changes += 1
      elif seat == '#' and n_adjacent >= seat_eviction_threshold:
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        new_grid[y][x] = 'L'
        n_changes += 1
      else:
        # Otherwise, the seat's state does not change.
        new_grid[y][x] = seat

  return new_grid, n_changes

def count_occupied(grid):
  n_occupied = 0
  for row in grid:
    for seat in row:
      if seat == '#':
        n_occupied += 1

  return n_occupied

def show_grid(grid):
  print('\n')
  for row in grid:
    print("".join(row))

n_changes = float('inf')
grid = [list(l) for l in lines]
while n_changes > 0:
  # show_grid(grid)
  grid, n_changes = next_state(grid, get_adjacent_seats, 4)

print('Part 1:', count_occupied(grid))

# lines = [
#   '.......#.',
#   '...#.....',
#   '.#.......',
#   '.........',
#   '..#L....#',
#   '....#....',
#   '.........',
#   '#........',
#   '...#.....',
# ]

# lines = [
#   '.............',
#   '.L.L.#.#.#.#.',
#   '.............',
# ]

# lines = [
#   '.##.##.',
#   '#.#.#.#',
#   '##...##',
#   '...L...',
#   '##...##',
#   '#.#.#.#',
#   '.##.##.',
# ]

def get_adjacent_seats_pt2(grid, pos):
  x, y = pos

  adjacent_directions = [
    (-1, -1), # top left
    (0, -1), # top middle
    (1, -1), # top right
    (-1, 0), # middle left
    (1, 0), # middle right
    (-1, 1), # bottom left
    (0, 1), # bottom middle
    (1, 1), # bottom right
  ]
  
  seats = []

  for direction in adjacent_directions:
    seat = None
    xx, yy = x, y
    while not seat:
      xx, yy = xx + direction[0], yy + direction[1]
      seat_pos = get_seat_at_pos(grid, (xx, yy))
      if seat_pos == '.':
        continue
      elif seat_pos == None:
        break
      else:
        seat = seat_pos
    seats.append(seat)

  return seats

n_changes = float('inf')
grid = [list(l) for l in lines]
while n_changes > 0:
  # show_grid(grid)
  grid, n_changes = next_state(grid, get_adjacent_seats_pt2, 5)

print('Part 2:', count_occupied(grid))