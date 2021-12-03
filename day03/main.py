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


def calc_power_consuption(input):
    zero_count, one_count = count_bits(input)
    ((_, gamma_rate), (_, epsilon_rate)) = calc_rates(zero_count, one_count)

    return gamma_rate * epsilon_rate


def filter_by_bit_count(input, index, reverse_criteria=False):
    zero_count, one_count = count_bits(input)

    criteria = "0" if zero_count[index] > one_count[index] else "1"

    if reverse_criteria:
        criteria = "1" if criteria == "0" else "0"

    return [binary for binary in input if binary[index] == criteria]


def calc_rating(input, reverse_criteria=False):
    filtered_input = input
    size = len(input[0])

    for index in range(size):
        filtered_input = filter_by_bit_count(filtered_input, index, reverse_criteria)
        if len(filtered_input) == 1:
            break

    rating_binary = filtered_input[0]

    return rating_binary, binary_to_decimal(rating_binary)


def calc_o2_generator_rating(input):
    return calc_rating(input, False)


def calc_co2_scrubber_rating(input):
    return calc_rating(input, True)


def calc_life_support_rating(input):
    (_, o2) = calc_o2_generator_rating(input)
    (_, co2) = calc_co2_scrubber_rating(input)

    return o2 * co2


def binary_to_decimal(binary):
    return int(binary, 2)


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
    part2_answer = calc_life_support_rating(input)

    return part1_answer, part2_answer


if __name__ == "__main__":
    part1_answer, part2_answer = solve("input.txt")
    print(f"part1: {part1_answer}")
    print(f"part2: {part2_answer}")
