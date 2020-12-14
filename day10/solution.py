#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from collections import Counter

path_to_input = sys.argv[1]

numbers = []
with open(path_to_input) as input_file:
    for line in input_file:
        numbers.append(int(line.strip()))

numbers.sort()

adapters = [0] + numbers + [numbers[-1] + 3]
differences = []
for i in range(1, len(adapters)):
    differences.append(adapters[i] - adapters[i-1])
counts = Counter(differences)
print(counts[1] * counts[3])

memory = {}
def how_many_ways(number):
    if number in memory: return memory[number]
    valid_children = []
    for offset in [-1, -2, -3]:
        if number + offset in adapters:
            valid_children.append(number + offset)
    if number == 0:
        memory[number] = 1
        return 1
    elif len(valid_children) == 0:
        memory[number] = 0
        return 0
    else:
        working_sum = 0
        for child in valid_children:
            x = how_many_ways(child) 
            memory[number] = x
            working_sum += x
        memory[number] = working_sum
        return working_sum

print(how_many_ways(adapters[-1]))