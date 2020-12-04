#!/usr/bin/env python3

import os
import itertools
import functools
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/input.txt", "r")
# file = open(dir_path + "/input.example.txt", "r")
lines = [l.strip() for l in file.readlines()]

req_fields = {
  'byr': '(Birth Year)',
  'iyr': '(Issue Year)',
  'eyr': '(Expiration Year)',
  'hgt': '(Height)',
  'hcl': '(Hair Color)',
  'ecl': '(Eye Color)',
  'pid': '(Passport ID)',
}

def get_records(input_lines):
  records = []
  while len(input_lines) > 0:
    record = list(itertools.takewhile(lambda x: x != '', input_lines))
    records.append(" ".join(record))

    if '' in input_lines:
      idx = input_lines.index('') + 1
      input_lines = input_lines[idx:]
    else:
      break
  return records

def is_valid_record(record):
  return all(field in record for field in req_fields.keys())

records = get_records(lines)
valid_records = list(filter(is_valid_record, records))

print('Part 1:', len(valid_records))

def passes_data_validation(record):
  is_pass = True
  fields = record.split()
  for field in fields:
    key, value = field.split(':')

    if key == 'byr':
      is_pass = is_pass and len(value) == 4 and (1920 <= int(value) <= 2002)
    elif key == 'iyr':
      is_pass = is_pass and len(value) == 4 and (2010 <= int(value) <= 2020)
    elif key == 'eyr':
      is_pass = is_pass and len(value) == 4 and (2010 <= int(value) <= 2030)
    elif key == 'hgt':
      if 'in' in value:
        is_pass = is_pass and (3 <= len(value) <= 4) and (59 <= int(value[:-2]) <= 76)
      else:
        is_pass = is_pass and (3 <= len(value) <= 5) and (150 <= int(value[:-2]) <= 193)
    elif key == 'hcl':
      is_pass = is_pass and (value[0] == '#') and len(value) == 7 and re.match('^[a-f0-9]+$', value[1:]) != None
    elif key == 'ecl':
      is_pass = is_pass and value in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    elif key == 'pid':
      is_pass = is_pass and len(value) == 9 and re.match('^[0-9]+$', value) != None
    
  return is_pass

def passes_data_validation_w_reduce(record):

  def accumulator(is_pass, field):
    key, value = field.split(':')
    if key == 'byr':
      is_pass = is_pass and len(value) == 4 and (1920 <= int(value) <= 2002)
    elif key == 'iyr':
      is_pass = is_pass and len(value) == 4 and (2010 <= int(value) <= 2020)
    elif key == 'eyr':
      is_pass = is_pass and len(value) == 4 and (2010 <= int(value) <= 2030)
    elif key == 'hgt':
      if 'in' in value:
        is_pass = is_pass and (3 <= len(value) <= 4) and (59 <= int(value[:-2]) <= 76)
      else:
        is_pass = is_pass and (3 <= len(value) <= 5) and (150 <= int(value[:-2]) <= 193)
    elif key == 'hcl':
      is_pass = is_pass and (value[0] == '#') and len(value) == 7 and re.match('^[a-f0-9]+$', value[1:]) != None
    elif key == 'ecl':
      is_pass = is_pass and value in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    elif key == 'pid':
      is_pass = is_pass and len(value) == 9 and re.match('^[0-9]+$', value) != None

    return is_pass
  
  return functools.reduce(accumulator, record.split(), True)

data_valid_records = list(filter(passes_data_validation, valid_records))
data_valid_records_reduced = list(filter(passes_data_validation_w_reduce, valid_records))

print('Part 2:', len(data_valid_records), len(data_valid_records_reduced))
