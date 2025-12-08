from functools import reduce
from operator import mul
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

ops = ('+', '*',)

lines = input.splitlines()
number_lines = lines[0:-1]
ops_line = lines[-1]

column_idx = {}

for i, o in enumerate(ops_line):
    if o == ' ':
        continue
    assert o in ops
    column_idx[i] = o

problems = []
cols = list(sorted(column_idx.keys()))
for i in range(len(cols)):
    a, b = i, i + 1
    

    if b >= len(cols):
        c1 = cols[a]
        ns = []
        for row in number_lines:
            n = int(row[c1:].strip())
            ns.append(n)

        problems.append((ns, column_idx[c1]))
    else: 
        c1 = cols[a]
        c2 = cols[b]
        ns = []
        for row in number_lines:
            n = int(row[c1:c2].strip())
            ns.append(n)

        problems.append((ns, column_idx[c1]))


def solve(problems):
    results = []
    for ns, op in problems:
        if op == '+':
            res = sum(ns)
        elif op == '*':
            res = reduce(mul, ns, 1)
        results.append(res)
    
    return results

print(sum(solve(problems)))


ns = {}
for i in range(len(number_lines[0])):
    n = ""
    for row in number_lines:
        if row[i] != ' ':
            n += row[i]
    if n:
        ns[i] = int(n)



problems = []
cols = list(sorted(column_idx.keys()))
for i in range(len(cols)):
    a, b = i, i + 1
    
    if b >= len(cols):
        op = column_idx[cols[a]]  
        opns = []
        for j in range(cols[a], len(number_lines[0])):
            if j in ns:
                opns.append(ns[j])
                    
        problems.append((opns, op))
    else: 
        op = column_idx[cols[a]]  
        opns = []
        for j in range(cols[a], cols[b]):
            if j in ns:
                opns.append(ns[j])
                    
        problems.append((opns, op))

print(sum(solve(problems)))