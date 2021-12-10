import fileinput
import math
from array import array


def letter_to_number(string):
    return int(pow(2, ord(string[0]) - 96) / 2)


def number_to_letter(number):
    return chr(int(math.log(number) / math.log(2)) + 97)


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
for segments, output in lines:
    numbers = array('i', (0,) * 10)
    for segment in segments:
        seg_len = total_segments_in_number[segment]
        if seg_len == 2:
            numbers[1] = segment
        elif seg_len == 3:
            numbers[7] = segment
        elif seg_len == 4:
            numbers[4] = segment
        elif seg_len == 7:
            numbers[8] = segment

    for segment in segments:
        seg_len = total_segments_in_number[segment]
        if seg_len == 6:
            if numbers[4] & segment == numbers[4]:
                numbers[9] = segment
            elif numbers[1] & segment == numbers[1]:
                numbers[0] = segment
            else:
                numbers[6] = segment
        elif seg_len == 5:
            if segment & numbers[1] == numbers[1]:
                numbers[3] = segment
            elif total_segments_in_number[segment & numbers[4]] == 3:
                numbers[5] = segment
            else:
                numbers[2] = segment

    mapped_numbers = {}
    for i in range(len(numbers)):
        mapped_numbers[numbers[i]] = str(i)

    digits = []
    for digit in output:
        digits.append(mapped_numbers[digit])
    digits = int(''.join(digits))
    total += digits

print(total)

exit(0)
