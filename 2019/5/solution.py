#!/usr/bin/env python3

import os
from enum import Enum

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

class ParameterMode(Enum):
  POSITION_MODE = 0
  IMMEDIATE_MODE = 1

class IntCodeComputer():
  def __init__(self, program):
    self.program = program
    self.head = 0

  @staticmethod
  def parse_opcode(value):
    digits = str(value)
    while len(digits) < 5:
      digits = '0' + digits
    opcode = int(digits[-2:])
    parameter_modes = [int(x) for x in list(digits[:3])]
    parameter_modes.reverse()
    return opcode, parameter_modes

  @property
  def opcode(self):
    opcode_value = self.program[self.head]
    opcode, _ = IntCodeComputer.parse_opcode(opcode_value)
    return Opcode(opcode)
  
  def parameter_mode(self, n_parameter):
    opcode_value = self.program[self.head]
    _, parameter_modes = IntCodeComputer.parse_opcode(opcode_value)
    return ParameterMode(parameter_modes[n_parameter-1])
  
  def read_parameter(self, n_parameter):
    param = self.program[self.head + n_parameter]
    
    if n_parameter == 3:
      return param
    
    param_mode = self.parameter_mode(n_parameter)
    if param_mode == ParameterMode.POSITION_MODE:
      return self.program[param]
    elif param_mode == ParameterMode.IMMEDIATE_MODE:
      return param
  
  @property
  def step_sise(self):
    return 4

  def run(self, input=None):
    self.input = input
    self.output = 0

    while self.opcode != Opcode.HALT:
      # print(self.opcode)
      # print(self.head)
      # print(self.program[self.head])
      if self.opcode == Opcode.ADD:
        self.add()
      elif self.opcode == Opcode.MULTIPLY:
        self.multiply()
      elif self.opcode == Opcode.STORE:
        self.store()
      elif self.opcode == Opcode.RETRIEVE:
        self.retrieve()
      elif self.opcode == Opcode.JUMP_IF_TRUE:
        self.jump_if_true()
      elif self.opcode == Opcode.JUMP_IF_FALSE:
        self.jump_if_false()
      elif self.opcode == Opcode.LESS_THAN:
        self.less_than()
      elif self.opcode == Opcode.EQUALS:
        self.equals()
      else:
        raise Exception('Unkown Opcode')
  
  def store(self):
    parameter = self.program[self.head + 1]
    input = self.input
    self.program[parameter] = input
    
    if parameter != self.head:
      self.head += 2
  
  def retrieve(self):
    parameter = self.program[self.head + 1]
    
    if self.parameter_mode(1) == ParameterMode.IMMEDIATE_MODE:
      self.output = parameter
    else:
      self.output = self.program[parameter]
    
    self.head += 2
  
  def add(self):
    a = self.read_parameter(1)
    b = self.read_parameter(2)
    c = self.read_parameter(3)
    
    self.program[c] = a + b
    
    if c != self.head:
      self.head += 4
  
  def multiply(self):
    a = self.read_parameter(1)
    b = self.read_parameter(2)
    c = self.read_parameter(3)
    
    self.program[c] = a * b
    
    if c != self.head:
      self.head += 4
  
  def jump_if_true(self):
    a = self.read_parameter(1)
    b = self.read_parameter(2)

    if a != 0:
      self.head = b
    else:
      self.head += 3
  
  def jump_if_false(self):
    a = self.read_parameter(1)
    b = self.read_parameter(2)
    
    if a == 0:
      self.head = b
    else:
      self.head += 3
  
  def less_than(self):
    a = self.read_parameter(1)
    b = self.read_parameter(2)
    c = self.read_parameter(3)
    
    if a < b:
      self.program[c] = 1
    else:
      self.program[c] = 0
    
    if c != self.head:
      self.head += 4
  
  def equals(self):
    a = self.read_parameter(1)
    b = self.read_parameter(2)
    c = self.read_parameter(3)
    
    if a == b:
      self.program[c] = 1
    else:
      self.program[c] = 0
    
    if c != self.head:
      self.head += 4

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
ints = [int(n) for n in file.read().split(',')]

program = ints[:]
computer = IntCodeComputer(program)
computer.run(input=1)
print(computer.output)

# # tests
# print('\ntests\n')

# program = [3,9,8,9,10,9,4,9,99,-1,8]
# computer = IntCodeComputer(program)
# computer.run(input=8)
# print(computer.output)
# computer.run(input=9)
# print(computer.output)

# program = [3,9,7,9,10,9,4,9,99,-1,8]
# computer = IntCodeComputer(program)
# computer.run(input=7)
# print(computer.output)
# computer.run(input=9)
# print(computer.output)

# program = [3,3,1108,-1,8,3,4,3,99]
# computer = IntCodeComputer(program)
# computer.run(input=8)
# print(computer.output)
# computer.run(input=9)
# print(computer.output)

# program = [3,3,1107,-1,8,3,4,3,99]
# computer = IntCodeComputer(program)
# computer.run(input=7)
# print(computer.output)
# computer.run(input=9)
# print(computer.output)

# # jump tests
# print('\njump tests\n')

# program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# computer = IntCodeComputer(program)
# computer.run(input=0)
# print(computer.output)

# program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# computer = IntCodeComputer(program)
# computer.run(input=1)
# print(computer.output)

# program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
# computer = IntCodeComputer(program)
# computer.run(input=-1)
# print(computer.output)

# # jump tests
# print('\nlong tests\n')

# program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# computer = IntCodeComputer(program)
# computer.run(input=6)
# print(computer.output)
# program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# computer = IntCodeComputer(program)
# computer.run(input=8)
# print(computer.output)
# program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
# computer = IntCodeComputer(program)
# computer.run(input=10)
# print(computer.output)

program = ints[:]
computer = IntCodeComputer(program)
computer.run(input=5)
print(computer.output)