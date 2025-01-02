from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()


grid = input.splitlines()

D = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),  # N E S W
    (1, -1),
    (1, 1),
    (-1, 1),
    (-1, -1),  # NE SE SW NW
]

xs = set()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "X":
            xs.add((x, y))


def bounds(loc, grid):
    x, y = loc
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


count = 0
for loc in xs:
    x, y = loc
    for dx, dy in D:
        xx, yy = x + dx, y + dy
        w = "X"
        if not bounds((xx, yy), grid):
            continue
        if grid[yy][xx] == "M":
            w += "M"
            for chr in ["A", "S"]:
                xx, yy = xx + dx, yy + dy
                if bounds((xx, yy), grid) and grid[yy][xx] == chr:
                    w += chr

            if w == "XMAS":
                count += 1

print(count)


# part 2


alocs = set()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "A":
            alocs.add((x, y))

count = 0
for loc in alocs:
    x, y = loc

    NE, SE, SW, NW = D[4:]

    nesw = []
    nwse = []
    for dx, dy in D[4:]:
        xx, yy = x + dx, y + dy
        if not bounds((xx, yy), grid):
            break
        if grid[yy][xx] == "S" or grid[yy][xx] == "M":
            if (dx, dy) == NE or (dx, dy) == SW:
                nesw.append(grid[yy][xx])
            elif (dx, dy) == NW or (dx, dy) == SE:
                nwse.append(grid[yy][xx])

    if sorted(nesw) == ["M", "S"] and sorted(nwse) == ["M", "S"]:
        count += 1

print(count)
