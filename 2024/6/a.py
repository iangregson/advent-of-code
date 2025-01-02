from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

grid = [list(x) for x in input.splitlines()]

start = (0, 0)


def bounds(x, y, g):
    W, H = len(g[0]), len(g)
    return 0 <= x < W and 0 <= y < H


for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "^":
            start = (x, y)
            break


D = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

visited = set()
Q = [(start, D[0])]

while Q:
    (x, y), (dx, dy) = Q.pop(0)
    visited.add((x, y))

    xx, yy = x + dx, y + dy

    if not bounds(xx, yy, grid):
        break

    if grid[yy][xx] != "#":
        Q.append(((xx, yy), (dx, dy)))
    else:
        new_d = D[(D.index((dx, dy)) + 1) % len(D)]
        Q.append(((x, y), new_d))

print(len(visited))


# part 2


def patrol(pos, d, grid):
    visited = set()
    Q = [(pos, d)]

    while Q:
        (x, y), (dx, dy) = Q.pop(0)

        if ((x, y), (dx, dy)) in visited:
            return (visited, True)

        visited.add(((x, y), (dx, dy)))

        xx, yy = x + dx, y + dy

        if not bounds(xx, yy, grid):
            break

        if grid[yy][xx] != "#" and grid[yy][xx] != "O":
            Q.append(((xx, yy), (dx, dy)))
        else:
            new_d = D[(D.index((dx, dy)) + 1) % len(D)]
            Q.append(((x, y), new_d))

    return visited, False


visited, _ = patrol(start, D[0], grid)
marks = set()
for step in visited:
    pos, d = step
    grid = [list(row) for row in input.splitlines()]

    x, y = pos
    dx, dy = d
    xx, yy = x + dx, y + dy
    if bounds(xx, yy, grid):
        grid[yy][xx] = "O"

    vs, cycled = patrol(start, D[0], grid)
    if cycled:
        marks.add((xx, yy))


print(len(marks))
