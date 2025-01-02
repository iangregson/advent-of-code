from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex1.txt").read_text()
# input = Path("ex2.txt").read_text()
# input = Path("ex3.txt").read_text()


class Garden:
    def __init__(self, input):
        self.rows = [list(row) for row in input.splitlines()]
        self.H = len(self.rows)
        self.W = len(self.rows[0])

    def bounds(self, loc):
        x, y = loc
        return 0 <= x < self.W and 0 <= y < self.H

    def plot(self, loc):
        x, y = loc
        return self.rows[y][x]

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.rows)


@dataclass
class Region:
    plots: set
    plant: str

    def __init__(self, plant, plots=set()) -> None:
        self.plant = plant
        self.plots = plots

    def area(self):
        return len(self.plots)

    def perimeter(self):
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perimeter = 0
        for x, y in self.plots:
            for dx, dy in D:
                if (x + dx, y + dy) not in self.plots:
                    perimeter += 1
        return perimeter

    def sides(self):
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perimeter = defaultdict(set)
        for x, y in self.plots:
            for dx, dy in D:
                if (x + dx, y + dy) not in self.plots:
                    perimeter[(dx, dy)].add((x + dx, y + dy))

        sides = 0
        for _, ps in perimeter.items():
            seen = set()
            for x, y in ps:
                if (x, y) not in seen:
                    sides += 1
                    Q = [(x, y)]
                    while Q:
                        X, Y = Q.pop(0)
                        if (X, Y) in seen:
                            continue
                        seen.add((X, Y))
                        for dx, dy in D:
                            xx, yy = X + dx, Y + dy
                            if (xx, yy) in ps:
                                Q.append((xx, yy))

        return sides

    def __str__(self) -> str:
        return f"{list(sorted(self.plots))}"


g = Garden(input)

plants = defaultdict(set)
regions = defaultdict(list)
seen = set()
for y in range(g.H):
    for x in range(g.W):
        if (x, y) in seen:
            continue
        p = g.plot((x, y))
        r = Region(p, {(x, y)})
        Q = [(x, y, r)]
        while Q:
            X, Y, R = Q.pop(0)
            if (X, Y) in seen:
                continue

            P = g.plot((X, Y))
            plants[P].add((X, Y))
            seen.add((X, Y))
            if P == R.plant:
                R.plots.add((X, Y))

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                xx, yy = X + dx, Y + dy
                if (
                    g.bounds((xx, yy))
                    and g.plot((xx, yy)) == p
                    and (xx, yy) not in seen
                ):
                    Q.append((xx, yy, R))
        regions[p].append(r)

price = 0
for plant, pregions in regions.items():
    for r in pregions:
        price += r.area() * r.perimeter()

print(price)

# Part 2

price = 0
for plant, pregions in regions.items():
    for r in pregions:
        price += r.area() * r.sides()

print(price)
