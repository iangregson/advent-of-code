from collections import defaultdict
from functools import cache
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

G = defaultdict(list)

for line in input.splitlines():
    a, b = line.split(": ")
    ns = b.split(" ")
    G[a] += ns

START = 'you'
END = 'out'

Q = [(START, [])]
paths = []
while Q:
    node, path = Q.pop(0)
    # print(node, path)
    if node == END:
        paths.append(path)
        continue

    if node in path:
        continue

    path.append(node)
    
    for n in G[node]:
        Q.append((n, path.copy()))

print(len(paths))


START = 'svr'
END = 'out'

@cache
def count_paths(start, end, has_dac=False, has_fft=False):
    if start == end:
        if has_dac and has_fft:
            return 1
        else:
            return 0
        
    total = 0
    for n in G[start]:
        now_has_dac = has_dac
        if n == 'dac':
            now_has_dac = True
        now_has_fft = has_fft
        if n == 'fft':
            now_has_fft = True

        total += count_paths(n, end, now_has_dac, now_has_fft)
    
    return total

print(count_paths(START, END))