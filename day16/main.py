HEX = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_binary(hex):
    return "".join([HEX[char] for char in hex])


def parse_header(bits):
    content = bits
    version, content = to_decimal(content[0:3]), content[3:]
    type_id, content = to_decimal(content[0:3]), content[3:]

    length_id = None

    if not type_id == 4:
        length_id, content = to_decimal(content[0]), content[1:]

    return version, type_id, length_id, content


def parse_literal(bits):
    values = []
    content = bits

    start, value, content = parse_group(content)
    values.append(value)

    while start == "1":
        start, value, content = parse_group(content)
        values.append(value)

    binary = "".join(values)

    return to_decimal(binary), content


def parse_group(bits):
    return bits[0], bits[1:5], bits[5:]


def parse_message(bits):
    content = bits
    values = []
    version_sum = 0

    while to_decimal(content) > 0:
        version, type_id, length_id, content = parse_header(content)
        version_sum += version

        if length_id == None:
            value, content = parse_literal(content)
            values.append(value)

        if length_id == 0:
            length, content = parse_length_id_zero(content)

        if length_id == 1:
            npackets, content = parse_length_id_one(content)

    return version_sum, values


def parse_length_id_zero(bits):
    length = to_decimal(bits[:15])
    return length, bits[15:]


def parse_length_id_one(bits):
    npackets = to_decimal(bits[:11])
    return npackets, bits[11:]


def to_decimal(binary):
    return int(binary, 2)


def solve_part1(hex):
    return parse_message(hex_to_binary(hex))[0]


###


def parse(filename):
    with open(filename) as file:
        return file.read().strip()


def solve(filename):
    hex = parse(filename)
    part1 = solve_part1(hex)
    part2 = None  # solve_part1(full_matrix(matrix, 5))

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
