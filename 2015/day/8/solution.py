#!/usr/bin/env python3

import os
import re
import struct

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.readlines()
lines = [line.strip() for line in input_txt]

# file = open(dir_path + "/test_input.txt", "r")
# input_txt = file.readlines()
# lines = [line.strip() for line in input_txt]


# print(lines)

def count_chars(s):
    s = eval(s)
    return len(s)


code_count = 0
char_count = 0
for line in lines:
    code_count += len(line)
    char_count += count_chars(line)

print("Part 1 answer:", code_count - char_count)


def encode(s):
    n = ""
    for char in s:
        if char == '"':
            n += "\\"
        if char == '\\':
            n += "\\"
        n += char
    return '"' + n + '"'


code_count = 0
encoded_count = 0
for line in lines:
    code_count += len(line)
    s = encode(line)
    encoded_count += len(s)

print("Part 2 answer:", encoded_count - code_count)
