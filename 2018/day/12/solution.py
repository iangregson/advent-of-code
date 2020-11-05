#!/usr/bin/env python3

import os
import math
import numpy
from collections import defaultdict, deque


dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]
# print(input_txt)

# input_txt = [
#   'initial state: #..#.#..##......###...###',
#   '',
#   '...## => #',
#   '..#.. => #',
#   '.#... => #',
#   '.#.#. => #',
#   '.#.## => #',
#   '.##.. => #',
#   '.#### => #',
#   '#.#.# => #',
#   '#.### => #',
#   '##.#. => #',
#   '##.## => #',
#   '###.. => #',
#   '###.# => #',
#   '####. => #',
# ]

state = input_txt[0].split('state: ').pop()
start_len = len(state)
# print(initial_state)

rules = {}
for rule in input_txt[2:]:
  rule, result = rule.split(' => ')
  rules[rule] = result


# print(0, state)
for t in range(20):
    state = '..'+state+'..'
    new_state = ['.' for _ in range(len(state))]
    read_state = '..'+state+'..'
    for i in range(len(state)):
        pat = read_state[i:i+5]
        new_state[i] = rules.get(pat, '.')

    state = ''.join(new_state)

    # print(t+1, state)

zero_idx = (len(state) - start_len) // 2
ans = 0
for i in range(len(state)):
    if state[i] == '#':
        ans += i-zero_idx
        # print(i-zero_idx, ans)
# print(state, len(state), start_len)

print("Part 1 answer:", ans)
