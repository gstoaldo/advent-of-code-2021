### part1 naive


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


### part2


def get_1D_intersection(range_a, range_b):
    x1a, x2a = range_a
    x1b, x2b = range_b

    x1 = max(x1a, x1b)
    x2 = min(x2a, x2b)

    return (x1, x2) if x2 >= x1 else False


def get_3D_intersection(range_a, range_b):
    intersection_3D = []

    for ra, rb in zip(range_a, range_b):
        intersection_1D = get_1D_intersection(ra, rb)

        if not intersection_1D:
            return False

        intersection_3D.append(intersection_1D)

    return intersection_3D


def run_steps2(steps):
    on_cuboides = []
    off_cuboides = []

    for state, step_cuboid in steps:
        off_copy = [*off_cuboides]
        on_copy = [*on_cuboides]
        for cuboid in off_copy:
            intersection = get_3D_intersection(step_cuboid, cuboid)

            if intersection:
                on_cuboides.append(intersection)

        for cuboid in on_copy:
            intersection = get_3D_intersection(step_cuboid, cuboid)

            if intersection:
                off_cuboides.append(intersection)

        if state == "on":
            on_cuboides.append(step_cuboid)

    return on_cuboides, off_cuboides


def count_cubes(cuboid):
    product = 1
    for dim in cuboid:
        product *= dim[1] - dim[0] + 1

    return product


def solve_part2(steps):
    on_cuboides, off_cuboides = run_steps2(steps)

    return sum(map(count_cubes, on_cuboides)) - sum(map(count_cubes, off_cuboides))


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
    part2 = solve_part2(steps)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
