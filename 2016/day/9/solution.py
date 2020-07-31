#!/usr/bin/env python3

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()

# input_txt = 'X(8x2)(3x3)ABCY'  # 18
# input_txt = '(6x1)(1x3)A'  # 6
# input_txt = 'A(2x2)BCD(2x2)EFG'  # 11
# input_txt = '(3x3)XYZ'  # 9
# input_txt = 'A(1x5)BC'  # 7
# input_txt = 'ADVENT ADVENT\nADVENT'  # 18
# input_txt = 'ADVENT'  # 6

# print(input_txt)

regx = re.compile(r'\((.*?)\)+')
s = regx.search(input_txt)
result = input_txt
read_head = 0
while s:
    s = list(s.span())
    s[0] = read_head + s[0]
    s[1] = read_head + s[1]
    # print(s)
    # print(result[s[0]:s[1]])
    marker = result[s[0]:s[1]][1:-1]
    n_chrs, N = [int(x) for x in marker.split('x')]
    head = result[:s[0]]
    tail = result[s[1]:]
    chrs_to_repeat = tail[:n_chrs]
    tail = tail[n_chrs:]
    repeated_chrs = chrs_to_repeat*N
    result = head + repeated_chrs + tail
    read_head = s[0] + (n_chrs * N) - 5
    # print(read_head)
    s = regx.search(result[read_head:])

    # print(result)


print("Part 1 answer:", len(re.sub(r'\s+', '', result, flags=re.UNICODE)))


# input_txt = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'  # 445
# input_txt = '(27x12)(20x12)(13x14)(7x10)(1x12)A'  # 241920
# input_txt = 'X(8x2)(3x3)ABCY'  # XABCABCABCABCABCABCY 20
# input_txt = '(3x3)XYZ'  # XYZXYZXYZ 9


def decompress(s):
    if '(' not in s:
        return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        ret += decompress(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    ret += len(s)
    return ret


print("Part 2 answer:", decompress(
    re.sub(r'\s+', '', input_txt, flags=re.UNICODE)))
