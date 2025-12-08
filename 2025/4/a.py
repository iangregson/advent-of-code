from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

class Grid:
    DIRECTIONS = {
        'N': (-1, 0),
        'NE': (-1, 1),
        'E': (0, 1),
        'SE': (1, 1),
        'S': (1, 0),
        'SW': (1, -1),
        'W': (0, -1),
        'NW': (-1, -1),
    }
    def __init__(self, data):
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0
        self.grid = defaultdict(str)
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[(r, c)] = data[r][c]

    def get(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[(r, c)]
        return None
    
    def set(self, r, c, v):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            self.grid[(r, c)] = v
    
    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors(self, r, c):
        for dr, dc in Grid.DIRECTIONS.values():
            nr, nc = r + dr, c + dc
            if self.in_bounds(nr, nc):
                yield self.get(nr, nc)

    def can_access(self, r, c):
        if not self.in_bounds(r, c):
            return False
        n_adjacent_rolls = sum([1 for n in list(self.neighbors(r, c)) if n == '@'])
        return n_adjacent_rolls < 4
    
    def remove_accessible_rolls(self):
        to_remove = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.get(r, c) == '@' and self.can_access(r, c):
                    to_remove.append((r, c))
        for r, c in to_remove:
            self.set(r, c, '.')

        print(f'removed {len(to_remove)} rolls')

        return len(to_remove)

grid_data = [list(line) for line in input.splitlines()]
grid = Grid(grid_data)

accessible_rolls = 0
for r in range(grid.rows):
    row = ""
    for c in range(grid.cols):
        cell = grid.get(r, c)
        row += cell

        if cell == '@':
            if grid.can_access(r, c):
                accessible_rolls += 1
                row = row[:-1] + 'x'

print(accessible_rolls)

rounds = 0
total_removed = 0
while True:
    removed = grid.remove_accessible_rolls()
    total_removed += removed
    if removed == 0:
        break
    rounds += 1

print(rounds, total_removed)