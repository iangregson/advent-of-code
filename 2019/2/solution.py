#!/usr/bin/env python3

import os
from enum import Enum

# class Opcode(Enum):
#     HALT = 99
#     ADD = 1
#     MULTIPLY = 2

# class IntCodeComputer():
#   def __init__(self, program):
#     self.program = program
#     self.head = 0

#   @property
#   def opcode(self):
#     return Opcode(self.program[self.head])

#   def run(self, program = None):
#     if program != None:
#       self.program = program

#     while self.opcode != Opcode.HALT:
#       # print(self.opcode)
#       if self.opcode == Opcode.ADD:
#         a, b = self.read(2)
#         self.write(a + b)
#       elif self.opcode == Opcode.MULTIPLY:
#         a, b = self.read()
#         self.write(a * b)
#       else:
#         raise Exception()
      
#       self.step(4)

#   def step(self, n):
#     self.head += n
  
#   def read(self, n_params=2):
#     positions = self.program[self.head + 1:self.head + n_params + 1]
#     return [self.program[p] for p in positions]
  
#   def write(self, value, look_ahead=3):
#     pos = self.program[self.head + look_ahead]
#     self.program[pos] = value


class Opcode(Enum):
    HALT = 99
    ADD = 1
    MULTIPLY = 2
    STORE = 3
    RETRIEVE = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8

class IntCodeComputer():
  def __init__(self, program):
    self.program = program
    self.head = 0

  @property
  def opcode(self):
    return Opcode(self.program[self.head])
  
  @property
  def step_sise(self):
    return 4

  def run(self, input=None):
    self.input = input
    self.output = None

    while self.opcode != Opcode.HALT:
      # print(self.opcode)
      if self.opcode == Opcode.ADD:
        self.add()
      elif self.opcode == Opcode.MULTIPLY:
        self.multiply()
      elif self.opcode == Opcode.STORE:
        self.store()
      elif self.opcode == Opcode.RETRIEVE:
        a = self.read(1)
        self.output = self.program[a]
        self.step(2)
      else:
        raise Exception('Unkown Opcode')
  
  def store(self):
    parameter = self.program[self.head + 1]
    input = self.input
    self.program[parameter] = input
    self.head += 2
  
  def retrieve(self):
    parameter = self.program[self.head + 1]
    self.output = self.program[parameter]
    self.head += 2
  
  def add(self):
    param_a = self.program[self.head + 1]
    param_b = self.program[self.head + 2]
    param_c = self.program[self.head + 3]
    a = self.program[param_a]
    b = self.program[param_b]
    self.program[param_c] = a + b
    self.head += 4
  
  def multiply(self):
    param_a = self.program[self.head + 1]
    param_b = self.program[self.head + 2]
    param_c = self.program[self.head + 3]
    a = self.program[param_a]
    b = self.program[param_b]
    self.program[param_c] = a * b
    self.head += 4
  
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
ints = [int(n) for n in file.read().split(',')]

program = ints[:]
program[1] = 12
program[2] = 2
computer = IntCodeComputer(program)
computer.run()
print(program[0])

for i in range(100):
  for j in range(100):
    program = ints[:]
    verb = j
    noun = i
    program[1] = noun
    program[2] = verb
    computer = IntCodeComputer(program)
    try:
      computer.run()
    except Exception:
      pass
    if program[0] == 19690720:
      print(100 * noun + verb)
      break
