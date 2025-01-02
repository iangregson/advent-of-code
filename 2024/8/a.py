import itertools
from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()


class Grid:
    def __init__(self, input):
        self.grid = {}
        lines = input.splitlines()
        self.W = len(lines[0])
        self.H = len(lines)
        for y, line in enumerate(input.splitlines()):
            for x, c in enumerate(line):
                if c.isalpha() or c.isdigit():
                    self.grid[(x, y)] = c

    def __str__(self):
        grid = []
        for y in range(self.H):
            line = ""
            for x in range(self.W):
                line += self.grid.get((x, y), ".")
            grid.append(line)
        return "\n".join(grid)

    def __repr__(self):
        return self.__str__()

    def in_bounds(self, x, y):
        return 0 <= x < self.W and 0 <= y < self.H


g = Grid(input)

antennae = defaultdict(list)
antinodes = set()
for y in range(g.H):
    for x in range(g.W):
        c = g.grid.get((x, y), ".")
        if c.isalpha() or c.isdigit():
            antennae[c].append((x, y))

for a in antennae:
    pairs = itertools.combinations(antennae[a], 2)
    for pair in pairs:
        a, b = sorted(pair)
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay

        nx, ny = ax - dx, ay - dy
        kx, ky = bx + dx, by + dy

        if g.in_bounds(nx, ny):
            antinodes.add((nx, ny))
        if g.in_bounds(kx, ky):
            antinodes.add((kx, ky))


print(len(antinodes))


antinodes = set()
for a in antennae:
    pairs = itertools.combinations(antennae[a], 2)
    for pair in pairs:
        a, b = sorted(pair)
        antinodes.add(a)
        antinodes.add(b)
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay

        nx, ny = ax - dx, ay - dy
        kx, ky = bx + dx, by + dy

        while g.in_bounds(nx, ny):
            antinodes.add((nx, ny))
            nx, ny = nx - dx, ny - dy

        while g.in_bounds(kx, ky):
            antinodes.add((kx, ky))
            kx, ky = kx + dx, ky + dy

# for y in range(g.H):
#     line = ""
#     for x in range(g.W):
#         if (x, y) in antinodes:
#             line += "#"
#         else:
#             line += g.grid.get((x, y), ".")
#     print(line)

print(len(antinodes))
