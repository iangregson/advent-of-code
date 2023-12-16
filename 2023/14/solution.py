from collections import defaultdict
from functools import reduce
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()

grid = text.splitlines()
w,h = len(grid[0]), len(grid)

rr = []
cr = set()

for y in range(h):
  for x in range(w):
    if grid[y][x] == 'O':
      rr.append((x,y))
    elif grid[y][x] == '#':
      cr.add((x,y))

directions = {
  (0,-1): 'N',
  (-1,0): 'W',
  (0,1):  'S',
  (1,0):  'E',
}

rr = dict.fromkeys(sorted(rr))
def tilt(rr: dict[tuple[int, int], int], direction: tuple[int, int]) -> dict[tuple[int, int], int]:
  global directions
  # need to sort appropriately for direction
  if directions[direction] == 'N':
    srr = sorted(rr)
  elif directions[direction] == 'S':
    srr = sorted(rr, reverse=True)
  elif directions[direction] == 'E':
    srr = sorted(rr, key=lambda x: (x[0]), reverse=True)
  elif directions[direction] == 'W':
    srr = sorted(rr, key=lambda x: (x[0])) 

  for rock in srr:
    x,y = rock
    dx, dy = direction
    yy = y + dy
    xx = x + dx 
    while 0 <= yy < h and 0 <= xx < w:
      next_pos = (xx,yy)
      if next_pos in rr:
        break
      if next_pos in cr:
        break
      
      rr.pop(rock)
      rr[next_pos] = None
      rock = next_pos
      yy += dy
      xx += dx
  return rr

rr = tilt(rr, direction=(0,-1))
def total_load(rr: dict[tuple[int, int], int]) -> int:
  ans = 0
  for x, y in sorted(rr):
    ans += h - y
  return ans

print(total_load(rr))


# Part 2 -------------------------------------

def cycle(rr: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
  global directions
  for direction in directions:
    rr = tilt(rr, direction)

  return rr

loads = defaultdict(list[int])
i = 0
T = int(1e9)
G = {}
while i < T: 
  i += 1
  rr = cycle(rr)

  hash = tuple(rr.keys())
  if hash in G:
    cycle_len = i - G[hash]
    jump = (T - i) // cycle_len
    i += jump * cycle_len
  
  G[tuple(rr.keys())] = i

print(total_load(rr))
# 100425 # low
# 100782 # high