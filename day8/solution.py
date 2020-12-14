#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import re

path_to_input = sys.argv[1]

def parse_line(line):
    opcode, arg = line.split(' ')
    sign, value = arg[0], int(arg[1:])
    sign = 1 if sign == '+' else -1
    return [opcode, sign*value]

instructions = []
with open(path_to_input) as input_file:
    for line in input_file:
        instructions.append(parse_line(line.strip()))

def run_instructions(instructions, silence_failures = False):
    accumulator = 0
    executed = set()
    program_counter = 0
    step = 0

    while True:
        if program_counter in executed:
            if not silence_failures:
                print("Failure: {}".format(accumulator))
            return None
        if program_counter == len(instructions):
            print("Success: {}".format(accumulator)) 
            return accumulator
        next_instruction = instructions[program_counter]
        executed.add(program_counter)
        opcode, value = next_instruction
        if opcode == 'nop':
            next_program_counter = program_counter + 1
        elif opcode == 'acc':
            next_program_counter = program_counter + 1
            accumulator += value
        else:
            next_program_counter += value
        
        #print("cycle {}: line {} -> {}: {} {}\tacc = {}".format(step, program_counter, next_program_counter, opcode, value, accumulator))
        program_counter = next_program_counter
        step += 1

run_instructions(instructions)

for i in range(len(instructions)):
    opcode, _ = instructions[i]
    if opcode == 'acc': continue
    instructions[i][0] = 'jmp' if opcode == 'nop' else 'nop'
    result = run_instructions(instructions, silence_failures = True)
    if result is not None:
        print(result)
    instructions[i][0] = 'nop' if opcode == 'nop' else 'jmp'
