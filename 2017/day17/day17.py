step = 363
# step = 3

buf = [0]
pos = 0
total = 1

for i in range(1, 50000001):
    pos = (pos + step) % total
    pos += 1
    if pos == 1:
        answer = i
    total += 1

print(answer)
