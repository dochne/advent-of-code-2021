import fileinput
from array import array


def build_tuple(string):
    _list = string.split(",")
    return int(_list[0]), int(_list[1])


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
    if vector[0][0] == vector[1][0]:
        lowest = min(vector[0][1], vector[1][1])
        highest = max(vector[0][1], vector[1][1]) + 1

        for y in range(lowest, highest):
            grid[y][vector[0][0]] += 1

    if vector[0][1] == vector[1][1]:
        lowest = min(vector[0][0], vector[1][0])
        highest = max(vector[0][0], vector[1][0]) + 1

        for x in range(lowest, highest):
            grid[vector[0][1]][x] += 1

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
exit(0)
# max_horizontal
num_increased: int = 0
for index in range(1, len(depths)):
    last_depth = depths[index - 1]
    depth = depths[index]

    if last_depth < depth:
        num_increased = num_increased + 1

print(num_increased)
