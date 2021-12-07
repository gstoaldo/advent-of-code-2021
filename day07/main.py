def total_fuel(crabs, position):
    return sum(abs(crab - position) for crab in crabs)


def find_best_position(crabs):
    max_position = max(crabs)
    best_fuel = total_fuel(crabs, 0)
    best_position = 0

    for position in range(1, max_position + 1):
        fuel = total_fuel(crabs, position)
        if fuel < best_fuel:
            best_fuel = fuel
            best_position = position

    return best_fuel, best_position


def parse(filename):
    with open(filename) as file:
        input = map(int, file.read().split(","))

    return list(input)


def solve(filename):
    crabs = parse(filename)
    part1 = find_best_position(crabs)

    return part1


if __name__ == "__main__":
    part1 = solve("input.txt")
    print(f"part1: {part1[0]}, position: {part1[1]}")
