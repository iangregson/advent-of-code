#!/usr/bin/env python3

import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.readlines()
lines = [line.strip() for line in input_txt]

# file = open(dir_path + "/test_input.txt", "r")
# input_txt = file.readlines()
# lines = [line.strip() for line in input_txt]

input_txt = lines[0]


def increment_pw(pw):
    pos = -1
    chars = []
    for char in pw:
        chars.append(char)

    char = chars[pos]

    while char == 'z':
        char = 'a'
        chars[pos] = char
        pos -= 1
        char = chars[pos]

    char = chr(ord(char)+1)
    chars[pos] = char
    new_pw = "".join([str(elem) for elem in chars])
    return new_pw


def has_straight(pw):
    az = string.ascii_lowercase
    for n in range(2, 26):
        straight = az[n-2:n+1]
        if straight in pw:
            return True
    return False


def has_iol(pw):
    if 'i' in pw:
        return True
    if 'o' in pw:
        return True
    if 'l' in pw:
        return True
    return False


def has_pairs(pw):
    i = 0
    j = 1
    pairs = []
    while i < len(pw):
        I = pw[i]
        J = ''
        try:
            J = pw[j]
        except:
            J = None
        i += 1
        j += 1

        if I == J:
            p = "".join([c for c in [I, J]])
            pairs.append(p)
    uniq_pairs = []
    for pair in pairs:
        if pair not in uniq_pairs:
            uniq_pairs.append(pair)

    if len(uniq_pairs) >= 2:
        return True

    return False


def valid_pw(pw):
    if input_txt == pw:
        return False
    if not has_straight(pw):
        return False
    if has_iol(pw):
        return False
    if not has_pairs(pw):
        return False
    return True


pw = input_txt
# pw = "abcdefgh"
# pw = "ghijklmn"
while not valid_pw(pw):
    pw = increment_pw(pw)

print("Part 1 answer:", pw)

input_txt = pw
while not valid_pw(pw):
    pw = increment_pw(pw)

print("Part 2 answer:", pw)
