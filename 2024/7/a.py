from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
input = Path("ex.txt").read_text()

samples = defaultdict(list)

for line in input.splitlines():
    test, ns = line.split(": ")
    test = int(test)
    ns = list(map(int, ns.split()))
    samples[test] = ns


def valid_sample(test, ns) -> bool:
    n = ns[0]
    Q = [(test, n, [x for x in ns[1:]], [n])]

    while Q:
        target, current, remain, path = Q.pop(0)

        # print(target, current, remain, path)
        if target == current and len(remain) == 0:
            return True

        if len(remain) > 0:
            next_n = remain.pop(0)
            for op in ["+", "*"]:
                if op == "+":
                    new_current = current + next_n
                    Q.append((target, new_current, remain[:], path + [op, next_n]))
                elif op == "*":
                    new_current = current * next_n
                    Q.append((target, new_current, remain[:], path + [op, next_n]))

    return False


count = 0
for test, ns in samples.items():
    if valid_sample(test, ns):
        count += test

print(count)


# part 2


def valid_sample_b(test, ns) -> bool:
    n = ns[0]
    Q = [(test, n, [x for x in ns[1:]], [n])]

    while Q:
        target, current, remain, path = Q.pop(0)

        # print(target, current, remain, path)
        if target == current and len(remain) == 0:
            return True

        if len(remain) > 0:
            next_n = remain.pop(0)
            for op in ["+", "*", "||"]:
                if op == "+":
                    new_current = current + next_n
                    Q.append((target, new_current, remain[:], path + [op, next_n]))
                elif op == "*":
                    new_current = current * next_n
                    Q.append((target, new_current, remain[:], path + [op, next_n]))
                elif op == "||":
                    new_current = int(str(current) + str(next_n))
                    Q.append((target, new_current, remain[:], path + [op, next_n]))

    return False


count = 0
for test, ns in samples.items():
    if valid_sample_b(test, ns):
        count += test

print(count)
