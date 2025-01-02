from pathlib import Path

input = Path("i.txt").read_text()

input = list(map(int, input.strip().split()))

memo = {}


def blink(stone, k):
    if (stone, k) in memo:
        return memo[(stone, k)]
    if k == 0:
        ans = 1
    elif stone == 0:
        ans = blink(1, k - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        a, b = s[: len(s) // 2], s[len(s) // 2 :]
        ans = blink(int(a), k - 1) + blink(int(b), k - 1)
    else:
        ans = blink(stone * 2024, k - 1)

    memo[(stone, k)] = ans
    return ans


print(sum([blink(stone, 25) for stone in input]))

# part 2

print(sum([blink(stone, 75) for stone in input]))
