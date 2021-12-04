import fileinput

instructions = []
for line in fileinput.input():
    instructions.append(line.rstrip().split(" "))

depth: int = 0
distance: int = 0
aim: int = 0

for instruction in instructions:
    rule = instruction[0]
    quantity: int = int(instruction[1])

    if rule == 'forward':
        distance += quantity
        depth += aim * quantity
    elif rule == 'down':
        aim += quantity
    elif rule == 'up':
        aim -= quantity

print(depth * distance)




