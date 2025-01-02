import numpy as np
from scipy import ndimage
from collections import defaultdict
from functools import reduce
from operator import mul
from pathlib import Path

input = Path("i.txt").read_text()
size = (101, 103)

# input = Path("ex.txt").read_text()
# size = (11, 7)

seconds = 100
robots = []
for line in input.splitlines():
    p, v = line.split(" ")
    p, v = eval(p[2:]), eval(v[2:])
    robots.append((p, v))


def bounds(x, limit):
    return 0 <= x < limit


for second in range(seconds):
    for i, robot in enumerate(robots):
        p, v = robot
        x, y = p
        vx, vy = v
        x += vx
        y += vy
        sx, sy = size
        if not bounds(x, sx):
            if x < 0:
                x = sx + x
            elif x >= sx:
                x = x - sx
        if not bounds(y, sy):
            if y < 0:
                y = sy + y
            elif y >= sy:
                y = y - sy
        robots[i] = ((x, y), v)

def render(robots, size):
    robot_p = set([robot[0] for robot in robots])
    rows = []
    X, Y = size
    for y in range(Y):
        row = ""
        for x in range(X):
            if (x, y) in robot_p:
                row += "#"
            else:
                row += "."
        rows.append(row)
    return "\n".join(rows)

quads = defaultdict(int)

for robot in robots:
    sx, sz = size
    midx = sx // 2
    midy = sz // 2

    p, v = robot
    x, y = p
    if x < midx and y < midy:
        quads[0] += 1
        continue
    if x > midx and y < midy:
        quads[1] += 1
        continue
    if x > midx and y > midy:
        quads[2] += 1
        continue
    if x < midx and y > midy:
        quads[3] += 1
        continue

print(reduce(mul, quads.values()))


# part 2

seconds = int(1e5)
robots = []
for line in input.splitlines():
    p, v = line.split(" ")
    p, v = eval(p[2:]), eval(v[2:])
    robots.append((p, v))

def is_interesting(f):
    binary_grid = np.array([[1 if char == '#' else 0 for char in row] for row in f])
    
    # Label connected components
    labeled_array, num_components = ndimage.label(binary_grid)
    
    # Analyze component properties
    def analyze_component(component_label):
        component_mask = (labeled_array == component_label)
        component_pixels = np.sum(component_mask)
        component_height = np.sum(np.any(component_mask, axis=1))
        component_width = np.sum(np.any(component_mask, axis=0))
        return component_pixels, component_height, component_width
    
    # Check for Christmas tree-like characteristics
    tree_candidates = []
    for label in range(1, num_components + 1):
        pixels, height, width = analyze_component(label)
        
        # Heuristics for Christmas tree:
        # 1. Triangular or pyramid-like shape (narrow at top, wider at bottom)
        # 2. Reasonable size (not too small, not too large)
        # 3. Height-to-width ratio suggests a tree
        aspect_ratio = height / width if width > 0 else 0
        
        if (aspect_ratio > 1.5 and  # Tall and narrow
            pixels > 10 and          # Minimum size
            pixels < 100 and         # Maximum size
            width < height):         # Wider at bottom
            tree_candidates.append(label)
    
    return len(tree_candidates) > 0

for second in range(seconds):
    for i, robot in enumerate(robots):
        p, v = robot
        x, y = p
        vx, vy = v
        x += vx
        y += vy
        sx, sy = size
        if not bounds(x, sx):
            if x < 0:
                x = sx + x
            elif x >= sx:
                x = x - sx
        if not bounds(y, sy):
            if y < 0:
                y = sy + y
            elif y >= sy:
                y = y - sy
        robots[i] = ((x, y), v)

    f = render(robots, size)
    if is_interesting(f):
        print(f)
        print(second+1)
        break


