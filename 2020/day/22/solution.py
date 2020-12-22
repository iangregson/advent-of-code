#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict
from itertools import takewhile

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/example.txt", "r")
# file = open(dir_path + "/example2.txt", "r")
player1, player2 = file.read().strip().split('\n\n')

class Game():
  def __init__(self, deck_player1, deck_player2):
    self.deck_player1 = deck_player1
    self.deck_player2 = deck_player2

  def turn(self):
    if len(self.deck_player1) == 0:
      return 'Player 2'
    if len(self.deck_player2) == 0:
      return 'Player 1'

    card1 = self.deck_player1.pop(0)
    card2 = self.deck_player2.pop(0)

    if card1 > card2:
      # print('Player 1 wins', card1, card2)
      self.deck_player1.append(card1)
      self.deck_player1.append(card2)
    else:
      # print('Player 2 wins', card1, card2)
      self.deck_player2.append(card2)
      self.deck_player2.append(card1)

    return None

  def play(self):
    self.winner = None
    while self.winner == None:
      self.winner = game.turn()

  def final_score(self):
    scores = []
    if self.winner == 'Player 1':
      scores = self.deck_player1.copy()
    else:
      scores = self.deck_player2.copy()

    scores.reverse()

    for idx, score in enumerate(scores):
      scores[idx] = score * (idx + 1)

    return sum(scores)

deck_player1 = [int(x) for x in player1.split('\n')[1:]]
deck_player2 = [int(x) for x in player2.split('\n')[1:]]
game = Game(deck_player1, deck_player2)
game.play()

print('Part 1:', game.final_score())

def final_score(deck_winner):
  scores = deck_winner
  scores.reverse()

  for idx, score in enumerate(scores):
    scores[idx] = score * (idx + 1)

  return sum(scores)

def seen_configuration(deck_player1, deck_player2, previous_configurations):
  if (str(deck_player1) + str(deck_player2)) in previous_configurations:
    return True

def game_turn(deck_player1, deck_player2, previous_configurations = set()):
  # print(str(deck_player1) + str(deck_player2), previous_configurations)
  if seen_configuration(deck_player1, deck_player2, previous_configurations):
    # print('seen this configuration before!', str(deck_player1) + str(deck_player2), previous_configurations)
    return 'Player 1'

  if len(deck_player1) == 0:
    return 'Player 2'
  if len(deck_player2) == 0:
    return 'Player 1'

  previous_configurations.add(str(deck_player1) + str(deck_player2))

  # print('Player 1 deck', deck_player1)
  # print('Player 2 deck', deck_player2)

  card1 = deck_player1.pop(0)
  card2 = deck_player2.pop(0)
  
  # print('Player 1 plays', card1)
  # print('Player 2 plays', card2)

  round_winner = None
  if len(deck_player1) >= card1 and len(deck_player2) >= card2:
    # print('Playing a sub-game to determine the winner...')
    new_deck1 = deck_player1.copy()[:card1]
    new_deck2 = deck_player2.copy()[:card2]
    new_previous_configurations = set()

    while round_winner == None:
      round_winner = game_turn(new_deck1, new_deck2, new_previous_configurations)
  else:
    if card1 > card2:
      round_winner = 'Player 1'
    else:
      round_winner = 'Player 2'

  if round_winner == 'Player 1':
    # print('Player 1 wins')
    deck_player1.append(card1)
    deck_player1.append(card2)
  else:
    # print('Player 2 wins')
    deck_player2.append(card2)
    deck_player2.append(card1)

  return None

deck_player1 = [int(x) for x in player1.split('\n')[1:]]
deck_player2 = [int(x) for x in player2.split('\n')[1:]]

winner = None
previous_configurations = set()
while winner == None:
  # print('Round', count + 1)
  winner = game_turn(deck_player1, deck_player2, previous_configurations)
  # print()

score = None
if winner == 'Player 1':
  score = final_score(deck_player1)
else:
  score = final_score(deck_player2)

print('Part 2:', score)