from sys import stdin
from bitstring import BitStream

hex_string = stdin.readlines()[0].rstrip()


def product(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def parse_packet(stream, depth):
    packet_version = stream.read('uint:3')
    packet_type = stream.read('uint:3')
    sub_packets = []

    if packet_type == 4:
        value = ''
        more_packets = True
        while more_packets:
            more_packets = stream.read('bool:1')
            value += stream.read('bin:4')
        return int(value, 2)

    length_type = stream.read('uint:1')
    if length_type == 0:
        packet_len = stream.read('uint:15')
        start_pos = bit_stream.pos
        while bit_stream.pos < start_pos + packet_len:
            sub_packets.append(parse_packet(stream, depth + 1))

    elif length_type == 1:
        total_packets = stream.read('uint:11')
        for x in range(total_packets):
            sub_packets.append(parse_packet(stream, depth + 1))

    print(packet_type, packet_version, sub_packets)
    if packet_type == 0:
        return sum(sub_packets)
    elif packet_type == 1:
        return product(sub_packets)
    elif packet_type == 2:
        return min(sub_packets)
    elif packet_type == 3:
        return max(sub_packets)
    elif packet_type == 5:
        return 1 if sub_packets[0] > sub_packets[1] else 0
    elif packet_type == 6:
        return 1 if sub_packets[0] < sub_packets[1] else 0
    elif packet_type == 7:
        print(''.join((' ',) * depth), sub_packets)
        return 1 if sub_packets[0] == sub_packets[1] else 0
    raise 'Undefined behaviour'


bit_stream = BitStream('0x' + hex_string)

print(parse_packet(bit_stream, 0))
