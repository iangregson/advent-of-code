#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

input_txt = open(dir_path + "/input.txt", "r")
input_txt = input_txt.read()

print(input_txt)

elves = []

N = 5
i = 1
while i <= N:
    elves.insert(i, (i,1))
    i += 1

print(elves)
          
while len(elves) > 1:
    for pos in range(1, N+1):
        elf = elves[pos]
        elf_n, elf_p = elf
        
        if pos % 2 != 0:
            


print("Part 1 answer:", 0)
print("Part 2 answer:", 0)
