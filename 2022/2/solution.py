from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class RockPaperScissors():
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

  LOSE = 0
  DRAW = 3
  WIN = 6

  d = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
  }
  
  d2 = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 0,
    'Y': 3,
    'Z': 6,
  }

  def __init__(self) -> None:
    pass

  def score_game(self, game):
    player2, player1 = game
    player2, player1 = self.d[player2], self.d[player1]

    if player1 == self.ROCK:
      if player2 == self.ROCK:
        return player1 + self.DRAW
      elif player2 == self.SCISSORS:
        return player1 + self.WIN
      elif player2 == self.PAPER:
        return player1 + self.LOSE
    
    if player1 == self.PAPER:
      if player2 == self.ROCK:
        return player1 + self.WIN
      elif player2 == self.SCISSORS:
        return player1 + self.LOSE
      elif player2 == self.PAPER:
        return player1 + self.DRAW
    
    if player1 == self.SCISSORS:
      if player2 == self.ROCK:
        return player1 + self.LOSE
      elif player2 == self.SCISSORS:
        return player1 + self.DRAW
      elif player2 == self.PAPER:
        return player1 + self.WIN

  def score_game_pt2(self, game):
    player2, end_state = game
    player2, end_state = self.d2[player2], self.d2[end_state]
    
    if end_state == self.WIN:
      if player2 == self.ROCK:
        return end_state + self.PAPER
      elif player2 == self.PAPER:
        return end_state + self.SCISSORS
      elif player2 == self.SCISSORS:
        return end_state + self.ROCK
    
    if end_state == self.LOSE:
      if player2 == self.ROCK:
        return end_state + self.SCISSORS
      elif player2 == self.PAPER:
        return end_state + self.ROCK
      elif player2 == self.SCISSORS:
        return end_state + self.PAPER
    
    if end_state == self.DRAW:
      if player2 == self.ROCK:
        return end_state + self.ROCK
      elif player2 == self.PAPER:
        return end_state + self.PAPER
      elif player2 == self.SCISSORS:
        return end_state + self.SCISSORS


Game = RockPaperScissors()
games = [tuple(line.split()) for line in text]

print("Part 1:", sum([Game.score_game(g) for g in games]))
print("Part 2:", sum([Game.score_game_pt2(g) for g in games]))
