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

    print_path(matrix, path)

    return get_path_risk(matrix, path)


def print_path(matrix, path):
    for i, row in enumerate(matrix):
        print([f" {x} " if (i, j) not in path else f"({x})" for j, x in enumerate(row)])


###


def parse(filename):
    with open(filename) as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def solve(filename):
    matrix = parse(filename)
    part1 = solve_part1(matrix)
    part2 = None  # solve_part2(template, rules)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
