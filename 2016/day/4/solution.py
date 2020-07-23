#!/usr/bin/env python3

import os
from collections import defaultdict
import string

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_lines = file.readlines()
input_lines = [line.strip() for line in input_lines]

# input_lines = [
#     'aaaaa-bbb-z-y-x-123[abxyz]',
#     'a-b-c-d-e-f-g-h-987[abcde]',
#     'not-a-real-room-404[oarel]',
#     'totally-real-room-200[decoy]'
# ]

# print(input_lines)


class Room():
    def __init__(self, line):
        name, sector_id, chksum, = self.parse(line)
        self.name = name
        self.sector_id = int(sector_id)
        self.chksum = chksum

    def __str__(self):
        return ','.join([self.name, str(self.sector_id), self.chksum])

    def parse(self, line):
        line_parts = line.split('-')
        name = '-'.join(line_parts[0:-1])
        sector_id, chksum = line_parts[-1].split('[')
        chksum = chksum[0:-1]
        return name, sector_id, chksum

    def is_real(self):
        chk = self.do_chksum()
        return chk == self.chksum

    def do_chksum(self):
        letter_counts = defaultdict(int)
        for c in self.name:
            if c == '-':
                continue
            if letter_counts[c]:
                letter_counts[c] += 1
            else:
                letter_counts[c] = 1

        count_letters = defaultdict(set)
        for (letter, count) in letter_counts.items():
            count_letters[count].add(letter)

        s = ''
        for (count, letters) in sorted(count_letters.items(), reverse=True):
            letters = sorted(letters)
            ls = ''.join(letters)
            s += ls

        return s[0:5]


sector_ids = []
for line in input_lines:
    r = Room(line)
    if r.is_real():
        sector_ids.append(r.sector_id)

print("Part 1 answer:", sum(sector_ids))


def decrypt_name(name, sector_id):
    az = string.ascii_lowercase
    dec_name = ''
    for enc_c in name:
        dec_c = ''
        if enc_c == '-':
            dec_c = ' '
        else:
            curr_idx = az.index(enc_c)
            distance = (sector_id % 26)
            new_idx = curr_idx + distance
            dec_c = az[new_idx % len(az)]
        dec_name += dec_c

    return dec_name


sector_id = None
for line in input_lines:
    r = Room(line)
    if r.is_real():
        sector_ids.append(r.sector_id)
        dec_name = decrypt_name(r.name, r.sector_id)
        if 'north' in dec_name:
            # print(dec_name)
            # print(r)
            sector_id = r.sector_id

print("Part 2 answer:", sector_id)
