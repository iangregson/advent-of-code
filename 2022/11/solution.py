from pathlib import Path
from functools import reduce
from operator import mul

file = Path(__file__).parent / 'input.txt'
# file = Path(__file__).parent / 'test_input.txt'
text = file.read_text()

class Monkey():
  def __init__(self, id = 0, holding = [], *, config = {}) -> None:
    self.id = id
    self.inspected_count = 0
    self.holding = holding
    self.config = config
    self.condition = lambda x: bool(x)
    self.operation = lambda x: x

  def __str__(self) -> str:
    return f"Monkey {self.id}: {', '.join([str(x) for x in self.holding])} | inspected: {self.inspected_count}"
  
  def __repr__(self) -> str:
    return f"{self}"

  @staticmethod
  def from_text(monkey_text, is_part_1 = True):
    monkey_text = [line.lstrip() for line in monkey_text.split('\n')]
    id = monkey_text[0][-2]
    holding = [int(x) for x in monkey_text[1].split(': ')[1].split(', ')]
    monkey_t = monkey_text[-2][-1]
    monkey_f = monkey_text[-1][-1]

    divisible_by = int(monkey_text[-3].split()[-1]) 

    m = Monkey(id, holding, config={
      'monkey_f': monkey_f,
      'monkey_t': monkey_t,
      'is_part_1': is_part_1,
      'divisible_by': divisible_by,
    })

    m.condition = lambda x: x % divisible_by == 0

    operation_op = monkey_text[2].split()[-2]
    operation_val = monkey_text[2].split()[-1]

    if operation_op == '*':
      if operation_val == 'old':
        m.operation = lambda x: x * x
      else:
        m.operation = lambda x: x * int(operation_val)
    elif operation_op == '+':
      if operation_val == 'old':
        m.operation = lambda x: x + x
      else:
        m.operation = lambda x: x + int(operation_val)

    return m

  def inspect(self, item):
    self.inspected_count += 1
    item = self.operation(item)
    if self.config['is_part_1'] == True:
      item = item // 3
    else:
      item = item // 1
    check = self.condition(item)
    return check, item

  def catch(self, item):
    self.holding.append(item)

  def turn(self, monkeys = {}, *, max_worry = None):
    while self.holding:
      item = self.holding.pop(0)

      if max_worry is not None:
        item = item % max_worry

      check, item = self.inspect(item)
      if check:
        monkeys[self.config['monkey_t']].catch(item)
      else:
        monkeys[self.config['monkey_f']].catch(item)
    

class Sim():
  def __init__(self, monkeys = [], *, max_rounds = 20, max_worry = None) -> None:
    self.__rounds = None
    self.max_rounds = max_rounds
    self.max_worry = max_worry
    self.monkeys = {m.id: m for m in monkeys}

  def __str__(self) -> str:
    return "\n".join([f"{m}" for m in self.monkeys.values()])

  def __repr__(self) -> str:
    return f"{self}"

  @property
  def rounds(self):
    return self.__rounds

  def __iter__(self):
    self.rounds = 0

  def __iter__(self):
    self.__rounds = 0
    return self

  def __next__(self):
    if self.rounds < self.max_rounds:
      self.__rounds += 1
      self.__round()
    else:
      raise StopIteration
    return self.rounds

  def __round(self):
    for monkey in self.monkeys.values():
      monkey.turn(self.monkeys, max_worry = self.max_worry)

monkey_texts = text.split("\n\n")
monkeys = [Monkey.from_text(mt) for mt in monkey_texts]

sim = Sim(monkeys, max_rounds = 20)
for round in sim:
  pass

inspected_counts = sorted([m.inspected_count for m in sim.monkeys.values()])
print("Part 1:", reduce(mul,inspected_counts[-2:]))

monkeys = [Monkey.from_text(mt, is_part_1=False) for mt in monkey_texts]
max_worry = 1
for m in monkeys:
  max_worry *= m.config['divisible_by']
sim = Sim(monkeys, max_rounds = 10000, max_worry = max_worry)
for round in sim:
  pass

inspected_counts = sorted([m.inspected_count for m in sim.monkeys.values()])
print("Part 2:", reduce(mul,inspected_counts[-2:]))