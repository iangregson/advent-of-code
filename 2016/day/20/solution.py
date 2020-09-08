#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

input_txt = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in input_txt.readlines()]
# input_txt = [
#     '5-8',
#     '0-2',
#     '4-7',
# ]
# print(input_txt)

ranges = sorted([[int(i) for i in l.split('-')] for l in input_txt])

low_valid_ip = None
while not low_valid_ip and len(ranges) > 0:
    r1, r2 = ranges.pop(0)
    R1, R2 = ranges[0]

    if (r2 + 1) < R1:
        low_valid_ip = r2 + 1



print("Part 1 answer:", low_valid_ip)

# input_txt = [
#     '5-8',
#     '1-6',
#     '3-9',
# ]
# print(input_txt)

ranges = sorted([[int(i) for i in l.split('-')] for l in input_txt], key=lambda x: x[1], reverse=True)
# print(ranges)

low_bound = 0
high_bound = (4294967295 + 1)
valid_ips = 0

valid_ips += high_bound - ranges[0][1]

while len(ranges) > 1:
    r1, r2 = ranges.pop(0)
    print(r2)

    valid_ips += high_bound - (r2+1)
    high_bound = r2

r1, r2 = ranges.pop(0)
valid_ips += max([r1 - low_bound, 0])

print("Part 2 answer:", valid_ips)

# 834840788 too high
# 4294213108