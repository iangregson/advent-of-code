#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")

lines = file.readlines()
lines = [line.strip() for line in lines]

# print(lines)


class Grid():
    def __init__(self, start_state):
        self.on = "#"
        self.off = "."
        self.size = len(start_state)
        self.grid = []
        for line in start_state:
            row = []
            for char in line:
                row.append(char)
            self.grid.append(row)

    def __str__(self):
        s = "\n"
        for row in self.grid:
            for char in row:
                s += char
            s += "\n"
        return s

    def step(self):
        new_grid = [[0 for i in range(self.size)] for j in range(self.size)]

        for y, row in enumerate(new_grid):
            for x, cell in enumerate(row):
                cell = self.next_state((x, y))
                new_grid[y][x] = cell

        self.grid = new_grid

    def step_pt2(self):
        new_grid = [[0 for i in range(self.size)] for j in range(self.size)]

        for y, row in enumerate(new_grid):
            for x, cell in enumerate(row):
                cell = self.next_state((x, y))
                new_grid[y][x] = cell

        self.grid = new_grid
        self.stuck_corners()

    def stuck_corners(self):
        self.grid[0][0] = self.on
        self.grid[0][self.size-1] = self.on
        self.grid[self.size-1][0] = self.on
        self.grid[self.size-1][self.size-1] = self.on

    def get_pos(self, pos):
        low_bound = 0
        high_bound = self.size - 1
        x, y = pos

        if x < low_bound:
            return None
        if x > high_bound:
            return None
        if y < low_bound:
            return None
        if y > high_bound:
            return None

        v = self.grid[y][x]
        return v

    def next_state(self, pos):
        current_state = self.get_pos(pos)
        x, y = pos
        neighbor_positions = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
            (x-1, y-1),
            (x-1, y+1),
            (x+1, y-1),
            (x+1, y+1)
        ]
        neighbor_values = []
        for p in neighbor_positions:
            v = self.get_pos(p)
            # print("Get pos: ", p, " with value: ", v)
            if v != None:
                neighbor_values.append(v)

        # print(neighbor_values)
        if current_state == self.on:
            if neighbor_values.count(self.on) == 2 or neighbor_values.count(self.on) == 3:
                return self.on
            else:
                return self.off
        else:
            if neighbor_values.count(self.on) == 3:
                return self.on
            else:
                return self.off

    def count_lights_on(self):
        count = 0
        for row in self.grid:
            count += row.count(self.on)

        return count


G = Grid(lines)

steps = 100
for i in range(steps):
    G.step()

print("Part 1 answer:", G.count_lights_on())

G = Grid(lines)
G.stuck_corners()

steps = 100
for i in range(steps):
    G.step_pt2()

print("Part 2 answer:", G.count_lights_on())
