#!/usr/bin/env python3

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")
# file = open(dir_path + "/test_input_2.txt", "r")

lines = file.readlines()
lines = [line.strip() for line in lines]
puzzle_input = int(lines[0])
# print(puzzle_input)


T = puzzle_input // 10
house_n = 1


def get_factors(n):
    x = 1
    factors = []
    while x ** 2 <= n:
        if n % x == 0:
            factors.append(x)
            factors.append(n // x)
        x += 1
    return factors


for house_n in range(1, T):
    # number of presents delivered is the sum of
    # the factors of the house number * 10
    factors = get_factors(house_n)
    presents = sum(factors)

    # print(f"House {house_n} got {presents * 10} presents")
    if presents > T:
        break


print("Part 1 answer:", house_n)

T = puzzle_input // 11
house_n = 1


for house_n in range(1, T):
    # number of presents delivered is the sum of
    # the factors of the house number * 10
    factors = get_factors(house_n)
    presents = sum([x for x in factors if house_n / x <= 50])

    # print(f"House {house_n} got {presents * 11} presents")
    if presents > T:
        break

print("Part 2 answer:", house_n)
