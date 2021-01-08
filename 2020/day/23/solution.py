#!/usr/bin/env python3

import os
from collections import deque

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()
# input_txt = '389125467'

cups = [int(x) for x in list(input_txt)]

N_MOVES = 100

q = deque(cups)

def next_state(q):
  # Before the crab starts, it will designate the first cup in your list as
  # the current cup.
  # print('cups:', q)
  current_cup = q.popleft()
  # print('current_cup:', current_cup)

  # The crab picks up the three cups that are immediately clockwise of the
  # current cup. They are removed from the circle; cup spacing is adjusted
  # as necessary to maintain the circle.
  c1 = q.popleft()
  c2 = q.popleft()
  c3 = q.popleft()
  removed_cups = [c1, c2, c3]
  q.appendleft(current_cup)
  # print('pick up:', removed_cups)

  # The crab selects a destination cup: the cup with a label equal to the
  # current cup's label minus one. If this would select one of the cups
  # that was just picked up, the crab will keep subtracting one until it
  # finds a cup that wasn't just picked up. If at any point in this process
  # the value goes below the lowest value on any cup's label, it wraps around
  # to the highest value on any cup's label instead.
  label = current_cup - 1
  if label < min(list(q)):
    label = max(list(q))
  while label in removed_cups:
    label -= 1
    if label < min(list(q)):
      label = max(list(q))
  destination_cup = q.index(label)
  # print('destination:', list(q)[destination_cup])

  # The crab places the cups it just picked up so that they are immediately
  # clockwise of the destination cup. They keep the same order as when they
  # were picked up.
  q.rotate(-(destination_cup+1))
  removed_cups.reverse()
  [q.appendleft(cup) for cup in removed_cups]
  
  # The crab selects a new current cup: the cup which is immediately
  # clockwise of the current cup.
  current_cup_pos = q.index(current_cup)
  q.rotate(-current_cup_pos)
  q.rotate(-1)

  return q

for move in range(1, N_MOVES + 1):
  # print('\n-- move {} --'.format(move))
  q = next_state(q)

# print('\n-- final --')
# print('cups: ', q)
# print()

idx = q.index(1)
q.rotate(-idx)
print('Part 1:', "".join([str(cup) for cup in list(q)][1:]))
