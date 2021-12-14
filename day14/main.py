from collections import defaultdict


def get_trio(template, pairs, i):
    pair = template[i : i + 2]
    element = pairs[pair]

    return "".join([pair[0], element, pair[1]])


def merge_trios(trios):
    return "".join([trios[0][0], *[trio[1:3] for trio in trios]])


def step(template, pairs):
    trios = []
    for i in range(len(template) - 1):
        trios.append(get_trio(template, pairs, i))

    return merge_trios(trios)


def steps(initial_template, pairs, nsteps):
    template = initial_template

    for _ in range(nsteps):
        template = step(template, pairs)

    return template


def count_elements(template):
    count = defaultdict(lambda: 0)

    for element in template:
        count[element] += 1

    return count


def solve_part1(initial_template, pairs):
    template = steps(initial_template, pairs, 10)
    count = count_elements(template).values()

    return max(count) - min(count)


###


def parse(filename):
    def parse_rules(line):
        pair, element = line.split("->")
        return (pair.strip(), element.strip())

    with open(filename) as file:
        _template, _rules = file.read().split("\n\n")
        template = _template.strip()

        rules = map(parse_rules, _rules.strip().split("\n"))
        rules = {pair: element for pair, element in rules}

    return template, rules


def solve(filename):
    template, rules = parse(filename)
    part1 = solve_part1(template, rules)
    part2 = None  # solve_part2(dots, folds)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
