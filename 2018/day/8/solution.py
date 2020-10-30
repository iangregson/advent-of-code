#!/usr/bin/env python3

import os
import math
from collections import defaultdict


dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read()
# input_txt = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
# print(input_txt)
Ns = [int(x) for x in input_txt.split()]
# print(input_nums)

# DFS via recursion
i = 0

def int_gen():
  i = 0
  Ns = [int(x) for x in input_txt.split()]
  while i <= len(Ns):
    i += 1
    yield Ns[i-1]
 
ints = int_gen()
  
def read_tree():
  nc, nm = next(ints), next(ints)
  children = []
  metadata = []
  for _ in range(nc):
      children.append(read_tree())
  for _ in range(nm):
      metadata.append(next(ints))
  return (children, metadata)

def sum_metas(tree):
  children, metadata = tree
  m = sum(metadata)
  m += sum([sum_metas(child) for child in children])
  return m

def value(tree):
  children, metadata = tree
  if not children:
    return sum(metadata)
  else:
    return sum([value(children[m-1]) for m in metadata if 1 <= m <= len(children)])

root = read_tree()

print("Part 1 answer:", sum_metas(root))
print("Part 2 answer:", value(root))
