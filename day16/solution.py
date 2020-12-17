#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from itertools import chain

path_to_input = sys.argv[1]

with open(path_to_input) as input_file:
    section = 0 # 0 = rules; 1 = my ticket; 2 = nearby tickets
    rules = {}
    ticket = []
    nearby_tickets = []
    expect_header = False
    for line in input_file:
        line = line.rstrip()
        if line == '': 
            section += 1 
            expect_header = True
            continue
        if expect_header:
            expect_header = False
            continue
        if section == 0:
            rule, ranges = [v.strip() for v in line.split(':')]
            range1, range2 = ranges.split(' or ')
            range1 = list(sorted(map(int, range1.split('-'))))
            range2 = list(sorted(map(int, range2.split('-'))))
            rules[rule] = [range1, range2]
        elif section == 1:
            ticket = list(map(int, line.split(',')))
        elif section == 2:
            nearby_ticket = list(map(int, line.split(',')))
            nearby_tickets.append(nearby_ticket)

valid = set()
for rule, ranges in rules.items():
    print(rule, ranges)
    for n in chain(range(ranges[0][0], ranges[0][1]+1), range(ranges[1][0], ranges[1][1]+1)):
        valid.add(n)

error = 0
flags = []
for nearby_ticket in nearby_tickets:
    status = True
    for field in nearby_ticket:
        if field in valid: 
            continue
        else:
            status = False
            error += field
    flags.append(status)

print(error, sum(flags))

real_tickets = [nearby_ticket for (nearby_ticket, flag) in zip(nearby_tickets, flags) if flag]

valid_fields = []
for i in range(len(ticket)):
    valid_fields.append(set(rules.keys()))

for real_ticket in real_tickets:
    for i, field_value in enumerate(real_ticket):
        valid_set = valid_fields[i]
        invalid_set = set()
        for rule_name in valid_set:
            ranges = rules[rule_name]
            if not any(ranges[j][0] <= field_value <= ranges[j][1] for j in range(2)):
                invalid_set.add(rule_name)
        valid_fields[i] -= invalid_set

sizes = map(len, valid_fields)

for i, size in sorted(enumerate(sizes), key = lambda x: x[1]):
    for j in range(len(ticket)):
        if i != j:
            valid_fields[j] -= valid_fields[i]

field_names = [list(valid_fields[i])[0] for i in range(len(ticket))]

labeled_ticket = dict(zip(field_names, ticket))

product = 1
for departure_field in filter(lambda field_name:'departure' in field_name, field_names):
    product *= labeled_ticket[departure_field]

print(product)