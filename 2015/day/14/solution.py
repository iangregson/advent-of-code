#!/usr/bin/env python3

import os
from collections import defaultdict
from itertools import permutations

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
lines = file.readlines()
lines = [line.strip().rstrip('.') for line in lines]

# file = open(dir_path + "/test_input.txt", "r")
# lines = file.readlines()
# lines = [line.strip().rstrip('.') for line in lines]

# print(lines)

rules = []
for line in lines:
    tokens = line.split(" ")
    name, speed, time, rest = tokens[0], tokens[3], tokens[6], tokens[-2]
    rule = (name, int(speed), int(time), int(rest))
    rules.append(rule)

# print(rules)


class Runner():
    def __init__(self, rule):
        name, speed, time, rest = rule
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.resting = False
        self.running = True
        self.rest_count = 0
        self.run_count = 0
        self.distance = 0
        self.score = 0

    def tick(self):
        if self.resting:
            self.rest_count += 1
            if self.rest_count == self.rest:
                self.start_running()
        else:
            self.run_count += 1
            self.distance += self.speed
            if self.run_count == self.time:
                self.start_resting()

    def reset(self):
        self.rest_count = 0
        self.run_count = 0

    def start_running(self):
        self.reset()
        self.running = True
        self.resting = False

    def start_resting(self):
        self.reset()
        self.running = False
        self.resting = True

    def is_leader(self, leader_distance):
        return self.distance == leader_distance


runners = []
for rule in rules:
    runners.append(Runner(rule))

N = 2503
n = 0
while n < N:
    for runner in runners:
        runner.tick()
        # print(runner.name, runner.distance)
    n += 1


distances = []
for runner in runners:
    # print(runner.name, runner.distance)
    r = (runner.distance, runner.name)
    distances.append(r)


print("Part 1 answer:", max(distances))

runners = []
for rule in rules:
    runners.append(Runner(rule))

N = 2503
n = 0
leader_distance = 0
while n < N:
    distances = []
    for runner in runners:
        runner.tick()
        distances.append(runner.distance)
        # print(runner.name, runner.distance)
    leader_distance = max(distances)
    for runner in runners:
        if runner.is_leader(leader_distance):
            runner.score += 1

    n += 1

distances = []
for runner in runners:
    # print(runner.name, runner.distance)
    r = (runner.score, runner.distance, runner.name)
    distances.append(r)

print("Part 2 answer:", max(distances))
