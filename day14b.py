import fileinput

chains = dict()
template = None
for key, line in enumerate(fileinput.input()):
    line = line.rstrip()
    if key == 0:
        template = line
        continue

    if line == '':
        continue

    exploded = line.split(" -> ")
    chains[exploded[0]] = exploded[1]


def template_to_state(template):
    state = (dict(), dict())

    for pos in range(len(template)):
        if template[pos] not in state[1]:
            state[1][template[pos]] = 0

        state[1][template[pos]] += 1

    for pos in range(len(template) - 1):
        chain = template[slice(pos, pos + 2)]
        # polymer = chains[chain]

        if chain not in state[0]:
            state[0][chain] = 0

        state[0][chain] += 1

    return state


def apply_polymer(state):
    new_state = (dict(), state[1])
    print(state[0])
    for chain in state[0]:
        value = state[0][chain]
        # print("Chain", chain, "Value", value)
        part1 = chain[0] + chains[chain]
        part2 = chains[chain] + chain[1]

        if chains[chain] not in new_state[1]:
            new_state[1][chains[chain]] = 0

        # print(part1, part2, chain, chains[chain], value)
        new_state[1][chains[chain]] += value

        if part1 not in new_state[0]:
            new_state[0][part1] = 0

        if part2 not in new_state[0]:
            new_state[0][part2] = 0

        # print(part1, part2)
        new_state[0][part1] += value
        new_state[0][part2] += value
    return new_state


current_state = template_to_state(template)

for x in range(40):
    current_state = apply_polymer(current_state)

print(max(current_state[1].values()) - min(current_state[1].values()))
