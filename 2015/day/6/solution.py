#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.readlines()

lines = [line.strip() for line in input_txt]

# print(lines)


class LightGrid:
    def __init__(self, size):
        self.g = [[0 for i in range(size)] for j in range(size)]

    def switch_on(self, start, end):
        self.switch(start, end, "on")

    def switch_off(self, start, end):
        self.switch(start, end, "off")

    def toggle(self, start, end):
        self.switch(start, end, "toggle")

    def switch(self, start, end, operation):
        [x1, y1] = [int(x) for x in start.split(',')]
        [x2, y2] = [int(x) for x in end.split(',')]
        y = y1
        while y <= y2:
            x = x1
            while x <= x2:
                if operation == "toggle":
                    if self.g[y][x] == 0:
                        self.g[y][x] = 1
                    elif self.g[y][x] == 1:
                        self.g[y][x] = 0
                elif operation == "on":
                    self.g[y][x] = 1
                elif operation == "off":
                    self.g[y][x] = 0
                x += 1
            y += 1

    def print(self):
        for row in self.g:
            print(row)
        print("\n")

    def parse_instruction(self, line):
        word_bag = line.split(" ")
        if word_bag[0] == "toggle":
            return [word_bag[1], word_bag[3], word_bag[0]]
        else:
            return [word_bag[2], word_bag[4], word_bag[1]]

    def count_lit(self):
        count = 0
        for row in self.g:
            for light in row:
                count += light
        return count


lg = LightGrid(1000)

for line in lines:
    start, end, operation = lg.parse_instruction(line)
    lg.switch(start, end, operation)

print("Part 1 answer:", lg.count_lit())


class LightGrid_part2:
    def __init__(self, size):
        self.g = [[0 for i in range(size)] for j in range(size)]

    def switch_on(self, start, end):
        self.switch(start, end, "on")

    def switch_off(self, start, end):
        self.switch(start, end, "off")

    def toggle(self, start, end):
        self.switch(start, end, "toggle")

    def switch(self, start, end, operation):
        [x1, y1] = [int(x) for x in start.split(',')]
        [x2, y2] = [int(x) for x in end.split(',')]
        y = y1
        while y <= y2:
            x = x1
            while x <= x2:
                if operation == "toggle":
                    self.g[y][x] += 2
                elif operation == "on":
                    self.g[y][x] += 1
                elif operation == "off":
                    self.g[y][x] = max(self.g[y][x] - 1, 0)
                x += 1
            y += 1

    def print(self):
        for row in self.g:
            print(row)
        print("\n")

    def parse_instruction(self, line):
        word_bag = line.split(" ")
        if word_bag[0] == "toggle":
            return [word_bag[1], word_bag[3], word_bag[0]]
        else:
            return [word_bag[2], word_bag[4], word_bag[1]]

    def count_brightness(self):
        count = 0
        for row in self.g:
            for light in row:
                count += light
        return count


lg = LightGrid_part2(1000)

for line in lines:
    start, end, operation = lg.parse_instruction(line)
    lg.switch(start, end, operation)

print("Part 2 answer:", lg.count_brightness())
