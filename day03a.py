import fileinput

inputs = []
for line in fileinput.input():
    inputs.append(line.rstrip())

total = []
for index in range(0, len(inputs[0])):
    total.append(round(sum(map(lambda row: int(row[index]), inputs)) / len(inputs)))

most_common = int(''.join(map(lambda row: str(row), total)), 2)
least_common = int(''.join(map(lambda row: str((row + 1) % 2), total)), 2)

print(most_common, least_common, most_common * least_common)

