#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import re

path_to_input = sys.argv[1]

def reify_customs_report(lines):
    questions = set()
    for line in lines:
        questions = questions.union(set(list(line)))
    return questions

def reify_joint_customs_report(lines):
    questions = set.intersection(*[set(list(line)) for line in lines])
    return questions

customs_reports = []
with open(path_to_input) as input_file:
    buffer = []
    for line in input_file:
        line = line.strip()
        if line == '':
            customs_report = reify_customs_report(buffer)
            customs_reports.append(customs_report)
            buffer = []
        else:
            buffer.append(line)
    if len(buffer) > 0:
        customs_report = reify_customs_report(buffer)
        customs_reports.append(customs_report)
        buffer = []

print(sum(map(len, customs_reports)))

customs_reports = []
with open(path_to_input) as input_file:
    buffer = []
    for line in input_file:
        line = line.strip()
        if line == '':
            customs_report = reify_joint_customs_report(buffer)
            customs_reports.append(customs_report)
            buffer = []
        else:
            buffer.append(line)
    if len(buffer) > 0:
        customs_report = reify_joint_customs_report(buffer)
        customs_reports.append(customs_report)
        buffer = []

print(sum(map(len, customs_reports)))
