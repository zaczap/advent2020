#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from itertools import chain, product
from collections import defaultdict
import numpy as np

def get_neighbors(x, y, z):
    offsets = [(x+dx, y+dy, z+dz) for dx,dy,dz in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])  if not all([dx == 0, dy == 0, dz == 0])]
    return offsets

def zslice(grid, z):
    xpoints = [x for (x,y,z) in grid.keys()]
    ypoints = [y for (x,y,z) in grid.keys()]
    minimum = min(*xpoints, *ypoints)
    maximum = max(*xpoints, *ypoints)
    print(minimum, maximum)
    for y in range(minimum, maximum+1):
        line = []
        for x in range(minimum, maximum+1):
            line.append('#' if grid[(x, y, z)] else '.')
        print("".join(line))


path_to_input = sys.argv[1]

grid = defaultdict(bool) # (x, y, z) --> Inactive/Active

with open(path_to_input) as input_file:
    y = 0
    for line in input_file:
        for x, state in enumerate(list(line.rstrip())):
            if state == '#':
                grid[(x, y, 0)] = True
        y += 1

def evolve_grid(grid, cube_size):
    next_grid = defaultdict(bool)
    for x0, y0, z0 in product(range(-cube_size, cube_size), range(-cube_size, cube_size), range(-cube_size, cube_size)):
        current_state = grid[(x0, y0, z0)]
        n_active_neighbors = 0
        for x, y, z in get_neighbors(x0, y0, z0):
            if grid[(x, y, z)]: n_active_neighbors += 1
        if current_state:
            if n_active_neighbors == 2 or n_active_neighbors == 3:
                next_state = True
            else:
                next_state = False
        else:
            if n_active_neighbors == 3:
                next_state = True
            else:
                next_state = False
        if next_state:
            next_grid[(x0, y0, z0)] = next_state
    
    return next_grid

n_cycles = 6
grid_size = 25
for cycle in range(n_cycles):
    if cycle == 0:
        next_grid = evolve_grid(grid, grid_size)
    else:
        next_grid = evolve_grid(next_grid, grid_size)

print(sum(next_grid.values()))




