from pathlib import Path
from collections import defaultdict
from functools import reduce
from operator import mul

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

m = [[int(x) for x in list(line)] for line in text]
M, N = len(m), len(m[0])

for y in range(M):
  for x in range(N):
    v = m[y][x]
    m[y][x] = (x,y,v)

def rotate_matrix(m):
  return [list(reversed(x)) for x in zip(*m)]

def visible_from_left(m):
  t = []
  M, N = len(m), len(m[0])
  for y in range(M):
    for x in range(N):
      tree = m[y][x]
      if x == 0:
        t.append(tree)
        continue

      tallest_left_neighbor = max([t[2] for t in m[y][:x]])
      if tree[2] > tallest_left_neighbor:
        t.append(tree)

  return t

rotations = {
  90: set(),
  180: set(),
  270: set(),
}

V = set(visible_from_left(m))
for r in rotations:
  m = rotate_matrix(m)
  V = V.union(set(visible_from_left(m)))

print("Part 1:", len(V))

def in_bounds(p, m):
  M, N = len(m), len(m[0])
  x, y = p
  return 0 <= x < N and 0 <= y < M

def get_score(p, m):
  D = {
    (0,1): 0,
    (0,-1): 0,
    (1,0): 0,
    (-1,0): 0
  }
  x, y = p
  for (dx, dy) in D:
    xx, yy = x + dx, y + dy
    while in_bounds((xx,yy), m):
      D[(dx, dy)] += 1
      if m[yy][xx] >= m[y][x]:
        break
      xx, yy = xx + dx, yy + dy
  
  return reduce(mul, D.values(), 1)

m = [[int(x) for x in list(line)] for line in text]
M, N = len(m), len(m[0])
best_view_score = -1
for y in range(M):
  for x in range(N):
    best_view_score = max(best_view_score, get_score((x,y), m))

print("Part 2:", best_view_score)