from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

def d2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

boxes = [tuple(map(int, line.split(','))) for line in input.splitlines()]
dist_boxes = {}
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        dist = d2(boxes[i], boxes[j])
        dist_boxes[dist] = (i, j)

dist_boxes = dict(sorted(dist_boxes.items()))

parents = {i: i for i in range(len(boxes))}
def find(x):
    if x==parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    if find(x) != find(y):
        parents[find(x)] = find(y)
        return True
    return False

for t, (i,j) in enumerate(list(dist_boxes.values())[:1000]):
    union(i,j)

circuit_sizes = defaultdict(int)
for x in range(len(boxes)):
    circuit_sizes[find(x)] += 1
circuit_sizes = sorted(circuit_sizes.values())
print(circuit_sizes[-1]*circuit_sizes[-2]*circuit_sizes[-3])

parents = {i: i for i in range(len(boxes))} # reset to run union find again
connections = 0
for t, (i,j) in enumerate(dist_boxes.values()):
    if union(i,j):
        connections += 1
        if connections==len(boxes)-1:
            print(boxes[i][0]*boxes[j][0])

        