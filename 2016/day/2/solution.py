#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_lines = [l.strip() for l in file.readlines()]

# input_lines = [
#     'ULL',
#     'RRDDD',
#     'LURDL',
#     'UUUUD'
# ]


class Grid():
    def __init__(self):
        self.grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.y_limit = len(self.grid) - 1
        self.x_limit = len(self.grid[0]) - 1
        self.pos = (1, 1)

    def get_current_pos(self):
        return self.pos

    def btn_at_current_pos(self):
        return self.grid[self.pos[0]][self.pos[1]]

    def move(self, direction):
        y = self.pos[0]
        x = self.pos[1]
        if direction == 'U':
            y = max(0, y - 1)
        if direction == 'D':
            y = min(self.y_limit, y + 1)
        if direction == 'L':
            x = max(0, x - 1)
        if direction == 'R':
            x = min(self.x_limit, x + 1)
        self.pos = (y, x)


G = Grid()
btns = []
for line in input_lines:
    for c in line:
        G.move(c)
    btns.append(G.btn_at_current_pos())


print("Part 1 answer:", btns)


class CrazyGrid():
    def __init__(self):
        self.grid = [
            [-1, -1, 1, -1, -1],
            [-1, 2, 3, 4, -1],
            [5, 6, 7, 8, 9],
            [-1, 'A', 'B', 'C', -1],
            [-1, -1, 'D', -1, -1]
        ]
        self.y_limit = len(self.grid) - 1
        self.x_limit = len(self.grid[0]) - 1
        self.pos = (2, 0)

    def get_current_pos(self):
        return self.pos

    def btn_at_current_pos(self):
        return self.grid[self.pos[0]][self.pos[1]]

    def btn_at_pos(self, pos):
        return self.grid[pos[0]][pos[1]]

    def move(self, direction):
        y = self.pos[0]
        x = self.pos[1]
        if direction == 'U':
            y = max(0, y - 1)
        if direction == 'D':
            y = min(self.y_limit, y + 1)
        if direction == 'L':
            x = max(0, x - 1)
        if direction == 'R':
            x = min(self.x_limit, x + 1)

        if not self.btn_at_pos((y, x)) == -1:
            self.pos = (y, x)


G = CrazyGrid()
crazy_btns = []
for line in input_lines:
    for c in line:
        G.move(c)
    crazy_btns.append(G.btn_at_current_pos())


print("Part 2 answer:", crazy_btns)
