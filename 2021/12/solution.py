#!/usr/bin/env python3

import os
import re
from collections import defaultdict
import collections

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

lines = [
  'start-A',
  'start-b',
  'A-c',
  'A-b',
  'b-d',
  'A-end',
  'b-end',
]

# lines = [
#   'dc-end',
#   'HN-start',
#   'start-kj',
#   'dc-start',
#   'dc-HN',
#   'LN-dc',
#   'HN-end',
#   'kj-sa',
#   'kj-HN',
#   'kj-dc',
# ]

# lines = [
#   'fs-end',
#   'he-DX',
#   'fs-he',
#   'start-DX',
#   'pj-DX',
#   'end-zg',
#   'zg-sl',
#   'zg-pj',
#   'pj-he',
#   'RW-he',
#   'fs-DX',
#   'pj-RW',
#   'zg-RW',
#   'start-pj',
#   'he-WI',
#   'zg-he',
#   'pj-fs',
#   'start-RW',
# ]

Graph = defaultdict(list)

for line in lines:
  node1, node2 = line.split('-')
  Graph[node1].append(node2)
  Graph[node2].append(node1)

# print(Graph)

def bfs(start, goal, allow_visit_twice):
  path_count = 0
  visited = set()
  q = [(start, visited, allow_visit_twice)]
  while q:
    node, visited, allow_visit_twice = q.pop(0)
    if node == goal:
      path_count += 1
      continue
    if node.islower():
      if node in visited:
        allow_visit_twice = False
      visited.add(node)
    for n in Graph[node]:
      if n not in visited or allow_visit_twice and n != start:
        q.append((n, visited.copy(), allow_visit_twice))
  
  return path_count

print(bfs('start', 'end', False))
print(bfs('start', 'end', True))
