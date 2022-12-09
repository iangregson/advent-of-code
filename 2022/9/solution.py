from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
# file = Path(__file__).parent / 'test_input2.txt'
text = file.read_text().splitlines()

class Grid():
  C = { 'R': (1,0), 'U': (0,-1), 'L': (-1,0), 'D': (0,1) }
  D = { 'UR': (1,-1), 'UL': (-1,-1), 'DL': (-1,1), 'DR': (1,1) }
  
  def __init__(self) -> None:
    pass

  @staticmethod
  def neighbors_all(pos):
    d = list(Grid.D.values()) + list(Grid.C.values())
    return Grid.neighbors(pos, d)
  
  @staticmethod
  def neighbors_diagonal(pos):
    return Grid.neighbors(pos, Grid.D.values())

  @staticmethod
  def neighbors_cardinal(pos):
    return Grid.neighbors(pos, Grid.C.values())

  @staticmethod
  def neighbors(pos, directions):
    x, y = pos
    neighbors = set()
    for (dx, dy) in directions:
      neighbors.add((dx + x, dy + y))

    return neighbors
  
  @staticmethod
  def plot(grid_size, knots, start_point=(0,0)):
    top_left, bottom_right = grid_size
    rows = []
    for y in range(top_left[1], bottom_right[1]+1):
      row = ""
      for x in range(top_left[0], bottom_right[0]+1):
        cell = '.'
        if (x,y) == start_point:
          cell = 's'

        for knot in knots:
          if (x,y) == knot.pos:
            cell = f"{knot}"
        
        row += cell
      rows.append(row)
    
    print("\n".join(rows))


class Rope():
  def __init__(self, knots) -> None:
    self.head = Knot(knots.pop(0))

    ptr = self.head
    while knots:
      k = knots.pop(0)
      ptr.next = Knot(k)
      ptr = ptr.next

  @property
  def tail(self):
    tail = self.head
    while tail.next:
      tail = tail.next

    return tail

  def __iter__(self):
    self.__ptr = self.head
    return self

  def __next__(self):
    n = None
    if self.__ptr:
      n = self.__ptr
      self.__ptr = n.next
    else:
      raise StopIteration
    return n

  def __repr__(self) -> str:
    return f"{list(self)}"

  def __str__(self) -> str:
    return f"{list(self)}"


class Knot():
  def __init__(self, id, pos = (0,0)) -> None:
    self.id = id
    self.next = None
    self.pos = None
    self.visited = set()
    self.move(pos)

  def __str__(self) -> str:
    return f"{self.id}"

  def __repr__(self) -> str:
    return f"{self.id}"

  def move(self, pos):   
    self.pos = pos
    self.visited.add(self.pos)

    if not self.next:
      return 

    if self.next.pos == self.pos:
      return 
    if self.next.pos in Grid.neighbors_all(self.pos):
      return 

    # Prefer a cardinal position
    for pos in Grid.neighbors_all(self.next.pos):
      if pos in Grid.neighbors_cardinal(self.pos):
        self.next.move(pos)
        break

    # But fall back to a diagonal
    if self.next.pos not in Grid.neighbors_all(self.pos):
      for pos in Grid.neighbors_all(self.next.pos):
        if pos in Grid.neighbors_all(self.pos):
          self.next.move(pos)
          break

class Sim():
  def __init__(self, instructions, rope, grid_size=[(0,-4),(5,0)]) -> None:
    self.instructions = instructions
    self.rope = rope
    self.grid_size = grid_size

  def visualize_step(self):
    knots = list(self.rope)
    knots.reverse()
    Grid.plot(self.grid_size, knots)
    print()

  def next(self, visualize=False):
    instruction = self.instructions.pop(0)
    direction, steps = instruction.split()

    for _ in range(int(steps)):
      x, y = self.rope.head.pos
      dx, dy = Grid.C[direction]
      self.rope.head.move((x + dx, y + dy))
      if visualize:
        self.visualize_step()

r = Rope(['H','T'])
simulator = Sim(text[:], r)
while simulator.instructions:
  simulator.next()
  
print("Part 1:", len(simulator.rope.tail.visited))

r = Rope(['H',1,2,3,4,5,6,7,8,9])
simulator = Sim(text[:], r, grid_size=[(-11,-15),(14,5)])
while simulator.instructions:
  simulator.next()

print("Part 2:", len(simulator.rope.tail.visited))