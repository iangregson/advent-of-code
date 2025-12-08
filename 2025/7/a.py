from collections import defaultdict
from functools import cache
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

class Grid:
    def __init__(self, data):
        self.entry_point = (0, 0)
        self.data = data
        self.grid = defaultdict(str)
        self.splitters = set()
        self.beams = set()
        self.height = len(self.data)
        self.width = len(self.data[0])

        for r, line in enumerate(data):
            for c, char in enumerate(line):
                if char == 'S':
                    self.entry_point = (r, c)
                elif char == '^':
                    self.splitters.add((r, c))

    def __str__(self):
        output = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                row.append(self.get(r, c))
            output.append(''.join(row))
        return '\n' + '\n'.join(output)
    
    def __repr__(self):
        return self.__str__()

    def in_bounds(self, r, c):
        return 0 <= c < self.width and 0 <= r < self.height
    
    def get(self, r, c):
        if self.in_bounds(r, c):
            if (r, c) in self.splitters:
                return '^'
            elif (r, c) in self.beams:
                return '|'
            elif (r, c) == self.entry_point:
                return 'S'
            else:
                return '.'
    

grid = Grid(input.splitlines())
# print(grid)

first_beam = (grid.entry_point[0] + 1, grid.entry_point[1])
assert grid.get(*first_beam) == '.'
grid.beams.add(first_beam)

# print(grid)
splits = 0
for r in range(2, grid.height):
    for c in range(grid.width):
        if grid.get(r - 1, c) == '|':
            if grid.get(r, c) == '.':
                grid.beams.add((r, c))
            elif grid.get(r, c) == '^':
                splits += 1
                grid.beams.add((r, c-1))
                grid.beams.add((r, c+1))
    # print(grid)
        
print(splits)

@cache
def timelines(r, c):
    if r+1 == grid.height:
        return 1
    if grid.get(r+1, c) == '^':
        return timelines(r+1, c-1) + timelines(r+1, c+1)
    else:
        return timelines(r+1, c)
    

print(timelines(*grid.entry_point))