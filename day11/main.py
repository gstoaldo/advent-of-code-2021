import math


def run_steps(states, nsteps):
    flash_count = 0
    for _ in range(nsteps):
        new_states, step_flash_count = step(states)
        flash_count += step_flash_count
        states = new_states

    return flash_count


def step(states):
    states = add_one(states)
    flashes = []

    while full_energy_count(states) > 0:
        for i, row in enumerate(states):
            for j, state in enumerate(row):
                if (i, j) not in flashes and state >= 10:
                    flashes.append((i, j))
                    states[i][j] = 0

                    for ai, aj in get_adjacents(states, i, j):
                        if (ai, aj) not in flashes:
                            states[ai][aj] += 1

    return states, len(flashes)


def add_one(states):
    return [[x + 1 for x in row] for row in states]


def full_energy_count(states):
    return sum(sum(1 for x in row if x >= 10) for row in states)


def get_adjacents(matrix, i, j):
    adjacents = []
    for x in range(0, 8):
        angle = x * math.pi / 4
        di, dj = int(round(math.sin(angle))), int(round(math.cos(angle)))
        ai, aj = i + di, j + dj

        if is_in_matrix(matrix, ai, aj):
            adjacents.append((ai, aj))

    return adjacents


def is_in_matrix(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


###


def first_full_flash(states):
    step_index = 0

    while not is_zero_energy(states):
        new_states, _ = step(states)
        step_index += 1
        states = new_states

    return step_index


def is_zero_energy(states):
    return sum(sum(x for x in row) for row in states) == 0


###


def parse(filename):
    def parse_line(line):
        return [int(x) for x in line.strip()]

    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    input = parse(filename)
    part1 = run_steps(input, 100)
    part2 = first_full_flash(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
