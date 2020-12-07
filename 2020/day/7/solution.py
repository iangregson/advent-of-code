#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'light red bags contain 1 bright white bag, 2 muted yellow bags.',
#   'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#   'bright white bags contain 1 shiny gold bag.',
#   'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#   'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#   'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#   'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#   'faded blue bags contain no other bags.',
#   'dotted black bags contain no other bags.',
# ]

G = defaultdict(list)

for line in lines:
  words = line.split()
  node = " ".join(words[:2])

  G[node] = []
  
  if 'contain no other' in line:
    continue
  
  if ',' in line:
    for i in range(0, line.count(',') + 1):
      leaf = " ".join(words[-3:-1])
      leaf_n = int(words[-4])
      G[node].append((leaf_n, leaf))
      words = words[:-4]
  else:
    leaf = " ".join(words[-3:-1])
    leaf_n = int(words[-4])
    G[node].append((leaf_n, leaf))

# print(G)

def check_bags(node, target, visited = set()):
  if node in visited: return 0

  bags = 0
  for leaf in G[node]:
    if leaf[1] == target:
      bags += 1
    bags += check_bags(leaf[1], target, visited)

  visited.add(node)

  return bags

total_bags = 0
for node in G:
  bags = check_bags(node, 'shiny gold', set())
  if bags > 0:
    total_bags += 1


print('Part 1:', total_bags)

# lines = [
#   'shiny gold bags contain 2 dark red bags.',
#   'dark red bags contain 2 dark orange bags.',
#   'dark orange bags contain 2 dark yellow bags.',
#   'dark yellow bags contain 2 dark green bags.',
#   'dark green bags contain 2 dark blue bags.',
#   'dark blue bags contain 2 dark violet bags.',
#   'dark violet bags contain no other bags.',
# ]

G = defaultdict(list)

for line in lines:
  words = line.split()
  node = " ".join(words[:2])

  G[node] = []
  
  if 'contain no other' in line:
    continue
  
  if ',' in line:
    for i in range(0, line.count(',') + 1):
      leaf = " ".join(words[-3:-1])
      leaf_n = int(words[-4])
      G[node].append((leaf_n, leaf))
      words = words[:-4]
  else:
    leaf = " ".join(words[-3:-1])
    leaf_n = int(words[-4])
    G[node].append((leaf_n, leaf))

# print(G)

def count_bags(node):
  bags = 0
  for leaf in G[node]:
    bags += leaf[0]
    bags += leaf[0] * count_bags(leaf[1])

  return bags

print('Part 2:', count_bags('shiny gold'))