from dataclasses import dataclass
from functools import cache
from pathlib import Path

from z3 import Int, Solver, sat

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()


@dataclass
class Game:
    A: tuple[int, int]
    B: tuple[int, int]
    prize: tuple[int, int]
    winnable = True

    def __init__(self, input) -> None:
        a_line, b_line, prize_line = input.splitlines()
        _, a_line = a_line.split(": ")
        ax, ay = [int(x[2:]) for x in a_line.split(", ")]
        self.A = (ax, ay)
        _, b_line = b_line.split(": ")
        bx, by = [int(x[2:]) for x in b_line.split(", ")]
        self.B = (bx, by)
        _, prize_line = prize_line.split(": ")
        px, py = [int(x[2:]) for x in prize_line.split(", ")]
        self.prize = int(px), int(py)

    @cache
    @staticmethod
    def step(A, B, prize):
        ax, ay = A
        bx, by = B
        px, py = prize
        if px == 0 and py == 0:
            return 0
        if px < 0 or py < 0:
            return float("inf")
        return min(
            3 + Game.step(A, B, (px - ax, py - ay)),
            1 + Game.step(A, B, (px - bx, py - by)),
        )

    def play(self):
        winning_game_cost = Game.step(self.A, self.B, self.prize)
        if winning_game_cost == float("inf"):
            return 0

        return winning_game_cost

    def solve(self):
        solver = Solver()

        ap, bp = Int("a"), Int("b")
        solver.add(ap >= 0)
        solver.add(bp >= 0)

        ax, ay = self.A
        bx, by = self.B
        px, py = self.prize
        solver.add(ap * ax + bp * bx == px)
        solver.add(ap * ay + bp * by == py)

        if solver.check() == sat:
            model = solver.model()
            a_value = model.evaluate(ap).as_long()
            b_value = model.evaluate(bp).as_long()

            tokens = a_value * 3 + b_value
            return tokens
        else:
            return 0


cost = 0
for block in input.split("\n\n"):
    g = Game(block)
    cost += g.play()

print(cost)


# part 2
# give up and use a sat solver
cost = 0
for block in input.split("\n\n"):
    g = Game(block)
    px, py = g.prize
    g.prize = (int(px+1e13), int(py+1e13))
    cost += g.solve()

print(cost)
