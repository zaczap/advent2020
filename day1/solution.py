#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

path_to_input = sys.argv[1]

seen = {}

with open(path_to_input) as input_file:
    for line in input_file:
        value = int(line.strip())
        partner = 2020 - value
        if partner in seen:
            print("Solution found! {0} + {1} = 2020 and their product is {2}".format(value, partner, value*partner))
        seen[value] = True

values = list(seen.keys())
n = len(values)

for i in range(n):
    for j in range(i+1, n):
        partner = 2020 - values[i] - values[j]
        if partner in seen:
            print("Solution found! {0} + {1} + {2} = 2020 and their product is {3}".format(values[i], values[j], partner, values[i]*values[j]*partner))
            sys.exit(0)