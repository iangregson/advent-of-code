#!/usr/bin/env python3

import os
from collections import defaultdict
import random
import difflib

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#   'abcdef',
#   'bababc',
#   'abbcde',
#   'abcccd',
#   'aabcdd',
#   'abcdee',
#   'ababab',
# ]

two_letter_count = 0
three_letter_count = 0

for line in input_txt:
  counts = defaultdict(int)
  for c in line:
    counts[c] += 1
  
  
  for letter, count in counts.items():
    if count == 2:
      two_letter_count += 1
      break
  
  for letter, count in counts.items():
    if count == 3:
      three_letter_count += 1
      break

print("Part 1 answer:", two_letter_count * three_letter_count)

# input_txt = [
#   'abcde',
#   'fghij',
#   'klmno',
#   'pqrst',
#   'fguij',
#   'axcye',
#   'wvxyz'
# ]


def count_changed_chars(s1, s2):
  count = 0
  for idx, c in enumerate(s1):
    if s2[idx] != c:
      count += 1
  return count

def remove_changed_chars(s1, s2):
  result = ''
  for idx, c in enumerate(s1):
    if s2[idx] == c:
      result += c
  return result
  
result = None

while True:
  s1, s2 = random.sample(input_txt, 2)
  if count_changed_chars(s1, s2) == 1:
    print(s1, s2)
    result = remove_changed_chars(s1, s2)
    break

  
  
print("Part 2 answer:", result)
