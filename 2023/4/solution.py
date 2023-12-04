from collections import defaultdict
import re
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
text = file.read_text()

# text = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """

lines = text.strip().split('\n')
cards: dict[int, tuple[list[int], list[int]], int] = defaultdict(tuple[list[int], list[int], int])
for line in lines:
  card_id, scores = line.split(': ')
  card_id = int(card_id.strip().split(' ')[-1])
  winners, numbers = scores.split(' | ')
  winners = [int(n) for n in re.findall(r'\d+', winners)]
  numbers = [int(n) for n in re.findall(r'\d+', numbers)]
  cards[card_id] = (winners, numbers, 1)

# print(cards)

points = 0
for winners, numbers, count in cards.values():
  matches = set(winners).intersection(set(numbers))
  score = 0
  if len(matches) == 1:
    score = 1
  elif len(matches) == 2:
    score = 2
  elif len(matches) > 2:
    score = 2**(len(matches)-1)
  points += score

print(points)


# Part 2 ---------------------------------------------

for card_id, (winners, numbers, count) in cards.items():
  matches = set(winners).intersection(set(numbers))
  for i in range(card_id+1, card_id+len(matches)+1):
    w,n,c = cards[i]
    c += count
    cards[i] = (w,n,c)
  
total_cards = sum([c for w,n,c in cards.values()])
print(total_cards)