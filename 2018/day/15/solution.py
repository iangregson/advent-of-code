#!/usr/bin/env python3
from enum import Enum
from collections import namedtuple
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")

P = namedtuple('P', ['x', 'y'])

