from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
input = Path("ex.txt").read_text()

input = input.strip()

files = list(zip(input[::2], input[1::2]))

if len(input) % 2 == 1:
    files.append((input[-1], "0"))

disk = []
for id, file in enumerate(files):
    blocks, free = int(file[0]), int(file[1])
    disk += [id] * blocks
    disk += [None] * free


for i in range(len(disk)):
    j = len(disk) - 1 - i
    b = disk[j]
    while b is None:
        j -= 1
        b = disk[j]

    a = disk[i]
    while a is not None:
        i += 1
        a = disk[i]

    if j < i:
        break

    disk[i], disk[j] = disk[j], disk[i]


checksum = 0
for i, file_id in enumerate(disk):
    if file_id is None:
        break
    checksum += i * int(file_id)

print(checksum)


disk_a = defaultdict(list)
for idx, block in enumerate(input):
    file_id = idx // 2
    if idx % 2 == 0:
        blocks = int(block)
        disk_a[file_id].append(blocks)
    else:
        free = int(block)
        disk_a[file_id].append(free)

    if idx == len(input) - 1:
        disk_a[file_id].append(0)

disk_b = []
for file_id in disk_a:
    blocks, free = disk_a[file_id]
    disk_b.append((file_id, blocks, free))

positions = defaultdict(list)
spaces = defaultdict(list)
pos = 0
for file_id, blocks, free in disk_b:
    for i in range(blocks):
        positions[file_id].append(pos)
        pos += 1
    for i in range(free):
        spaces[file_id].append(pos)
        pos += 1

spaces = dict(sorted(spaces.items()))

for file in reversed(disk_b):
    file_id, blocks, free = file
    file_positions = positions[file_id]

    for spaces_file_id in spaces:
        space_positions = spaces[spaces_file_id]

        if len(space_positions) >= blocks:
            for i, fp in enumerate(file_positions):
                if space_positions[0] < fp:
                    fp = space_positions.pop(0)
                    file_positions[i] = fp
            positions[file_id] = file_positions
            spaces[spaces_file_id] = space_positions
            break

disk_c = [None] * pos

for file_id, pos in positions.items():
    for p in pos:
        disk_c[p] = file_id

checksum = 0
for i, file_id in enumerate(disk_c):
    if file_id is None:
        continue
    checksum += i * int(file_id)

print(checksum)
