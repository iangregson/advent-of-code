#!/usr/bin/env python3

import os
import statistics

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '[({(<(())[]>[[{[]{<()<>>',
#   '[(()[<>])]({[<{<<[]>>(',
#   '{([(<{}[<>[]}>{[]{[(<()>',
#   '(((({<>}<{<{<>}{[]{[]{}',
#   '[[<[([]))<([[{}[[()]]]',
#   '[{[{({}]{}}([{[{{{}}([]',
#   '{<[[]]>}<{[{[{[]{()[[[]',
#   '[<(<(<(<{}))><([]([]()',
#   '<{([([[(<>()){}]>(<<{{',
#   '<{([{{}}[<[[[<>{}]]]>[]]'
# ]

valid_open_chunk = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<',
}
valid_close_chunk = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}
illegal_score_map = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}
scores = {
  ')': 0,
  ']': 0,
  '}': 0,
  '>': 0,
}

corrupt = []
for line in lines:
  stack = []
  tokens = list(line)
  for t in tokens:
    if t in ['(','[','{','<']:
      stack.append(t)
      continue
    elif t in [')',']','}','>']:
      open_chunk = stack.pop()
      if open_chunk != valid_open_chunk[t]:
        corrupt.append(line)
        break

# print(len(corrupt))

for line in corrupt:
  stack = []
  tokens = list(line)
  for t in tokens:
    if t in ['(','[','{','<']:
      stack.append(t)
      continue
    elif t in [')',']','}','>']:
      open_chunk = stack.pop()
      if open_chunk != valid_open_chunk[t]:
        scores[t] += illegal_score_map[t]

print(sum(scores.values()))


corrupt = []
for idx, line in enumerate(lines):
  stack = []
  tokens = list(line)
  for t in tokens:
    if t in ['(','[','{','<']:
      stack.append(t)
      continue
    elif t in [')',']','}','>']:
      open_chunk = stack.pop()
      if open_chunk != valid_open_chunk[t]:
        corrupt.append(line)
        break

# print(len(corrupt))
lines = [l for l in lines if l not in corrupt]
# print(len(lines))

line_completions = []
for idx, line in enumerate(lines):
  stack = []
  tokens = list(line)
  for t in tokens:
    if t in ['(','[','{','<']:
      stack.append(t)
      continue
    elif t in [')',']','}','>']:
      open_chunk = stack.pop()
  line_completion = []
  while len(stack):
    t = stack.pop()
    line_completion.append(valid_close_chunk[t])
  line_completions.append(line_completion)

incomplete_score_map = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}
line_scores = []
for line in line_completions:
  score = 0
  for t in line:
    score = (score * 5) + incomplete_score_map[t]
  line_scores.append(score)

print(statistics.median(line_scores))