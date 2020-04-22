#!/usr/bin/env python3

import os
from collections import defaultdict
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/test_input.txt", "r")
# file = open(dir_path + "/test_input_2.txt", "r")

lines = file.readlines()
lines = [line.strip() for line in lines]

# print(lines)

boss_stats = defaultdict(dict)

for line in lines:
    stat, value = line.split(": ")
    boss_stats[stat] = int(value)

# print(boss_stats)


class Player():
    def __init__(self, name, stats):
        hit, damage, armor = stats
        self.name = name
        self.hit = hit
        self.damage = damage
        self.armor = armor
        self.gold_spent = 0

    def attack(self, other):
        other.defend(self.damage)

    def defend(self, damage):
        damage = damage - self.armor
        self.hit -= damage

    def purchase(self, shopping_list):
        for item in shopping_list:
            cost, damage, armor = item
            self.gold_spent += cost
            self.damage += damage
            self.armor += armor

    def is_dead(self):
        return self.hit <= 0


class Game():
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss
        self.winner = None

        self.turn_of = 'player'

    def turn(self):
        if self.turn_of == 'player':
            self.player.attack(self.boss)
            self.turn_of = 'boss'
        else:
            self.boss.attack(self.player)
            self.turn_of = 'player'

    def game_over(self):
        if self.player.is_dead():
            self.winner = self.boss
            return True

        if self.boss.is_dead():
            self.winner = self.player
            return True

        return False


class Shop():
    def __init__(self):
        self.shop = defaultdict(dict)

        self.shop['Weapons'] = {
            'Dagger': (8, 4, 0),
            'Shortsword': (10, 5, 0),
            'Warhammer': (25, 6, 0),
            'Longsword': (40, 7, 0),
            'Greataxe': (74, 8, 0),
        }
        self.shop['Armor'] = {
            'Leather': (13, 0, 1),
            'Chainmail': (31, 0, 2),
            'Splintmail': (53, 0, 3),
            'Bandedmail': (75, 0, 4),
            'Platemail': (102, 0, 5),
            'NONE': (0, 0, 0),
        }
        self.shop['Rings'] = {
            'Damage +1': (25, 1, 0),
            'Damage +2': (50, 2, 0),
            'Damage +3': (100, 3, 0),
            'Defense +1': (20, 0, 1),
            'Defense +2': (40, 0, 2),
            'Defense +3': (80, 0, 3),
            'NONE': (0, 0, 0),
        }

        self.weapon_list = list([x for x in self.shop['Weapons']])
        self.armor_list = list([x for x in self.shop['Armor']])
        self.ring_list = list([x for x in self.shop['Rings']])

    def generate_list(self):
        L = []
        w = random.choice(self.weapon_list)
        a = random.choice(self.armor_list)
        r = random.sample(self.ring_list, 2)

        weapon = self.shop['Weapons'][w]
        L.append(weapon)

        armor = self.shop['Armor'][a]
        L.append(armor)

        for ring in r:
            R = self.shop['Rings'][ring]
            L.append(R)

        return L


S = Shop()
gold_spent = []
for game in range(0, 10000):
    P = Player('player1', (100, 0, 0))
    shopping_list = S.generate_list()
    P.purchase(shopping_list)
    B = Player('boss', tuple(boss_stats.values()))
    G = Game(P, B)
    while not G.game_over():
        G.turn()

    print(G.winner.name)

    if G.winner == P:
        gold_spent.append(P.gold_spent)


print("Part 1 answer:", min(gold_spent))

gold_spent = []
for game in range(0, 10000):
    P = Player('player1', (100, 0, 0))
    shopping_list = S.generate_list()
    P.purchase(shopping_list)
    B = Player('boss', tuple(boss_stats.values()))
    G = Game(P, B)
    while not G.game_over():
        G.turn()

    print(G.winner.name)

    if G.winner == B:
        gold_spent.append(P.gold_spent)

print("Part 2 answer:", max(gold_spent))
