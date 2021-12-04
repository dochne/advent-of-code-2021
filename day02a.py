import fileinput

instructions = []
for line in fileinput.input():
    instructions.append(line.rstrip().split(" "))

depth: int = 0
distance: int = 0

for instruction in instructions:
    rule = instruction[0]
    quantity: int = int(instruction[1])

    if rule == 'forward':
        distance += quantity
    elif rule == 'down':
        depth += quantity
    elif rule == 'up':
        depth -= quantity

print(depth * distance)




