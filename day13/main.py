def fold_up(dots, fy):
    return [(x, y if y < fy else 2 * fy - y) for x, y in dots]


def fold_right(dots, fx):
    return [(x if x > fx else 2 * fx - x, y) for x, y in dots]


def cut_left(dots, fx):
    return [(x - fx - 1, y) for x, y in dots]


def run_fold(dots, fold):
    axis, value = fold

    if axis == "x":
        return cut_left(fold_right(dots, value), value)

    return fold_up(dots, value)


def run_folds(dots, folds):
    for fold in folds:
        dots = run_fold(dots, fold)

    return dots


def count_unique_dots(dots):
    return len(set(dots))


def solve_part1(dots, folds):
    return count_unique_dots(run_folds(dots, folds[:1]))


###


def parse(filename):
    def parse_dot(line):
        x, y = line.strip().split(",")
        return (int(x), (int(y)))

    def parse_fold(line):
        _, fold = line.strip().split("fold along")
        axis, value = fold.strip().split("=")
        return (axis, int(value))

    with open(filename) as file:
        _dots, _folds = file.read().split("\n\n")
        dots = map(parse_dot, _dots.split("\n"))
        folds = map(parse_fold, _folds.split("\n"))

    return list(dots), list(folds)


def solve(filename):
    dots, folds = parse(filename)
    part1 = solve_part1(dots, folds)  # run_steps(input, 100)
    part2 = None  # first_full_flash(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
