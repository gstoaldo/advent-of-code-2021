def calculate_final_position(steps):
    final_position = [0, 0]

    for step in steps:
        axis, value = get_step_axis(step)
        final_position[axis] += value

    return final_position, position_product(final_position)


def get_step_axis(step):
    command, value = step
    return {
        "forward": (0, value),
        "down": (1, value),
        "up": (1, -value),
    }[command]


def read_file(filename):
    def parse_line(line):
        command, value = line.strip().split(" ")
        return (command, int(value))

    with open(filename) as file:
        lines = file.readlines()
        data = map(parse_line, lines)

    return list(data)


def position_product(position):
    return position[0] * position[1]


def solve(filename):
    input = read_file(filename)
    part1_answer = calculate_final_position(input)

    return part1_answer


if __name__ == "__main__":
    part1_answer = solve("input.txt")
    print(part1_answer)
