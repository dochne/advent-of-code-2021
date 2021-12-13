import fileinput
import re
from array import array

dots = set()
folds = []
for line in fileinput.input():
    if line == '\n':
        continue

    match = re.search("fold along (y|x)=([0-9]*)", line)
    if match:
        folds.append((match[1], int(match[2])))
    else:
        dots.add(tuple([int(v) for v in line.split(",")]))


def print_grid(dot_array):
    max_x = 0
    max_y = 0
    for dot in dot_array:
        max_x = max(max_x, dot[0])
        max_y = max(max_y, dot[1])

    grid = []
    for y in range(max_y + 1):
        grid.append(array('b', (False,) * (max_x + 1)))

    for (x, y) in dot_array:
        grid[y][x] = True

    for y in range(len(grid)):
        print(''.join(map(lambda x: '#' if x else '.', grid[y])))

    print()


# print_grid(dots)
for fold in folds:
    print(fold)
    for dot in set(dots):
        dots.remove(dot)
        was = dot

        if fold[0] == 'x':
            if fold[1] < dot[0]:
                dot = (fold[1] - (dot[0] - fold[1]), dot[1])
        else:
            if fold[1] < dot[1]:
                dot = (dot[0], fold[1] - (dot[1] - fold[1]))

        dots.add(dot)

print_grid(dots)
