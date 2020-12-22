#!/usr/bin/env python3

import os
from collections import namedtuple, defaultdict


dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
#   'trh fvjkl sbzzf mxmxvkd (contains dairy)',
#   'sqjhc fvjkl (contains soy)',
#   'sqjhc mxmxvkd sbzzf (contains fish)',
# ]

Food = namedtuple('Food', ['ingredients', 'allergens'])

def parse_line(line):
  ingredients, allergens = line.split(' (')
  ingredients = ingredients.split()
  allergens = [s.replace(',', '') for s in allergens[:-1].split()[1:]]
  
  return Food(ingredients, allergens)

foods = [parse_line(line) for line in lines]

all_allergens = set()
all_ingredients = set()
for food in foods:
  all_ingredients = all_ingredients | set(food.ingredients)
  all_allergens = all_allergens | set(food.allergens)
  # print(food)

# print()
# print(all_ingredients)
# print(all_allergens)

allergens_ingredients_map = {}
ingredients_w_potential_allergens = set()
for allergen in all_allergens:
  allergens_ingredients_map[allergen] = set()
  for food in foods:
    if allergen in food.allergens:
      if len(allergens_ingredients_map[allergen]) == 0:
        allergens_ingredients_map[allergen] = set(food.ingredients)
      else:
        allergens_ingredients_map[allergen] = allergens_ingredients_map[allergen] & set(food.ingredients)
  ingredients_w_potential_allergens = ingredients_w_potential_allergens | allergens_ingredients_map[allergen]
    
ingredients_wout_potential_allergens = all_ingredients - ingredients_w_potential_allergens
# print(ingredients_w_potential_allergens)
# print(ingredients_wout_potential_allergens)

count = 0
for ingredient in ingredients_wout_potential_allergens:
  for food in foods:
    if ingredient in food.ingredients:
      count += 1

print('Part 1:', count)

# print()
# print(allergens_ingredients_map)
final_allergens_ingredients_map = {}
while len(final_allergens_ingredients_map.keys()) < len(allergens_ingredients_map.keys()):
  for allergen in allergens_ingredients_map:
    if len(allergens_ingredients_map[allergen]) == 1:
      final_allergens_ingredients_map[allergen] = allergens_ingredients_map[allergen]
    else:
      for known_allergen in final_allergens_ingredients_map:
        allergens_ingredients_map[allergen] = allergens_ingredients_map[allergen] - final_allergens_ingredients_map[known_allergen]

canonical_dangerous_ingredients = ''
for allergen in sorted(final_allergens_ingredients_map):
  ingredient = list(final_allergens_ingredients_map[allergen])[0]
  # print(allergen, ingredient)
  canonical_dangerous_ingredients += ingredient + ','


print('Part 2:', canonical_dangerous_ingredients[:-1])

