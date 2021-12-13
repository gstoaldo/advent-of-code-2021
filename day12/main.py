from collections import defaultdict


def get_paths(graph):
    paths = [["start"]]

    while any(path[-1] != "end" for path in paths):
        new_paths = []

        for path in paths:
            head = path[-1]

            if head == "end":
                new_paths.append(path)
                continue

            caves = graph[head]

            for cave in caves:
                if is_small(cave) and cave in path:
                    continue

                new_paths.append([*path, cave])

        paths = new_paths

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
    part1 = len(get_paths(input))
    part2 = None

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
