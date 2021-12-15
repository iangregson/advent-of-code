#!/usr/bin/env python3

import re
from enum import Enum
from collections import namedtuple

class Opcode(Enum):
    HALT = 99
    ADD = 1
    MULTIPLY = 2

class IntCodeComputer():
  def __init__(self, program):
    self.program = program
    self.head = 0

  @property
  def opcode(self):
    return Opcode(self.program[self.head])

  def run(self, program = None):
    if program != None:
      self.program = program

    while self.opcode != Opcode.HALT:
      # print(self.opcode)
      if self.opcode == Opcode.ADD:
        a, b = self.read()
        self.write(a + b)
      elif self.opcode == Opcode.MULTIPLY:
        a, b = self.read()
        self.write(a * b)
      else:
        raise Exception()
      
      self.step()

  def step(self):
    self.head += 4
  
  def read(self):
    pos_1 = self.program[self.head + 1]
    pos_2 = self.program[self.head + 2]
    return self.program[pos_1], self.program[pos_2]
  
  def write(self, value):
    pos = self.program[self.head + 3]
    self.program[pos] = value

pw_range = '193651-649729'

pw_range = range(*[int(n) for n in pw_range.split('-')])


# rules
# Two adjacent digits are the same (like 22 in 122345).
def has_duplicate_adjacent(n):
  m = re.search(r'(\d)\1+', str(n))
  return m is not None

# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
def never_decreases(n):
  digits = [int(x) for x in list(str(n))]
  # print(digits)
  result = True
  for idx, d in enumerate(digits):
    if idx == 0:
      continue
    if d < digits[idx-1]:
      result = False
      break
  return result

n_passwords = 0
for i in pw_range:
  if has_duplicate_adjacent(i) and never_decreases(i):
    n_passwords += 1

print(n_passwords)

def duplicate_adjacent_repeats(n):
  str_n = str(n)
  matches = re.findall(r'(\d)\1+', str_n)
  return 2 in [str_n.count(x) for x in matches]

# print(duplicate_adjacent_repeats(112233))
# print(duplicate_adjacent_repeats(123444))
# print(duplicate_adjacent_repeats(111122))

n_passwords = 0
for i in pw_range:
  if not has_duplicate_adjacent(i):
    continue
  if not duplicate_adjacent_repeats(i):
    continue
  if not never_decreases(i):
    continue
  n_passwords += 1

print(n_passwords)

