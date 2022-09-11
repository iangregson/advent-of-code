#!/usr/bin/env python3

import os
import sys
from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
import itertools
import functools
import operator
import random

# sys.setrecursionlimit(100000)

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
lines = [line.strip() for line in file.readlines()]
