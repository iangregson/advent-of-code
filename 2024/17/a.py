from collections import defaultdict
from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

r = defaultdict(list[int])


class Computer:
    def __init__(self, input):
        self.registers = defaultdict(int)
        registers, program = input.split("\n\n")
        program = list(map(int, program.split(": ")[1].split(",")))
        for line in registers.splitlines():
            id, v = line.split(": ")
            id = id[-1]
            v = int(v)
            self.registers[id] = v
        self.program = program
        self.insp = 0
        self.eof = len(program)
        self.output = []

    def __str__(self) -> str:
        return f"""
            {self.registers}
            {self.program}
            {self.output}
        """
    
    def __repr__(self) -> str:
        return str(self)
    
    def stdout(self):
        return ",".join(map(str, self.output))
    
    @property
    def a(self):
        return self.registers["A"]
    @a.setter
    def a(self, value):
        self.registers["A"] = value
    @property
    def b(self):
        return self.registers["B"]
    @b.setter
    def b(self, value):
        self.registers["B"] = value
    @property
    def c(self):
        return self.registers["C"]
    @c.setter
    def c(self, value):
        self.registers["C"] = value
    
    def combo(self, operand):
        """
        Combo operands 0 through 3 represent literal values 0 through 3.
        Combo operand 4 represents the value of register A.
        Combo operand 5 represents the value of register B.
        Combo operand 6 represents the value of register C.
        Combo operand 7 is reserved and will not appear in valid programs.
        """
        assert operand < 7
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c

    def adv(self):
        """
        The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
        The denominator is found by raising 2 to the power of the instruction's combo operand.
        (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
        The result of the division operation is truncated to an integer and then written to the A register.
        """
        operand = self.program[self.insp + 1]
        numerator = self.a
        denominator = 2 ** self.combo(operand)
        self.a = numerator // denominator

    def bxl(self):
        """
        The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's 
        literal operand, then stores the result in register B.
        """
        operand = self.program[self.insp + 1]
        self.b = self.b ^ operand

    def bst(self):
        """
        The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby 
        keeping only its lowest 3 bits), then writes that value to the B register.
        """
        operand = self.program[self.insp + 1]
        self.b = self.combo(operand) % 8

    def jnz(self):
        """
        The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register 
        is not zero, it jumps by setting the instruction pointer to the value of its literal operand; 
        if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        """
        operand = self.program[self.insp + 1]
        if self.a != 0:
            self.insp = operand
            return
        self.insp += 2

    def bxc(self):
        """
        The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then
        stores the result in register B. (For legacy reasons, this instruction reads an operand
        but ignores it.)
        """
        _ = self.program[self.insp + 1]
        self.b = self.b ^ self.c

    def out(self):
        """
        The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs
        that value. (If a program outputs multiple values, they are separated by commas.)
        """
        operand = self.program[self.insp + 1]
        self.output.append(self.combo(operand) % 8)

    def bdv(self):
        """
        The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is
        stored in the B register. (The numerator is still read from the A register.)
        """
        operand = self.program[self.insp + 1]
        numerator = self.a
        denominator = 2 ** self.combo(operand)
        self.b = numerator // denominator
        

    def cdv(self):
        """
        The cdv instruction (opcode 7) works exactly like the adv instruction except that the result 
        is stored in the C register. (The numerator is still read from the A register.)
        """
        operand = self.program[self.insp + 1]
        numerator = self.a
        denominator = 2 ** self.combo(operand)
        self.c = numerator // denominator

    def run(self):
        while self.insp < self.eof:
            assert self.insp + 1 <= self.eof
            opcode, operand = self.program[self.insp], self.program[self.insp + 1]
            if opcode == 0:
                self.adv()
                self.insp += 2
            elif opcode == 1:
                self.bxl()
                self.insp += 2
            elif opcode == 2:
                self.bst()
                self.insp += 2
            elif opcode == 3:
                self.jnz()
                # self.insp += 2 # handled in jnz
            elif opcode == 4:
                self.bxc()
                self.insp += 2
            elif opcode == 5:
                self.out()
                self.insp += 2
            elif opcode == 6:
                self.bdv()
                self.insp += 2
            elif opcode == 7:
                self.cdv()
                self.insp += 2
            else:
                raise ValueError(f"Unknown opcode {opcode}")


c = Computer(input)
c.run()
print(c.stdout())

Q = [(0,1)]

A = 1e18
while True:
    j = None
    try:
        j = Q.pop()
    except:
        pass

    if j is None:
        break

    a, d = j
    c = Computer(input)
    
    if d > len(c.program):
        break

    for i in range(8):
        c = Computer(input)
        c.a = a*8+i
        c.run()

        if c.output != c.program[-d:]:
            continue

        if d == len(c.program):
            if a*8+i < A:
                A = a*8+i
        else:
            Q.append((a*8+i, d+1))
    
print(A)