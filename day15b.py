import fileinput
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

original_matrix = []
for line in fileinput.input():
    original_matrix.append(list(map(lambda x: int(x), list(line.rstrip()))))

matrix = []
for y_inc in range(5):
    for y in range(len(original_matrix)):
        line = []
        for x_inc in range(5):
            for x in range(len(original_matrix[y])):
                new_value = original_matrix[y][x] + y_inc + x_inc
                if new_value > 9:
                    new_value -= 9
                line.append(new_value)
        matrix.append(line)

grid = Grid(matrix=matrix)

start = grid.node(0, 0)
end = grid.node(len(matrix[0]) - 1, len(matrix[0]) - 1)

finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(path)
print(grid.grid_str(path=path, start=start, end=end))

weight = 0
for node in path:
    if node != (0, 0):
        weight += matrix[node[1]][node[0]]

print(weight)
