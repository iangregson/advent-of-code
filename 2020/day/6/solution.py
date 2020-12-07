#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'abc',
#   '',
#   'a',
#   'b',
#   'c',
#   '',
#   'ab',
#   'ac',
#   '',
#   'a',
#   'a',
#   'a',
#   'a',
#   '',
#   'b',
# ]

questions_answered_by_group = set()
total = 0

for line in lines:
  if line == '':
    total += len(questions_answered_by_group)
    questions_answered_by_group = set()
  else:
    for char in line:
      questions_answered_by_group.add(char)
total += len(questions_answered_by_group)

print('Part 1:', total)

groups = []
curr_group = []
for line in lines:
  if line == '':
    groups.append(curr_group)
    curr_group = []
  else:
    curr_group.append(line)
groups.append(curr_group)

# print(groups)
total_score = 0
for group in groups:
  n_members = len(group)
  all_members = "".join(group)
  uniq_chars = set(list(all_members))
  score = 0

  for char in uniq_chars:
    if all_members.count(char) == n_members:
      score += 1

  # print(n_members, all_members, uniq_chars, score)
  total_score += score

print('Part 2:', total_score)