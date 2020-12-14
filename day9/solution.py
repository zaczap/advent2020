#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from collections import deque
from itertools import combinations

path_to_input = sys.argv[1]

numbers = []
with open(path_to_input) as input_file:
    for line in input_file:
        numbers.append(int(line.strip()))

def validate_numbers(numbers, preamble_length):
    working_set = deque(maxlen=preamble_length)
    for number in numbers:
        if len(working_set) < preamble_length:
            working_set.append(number)
        else:
            valid = False
            for pair in combinations(working_set, 2):
                if pair[0] + pair[1] == number:
                    valid = True
                    working_set.append(number)
                    break
            if not valid:
                print("Invalid number found: {}".format(number))
                return(number)


print(numbers)

invalid_number = validate_numbers(numbers, 25)

frame_found = False
frame_min = 0
frame_max = 0
for frame_start in range(len(numbers)):
    if frame_found: break
    for frame_end in range(len(numbers)):
        frame_sum = sum(numbers[frame_start:frame_end]) 
        if frame_sum == invalid_number:
            frame_found = True
            frame_min = min(numbers[frame_start:frame_end])
            frame_max = max(numbers[frame_start:frame_end])
            print("Frame found: {}".format(numbers[frame_start:frame_end]))
        if frame_sum < invalid_number: continue # expand frame
        if frame_sum > invalid_number: break # slide frame to left and restart

print("Min: {}\nMax: {}\nSum: {}".format(frame_min, frame_max, frame_min + frame_max))