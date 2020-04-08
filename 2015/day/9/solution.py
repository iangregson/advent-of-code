#!/usr/bin/env python3

import os
from collections import defaultdict
from itertools import permutations

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.readlines()
lines = [line.strip() for line in input_txt]

# file = open(dir_path + "/test_input.txt", "r")
# input_txt = file.readlines()
# lines = [line.strip() for line in input_txt]

print(lines)

# Build Graph
Ns = set()
Es = []
G = defaultdict(dict)

for line in lines:
    ns, dist = line.split(" = ")
    dist = int(dist)
    src, dest = ns.split(" to ")
    e = (src, dest, dist)

    Es.append(e)
    Ns.add(src)
    Ns.add(dest)
    G[src][dest] = dist
    G[dest][src] = dist

# print(G)
# print(Ns)
# print(Es)

distances = []
for tour in permutations(Ns):
    tour_travelled = sum(map(lambda x, y: G[x][y], tour[:-1], tour[1:]))
    distances.append(tour_travelled)

# print(distances)
print("Part 1 answer:", min(distances))
print("Part 2 answer:", max(distances))
