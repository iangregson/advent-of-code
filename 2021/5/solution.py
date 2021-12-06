#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [l.strip() for l in file.readlines()]

# lines = [
#   '0,9 -> 5,9',
#   '8,0 -> 0,8',
#   '9,4 -> 3,4',
#   '2,2 -> 2,1',
#   '7,0 -> 7,4',
#   '6,4 -> 2,0',
#   '0,9 -> 2,9',
#   '3,4 -> 1,4',
#   '0,0 -> 8,8',
#   '5,5 -> 8,2',
# ]

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f"{self.x},{self.y}"

class Line():
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __str__(self):
    return f"{self.start} -> {self.end}"

  def has_point(self, point):
    min_x = min([self.start.x, self.end.x])
    max_x = max([self.start.x, self.end.x])
    min_y = min([self.start.y, self.end.y])
    max_y = max([self.start.y, self.end.y])
    return point.x >= min_x and point.x <= max_x and point.y >= min_y and point.y <= max_y

  def points(self):
    points = []
    min_x = min([self.start.x, self.end.x])
    max_x = max([self.start.x, self.end.x])
    min_y = min([self.start.y, self.end.y])
    max_y = max([self.start.y, self.end.y])
    
    if self.start.x == self.end.x or self.start.y == self.end.y:
      # horizontal or vertical lines
      for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
          points.append(Point(x, y))
    else:
      if self.start.x > self.end.x:
        self.start.x, self.end.x = self.end.x, self.start.x
        self.start.y, self.end.y = self.end.y, self.start.y
      x_delta = int((self.end.x - self.start.x) / abs(self.end.x - self.start.x))
      y_delta = int((self.end.y - self.start.y) / abs(self.end.y - self.start.y))

      x = self.start.x
      y = self.start.y
      while x <= self.end.x:
        points.append(Point(x, y))
        x += x_delta
        y += y_delta
    
    return points

lines = [line.split(' -> ') for line in lines]
lines = list(map(lambda line: [[int(p) for p  in pos.split(',')] for pos in line], lines))
lines = list(map(lambda line: Line(Point(*line[0]), Point(*line[1])), lines))
# only horizontal and vertical (for now)
lines_pt1 = [line for line in lines if line.start.x == line.end.x or line.start.y == line.end.y]

points_visited = defaultdict(int)
for line in lines_pt1:
  for point in line.points():
    points_visited[point.x, point.y] += 1

print(len([count for count in points_visited.values() if count >= 2]))

points_visited = defaultdict(int)
for line in lines:
  # print(line)
  for point in line.points():
    # print(point)
    points_visited[point.x, point.y] += 1

# print(points_visited)
print(len([count for count in points_visited.values() if count >= 2]))