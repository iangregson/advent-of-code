#!/usr/bin/env python3

import os
import re
import struct

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.readlines()
lines = [line.strip() for line in input_txt]

# input_txt = """123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i"""

# lines = input_txt.split("\n")


# print(lines)

class Circuit():
    def __init__(self, instructions):
        self.instructions = instructions
        self.wires = {}
        self.ops = {}

        for i in self.instructions:
            ins, target = i.split(' -> ')
            self.ops[target] = self.parse(ins)

    def parse(self, instruction):
        tokens = instruction.split(" ")
        op = "VAL"
        v = []

        if len(tokens) == 1 and re.search("[0-9]", tokens[0]) != None:
            v.insert(0, int(tokens[0]))
            return (op, v)

        for idx, token in enumerate(tokens):
            if re.search("[A-Z]", token) != None:
                op = token
            elif re.search("[a-z]", token) != None:
                v.insert(idx, token)
            elif re.search("[0-9]", token) != None:
                v.insert(idx, int(token))

        return (op, v)

    def wire(self, name):
        if name in self.wires:
            return self.wires[name]

        try:
            return int(name)
        except ValueError:
            pass

        op, v = self.ops[name]

        print(op, v)

        if op == "VAL":
            self.wires[name] = self.wire(v[0])
        if op == "NOT":
            self.wires[name] = NOT(self.wire(v[0]))
        if op == "AND":
            self.wires[name] = AND(self.wire(v[0]), self.wire(v[1]))
        if op == "OR":
            self.wires[name] = OR(self.wire(v[0]), self.wire(v[1]))
        if op == "LSHIFT":
            self.wires[name] = LSHIFT(self.wire(v[0]), self.wire(v[1]))
        if op == "RSHIFT":
            self.wires[name] = RSHIFT(self.wire(v[0]), self.wire(v[1]))

        return self.wires[name]


def NOT(a):
    return ~a & 0xffff


def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def LSHIFT(a, b):
    return a << b


def RSHIFT(a, b):
    return a >> b


c = Circuit(lines)

print("Part 1 answer:", c.wire("a"))

lines.append("956 -> b")
c = Circuit(lines)
print("Part 2 answer:", c.wire("a"))
