#!/usr/bin/env python3

import os
import random
from collections import defaultdict
from functools import reduce
from operator import mul
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")

lines = file.readlines()
lines = [line.strip().rstrip('.') for line in lines]


class Ingredient():
    def __init__(self, name, ingredient):
        self.props = ingredient
        self.name = name

    def totals(self, n_teaspoons):
        return tuple(map(lambda x: x*n_teaspoons, self.props))


class Mixer():
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def combine(self, quantities, target_calories=None):
        totals = []
        calories = []
        for (idx, q) in enumerate(quantities):
            t = self.ingredients[idx].totals(q)
            totals.append(t[:-1])
            calories.append(t[-1])
        result = [max(sum(t), 0) for t in zip(*totals)]
        total_calories = max(sum(calories), 0)

        if target_calories != None and total_calories != target_calories:
            return 0

        return reduce(mul, result)

    def count_ingredients(self):
        return len(self.ingredients)

    def generate_weights(self):
        n = self.count_ingredients()
        for t in itertools.combinations_with_replacement(range(101), n):
            if sum(t) == 100:
                yield from itertools.permutations(t)


M = Mixer()
for line in lines:
    name, values = line.split(":")
    values = [int(v.split(" ")[-1]) for v in values.strip().split(",")]
    i = Ingredient(name, values)
    M.add_ingredient(i)


scores = []
for quantities in M.generate_weights():
    score = M.combine(quantities)
    scores.append(score)

print("Part 1 answer:", max(scores))

scores = []
for quantities in M.generate_weights():
    score = M.combine(quantities, 500)
    scores.append(score)

print("Part 2 answer:", max(scores))
