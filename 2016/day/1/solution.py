#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()

moves = input_txt.split(", ")

# moves = ['R2', 'L3']
# moves = ['R2', 'R2', 'R2']
# moves = ['R5', 'L5', 'R5', 'R3']
# moves = ['R8', 'R4', 'R4', 'R8']

# print(moves)

start_pos = (0, 0)
current_orientation = 'N'
current_pos = (0, 0)
first_pos_visited_twice = None
visited = set()

for move in moves:
    visited.add(current_pos)
    direction = move[0]
    distance = int(move[1:])

    if direction == 'L':
        if current_orientation == 'N':
            current_orientation = 'W'
        elif current_orientation == 'S':
            current_orientation = 'E'
        elif current_orientation == 'E':
            current_orientation = 'N'
        elif current_orientation == 'W':
            current_orientation = 'S'

    elif direction == 'R':
        if current_orientation == 'N':
            current_orientation = 'E'
        elif current_orientation == 'S':
            current_orientation = 'W'
        elif current_orientation == 'E':
            current_orientation = 'S'
        elif current_orientation == 'W':
            current_orientation = 'N'

    if current_orientation == 'N':
        x, y = current_pos

        for n in range(distance):
            y += 1
            current_pos = (x, y)
            if current_pos in visited and first_pos_visited_twice == None:
                first_pos_visited_twice = current_pos
            visited.add(current_pos)

    if current_orientation == 'S':
        x, y = current_pos
        for n in range(distance):
            y -= 1
            current_pos = (x, y)
            if current_pos in visited and first_pos_visited_twice == None:
                first_pos_visited_twice = current_pos
            visited.add(current_pos)
    if current_orientation == 'E':
        x, y = current_pos
        for n in range(distance):
            x += 1
            current_pos = (x, y)
            if current_pos in visited and first_pos_visited_twice == None:
                first_pos_visited_twice = current_pos
            visited.add(current_pos)
    if current_orientation == 'W':
        x, y = current_pos
        for n in range(distance):
            x -= 1
            current_pos = (x, y)
            if current_pos in visited and first_pos_visited_twice == None:
                first_pos_visited_twice = current_pos
            visited.add(current_pos)


print("Part 1 answer:", sum(map(abs, current_pos)))
print("Part 2 answer:", sum(map(abs, first_pos_visited_twice)))
