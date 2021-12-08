#!/usr/bin/env python3

import os
import statistics

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
ints = [int(n) for n in file.read().strip().split(',')]

# ints = [16,1,2,0,4,2,7,1,2,14]

median = statistics.median(sorted(ints))
fuel_costs = int(sum([abs(n-median) for n in ints]))

print(fuel_costs)

def fuel_calculator(start, finish):
  distance = abs(finish - start)
  return sum(range(1, distance + 1))

mean = round(statistics.mean(sorted(ints)))
fuel_costs = sum([fuel_calculator(mean, n) for n in ints])
print(fuel_costs)

all_fuel_costs = []
for i in range(min(ints), max(ints)):
  fuel_costs = sum([fuel_calculator(i, n) for n in ints])
  all_fuel_costs.append(fuel_costs)

print(min(all_fuel_costs))