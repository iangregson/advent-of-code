#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [line.strip() for line in file.readlines()]

# input_txt = [
#     'rect 3x2',
#     'rotate column x=1 by 1',
#     'rotate row y=0 by 4',
#     'rotate column x=1 by 1'
# ]

print(input_txt)


class Screen():
    def __init__(self, dims=(7, 3)):
        x, y = dims
        self.screen = [['.' for i in range(x)] for j in range(y)]

    def __str__(self,):
        rows = []
        for row in self.screen:
            rows.append("".join(row))

        return "\n".join(rows)

    def rect(self, dims=(1, 1)):
        x, y = dims
        for i in range(y):
            for j in range(x):
                self.screen[i][j] = '#'

    def rotate_column(self, col_idx, by):
        curr_values = [None for i in range(len(self.screen))]
        for i in range(len(self.screen)):
            curr_values[i] = self.screen[i][col_idx]
        for i in range(len(self.screen)):
            new_idx = (i+by) % len(self.screen)
            self.screen[new_idx][col_idx] = curr_values[i]

    def rotate_row(self, row_idx, by):
        curr_values = [None for i in range(len(self.screen[0]))]
        for j in range(len(self.screen[0])):
            curr_values[j] = self.screen[row_idx][j]
        for j in range(len(self.screen[0])):
            new_idx = (j+by) % len(self.screen[0])
            self.screen[row_idx][new_idx] = curr_values[j]

    def parse_instruction(self, line):
        if line.startswith('rect'):
            dims = line.split(' ')[1]
            dims = [int(d) for d in dims.split('x')]
            dims = (dims[0], dims[1])
            self.rect(dims)
        elif line.startswith('rotate'):
            _, row_or_col, idx, __, N = line.split(' ')
            idx = int(idx.split('=')[1])
            N = int(N)
            if row_or_col == 'column':
                self.rotate_column(idx, N)
            elif row_or_col == 'row':
                self.rotate_row(idx, N)

    def count_lit(self):
        lit = 0
        for i in range(len(self.screen)):
            for j in range(len(self.screen[0])):
                if self.screen[i][j] == '#':
                    lit += 1
        return lit


S = Screen()
S = Screen((50, 6))

for line in input_txt:
    S.parse_instruction(line)

print(S)

print("Part 1 answer:", S.count_lit())
print("Part 2 answer:", 'RURUCEOIL')
