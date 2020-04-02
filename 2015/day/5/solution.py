#!/usr/bin/env python3

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = file.readlines()

lines = [line.strip() for line in input_txt]

# lines = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp",
#          "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]

# lines = ["qjhvhtzxzqqjkmpb", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]

VOWELS = ['a', 'e', 'i', 'o', 'u']


class Token:
    def __init__(self, s):
        self.s = s

    def has_3_vowels(self):
        count = 0
        for char in self.s:
            if char in VOWELS:
                count += 1
        return count > 2

    def has_double_letter(self):
        r = re.compile(r"(.)\1")
        return re.search(r, self.s) != None

    def no_banned_substring(self):
        banned_substring = ["ab", "cd", "pq", "xy"]
        for ss in banned_substring:
            if ss in self.s:
                return False
        return True

    def repeat_w_letter_between(self):
        r = re.compile(r"(.).\1")
        return re.search(r, self.s) != None

    def repeating_pair(self):
        r = re.compile(r"(..).*\1")
        return re.search(r, self.s) != None

    def is_nice(self):
        return self.has_3_vowels() and self.no_banned_substring() and self.has_double_letter()

    def is_nice_pt2(self):
        return self.repeating_pair() and self.repeat_w_letter_between()


count = 0
for line in lines:
    t = Token(line)
    if t.is_nice():
        count += 1

print("Part 1 answer:", count)

count = 0
for line in lines:
    t = Token(line)
    if t.is_nice_pt2():
        count += 1

print("Part 2 answer:", count)
