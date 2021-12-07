import fileinput
from array import array


def build_tuple(string):
    _list = string.split(",")
    return int(_list[0]), int(_list[1])


def calc_step(pos_1, pos_2):
    if pos_1 == pos_2:
        return 0
    elif pos_1 < pos_2:
        return 1
    else:
        return -1


def calc_distance(vector1, vector2):
    vertical = max(vector1[1], vector2[1]) - min(vector1[1], vector2[1])
    horizontal = max(vector1[0], vector2[0]) - min(vector1[0], vector2[0])
    return max(vertical, horizontal)


max_x: int = 0
max_y: int = 0
vectors = []
for line in fileinput.input():
    split = line.rstrip().split(' -> ')
    vector = (build_tuple(split[0]), build_tuple(split[1]))
    max_x = max(max_x, vector[0][0], vector[1][0])
    max_y = max(max_y, vector[0][1], vector[1][1])
    vectors.append(vector)

# grid = [0 *]
grid = []
for y in range(max_y + 1):
    grid.append(array('i', (0,) * (max_x + 1)))

for vector in vectors:
    distance = calc_distance(vector[0], vector[1])
    x_step = calc_step(vector[0][0], vector[1][0])
    y_step = calc_step(vector[0][1], vector[1][1])

    for i in range(distance + 1):
        grid[vector[0][1] + (y_step * i)][vector[0][0] + (x_step * i)] += 1

total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 0:
            print('.', end='')
        else:
            print(grid[y][x], end='')
            if grid[y][x] > 1:
                total += 1

    print("")

print(total)
