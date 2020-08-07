#!/usr/bin/env python3

import os
from collections import defaultdict

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [l.strip() for l in file.readlines()]

# input_txt = [
#     'value 5 goes to bot 2',
#     'bot 2 gives low to bot 1 and high to bot 0',
#     'value 3 goes to bot 1',
#     'bot 1 gives low to output 1 and high to bot 0',
#     'bot 0 gives low to output 2 and high to output 0',
#     'value 2 goes to bot 2',
# ]

# print(input_txt)


class Bot():
    def __init__(self, id, bot_ctrl):
        self.bot_ctrl = bot_ctrl
        self.chip_history = set()
        self.chips = set()
        self.id = id
        self.rule = None

    def __str__(self):
        return str(self.id) + ' :: ' + str(self.chip_history)

    def take_token(self, value):
        self.chips.add(value)
        if len(self.chips) == 2:
            self.give_tokens()

    def give_tokens(self):
        high_token = sorted(self.chips)[1]
        low_token = sorted(self.chips)[0]
        rule_lst = self.rule.split()
        high_dest = rule_lst[-2]
        low_dest = rule_lst[5]
        high_dest_id = int(rule_lst[-1])
        low_dest_id = int(rule_lst[6])

        if high_dest == 'bot':
            self.bot_ctrl.bots[high_dest_id].take_token(high_token)
        elif high_dest == 'output':
            self.bot_ctrl.outputs[high_dest_id].append(high_token)

        if low_dest == 'bot':
            self.bot_ctrl.bots[low_dest_id].take_token(low_token)
        elif low_dest == 'output':
            self.bot_ctrl.outputs[low_dest_id].append(low_token)

        # print('Bot {} gave high token: '.format(self.id),
        #       high_token, high_dest, high_dest_id)
        # print('Bot {} gave low token: '.format(
            # self.id), low_token, low_dest, low_dest_id)
        self.chip_history.add(high_token)
        self.chip_history.add(low_token)
        self.chips = set()
        # print(self)


class BotCtrl():
    def __init__(self):
        self.bots = defaultdict(Bot)
        self.outputs = defaultdict(list)
        self.instructions = []

    def get_line_type(self, line):
        if line.startswith('value'):
            type = 'INSTRUCTION'
        if line.startswith('bot'):
            type = 'RULE'

        return type

    def parse_instruction(self, line):
        type = self.get_line_type(line)

        if type == 'INSTRUCTION':
            self.instructions.append(line)
        elif type == 'RULE':
            self.give_rule(line)

    def execute_instructions(self):
        for line in self.instructions:
            self.give_instruction(line)

    def give_instruction(self, line):
        bot_id = int(line.split()[-1])
        value = int(line.split()[1])
        if bot_id not in self.bots:
            self.bots[bot_id] = Bot(bot_id, self)
        self.bots[bot_id].take_token(int(value))

    def give_rule(self, line):
        bot_id = int(line.split()[1])
        if bot_id not in self.bots:
            self.bots[bot_id] = Bot(bot_id, self)
        self.bots[bot_id].rule = line

    def find_responsible_bot(self, Ns):
        responsible_bot = None
        for bot in self.bots.values():
            if sorted(bot.chip_history.intersection(set(Ns))) == sorted(set(Ns)):
                responsible_bot = bot
                break
        return responsible_bot


N1 = 61
N2 = 17

# N1 = 5
# N2 = 2

bot_ctrl = BotCtrl()

for line in input_txt:
    bot_ctrl.parse_instruction(line)
bot_ctrl.execute_instructions()

print("Part 1 answer:", bot_ctrl.find_responsible_bot([N1, N2]))

a = bot_ctrl.outputs[0][0]
b = bot_ctrl.outputs[1][0]
c = bot_ctrl.outputs[2][0]
print("Part 2 answer:", a*b*c)
