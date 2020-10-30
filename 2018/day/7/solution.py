#!/usr/bin/env python3

import os
import math
from collections import defaultdict


dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]
# input_txt = [
#   'Step C must be finished before step A can begin.',
#   'Step C must be finished before step F can begin.',
#   'Step A must be finished before step B can begin.',
#   'Step A must be finished before step D can begin.',
#   'Step B must be finished before step E can begin.',
#   'Step D must be finished before step E can begin.',
#   'Step F must be finished before step E can begin.',
# ]
# print(input_txt)

def get_roots(T):
  roots = []
  for node in T:
    parents = node.get_parents(T)
    if len(parents) == 0:
      roots.append(node)

  return roots

class Node(str):

  def get_parents(self, Tree):
    parents = []
    for n, children in Tree.items():
      if self in children:
        parents.append(n)
    
    return parents

  def get_children(self, Tree):
    return Tree[self]

Tree = defaultdict(list)
Degrees = defaultdict(int)

for line in input_txt:
  parent = Node(line.split()[1])
  child = Node(line.split()[-3])
  Tree[parent].append(child)
  Degrees[child] += 1

for node in Tree:
  Tree[node] = sorted(Tree[node])

Q = [node for node in get_roots(Tree)]
seen = []
while len(Q):
  Q = sorted(Q)
  node = Q.pop(0)
  
  seen.append(node)
  children = node.get_children(Tree)
  for child in children:
    Degrees[child] -= 1
    if Degrees[child] == 0:
      Q.append(child)
    
  

# CFMNLOAHRKPTWBJSYZVGUQXIDE
print("Part 1 answer:", "".join([str(node) for node in seen]))

def duration(task_id, t, delay=60):
  t += delay
  duration = 1 + (ord(task_id) - ord('A'))
  t += duration
  return t

Tree = defaultdict(list)
Degrees = defaultdict(int)

for line in input_txt:
  parent = Node(line.split()[1])
  child = Node(line.split()[-3])
  Tree[parent].append(child)
  Degrees[child] += 1

for node in Tree:
  Tree[node] = sorted(Tree[node])

Q = [node for node in get_roots(Tree)]
t = 0
EV = []
workers = list(range(5))
done = []

def do_work():
  global Q
  while len(EV) < len(workers) and Q:
    # print(Q)
    node = min(Q)
    Q = [n for n in Q if n != node]
    # print('Adding to EV: ', (node, t))
    EV.append((duration(node, t), node))
    # print(EV)

do_work()

while EV or Q:
  t, node = min(EV)
  EV = [n for n in EV if n != (t, node)]
  # print(t, node)
  done.append((t, node))

  children = node.get_children(Tree)
  # print(children)
  for child in children:
    Degrees[child] -= 1
    if Degrees[child] == 0:
        Q.append(child)

  do_work()


# print(done)

print("Part 2 answer:", done[-1][0])
