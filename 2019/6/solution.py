#!/usr/bin/env python3

import os
import sys
from enum import Enum
from collections import defaultdict
from functools import cache

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
lines = [line.strip() for line in file.readlines()]

# lines = [
#   'COM)B',
#   'B)C',
#   'C)D',
#   'D)E',
#   'E)F',
#   'B)G',
#   'G)H',
#   'D)I',
#   'E)J',
#   'J)K',
#   'K)L',
# ]

G = defaultdict(list)

for line in lines:
  left_node, right_node = line.split(')')
  G[left_node].append(right_node)
  G[right_node].append(left_node)


def dfs(node, graph, visited, target_node='COM', edge_count=0):
  # print(node)
  
  if node in visited:
    return 0

  if node == target_node:
    return edge_count

  
  visited.add(node)
  edge_count += 1
  adj_nodes = graph[node]

  return dfs(adj_nodes[0], graph, visited, target_node, edge_count)

def iter_dfs(node, graph, target_node='COM'):
  edge_count = 0

  if node == target_node:
    return edge_count

  visited = set()
  visited.add(node)
  edge_count += 1
  adj_nodes = graph[node]
  Q = [adj_nodes[0]]

  # print(node)
  while len(Q):
    n = Q.pop(0)
    # print(n)
    if n == target_node:
      break
    if n in visited:
      continue
    visited.add(node)
    edge_count += 1
    adj_nodes = graph[n]
    Q.append(adj_nodes[0])

  return edge_count

# print(iter_dfs('D', G))
# print(iter_dfs('L', G))
# print(iter_dfs('I', G))

total_orbits = 0
for node in G.keys():
  # print(node, iter_dfs(node, G))
  # total_orbits += iter_dfs(node, G)
  total_orbits += dfs(node, G, set())
print(total_orbits)
