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

def parse(cups):
    start_cup = cups[0]
    successors = [0] * (len(cups) + 1)

    for i in range(len(cups) - 1):
        successors[cups[i]] = cups[i + 1]
    successors[cups[-1]] = start_cup

    return start_cup, successors

def move(current_cup, succ):
    p0 = succ[current_cup]
    p1 = succ[p0]
    p2 = succ[p1]
    nextCup = succ[p2]

    destCup = current_cup - 1
    while True:
        if destCup < 1:
            destCup = max(succ)
        if destCup not in (p0, p1, p2):
            break
        destCup = destCup - 1

    succ[current_cup] = nextCup
    succ[p2] = succ[destCup]
    succ[destCup] = p0
    return nextCup


current_cup, successors = parse(cups)
ms = max(successors)
successors.extend(range(ms + 2, 1000000 + 2))
successors[cups[-1]] = ms + 1
successors[1000000] = cups[0]

for _ in range(10000000):
    current_cup = move(current_cup, successors)

result = successors[1] * successors[successors[1]]

print('Part 2:', result)
