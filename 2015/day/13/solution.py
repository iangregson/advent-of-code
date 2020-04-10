#!/usr/bin/env python3

import os
from collections import defaultdict
from itertools import permutations

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
lines = file.readlines()
lines = [line.strip().rstrip('.') for line in lines]

# file = open(dir_path + "/test_input.txt", "r")
# lines = file.readlines()
# lines = [line.strip().rstrip('.') for line in lines]

# print(lines)

# Build graph
G = defaultdict(dict)
E = []
Ns = set()
for line in lines:
    tokens = line.split(" ")
    n, N, = tokens[0], tokens[-1]
    cost = 0
    if tokens[2] == 'gain':
        cost += int(tokens[3])
    else:
        cost -= int(tokens[3])
    edge = (n, N, cost)
    G[n][N] = cost
    E.append(edge)
    Ns.add(n)

# print(G)
# print(E)
# print(Ns)

happiness = []
for tour in permutations(Ns):
    tour_happiness = 0
    for (idx, person) in enumerate(tour):
        next_idx = (idx + 1) % len(tour)
        next_person = tour[next_idx]
        cost1 = G[person][next_person]
        cost2 = G[next_person][person]
        tour_happiness += cost1 + cost2

    happiness.append(tour_happiness)

print("Part 1 answer:", max(happiness))

# Build graph
G = defaultdict(dict)
E = []
Ns = set()
Ns.add('Me')
for line in lines:
    tokens = line.split(" ")
    n, N, = tokens[0], tokens[-1]
    cost = 0
    if tokens[2] == 'gain':
        cost += int(tokens[3])
    else:
        cost -= int(tokens[3])
    edge = (n, N, cost)
    G[n][N] = cost
    G['Me'][N] = 0
    G[n]['Me'] = 0
    E.append(edge)
    E.append(('Me', N, 0))
    E.append((n, 'Me', 0))
    Ns.add(n)

# print(G)
# print(E)
# print(Ns)

happiness = []
for tour in permutations(Ns):
    tour_happiness = 0
    for (idx, person) in enumerate(tour):
        next_idx = (idx + 1) % len(tour)
        next_person = tour[next_idx]
        cost1 = G[person][next_person]
        cost2 = G[next_person][person]
        tour_happiness += cost1 + cost2

    happiness.append(tour_happiness)

print("Part 2 answer:", max(happiness))
