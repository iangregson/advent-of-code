from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
# file = Path(__file__).parent / 'test_input2.txt'
text = file.read_text().splitlines()

class Addx():
  def __init__(self, instruction) -> None:
    self.cycles = 2
    self.args = Addx.parse_args(instruction)

  @staticmethod
  def parse_args(instruction):
    args = instruction[4:].split()
    return args

  def __repr__(self) -> str:
    return f"{self.__class__.__name__.lower()}({','.join(self.args)})"

  def exec(self, cpu):
    for _ in range(self.cycles):
      cpu.cycle()
    
    cpu.registers['X'] += int(self.args[0])

class Noop():
  def __init__(self, instruction) -> None:
    self.cycles = 1
    self.args = Noop.parse_args(instruction)

  @staticmethod
  def parse_args(instruction):
    args = instruction[4:].split()
    return args
  
  def __repr__(self) -> str:
    return f"{self.__class__.__name__.lower()}({','.join(self.args)})"

  def exec(self, cpu):
    for _ in range(self.cycles):
      cpu.cycle()

class CRT():
  WIDTH = 40
  HEIGHT = 6
  
  def __init__(self) -> None:
    self.screen = []
    for y in range(self.HEIGHT):
      r = []
      for x in range(self.WIDTH):
        r.append('-')
      self.screen.append(r)

  def __str__(self):
    return "\n".join("".join(r) for r in self.screen)
  
  def __repr__(self):
    return f"{self}"

  def draw_pixel(self, cpu):
    sprite_xs = [cpu.registers['X']-1,cpu.registers['X'],cpu.registers['X']+1]
    pixel_x = cpu.cycles % CRT.WIDTH
    pixel_y = cpu.cycles // CRT.WIDTH

    if 0 <= pixel_x < CRT.WIDTH and 0 <= pixel_y < CRT.HEIGHT:
      if pixel_x in sprite_xs:
        self.screen[pixel_y][pixel_x] = '#'
      else:
        self.screen[pixel_y][pixel_x] = '.'

class CPU():
  instructions = {
    'addx': Addx,
    'noop': Noop
  }

  interesting_cycles = [20,60,100,140,180,220]

  def __init__(self, program: list[str], input = None) -> None:
    self.registers = { 'X': 1 }
    self.cycles = 0
    self.program = program[:]
    self.stack = []
    self.input = input
    self.output = []
    self.exit_code = -1
    self.crt = CRT()

    for instruction in self.program:
      cmd = instruction[:4]
      cmd = CPU.instructions[cmd]
      self.stack.insert(0, cmd(instruction))

  def cycle(self):
    self.crt.draw_pixel(cpu)
    self.cycles += 1
    if self.cycles in CPU.interesting_cycles:
      self.output.append(self.cycles * self.registers['X'])

  def run(self):
    while self.stack:
      cmd = self.stack.pop()
      cmd.exec(self)

    self.exit_code = 0

cpu = CPU(text[:])
while cpu.exit_code == -1:
  cpu.run()

print("Part 1:", sum(cpu.output))
print("Part2:")
print(cpu.crt)