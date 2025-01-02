import heapq
from pathlib import Path

input = Path("i.txt").read_text()
size = (70,70)
limit = 1024

# input = Path("ex.txt").read_text()
# size = (6,6)
# limit = 12

grid = [['.' for _ in range(size[1] + 1)] for _ in range(size[0] + 1)]

byte_positions = [tuple(map(int, line.split(','))) for line in input.splitlines()]

for i in range(limit):
    x,y = byte_positions[i]
    grid[y][x] = '#'

def grid_print():
    for row in grid:
        print("".join(row))

def grid_bounds(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
    

Q = [(0, (0,0))]
visited = set()
target = size
while Q:
    dist, p = heapq.heappop(Q)
    if p in visited:
        continue
    visited.add(p)
    
    if (p == target):
        print(dist)
        break
    
    x,y = p
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x + dx, y + dy
        if grid_bounds(grid, nx, ny) and grid[ny][nx] != '#':
            heapq.heappush(Q, (dist + 1, (nx, ny)))

byte_pos = None
for i in range(limit, len(byte_positions)):
    byte_pos = byte_positions[i]
    bx, by = byte_pos
    grid[by][bx] = '#'
    path_found = False

    Q = [(0, (0,0))]
    visited = set()
    target = size
    while Q:
        dist, p = heapq.heappop(Q)
        if p in visited:
            continue
        visited.add(p)
        
        if (p == target):
            path_found = True
            break
        
        x,y = p
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if grid_bounds(grid, nx, ny) and grid[ny][nx] != '#':
                heapq.heappush(Q, (dist + 1, (nx, ny)))

    if not path_found:
        print(byte_pos)
        break
