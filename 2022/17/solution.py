from pathlib import Path
import functools, itertools

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text().splitlines()

class Valve():
  def __init__(self, label, *, flow = 0, edges = []) -> None:
    self.label = label
    self.flow = flow
    self.edges = edges

  def __str__(self) -> str:
    return f"{self.label}<{self.flow}>"

  def __repr__(self) -> str:
    return f"{self.label}<{self.flow}>"

  def __hash__(self):
        return hash((self.label))

  def __eq__(self, other):
      if isinstance(other, Valve):
        return (self.label) == (other.label)
      elif isinstance(other, str):
        return (self.label) == (other)

  def __ne__(self, other):
      return not(self == other)
  
  def __le__(self, other):
      assert(isinstance(other, Valve))
      return self.flow <= other.flow
  
  def __ge__(self, other):
      assert(isinstance(other, Valve))
      return self.flow >= other.flow
  
  def __lt__(self, other):
      assert(isinstance(other, Valve))
      return self.flow < other.flow
  
  def __gt__(self, other):
      assert(isinstance(other, Valve))
      return self.flow > other.flow

  @staticmethod
  def from_text(line):
    tokens = line.split()
    label = tokens[1]
    flow = int(tokens[4].split('=')[-1][:-1])
    edges = [t.replace(',', '') for t in tokens[9:]]

    return Valve(label, flow=flow, edges=edges)

# map valves
valves = {}
# map valves to their adjacent valves
G = {}

for line in text:
  v = Valve.from_text(line)
  valves[v] = v

for v in valves:
  edges = [valves[label] for label in v.edges]
  v.edges = edges
  G[v] = v.edges

# make a [floyd-warshall](https://brilliant.org/wiki/floyd-warshall-algorithm/)
# style table of the shortest distance between all nodes
# edge cost is always 1 for any hop
dp = {valve: {v: int(1e9) for v in valves} for valve in valves}
for a in valves:
  for b in valves:
    if a == b:
      dp[a][b] = 0
    if b in a.edges:
      dp[a][b] = 1

for k in valves:
  for i in valves:
    for j in valves:
      nd = dp[i][k] + dp[k][j]
      if nd < dp[i][j]:
        dp[i][j] = nd



start_node = 'AA'
MAX_T = 30
max_flow_step = sum([v.flow for v in valves])
max_flow = 0
# known_best_path = [valves['DD'],valves['BB'],valves['JJ'],valves['HH'],valves['EE'],valves['CC']]
closed_valves = [v for v in valves if v.flow > 0]
for path in itertools.permutations(closed_valves):
  open_valves = set()
  acc_flow = 0
  cur_flow = sum([v.flow for v in open_valves])
  T = 0
  node = valves[start_node]
  for target in path:
    flow = sum([v.flow for v in open_valves])
    
    d = dp[node][target] + 1
    
    acc_flow += flow * d
    max_flow = max(acc_flow, max_flow)

    T += d

    open_valves.add(target)
    
    node = target

    if node == path[-1]:
      acc_flow += max_flow_step * (MAX_T - T)
      max_flow = max(acc_flow, max_flow)


print("Part 1:", max_flow)


# @functools.lru_cache()
# def next_target(start_node, valves, open_valves, dp):
#   # the target node is the closest, highest value valve that is not already on
#     shut_valves = set([v for v in valves if v.flow > 0]) - set(open_valves)
#     shut_valves = list(shut_valves)
#     shut_valves.sort()
#     print(shut_valves)
#     if not shut_valves:
#       return None, None
    
#     shut_valves.reverse()
#     shut_valves_d = [(dp[start_node][v], v.flow, v) for v in shut_valves if dp[start_node][v] != 0]
#     shut_valves_d = sorted(shut_valves_d, key=lambda t: (-t[0], t[1]))
#     print(shut_valves_d)

    
#     d, c, target = shut_valves_d[0]
#     return target, d

# @functools.lru_cache()
# def calc_flow(open_valves):
#   return sum([v.flow for v in open_valves])

# use a priority queue to make sure we're hitting the most valuable valves
# start_node = 'AA'
# MAX_T = 30
# max_flow = -1 

# closed_valves = [v for v in valves if v.flow == 0]
# Q = [(valves[start_node], 0, 0, [v for v in valves if v.flow == 0])]
# while Q:
#   valve, T, flow, open_valves = Q.pop(0)
#   closed_valves = [v for v in valves if v not in open_valves]
  
#   if T > MAX_T:
#     continue
  
#   if T == MAX_T:
#     max_flow = max(max_flow, flow)
#     continue
  
#   if len(open_valves) == len(valves):
#     n_flow = calc_flow(tuple(open_valves)) * (MAX_T - T)
#     max_flow = max(max_flow, flow + n_flow)
#     continue

#   for v in closed_valves:
#     dist_to_v = dp[valve][v] + 1
#     n_flow = calc_flow(tuple(open_valves)) * dist_to_v
#     Q.append((v, T + dist_to_v, flow + n_flow, open_valves + [v]))

