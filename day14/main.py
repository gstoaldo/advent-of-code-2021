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


def count_pairs(template, pairs):
    count = {pair: 0 for pair in pairs}

    for i in range(len(template) - 1):
        pair = template[i : i + 2]
        count[pair] += 1

    return count


def step_optimized(initial_pair_count, pairs):
    pair_count = {pair: 0 for pair in pairs}

    for pair, count in initial_pair_count.items():
        insert_element = pairs[pair]
        left_pair = pair[0] + insert_element
        right_pair = insert_element + pair[1]

        pair_count[left_pair] += count
        pair_count[right_pair] += count

    return pair_count


def steps_optimized(initial_template, pairs, nsteps):
    pair_count = count_pairs(initial_template, pairs)

    for _ in range(nsteps):
        pair_count = step_optimized(pair_count, pairs)

    return pair_count


def count_chars(pair_count):
    chars_count = defaultdict(lambda: 0)

    for pair, count in pair_count.items():
        chars_count[pair[0]] += count
        chars_count[pair[1]] += count

    return chars_count


def solve_part2(initial_template, pairs):
    start_char = initial_template[0]
    end_char = initial_template[-1]

    pair_count = steps_optimized(initial_template, pairs, 40)

    chars_count = count_chars(pair_count)

    chars_count[start_char] += 1
    chars_count[end_char] += 1

    merged_chars_count = {
        char: count // 2 for char, count in chars_count.items()
    }.values()

    return max(merged_chars_count) - min(merged_chars_count)


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
    part2 = solve_part2(template, rules)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
