#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = 1350
# input_txt = 10

def wall_or_open(point, N = input_txt):
    x, y = point
    n =  x*x + 3*x + 2*x*y + y + y*y
    n += N
    bn = bin(n)
    n1s = str(bn).count('1')
    if n1s % 2 == 0:
        return '.'
    else:
        return '#'


# for y in range(10):
#     line = ''
#     for x in range(10):
#         line += wall_or_open((x, y))

#     print(line)

def is_valid_move(pos, move):
    pos_x, pos_y = pos
    mv_x, mv_y = move
    new_pos = (pos_x + mv_x, pos_y + mv_y)
    x, y = new_pos
    if x < 0:
        return False
    if y < 0:
        return False
    if wall_or_open(new_pos) == '#':
        return False
    return True


GOAL = (31,39)
# GOAL = (7,4)
N_STEPS = None
MAX_STEPS = 50
q = []
visited = {}
moves = [
    (0, -1), # up
    (0, 1),  # down
    (-1, 0), # left
    (1, 0),  # right
]
starting_pos = (1, 1, 0)
q.append(starting_pos)

while len(q):
    pos = q.pop()
    x, y, d = pos
    visited[(x, y)] = d
    if (x, y) == GOAL:
        N_STEPS = d
    possible_moves = [m for m in moves if is_valid_move((x, y), m)]
    for mv in possible_moves:
        mv_x, mv_y = mv
        X =  x + mv_x
        Y = y + mv_y
        D = d + 1
        if (X, Y) not in visited or visited[(X, Y)] > d:
            q.append((X, Y, D))
    

print("Part 1 answer:", N_STEPS)
print("Part 2 answer:", len([visited[x] for x in visited.keys() if visited[x] <= MAX_STEPS]))
