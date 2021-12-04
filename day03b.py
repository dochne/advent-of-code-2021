import fileinput
import math

inputs = []
for line in fileinput.input():
    inputs.append(line.rstrip())


def filter_oxygen(data, pos=0):
    if len(data) == 1:
        return data[0]

    most_common_bit = math.floor(sum(map(lambda row: int(row[pos]), data)) / len(data) + 0.5)
    new_list = list(filter(lambda row: int(row[pos]) == most_common_bit, data))
    return filter_oxygen(new_list, pos + 1)


def co2_scrubber(data, pos=0):
    if len(data) == 1:
        return data[0]

    most_common_bit = math.floor(sum(map(lambda row: int(row[pos]), data)) / len(data) + 0.5)
    new_list = list(filter(lambda row: int(row[pos]) != most_common_bit, data))
    return co2_scrubber(new_list, pos + 1)


print(int(filter_oxygen(inputs), 2) * int(co2_scrubber(inputs), 2))
