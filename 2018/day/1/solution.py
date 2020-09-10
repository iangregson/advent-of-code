#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#   '+3',
#   '+3',
#   '+4',
#   '-2',
#   '-4'
# ]

numbers = [int(n) for n in input_txt]

print("Part 1 answer:", sum(numbers))


count_freq = defaultdict(int)
freq = 0
freq_seen_twice = None
while not freq_seen_twice:
  for n in numbers:
    freq += n
    count_freq[freq] += 1

    if count_freq[freq] == 2:
      freq_seen_twice = freq
      break
  

print("Part 2 answer:", freq_seen_twice)
