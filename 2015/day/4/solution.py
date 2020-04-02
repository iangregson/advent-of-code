#!/usr/bin/env python3

import os
import hashlib

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.read().strip()

# print(input_txt)

# input_txt = "abcdef"
# input_txt = "pqrstuv"


def try_suffix(suffix, starts_with):
    s = input_txt + str(suffix)
    m = hashlib.md5()
    m.update(s.encode())
    result_hex = m.hexdigest()
    return result_hex.startswith(starts_with)


suffix = 0
while True:
    if try_suffix(suffix, "00000"):
        break
    suffix += 1

print("Part 1 answer:", suffix)

suffix = 0
while True:
    if try_suffix(suffix, "000000"):
        break
    suffix += 1

print("Part 2 answer:", suffix)
