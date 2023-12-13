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
    print('vertical', vertical_symmetry)
    return vertical_symmetry, True

  horizontal_symmetry = find_horizontal_symmetry(pattern)
  if horizontal_symmetry > 0:
    print('horizontal', horizontal_symmetry)
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

