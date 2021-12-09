#!/usr/bin/env python3

import os
import random
from enum import Enum

class Opcode(Enum):
    HALT = 99
    ADD = 1
    MULTIPLY = 2

    
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
ints = [int(n) for n in file.read().split(',')]

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
