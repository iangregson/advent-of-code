from functools import cache
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

rr = dict.fromkeys(sorted(rr))
for rock in sorted(rr):
  x,y = rock
  yy = y - 1
  while 0 <= yy < h:
    next_pos = (x,yy)
    if next_pos in rr:
      break
    if next_pos in cr:
      break
    
    rr.pop(rock)
    rr[next_pos] = None
    rock = next_pos
    yy -= 1

ans = 0
for x, y in sorted(rr):
  ans += h - y

print(ans)