from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

E = set()
G = defaultdict(list)
for line in input.splitlines():
    a, b = line.split("-")
    E.add((a, b))
    G[a].append(b)
    G[b].append(a)

triangles = set()

for edge in E:
    a, b = edge
    for n in G[a]:
        if n != b and b in G[n]:
            triangle = tuple(sorted([a, b, n]))
            triangles.add(triangle)


count = 0
for t in triangles:
    if any(node.startswith("t") for node in t):
        count += 1
        print(t)

print(count)

import networkx as nx

G_nx = nx.Graph()
G_nx.add_edges_from(E)

for _ in range(10):
    largest_clique = nx.approximation.max_clique(G_nx)
    pw = ""
    for n in sorted(largest_clique):
        pw += n
        pw += ','
    print(pw[:-1])