#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = ['0,3,6']
# lines = ['1,3,2']
# lines = ['2,1,3']
# lines = ['1,2,3']
# lines = ['2,3,1']
# lines = ['3,2,1']
# lines = ['3,1,2']

numbers = [int(x) for x in lines[0].split(',')]

# print(numbers)

mem = defaultdict(list)

prev_number = None
for i in range(0, 2020):
  if i < len(numbers):
    prev_number = numbers[i]
    mem[prev_number].append(i)
  else:
    if len(mem[prev_number]) == 1:
      prev_number = 0
      mem[prev_number].append(i)
    else:
      prev_number = mem[prev_number][-1] - mem[prev_number][-2]
      mem[prev_number].append(i)

print('Part 1:', prev_number)

mem = defaultdict(list)

prev_number = None
for i in range(0, 30000000):
  if i < len(numbers):
    prev_number = numbers[i]
    mem[prev_number].append(i)
  else:
    if len(mem[prev_number]) == 1:
      prev_number = 0
      mem[prev_number].append(i)
    else:
      prev_number = mem[prev_number][-1] - mem[prev_number][-2]
      mem[prev_number].append(i)
  
  if len(mem[prev_number]) > 2:
    mem[prev_number] = mem[prev_number][-2:]

print('Part 2:', prev_number)




