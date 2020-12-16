#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import math

path_to_input = sys.argv[1]

with open(path_to_input) as input_file:
    minimum_time = int(input_file.readline().strip())
    raw_buses = [(int(x) if x != 'x' else -1) for x in input_file.readline().strip().split(',')]
    buses = [x for x in raw_buses if x != -1]

## Part 1:

first_time = [math.ceil(float(minimum_time)/float(t))*t for t in buses]

for bus_id, time in sorted(zip(buses, first_time), key = lambda t:t[1]):
    print(bus_id, time, time - minimum_time, (time - minimum_time) * bus_id)
    break

## Part 2:

time, step = 0, 1
offsets = [x for x in enumerate(raw_buses) if x[1] != -1]
for i in range(len(offsets) - 1):
    next_bus_offset, next_bus_id  = offsets[i+1]
    bus_offset, bus_id = offsets[i] 
    step *= bus_id
    n_steps = 0
    while (time + next_bus_offset) % next_bus_id != 0:
        n_steps += 1
        time += step

print(time)




