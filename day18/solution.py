#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import re
from functools import partial

def evaluate_canonical_form(input_list):
    evaluated = 0
    i = 0
    while i < len(input_list):
        if i == 0:
            evaluated = input_list[i]
            i += 1
        elif input_list[i] == '+':
            evaluated += input_list[i+1]
            i += 2
        elif input_list[i] == '*':
            evaluated *= input_list[i+1]
            i += 2
    return evaluated

def evaluate_canonical_form_with_precedence(input_list):
    evaluated = 0
    while input_list.count('+') > 0:
        mid = input_list.index('+')
        a, b = input_list[mid-1], input_list[mid+1]
        input_list[mid-1] = 1
        input_list[mid] = '*'
        input_list[mid+1] = a + b
    
    i = 0
    while i < len(input_list):
        if i == 0:
            evaluated = input_list[i]
            i += 1
        elif input_list[i] == '*':
            evaluated *= input_list[i+1]
            i += 2
    return evaluated
        
def evaluate_raw_expression(expression, evaluator):
    atomized = re.split('[\s()]', expression)

    stack = []
    lparen_indices = []

    for atom in atomized:
        # atom can be an operation, a space, or an integer
        if atom in ('*','+'):
            stack.append(atom)
        elif atom == '':
            if len(stack) == 0:
                stack.append('LPAREN')
                lparen_indices.append(len(stack)-1)
            elif stack[-1] in ('*','+','LPAREN'):
                stack.append('LPAREN')
                lparen_indices.append(len(stack)-1)
            else:
                last_lparen_index = 0 if len(lparen_indices) == 0 else lparen_indices.pop()
                fragment = stack[last_lparen_index:]
                evaluated = evaluator(fragment[1:])
                for _ in range(len(fragment)): stack.pop()
                stack.append(evaluated)
        else:
            stack.append(int(atom))

    if len(stack) > 1:
        return(evaluator(stack))
    elif len(stack) == 0:
        return(stack[0])

path_to_input = sys.argv[1]

expressions = []

with open(path_to_input) as input_file:
    for line in input_file:
        expression = line.rstrip()
        expressions.append(expression)
    
# part 1:
evaluated = map(partial(evaluate_raw_expression, evaluator = evaluate_canonical_form), expressions)
print(sum(evaluated))

# part 2:
evaluated = map(partial(evaluate_raw_expression, evaluator = evaluate_canonical_form_with_precedence), expressions)
print(sum(evaluated))
