from functools import cache
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()

grid = text.splitlines()
W, H = len(grid[0]), len(grid)
Q = []
D = {
  (0,-1): 'N',
  (0,1): 'S',
  (1,0): 'E',
  (-1,0): 'W',
}
DD = {k: v for v, k in D.items()}

state = ((0,0), (1,0), []) # pos, direction, visited
Q.append(state)
visited = set()
while Q:
  pos, direction, path = Q.pop(0)
  x,y = pos
  dx, dy = direction

  if 0 > x or x >= W or 0 > y or y >= H:
    continue

  if ((x,y), direction) in path:
    continue

  path.append((pos, direction))
  visited.add(pos)

  if grid[y][x] == '.':
    next_pos = (x+dx, y+dy)
    Q.append((next_pos, direction, path))
    continue

  if grid[y][x] == '-':
    if D[direction] == 'E' or D[direction] == 'W':
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, direction, path))
      continue
    else:
      east, west = DD['E'], DD['W']
      for dx, dy in [east, west]:
        next_pos = (x+dx, y+dy)
        Q.append((next_pos, (dx,dy), path))
        continue
  
  if grid[y][x] == '|':
    if D[direction] == 'N' or D[direction] == 'S':
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, direction, path))
      continue
    else:
      north, south = DD['N'], DD['S']
      for dx, dy in [north, south]:
        next_pos = (x+dx, y+dy)
        Q.append((next_pos, (dx,dy), path))
        continue
  
  if grid[y][x] == '\\':
    if D[direction] == 'N':
      dx, dy = DD['W']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
    elif D[direction] == 'S':
      dx, dy = DD['E']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
    elif D[direction] == 'E':
      dx, dy = DD['S']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
    elif D[direction] == 'W':
      dx, dy = DD['N']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
  
  if grid[y][x] == '/':
    if D[direction] == 'N':
      dx, dy = DD['E']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
    elif D[direction] == 'S':
      dx, dy = DD['W']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
    elif D[direction] == 'E':
      dx, dy = DD['N']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue
    elif D[direction] == 'W':
      dx, dy = DD['S']
      next_pos = (x+dx, y+dy)
      Q.append((next_pos, (dx,dy), path))
      continue

def print_grid(grid, visited):
  for y in range(H):
    row = ""
    for x in range(W):
      if (x,y) in visited:
        row += '#'
      else:
        row += grid[y][x]
    print(row)

# print_grid(grid, visited)
print()
print(len(visited))