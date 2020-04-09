#!/usr/bin/env python3

# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))

# file = open(dir_path + "/input.txt", "r")
# input_txt = file.readlines()
# lines = [line.strip() for line in input_txt]

# file = open(dir_path + "/test_input.txt", "r")
# input_txt = file.readlines()
# lines = [line.strip() for line in input_txt]

input_txt = "3113322113"
# input_txt = "1"
# input_txt = "11"
# input_txt = "21"
# input_txt = "1211"
# input_txt = "111221"


def get_idx_or_none(idx, s):
    try:
        x = s[idx]
        return x
    except:
        return None


N = 40
s = input_txt

for n in range(N):
    M = len(s)
    fast_pointer = 1
    slow_pointer = 0
    seqs = []
    while slow_pointer < M:
        i = get_idx_or_none(slow_pointer, s)
        j = get_idx_or_none(fast_pointer, s)

        seq = i
        while i == j:
            seq += j
            fast_pointer += 1
            slow_pointer += 1
            i = get_idx_or_none(slow_pointer, s)
            j = get_idx_or_none(fast_pointer, s)

        fast_pointer += 1
        slow_pointer += 1
        seqs.append(seq)

    # print(seqs)
    S = ""
    for seq in seqs:
        S += str(len(seq)) + seq[0]
    # print(s, S)
    s = S

print("Part 1 answer:", len(s))

N = 50
s = input_txt

for n in range(N):
    M = len(s)
    fast_pointer = 1
    slow_pointer = 0
    seqs = []
    while slow_pointer < M:
        i = get_idx_or_none(slow_pointer, s)
        j = get_idx_or_none(fast_pointer, s)

        seq = i
        while i == j:
            seq += j
            fast_pointer += 1
            slow_pointer += 1
            i = get_idx_or_none(slow_pointer, s)
            j = get_idx_or_none(fast_pointer, s)

        fast_pointer += 1
        slow_pointer += 1
        seqs.append(seq)

    # print(seqs)
    S = ""
    for seq in seqs:
        S += str(len(seq)) + seq[0]
    # print(s, S)
    s = S

print("Part 2 answer:", len(s))
