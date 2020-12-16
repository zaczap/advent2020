#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from collections import defaultdict
from itertools import chain

input_array = [15,5,1,4,7,0]
timepoint_last_said = defaultdict(list)

target = 30000000 #  2020

for t in range(target):
    if t < len(input_array):
        last_said = input_array[t]
        timepoint_last_said[input_array[t]].append(t)
    else:
        if len(timepoint_last_said[last_said]) > 1:
            # we've said that number before!
            next_number = (t-1) - timepoint_last_said[last_said][-2]
        else:
            # that was the first time we've said that number
            next_number = 0
        last_said = next_number
        timepoint_last_said[next_number].append(t)
        if t == 2019: print("t = {} -> {} ({}%)".format(t, last_said, round((t+1) / target * 100, 2)))
        if t % 1000000 == 0: print("t = {} -> {} ({}%)".format(t, last_said, round((t+1) / target * 100, 2)))

print(last_said)


