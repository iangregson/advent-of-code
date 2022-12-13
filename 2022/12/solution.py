from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text()

Map = [list(row) for row in text.splitlines()]
M, N, = len(Map), len(Map[0])
start_location = None
target_location = None
for y in range(M):
  for x in range(N):
    if Map[y][x] == 'E':
      target_location = (x,y)
    elif Map[y][x] == 'S':
      start_location = (x,y)

Map[start_location[1]][start_location[0]] = 'a'
Map[target_location[1]][target_location[0]] = 'z'

def valid_move(cpos, npos, Map):
  M, N, = len(Map), len(Map[0])
  x,y = cpos
  xx,yy = npos

  if 0 <= xx < N and 0 <= yy < M:
    celev = Map[y][x]
    nelev = Map[yy][xx]
    if nelev <= celev:
      return True
    else:
      return (ord(nelev) - ord(celev)) == 1
  else:
    return False

D = [(0,-1),(0,1),(-1,0),(1,0)]
Q = [(start_location, 0)]
visited = set()
final_steps = None
while Q:
  pos, steps = Q.pop(0)

  if pos in visited:
    continue

  if target_location == pos:
    final_steps = steps
    break

  visited.add(pos)

  x,y = pos
  candidate_cells = [(x+dx, y+dy) for (dx, dy) in D if valid_move((x, y), (x+dx, y+dy), Map)]
  for cell in candidate_cells:
      Q.append((cell, steps + 1))

print("Part 1:", final_steps)

Q = []
for y in range(M):
  for x in range(N):
    if Map[y][x] == 'a':
      Q.append(((x,y), 0))

final_steps
visited = set()
while Q:
  pos, steps = Q.pop(0)

  if pos in visited:
    continue

  if target_location == pos:
    final_steps = steps
    break

  visited.add(pos)

  x,y = pos
  candidate_cells = [(x+dx, y+dy) for (dx, dy) in D if valid_move((x, y), (x+dx, y+dy), Map)]
  for cell in candidate_cells:
      Q.append((cell, steps + 1))

print("Part 2:", final_steps)
