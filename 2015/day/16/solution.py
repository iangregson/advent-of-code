#!/usr/bin/env python3

import os
import re
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")

lines = file.readlines()
lines = [line.strip().rstrip('.') for line in lines]

# lines = lines[:11]
G = defaultdict(dict)

for line in lines:
    n = int(re.findall(r"\d+:", line)[0].rstrip(":"))
    sue, props = re.split(r"\d+:", line)
    props = [prop.strip().split(": ") for prop in props.split(",")]
    # props = [p.split(":") for p in props]
    for prop in props:
        G[n][prop[0]] = int(prop[1])
    G[n]['matches'] = set()

target_props = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def has_prop(name, value, sue):
    if name in sue and sue[name] == value:
        return True
    return False


for s in G:
    for prop_name in target_props:
        value = target_props[prop_name]
        if has_prop(prop_name, value, G[s]):
            G[s]['matches'].add(prop_name)

matches = []
for s in G:
    matches.append((len(G[s]['matches']), s))


print("Part 1 answer:", max(matches))


def has_prop_pt2(name, value, sue):
    if name in sue:
        if name in {'cats', 'tress'}:
            if sue[name] > value:
                return True
        elif name in {'pomeranians', 'goldfish'}:
            if sue[name] < value:
                return True
        else:
            if sue[name] == value:
                return True
    return False


for s in G:
    for prop_name in target_props:
        value = target_props[prop_name]
        if has_prop_pt2(prop_name, value, G[s]):
            G[s]['matches'].add(prop_name)

matches = []
for s in G:
    matches.append((len(G[s]['matches']), s))

print("Part 2 answer:", max(matches))
