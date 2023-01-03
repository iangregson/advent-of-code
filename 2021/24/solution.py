from typing import List, Tuple
from pathlib import Path

file = Path(__file__).parent / "input.txt"
lines = file.read_text().splitlines()

class ArithmeticLogicUnitRegister:
    def __set_name__(self, owner: object, name: str):
        self.name = name

    def __get__(self, obj: object, objtype=None) -> int:
        return getattr(obj, '_registers')[self.name]

    def __set__(self, obj: object, value: int):
        getattr(obj, '_registers')[self.name] = value


class ArithmeticLogicUnit:
    w = ArithmeticLogicUnitRegister()
    x = ArithmeticLogicUnitRegister()
    y = ArithmeticLogicUnitRegister()
    z = ArithmeticLogicUnitRegister()

    def __init__(self, w: int = 0, x: int = 0, y: int = 0, z: int = 0) -> None:
        self._registers = {'w': w, 'x': x, 'y': y, 'z': z}

    def execute(self, instructions: List[str], inputs: List[int] = None) -> None:
        inputs = inputs.copy() if inputs else []
        operations = {
            'inp': lambda a, b: int(inputs.pop(0)),
            'add': lambda a, b: self._registers[a] + b,
            'mul': lambda a, b: self._registers[a] * b,
            'div': lambda a, b: int(self._registers[a] / b),
            'mod': lambda a, b: self._registers[a] % b,
            'eql': lambda a, b: int(self._registers[a] == b)
        }
        for instruction in instructions:
            operation, arg_a, arg_b = (instruction + ' 0').split(' ')[:3]
            arg_b = self._registers[arg_b] if arg_b.isalpha() else int(arg_b)
            self._registers[arg_a] = (operations[operation])(arg_a, arg_b)


def check_version_number(instructions: List[str], version_number: int) -> bool:
    alu = ArithmeticLogicUnit()
    alu.execute(instructions, [int(d) for d in list(str(version_number))])
    return not alu.z


def find_digits(left: int, right: int, find_max: bool = True) -> Tuple[int, int]:
    if find_max:
        if left + right <= 0:
            return 9, 9 + left + right
        else:
            return 9 - left - right, 9
    else:
        if left + right <= 0:
            return 1 - left - right, 1
        else:
            return 1, 1 + left + right


def calculate_version(instructions: List[str], find_max: bool = True) -> int:
    instruction_sets = []
    for instruction in instructions:
        if instruction.startswith('inp'):
            instruction_sets.append([])
        instruction_sets[-1].append(instruction)

    version_number_digits: List = [None] * len(instruction_sets)
    left_digit_stack = []
    for i in range(len(instruction_sets)):
        if instruction_sets[i][4] == 'div z 1':
            left_digit_stack.append((i, instruction_sets[i]))
        else:
            left_i, left_instruction_set = left_digit_stack.pop()
            left_increment = int(left_instruction_set[15].split(' ')[2])
            right_increment = int(instruction_sets[i][5].split(' ')[2])
            version_number_digits[left_i], version_number_digits[i] = \
                find_digits(left_increment, right_increment, find_max)
    return int(''.join([str(d) for d in version_number_digits]))


print(f'Part 1: {calculate_version(lines)}')
print(f'Part 2: {calculate_version(lines, False)}')