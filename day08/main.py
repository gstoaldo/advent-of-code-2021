LEN_UNIQUE = set([2, 3, 4, 7])


def count_unique_segments(output_values):
    return len([digit for digit in output_values if len(digit) in LEN_UNIQUE])


def count_output_unique_segments(input):
    return sum(count_unique_segments(output) for _, output in input)


###


def parse(filename):
    def parse_line(line):
        return tuple(map(lambda x: x.strip().split(" "), line.split("|")))

    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    input = parse(filename)
    part1 = count_output_unique_segments(input)

    return part1


if __name__ == "__main__":
    part1 = solve("input.txt")
    print(f"part1: {part1}")
