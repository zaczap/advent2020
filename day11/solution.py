#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
from copy import deepcopy

path_to_input = sys.argv[1]

grid = []
with open(path_to_input) as input_file:
    for line in input_file:
        grid.append(list(line.strip()))

original_grid = deepcopy(grid)

def plot(grid):
    for row in grid:
        print("".join(row))

adj_memory = {}
def get_adj_neighbors(grid, r, c):
    if (r,c) in adj_memory: return adj_memory[(r,c)]
    nrow = len(grid)
    ncol = len(grid[0])
    neighbors = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
    valid_neighbors = []
    for neighbor in neighbors:
        nr, nc = neighbor
        if (nr < 0 or nr >= nrow) or (nc < 0 or nc >= ncol): 
            continue 
        valid_neighbors.append(neighbor)
    adj_memory[(r,c)] = valid_neighbors
    return valid_neighbors

vis_memory = {}
def get_vis_neighbors(grid, r, c):
    if (r,c) in vis_memory: return vis_memory[(r,c)]
    nrow = len(grid)
    ncol = len(grid[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    valid_neighbors = []
    for direction in directions:
        dr, dc = direction
        b = 1
        while True:
            possible_neighbor = (r + b*dr, c + b*dc)
            nr, nc = possible_neighbor
            if (nr < 0 or nr >= nrow) or (nc < 0 or nc >= ncol):
                #print("Failed: {}".format(possible_neighbor))
                break # no neighbor in this direction
            if grid[nr][nc] in ('#', 'L'):
                #print("Passed: {}".format(possible_neighbor))
                valid_neighbors.append((nr,nc))
                break
            b += 1    
    vis_memory[(r,c)] = valid_neighbors
    return valid_neighbors

def get_neighbor_values(grid, r, c, type):
    if type == 'adj':
        neighbors = get_adj_neighbors(grid, r, c)
    elif type == 'vis':
        neighbors = get_vis_neighbors(grid, r, c)
    values = []
    for neighbor in neighbors:
        nr, nc = neighbor
        values.append(grid[nr][nc])
    return values

def evolve_grid(grid, type, tolerance):
    nrow = len(grid)
    ncol = len(grid[0])
    new_grid = []
    for r in range(nrow):
        new_grid.append(['.']*ncol)
    n_modified = 0
    for r in range(nrow):
        for c in range(ncol):
            values = get_neighbor_values(grid, r, c, type)
            #print(r, c, values)
            if grid[r][c] == 'L' and all(value != '#' for value in values):
                n_modified += 1
                new_grid[r][c] = '#'
            elif grid[r][c] == '#' and sum(value == '#' for value in values) >= tolerance:
                n_modified += 1
                new_grid[r][c] = 'L'
            else:
                new_grid[r][c] = grid[r][c]
    return (new_grid, n_modified == 0)

plot(grid)

print(get_adj_neighbors(grid, 0, 1))
print(get_neighbor_values(grid, 0, 1, 'adj'))
print(get_neighbor_values(grid, 0, 0, 'adj'))

plot(grid)
i = 0
while True:
    i = i + 1
    grid, status = evolve_grid(grid, 'adj', tolerance = 4)
    if status:
        print("Took {} epochs".format(i))
        plot(grid)
        break

n_occupied = 0
for row in grid:
    n_occupied += sum(seat == '#' for seat in row)
print(n_occupied)

grid = deepcopy(original_grid)

plot(grid)
i = 0
while True:
    i = i + 1
    grid, status = evolve_grid(grid, 'vis', tolerance = 5)
    if status:
        print("Took {} epochs".format(i))
        plot(grid)
        break

n_occupied = 0
for row in grid:
    n_occupied += sum(seat == '#' for seat in row)
print(n_occupied)
