#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import math

path_to_input = sys.argv[1]

instructions = []
with open(path_to_input) as input_file:
    for line in input_file:
        instruction = line.strip()
        code, value = instruction[0], int(instruction[1:])
        instructions.append((code, value))

position = [0,0] # east <-> west, north <-> south
angle = 0

for (code, value) in instructions:
    if code == 'F':
        angle = angle % 360
        if angle == 0:
            position[0] += value # move east
        elif angle == 90:
            position[1] += value # move north
        elif angle == 180:
            position[0] -= value # move west
        elif angle == 270:
            position[1] -= value # move south
    elif code == 'E':
        position[0] += value # move east
    elif code == 'N':
        position[1] += value # move north
    elif code == 'W':            
        position[0] -= value # move west
    elif code == 'S':            
        position[1] -= value # move south
    elif code == 'L':
        angle += value
    elif code == 'R':
        angle -= value

print(sum(map(abs, position)))

position = [0,0]
waypoint = [10,1] # relative to position

for (code, value) in instructions:
    if code == 'F':
        position[0] += waypoint[0]*value
        position[1] += waypoint[1]*value
    elif code == 'E':
        waypoint[0] += value # move waypoint east
    elif code == 'N':
        waypoint[1] += value # move waypoint north
    elif code == 'W':            
        waypoint[0] -= value # move waypoint west
    elif code == 'S':            
        waypoint[1] -= value # move waypoint south
    elif code == 'L' or code == 'R':
        angle = value*math.pi/180*(-1 if code == 'R' else 1)
        updated = [0, 0]
        updated[0] = int(round(waypoint[0]*math.cos(angle) - waypoint[1]*math.sin(angle)))
        updated[1] = int(round(waypoint[0]*math.sin(angle) + waypoint[1]*math.cos(angle)))
        waypoint[0], waypoint[1] = updated[0], updated[1]

print(sum(map(abs, position)))
