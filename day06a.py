import fileinput

depths = []
for line in fileinput.input():
    depths.append(int(line.rstrip()))

num_increased: int = 0
for index in range(1, len(depths)):
    last_depth = depths[index - 1]
    depth = depths[index]

    if last_depth < depth:
        num_increased = num_increased + 1

print(num_increased)





