#!/usr/bin/env python3

import os
from collections import namedtuple
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'F10',
#   'N3',
#   'F7',
#   'R90',
#   'F11'
# ]

# print(lines)

I = namedtuple('I', ['action', 'value'])
P = namedtuple('P', ['x', 'y'])

class Ship():
  def __init__(self):
    self.facing = 'E'
    self.degrees = 90
    self.pos = P(0,0)

  def move(self, instruction):
    directions = {
      'N': (0, -1),
      'E': (1, 0),
      'S': (0, 1),
      'W': (-1, 0),
    }
    rotations = {
      90: 'E',
      180: 'S',
      270: 'W',
      0: 'N',
    }

    if instruction.action == 'F':
      d = directions[self.facing]
      xx = d[0] * instruction.value
      yy = d[1] * instruction.value
      x = self.pos.x + xx
      y = self.pos.y + yy
      self.pos = P(x, y)
    elif instruction.action == 'L':
      self.degrees = (self.degrees - instruction.value + 360) % 360
      self.facing = rotations[self.degrees]
    elif instruction.action == 'R':
      self.degrees = (self.degrees + instruction.value + 360) % 360
      self.facing = rotations[self.degrees]
    else:
      d = directions[instruction.action]
      xx = d[0] * instruction.value
      yy = d[1] * instruction.value
      x = self.pos.x + xx
      y = self.pos.y + yy
      self.pos = P(x, y)

  def manhattan_distance(self):
    return self.pos.x + self.pos.y


ship = Ship()

for line in lines:
  action = line[0]
  value = int(line[1:])
  instruction = I(action, value)
  ship.move(instruction)

print('Part 1:', ship.pos, ship.manhattan_distance())

import math

def rotate(point, angle, origin=(0,0)):
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx, 0)), int(round(qy, 0))

class Ship():
  def __init__(self):
    self.facing = 'E'
    self.degrees = 90
    self.pos = P(0,0)
    self.waypoint = P(10,-1)
    self.waypoint_pos = P(10,-1)

  def __str__(self):
    return "pos={} waypoint={} manhattan={}".format(self.pos, self.waypoint, self.manhattan_distance())

  def move(self, instruction):
    directions = {
      'N': (0, -1),
      'E': (1, 0),
      'S': (0, 1),
      'W': (-1, 0),
    }

    if instruction.action == 'F':
      xx = self.waypoint.x * instruction.value
      yy = self.waypoint.y * instruction.value
      x = self.pos.x + xx
      y = self.pos.y + yy
      self.pos = P(x, y)
    elif instruction.action == 'L':
      wx, wy = rotate(self.waypoint, -instruction.value)
      self.waypoint = P(wx, wy)
    elif instruction.action == 'R':
      wx, wy = rotate(self.waypoint, instruction.value)
      self.waypoint = P(wx, wy)
    else:
      d = directions[instruction.action]
      xx = d[0] * instruction.value
      yy = d[1] * instruction.value
      
      wx = self.waypoint.x + xx
      wy = self.waypoint.y + yy
      self.waypoint = P(wx, wy)

    # print(instruction, self.pos, self.facing)

  def manhattan_distance(self):
    return abs(self.pos.x) + abs(self.pos.y)

ship = Ship()

for line in lines:
  action = line[0]
  value = int(line[1:])
  instruction = I(action, value)
  ship.move(instruction)
  # print(instruction, ship)

print('Part 2:', ship.pos, ship.waypoint, ship.manhattan_distance())
