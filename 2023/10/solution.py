import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()

grid = text.splitlines()

# find s
S = (-1,-1)
for y, line in enumerate(grid):
  x = line.find('S')
  if x >= 0:
    S = (x,y)

print(S)

DN = {
  'N': (0,-1),
  'S': (0,1),
  'E': (1,0),
  'W': (-1,0),
}

D = {
  (0,-1): 'N',
  (0,1): 'S',
  (1,0): 'E',
  (-1,0): 'W',
}

Pipes = {
  '|': [DN['N'], DN['S']], # is a vertical pipe connecting north and south.
  '-': [DN['E'], DN['W']], # is a horizontal pipe connecting east and west.
  'L': [DN['N'], DN['E']], # is a 90-degree bend connecting north and east.
  'J': [DN['N'], DN['W']], # is a 90-degree bend connecting north and west.
  '7': [DN['S'], DN['W']], # is a 90-degree bend connecting south and west.
  'F': [DN['S'], DN['E']], # is a 90-degree bend connecting south and east.
  '.': [],                 # is ground; there is no pipe in this tile.
  'S': [DN['N'], DN['S']], # is the starting position of the animal; there is a pipe on this
}

Q = [(S, 0)]
seen = set()
while Q:
  tile, steps = Q.pop(0)
  x, y = tile
  print(tile, grid[y][x], steps)

  if tile in seen:
    continue

  seen.add(tile)

  for dx, dy in D:
    xx, yy = (x+dx, y+dy)
    if (xx,yy) in seen:
      continue
    if 0 <= xx < len(grid[0]) and 0 <= yy < len(grid):
      new_tile_pos = (xx,yy)
      new_tile = grid[yy][xx]
      # print('\t', (dx, dy), new_tile)
      if new_tile in Pipes:
        if (dx*-1,dy*-1) in Pipes[new_tile]:
          Q.append((new_tile_pos, steps+1))

