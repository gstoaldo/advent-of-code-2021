def get_cover_points(p1, p2):
    cover_points = []
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            p = (x1, y)
            cover_points.append(p)
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            p = (x, y1)
            cover_points.append(p)
    else:
        line_eq = get_line_eq(p1, p2)
        for x in range(min(x1, x2), max(x1, x2) + 1):
            p = (x, int(line_eq(x)))
            cover_points.append(p)

    return cover_points


def is_horizontal_or_vertical(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x1 == x2 or y1 == y2


def mark_line(diagram, p1, p2, allow_diagonals=False):
    if not is_horizontal_or_vertical(p1, p2) and not allow_diagonals:
        return

    for point in get_cover_points(p1, p2):
        diagram.mark(point)


def get_overlaps(lines, allow_diagonals=False):
    size = get_max_coordinate(lines)
    diagram = Diagram(size)

    for p1, p2 in lines:
        mark_line(diagram, p1, p2, allow_diagonals)

    return diagram.n_overlaps()


def get_max_coordinate(lines):
    max_coordinate = 0

    for p1, p2 in lines:
        max_coordinate = max(max_coordinate, *p1, *p2)

    return max_coordinate + 1


def get_line_eq(p1, p2):
    x1, y1, x2, y2 = (*p1, *p2)
    line_m = (y2 - y1) / (x2 - x1)

    return lambda x: line_m * (x - x1) + y1


class Diagram:
    def __init__(self, size):
        self.diagram = [[0 for _ in range(0, size)] for _ in range(0, size)]

    def mark(self, point):
        self.diagram[point[0]][point[1]] += 1

    def n_overlaps(self):
        n_overlaps = 0
        for row in self.diagram:
            for n in row:
                if n > 1:
                    n_overlaps += 1

        return n_overlaps


def read_file(filename):
    def parse_line(line):
        points = line.strip().split(" -> ")
        p1 = tuple(map(int, points[0].split(",")))
        p2 = tuple(map(int, points[1].split(",")))

        return (p1, p2)

    with open(filename) as file:
        lines = file.readlines()
        data = map(parse_line, lines)

    return list(data)


def solve(filename):
    input = read_file(filename)
    part1_answer = get_overlaps(input, allow_diagonals=False)
    part2_answer = get_overlaps(input, allow_diagonals=True)

    return part1_answer, part2_answer


if __name__ == "__main__":
    part1_answer, part2_answer = solve("input.txt")
    print(f"part1: {part1_answer}")
    print(f"part2: {part2_answer}")
