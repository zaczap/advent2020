#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from itertools import chain, product
from collections import defaultdict

def get_neighbors(x, y, z, w):
    offsets = [(x+dx, y+dy, z+dz, w+dw) for dx,dy,dz,dw in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1])  if not all([dx == 0, dy == 0, dz == 0, dw == 0])]
    return offsets

path_to_input = sys.argv[1]

grid = defaultdict(bool) # (x, y, z, w) --> Inactive/Active

with open(path_to_input) as input_file:
    y = 0
    for line in input_file:
        for x, state in enumerate(list(line.rstrip())):
            if state == '#':
                grid[(x, y, 0, 0)] = True
        y += 1

def evolve_grid(grid):
    next_grid = defaultdict(bool)
    # adaptive sampling of the hypercube
    xlim = max(map(abs, [x for (x,y,z,w) in grid.keys()])) + 2
    ylim = max(map(abs, [y for (x,y,z,w) in grid.keys()])) + 2
    zlim = max(map(abs, [z for (x,y,z,w) in grid.keys()])) + 2
    wlim = max(map(abs, [w for (x,y,z,w) in grid.keys()])) + 2
    for x0, y0, z0, w0 in product(range(-xlim, xlim), range(-ylim, ylim), range(-zlim, zlim), range(-wlim, wlim)):
        current_state = grid[(x0, y0, z0, w0)]
        n_active_neighbors = 0
        for x, y, z, w in get_neighbors(x0, y0, z0, w0):
            if grid[(x, y, z, w)]: n_active_neighbors += 1
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
            next_grid[(x0, y0, z0, w0)] = next_state
    
    return next_grid

n_cycles = 6
for cycle in range(n_cycles):
    if cycle == 0:
        next_grid = evolve_grid(grid)
    else:
        next_grid = evolve_grid(next_grid)
    print("Finished {} epoch".format(cycle + 1))
    
print(sum(next_grid.values()))




