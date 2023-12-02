from dataclasses import dataclass
from enum import Enum
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
text = file.read_text()

# text = """
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """

class Color(Enum):
  RED = 'red'
  GREEN = 'green'
  BLUE = 'blue'


@dataclass
class Game():
  id: int
  turns: list[list[tuple[Color, int]]]

  def fewest_cubes(self) -> dict[Color, int]:
    totals = {
      Color.RED: 0,
      Color.GREEN: 0,
      Color.BLUE: 0,
    }
    for turn in self.turns:
      for color, count in turn:
        totals[color] = max(totals[color], count)
    return totals

  def check(self, totals: dict[Color, int]) -> bool:
    for turn in self.turns:
      for color, count in turn:
        if count > totals[color]:
          return False
    return True


lines = text.strip().split('\n')
games = []
for line in lines:
  id, turns = line.split(': ')
  id = int(id.split(' ')[-1])
  game = Game(id, [])
  turns = turns.split('; ')
  for turn in turns:
    t = []
    for round in turn.split(', '):
      count, color = round.split(' ')
      t.append((Color(color), int(count)))
    game.turns.append(t)

  games.append(game)
    

sum = 0
for game in games:
  if game.check({Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}):
    sum += game.id

print(sum)

# Part 2 ---------------------------------------------


from operator import mul
from functools import reduce

sum = 0
for game in games:
  power = reduce(mul, game.fewest_cubes().values())
  # print(game.fewest_cubes(), power)
  sum += power

print(sum)
