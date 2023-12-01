from pathlib import Path
from collections import defaultdict

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
# file = Path(__file__).parent / 'test_input_small.txt'
text = file.read_text().splitlines()

class Compass():
  D = {
    'N': (0,-1),
    'NE': (1,-1),
    'E': (1,0),
    'SE': (1,1),
    'S': (0,1),
    'SW': (-1,1),
    'W': (-1,0),
    'NW': (-1,-1),
  }

class Grove():
  def __init__(self, elves = set()) -> None:
    self.elves = elves

  def has_elf(self, pos=[]):
    return any([p in self.elves for p in pos])

  def is_alone(self, elf):
    x,y = elf
    return not self.has_elf([(x+dx,y+dy) for (dx, dy) in Compass.D.values()])

  def move_elf(self, elf, pos):
    self.elves.remove(elf)
    self.elves.add(pos)

  @property
  def min_x(self):
    return min([x for (x,_) in self.elves])
  @property
  def min_y(self):
    return min([y for (_,y) in self.elves])
  @property
  def max_x(self):
    return max([x for (x,_) in self.elves])
  @property
  def max_y(self):
    return max([y for (_,y) in self.elves])

  def empty_tiles(self):
    n_empty = 0

    for y in range(self.min_y, self.max_y + 1):
      for x in range(self.min_x, self.max_x + 1):
        if (x,y) not in self.elves:
          n_empty += 1

    return n_empty

  def __str__(self) -> str:
    return "\n".join(self.rows)

  def __repr__(self) -> str:
    return f"{self}"
  
  @property
  def rows(self):
    rows = []
    for y in range(self.min_y, self.max_y + 1):
      row = ""
      for x in range(self.min_x, self.max_x + 1):
        if (x,y) not in self.elves:
          row += '.'
        else:
          row += '#'
      rows.append(row)

    return rows

  @staticmethod
  def from_text(lines):
    elf_positions = set()

    for y, row in enumerate(lines):
      for x, chr in enumerate(row):
        if chr == '#':
          elf_positions.add((x,y))

    return Grove(elves=elf_positions)

class Sim():
  D = {
    'N': (0,-1),
    'NE': (1,-1),
    'E': (1,0),
    'SE': (1,1),
    'S': (0,1),
    'SW': (-1,1),
    'W': (-1,0),
    'NW': (-1,-1),
  }
  
  def __init__(self, grove: Grove) -> None:
    self.grove = grove
    self.d = ['N','S','W','E']
    self.DH = {
      'N': [Sim.D['N'],Sim.D['NE'],Sim.D['NW']],
      'E': [Sim.D['E'],Sim.D['NE'],Sim.D['SE']],
      'S': [Sim.D['S'],Sim.D['SE'],Sim.D['SW']],
      'W': [Sim.D['W'],Sim.D['SW'],Sim.D['NW']],
    }

  def turn(self):
    proposals = defaultdict(list)
    """rules
    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
    """
    for elf in self.grove.elves:
      if self.grove.is_alone(elf):
        continue
      
      proposed_moves = []
      for d in self.d:
        x,y = elf
        pos = [(x+dx,y+dy) for (dx,dy) in self.DH[d]]
        if not self.grove.has_elf(pos):
          dx,dy = Compass.D[d]
          tx,ty = x+dx,y+dy
          proposed_moves.append((tx,ty))

      if len(proposed_moves):
        move = proposed_moves.pop(0)
        proposals[move].append(elf)
    
    n_elves_moved = 0
    for target_pos, elves in proposals.items():
      if len(elves) == 1:
        self.grove.move_elf(elves[0], target_pos)
        n_elves_moved += 1

    self.d.append(self.d.pop(0))

    return n_elves_moved

grove = Grove.from_text(text)
sim = Sim(grove)

for _ in range(10):
  sim.turn()

print("Part 1:", sim.grove.empty_tiles())

grove = Grove.from_text(text)
sim = Sim(grove)

for i in range(1,int(1e10)):
  n_elves_moved = sim.turn()
  if n_elves_moved == 0:
    break

print("Part 2:", i)
