def constant_eq(position, position_to_move):
    return abs(position - position_to_move)


def not_constant_eq(position, position_to_move):
    return sum_pa(abs(position_to_move - position))


def sum_pa(an):
    a1 = 1
    n = an
    return (a1 + an) * n / 2


def total_fuel(crabs, position, move_eq=constant_eq):
    return sum(move_eq(crab, position) for crab in crabs)


def find_best_position(crabs, move_eq=constant_eq):
    max_position = max(crabs)
    best_fuel = total_fuel(crabs, 0, move_eq)
    best_position = 0

    for position in range(1, max_position + 1):
        fuel = total_fuel(crabs, position, move_eq)
        if fuel < best_fuel:
            best_fuel = fuel
            best_position = position

    return best_fuel, best_position


###


def parse(filename):
    with open(filename) as file:
        input = map(int, file.read().split(","))

    return list(input)


def solve(filename):
    crabs = parse(filename)
    part1 = find_best_position(crabs, move_eq=constant_eq)
    part2 = find_best_position(crabs, move_eq=not_constant_eq)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1[0]}, position: {part1[1]}")
    print(f"part2: {part2[0]}, position: {part2[1]}")
