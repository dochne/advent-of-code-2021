import fileinput

lines = []
for line in fileinput.input():
    lines.append(list(line.rstrip()))

param_map = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}


def solve(line):
    stack = []
    for char in line:
        if char in param_map.keys():
            stack.append(char)
        else:
            expected = param_map[stack.pop()]
            if expected != char:
                return None

    stack.reverse()
    value = 0
    for char in stack:
        value = value * 5
        if char == '(':
            value += 1
        elif char == '[':
            value += 2
        elif char == '{':
            value += 3
        elif char == '<':
            value += 4

    return value


scores = []
for line in lines:
    result = solve(line)
    if result is not None:
        scores.append(result)

scores.sort()

half_way = (len(scores) / 2) - 0.5
print(scores[(int(half_way))])
