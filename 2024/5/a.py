from collections import defaultdict
from functools import lru_cache
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

rules, updates = input.split("\n\n")

rules_before = defaultdict(list)
rules_after = defaultdict(list)

for rule in rules.splitlines():
    l, r = rule.split("|")
    rules_before[l].append(r)
    rules_after[r].append(l)


@lru_cache
def is_before(n, k, ns):
    ni = ns.index(n)
    try:
        ki = ns.index(k)
        return ni < ki
    except ValueError:
        return True


@lru_cache
def is_after(n, k, ns):
    ni = ns.index(n)
    try:
        ki = ns.index(k)
        return ni > ki
    except ValueError:
        return True


def has_error(update):
    for entry in update:
        if entry in rules_before:
            for rule in rules_before[entry]:
                if not is_before(entry, rule, tuple(update)):
                    return (True, entry, rule)
        if entry in rules_after:
            for rule in rules_after[entry]:
                if not is_after(entry, rule, tuple(update)):
                    return (True, entry, rule)
    return (False, None, None)


count = 0
for update in updates.splitlines():
    ns = update.split(",")
    mid = len(ns) // 2
    if not has_error(ns)[0]:
        count += int(ns[mid])


print(count)


# part 2

incorrect_updates = []
for update in updates.splitlines():
    ns = update.split(",")
    err, entry, rule = has_error(ns)
    if err:
        incorrect_updates.append((ns, entry, rule))


def do_swap(ns, entry, rule):
    i = ns.index(entry)
    j = ns.index(rule)
    ns[i], ns[j] = rule, entry
    return ns


count = 0
for update in incorrect_updates:
    ns, entry, rule = update
    ns = do_swap(ns, entry, rule)
    err, entry, rule = has_error(ns)
    while err:
        ns = do_swap(ns, entry, rule)
        err, entry, rule = has_error(ns)

    mid = len(ns) // 2
    count += int(ns[mid])

print(count)
