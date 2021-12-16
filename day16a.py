from sys import stdin
from dataclasses import dataclass
from bitstring import BitStream
from typing import List

hex_string = stdin.readlines()[0].rstrip()


@dataclass
class Packet:
    Version: int
    Type: int
    Value: int
    Packets: List['Packet']


def parse_packet(stream):
    packet_version = stream.read('uint:3')
    packet_type = stream.read('uint:3')
    sub_packets = []

    value = 0
    if packet_type == 4:
        value = ''
        more_packets = True
        while more_packets:
            more_packets = stream.read('bool:1')
            value += stream.read('bin:4')

        value = int(value, 2)
    else:
        length_type = stream.read('uint:1')
        if length_type == 0:
            packet_len = stream.read('uint:15')
            start_pos = bit_stream.pos
            while bit_stream.pos < start_pos + packet_len:
                sub_packets.append(parse_packet(stream))

        elif length_type == 1:
            total_packets = stream.read('uint:11')
            for x in range(total_packets):
                sub_packets.append(parse_packet(stream))

    return Packet(packet_version, packet_type, value, sub_packets)


bit_stream = BitStream('0x' + hex_string)
packet = parse_packet(bit_stream)


def sum_packets(sub_packets):
    total_version = 0
    for packet in sub_packets:
        total_version += packet.Version
        total_version += sum_packets(packet.Packets)
    return total_version


print(sum_packets([packet]))
