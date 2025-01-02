from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()


def validate(report):
    deltas = []
    errors = 0
    for i in range(0, len(report) - 1):
        a, b = report[i], report[i + 1]
        if not 1 <= abs(b - a) <= 3:
            errors += 1
        delta = b - a
        deltas.append((delta, errors))

    all_increasing = all(delta > 0 for delta, _ in deltas)
    all_descending = all(delta < 0 for delta, _ in deltas)

    return (all_increasing or all_descending) and errors == 0


count = 0
for report in input.splitlines():
    levels = list(map(int, report.split()))

    valid = validate(levels)

    if valid:
        count += 1
        continue

print(count)


# part 2

count = 0
for report in input.splitlines():
    levels = list(map(int, report.split()))

    valid = validate(levels)

    if valid:
        count += 1
        continue

    for i in range(0, len(levels)):
        new_report = levels[:]
        new_report.pop(i)
        valid = validate(new_report)
        if valid:
            count += 1
            break


print(count)
