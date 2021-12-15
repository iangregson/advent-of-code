#!/usr/bin/env python3

import os
from collections import defaultdict, Counter
import heapq as hq

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '1163751742',
#   '1381373672',
#   '2136511328',
#   '3694931569',
#   '7463417111',
#   '1319128137',
#   '1359912421',
#   '3125421639',
#   '1293138521',
#   '2311944581',
# ]

G = [[int(x) for x in list(line)] for line in lines]
W = len(G[0])
H = len(G)
# print(G)
def get(loc, grid):
  x, y = loc
  if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
    return grid[y][x]
  else:
    return None

# up down left right
D = [(0,1), (0,-1), (-1,0), (1,0)]

# (isk, (x,y))
Q = [(0, (0,0))]
hq.heapify(Q)

best_risk_level = None
visited = set()
while len(Q):
  risk, (x, y) = hq.heappop(Q)

  # if we're in the finish location
  if (x,y) == (W-1, H-1):
    best_risk_level = risk
    break

  for d in D:
    dx, dy = x + d[0], y + d[1]
    next_risk = get((dx, dy), G)
    if next_risk is not None and (dx, dy) not in visited:
      hq.heappush(Q,(risk + next_risk, (dx, dy)))
      visited.add((dx, dy))

print(best_risk_level)

H = len(lines)
W = len(lines[0])
G = []
for y in range(H*5):
  row = []
  for x in range(W*5):
    i = int(lines[y%H][x%W]) + x // W + y // H
    row.append(i)
  G.append(row)

H = len(G)
W = len(G[0])

Q = [(0, (0,0))]
hq.heapify(Q)

best_risk_level = None
visited = set()
while len(Q):
  risk, (x, y) = hq.heappop(Q)

  # if we're in the finish location
  if (x,y) == (W-1, H-1):
    best_risk_level = risk
    break

  for d in D:
    dx, dy = x + d[0], y + d[1]
    next_risk = get((dx, dy), G)
    if next_risk is not None and (dx, dy) not in visited:
      next_risk = (next_risk - 1) % 9 + 1
      hq.heappush(Q,(risk + next_risk, (dx, dy)))
      visited.add((dx, dy))

print(best_risk_level)