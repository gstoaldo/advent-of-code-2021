# part 1
def count_increases(depth_measurements):
    count = 0
    for i in range(1, len(depth_measurements)):
        if depth_measurements[i] > depth_measurements[i - 1]:
            count += 1

    return count


# part 2
def count_window_increases(depth_measurements, window_length=3):
    count = 0
    for i in range(window_length, len(depth_measurements)):
        if sum_window(depth_measurements, i, window_length) > sum_window(
            depth_measurements, i - 1, window_length
        ):
            count += 1

    return count


def sum_window(data, index, window_length):
    return sum(data[index - window_length + 1 : index + 1])


def read_file(filename):
    def line_to_int(line):
        return int(line.rstrip())

    with open(filename) as file:
        lines = file.readlines()
        data = map(line_to_int, lines)

    return list(data)


def solve(filename):
    input = read_file(filename)
    part1_answer = count_increases(input)
    part2_answer = count_window_increases(input)

    return part1_answer, part2_answer


if __name__ == "__main__":
    part1_answer, part2_answer = solve("input.txt")
    print(part1_answer, part2_answer)
