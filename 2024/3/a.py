import re
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()
# input = Path("ex2.txt").read_text()

muls = re.findall(r"(?i)mul\(\d+,\d+\)", input)


def mul(a, b):
    return a * b


s = 0
for m in muls:
    s += eval(m)

print(s)


# part 2

matches = []
for match in re.finditer(r"do\(\)", input):
    matches.append((match.start(), match.group()))

for match in re.finditer(r"don't\(\)", input):
    matches.append((match.start(), match.group()))

for match in re.finditer(r"(?i)mul\(\d+,\d+\)", input):
    matches.append((match.start(), match.group()))

matches = sorted(matches)

s = 0
DO = True
for _, a in matches:
    if a == "do()":
        DO = True
    elif a == "don't()":
        DO = False
    else:
        if DO:
            s += eval(a)

print(s)
