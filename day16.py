def perform_op(opcode, r0, r1):
    if r0 is None:
        return r1

    if opcode == 0:
        return r0 + r1
    elif opcode == 1:
        return r0 * r1
    elif opcode == 2:
        return min(r0, r1)
    elif opcode == 3:
        return max(r0, r1)
    elif opcode == 5:
        return r0 > r1
    elif opcode == 6:
        return r0 < r1
    elif opcode == 7:
        return r0 == r1


# returns:
# (next index to decode, value returned by operations, sum of packet versions)
def loader(text, index):
    version = int(text[index:index+3], 2)
    type_id = int(text[index+3:index+6], 2)

    if type_id == 4:
        index += 6
        ret = 0

        while ret == 0 or text[index - 5] != '0':
            ret = ret * 16 + int(text[index+1:index+5], 2)
            index += 5

    else:
        length_type_id = int(text[index+6], 2)
        ret = None

        if length_type_id == 0:
            length = int(text[index+7:index+22], 2)
            index += 22
            index_max = index + length

            while index < index_max:
                index, packet_version, packet_ret = loader(text, index)
                version += packet_version
                ret = perform_op(type_id, ret, packet_ret)
        else:
            length = int(text[index+7:index+18], 2)
            index += 18

            for _ in range(length):
                index, packet_version, packet_ret = loader(text, index)
                version += packet_version
                ret = perform_op(type_id, ret, packet_ret)

    return index, version, ret


with open('day16.txt', 'r') as text:
    hex_conv = ['0000', '0001', '0010', '0011',
                '0100', '0101', '0110', '0111',
                '1000', '1001', '1010', '1011',
                '1100', '1101', '1110', '1111']
    bin_str = ""
    for x in text.read().strip():
        bin_str = bin_str + hex_conv[int(x, 16)]

    _, part1, part2 = loader(bin_str, 0)
    print(part1)
    print(part2)
