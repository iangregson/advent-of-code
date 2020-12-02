#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# print(lines)

# lines = [
#   '1-3 a: abcde',
#   '1-3 b: cdefg',
#   '2-9 c: ccccccccc',
# ]

def parse_line(line):
  limit_str, char, pw = line.split(' ')
  char = char[:-1]
  limit_low = int(limit_str.split('-')[0])
  limit_high = int(limit_str.split('-')[-1])
  return limit_low, limit_high, char, pw

valid_pws = []

for line in lines:
  limit_low, limit_high, char, pw = parse_line(line)
  if pw.count(char) in list(range(limit_low, limit_high + 1)):
    valid_pws.append(pw)
 

print('Part 1:', len(valid_pws))


valid_pws = []
invalid_pws = []

for line in lines:
  pos_1, pos_2, char, pw = parse_line(line)
  if pw[pos_1 - 1] == char and pw[pos_2 - 1] == char:
    invalid_pws.append(pw)
  if pw[pos_1 - 1] != char and pw[pos_2 - 1] != char:
    invalid_pws.append(pw)
  if pw[pos_1 - 1] == char and pw[pos_2 - 1] != char:
    valid_pws.append(pw)
  if pw[pos_1 - 1] != char and pw[pos_2 - 1] == char:
    valid_pws.append(pw)

print('Part 2:', len(valid_pws))