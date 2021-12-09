#!/usr/bin/env python3

import os
from enum import Enum
from collections import namedtuple

class Opcode(Enum):
    HALT = 99
    ADD = 1
    MULTIPLY = 2

class IntCodeComputer():
  def __init__(self, program):
    self.program = program
    self.head = 0

  @property
  def opcode(self):
    return Opcode(self.program[self.head])

  def run(self, program = None):
    if program != None:
      self.program = program

    while self.opcode != Opcode.HALT:
      # print(self.opcode)
      if self.opcode == Opcode.ADD:
        a, b = self.read()
        self.write(a + b)
      elif self.opcode == Opcode.MULTIPLY:
        a, b = self.read()
        self.write(a * b)
      else:
        raise Exception()
      
      self.step()

  def step(self):
    self.head += 4
  
  def read(self):
    pos_1 = self.program[self.head + 1]
    pos_2 = self.program[self.head + 2]
    return self.program[pos_1], self.program[pos_2]
  
  def write(self, value):
    pos = self.program[self.head + 3]
    self.program[pos] = value

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
wires = [line.strip() for line in file.readlines()]

# wires = [
#   'R75,D30,R83,U83,L12,D49,R71,U7,L72',
#   'U62,R66,U55,R34,D71,R55,D58,R83'
# ] # distance 159
# wires = [
#   'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
#   'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
# ] # distance 135
# wires = [
#   'R8,U5,L5,D3',
#   'U7,R6,D4,L4'
# ] # distance 6

P = namedtuple('Point', ['x', 'y'])
D = namedtuple('Direction', ['direction', 'distance'])

def parse(d):
  return d[0], int(d[1:])

wire_a = [D(*parse(d)) for d in wires[0].split(',')]
wire_b = [D(*parse(d)) for d in wires[1].split(',')]

def walk(wire):
  points = [P(0,0)]
  for d in wire:
    if d.direction == 'U':
      x = points[-1].x
      for i in range(d.distance):
        y = points[-1].y + 1
        points.append(P(x, y))
    elif d.direction == 'D':
      x = points[-1].x
      for i in range(d.distance):
        y = points[-1].y - 1
        points.append(P(x, y))
    elif d.direction == 'L':
      y = points[-1].y
      for i in range(d.distance):
        x = points[-1].x - 1
        points.append(P(x, y))
    elif d.direction == 'R':
      y = points[-1].y
      for i in range(d.distance):
        x = points[-1].x + 1
        points.append(P(x, y))
  return points[1:]


wire_a_points = walk(wire_a)
wire_b_points = walk(wire_b)

# print(wire_a_points)
# print(wire_b_points)
intersections = set(wire_a_points).intersection(set(wire_b_points))
distances = [abs(p.x) + abs(p.y) for p in intersections]

print(min(distances))

def steps_to_intersection(point, wire):
  return wire.index(point) + 1

steps = []
for point in intersections:
  wire_a_steps = steps_to_intersection(point, wire_a_points)
  wire_b_steps = steps_to_intersection(point, wire_b_points)
  steps.append(wire_a_steps + wire_b_steps)

print(min(steps))