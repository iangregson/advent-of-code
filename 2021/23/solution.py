#!/usr/bin/env python3

import os
import sys
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random

# sys.setrecursionlimit(100000)

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [line.strip() for line in file.readlines()]

lines = [
  '#############',
  '#...........#',
  '###B#B#D#D###',
  '  #C#A#A#C#',
  '  #########',
]


lines = [ # 12521
  '#############',
  '#...........#',
  '###B#C#B#D###',
  '  #A#D#C#A#',
  '  #########',
]


COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

game_state = {}

def puzzle_complete(game_state):
  return False

# keep making random moves, according to the constraints, until the 
# puzzle is complete. When any 1 pod starts to move, it tries to go
# directly to it's house. 

# When a move is complete, we want to remember that move and start from
# this position again.



class GameBoard():
  def __init__(self) -> None:
    # it's a 13x5 grid
    self.width = 13
    self.height = 5
    # but the only empty positions are the hallway 
    # on the first row, and it's adjoining rooms
    self.hallway = set([(x,1) for x in range(1,12)])
    self.room_a = set([(3,2),(3,3)])
    self.room_b = set([(5,2),(5,3)])
    self.room_c = set([(7,2),(7,3)])
    self.room_d = set([(9,2),(9,3)])
    self.rooms = set.union(self.room_a, self.room_b, self.room_c, self.room_d)

    self.bots = {
      'A': [(3,3),(9,3)],
      'B': [(3,2),(7,2)],
      'C': [(5,2),(7,3)],
      'D': [(5,3),(9,2)]
    }

  def __str__(self):
    rows = []
    for y in range(self.height):
      row = []
      for x in range(self.width):
        if (x,y) in self.hallway:
          row += '.'
        elif (x,y) in self.rooms:
          row += '.'
        else:
          row += '#'
      rows.append(row)

    for bot, bot_locs in self.bots.items():
      for (x,y) in bot_locs:
        rows[y][x] = bot
    
    return "\n".join(["".join(row) for row in rows])

    

board = GameBoard()

print(board)