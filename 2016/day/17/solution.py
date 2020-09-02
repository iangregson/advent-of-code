#!/usr/bin/env python3

import hashlib

input_txt = 'veumntbg'
input_txt = 'ihgpwlah'
# input_txt = 'kglvqrro'
# input_txt = 'ulqzkmiv'

print(input_txt)

def gen_hash(p=''):
    m = hashlib.md5()
    m.update(input_txt.encode('utf-8'))
    m.update(p.encode('utf-8'))
    return m.hexdigest()[:4]

def is_open(direction, position, hash, grid):
    open_values = ['b', 'c', 'd', 'e', 'f']
    u, d, l, r = [char for char in hash]
    x, y = position
    key, D = direction
    dx, dy = D

    result = False

    if key == 'U':
        if u in open_values and y + dy >= 0:
            result = True
    if key == 'D':
        if d in open_values and y + dy <= len(grid):
            result = True
    if key == 'L':
        if l in open_values and x + dx >= 0:
            result = True
    if key == 'R':
        if r in open_values and x + dx <= len(grid[0]):
            result = True

    return result

def update_pos(pos, d):
    px, py = pos
    dx, dy = d
    new_pos = (px + dx, py + dy)
    return new_pos


Directions = {
    'U': (0, -1), # UP,
    'D': (0, 1), # DOWN,
    'L': (-1, 0), # LEFT,
    'R': (1, 0) # RIGHT,
}

Grid = [
    ['#','.','.','.',],
    ['.','.','.','.',],
    ['.','.','.','.',],
    ['.','.','.','.',]
]

s_pos = (0,0)
s_path = str()
target = (3,3)
q = [(s_pos,s_path)]
paths = []

count = 0

while len(q) and count < 10000:
    pos, current_path = q.pop()
    # print(pos, current_path)

    if pos == target:
        paths.append(current_path)
        break

    h = gen_hash(current_path)
    for D in Directions.items():
        if is_open(D, pos, h, Grid):
            dir_key, dir_val = D
            new_pos = update_pos(pos, Directions[dir_key])
            q.insert(0, (new_pos, current_path + dir_key))

    count += 1



print("Part 1 answer:", paths)

def bfs(start, goal):
    queue = [(start, [start], [])]
    while queue:
        (x, y), path, dirs = queue.pop(0)
        h = gen_hash("".join(dirs))
        for D in Directions.items():
            dir_key, dir_val = D
            if is_open(D, (x, y), h, Grid):
                new_pos = update_pos(pos, Directions[dir_key])
                if new_pos == goal:
                    yield dirs + [dir]
                else:
                    queue.append((new_pos, path + [new_pos], dirs + [dir_key]))

P = list(bfs((0,0), (3,3)))
print("Part 2 answer:", P)
