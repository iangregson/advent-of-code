#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '.#.',
#   '..#',
#   '###',
# ]


# print(lines)

P = namedtuple('P', ['x','y','z'])

cells = defaultdict(lambda: '.')

for y, line in enumerate(lines):
  for x, char in enumerate(line):
    if char == '.': continue
    z = 0
    pos = P(x, y, z)
    cells[pos] = char


def get_neighbors(cell_pos):
  positions = []
  X, Y, Z = cell_pos
  for z in range(-1, 2):
    for y in range(-1, 2):
      for x in range(-1, 2):
        p = P(X+x, Y+y, Z+z)
        if p != cell_pos:
          positions.append(p)

  return positions

def is_active(cell, cells):
  return cells[cell] == '#'

def get_min(list_positions, xyz):
  if xyz == 'x':
    return min([p.x for p in list_positions])
  elif xyz == 'y':
    return min([p.y for p in list_positions])
  elif xyz == 'z':
    return min([p.z for p in list_positions])

def get_max(list_positions, xyz):
  if xyz == 'x':
    return max([p.x for p in list_positions])
  elif xyz == 'y':
    return max([p.y for p in list_positions])
  elif xyz == 'z':
    return max([p.z for p in list_positions])

def visualize_state(cells):
  min_x, max_x = get_min(list(cells), 'x'), get_max(list(cells), 'x')
  min_y, max_y = get_min(list(cells), 'y'), get_max(list(cells), 'y')
  min_z, max_z = get_min(list(cells), 'z'), get_max(list(cells), 'z')

  for z in range(min_z, max_z + 1):
    print('z =', z)
    for y in range(min_y, max_y + 1):
      row = []
      for x in range(min_x, max_x + 1):
        row.append(cells[P(x, y, z)])
      print("".join(row))


def next_state(prev_state):
  new_state = defaultdict(lambda: '.')
  # walk the 3d grid
  min_x, max_x = get_min(list(prev_state), 'x'), get_max(list(prev_state), 'x')
  min_y, max_y = get_min(list(prev_state), 'y'), get_max(list(prev_state), 'y')
  min_z, max_z = get_min(list(prev_state), 'z'), get_max(list(prev_state), 'z')

  # build the new state  
  for z in range(min_z - 1, max_z + 2):
    for y in range(min_y - 1, max_y + 2):
      for x in range(min_x -1, max_x + 2):
        current_pos = P(x, y, z)
        current_state = prev_state[current_pos]
        neighbors = get_neighbors(current_pos)

        n_active_neighbors = sum([1 if is_active(n, prev_state) else 0 for n in neighbors])

        if current_state == '#':
          # If a cube is active and exactly 2 or 3 of its neighbors are also active,
          # the cube remains active. Otherwise, the cube becomes inactive.
          if n_active_neighbors == 2 or n_active_neighbors == 3:
            current_state = '#'
          else:
            current_state = '.'
        else:
          # If a cube is inactive but exactly 3 of its neighbors are active,
          # the cube becomes active. Otherwise, the cube remains inactive.
          if n_active_neighbors == 3:
            current_state = '#'
          else:
            current_state = '.'

        new_state[current_pos] = current_state
  
  return new_state

# print(cells)

state = cells
for _ in range(6):
  state = next_state(state)


print('Part 1:', sum([1 if x == '#' else 0 for x in state.values()]))

P = namedtuple('P', ['x','y','z','w'])

cells = defaultdict(lambda: '.')

for y, line in enumerate(lines):
  for x, char in enumerate(line):
    if char == '.': continue
    z = 0
    w = 0
    pos = P(x, y, z, w)
    cells[pos] = char


def get_neighbors(cell_pos):
  positions = []
  X, Y, Z, W = cell_pos
  for w in range(-1, 2):
    for z in range(-1, 2):
      for y in range(-1, 2):
        for x in range(-1, 2):
          p = P(X+x, Y+y, Z+z, W+w)
          if p != cell_pos:
            positions.append(p)

  return positions

def next_state(prev_state):
    neighbor_count = {}

    # Find each active coordinate, and update its neighbors
    for this_coord in prev_state:
        if prev_state[this_coord] == '#':
            neighbor_list = get_neighbors(this_coord)
            for this_neighbor in neighbor_list:
                # If this neighbor hasn't been added, add it
                try:
                    neighbor_count[this_neighbor] += 1
                except KeyError:
                    neighbor_count[this_neighbor] = 1

    n_map = defaultdict(lambda: '.')
    active_count = 0

    # Go through each coord with active neighbors and see if it needs to change its state
    for this_coord in neighbor_count:
        # If the coord is newly viewed, then its initial state must be inactive.
        try:
            current_state = prev_state[this_coord]
        except KeyError:
            current_state = '.'
        n_active_neighbors = neighbor_count[this_coord]


        if current_state == '#':
          # If a cube is active and exactly 2 or 3 of its neighbors are also active,
          # the cube remains active. Otherwise, the cube becomes inactive.
          if n_active_neighbors == 2 or n_active_neighbors == 3:
            current_state = '#'
          else:
            current_state = '.'
        else:
          # If a cube is inactive but exactly 3 of its neighbors are active,
          # the cube becomes active. Otherwise, the cube remains inactive.
          if n_active_neighbors == 3:
            current_state = '#'
          else:
            current_state = '.'
        n_map[this_coord] = current_state
        if n_map[this_coord] == '#':
            active_count += 1

    return n_map

state = cells
for i in range(6):
    state = next_state(state)

print('Part 2:', sum([1 if x == '#' else 0 for x in state.values()]))
