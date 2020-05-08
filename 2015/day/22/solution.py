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


class Spellbook():
    def __init__(self):
        self.spells = defaultdict(dict)

        # Spell = (cost, damages, heals, armors, duration, manas)
        self.spells['Magic Missile'] = (53, 4, 0, 0, 1, 0)
        self.spells['Drain'] = (73, 2, 2, 0, 1, 0)
        self.spells['Sheild'] = (53, 0, 0, 7, 6, 0)
        self.spells['Poison'] = (173, 3, 0, 0, 6, 0)
        self.spells['Recharge'] = (229, 0, 0, 0, 5, 101)

        self.spell_list = list([x for x in self.spells])

    def choose_spell(self, active_spells, available_mana):
        available_spells = list(set(self.spell_list) - set(active_spells))

        spell = None
        s = random.choice(available_spells)
        while spell == None and len(available_spells) > 0:
            cost, damages, heals, armors, duration, manas = self.spells[s]
            if cost > available_mana:
                available_spells = list(set(available_spells) - set([s]))
                continue
            else:
                spell = (cost, damages, heals, armors, duration, manas)
        return spell


class Player():
    def __init__(self, name, stats):
        hit, damage, mana = stats
        self.name = name
        self.hit = hit
        self.damage = damage
        self.armor = 0
        self.mana_spent = 0
        self.mana_current = mana
        self.spellbook = Spellbook()
        self.active_spells = []

    def attack(self, other, damage=None):
        other.defend(damage or self.damage)

    def defend(self, damage):
        armor = self.has_armor()
        damage = max(damage - armor, 1)
        self.hit -= damage

    def has_armor(self):
        armor = 0
        if len(self.active_spells) == 0:
            return armor
        else:
            for spell in self.active_spells:
                cost, damages, heals, armors, duration, manas = spell
                armor += armors
            return armors

    def cast_spell(self, other):
        for (idx, spell) in enumerate(self.active_spells):
            cost, damages, heals, armors, duration, manas = spell
            self.attack(other, damages)
            self.hit += heals
            self.mana_current += manas

            cost = 0
            duration -= 1

            if duration > 0:
                self.active_spells[idx] = (
                    cost, damages, heals, armors, duration, manas)
            else:
                del self.active_spells[idx]

        s = self.spellbook.choose_spell(self.active_spells, self.mana_current)
        if s == None:
            self.game_over()
            return

        cost, damages, heals, armors, duration, manas = s
        self.mana_spent += cost
        self.attack(other, damages)
        self.hit += heals
        self.armor = armors
        self.mana_current += manas

        cost = 0
        duration -= 1

        if duration > 0:
            self.active_spells.append(
                (cost, damages, heals, armors, duration, manas))

    def is_dead(self):
        return self.hit <= 0

    def game_over(self):
        self.hit = 0


class Game():
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss
        self.winner = None

        self.turn_of = 'player'

    def turn(self):
        if self.turn_of == 'player':
            self.player.cast_spell(self.boss)
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


N = 50000
mana_spent = []
for game in range(0, N):
    P = Player('player1', (50, 0, 500))
    B = Player('boss', tuple(boss_stats.values()))
    G = Game(P, B)
    while not G.game_over():
        G.turn()

    print("WINNER ", G.winner.name)

    if G.winner == P:
        mana_spent.append(P.mana_spent)


print("Part 1 answer:", min(mana_spent))
print("Part 2 answer:", 0)
