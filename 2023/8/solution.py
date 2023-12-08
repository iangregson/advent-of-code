from dataclasses import dataclass
from collections import defaultdict
from math import gcd
import pathlib
file = pathlib.Path(__file__).parent.resolve() / 'input.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example2.txt'
# file = pathlib.Path(__file__).parent.resolve() / 'example3.txt'
text = file.read_text()


instructions, network = text.split('\n\n')
instructions = instructions.strip()


G = defaultdict(list[str])

for line in network.split('\n'):
  node_id, siblings = line.split(' = ')

  left, right = siblings[1:-1].split(', ')
  G[node_id].append(left)
  G[node_id].append(right)

start = 'AAA'
target = 'ZZZ'

Q = [(start, 0)]
while Q:
  node_id, d = Q.pop(0)

  if node_id == target:
    print(d)
    break

  instruction = instructions[d % len(instructions)]

  if len(G[node_id]) == 0:
    break

  if instruction == 'L':
    next_node = G[node_id][0]
  else:
    next_node = G[node_id][1]

  Q.append((next_node, d + 1))


# Part 2 ------------------------------------------

G = defaultdict(list[str])

for line in network.split('\n'):
  node_id, siblings = line.split(' = ')

  left, right = siblings[1:-1].split(', ')
  G[node_id].append(left)
  G[node_id].append(right)

# for node in G:
#   print(node, G[node])

Q = []
for node in G:
  if node.endswith('A'):
    Q.append(node)

step = 0
cycle_times = {}
while Q:
  next_nodes = []
  for idx, node in enumerate(Q):
    assert len(G[node]) > 0, f"{node}"

    instruction = instructions[step % len(instructions)]
    if instruction == 'L':
      next_node = G[node][0]
    else:
      next_node = G[node][1]

    # print(instruction, node, G[node], next_node)
    if next_node.endswith('Z'):
      cycle_times[idx] = step+1

    # if every position in the Q has had a cycle, we can break
    if len(cycle_times) == len(Q):
      next_nodes = []
      break

    next_nodes.append(next_node)

  Q = next_nodes
  step += 1


def lcm(nums: list[int]) -> int:
  lcm = nums[0]
  for i in nums[1:]:
    lcm = lcm * i // gcd(lcm, i)
  return lcm 

print(lcm(list(cycle_times.values())))