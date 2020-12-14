#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
#   'mem[8] = 11',
#   'mem[7] = 101',
#   'mem[8] = 0',
# ]

I = namedtuple('I', ['cmd', 'address', 'value'])

def parse(line):
  l, r = line.split(' = ')

  if l.startswith('mask'):
    return I('mask', None, r)
  elif l.startswith('mem'):
    cmd, address = l.split('[')
    address = int(address[:-1])
    return I(cmd, address, int(r))

def decimal_to_bin(number):
  return bin(number)[2:].zfill(36)

def apply_mask(number, mask):
  binary_rep_number = decimal_to_bin(number)
  new_binary_rep_number = []

  for idx, char in enumerate(mask):
    if char == 'X':
      new_binary_rep_number.append(binary_rep_number[idx])
    else:
      new_binary_rep_number.append(mask[idx])

  return int("".join(new_binary_rep_number), 2)

program = [parse(line) for line in lines]

mask = None
mem = defaultdict(str)

for instruction in program:
  if instruction.cmd == 'mask':
    mask = instruction.value
  elif instruction.cmd == 'mem':
    mem[instruction.address] = apply_mask(instruction.value, mask)

print('Part 1:', sum(mem.values()))

# lines = [
#   'mask = 000000000000000000000000000000X1001X',
#   'mem[42] = 100',
#   'mask = 00000000000000000000000000000000X0XX',
#   'mem[26] = 1',
# ]

def apply_mask_pt2(number, mask):
  binary_rep_number = decimal_to_bin(number)
  new_binary_rep_number = []

  for idx, char in enumerate(mask):
    if char == 'X':
      new_binary_rep_number.append(char)
    elif char == '0':
      new_binary_rep_number.append(binary_rep_number[idx])
    elif char == '1':
      new_binary_rep_number.append(char)

  numbers = [new_binary_rep_number]
  working_idx = 0
  while any([True if 'X' in n else False for n in numbers]):
    n = numbers[working_idx]
    for idx, char in enumerate(n):
      if char == 'X':
        nn = n.copy()
        nn[idx] = '1'
        n[idx] = '0'
        numbers.append(nn)
    working_idx += 1
    if working_idx >= len(numbers):
      break


  # return numbers
  return [int("".join(n), 2) for n in numbers]

program = [parse(line) for line in lines]

mask = None
mem = defaultdict(str)

for instruction in program:
  if instruction.cmd == 'mask':
    mask = instruction.value
  elif instruction.cmd == 'mem':
    addresses = apply_mask_pt2(instruction.address, mask)
    for address in addresses:
      mem[address] = instruction.value

print('Part 2:', sum(mem.values()))