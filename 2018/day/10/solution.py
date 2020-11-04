#!/usr/bin/env python3

import os
import math
from collections import defaultdict, deque


dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]
# print(input_txt)
# input_txt = [
#   'position=< 9,  1> velocity=< 0,  2>',
#   'position=< 7,  0> velocity=<-1,  0>',
#   'position=< 3, -2> velocity=<-1,  1>',
#   'position=< 6, 10> velocity=<-2, -1>',
#   'position=< 2, -4> velocity=< 2,  2>',
#   'position=<-6, 10> velocity=< 2, -2>',
#   'position=< 1,  8> velocity=< 1, -1>',
#   'position=< 1,  7> velocity=< 1,  0>',
#   'position=<-3, 11> velocity=< 1, -2>',
#   'position=< 7,  6> velocity=<-1, -1>',
#   'position=<-2,  3> velocity=< 1,  0>',
#   'position=<-4,  3> velocity=< 2,  0>',
#   'position=<10, -3> velocity=<-1,  1>',
#   'position=< 5, 11> velocity=< 1, -2>',
#   'position=< 4,  7> velocity=< 0, -1>',
#   'position=< 8, -2> velocity=< 0,  1>',
#   'position=<15,  0> velocity=<-2,  0>',
#   'position=< 1,  6> velocity=< 1,  0>',
#   'position=< 8,  9> velocity=< 0, -1>',
#   'position=< 3,  3> velocity=<-1,  1>',
#   'position=< 0,  5> velocity=< 0, -1>',
#   'position=<-2,  2> velocity=< 2,  0>',
#   'position=< 5, -2> velocity=< 1,  2>',
#   'position=< 1,  4> velocity=< 2,  1>',
#   'position=<-2,  7> velocity=< 2, -2>',
#   'position=< 3,  6> velocity=<-1, -1>',
#   'position=< 5,  0> velocity=< 1,  0>',
#   'position=<-6,  0> velocity=< 2,  0>',
#   'position=< 5,  9> velocity=< 1, -2>',
#   'position=<14,  7> velocity=<-2,  0>',
#   'position=<-3,  6> velocity=< 2, -1>',
# ]
# print(input_txt)

class Point(tuple):
  @staticmethod
  def parse(line):
    l, r = line.split('> ')
    position = l.split('=<').pop().strip()
    x, y = [int(i.strip()) for i in position.split(',')]

    velocity = r.split('=<').pop().strip()[:-1]
    vx, vy = [int(i.strip()) for i in velocity.split(',')]

    return (x, y, vx, vy)
  
  @staticmethod
  def next(point):
    x, y, vx, vy = point
    x, y = x + vx, y + vy
    return (x, y, vx, vy)

  def __str__(self):
    return '<{}, {}> <{}, {}>'.format(self.x, self.y, self.vx, self.vy)

  @property
  def position(self):
    return (self.x, self.y)
  
  @property
  def velocity(self):
    return (self.vx, self.vy)
  
  @property
  def x(self):
    return self[0]
  
  @property
  def y(self):
    return self[1]
  
  @property
  def vx(self):
    return self[2]
  
  @property
  def vy(self):
    return self[3]


class Grid():
  def __init__(self, input_txt):
    self.points = defaultdict()
    for line in input_txt:
      p = Point.parse(line)      
      p = Point(p)
      # print(p)
      self.points[p] = p

  @property
  def min_x(self):
    return min([p.x for p in self.points.keys()])
  @property
  def max_x(self):
    return max([p.x for p in self.points.keys()]) + 1
  @property
  def min_y(self):
    return min([p.y for p in self.points.keys()])
  @property
  def max_y(self):
    return max([p.y for p in self.points.keys()]) + 1


  def plot(self):
    known_positions = [p.position for p in self.points]
    print('\n')
    for y in range(self.min_y, self.max_y):
      row = []
      for x in range(self.min_x, self.max_x):
        p = (x, y)
        if p in known_positions:
          row.append('#')
        else:
          row.append('.')
      print("".join(row))

    print('\n')

  def next_state(self):
    new_points = defaultdict()
    for point in self.points:
      p = Point.next(point)
      p = Point(p)
      new_points[p] = p
    # print(self.points, new_points)
    self.points = new_points



points = Grid(input_txt)

N_TURNS = 100000
W = 100

for T in range(N_TURNS):
  if points.min_x+W >= points.max_x and points.min_y + W >= points.max_y:
    print('T', T)
    points.plot()
  
  points.next_state()

print("Part 1 answer:", 0)
print("Part 2 answer:", 0)
