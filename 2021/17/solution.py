#!/usr/bin/env python3

import os
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
line = file.read().strip()

line = 'target area: x=244..303, y=-91..-54'
line = 'target area: x=20..30, y=-10..-5'

class Simulator():
  def __init__(self, tagret_area):
    self.target_area = tagret_area
    self.gravity = 1
    self.drag = 1
  
  def in_target_area(self, pos):
    x,y = pos
    x1,x2,y1,y2 = self.target_area
    return x1 <= x <= x2 and y1 <= y <= y2 

  def run(self, v):
    max_y = 0
    vx, vy = v
    x, y = (0,0)
    while x <= x2 and y1 <= y:
      x, y = x+vx, y+vy
      vx, vy = max(0, vx - self.drag), vy - self.gravity
      max_y = max(max_y, y)
      if self.in_target_area((x,y)):
        return max_y
    
    return -1
  
sim = Simulator((244,303,-91,-54))
# sim = Simulator((20,30,-10,-5))
attempts = {}
x1,x2,y1,y2 = sim.target_area
for x in range(x2+1):
  for y in range(y1, -y1):
    max_y = sim.run((x,y))
    if max_y >= 0:
      attempts[(x,y)] = max_y

print(max(attempts.values()))
print(len(attempts.keys()))
