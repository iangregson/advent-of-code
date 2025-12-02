import re
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

ranges = [tuple([int(x) for x in r.split("-")]) for r in input.strip().split(",")]

def valid_a(n):
    sn = str(n)
    assert sn[0] != "0"
    if re.match(r'^(\d+)\1$', sn): # https://regex101.com/r/Po8oaj/1
        return False
    
    return True

def valid_b(n):
    sn = str(n)
    assert sn[0] != "0"
    if re.match(r'^(\d+)\1+$', sn): # https://regex101.com/r/Po8oaj/2
        return False
    
    return True

invalid_ids = set()
for (a, b) in ranges:
    for i in range(a, b + 1):
        if not valid_a(i):
            invalid_ids.add(i)

print(sum(invalid_ids))

invalid_ids = set()
for (a, b) in ranges:
    for i in range(a, b + 1):
        if not valid_b(i):
            invalid_ids.add(i)

print(sum(invalid_ids))