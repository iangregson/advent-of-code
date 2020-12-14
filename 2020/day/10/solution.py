#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# print(lines)

# lines = [
#   '16',
#   '10',
#   '15',
#   '5',
#   '1',
#   '11',
#   '7',
#   '19',
#   '6',
#   '12',
#   '4',
# ]

# lines = [
#   '28',
#   '33',
#   '18',
#   '42',
#   '31',
#   '14',
#   '46',
#   '20',
#   '48',
#   '47',
#   '24',
#   '23',
#   '49',
#   '45',
#   '19',
#   '38',
#   '39',
#   '11',
#   '1',
#   '32',
#   '25',
#   '35',
#   '8',
#   '17',
#   '7',
#   '9',
#   '4',
#   '2',
#   '34',
#   '10',
#   '3',
# ]


bag_adapters = sorted([int(l) for l in lines])
device_adapter = max(bag_adapters) + 3

# print(bag_adapters)
# print(device_adapter)

diff_count = defaultdict(int)

current_jolt_rating = 0
while len(bag_adapters):
  adapter = bag_adapters.pop(0)
  diff = adapter - current_jolt_rating
  diff_count[diff] += 1
  current_jolt_rating = adapter

final_diff = device_adapter - current_jolt_rating
diff_count[final_diff] += 1

# print(diff_count)

print('Part 1:', diff_count[1] * diff_count[3])


bag_adapters = sorted([int(l) for l in lines])
device_adapter = max(bag_adapters) + 3
q = bag_adapters.copy()
q.append(device_adapter)
q.insert(0,0)
G = defaultdict(list)

while len(q):
  current_jolts = q.pop(0)

  for i in range(current_jolts - 3, current_jolts + 4):
    if i == current_jolts: continue

    if i in q:
      G[current_jolts].append(i)

# print(G)

def get_paths_to_target(G, target, mem):
  nodes = []
  for node in sorted(G.keys(), reverse=True):
    if target in G[node]:
      nodes.append(node)

  return nodes

n_paths = 1
stack = [device_adapter]
mem = {}
# while len(stack):
#   target = stack.pop()
  
#   paths_to_target = None

#   if target in mem:
#     paths_to_target = mem[target]
#   else:
#     paths_to_target = get_paths_to_target(G, target, mem)
#     mem[target] = paths_to_target

#   if len(paths_to_target) > 1:
#     n_paths += len(paths_to_target) - 1

#   for node in paths_to_target:
#     stack.append(node)
  # print(target, len(paths_to_target), n_paths)
 

# print('Part 2:', n_paths)


mem = {}

def paths_to_target(G, node):
  if node in mem:
    return mem[node]
  paths = 0
  
  if len(G[node]) > 1:
    paths += len(G[node]) - 1
  
  for adapter in G[node]:
    paths += paths_to_target(G, adapter)

  mem[node] = paths
  return paths
# print(G)
print('Part 2:', paths_to_target(G, 0) + 1)
  