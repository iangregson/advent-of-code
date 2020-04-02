#!/usr/bin/env python3

from enum import Enum
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()

# print(input_txt)


class Direction(Enum):
    NORTH = '^'
    EAST = '>'
    SOUTH = 'v'
    WEST = '<'


class Board():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.robo_x = 0
        self.robo_y = 0
        self.move_count = 0
        self.presents_delivered = 1
        self.robo_presents_delivered = 0
        self.houses_delivered = 1
        self.visited = set()
        self.robo_visited = set()
        self.visited.add((0, 0))
        self.robo_visited.add((0, 0))

    def total(self):
        return self.presents_delivered + self.robo_presents_delivered

    def move1(self, direction):
        if d == Direction.NORTH:
            self.y += 1
        elif d == Direction.SOUTH:
            self.y -= 1
        if d == Direction.EAST:
            self.x += 1
        if d == Direction.WEST:
            self.x -= 1

        point = (self.x, self.y)

        if point not in self.visited:
            self.presents_delivered += 1
            self.visited.add(point)

    def move2(self, direction):
        self.move_count += 1
        if self.move_count % 2 == 0:
            if d == Direction.NORTH:
                self.robo_y += 1
            elif d == Direction.SOUTH:
                self.robo_y -= 1
            if d == Direction.EAST:
                self.robo_x += 1
            if d == Direction.WEST:
                self.robo_x -= 1

            point = (self.robo_x, self.robo_y)
            # print("Move Robo", self.move_count, point)
            if point not in self.robo_visited and point not in self.visited:
                # print("Robo present delivered")
                self.houses_delivered += 1
                self.robo_visited.add(point)

        else:
            if d == Direction.NORTH:
                self.y += 1
            elif d == Direction.SOUTH:
                self.y -= 1
            if d == Direction.EAST:
                self.x += 1
            if d == Direction.WEST:
                self.x -= 1

            point = (self.x, self.y)
            # print("Move Santa", self.move_count, point)
            if point not in self.robo_visited and point not in self.visited:
                # print("Santa present delivered")
                self.houses_delivered += 1
                self.visited.add(point)


b = Board()

for char in input_txt:
    d = Direction(char)
    b.move1(d)

print("Part 1 answer:", b.presents_delivered)

# input_txt = "^v"
# input_txt = "^>v<"
# input_txt = "^v^v^v^v^v"

b = Board()
for char in input_txt:
    d = Direction(char)
    b.move2(d)

# print("Part 2 answer:", b.total())
print("Part 2 answer:", b.houses_delivered)
