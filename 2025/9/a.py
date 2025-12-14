from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()



points = [tuple(map(int, line.split(','))) for line in input.strip().splitlines()]
points = list(sorted([(r, c) for c,r in points]))

a, b = 0, len(points) - 1
best_coverage = 0

def calc_coverage(ar, ac, br, bc):
    return (abs(br - ar) + 1) * (abs(bc - ac) + 1)


while True:
    if a >= b:
        break
    ar, ac = points[a]
    
    bi = b 
    while bi > a:
        br, bc = points[bi]
        coverage = calc_coverage(ar, ac, br, bc)
        best_coverage = max(best_coverage, coverage)
        bi -= 1
    
    a += 1

print(best_coverage)

import shapely

points = [tuple(map(int, line.split(','))) for line in input.strip().splitlines()]
# points = list(sorted(points))
polygon = shapely.Polygon(points)
shapely.prepare(polygon)

a, b = 0, len(points) - 1
best_coverage = 0

while a < len(points):
    ax, ay = points[a]
    
    bi = b 
    while bi > a:
        bx, by = points[bi]
        
        corners = [(ax, ay), (ax, by), (bx, by), (bx, ay)]
        rect = shapely.Polygon(corners)
        
        if polygon.contains(rect):
            coverage = calc_coverage(ay, ax, by, bx)
            best_coverage = max(best_coverage, coverage)
        
        bi -= 1
    
    a += 1

print(best_coverage)
