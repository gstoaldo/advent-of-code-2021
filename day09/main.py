def risk_level_sum(matrix):
    local_mins, _ = get_local_mins(matrix)
    return sum([x + 1 for x in local_mins])


def get_local_mins(matrix):
    local_mins = []
    local_mins_ij = []

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if is_local_min(matrix, i, j):
                local_mins.append(value)
                local_mins_ij.append((i, j))

    return local_mins, local_mins_ij


def is_local_min(matrix, i, j):
    return matrix[i][j] < min(
        map(lambda ij: matrix[ij[0]][ij[1]], get_adjacents(matrix, i, j))
    )


def get_adjacents(matrix, i, j):
    adjacents = []
    for adj_i, adj_j in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
        if is_in_matrix(matrix, adj_i, adj_j):
            adjacents.append((adj_i, adj_j))

    return adjacents


def is_in_matrix(matrix, i, j):
    max_i = len(matrix)
    max_j = len(matrix[0])

    return 0 <= i < max_i and 0 <= j < max_j


###


def get_basin(matrix, i, j, basin=[]):
    if len(basin) == 0:
        basin = [(i, j)]

    adjacents = [
        (ai, aj)
        for (ai, aj) in get_adjacents(matrix, i, j)
        if matrix[ai][aj] < 9 and (ai, aj) not in basin
    ]

    basin.extend(adjacents)

    for adj in adjacents:
        get_basin(matrix, adj[0], adj[1], basin)

    return basin


def get_all_basins(matrix):
    basins = []
    _, local_mins_ij = get_local_mins(matrix)
    for (i, j) in local_mins_ij:
        basins.append(get_basin(matrix, i, j))

    return basins


def get_largest_basins(matrix, n_basins=3):
    basins = get_all_basins(matrix)
    largest = sorted(basins, key=len, reverse=True)[:n_basins]

    prod = 1

    for basin in largest:
        prod *= len(basin)

    return prod, [len(basin) for basin in largest]


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
    part2, _ = get_largest_basins(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
