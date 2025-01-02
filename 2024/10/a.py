from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()


class IntGrid:
    def __init__(self, input):
        self.grid = [[int(c) for c in r] for r in input.splitlines()]
        self.W = len(self.grid[0])
        self.H = len(self.grid)

    def in_bounds(self, p):
        x, y = p
        return 0 <= x < self.W and 0 <= y < self.H

    def __str__(self):
        return "\n".join("".join(str(c) for c in r) for r in self.grid)

    def __repr__(self) -> str:
        return self.__str__()

    def loc(self, p):
        x, y = p
        return self.grid[y][x]


g = IntGrid(input)

trailheads = set()
for y in range(g.H):
    for x in range(g.W):
        if g.loc((x, y)) == 0:
            trailheads.add((x, y))

# print(trailheads)


def walk_trail(trailhead, target, increment, grid):
    peaks = set()
    trails = set()
    Q = [(trailhead, [])]

    while Q:
        p, visited = Q.pop()
        visited.append(p)

        h = grid.loc(p)
        if h == target:
            peaks.add(p)
            trails.add(f"{visited}")
            continue

        x, y = p
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_p = (x + dx, y + dy)
            if grid.in_bounds(new_p):
                new_h = grid.loc(new_p)
                if new_h == h + increment:
                    Q.append((new_p, visited))

    return len(peaks), len(trails)


scores = []
ratings = []
for trailhead in trailheads:
    score, rating = walk_trail(trailhead, 9, 1, g)
    scores.append(score)
    ratings.append(rating)

print(sum(scores))
print(sum(ratings))
