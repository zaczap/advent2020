#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

path_to_input = sys.argv[1]

valid = 0
with open(path_to_input) as input_file:
    for line in input_file:
        rule, password = line.strip().split(':')
        limits, character = rule.split(' ')
        lower, upper = map(int, limits.split('-'))
        if lower <= password.count(character) <= upper:
            valid += 1
print(valid)

valid = 0
with open(path_to_input) as input_file:
    for line in input_file:
        rule, password = line.strip().split(':')
        limits, character = rule.split(' ')
        lower, upper = map(int, limits.split('-'))
        if (password[lower] == character) ^ (password[upper] == character):
            print(line, password[lower], password[upper])
            valid += 1
            
print(valid)