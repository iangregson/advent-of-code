#!/usr/bin/env python3

import os
import math
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#   '1, 1',
#   '1, 6',
#   '8, 3',
#   '3, 4',
#   '5, 5',
#   '8, 9',
# ]

# print(input_txt)

class Point():
  def __init__(self, p=(0,0)):
    self.p = p
    self.id = str(p)
    
  @property
  def x(self):
    return int(self.p[0])
  @property
  def y(self):
    return int(self.p[1])

  def __str__(self):
    return str(self.id)

  def __iter__(self):
    for i in self.p:
      yield i

  def distance_from(self, other):
    x = abs(self.x - other.x)
    y = abs(self.y - other.y)
    return x + y

  def closest_others(self, others):
    distances = []
    for other in others:
      d = self.distance_from(other)
      distances.append((d, other))
    
    return sorted(distances, key=lambda x: x[0])

  def total_distance_to_all_others(self, others):
    distances = []
    for other in others:
      d = self.distance_from(other)
      distances.append(d)

    return sum(distances)


points = defaultdict()

for idx, line in enumerate(input_txt):
  p = tuple([int(i) for i in line.split(', ')])
  p = Point(p)
  points[p] = 0


class Grid():
  def __init__(self, points):
    self.points = points
    self.areas = defaultdict(int)
    self.rows = self.build_rows()

  @property
  def max_x(self):
    return max([p.x for p in self.points]) + 10
  
  @property
  def min_x(self):
    return min([p.x for p in self.points]) - 10
  
  @property
  def max_y(self):
    return max([p.y for p in self.points]) + 10
  
  @property
  def min_y(self):
    return min([p.x for p in self.points]) - 10
  
  @property
  def width(self):
    return len(self.rows[0])
  
  @property
  def height(self):
    return len(self.rows)
  
  def __iter__(self):
    for row in self.rows:
      yield "".join(row)
  def __str__(self):
    return "\n" + "\n".join(list(self)) + "\n"

  def build_rows(self):
    rows = [['.' for i in range(0, self.max_x)] for j in range(0, self.max_y)]
    for y, row in enumerate(rows):
      for x, char in enumerate(row):
        P = Point((x, y))
        closest_others = P.closest_others(self.points)
        smallest_distance, closest_point = closest_others[0]
        if closest_others[1][0] == smallest_distance:
          # there's a conflict
          rows[y][x] = '.'
        else:
          if P.id == closest_point.id:
            rows[y][x] = self.get_point_name(closest_point)
            self.areas[closest_point] += 1
          else:
            rows[y][x] = self.get_point_name(closest_point).lower()
            self.areas[closest_point] += 1
    return rows

  def get_point_name(self, point):
    point_names = {
      '(1, 1)': 'A',
      '(8, 3)': 'C',
      '(3, 4)': 'D',
      '(5, 5)': 'E',
      '(1, 6)': 'B',
      '(8, 9)': 'F',
    }

    if str(point) in point_names:
      return point_names[str(point)]
    else:
      return str(point)

  def largest_area(self):
    sorted_areas = list(sorted(self.areas.items(), key=lambda x: x[1]))
    return sorted_areas.pop()[1]
  
  def largest_finite_area(self):
    sorted_areas = list(sorted(self.areas.items(), key=lambda x: x[1]))
    largest = 0
    for point, area in self.areas.items():
      if self.is_finite(point) and area > largest:
        largest = area
      
    return largest

  
  def is_finite(self, point):
    infinite_x = False
    infinite_y = False

    infinite_x = self.rows[point.y][0].lower() == self.get_point_name(point).lower() or self.rows[point.y][-1].lower() == self.get_point_name(point).lower()
    infinite_y = self.rows[0][point.x].lower() == self.get_point_name(point).lower() or self.rows[-1][point.x].lower() == self.get_point_name(point).lower()

    return not infinite_x and not infinite_y

  def optimum_region_size(self, optimum_size=32):
    points_in_optimum_region = []
    for y, row in enumerate(self.rows):
      for x, char in enumerate(row):
        P = Point((x, y))
        total_distance = P.total_distance_to_all_others(self.points)
        if total_distance < optimum_size:
          points_in_optimum_region.append(P)

    return len(points_in_optimum_region)




G = Grid(points)
# print(G)

print("Part 1 answer:", G.largest_finite_area())
print("Part 2 answer:", G.optimum_region_size(10000))
