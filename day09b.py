import fileinput

grid = []
for line in fileinput.input():
    grid.append(list(map(lambda x: int(x), list(line.rstrip()))))

low_points = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        is_lowest = True
        for x_offset, y_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (x + x_offset >= len(grid[y])) or (y + y_offset >= len(grid)):
                continue

            if grid[y + y_offset][x + x_offset] <= grid[y][x]:
                is_lowest = False
                break

        if is_lowest:
            low_points.append((x, y))


def expand_grid(x, y):
    total = 0
    for x_offset, y_offset in [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)]:
        if (x + x_offset >= len(grid[y])) or (y + y_offset >= len(grid)) or y + y_offset < 0 or x + x_offset < 0:
            continue

        value = grid[y + y_offset][x + x_offset]
        if value < 9 and value != -1:
            grid[y + y_offset][x + x_offset] = -1
            total += 1 + expand_grid(x + x_offset, y + y_offset)

    return total


def print_grid():
    for row in grid:
        print(''.join([str(x) if x != -1 else '.' for x in row]))


output = []
for point in low_points:
    output.append(expand_grid(point[0], point[1]))

output.sort(reverse=True)

response = 1
for x in output[slice(0, 3)]:
    response = response * x

print_grid()
print(response)
