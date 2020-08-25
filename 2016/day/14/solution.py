#!/usr/bin/env python3

import os
import re
import hashlib

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = 'ahsbgdzn'
# input_txt = 'abc'

print(input_txt)

hashes = {}

def mdee5(i):
    if i in hashes:
        return hashes[i]

    m = hashlib.md5()
    m.update(input_txt.encode('utf-8'))
    m.update(str(i).encode('utf-8'))
    result = m.hexdigest()
    hashes[i] = result
    return result

def mdee5_pt2(i):
    h = mdee5(i)

    for i in range(2016):
        h = hashlib.md5(h.encode("utf-8")).hexdigest()

    return h


def has_tri(s):
    matcher = re.compile(r'(.)\1\1')
    
    result = matcher.search(s)

    if result is not None:
        return result.group(1)
    else:
        return None

def has_quint(s, t):
    match = t*5
    
    if match in s:
        return match
    else:
        return None

def is_key(i, triple):
    result = None
    j = I + 1
    while j < I + 1000:
        t = mdee5(j)
        # print('\t', j, t)
        q = has_quint(t, triple[0])
        if q is not None:
            result = q
            break
        j += 1

    return result, j


I = 0

keys = []

while True:
    T = mdee5(I)
    # print(I, T)
    tri = has_tri(T)
    if tri is not None:
        # print('Triple!:', I)
        key, key_idx = is_key(I, tri)
        if key is not None:
            keys.append(I)
            # print('KEY:', len(keys), I, tri, key_idx, key)

    I += 1

    if len(keys) == 64:
        break

# print(len(keys))
# print(keys)
print("Part 1 answer:", keys[63])

hashes = {}

def mdee5(i):
    if i in hashes:
        return hashes[i]

    m = hashlib.md5()
    m.update(input_txt.encode('utf-8'))
    m.update(str(i).encode('utf-8'))
    result = m.hexdigest()
    hashes[i] = result
    return result

def mdee5_pt2(i):
    h = mdee5(i)

    for i in range(2016):
        h = hashlib.md5(h.encode("utf-8")).hexdigest()

    return h


def has_tri(s):
    matcher = re.compile(r'(.)\1\1')
    
    result = matcher.search(s)

    if result is not None:
        return result.group(1)
    else:
        return None

def has_quint(s, t):
    match = t*5
    
    if match in s:
        return match
    else:
        return None

def is_key(i, triple):
    result = None
    j = I + 1
    while j < I + 1000:
        t = mdee5_pt2(j)
        # print('\t', j, t)
        q = has_quint(t, triple[0])
        if q is not None:
            result = q
            break
        j += 1

    return result, j


I = 0

keys = []

while True:
    T = mdee5_pt2(I)
    # print(I, T)
    tri = has_tri(T)
    if tri is not None:
        # print('Triple!:', I)
        key, key_idx = is_key(I, tri)
        if key is not None:
            keys.append(I)
            # print('KEY:', len(keys), I, tri, key_idx, key)

    I += 1

    if len(keys) == 64:
        break

# print(len(keys))
# print(keys)
print("Part 2 answer:", keys[63])
