#!/usr/bin/env python3

import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

print(sum([math.floor((int(l) / 3) - 2) for l in lines]))

masses = [int(l) for l in lines]

def calc_fuel(mass):
  fuel = math.floor(mass / 3) - 2
  if fuel <= 0:
    return 0
  else:
    return fuel + calc_fuel(fuel)

print(sum([calc_fuel(int(l)) for l in lines]))