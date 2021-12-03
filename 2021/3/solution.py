#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '00100',
#   '11110',
#   '10110',
#   '10111',
#   '10101',
#   '01111',
#   '00111',
#   '11100',
#   '10000',
#   '11001',
#   '00010',
#   '01010',
# ]

# print(lines)

gamma = ""
epsilon = ""

for column in range(len(lines[0])):
  col = "".join(list(map(lambda x: x[column], lines)))
  zero_count = col.count('0')
  bit_count = col.count('1')
  if bit_count > zero_count:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'


print(int(gamma, 2) * int(epsilon, 2))

# lines = [
#   '00100',
#   '11110',
#   '10110',
#   '10111',
#   '10101',
#   '01111',
#   '00111',
#   '11100',
#   '10000',
#   '11001',
#   '00010',
#   '01010',
# ]

numbers = lines[:]
bit_pos = 0

while len(numbers) != 1:
  col = "".join(list(map(lambda x: x[bit_pos], numbers)))
  zero_count = col.count('0')
  bit_count = col.count('1')
  if bit_count >= zero_count:
    numbers = list(filter(lambda x: x[bit_pos] == '1', numbers))
  else:
    numbers = list(filter(lambda x: x[bit_pos] == '0', numbers))
  bit_pos += 1

oxygen_generator = int(numbers[0], 2)

numbers = lines[:]
bit_pos = 0

while len(numbers) != 1:
  col = "".join(list(map(lambda x: x[bit_pos], numbers)))
  zero_count = col.count('0')
  bit_count = col.count('1')
  if zero_count <= bit_count:
    numbers = list(filter(lambda x: x[bit_pos] == '0', numbers))
  else:
    numbers = list(filter(lambda x: x[bit_pos] == '1', numbers))
  bit_pos += 1

c02_scrubber = int(numbers[0], 2)

print(oxygen_generator * c02_scrubber)
