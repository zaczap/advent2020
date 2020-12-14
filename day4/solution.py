#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import re

path_to_input = sys.argv[1]

def reify_passport(lines):
    fields = {}
    for line in lines:
        for pair in line.split(' '):
            key, value = pair.split(':')
            fields[key] = value
    return fields

def validate_passport(passport, required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
    for field in required_fields:
        if field not in passport:
            return False
    return True

passports = []
n_valid = 0
with open(path_to_input) as input_file:
    buffer = []
    for line in input_file:
        line = line.strip()
        if line == '':
            passport = reify_passport(buffer)
            n_valid += 1 if validate_passport(passport) else 0
            passports.append(passport)
            buffer = []
        else:
            buffer.append(line)
    if len(buffer) > 0:
        passport = reify_passport(buffer)
        n_valid += 1 if validate_passport(passport) else 0
        passports.append(passport)
        buffer = []

print(n_valid)

def is_valid_year(value, lower, upper):
    if not value.isnumeric():
        return False
    if lower > int(value) or int(value) > upper:
        return False
    return True

def is_valid_height(value):
    pattern = '([1-9]*[0-9]*)(in|cm)'
    match = re.fullmatch(pattern, value)
    if match is None:
        return False
    number, unit = match.group(1), match.group(2)
    if unit == 'cm':
        if 150 <= int(number) <= 193:
            return True
    if  unit == 'in':
        if 59 <= int(number) <= 76:
            return True
    return False

def is_valid_hair_color(value):
    pattern = '#[0-9a-f]{6}'
    match = re.fullmatch(pattern, value)
    if match is None:
        return False
    return True

def is_valid_eye_color(value):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value not in valid_colors:
        return False
    return True

def is_valid_passport_id(value):
    pattern = '[0-9]{9}'
    match = re.fullmatch(pattern, value)
    if match is None:
        return False
    return True

def validate_passport_strict(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport:
            return False
    if not is_valid_year(passport['byr'], 1920, 2002): 
        print("Failed byr: {}".format(passport['byr']))
        return False
    if not is_valid_year(passport['iyr'], 2010, 2020):
        print("Failed iyr: {}".format(passport['iyr']))
        return False
    if not is_valid_year(passport['eyr'], 2020, 2030):
        print("Failed eyr: {}".format(passport['eyr']))
        return False
    if not is_valid_height(passport['hgt']):
        print("Failed hgt: {}".format(passport['hgt']))
        return False
    if not is_valid_hair_color(passport['hcl']):
        print("Failed hcl: {}".format(passport['hcl']))
        return False
    if not is_valid_eye_color(passport['ecl']):
        print("Failed ecl: {}".format(passport['ecl']))
        return False
    if not is_valid_passport_id(passport['pid']):
        print("Failed pid: {}".format(passport['pid']))
        return False
    return True
    
n_valid = 0
for passport in passports:
    n_valid += 1 if validate_passport_strict(passport) else 0
print(n_valid)