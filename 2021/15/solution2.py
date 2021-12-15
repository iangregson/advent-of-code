#!/usr/bin/env python3

import os
import numpy as np
import heapq as hq

dir_path = os.path.dirname(os.path.realpath(__file__))
# m = np.genfromtxt(dir_path + "/input.txt", dtype=int, delimiter=1)
m = np.genfromtxt(dir_path + "/ex_input.txt", dtype=int, delimiter=1)

# file = open(dir_path + "/input.txt", "r")
file = open(dir_path + "/ex_input.txt", "r")
lines = [l.strip() for l in file.readlines()]
G = [[int(x) for x in list(line)] for line in lines]


def search(m):
    visited = set()
    h,w = np.shape(m)
    q = [(0,(0,0))]     # risk, starting point
    while q:
        risk, (x,y) = hq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk
        for x,y in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            if x >= 0 and x < w and y >= 0 and y < h and (x, y) not in visited:
                hq.heappush(q, (risk+m[y][x], (x,y)))
                visited.add((x,y))

print(search(m.copy()))
print(search(G.copy()))

def search(m):
    visited = set()
    h,w = np.shape(m)
    q = [(0,(0,0))]     # risk, starting point
    while q:
        risk, (x,y) = hq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk
        for x,y in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            if x >= 0 and x < w and y >= 0 and y < h and (x, y) not in visited:
                hq.heappush(q, (risk+((m[y][x]-1)%9)+1, (x,y)))
                visited.add((x,y))

m = np.concatenate([m+i for i in range(5)], axis=0)
m = np.concatenate([m+i for i in range(5)], axis=1)
print(search(m))

H = len(lines)
W = len(lines[0])
G = []
for y in range(H*5):
  row = []
  for x in range(W*5):
    i = int(lines[y%H][x%W]) + x // W + y // H
    row.append(i)
  G.append(row)

print(search(G))