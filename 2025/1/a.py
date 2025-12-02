from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

instructions = [line.strip() for line in input.splitlines() if line.strip()]
instructions = [(line[0], int(line[1:])) for line in instructions]

dial_min = 0
dial_max = 99
dial = 50
count_zero = 0
count_click = 0 

for d, amount in instructions:
    for i in range(amount):
        if d == 'L':
            dial = (dial-1+100)%100
            if dial == 0:
                count_click += 1
        elif d == 'R':
            dial = (dial+1)%100
            if dial == 0:
                count_click += 1

    if dial == 0:
        count_zero += 1


print(count_zero, count_click)
