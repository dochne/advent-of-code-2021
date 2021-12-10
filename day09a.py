import fileinput

grid = []
for line in fileinput.input():
    grid.append(list(map(lambda x: int(x), list(line.rstrip()))))

risk_level = 0
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
            risk_level += grid[y][x] + 1
            print((x, y), "is a low point", grid[y][x])

print(risk_level)
