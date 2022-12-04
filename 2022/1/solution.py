from pathlib import Path

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.readlines()

elf_cals = [[int(cals) for cals in block.split("\n")] for block in text.split("\n\n")]

print("Part 1:", max([sum(cals) for cals in elf_cals]))
print("Part 2:", sum(sorted([sum(cals) for cals in elf_cals])[-3:]))