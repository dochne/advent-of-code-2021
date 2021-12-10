import fileinput


def letter_to_number(string):
    return int(pow(2, ord(string[0]) - 96) / 2)


def list_to_number(_list):
    return sum(map(lambda x: letter_to_number(x), _list))


total_segments_in_number = []
for i in range(128):
    count = 0
    v = i
    while v > 0:
        count = count + 1
        v = v & (v - 1)
    total_segments_in_number.append(count)

lines = []
for line in fileinput.input():
    split = line.rstrip().split("|")
    segments = list(map(lambda x: list_to_number(list(x)), split[0].strip().split(' ')))
    output = list(map(lambda x: list_to_number(list(x)), split[1].strip().split()))
    lines.append((segments, output))

total = 0
for line in lines:
    for digit in line[1]:
        if total_segments_in_number[digit] in [2, 4, 3, 7]:
            total += 1

print(total)

exit(0)
# print(chr(97))
# exit(0)
# def list_to_binary(numbers):
#     //chr(1 ^ 2)


lines = []
for line in fileinput.input():
    split = line.rstrip().split("|")
    segments = list(map(lambda x: set(x), split[0].strip().split(' ')))
    output = list(map(lambda x: set(x), split[1].strip().split()))
    lines.append((segments, output))

    print(segments)

print(lines)
exit(0)


def update_state(state, segment, letters):
    for letter in letters:
        state.update({letter: state.get(letter).intersection(segment)})
    return state


total = 0
all_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
for (segments, output) in lines:
    state = {
        "a": all_letters,
        "b": all_letters,
        "c": all_letters,
        "d": all_letters,
        "e": all_letters,
        "f": all_letters,
        "g": all_letters
    }

    for segment in segments:
        # Number 1
        if len(segment) == 2:
            state = update_state(state, segment, ['c', 'f'])
            # total += 1

        # Number 7
        elif len(segment) == 3:
            state = update_state(state, segment, ['a', 'c', 'f'])
            # total += 1

        # Number 4
        elif len(segment) == 4:
            state = update_state(state, segment, ['b', 'c', 'd', 'f'])
            # total += 1

    # for digit in output:
    #     if state.get()
    # Number 8
    # elif len(segment) == 8:
    #     total += 1
    print(output)
    # Number 9 OR number 0
    # elif len(segment) == 6:
    # state.update({'e': state.get('e').intersection(all_letters.difference(segment))})
    # state.update({
    #     'a': state.get('a').intersection(segment),
    #     'c': state.get('c').intersection(segment),
    #     'f': state.get('f').intersection(segment),
    # })

for key, value in state.items():
    print(key, ':', value)

print(total)
# state[f] = state.f.intersection(segment)
# print(state)

# num_increased: int = 0
# for index in range(1, len(depths)):
#     last_depth = depths[index - 1]
#     depth = depths[index]
#
#     if last_depth < depth:
#         num_increased = num_increased + 1
#
# print(num_increased)
