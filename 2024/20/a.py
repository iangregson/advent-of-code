import heapq
from dataclasses import dataclass
from collections import defaultdict, Counter
from pathlib import Path

input = Path("i.txt").read_text()
min_saving = 100

# input = Path("ex.txt").read_text()
# min_saving = 50

@dataclass
class Track():
    walls: set[tuple[int, int]]
    track: set[tuple[int, int]]
    start: tuple[int, int]
    end: tuple[int, int]
    W: int
    H: int

    def __init__(self, input):
        self.grid = list(input.splitlines())
        self.W = len(self.grid[0])
        self.H = len(self.grid)
        self.walls = set()
        self.track = set()
        self.start = None
        self.end = None
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == "#":
                    self.walls.add((x, y))
                elif cell == ".":
                    self.track.add((x, y))
                elif cell == "S":
                    self.start = (x, y)
                    self.track.add((x, y))
                elif cell == "E":
                    self.end = (x, y)
                    self.track.add((x, y))

    def bounds(self, x, y):
        return 0 <= x < self.W and 0 <= y < self.H
    
    def reachable_positions(self, k, x, y):
        # can go through the wall if free space is reachable
        # in k moves
        start_p = (x, y)
        rp = set()
        Q = [(0, (x, y), [self.grid[y][x]])]
        visited = set()
        while Q:
            moves, p, path = Q.pop(0)
            
            if p in visited:
                continue
            visited.add(p)

            if moves > k:
                continue
            
            # we only care about it if we went through a wall
            if p != start_p and p in self.track and '#' in path:
                rp.add((p, start_p, moves))
            
            x, y = p
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                if self.bounds(nx, ny) and (nx, ny) not in visited:
                    Q.append((moves + 1, (nx, ny),  path + [self.grid[ny][nx]]))
        return rp
        
    def print(self, path = []):
        for y in range(self.H):
            for x in range(self.W):
                if (x, y) in self.walls:
                    print("#", end="")
                elif (x, y) == self.end:
                    print("E", end="")
                elif (x, y) == self.start:
                    print("S", end="")
                elif (x, y) in path:
                    print("O", end="")
                else:
                    print(".", end="")
            print()

T = Track(input)
distances = {}
Q = [(0, T.end)]
while Q:
    d, p = heapq.heappop(Q)
    if p in distances:
        continue
    
    distances[p] = d    
    x,y = p
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if T.bounds(nx, ny) and (nx, ny) in T.track:
            heapq.heappush(Q, (d + 1, (nx, ny)))

cheats = defaultdict(int)
for P in T.track:
    for p, sp, k in T.reachable_positions(2, *P):
        D = distances[T.start] 
        d = D - distances[P]
        dd = d + distances[p] + k
        saving = D - dd
        if saving >= min_saving:
            cheats[saving] += 1
        
# for d, n in sorted(cheats.items()):
#     print(f"There is {n} cheat that saves {d} picoseconds.")

print(sum(cheats.values()))

# part 2

cheats = defaultdict(int)

for P in T.track:
    for p, sp, k in T.reachable_positions(20, *P):
        D = distances[T.start] 
        d = D - distances[P]
        dd = d + distances[p] + k
        saving = D - dd
        if saving >= min_saving:
            cheats[saving] += 1
        
# for d, n in sorted(cheats.items()):
#     print(f"There is {n} cheat that saves {d} picoseconds.")

print(sum(cheats.values()))
