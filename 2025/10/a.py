from pathlib import Path
from z3 import *

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

lines = input.splitlines()

class Machine:
    def __init__(self, lights, wiring, joltage):     
        self.lights = lights
        self.wiring = wiring
        self.joltage = joltage

    @staticmethod
    def from_line(line):
        parts = line.split(" ")
        lights = tuple(parts[0][1:-1])
        wiring = [tuple(part[1:-1].split(",")) for part in parts[1:-1]]
        joltage = tuple(parts[-1][1:-1].split(","))

        wiring = [tuple(int(x) for x in wire) for wire in wiring]
        joltage = tuple(int(x) for x in joltage)
        return Machine(lights, wiring, joltage)
        
    def __str__(self):
        return f"Machine(lights={self.lights}, wiring={self.wiring}, joltage={self.joltage})"
    
    def __repr__(self):
        return str(self)
    
    def solve(self):
        target = [1 if c == '#' else 0 for c in self.lights]
        solver = Optimize()

        presses = [Bool(f'b{idx}') for idx in range(len(self.wiring))]
        
        for i in range(len(self.lights)):
            toggles = []
            for j, effects in enumerate(self.wiring):
                if i in effects:
                    toggles.append(presses[j])
            
            if toggles:
                xor_result = toggles[0]
                for toggle in toggles[1:]:
                    xor_result = Xor(xor_result, toggle)
                
                if target[i] == 1:
                    solver.add(xor_result == True)
                else:
                    solver.add(xor_result == False)
            else:
                solver.add(target[i] == 0)
        
        press_count = Sum([If(bp, 1, 0) for bp in presses])
        solver.minimize(press_count)

        assert solver.check() == sat, "not haz solve"
        
        model = solver.model()
        pressed_buttons = [i for i, bp in enumerate(presses) if model.evaluate(bp)]
        return len(pressed_buttons)
    
    def solve_joltage(self):
        solver = Optimize()

        presses = [Int(f'b{idx}') for idx in range(len(self.wiring))]
        
        for bp in presses:
            solver.add(bp >= 0)

        for i in range(len(self.joltage)):
            t = []
            for j in range(len(self.wiring)):
                if i in self.wiring[j]:
                    t.append(presses[j])
            solver.add(Sum(t) == self.joltage[i])

        solver.minimize(Sum(presses))

        assert solver.check() == sat, "not haz solve"
        
        model = solver.model()

        return sum([model[d].as_long() for d in model.decls()])


machines = [Machine.from_line(line) for line in lines]
print(sum(machine.solve() for machine in machines))
print(sum(machine.solve_joltage() for machine in machines))