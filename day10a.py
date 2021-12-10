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
                return char
    return None


score = 0
for line in lines:
    result = solve(line)
    if result == ')':
        score += 3
    elif result == ']':
        score += 57
    elif result == '}':
        score += 1197
    elif result == '>':
        score += 25137

print(score)
exit(0)
