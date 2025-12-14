from functools import cache
from pathlib import Path
from shapely.geometry import Polygon
from shapely.affinity import rotate, translate
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPLPolygon


input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

class Present:
    def __init__(self, idx, shape_text):
        self.idx = idx
        self._shape = shape_text

    @staticmethod
    def from_text(text):
        lines = text.strip().split("\n")
        idx = int(lines[0].split(':')[0])
        shape_text = "\n".join(lines[1:])
        return Present(idx, shape_text)

    @property
    @cache
    def shape(self):
        p = Polygon()
        for y, line in enumerate(self._shape.strip().split("\n")):
            for x, c in enumerate(line):
                if c == "#":
                    p = p.union(Polygon([(x, y), (x+1, y), (x+1, y+1), (x, y+1)]))

        return p

    @property
    @cache
    def size(self):
        s = 0
        for line in self._shape.strip().split("\n"):
            for c in line:
                if c == "#":
                    s += 1
        return s

    @property
    @cache
    def rotations(self):
        rotations = []
        current = self.shape
        for angle in [0, 90, 180, 270]:
            rotated = rotate(current, angle, origin=(0, 0))
            minx, miny, _, _ = rotated.bounds
            normalized = translate(rotated, -minx, -miny)
            rotations.append(normalized)
            current = rotated

        unique = []
        for r in rotations:
            if not any(r.equals(u) for u in unique):
                unique.append(r)
        return unique
            

class Tree:
    def __init__(self, x, y, presents):
        self.x = x
        self.y = y
        self.presents = presents
        self.size = x * y

        self.grid = Polygon([(0, 0), (self.x, 0), (self.x, self.y), (0, self.y)])
        self.placed_shapes = []

    @staticmethod
    def from_text(text, present_catalog):
        size, reqs_text = text.strip().split(": ")
        x, y = map(int, size.split("x"))
        present_reqs = list(map(int, reqs_text.split(" ")))
        presents = [present_catalog[idx] for idx, qty in enumerate(present_reqs) for _ in range(qty)]
        return Tree(x, y, presents)

    def candidates(self, shape, step=1):
        candidates = []
        rotations = shape.rotations
        
        for rotated in rotations:
            for y in range(0, int(self.y) + 1, step):
                for x in range(0, int(self.x) + 1, step):
                    candidates.append((x, y, rotated))
        
        return candidates
    
    def can_place(self, shape, x, y):
        positioned = translate(shape, x, y)
        
        # in bounds
        if not self.grid.covers(positioned):
            return False
            
        for placed in self.placed_shapes:
            intersection = positioned.intersection(placed)
            # if intersection has area (not just boundary), shapes overlap - allows touching
            if intersection.area > 1e-9:  # Small epsilon for floating point
                return False
        
        return True
    
    def place(self, shape, x, y):
        positioned = translate(shape, x, y)
        self.placed_shapes.append(positioned)
        return positioned
    
    def remove_last(self):
        if self.placed_shapes:
            self.placed_shapes.pop()

    def pack(self, shapes, *, idx=0, k=0, max_k=1e4):

        total_size_placed = sum([s.size for s in shapes])

        if total_size_placed > self.size:
            return False
        
        # !@£(*&^%$#@! trollface
        if self.size >= total_size_placed * 1.25:
            return True
        
        if idx >= len(shapes):
            return True
        
        # no haz infinite loops
        if k > max_k:
            return False
        
        current_shape = shapes[idx]
        candidates = self.candidates(current_shape)
        for x, y, rotated in candidates:
            if self.can_place(rotated, x, y):
                self.place(rotated, x, y)
                
                # can haz all packed?
                if self.pack(shapes, idx=idx + 1, k=k + 1, max_k=max_k):
                    return True
                
                # backtrack
                self.remove_last()
        
        return False



blocks = input.strip().split("\n\n")
presents, trees = blocks[0:-1], blocks[-1]
presents = [Present.from_text(p) for p in presents]
presents = {p.idx: p for p in presents}
trees = [Tree.from_text(t, present_catalog=presents) for t in trees.strip().split("\n")]

def vizualize(tree):
    _, ax = plt.subplots(figsize=(8, 8))

    # Draw grid boundary
    grid_patch = MPLPolygon(list(tree.grid.exterior.coords), 
                            fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(grid_patch)

    # Draw placed shapes with different colors
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']
    for i, shape in enumerate(tree.placed_shapes):
        patch = MPLPolygon(list(shape.exterior.coords), 
                            alpha=0.5, facecolor=colors[i % len(colors)], 
                            edgecolor='black', linewidth=1)
        ax.add_patch(patch)

    ax.set_xlim(-1, tree.x + 1)
    ax.set_ylim(-1, tree.y + 1)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title(f'Shape Packing Result ({len(tree.placed_shapes)}/{len(tree.presents)} shapes)')
    plt.show()

count = 0
for tree in trees:
    success = tree.pack(tree.presents, max_k=1e5)
    if success:
        count += 1

print(count)