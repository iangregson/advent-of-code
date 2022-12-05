import string
from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text()

crates, moves = text.split("\n\n")
crates, moves = crates.splitlines(), moves.splitlines()

stacks_9000 = {i: [] for i in crates[-1].replace(" ", "")}
stacks_9001 = {i: [] for i in crates[-1].replace(" ", "")}

n = len(crates) - 1
m = len(crates[0])
for i in range(n):
  for j in range(m):
    c = crates[i][j]
    if c in string.ascii_uppercase:
      stack = crates[-1][j]
      stacks_9000[stack].insert(0, c)
      stacks_9001[stack].insert(0, c)

for move in moves:
  move = move.split(' ')
  n_crates, src, dest = int(move[1]), move[3], move[5]
  lift_9000 = []
  lift_9001 = []
  for _ in range(n_crates):
    lift_9000.insert(0, stacks_9000[src].pop())
    lift_9001.append(stacks_9001[src].pop())

  for _ in range(n_crates):
    stacks_9000[dest].append(lift_9000.pop())
    stacks_9001[dest].append(lift_9001.pop())


print("Part 1:", "".join([stack[-1] for stack in stacks_9000.values()]))
print("Part 2:", "".join([stack[-1] for stack in stacks_9001.values()]))
