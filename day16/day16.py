def load_input():
    with open('./day16/input.txt', 'r') as f:
        x = f.readline().rstrip()
        return str(bin(int(x, 16))[2:].zfill(len(x) * 4))

def read_header(data):
    version = int(data[:3], 2)
    id = int(data[3:6], 2)

    return version, id

def read_literal_value(data):
    i = 6
    val = ''
    blocks = 0
    while True:
        blocks += 1
        val += data[i+1:i+5]

        if data[i] == '0':
            break
        
        i += 5
    
    return val, blocks

def read_literal_packet(packet):
    version, id = read_header(packet)

    if id == 4:
        literal_value, blocks = read_literal_value(packet)
        return 6 + blocks*5, (version, id, int(literal_value, 2))

def read_len(packet):
    if packet[6] == '0':
        return ('L', int(packet[7:7+15], 2))
    else:
        return ('P', int(packet[7:7+11], 2))

def read_l_packet(packet, l):
    version, id = read_header(packet)
    read_l = 22

    subpackets = []
    while read_l < l+22:
        pck_l, pck = read_packet(packet[read_l:])
        subpackets.append(pck)
        read_l += pck_l
        
    return read_l, (version, id, subpackets)

def read_p_packet(packet, c):
    version, id = read_header(packet)
    read_l = 18

    subpackets = []
    for i in range(c):
        pck_l, pck = read_packet(packet[read_l:])
        subpackets.append(pck)
        read_l += pck_l

    return read_l, (version, id, subpackets)

def read_packet(packet):
    _, id = read_header(packet)

    if id == 4:
        return read_literal_packet(packet)
    else:
        t, l = read_len(packet)
        if t == 'L':
            return read_l_packet(packet, l)
        else:
            return read_p_packet(packet, l)

data = load_input()

_, parsed = read_packet(data)

def calculate_version_sum(packet):
    if packet[1] == 4:
        return packet[0]
    else:
        return packet[0] + sum((calculate_version_sum(i) for i in packet[2]))

print(f'version_sum: {calculate_version_sum(parsed)}')

# -- p2

import math

def packet_value(packet):
    if packet[1] == 0:
        return sum(packet_value(i) for i in packet[2])
    elif packet[1] == 1:
        return math.prod(packet_value(i) for i in packet[2])
    elif packet[1] == 2:
        return min(packet_value(i) for i in packet[2])
    elif packet[1] == 3:
        return max(packet_value(i) for i in packet[2])
    elif packet[1] == 4:
        return packet[2]
    elif packet[1] == 5:
        a = packet_value(packet[2][0])
        b = packet_value(packet[2][1])
        if a > b:
            return 1
        else:
            return 0
    elif packet[1] == 6:
        a = packet_value(packet[2][0])
        b = packet_value(packet[2][1])
        if a < b:
            return 1
        else:
            return 0
    elif packet[1] == 7:
        a = packet_value(packet[2][0])
        b = packet_value(packet[2][1])
        if a == b:
            return 1
        else:
            return 0

print(f'packet value: {packet_value(parsed)}')