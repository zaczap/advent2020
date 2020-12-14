#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

path_to_input = sys.argv[1]

trees = []
with open(path_to_input) as input_file:
    for line in input_file:
        trees.append(line.strip())

def find_tree_burden(trees, slope):
    position = [0, 0]

    n = len(trees)
    m = len(trees[0])
    n_trees = 0

    while position[1] < n - 1:
        position[0], position[1] = position[0] + slope[0], position[1] + slope[1]
        if position[0] >= m:
            position[0] = position[0] % m
        if trees[position[1]][position[0]] == '#':
            n_trees += 1
    
    return n_trees

print(find_tree_burden(trees, [3, 1]))

slopes = [[1,1], [3,1], [5,1], [7,1], [1, 2]]
product = 1
for slope in slopes:
    burden = find_tree_burden(trees, slope)
    print("Burden for slope {0} is {1}".format(slope, burden))
    product *= burden

print(product)

