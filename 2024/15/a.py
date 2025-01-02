from functools import reduce
from operator import iconcat
from collections import defaultdict, deque
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()
# input = Path("ex2.txt").read_text()
# input = Path("ex3.txt").read_text()

grid, moves = input.split('\n\n')

moves = list(reduce(iconcat, moves.splitlines()))

class Grid:
    W: int
    H: int
    D = { '^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0) }

    def __init__(self, input):
        self._grid = [list(row) for row in input.splitlines()]
        self.W = len(self._grid[0])
        self.H = len(self._grid)
        self.walls = set()
        self.boxes = set()
        self.robot = (0,0)
        for y in range(self.H):
            for x in range(self.W):
                if self._grid[y][x] == 'O':
                    self.boxes.add((x, y))
                elif self._grid[y][x] == '#':
                    self.walls.add((x, y))
                elif self._grid[y][x] == '@':
                    self.robot = (x, y)


    def bounds(self, x, y):
        if (x,y) in self.walls:
            return False
        return 0 <= x < self.W and 0 <= y < self.H

    def __str__(self):
        grid = []
        for y in range(self.H):
            line = ""
            for x in range(self.W):
                if (x,y) in self.walls:
                    line += "#"
                elif (x,y) in self.boxes:
                    line += "O"
                elif (x,y) == self.robot:
                    line += "@"
                else:
                    line += "."
            grid.append(line)
        return "\n".join(grid)

    def __repr__(self):
        return self.__str__()

    def loc(self, x, y):
        if not self.bounds(x,y):
            return None
        if (x,y) in self.walls:
            return "#"
        elif (x,y) in self.boxes:
            return "O"
        elif (x,y) == self.robot:
            return "@"
        else:
            return "."

    def npos(self, direction, x, y):
        d = self.D[direction]

        dx, dy = d
        nx, ny = x+dx, y+dy
        n = (nx, ny)

        return n


    def nloc(self, direction, x, y):
        nx, ny = self.npos(direction, x, y)
        if not self.bounds(nx,ny):
            return None
        if (nx,ny) in self.walls:
            return "#"
        elif (nx,ny) in self.boxes:
            return "O"
        elif (nx,ny) == self.robot:
            return "@"
        else:
            return "."

    def move_boxes(self, direction, x, y):
        dx, dy = self.D[direction]
        px, py = x, y
        # advance to next free space
        free_space = None
        while self.bounds(px, py):
            px, py = px + dx, py + dy
            if self.loc(px, py) == ".":
                free_space = (px, py)
                break

        if free_space is None:
            return

        assert(self.loc(*free_space) == '.')

        # work back from free space
        target = (x, y)
        while free_space != target:
            px, py = free_space
            xx, yy = px-dx, py-dy
            assert(self.loc(xx,yy) == 'O')
            self.boxes.remove((xx, yy))
            self.boxes.add((px, py))
            assert(self.loc(xx,yy) == '.')
            px, py = xx, yy
            free_space = (px, py)

        assert(self.loc(x,y) == '.')

    def move_robot(self, direction):
        n = self.npos(direction, *self.robot)

        if not self.bounds(*n):
            return

        if self.nloc(direction, *self.robot) == '.':
            self.robot = self.npos(direction, *self.robot)
            return

        if self.nloc(direction, *self.robot) == 'O':
            boxp = self.npos(direction, *self.robot)
            self.move_boxes(direction, *boxp)

            if self.loc(*boxp) == '.':
                self.robot = boxp
                return

    def sum_gps(self):
        return sum([x + y*100 for x,y in self.boxes])


g = Grid(grid)
print(moves)
for move in moves:
    g.move_robot(move)
print(g)
print(g.sum_gps())

# part 2

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()
# input = Path("ex2.txt").read_text()
# input = Path("ex3.txt").read_text()

grid, moves = input.split('\n\n')

moves = list(reduce(iconcat, moves.splitlines()))

class BigGrid:
    W: int
    H: int
    D = { '^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0) }

    def __init__(self, input):
        self._grid = []
        for line in input.splitlines():
            row = ""
            for c in line:
                if c == '.':
                    row += '..'
                elif c == '@':
                    row += '@.'
                elif c == 'O':
                    row += '[]'
                elif c == '#':
                    row += '##'
            self._grid.append(row)
        self.W = len(self._grid[0])
        self.H = len(self._grid)
        self.walls = set()
        self.boxes = defaultdict(str)
        self.robot = (0,0)
        for y in range(self.H):
            for x in range(self.W):
                if self._grid[y][x] == '[':
                    self.boxes[(x,y)] = '['
                elif self._grid[y][x] == ']':
                    self.boxes[(x,y)] = ']'
                elif self._grid[y][x] == '#':
                    self.walls.add((x, y))
                elif self._grid[y][x] == '@':
                    self.robot = (x, y)


    def bounds(self, x, y):
        if (x,y) in self.walls:
            return False
        return 0 <= x < self.W and 0 <= y < self.H

    def __str__(self):
        grid = []
        for y in range(self.H):
            line = ""
            for x in range(self.W):
                if (x,y) in self.walls:
                    line += "#"
                elif (x,y) in self.boxes:
                    line += self.boxes[(x,y)]
                elif (x,y) == self.robot:
                    line += "@"
                else:
                    line += "."
            grid.append(line)
        return "\n".join(grid)

    def __repr__(self):
        return self.__str__()

    def loc(self, x, y):
        if not self.bounds(x,y):
            return None
        if (x,y) in self.walls:
            return "#"
        elif (x,y) in self.boxes:
            return self.boxes[(x,y)]
        elif (x,y) == self.robot:
            return "@"
        else:
            return "."

    def npos(self, direction, x, y):
        d = self.D[direction]

        dx, dy = d
        nx, ny = x+dx, y+dy
        n = (nx, ny)

        return n


    def nloc(self, direction, x, y):
        nx, ny = self.npos(direction, x, y)
        if not self.bounds(nx,ny):
            return None
        if (nx,ny) in self.walls:
            return "#"
        elif (nx,ny) in self.boxes:
            return self.boxes[(nx,ny)]
        elif (nx,ny) == self.robot:
            return "@"
        else:
            return "."

    def move_boxes(self, direction, x, y):
        px, py = x, y
        assert self.loc(px, py) in {'[', ']'}

        # gather up all the boxes
        print(f"moving boxes from {x}, {y}, direction: {direction}")
        boxes = set()
        visited = set()
        blocked = False
        Q = [(px, py)]
        while Q:
            p = Q.pop(0)
            if p in visited:
                continue
            visited.add(p)
            px, py = p
            l, r = None, None
            if self.loc(px, py) == ']':
                r = (px, py)
                l = (px-1, py)
            elif self.loc(px, py) == '[':
                l = (px, py)
                r = (px+1, py)
            if l is not None and r is not None:           
                nl = self.npos(direction, *l)
                nr = self.npos(direction, *r)
                # if the next position is out of bounds, the move can't happen
                if not self.bounds(*nl) or not self.bounds(*nr):
                    blocked = True
                    break
                else:
                    boxes.add((l, r))
                    Q.append(nl)
                    Q.append(nr)

        if blocked:
            return
        
        boxes = deque(list(boxes))
        assert len(boxes) > 0

        # try to move all the boxes and quit if any hit a wall
        while boxes:
            box = boxes.popleft()
            l, r = box
            assert l in self.boxes and r in self.boxes
            # fail if wall blocks an edge
            if not self.bounds(*self.npos(direction, *r)) or not self.bounds(*self.npos(direction, *l)):
                # rollback
                assert False # this should not happen - should have been caught at `blocked` above
            # if either edge is blocked by another box, put this one back
            # this gets things in to the right order
            if direction in {'^', 'v'}:
                if self.is_box(*self.npos(direction, *l)) or self.is_box(*self.npos(direction, *r)):
                    boxes.append(box)
                    continue
            elif direction == '>':
                if self.is_box(*self.npos(direction, *r)):
                    boxes.append(box)
                    continue
            elif direction == '<':
                if self.is_box(*self.npos(direction, *l)):
                    boxes.append(box)
                    continue
            else:
                raise ValueError(f"unknown direction {direction}")
            
            # move the box and keep an undo list
            nl, nr = self.npos(direction, *l), self.npos(direction, *r)
            del self.boxes[l]
            del self.boxes[r]
            self.boxes[nl] = '['
            self.boxes[nr] = ']'

        # if we got this far, there should be a free space
        assert(self.is_free(x,y))

    def is_box(self, x, y):
        return self.loc(x,y) in {'[', ']'}
    
    def is_free(self, x, y):
        return self.loc(x,y) == '.'

    def move_robot(self, direction):
        n = self.npos(direction, *self.robot)

        if not self.bounds(*n):
            return
        

        if self.nloc(direction, *self.robot) == '.':
            self.robot = self.npos(direction, *self.robot)
            return

        if self.is_box(*self.npos(direction, *self.robot)):
            boxp = self.npos(direction, *self.robot)
            self.move_boxes(direction, *boxp)

            if self.loc(*boxp) == '.':
                self.robot = boxp
                return

    def sum_gps(self):
        return sum([x + y*100 for x,y in self.boxes if self.boxes[(x,y)] == '['])


g = BigGrid(grid)
print(moves)
print(g)
for move in moves:
    g.move_robot(move)
print(g)
print(g.sum_gps())
