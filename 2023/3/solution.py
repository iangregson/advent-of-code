from collections import defaultdict
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
text = file.read_text()

# text = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """

# # Thanks to https://www.reddit.com/r/adventofcode/comments/189q9wv/2023_day_3_another_sample_grid_to_use/
# text="""
# 12.......*..
# +.........34
# .......-12..
# ..78........
# ..*....60...
# 78..........
# .......23...
# ....90*12...
# ............
# 2.2......12.
# .*.........*
# 1.1.......56
# """

lines = text.strip().split('\n')
symbols: dict[tuple[int, int], str] = {}
for y, line in enumerate(lines):
  for x, char in enumerate(line):
    if not char.isalnum() and char != '.':
      # # negatives aren't symbols
      # if char == '-':
      #   if x + 1 < len(line) and line[x+1].isnumeric():
      #     continue
  
      symbols[(x, y)] = char  

# print(symbols)

def has_symbol(n: str, pos: tuple[int,int], grid: list[str]) -> bool:
  global symbols
  max_x = len(grid[0])
  max_y = len(grid)
  end_x = pos[0] + 1
  start_x = pos[0] - len(n) - 1

  for dy in range(-1, 2):
    y = pos[1] + dy
    for x in range(start_x, end_x):
      if 0 <= x < max_x and 0 <= y < max_y:
        if (x,y) in symbols:
          return True
        
  return False

def has_gear(n: str, pos: tuple[int,int], grid: list[str]) -> bool:
  global symbols
  max_x = len(grid[0])
  max_y = len(grid)
  end_x = pos[0] + 1
  start_x = pos[0] - len(n) - 1

  for dy in range(-1, 2):
    y = pos[1] + dy
    for x in range(start_x, end_x):
      if 0 <= x < max_x and 0 <= y < max_y:
        if (x,y) in symbols and symbols[(x,y)] == '*':
          return (x,y)
        
  return False

s = 0
for y, line in enumerate(lines):
  n = ""
  for x, char in enumerate(line):
    if char.isnumeric():
      n += char
      # # handle negatives 
      # if x > 0 and line[x-1] == '-':
      #   n = "-" + n
      # handle end of line
      if x == len(line) - 1:
        if has_symbol(n, (x,y), lines):
          # print(n)
          s += int(n)
        else:
          # print(f"no symbol for {n}")
          pass
        n = ""
    elif n:
      if has_symbol(n, (x,y), lines):
        # print(n)
        s += int(n)
      else:
        # print(f"no symbol for {n}")
        pass
      n = ""

print(s)

# print("\n\n\n")
# Part 2 ----------------------------

gears: dict[tuple[int, int], list[str]] = defaultdict(list)
s = 0
for y, line in enumerate(lines):
  n = ""
  for x, char in enumerate(line):
    if char.isnumeric():
      n += char
      # # handle negatives 
      # if x > 0 and line[x-1] == '-':
      #   n = "-" + n
      # handle end of line
      if x == len(line) - 1:
        g = has_gear(n, (x,y), lines)
        if g != False:
          # print(n)
          gears[g].append(n)  
        # else:
        #   print(f"no gear for {n}")
        n = ""
    elif n:
      g = has_gear(n, (x,y), lines)
      if g != False:
        # print(n)
        gears[g].append(n)  
      else:
        # print(f"no gear for {n}")
        pass
      n = ""

# for gear in gears:
#   print(gear, gears[gear])

for nums in gears.values():
  if len(nums) == 2:
    gear_ratio = int(nums[0]) * int(nums[1])
    s += gear_ratio

print(s)