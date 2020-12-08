#!/usr/bin/env python3

import os
import random
from collections import namedtuple, defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]


"""
acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
"""

# lines = [
#   'nop +0',
#   'acc +1',
#   'jmp +4',
#   'acc +3',
#   'jmp -3',
#   'acc -99',
#   'acc +1',
#   'jmp -4',
#   'acc +6',
# ]

accumulator = 0
instruction_counts = defaultdict(int)
instruction_history = []
instruction_idx = 0

def acc(arg):
  global accumulator
  accumulator += arg

def jmp(arg):
  global instruction_idx
  instruction_idx += arg

def nop(arg):
  return None

instructions = {
  'acc': acc,
  'jmp': jmp,
  'nop': nop,
}

I = namedtuple('I', ['op', 'arg'])

def parse(line):
  op, arg = line.split()
  arg = int(arg)
  return I(op, arg)

program = [parse(line) for line in lines]

# print(program)

terminated = False
while not terminated:
  if 2 in instruction_counts.values():
    break
  instruction = program[instruction_idx]
  instruction_counts[instruction_idx] += 1
  instructions[instruction.op](instruction.arg)
  instruction_history.append(instruction)
  if instruction.op != 'jmp':
    instruction_idx += 1

print('Part 1:', accumulator - instruction_history[-1].arg)


# lines = [
#   'nop +0',
#   'acc +1',
#   'jmp +4',
#   'acc +3',
#   'jmp -3',
#   'acc -99',
#   'acc +1',
#   'nop -4',
#   'acc +6',
# ]

def run_program(program):
  accumulator = 0
  instruction_counts = defaultdict(int)
  instruction_history = []
  instruction_idx = 0
  terminated = False
  success = False

  while not terminated:
    try:
      instruction = program[instruction_idx]
    except IndexError:
      success = True
      break
    
    if 2 in instruction_counts.values():
      break
    # print(instruction)
    instruction_counts[instruction_idx] += 1
    instruction_history.append(instruction)
    
    if instruction.op == 'acc':
      accumulator += instruction.arg
      instruction_idx += 1
    if instruction.op == 'jmp':
      instruction_idx += instruction.arg
    if instruction.op == 'nop':
      instruction_idx += 1

  return success, accumulator

accumulator = 0
success = False
while not success:
  program = [parse(line) for line in lines]
  idx = random.choice(range(0, len(program)))
  if program[idx].op == 'jmp':
    arg = program[idx].arg
    program[idx] = I('nop', arg)
  elif program[idx].op == 'nop':
    arg = program[idx].arg
    program[idx] = I('jmp', arg)
  # print(program)
  success, accumulator = run_program(program)

print('Part 2:', accumulator)