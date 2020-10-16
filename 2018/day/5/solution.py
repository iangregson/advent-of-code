#!/usr/bin/env python3

import os
import math
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read()

# input_txt = 'aA'
# input_txt = 'abBA'
# input_txt = 'abAB'
# input_txt = 'aabAAB'
# input_txt = 'dabAcCaCBAcCcaDA'


S = input_txt

def react(S):
  i = 0
  j = 1
  while j < len(S):
    I = S[i]
    J = S[j]
    # print(S, i, j, I, J)

    if I.isupper() and J == I.lower():
      S = S[:i] + S[j+1:]
      i = 0
      j = 1
      continue

    if I.islower() and J == I.upper():
      S = S[:i] + S[j+1:]
      i = 0
      j = 1
      continue

    i += 1
    j += 1

  return S

# print('S = ', S)
# print('len(S) = ', len(S))
S = react(S)

print("Part 1 answer:", len(S))

most_common = Counter(input_txt.upper()).most_common()
# print(most_common)

shortest = math.inf

for common in most_common:
  S = input_txt
  char, count = common
  S = S.replace(char, '')
  S = S.replace(char.lower(), '')
  S = react(S)

  if len(S) < shortest:
    shortest = len(S)
  else:
    break

print("Part 2 answer:", shortest)