#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'forward 5',
#   'down 5',
#   'forward 8',
#   'up 3',
#   'down 8',
#   'forward 2',
# ]

depth = 0
horizontal = 0

for line in lines:
  direction, amount = line.split()
  amount = int(amount)

  if direction == 'forward':
    horizontal += amount
  elif direction == 'up':
    depth -= amount
  elif direction == 'down':
    depth += amount

print(depth * horizontal)

# lines = [
#   'forward 5',
#   'down 5',
#   'forward 8',
#   'up 3',
#   'down 8',
#   'forward 2',
# ]

depth = 0
horizontal = 0
aim = 0

for line in lines:
  direction, amount = line.split()
  amount = int(amount)

  if direction == 'forward':
    horizontal += amount
    depth += aim * amount
  elif direction == 'up':
    aim -= amount
  elif direction == 'down':
    aim += amount

print(depth * horizontal)