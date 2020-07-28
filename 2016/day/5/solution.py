#!/usr/bin/env python3

import os
import hashlib
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()

print(input_txt)

door_id = input_txt
# door_id = 'abc'


def H(s, i):
    result = hashlib.md5(bytes(str(s) + str(i), 'utf8'))
    return result.hexdigest()


def starts_w_zeros(s, N):
    return str(s)[0:5] == '0'*N


# N_zeros = 5
# I = 0
# chars = []
# for i in range(8):
#     c = None
#     while True:
#         h = H(door_id, I)
#         if starts_w_zeros(h, N_zeros):
#             c = h[N_zeros]
#             chars.append(c)
#             I += 1
#             break
#         else:
#             I += 1

# result = "".join(chars)

# print("Part 1 answer:", result)

N_zeros = 5
I = 0
chars = ['_']*8
for i in range(8):
    c = None
    while True:
        h = H(door_id, I)
        sys.stdout.write("\r" + str(I) + "\t\t" + "".join(chars))
        if starts_w_zeros(h, N_zeros):
            pos = h[N_zeros]
            if pos.isnumeric() and int(pos) < len(chars) and chars[int(pos)] == '_':
                c = h[N_zeros+1]
                chars[int(pos)] = c
                I += 1
                break
            else:
                I += 1
        else:
            I += 1

result = "".join(chars)

print("\nPart 2 answer:", result)
