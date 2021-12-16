def get_adjacents(matrix, i, j):
    for ai, aj in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
        if 0 <= ai < len(matrix) and 0 <= aj < len(matrix[0]):
            yield (ai, aj)


def get_path(matrix, start=None, end=None):
    start = (0, 0) if start is None else start
    end = (len(matrix) - 1, len(matrix[0]) - 1) if end is None else end

    risks = [[0 for _ in row] for row in matrix]
    paths = [[start]]

    while any(path[-1] != end for path in paths):
        next_paths = []

        for path in paths:

            head = path[-1]

            if head == end:
                next_paths.append(path)
                continue

            adjacents = get_adjacents(matrix, *head)

            for adj in adjacents:
                ai, aj = adj

                path_risk = get_path_risk(matrix, path) + matrix[ai][aj]

                if risks[ai][aj] == 0 or path_risk < risks[ai][aj]:
                    next_paths.append([*path, adj])
                    risks[ai][aj] = path_risk

        paths = remove_riskier_paths(matrix, risks, next_paths)

    return paths[0]


def get_path_risk(matrix, path):
    return sum(matrix[i][j] for i, j in path[1:])


def remove_riskier_paths(matrix, risks, paths):
    best_paths = []

    for path in paths:
        i, j = path[-1]

        if get_path_risk(matrix, path) == risks[i][j]:
            best_paths.append(path)

    return best_paths


def solve_part1(matrix):
    path = get_path(matrix)

    # print_path(matrix, path)

    return get_path_risk(matrix, path)


def print_path(matrix, path):
    for i, row in enumerate(matrix):
        print([f" {x} " if (i, j) not in path else f"({x})" for j, x in enumerate(row)])


###


def full_matrix(initial_matrix, n_times=5, max_risk=9):
    hi = len(initial_matrix)
    wi = len(initial_matrix[0])
    h = hi * n_times
    w = wi * n_times
    full_matrix = [[0 for _ in range(w)] for _ in range(h)]

    for i, row in enumerate(full_matrix):
        ni = i // hi
        for j, _ in enumerate(row):
            nj = j // wi

            x = initial_matrix[i % hi][j % wi]

            hor_x = (x + nj) - ((x + nj - 1) // max_risk) * (max_risk)
            ver_x = (hor_x + ni) - (hor_x + ni - 1) // max_risk * max_risk

            full_matrix[i][j] = ver_x

    return full_matrix


###


def parse(filename):
    with open(filename) as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def solve(filename):
    matrix = parse(filename)
    part1 = solve_part1(matrix)
    part2 = solve_part1(full_matrix(matrix, 5))

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
