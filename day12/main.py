from collections import defaultdict


def get_paths2(graph):
    paths = []
    to_visit = []
    visited = set()
    cave = "start"

    while len(to_visit) > 0:
        path = []
        while cave != "end":
            path.append(cave)
            to_visit = graph[cave]
            cave = to_visit.pop()

        paths.append(path)

    return paths


def get_paths(graph, start="start", visited=set()):
    paths = []

    if start == "end":
        return [["end"]]

    visited.add(start)

    for cave in graph[start]:

        print(cave, paths, visited)

        if is_small(cave) and cave in visited:
            continue

        for path in get_paths(graph, cave, visited):
            paths.append([start, *path])

    return paths


def is_small(cave):
    return cave.lower() == cave


def parse(filename):
    graph = defaultdict(list)

    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split("-")
            graph[key].append(value)
            graph[value].append(key)

    graph["end"] = []

    return dict(graph)


def solve(filename):
    input = parse(filename)
    part1 = get_paths(input)  # run_steps(input, 100)
    part2 = None  # first_full_flash(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("example.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
