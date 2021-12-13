import fileinput

grid = []
for line in fileinput.input():
    grid.append(list(map(lambda x: int(x), list(line.rstrip()))))


def print_grid():
    for row in grid:
        print(''.join([str(x) if x != -1 else '.' for x in row]))


def increment_grid(x, y):
    total = 0
    if -1 < y < len(grid) and -1 < x < len(grid[y]):
        grid[y][x] += 1
        if grid[y][x] == 10:
            total += 1
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:
                    total += increment_grid(x + x_offset, y + y_offset)
    return total


flashes = 0
for i in range(100):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            flashes += increment_grid(x, y)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] > 9:
                grid[y][x] = 0

print_grid()
print(flashes)
