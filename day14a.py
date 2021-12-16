import fileinput

chains = dict()
start_template = None
for key, line in enumerate(fileinput.input()):
    line = line.rstrip()
    if key == 0:
        start_template = line
        continue

    if line == '':
        continue

    exploded = line.split(" -> ")
    chains[exploded[0]] = exploded[1]


def apply_polmer(template):
    result = [template[0]]
    for pos in range(len(template) - 1):
        polymer = template[slice(pos, pos + 2)]
        # print(polymer, chains[polymer])
        result.append(chains[polymer])
        result.append(template[pos + 1])
    return ''.join(result)


current_template = start_template
for x in range(10):
    # print(current_template)
    current_template = apply_polmer(current_template)

print(current_template)
output = dict()
for pos in range(len(current_template)):
    char = current_template[pos]
    if char not in output:
        output[char] = 0

    output[char] += 1

print(max(output.values()) - min(output.values()))
print(output)
