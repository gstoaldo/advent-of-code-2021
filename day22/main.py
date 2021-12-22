def range_to_cuboid(cuboid_range):
    cuboid = []
    rx, ry, rz = cuboid_range
    for x in range(rx[0], rx[1] + 1):
        for y in range(ry[0], ry[1] + 1):
            for z in range(rz[0], rz[1] + 1):
                cuboid.append((x, y, z))

    return cuboid


def run_steps(steps, inf=-50, sup=50):
    on_cubes = set()

    for state, cuboid_range in steps:
        if not all([inside_limits(x, inf, sup) for x in cuboid_range]):
            continue

        cuboid = range_to_cuboid(cuboid_range)

        if state == "on":
            on_cubes.update(cuboid)
        if state == "off":
            on_cubes.difference_update(cuboid)

    return on_cubes


def inside_limits(axis_range, inf, sup):
    x0, x1 = axis_range
    return x0 >= inf and x1 <= sup


def solve_part1(steps):
    return len(run_steps(steps))


###


def parse(filename):
    def parse_line(line):
        state, rest = line.split()
        return state, [
            tuple(map(int, axis[2:].split(".."))) for axis in rest.split(",")
        ]

    input = None
    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    steps = parse(filename)
    part1 = solve_part1(steps)
    part2 = None  # solve_part1(full_matrix(matrix, 5))

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
