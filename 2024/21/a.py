import re
import heapq
from dataclasses import dataclass
from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
input = Path("ex.txt").read_text()

n_pad_grid = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['_','0','A']
]
d_pad_grid = [
    ['_','^','A'],
    ['<','v','>']
]

@dataclass
class Keypad:
    def __init__(self, grid):
        self.grid = grid
        self.points = defaultdict(tuple[int, int])
        self.buttons = defaultdict(str)
        self.W = len(grid[0])
        self.H = len(grid)
        for y in range (self.H):
            for x in range(self.W):
                self.points[(x, y)] = self.grid[y][x]
                self.buttons[self.grid[y][x]] = (x,y)
                
    def bounds(self, x, y):
        return 0 <= x < self.W and 0 <= y < self.H
    
    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)
    
d_pad = Keypad(d_pad_grid)
n_pad = Keypad(n_pad_grid)
D = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}
DD = {
    (0, -1): '^',
    (1, 0): '>',
    (0, 1): 'v',
    (-1, 0): '<',
}

def find_seq(seq: str, pad: Keypad) -> str:
    pos = pad.buttons['A']
    path = []
    for c in seq:
        Q = [(0, pos, [])]
        visited = set()
        target = pad.buttons[c]
        while Q:
            s, p, pp = heapq.heappop(Q)
            if p in visited:
                continue
            visited.add(p)
            
            if p == target:
                pos = p
                path += pp + ['A']
                break
            
            x, y = p
            for dx, dy in D.values():
                nx, ny = x + dx, y + dy
                if pad.bounds(nx, ny) and pad.points[(nx, ny)] != '_':
                    heapq.heappush(Q, (s + 1, (nx, ny), pp + [DD[(dx, dy)]]))
    
    return "".join(path)

code = '029A'
path_a = find_seq(code, n_pad)
path_b = find_seq(path_a, d_pad)
path_c = find_seq(path_b, d_pad)
print(path_c)
print(path_b)
print(path_a)
print(code)

# codes = {code: "" for code in input.splitlines()}
# result = 0
# for code in codes:
#     path = find_seq(code, n_pad)
#     path = find_seq(path, d_pad)
#     path = find_seq(path, d_pad)
#     codes[code] = path

# # codes = {
# #     '029A': '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A',
# #     '980A': '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A',
# #     '179A': '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A',
# #     '456A': '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A',
# #     '379A': '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A',
# # }

# complexity = 0
# for code, path in codes.items():
#     complexity += int("".join(re.findall(f'\d', code))) * len(path)

# print(complexity)


