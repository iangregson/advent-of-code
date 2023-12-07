from collections import Counter 
from operator import mul
from functools import reduce
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
text = file.read_text()

hands = [tuple(line.split(' ')) for line in text.split('\n')]

card_rank = {
  'A': 14, 
  'K': 13,
  'Q': 12,
  'J': 11,
  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2
}
hand_rank = {
  'Five of a kind': 7, # where all five cards have the same label: AAAAA
  'Four of a kind': 6, # where four cards have the same label and one card has a different label: AA8AA
  'Full house': 5, # where three cards have the same label, and the remaining two cards share a different label: 23332
  'Three of a kind': 4, # where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
  'Two pair': 3, # where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
  'One pair': 2, # where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
  'High card': 1, # where all cards' labels are distinct: 23456
}

def rank_cards(hand: str, card_ranks: dict[str, int]) -> str:
  # get an ordered list of cards as string to leverage
  # lexical sort
  ranks = ""
  for card in hand:
    i = card_ranks[card]
    ranks += chr(76 + i)

  return ranks

def rank_hand(hand: str, hand_rank: dict[str, int]) -> int:
  count = Counter(hand)
  cv = list(sorted(count.values()))
  if 5 in cv:
    return hand_rank['Five of a kind']
  elif 4 in cv:
    return hand_rank['Four of a kind']
  elif cv == [2,3]:
    return hand_rank['Full house']
  elif 3 in cv:
    return hand_rank['Three of a kind']
  elif cv == [1,2,2]:
    return hand_rank['Two pair']
  elif cv == [1,1,1,2]:
    return hand_rank['One pair']
  elif len(cv) == 5:
    return hand_rank['High card']

  return 0

ranked_hands = [] # (hand rank, first card rank, hand, bid)
for (hand, bid) in hands:
  first_card_rank = rank_cards(hand, card_rank)
  hand_ranked = rank_hand(hand, hand_rank)
  ranked_hands.append((hand_ranked, first_card_rank, hand, int(bid)))

ranked_hands = sorted(ranked_hands, key=lambda x: (x[0], x[1]))

result = 0
for i in range(1, len(ranked_hands) + 1):
  rank, card_rank, hand, bid = ranked_hands[i-1]
  result += bid * i

print(result)


# Part 2 -----------------------------------------------

card_rank_joker = {
  'A': 14, 
  'K': 13,
  'Q': 12,
  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2,
  'J': 1,
}

def make_strongest(hand: str) -> str:
  count = Counter(hand)
  
  # find the highest group that's not J
  strongest_card = list(count.keys())[0]
  for card in count:
    if card == 'J':
      continue
    if count[card] > count[strongest_card] or strongest_card == 'J':
      strongest_card = card
    
  # and replace J with that card
  hand = hand.replace('J', strongest_card)
  return hand

ranked_hands = [] # (hand rank, first card rank, hand, bid)
for (hand, bid) in hands:
  first_card_rank = rank_cards(hand, card_rank_joker)
  if 'J' in hand:
    hand = make_strongest(hand)
  hand_ranked = rank_hand(hand, hand_rank)
  ranked_hands.append((hand_ranked, first_card_rank, hand, int(bid)))

ranked_hands = sorted(ranked_hands, key=lambda x: (x[0], x[1]))

result = 0
for i in range(1, len(ranked_hands) + 1):
  hand_rank, card_rank, hand, bid = ranked_hands[i-1]
  result += bid * i

print(result)
