#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
#   '',
#   '22 13 17 11  0',
#   ' 8  2 23  4 24',
#   '21  9 14 16  7',
#   ' 6 10  3 18  5',
#   ' 1 12 20 15 19',
#   '',
#   ' 3 15  0  2 22',
#   ' 9 18 13 17  5',
#   '19  8  7 25 23',
#   '20 11 10 24  4',
#   '14 21 16 12  6',
#   '',
#   '14 21 17 24  4',
#   '10 16 15  9 19',
#   '18  8 23 26 20',
#   '22 11 13  6  5',
#   ' 2  0 12  3  7',
# ]

numbers = [int(n) for n in lines[0].split(',')]
numbers_pt2 = [int(n) for n in lines[0].split(',')]
lines = lines[2:]

boards = []
while len(lines) != 0:
  board = [[int(n.strip()) for n in row.split()] for row in lines[0:5]]
  boards.append(board)
  lines = lines[6:]


def check_winner(draw, rows):
  cols = list(zip(*rows))
  winner = False
  # by row
  for i in range(5):
    winner = (len(set(draw).intersection(set(rows[i]))) == 5) or (len(set(draw).intersection(set(cols[i]))) == 5)
    if winner == True:
      break

  return winner

draw = []
winner = None
while len(numbers) != 0:
  draw.append(numbers.pop(0))
  for board in boards:
    if check_winner(draw, board) == True:
      winner = board

  if winner != None:
    break

# print(winner)

sum_winner = sum([sum([n for n in row if n not in draw]) for row in winner])
print(sum_winner * draw.pop())

numbers = numbers_pt2
draw = []
draws = []
winners = []
while len(numbers) != 0:
  draw.append(numbers.pop(0))
  for idx, board in enumerate(boards):
    if check_winner(draw, board) == True:
      winners.append(boards.pop(idx))
      draws.append(draw.copy())
      

last_winner = winners.pop()
draw_winner = draws.pop()
sum_winner = sum([sum([n for n in row if n not in draw_winner]) for row in last_winner])

print(sum_winner * draw_winner.pop())