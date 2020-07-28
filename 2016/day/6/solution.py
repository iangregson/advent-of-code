#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [line.strip() for line in file.readlines()]

# input_txt = [
#     'eedadn',
#     'drvtee',
#     'eandsr',
#     'raavrd',
#     'atevrs',
#     'tsrnev',
#     'sdttsa',
#     'rasrtv',
#     'nssdts',
#     'ntnada',
#     'svetve',
#     'tesnvt',
#     'vntsnd',
#     'vrdear',
#     'dvrsen',
#     'enarar',
# ]


cols = defaultdict(dict)
for col_idx, _ in enumerate(input_txt[0]):
    cols[col_idx] = defaultdict(int)

for line in input_txt:
    for col_idx, char in enumerate(line):
        if cols[col_idx][char]:
            cols[col_idx][char] += 1
        else:
            cols[col_idx][char] = 1

result = []
for idx, col in cols.items():
    mcc = sorted(col.items(), key=lambda x: x[1], reverse=True)[0]
    result.append(mcc[0])

print("Part 1 answer:", "".join(result))

result = []
for idx, col in cols.items():
    lcc = sorted(col.items(), key=lambda x: x[1])[0]
    result.append(lcc[0])

print("Part 2 answer:", "".join(result))
