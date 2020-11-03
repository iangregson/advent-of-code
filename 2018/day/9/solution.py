#!/usr/bin/env python3

import os
import math
from collections import defaultdict, deque


dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read()
# input_txt = '9 players; last marble is worth 25 points'
# input_txt = '10 players; last marble is worth 1618 points'
# input_txt = '13 players; last marble is worth 7999 points'
# input_txt = '17 players; last marble is worth 1104 points'
# input_txt = '21 players; last marble is worth 6111 points'
# input_txt = '30 players; last marble is worth 5807 points'
print(input_txt)

class MarbleGame():
  def __init__(self, N_PLAYERS, MAX_POINTS):
    self.MAX_POINTS = MAX_POINTS
    self.N_PLAYERS = N_PLAYERS
    self.ring = deque([0])
    self.scores = defaultdict(int)
    self.players = MarbleGame.player_gen(N_PLAYERS)
    self.marbles = MarbleGame.marble_gen(MAX_POINTS)

  @staticmethod
  def is_mult_of_23(n):
    return (n % 23) == 0
  
  @staticmethod
  def marble_gen(MAX_POINTS):
    i = 0
    while True:
      i += 1
      if i > MAX_POINTS:
        yield None
      else:
        yield i
  
  @staticmethod
  def player_gen(N_PLAYERS):
    i = 0
    while True:
      i += 1
      yield i % N_PLAYERS

  def play(self):
    current_marble = 0
    while current_marble <= self.MAX_POINTS:
      current_marble = next(self.marbles)
      current_player = next(self.players)

      if not current_marble:
        break

      if MarbleGame.is_mult_of_23(current_marble):
        self.ring.rotate(7)
        self.scores[current_player] += current_marble + self.ring.pop()
        self.ring.rotate(-1)
      else:
        self.ring.rotate(-1)
        self.ring.append(current_marble)

  @property
  def high_score(self):
    return max(self.scores.values()) if self.scores else 0


N_PLAYERS, MAX_POINTS = int(input_txt.split()[0]), int(input_txt.split()[-2])
# print(N_PLAYERS, MAX_POINTS)


game = MarbleGame(N_PLAYERS, MAX_POINTS)
game.play()
print("Part 1 answer:", game.high_score)

game = MarbleGame(N_PLAYERS, MAX_POINTS * 100)
game.play()
print("Part 2 answer:", game.high_score)
