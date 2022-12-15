from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class Grid():
  def __init__(self, *, rock_formations = [], start_pos = (0,0), has_floor = False) -> None:
    self.rock_formations = rock_formations
    self.start_pos = start_pos
    self.grid = {self.start_pos: '+'}
    self.has_floor = has_floor

    for formation in rock_formations:
      start = formation.pop(0)
      while formation:
        end = formation.pop(0)
        sx, sy = start
        ex, ey = end
        min_x, max_x = min(sx, ex), max(sx, ex)
        min_y, max_y = min(sy, ey), max(sy, ey)
        for y in range(min_y, max_y + 1):
          for x in range(min_x, max_x + 1):
            self.grid[(x,y)] = '#'

        start = end

    self.max_y = max([y for (_, y) in self.grid] + [self.start_pos[1]])
   
    if self.has_floor:
      self.max_y += 2
      for x in range(self.min_x, self.max_x + 1):
        self.grid[(x,self.max_y)] = '#'

  @property
  def min_x(self):
    return min([x for (x, _) in self.grid] + [self.start_pos[0]])
  @property
  def min_y(self):
    return min([y for (_, y) in self.grid] + [self.start_pos[1]])
  @property
  def max_x(self):
    return max([x for (x, _) in self.grid] + [self.start_pos[0]])

  @staticmethod
  def from_text(lines, *, start_pos = (0,0), has_floor = False):
    rock_formations = [[tuple(map(int, pair.split(','))) for pair in line.split(' -> ')] for line in lines]
    return Grid(rock_formations=rock_formations, start_pos=start_pos, has_floor=has_floor)

  def __getitem__(self, idx):
    row = ""
    for x in range(self.min_x, self.max_x + 1):
      pos = (x, idx)
      row += self.grid.get(pos, '.')

    return row

  def __iter__(self):
    self.__row = self.min_y
    return self

  def __next__(self):
    row = None
    if self.__row <= self.max_y:
      row = self[self.__row]
      self.__row += 1
    else:
      raise StopIteration

    return row

  def __str__(self) -> str:
    return "\n".join(self)

  def __repr__(self) -> str:
    return f"{self}"

  def add_sand(self):
    pos = self.start_pos

    while pos[1] <= self.max_y:
      x,y = pos
      if self.has_floor and y == self.max_y - 1:
        self.grid[pos] = 'o'
        pos = self.start_pos
        continue
      if (x, y + 1) not in self.grid:
        pos = (x, y + 1)
      elif (x - 1, y + 1) not in self.grid:
        pos = (x - 1, y + 1)
      elif (x + 1, y + 1) not in self.grid:
        pos = (x + 1, y + 1)
      elif pos == self.start_pos:
        break
      else:
        self.grid[pos] = 'o'
        pos = self.start_pos
        continue

  @property
  def sand(self):
    return set([pos for pos in self.grid if self.grid[pos] == 'o'])


G = Grid.from_text(text[:], start_pos=(500,0), has_floor = False)
G.add_sand()

print("Part 1:", len(G.sand))

G = Grid.from_text(text[:], start_pos=(500,0), has_floor = True)
G.add_sand()

print("Part 2:", len(G.sand) + 1)