#!/usr/bin/env python3

import os
import random
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
input_txt = [line.strip() for line in file.readlines()]
# input_txt = ['5764801', '17807724']
# print(input_txt)

MAX_ITERATIONS = 100000000
MODULUS = 20201227
MAGIC_NUMBER = 7

def find_loop_size(public_key, max_iterations = MAX_ITERATIONS):
  loop_size = None
  value = 1
  counter = 0
  while not loop_size and counter < max_iterations:
    counter += 1
    value = (value * MAGIC_NUMBER) % MODULUS
    if value == public_key:
      loop_size = counter

  return loop_size

card_public_key, door_public_key = [int(x) for x in input_txt]
card_loop_size = find_loop_size(card_public_key)

encryption_key = None

if card_loop_size == None:
  print('Could not find card loop size')
else:
  encryption_key = pow(door_public_key, card_loop_size, MODULUS)

print('Part 1:', encryption_key)