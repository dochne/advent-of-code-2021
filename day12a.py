import fileinput

graph = {}
for line in fileinput.input():
    node1, node2 = line.rstrip().split("-")
    if node1 not in graph:
        graph[node1] = set()
    if node2 not in graph:
        graph[node2] = set()

    graph[node1].add(node2)
    graph[node2].add(node1)


def is_large_cave(node):
    return node.upper() == node


def recurse_paths(node, route):
    route.append(node)

    paths = []
    if node == 'end':
        paths.append(route)

        return paths

    for cave in graph[node]:
        if is_large_cave(cave) or cave not in route:
            paths = paths + recurse_paths(cave, list(route))

    return paths


result = recurse_paths('start', [])

print(len(result))
