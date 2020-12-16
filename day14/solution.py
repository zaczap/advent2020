#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import math
from collections import defaultdict
from itertools import product

path_to_input = sys.argv[1]

def apply_mask(mask, value):
    source_string = "{0:b}".format(value).zfill(36)
    destination_string = "".join([flag if flag != 'X' else source for flag, source in zip(list(mask), list(source_string))])
    return int(destination_string, 2)

def parse_mask(mask):
    groups = []
    buffer = []
    for x in mask:
        if x == 'X':
            if len(buffer) == 0:
                groups.append('X')
            else:
                groups.append(''.join(buffer))
                groups.append('X')
                buffer = []
        else:
            buffer.append(x)
    if len(buffer) > 0:
        groups.append(''.join(buffer))
        buffer = []
    return groups

memory = defaultdict(int)
mask = 'X'*36
instructions = []
with open(path_to_input) as input_file:
    for line in input_file:
        instruction, value = line.strip().split(' = ')
        instructions.append((instruction, value))
        if instruction == 'mask':
            mask = value
            pass
        else:
            address = int(instruction[4:(len(instruction)-1)])
            recoded = apply_mask(mask, int(value))
            memory[address] = recoded
            print("mem[{}] = mask({}) -> {} w/ mask {}".format(address, int(value), recoded, mask))

print(sum(memory.values()))

memory = defaultdict(int) # reset device memory

for instruction, value in instructions:
    if instruction == 'mask':
        mask = value
    else:
        decimal_address = int(instruction[4:(len(instruction)-1)])
        mask_fragments = parse_mask(mask)
        binary_address = "{0:b}".format(decimal_address).zfill(36)
        value = int(value)
        i = 0
        address_buffer = []
        while i < len(binary_address):
            for fragment in mask_fragments:    
                if fragment == 'X':
                    address_buffer.append(['0', '1'])
                    i += 1
                else:
                    length = len(fragment)
                    original_address = binary_address[i:(i+length)]
                    masked_address = "".join([o if flag == '0' else '1' for (o, flag) in zip(original_address, fragment)])
                    address_buffer.append([masked_address])
                    i += length 

        for binary_address in product(*address_buffer):
            binary_address = "".join(binary_address)
            decimal_address = int(binary_address, 2)
            memory[decimal_address] = value
            print("{} <- {}".format(binary_address, value))
        
print(sum(memory.values()))