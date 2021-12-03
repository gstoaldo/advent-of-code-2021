def count_bits(input):
    zero_count = [0 for _ in range(len(input[0]))]

    for binary in input:
        for i in range(len(binary)):
            if binary[i] == "0":
                zero_count[i] += 1

    one_count = [len(input) - zc for zc in zero_count]

    return zero_count, one_count


def calc_rates(zero_count, one_count):
    gamma_rate_binary = ""
    epsilon_rate_binary = ""

    for (zero, one) in zip(zero_count, one_count):
        gamma_rate_binary += "0" if zero >= one else "1"
        epsilon_rate_binary += "0" if zero < one else "1"

    return (
        (gamma_rate_binary, binary_to_decimal(gamma_rate_binary)),
        (epsilon_rate_binary, binary_to_decimal(epsilon_rate_binary)),
    )


def binary_to_decimal(binary):
    return int(binary, 2)


def calc_power_consuption(input):
    zero_count, one_count = count_bits(input)
    ((_, gamma_rate), (_, epsilon_rate)) = calc_rates(zero_count, one_count)

    return gamma_rate * epsilon_rate


def read_file(filename):
    def parse_line(line):
        return line.rstrip()

    with open(filename) as file:
        lines = file.readlines()
        data = map(parse_line, lines)

    return list(data)


def solve(filename):
    input = read_file(filename)
    part1_answer = calc_power_consuption(input)

    return part1_answer


if __name__ == "__main__":
    part1_answer = solve("input.txt")
    print(part1_answer)
