from functools import cache
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()

def find_vertical_symmetry(pattern: list[str]) -> int:
  candidates = []
  i,j = 0,1
  n = len(pattern[0])
  while j < n:
    if pattern[0][i] == pattern[0][j]:
      candidates.append((i,j))
    i += 1
    j += 1

  # print(candidates)
  if len(candidates) == 0:
    return -1

  for idx, (i,j) in enumerate(candidates):
    for row in pattern:
      if row[i] != row[j]:
        candidates[idx] = (-1,-1)
        break
  candidates = [c for c in candidates if c != (-1,-1)]

  # print(candidates)
  if len(candidates) == 0:
    return -1
  
  for idx, c in enumerate(candidates):
    for row in pattern:
      i,j = c
      row_symmetry = True
      while 0 <= i and j < n:
        if row[i] != row[j]:
          row_symmetry = False
          break
        i -= 1
        j += 1
      if row_symmetry == False:
        candidates[idx] = (-1,-1)
        break
  
  candidates = [c for c in candidates if c != (-1,-1)]
  # print(candidates)
  if len(candidates) == 1:
    return candidates[0][1]
  
  return -1

def find_horizontal_symmetry(pattern) -> int:
  candidates = []
  i,j = 0,1
  n = len(pattern)
  while j < n:
    if pattern[i][0] == pattern[j][0]:
      candidates.append((i,j))
    i += 1
    j += 1

  # print(candidates)
  if len(candidates) == 0:
    return -1

  for idx, (i,j) in enumerate(candidates):
    for col in range(len(pattern[0])):
      if pattern[i][col] != pattern[j][col]:
        candidates[idx] = (-1,-1)
        break

  candidates = [c for c in candidates if c != (-1,-1)]

  # print(candidates)
  if len(candidates) == 0:
    return -1

  for idx, c in enumerate(candidates):
    for col in range(len(pattern[0])):
      i,j = c
      col_symmetry = True
      while 0 <= i and j < n:
        if pattern[i][col] != pattern[j][col]:
          col_symmetry = False
          break
        i -= 1
        j += 1
      if col_symmetry == False:
        candidates[idx] = (-1,-1)
        break

  candidates = [c for c in candidates if c != (-1,-1)]
  
  # print(candidates)
  if len(candidates) == 1:
    return candidates[0][1]

  return -1

def find_symmetry(pattern: str) -> (int, bool):
  pattern = pattern.split('\n')
  vertical_symmetry = find_vertical_symmetry(pattern)
  if vertical_symmetry > 0:
    # print('vertical', vertical_symmetry)
    return vertical_symmetry, True

  horizontal_symmetry = find_horizontal_symmetry(pattern)
  if horizontal_symmetry > 0:
    # print('horizontal', horizontal_symmetry)
    return horizontal_symmetry, False
  
  print('None')
  return 0, False


patterns = text.split('\n\n')
ans = 0
for pattern in patterns:
  idx, is_vertical = find_symmetry(pattern)
  if is_vertical:
    ans += idx
  else:
    ans += idx * 100

print(ans)

# find_symmetry(patterns[2])

# part 2 -------------------------------------------

"""
The 'candidates' approach from part 1 one won't work. 
Maybe just need to compare all with all. Should be fine 
because each pattern is fairly small.
"""

def find_vertical_symmetry(pattern: list[str]) -> int:
  width, height = len(pattern[0]), len(pattern)
  for x in range(width-1):
    errors = 0
    for xx in range(width):
      l,r = x - xx, x + xx + 1
      if 0 <= l < r < width:
        for y in range(height):
          if pattern[y][l] != pattern[y][r]:
            errors += 1

    # we want the off by 1
    if errors == 1:
      return x + 1
  
  return -1


def find_horizontal_symmetry(pattern) -> int:
  width, height = len(pattern[0]), len(pattern)
  for y in range(height-1):
    errors = 0
    for yy in range(height):
      u,d = y - yy, y + yy + 1
      if 0 <= u < d < height:
        for x in range(width):
          if pattern[u][x] != pattern[d][x]:
            errors += 1

    # we want the off by 1
    if errors == 1:
      return y + 1
  
  return -1

def find_symmetry(pattern: str) -> (int, bool):
  pattern = pattern.split('\n')
  vertical_symmetry = find_vertical_symmetry(pattern)
  if vertical_symmetry > 0:
    # print('vertical', vertical_symmetry)
    return vertical_symmetry, True

  horizontal_symmetry = find_horizontal_symmetry(pattern)
  if horizontal_symmetry > 0:
    # print('horizontal', horizontal_symmetry)
    return horizontal_symmetry, False
  
  # print('None')
  return 0, False


patterns = text.split('\n\n')
ans = 0
for pattern in patterns:
  idx, is_vertical = find_symmetry(pattern)
  if is_vertical:
    ans += idx
  else:
    ans += idx * 100

print(ans)