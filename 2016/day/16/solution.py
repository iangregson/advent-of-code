#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")

def generate_data(s):
    a = s
    b=[] 
    b[:0]=a
    # print(b)
    b.reverse()
    # print(b)

    for idx, c in enumerate(b):
        if c == '1':
            b[idx] = '0'
        elif c == '0':
            b[idx] = '1'

    b = "".join(b)
    # print(b)

    return a + '0' + b

def generate_data_of_length(s, N):
    S = generate_data(s)

    while len(S) < N:
        S = generate_data(S)

    return S[:N]

def checksum(s):
    i = 0
    j = 1

    S = []

    while j < len(s):
        if s[i:j+1] == '00' or s[i:j+1] == '11':
            S.append('1')
        else:
            S.append('0')

        i += 2
        j += 2

    return "".join(S)

def find_checksum(s):
    cs = checksum(s)

    while len(cs) % 2 == 0:
        cs = checksum(cs)
    
    return cs


input_txt = '10001001100000001'
L = 272
# input_txt = '10000'
# L = 20

S = generate_data_of_length(input_txt, L)
C = find_checksum(S)

print("Part 1 answer:", C)


input_txt = '10001001100000001'
L = 35651584

S = generate_data_of_length(input_txt, L)
C = find_checksum(S)

print("Part 2 answer:", C)
