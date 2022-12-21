from pathlib import Path
from collections import defaultdict

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

cubes = [tuple(map(int, line.split(','))) for line in text]
cubes = {(x,y,z): 6 for (x,y,z) in cubes}
N = len(cubes)
X, Y, Z = defaultdict(list), defaultdict(list), defaultdict(list)

for cube in cubes:
  x,y,z = cube

  X[(y,z)].append(x)
  Y[(x,z)].append(y)
  Z[(x,y)].append(z)

  cubes[(x,y,z)] = 6

  # connected x
  if (y,z) in X:
    if x+1 in X[(y,z)]:
      cubes[(x,y,z)] -= 1
      cubes[(x+1,y,z)] -= 1
    
    if x-1 in X[(y,z)]:
      cubes[(x,y,z)] -= 1
      cubes[(x-1,y,z)] -= 1
  # connected y
  if (x,z) in Y:
    if y+1 in Y[(x,z)]:
      cubes[(x,y,z)] -= 1
      cubes[(x,y+1,z)] -= 1
    
    if y-1 in Y[(x,z)]:
      cubes[(x,y,z)] -= 1
      cubes[(x,y-1,z)] -= 1
  # connected z
  if (x,y) in Z:
    if z+1 in Z[(x,y)]:
      cubes[(x,y,z)] -= 1
      cubes[(x,y,z+1)] -= 1
    
    if z-1 in Z[(x,y)]:
      cubes[(x,y,z)] -= 1
      cubes[(x,y,z-1)] -= 1


print("Part 1:", sum(cubes.values()))

class Space():
  D = [
    (-1,0,0), # left
    (1,0,0),  # right
    (0,-1,0), # up
    (0,1,0),  # down
    (0,0,1),  # fwd
    (0,0,-1), # back
  ]

  def __init__(self, cubes) -> None:
    self.cubes = cubes
 
    self.minx = min([x for x,y,z in cubes]) - 1
    self.miny = min([y for x,y,z in cubes]) - 1
    self.minz = min([z for x,y,z in cubes]) - 1
    self.maxx = max([x for x,y,z in cubes]) + 1
    self.maxy = max([y for x,y,z in cubes]) + 1
    self.maxz = max([z for x,y,z in cubes]) + 1

  def in_bounds(self, cube):
    x,y,z = cube
    return self.minx <= x <= self.maxx and self.miny <= y <= self.maxy and self.minz <= z <= self.maxz

space = Space(cubes)
Q = [(space.minx,space.miny,space.minz)]
visited = set()
exterior_cubes = set()

while Q:
  cube = Q.pop()
 
  if cube in visited:
    continue

  x,y,z = cube
  for dx,dy,dz in space.D:
    cubep = (x+dx,y+dy,z+dz)
    if not space.in_bounds(cubep):
      continue
    if cubep in cubes:
      exterior_cubes.add((cubep, (dx,dy,dz)))
    else:
      Q.append(cubep)

  visited.add(cube)

print("Part 2:", len(exterior_cubes))
