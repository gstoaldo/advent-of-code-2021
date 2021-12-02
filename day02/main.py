def step_parser_without_aim(step):
    command, value = step
    return {
        "forward": (0, value),
        "down": (1, value),
        "up": (1, -value),
    }[command]


def step_parser_with_aim(step):
    command, value = step
    return {
        "forward": (0, value),
        "down": (2, value),
        "up": (2, -value),
    }[command]


def calculate_final_position(
    steps, step_parser=step_parser_without_aim, aim_multiplier=0
):
    final_position = [0, 0, 0]

    for step in steps:
        axis, value = step_parser(step)
        final_position[axis] += value

        if axis == 0:
            final_position[1] += final_position[2] * value * aim_multiplier

    return final_position, position_product(final_position)


def position_product(position):
    return position[0] * position[1]


def read_file(filename):
    def parse_line(line):
        command, value = line.strip().split(" ")
        return (command, int(value))

    with open(filename) as file:
        lines = file.readlines()
        data = map(parse_line, lines)

    return list(data)


def solve(filename):
    input = read_file(filename)
    part1_answer = calculate_final_position(input, step_parser_without_aim, 0)
    part2_answer = calculate_final_position(input, step_parser_with_aim, 1)

    return part1_answer, part2_answer


if __name__ == "__main__":
    part1_answer, part2_answer = solve("input.txt")
    print(part1_answer, part2_answer)
