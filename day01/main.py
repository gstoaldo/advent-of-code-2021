def count_increases(depth_measurements):
    count = 0
    for i in range(1, len(depth_measurements)):
        if depth_measurements[i] > depth_measurements[i - 1]:
            count += 1

    return count


def read_file(filename):
    def line_to_int(line):
        return int(line.rstrip())

    with open(filename) as file:
        lines = file.readlines()
        data = map(line_to_int, lines)

    return list(data)


def solve(filename):
    return count_increases(read_file(filename))


if __name__ == "__main__":
    answer = solve("input.txt")
    print(answer)
