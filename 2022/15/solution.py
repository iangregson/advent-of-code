from pathlib import Path
import random

file = Path(__file__).parent / 'input.txt'
Y = 2000000
MAX_X = 4000000
MIN_X = 0
MAX_Y = 4000000
MIN_Y = 0

file = Path(__file__).parent / 'test_input.txt'
Y = 10
MAX_X = 20
MIN_X = 0
MAX_Y = 20
MIN_Y = 0

text = file.read_text().splitlines()


class Beacon():
  def __init__(self, pos, sensor) -> None:
    self.pos = pos
    self.sensor = sensor

  def __str__(self) -> str:
    return f"B{self.pos}"

  def __repr__(self) -> str:
    return f"{self}"

  def __hash__(self) -> int:
    return hash(self.pos)

  @property
  def x(self):
    return self.pos[0]
  
  @property
  def y(self):
    return self.pos[1]
  
  @property
  def distance_to(self, pos):
    x,y = pos
    return abs(self.x - x) + (self.y - y)

class Sensor():
  def __init__(self, pos, beacon) -> None:
    self.pos = pos
    self.beacon = Beacon(beacon, self)
    self.range = self.distance_to(self.beacon.pos)
    self.min_x = self.x - self.range
    self.min_y = self.y - self.range
    self.max_x = self.x + self.range
    self.max_y = self.y + self.range

  def __str__(self) -> str:
    return f"S{self.pos}"

  def __repr__(self) -> str:
    return f"{self}"

  def __hash__(self) -> int:
    return hash(self.pos)

  @staticmethod
  def from_text(text):
    text = text.split()
    sx, sy = int(text[2][2:-1]), int(text[3][2:-1])
    bx, by = int(text[-2][2:-1]), int(text[-1][2:])
    return Sensor((sx,sy), (bx,by))

  @property
  def x(self):
    return self.pos[0]
  
  @property
  def y(self):
    return self.pos[1]

  def distance_to(self, pos):
    x,y = pos
    return abs(self.x - x) + abs(self.y - y)

  def covers(self, pos):
    return self.distance_to(pos) <= self.range

class Grid():
  def __init__(self, sensors, beacons) -> None:
    self.sensors = sensors
    self.beacons = beacons

  @property
  def min_x(self):
    bx = min([b.x for b in self.beacons.values()])
    sx = min([s.min_x for s in self.sensors.values()])
    return min(bx, sx)
  @property
  def max_x(self):
    bx = max([b.x for b in self.beacons.values()])
    sx = max([s.max_x for s in self.sensors.values()])
    return max(bx, sx)
  @property
  def min_y(self):
    by = min([b.y for b in self.beacons.values()])
    sy = min([s.min_y for s in self.sensors.values()])
    return min(by, sy)
  @property
  def max_y(self):
    by = max([b.y for b in self.beacons.values()])
    sy = max([s.max_y for s in self.sensors.values()])
    return max(by, sy)

  def __getitem__(self, idx):
    row = []
    for x in range(self.min_x, self.max_x):
      pos = (x, idx)
      if pos in self.beacons:
        row.append((x, self.beacons[pos]))
      elif pos in self.sensors:
        row.append((x, self.sensors[pos]))
      else:
        row.append((x, None))

    return row

  def __iter__(self):
    self.__row = min(self.ys)
    return self

  def __next__(self):
    row = None
    if self.__row <= max(self.ys):
      row = self[self.__row]
      self.__row += 1
    else:
      raise StopIteration

    return row

  def is_covered(self, pos):
    for s in self.sensors.values():
      if s.covers(pos):
        return True

    return False

beacons = {}
sensors = {}

for line in text:
  s = Sensor.from_text(line)
  beacons[s.beacon.pos] = s.beacon
  sensors[s.pos] = s

grid = Grid(sensors, beacons)

def print_row(grid, row_idx):
  r = ""
  for x,v in grid[row_idx]:
    if isinstance(v, Beacon):
      r += 'B'
    elif isinstance(v, Sensor):
      r += 'S'
    elif grid.is_covered((x,row_idx)):
      r += '#'
    else:
      r += '.'

  return r

def count_covered(prow):
  count = 0
  for c in prow:
    if c == '#':
      count += 1
  return count

print("Part 1:", count_covered(print_row(grid, Y)))


