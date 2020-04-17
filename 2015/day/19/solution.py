#!/usr/bin/env python3

import os
from itertools import zip_longest, tee
from random import shuffle

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")
# file = open(dir_path + "/test_input_2.txt", "r")

lines = file.readlines()
lines = [line.strip() for line in lines]

# print(lines)

mappings = [tuple(line.split(" => ")) for line in lines[0:-2]]
medicine_molecule = lines[-1]

# print(mappings)
# print(medicine_molecule)

distinct_molecules = set()


def splice(mol, idx, rule):
    f, t = rule
    i, j = idx, idx + len(f)
    c = mol[i:j]
    if c == f:
        mol = mol[:i] + t + mol[j:]
    return mol


for m in mappings:
    for i in range(len(medicine_molecule)):
        mol = medicine_molecule
        mol = splice(mol, i, m)
        if mol != medicine_molecule:
            distinct_molecules.add(mol)


# print(distinct_molecules)

print("Part 1 answer:", len(distinct_molecules))

count = 0
mol = medicine_molecule
while len(mol) > 1:
    start = mol
    for f, t in mappings:
        while t in mol:
            count += mol.count(t)
            mol = mol.replace(t, f)

    if start == mol:  # start over if we're getting nowhere
        shuffle(mappings)
        mol = medicine_molecule
        count = 0

print("Part 2 answer:", count)
