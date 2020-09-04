#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

input_txt = open(dir_path + "/input.txt", "r")
input_txt = input_txt.read()

# print(input_txt)

def is_trap(prev_row, pos):
    L, C, R = None, None, None

    if pos - 1 < 0:
        L = '.'
    else:
        L = prev_row[pos-1]
    
    if pos + 1 >= len(prev_row):
        R = '.'
    else:
        R = prev_row[pos+1]

    C = prev_row[pos]

    if L == '^' and C == '^' and R != '^':
        return True
    if L != '^' and C == '^' and R == '^':
        return True
    if L == '^' and C != '^' and R != '^':
        return True
    if L != '^' and C != '^' and R == '^':
        return True

    return False
    


N_rows = 40
rows = [
    input_txt
]

# N_rows = 10
# rows = [
#     '.^^.^.^^^^'
# ]

# N_rows = 3
# rows = [
#     '..^^.'
# ]

N_safe = 0

for tile in rows[0]:
    if tile == '.':
        N_safe += 1

for i in range(N_rows-1):
    n_row = ''
    for pos in range(len(rows[i])):
        if is_trap(rows[i], pos):
            n_row += '^'
        else:
            n_row += '.'
            N_safe += 1
    rows.append(n_row)

for row in rows:
    print(row)


print("Part 1 answer:", N_safe)

N_rows = 400000
rows = [
    input_txt
]

N_safe = 0

for tile in rows[0]:
    if tile == '.':
        N_safe += 1

for i in range(N_rows-1):
    n_row = ''
    for pos in range(len(rows[i])):
        if is_trap(rows[i], pos):
            n_row += '^'
        else:
            n_row += '.'
            N_safe += 1
    rows.append(n_row)

print("Part 2 answer:", N_safe)
