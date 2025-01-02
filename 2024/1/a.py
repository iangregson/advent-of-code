from pathlib import Path
from collections import Counter

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

a, b = list(zip(*[[int(x) for x in line.split()] for line in input.splitlines()]))

a = sorted(a)
b = sorted(b)

t = 0
for i in range(len(a)):
    t += abs(a[i] - b[i])

print(t)

# part 2

bb = Counter(b)


score = 0
for x in a:
    score += x * bb[x]

print(score)
