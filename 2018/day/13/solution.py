#!/usr/bin/env python3

import os
import math
from collections import defaultdict, deque, namedtuple
from enum import Enum

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
file = open(dir_path + "/input.test.txt", "r")
file = open(dir_path + "/input.test2.txt", "r")
lines = file.readlines()
lines = [list(line.replace('\n', '')) for line in lines]

class Map():
  def __init__(self, lines):
    self.m = lines
    carts = []
    for y, row in enumerate(self.m):
      for x, char in enumerate(row):
        if Map.is_cart(char):
          carts.append(Cart(char, (x, y)))
    self.carts = carts
    self.crashes = set()
  
  def __str__(self):
    return "\n".join(["".join(row) for row in self.m])

  def next_state(self):
    for cart in self.carts:
      if cart.is_crashed():
        continuel
      # print(cart)
      self.move_cart(cart)
   

  def move_cart(self, cart):
    
    curr_position = cart.location
    next_position = cart.next_position()

    x, y = curr_position
    xx, yy = next_position
    cur_char = cart.map_char
    next_char = self.m[yy][xx]
    print('moving from ({}, {}) to ({}, {})'.format(curr_position, cur_char, next_position, next_char))
    
    self.m[y][x] = cur_char
    
    if Map.is_cart(next_char) or next_char == 'X':
      print('crash!', (xx, yy))
      cart.crash()
      self.m[yy][xx] = 'X'
      self.crashes.add((xx, yy))
      return

    cart.map_char = next_char
    cart.location = (xx, yy)
    if Map.is_left_turn(cart.map_char, cart.direction):
      cart.turn_left()
    elif Map.is_right_turn(cart.map_char, cart.direction):
      cart.turn_right()
    elif Map.is_intersection(cart.map_char):
      cart.turn_intersection()

    self.m[yy][xx] = cart.icon

    return


  @staticmethod
  def is_cart(s):
    return s in 'v^<>'
  @staticmethod
  def is_intersection(s):
    return s == '+'
  @staticmethod
  def is_left_turn(s, direction):
    if direction == 'E' or direction == 'W':
      return str(s) == '/'
    elif direction == 'N' or direction == 'S':
      return str(s) == "\\"
  @staticmethod
  def is_right_turn(s, direction):
    if direction == 'E' or direction == 'W':
      return str(s) == "\\"
    elif direction == 'N' or direction == 'S':
      return str(s) == '/'
  @staticmethod
  def is_path(s):
    return s in '-|'

class Cart(object):
  def __init__(self, icon, location, map_char=None, direction=None):
    self.intersection_turn_count = 0
    self.location = location
    self.icon = icon
    if not map_char:
      if icon in '<>':
        self.map_char = '-'
      elif icon in 'v^':
        self.map_char = '|'
    if not direction:
      if icon == '<':
        self.direction = 'W'
      elif icon == '>':
        self.direction = 'E'
      elif icon == '^':
        self.direction = 'N'
      elif icon == 'v':
        self.direction = 'S'

  def __iter__(self):
    for v in [self.icon, self.location, self.map_char, self.direction]:
      yield v

  def __str__(self):
    return str(tuple(self))

  def next_position(self):
    directions = {
      'W': (-1, 0),
      'E': (1, 0),
      'N': (0, -1),
      'S': (0, 1),
    }

    xx = self.x + directions[self.direction][0]
    yy = self.y + directions[self.direction][1]

    return (xx, yy)

  def crash(self):
    self.icon = 'X'
    self.map_char = 'X'
  
  def is_crashed(self):
    return self.icon == 'X'

  def turn_left(self):
    # print('turn left')
    if self.direction == 'N':
      self.direction = 'W'
      self.icon = '<'
    elif self.direction == 'S':
      self.direction = 'E'
      self.icon = '>'
    elif self.direction == 'W':
      self.direction = 'S'
      self.icon = 'v'
    elif self.direction == 'E':
      self.direction = 'N'
      self.icon = '^'

  def turn_right(self):
    # print('turn right')
    if self.direction == 'N':
      self.direction = 'E'
      self.icon = '>'
    elif self.direction == 'S':
      self.direction = 'W'
      self.icon = '<'
    elif self.direction == 'W':
      self.direction = 'N'
      self.icon = '^'
    elif self.direction == 'E':
      self.direction = 'S'
      self.icon = 'v'

  def turn_intersection(self):
    # print('turn intersection')
    if self.intersection_turn_count == 0:
      self.turn_left()
      self.intersection_turn_count += 1
      return
    if self.intersection_turn_count == 1:
      self.intersection_turn_count += 1
      return
    if self.intersection_turn_count == 2:
      self.turn_right()
      self.intersection_turn_count = 0
      return


  @property
  def x(self):
    return self.location[0]
  @property
  def y(self):
    return self.location[1]

M = Map(lines)
# print(M)

N_STEPS = 1000
N = 0
while N < N_STEPS:
  M.next_state()
  print(M)
  print('\n')
  N += 1

  if len(M.crashes) > 0:
    break

print(M.crashes)

print("Part 1 answer:", M.crashes[0] if len(M.crashes) > 0 else None)
print("Part 2 answer:", 0)
