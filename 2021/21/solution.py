#!/usr/bin/env python3

import sys
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random

# sys.setrecursionlimit(100000)

input_text = """
  Player 1 starting position: 9
  Player 2 starting position: 3
  """

# input_text = """
#   Player 1 starting position: 4
#   Player 2 starting position: 8
#   """

player1, player2 = input_text.strip().split('\n')
player1_start = int(player1.split(': ')[-1].strip())
player2_start = int(player2.split(': ')[-1].strip())
# print(player1)
# print(player2)


def Die(n):
    faces = [i+1 for i in range(n)]
    roll_count = -1
    while True:
      roll_count += 1
      yield faces[roll_count % n]


class Player():
  def __init__(self, id, start_pos, die, track, winning_score=1000) -> None:
    self.pos = start_pos
    self.die = die
    self.score = 0
    self.track = track
    self.id = id
    self.winning_score = winning_score

  def __str__(self):
    return f"Player {self.id} score: {self.score}"
  
  def __repr__(self):
    return (self.score, self.pos)

  def __hash__(self):
    return hash(self.__repr__())

  @property
  def is_winner(self):
    return self.score >= self.winning_score

  def move(self, n_places):
    move = (self.pos + n_places) - 1
    self.pos = self.track[move % len(track)]

  def turn(self):
    n_dice_rolls = 3
    dice_values = sum([next(self.die) for _ in range(n_dice_rolls)])
    self.move(dice_values)
    self.score += self.pos



die = Die(100)
track = [1,2,3,4,5,6,7,8,9,10]

player1 = Player(1, player1_start, die, track)
player2 = Player(2, player2_start, die, track)

dice_roll_count = 0
while True:
  player1.turn()
  dice_roll_count += 3
  if player1.is_winner:
    print(dice_roll_count, player1.score, player2.score, dice_roll_count * player2.score)
    break
  
  player2.turn()
  dice_roll_count += 3
  if player1.is_winner:
    print(dice_roll_count, player1.score, player2.score, dice_roll_count * player1.score)
    break


# Part 2
# Using the same starting positions as in the example above, player 1 wins
# in 444356092776315 universes, while player 2 merely wins in 341960390180808
# universes.

# Big numbers! Maybe the space is too big for straight simulation. Try something
# mumble memoization mumble instead.


die = Die(3)
track = [1,2,3,4,5,6,7,8,9,10]

player1 = Player(1, player1_start, die, track, winning_score=21)
player2 = Player(2, player2_start, die, track, winning_score=21)

# CACHE = {}
@functools.cache
def quantum_roll(p1_pos, p1_score, p2_pos, p2_score):
  global track

  # count the number of wins for eah player and return as a tuple
  # so if there's a winner on this recursion, return a count for the winner

  if p1_score >= 21:
    return (1,0)
  
  if p2_score >= 21:
    return (0,1)

  # if (player1, player2) in CACHE:
  #   return CACHE[(player1, player2)]

  # if no one wins on this recursion, roll the quantum dice again

  winner_count = (0,0)
  # fan out 27 (3^3)
  for i in [1,2,3]:
    for j in [1,2,3]:
      for k in [1,2,3]:
        # one recursion == one turn, so only move one player each recursion,
        new_pos1 = ((p1_pos+i+j+k) % 10)
        new_score1 = p1_score + new_pos1 + 1

        # and swap the player order on the next recursion
        player2_win_count, player1_win_count = quantum_roll(p2_pos, p2_score, new_pos1, new_score1)
        winner_count = (winner_count[0] + player1_win_count, winner_count[1] + player2_win_count)

  # CACHE[(player1, player2)] = winner_count
  return winner_count

player1_win_total, player2_win_total = quantum_roll(player1.pos-1 , player1.score, player2.pos-1, player2.score)
print(player1_win_total, player2_win_total)
print(max([player1_win_total, player2_win_total]))