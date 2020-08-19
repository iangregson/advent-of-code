#!/usr/bin/env python3

import os
from collections import defaultdict
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#     'cpy 41 a',
#     'inc a',
#     'inc a',
#     'dec a',
#     'jnz a 2',
#     'dec a',
# ]

# print(input_txt)

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0
}

pos = 0
instructions = input_txt
while True:
    # print(registers['a'])
    if pos >= len(instructions):
        # print('out of bounds high!')
        break;
    elif pos < 0:
        # print('out of bounds low!')
        break;
    
    line = instructions[pos]

    if line.startswith('cpy'):
        _, x, y = line.split(' ')
        if x.isnumeric():
            registers[y] = int(x)
        else:
            registers[y] = registers[x]

    if line.startswith('inc'):
        _, x = line.split(' ')
        registers[x] += 1

    if line.startswith('dec'):
        _, x = line.split(' ')
        registers[x] -= 1

    if line.startswith('jnz'):
        _, x, y = line.split(' ')
        if x.isnumeric() and x != 0:
            pos += int(y)
            continue
        elif registers[x] != 0:
            pos += int(y)
            continue

    pos += 1



print("Part 1 answer:", registers['a'])

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

pos = 0
instructions = input_txt
while True:
    # print(registers['a'])
    if pos >= len(instructions):
        # print('out of bounds high!')
        break;
    elif pos < 0:
        # print('out of bounds low!')
        break;
    
    line = instructions[pos]

    if line.startswith('cpy'):
        _, x, y = line.split(' ')
        if x.isnumeric():
            registers[y] = int(x)
        else:
            registers[y] = registers[x]

    if line.startswith('inc'):
        _, x = line.split(' ')
        registers[x] += 1

    if line.startswith('dec'):
        _, x = line.split(' ')
        registers[x] -= 1

    if line.startswith('jnz'):
        _, x, y = line.split(' ')
        if x.isnumeric() and x != 0:
            pos += int(y)
            continue
        elif registers[x] != 0:
            pos += int(y)
            continue

    pos += 1

print("Part 2 answer:", registers['a'])
