import heapq
from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()
# input = Path("ex2.txt").read_text()


class Grid:
    W: int
    H: int
    D = [(0,-1), (1,0), (0,1), (-1,0)]
    start: tuple[int, int]
    end: tuple[int, int]
    open_tiles: set[tuple[int,int]]

    def __init__(self, input):
        self.grid = input.splitlines()
        self.W = len(self.grid[0])
        self.H = len(self.grid)
        self.open_tiles = set()

        for y in range(self.H):
            for x in range(self.W):
                if self.grid[y][x] == "S":
                    self.start = (x, y)
                    self.open_tiles.add((x, y))
                elif self.grid[y][x] == "E":
                    self.end = (x, y)
                    self.open_tiles.add((x, y))
                elif self.grid[y][x] == ".":
                    self.open_tiles.add((x, y))

    def bounds(self, p):
        x, y = p
        return 0 <= x < self.W and 0 <= y < self.H

    def loc(self, p):
        x, y = p
        if not self.bounds(p):
            return None

        return self.grid[y][x]


best_score = 2**32
g = Grid(input)
east = 1
v = defaultdict(int)
best_path_tile = None
# game state (score, position, path, direction index)
Q = [(0, g.start, [g.start], east)]

while Q:
    s,p,pa,d = heapq.heappop(Q)

    seen_score = v.get((p,d), 2**32)

    if s > best_score:
        continue
    if s > seen_score:
        continue

    if p == g.end:
        if s < best_score:
            best_score = s
            best_path_tile = set(pa)
        elif s == best_score:
            best_path_tile = best_path_tile.union(set(pa))
        continue

    if g.loc(p) != '#':
        v[(p,d)] = s
        x, y  = p
        dx, dy = g.D[d]
        xx, yy = x + dx, y + dy
        pp = (xx, yy)
        if g.bounds(pp) and g.loc(pp) != '#':
            heapq.heappush(Q, (s+1, pp, pa + [pp], d))
        heapq.heappush(Q, (s+1000, p, pa, (d+1)%4)) # clockwise
        heapq.heappush(Q, (s+1000, p, pa, (d+3)%4)) # anticlockwise

print(best_score)
print(len(best_path_tile))
