from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text()

moves = [caret for caret in list(text)]

class Grid():
  def __init__(self, init_size=(7,3)) -> None:
    init_x, init_y = init_size
    self.rocks = set([(x, 0) for x in range(init_x)])

  @property
  def max_y(self):
    return max([y for (_, y) in self.rocks])
  
  @property
  def min_y(self):
    return min([y for (_, y) in self.rocks])

  @property
  def max_x(self):
    return max([x for (x, _) in self.rocks])
  
  @property
  def min_x(self):
    return min([x for (x, _) in self.rocks])

  @property
  def floor(self):
    return self.min_y - 1
  
  @property
  def top(self):
    return self.max_y + 4

  @property
  def rows(self):
    rows = []

    for y in range(self.top-1, self.floor - 1, -1):
      row = ""
      for x in range(self.min_x-1, self.max_x + 2):
        if x == self.max_x + 1 or x == self.min_x - 1:
          if y == self.floor:
            row += '+'
          else:
            row += '|'
        else:
          if y == self.floor:
            row += '-'
          else:
            row += '.'
      rows.append(row)
    
    return rows

  def __str__(self) -> str:
    return "\n".join(self.rows)

  def signature(self):
    max_y = self.max_y
    return frozenset([(x, max_y-y) for (x,y) in self.rocks if max_y - y <= 30])

class Rock(set):
  N_TYPES = 5
  
  @staticmethod
  def new(turn, y):
    if turn % Rock.N_TYPES == 0:
      return Rock([(2,y), (3,y), (4,y), (5,y)])
    elif turn % Rock.N_TYPES  ==  1:
      return Rock([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif turn % Rock.N_TYPES  ==  2:
      return Rock([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif turn % Rock.N_TYPES == 3:
      return Rock([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif turn % Rock.N_TYPES == 4:
      return Rock([(2,y+1),(2,y),(3,y+1),(3,y)])
     
  def move_left(self):
    if any([x==0 for (x,y) in self]):
      return self
    return Rock([(x-1,y) for (x,y) in self])

  def move_right(self):
    if any([x==6 for (x,y) in self]):
      return self
    return Rock([(x+1,y) for (x,y) in self])
  
  def move_down(self):
    return Rock([(x,y-1) for (x,y) in self])
  
  def move_up(self):
    return Rock([(x,y+1) for (x,y) in self])


G = Grid()
limit = 2022
move_ptr = 0
turn = 0
while turn < limit:
    rock = Rock.new(turn, G.top)
    while True:
      if moves[move_ptr] == '<':
        rock = rock.move_left()
        
        if rock.intersection(G.rocks):
          rock = rock.move_right()
      else:
        rock = rock.move_right()
        
        if rock.intersection(G.rocks):
          rock = rock.move_left()
      
      move_ptr = (move_ptr + 1) % len(moves)
      
      rock = rock.move_down()
      if rock.intersection(G.rocks):
        rock = rock.move_up()
        G.rocks.update(rock)
        break
    
    turn += 1
  
print("Part 1:", G.max_y)

G = Grid()
limit = 1000000000000
move_ptr = 0
turn = 0
SEEN = {}
added = 0
while turn < limit:
    rock = Rock.new(turn, G.top)
    while True:
      if moves[move_ptr] == '<':
        rock = rock.move_left()
        
        if rock.intersection(G.rocks):
          rock = rock.move_right()
      else:
        rock = rock.move_right()
        
        if rock.intersection(G.rocks):
          rock = rock.move_left()
      
      move_ptr = (move_ptr + 1) % len(moves)
      
      rock = rock.move_down()
      if rock.intersection(G.rocks):
        rock = rock.move_up()
        G.rocks.update(rock)

        SR = (move_ptr, turn % Rock.N_TYPES, G.signature())
        if SR in SEEN and turn>=2022:
          (oldt, oldy) = SEEN[SR]
          dy = G.max_y-oldy
          dt = turn-oldt
          amt = (limit-turn)//dt
          added += amt*dy
          turn += amt*dt
          assert turn<=limit
        SEEN[SR] = (turn,G.max_y)
        break
    turn += 1

print("Part 2:", G.max_y + added)