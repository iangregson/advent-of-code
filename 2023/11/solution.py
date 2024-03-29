import itertools
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()

space = text.splitlines()

class Grid():
  def __init__(self, lines: list[str]):
    self.grid = lines

  @property
  def width(self):
    return len(self.grid[0])
  
  @property
  def height(self):
    return len(self.grid)

  def row(self, idx):
    return self.grid[idx]
  
  def col(self, idx):
    return "".join([row[idx] for row in self.grid])
  
  def __str__(self):
    return "\n".join(self.grid)
  
space = Grid(space)

def expand_space(space: Grid) -> Grid:
  new_space: list[str] = []
  empty_rows: list[int] = []
  empty_cols: list[int] = []

  for x in range(space.width):
    column = space.col(x)
    if '#' not in column:
      empty_cols.append(x)

  for y in range(space.height):
    row = space.row(y)
    if '#' not in row:
      empty_rows.append(y)

  for y in range(space.height):
    new_row = ""
    for x in range(space.width):
      if x in empty_cols:
        new_row += '..'
      else:
        new_row += space.row(y)[x]
    new_space.append(new_row)
    if y in empty_rows:
      new_space.append(new_row)

  return Grid(new_space)

space = expand_space(space)
# print(space)

galaxies = {}
for y in range(space.height):
  for x in range(space.width):
    if space.row(y)[x] == '#':
      n = len(galaxies)
      galaxies[n] = (x,y)


galaxy_pairs = list(itertools.combinations(galaxies.keys(), 2))
sum_d = 0
for a, b in galaxy_pairs:
  ga, gb = galaxies[a], galaxies[b]
  d = abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])
  sum_d += d

print(sum_d)
  

# Part 2 ---------------------------------------
# Needs to be 1 million times as big, so need to use a multiplier
# don't actually redraw the space in memory

space = text.splitlines()
space = Grid(space)

size_multiplier = 1e6
# size_multiplier = 2

galaxies = {}
for y in range(space.height):
  for x in range(space.width):
    if space.row(y)[x] == '#':
      n = len(galaxies)
      galaxies[n] = (x,y)

# print(galaxies)

empty_rows: list[int] = []
empty_cols: list[int] = []
for x in range(space.width):
  column = space.col(x)
  if '#' not in column:
    empty_cols.append(x)
for y in range(space.height):
  row = space.row(y)
  if '#' not in row:
    empty_rows.append(y)
# print(empty_rows, empty_cols)


def map_new_galaxy(pos: tuple[int, int], empty_cols: list[int], empty_rows: list[int]) -> tuple[int, int]:
  x, y = pos
  nexs = 0
  for ex in empty_cols:
    if x > ex:
      nexs += 1
  neys = 0
  for ey in empty_rows:
    if y > ey:
      neys += 1

  xx = x + (nexs * (size_multiplier - 1))
  yy = y + (neys * (size_multiplier - 1))

  return (xx, yy)

for gal in galaxies:
  pos = galaxies[gal]
  new_pos = map_new_galaxy(pos, empty_cols, empty_rows)
  # print(pos, new_pos)
  galaxies[gal] = new_pos

galaxy_pairs = list(itertools.combinations(galaxies.keys(), 2))
sum_d = 0
for a, b in galaxy_pairs:
  ga, gb = galaxies[a], galaxies[b]
  d = abs(ga[0] - gb[0]) + abs(ga[1] - gb[1])
  sum_d += d

print(sum_d)
  
