#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

path_to_input = sys.argv[1]

def parse_rule(line):
    fragments = [x.strip() for x in line.split('contain')]
    bag_type = fragments[0].rstrip('s')
    contains = [f.strip().rstrip('s') for f in fragments[1].split(',')]
    return (bag_type, contains)

def extract_bag_type(rule):
    return ' '.join(rule.split(' ')[1:])

def extract_bag_count(rule):
    count = rule.split(' ')[0]
    if count == 'no':
        return 0
    return int(count)

rules = {}
with open(path_to_input) as input_file:
    for line in input_file:
        bag_type, contains = parse_rule(line.strip().strip('.'))
        rules[bag_type] = contains


possible = {bag_type:None for bag_type in rules}
def can_contain(bag_type):
    if bag_type not in rules:
        return False
    children = [extract_bag_type(x) for x in rules[bag_type]]
    #print(bag_type, children)
    if 'shiny gold bag' in children:
        return True
    elif any(can_contain(child) for child in children):
        return True
    return False

total = 0
for bag_type in rules:
    if bag_type == 'shiny gold bag': continue
    if can_contain(bag_type):
        total += 1

print(total)

def recursive_bag_counting(bag_type):
    if bag_type not in rules:
        return 0
    else:
        children = rules[bag_type]
        bag_types = [extract_bag_type(x) for x in rules[bag_type]]
        bag_counts = [extract_bag_count(x) for x in rules[bag_type]]
        return sum(bag_counts) + sum([count*recursive_bag_counting(child_type) for (count, child_type) in zip(bag_counts, bag_types)])

print(recursive_bag_counting('shiny gold bag'))