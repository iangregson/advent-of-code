#!/usr/bin/env python3

import os
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
file = open(dir_path + "/ex_input.txt", "r")
scanner_blocks = file.read().strip().split('\n\n')
scanner_blocks = [block.split('\n') for block in scanner_blocks]
scanner_blocks = {block[0]: [tuple(map(int, line.split(','))) for line in block[1:]] for block in scanner_blocks}

scanners = list(scanner_blocks.values())
n_scanners = len(scanners)

#In total, each scanner could be in any of 24 different orientations: facing positive or negative x, y, or z, and considering any of four directions "up" from that facing.
# suppose we face +x. up=y=(+/- y/z). then z=+last?

# permute dimensions and +/- in each dimension = 48? 6*2*2*2 = 48
# scanner says: x, y, z
# could mean:
#  x, y, z
#  x, z, y
#  -y, z, -x

def adjust(point, d):
  assert 0<=d<48
  # last bit of d says whether to flip x
  # second to last bit of d says whether to flip y
  # third to last bit of d says whether to flip z
  # rest of d (d//8) identifies which of the 6 permutations

  ret = [point[0], point[1], point[2]]
  for i,p in enumerate(list(itertools.permutations([0, 1, 2]))):
    if d//8 == i:
      ret = [ret[p[0]], ret[p[1]], ret[p[2]]]
  
  if d%2==1:
    ret[0] *= -1
  if (d//2)%2==1:
    ret[1] *= -1
  if (d//4)%2==1:
    ret[2] *= -1
  return ret

N = n_scanners
FINAL = set(scanners[0])
P = [None for _ in range(N)]
P[0] = (0,0,0)

GOOD = set([0])
BAD = set([x for x in range(1,N)])

B_ADJ = {}
for i in range(N):
  for d in range(48):
    B_ADJ[(i,d)] = [adjust(p, d) for p in scanners[i]]

while BAD:
  found = None
  for b in BAD:
    if found:
      continue
    for g in [0]:
      # could be invalid. I allow you to match to any mix of "good" scanners/beacons, whereas the problem says you should match to 12 beacons from a single good scanner
      g_scan = [tuple([p[0]+P[g][0], p[1]+P[g][1], p[2]+P[g][2]]) for p in FINAL] #B[g]]
      g_set = set(g_scan)
      # g has (+x, +y, +z)
      for b_dir in range(48):
        b_scan = B_ADJ[(b, b_dir)]#[adjust(p, b_dir) for p in B[b]]
        VOTE = defaultdict(int)
        for bi in range(len(scanners[b])):
          for gi in range(len(g_scan)):
            # assume B[b][bi] and G[g][gi] are the same beacon
            # can we find 11 other matching beacons?
            # find dx s.t. b[0] + dx == g[0] i.e. dx = g[0]-b[0]
            dx = -b_scan[bi][0] + g_scan[gi][0]
            dy = -b_scan[bi][1] + g_scan[gi][1]
            dz = -b_scan[bi][2] + g_scan[gi][2]
            VOTE[(dx,dy,dz)] += 1
        for (dx,dy,dz), val in VOTE.items():
          if val >= 12:
              P[b] = (dx, dy, dz)
              #print(f'FOUND {b} via {g} at (x={dx} y={dy} z={dz})')
              for p in b_scan:
                FINAL.add(tuple([p[0] + dx, p[1]+dy, p[2]+dz]))
              found = b
  #print(BAD, found)
  assert found
  BAD.remove(found)
  GOOD.add(found)
print(len(FINAL))

p2_ans = 0
for p1 in P:
  for p2 in P:
    dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])
    if dist > p2_ans:
      p2_ans = dist
print(p2_ans)