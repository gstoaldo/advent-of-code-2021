def risk_level_sum(matrix):
    local_mins = get_local_mins(matrix)
    return sum([x + 1 for x in local_mins])


def get_local_mins(matrix):
    local_mins = []

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if is_local_min(matrix, i, j):
                local_mins.append(value)

    return local_mins


def is_local_min(matrix, i, j):
    return matrix[i][j] < min(get_adjacents(matrix, i, j))


def get_adjacents(matrix, i, j):
    adjacents = []
    for adj_i, adj_j in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
        if is_in_matrix(matrix, adj_i, adj_j):
            adjacents.append(matrix[adj_i][adj_j])

    return adjacents


def is_in_matrix(matrix, i, j):
    max_i = len(matrix)
    max_j = len(matrix[0])

    return 0 <= i < max_i and 0 <= j < max_j


###


def parse(filename):
    def parse_line(line):
        return [int(x) for x in line.strip()]

    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    input = parse(filename)
    part1 = risk_level_sum(input)
    # part2 = sum_outputs(input)

    return part1


if __name__ == "__main__":
    part1 = solve("input.txt")
    print(f"part1: {part1}")
    # print(f"part2: {part2}")
