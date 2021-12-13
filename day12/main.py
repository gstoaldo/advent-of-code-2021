from collections import defaultdict


def get_paths(graph, selected_small_cave=""):
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
                if cave == selected_small_cave and count_in_path(path, cave) < 2:
                    new_paths.append([*path, cave])
                    continue

                if is_small(cave) and cave in path:
                    continue

                new_paths.append([*path, cave])

        paths = new_paths

    return paths


def is_small(cave):
    return cave.lower() == cave


def count_in_path(path, cave):
    return len([x for x in path if x == cave])


def run_part2(graph):
    small_caves = [
        cave for cave in graph if is_small(cave) and cave != "start" and cave != "end"
    ]

    paths = []

    for cave in small_caves:
        p = get_paths(graph, cave)
        paths.extend(p)

    # gambiarra
    paths = remove_duplicates(paths)

    return len(paths)


def remove_duplicates(paths):
    unique_paths = []

    for p in paths:
        if not p in unique_paths:
            print(p)
            unique_paths.append(p)

    return unique_paths


###


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
    part2 = run_part2(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
