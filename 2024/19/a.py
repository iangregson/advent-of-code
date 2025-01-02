from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

valid_designs, target_designs = input.split("\n\n")

valid_designs = set(valid_designs.split(', '))
target_designs = list(target_designs.splitlines())

idx_valid_designs = defaultdict(set[str])

for valid_design in valid_designs:
    idx_valid_designs[len(valid_design)].add(valid_design)

def validate_design(design: str) -> bool:
    seen = set()
    Q = [(design, "")]

    while Q:
        d, p = Q.pop()

        if len(d) == 0:
            return True

        for i, vds in idx_valid_designs.items():
            if i > len(d):
                continue

            for vd in vds:
                if d.startswith(vd) and p + vd not in seen:
                    seen.add(p + vd)
                    Q.append((d[len(vd):], p + vd))


approved_designs = [t for t in target_designs if validate_design(t)]
print(len(approved_designs))

# part 2
char_idx_valid_designs = defaultdict(set[str])
for valid_design in valid_designs:
    a = valid_design[0]
    char_idx_valid_designs[a].add(valid_design)

memo = {}
def valid_design_options(design) -> int:
    if design in memo:
        return memo[design]
    
    c = 0 

    if len(design) == 0:
        c = 1
    else:
        a = design[0]

        for vd in char_idx_valid_designs[a]:
            if design.startswith(vd):
                c += valid_design_options(design[len(vd):])
    
    memo[design] = c
    return c


print(sum(valid_design_options(d) for d in approved_designs))