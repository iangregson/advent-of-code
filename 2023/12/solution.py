from functools import cache
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
text = file.read_text()


rows = []

for line in text.splitlines():
  row, group_lengths = line.split(' ')
  group_lengths = [int(x) for x in group_lengths.split(',')]
  rows.append((row, tuple(group_lengths)))

@cache
def solve_row(row, state):
  r, groups = row
  i,j,k = state

  if i == len(r):
    if j == len(groups) and k == 0:
      return 1
    elif j == len(groups) - 1 and groups[j] == k:
      return 1
    else:
      return 0
  
  ans = 0
  for c in ['.', '#']:
    if r[i] == c or r[i] == '?':
      if c == '.' and k == 0:
        ans += solve_row(row, (i+1, j, 0))
      elif c == '.' and k > 0 and j < len(groups) and groups[j] == k:
        ans += solve_row(row, (i+1, j+1, 0))
      elif c == '#':
        ans += solve_row(row, (i+1, j, k+1))
  return ans

s = 0
for row in rows:
 s += solve_row(row, (0,0,0))

print(s)

# Part 2 ---------------------------------

rows = []
for line in text.splitlines():
  row, group_lengths = line.split(' ')
  row = '?'.join([row, row, row, row, row])
  group_lengths = ','.join([group_lengths, group_lengths, group_lengths, group_lengths, group_lengths])
  group_lengths = [int(x) for x in group_lengths.split(',')]
  rows.append((row, tuple(group_lengths)))


s = 0
for row in rows:
 s += solve_row(row, (0,0,0))

print(s)


# All thanks and credit goes to J Paulson https://www.youtube.com/watch?v=xTGkP2GNmbQ