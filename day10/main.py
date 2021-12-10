PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

ERROR_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

AUTOCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_first_illegal_char(line):
    close_stack = []

    for char in line:
        if char in PAIRS:
            close_stack.append(PAIRS[char])
        elif char == close_stack[-1]:
            close_stack.pop()
        else:
            return char, list(reversed(close_stack))

    return None, list(reversed(close_stack))


def syntax_error_score(lines):
    illegal_chars = []
    for line in lines:
        illegal_char, _ = find_first_illegal_char(line)
        if illegal_char != None:
            illegal_chars.append(illegal_char)

    return sum(ERROR_POINTS[char] for char in illegal_chars)


def autocomplete_score(lines):
    scores = []
    for line in lines:
        illegal_char, chars = find_first_illegal_char(line)

        if illegal_char == None:
            scores.append(get_line_autocomplete_score(chars))

    return sorted(scores)[len(scores) // 2]


def get_line_autocomplete_score(chars):
    score = 0

    for char in chars:
        score *= 5
        score += AUTOCOMPLETE_POINTS[char]

    return score


def parse(filename):
    def parse_line(line):
        return line.strip()

    with open(filename) as file:
        input = map(parse_line, file.readlines())

    return list(input)


def solve(filename):
    input = parse(filename)
    part1 = syntax_error_score(input)
    part2 = autocomplete_score(input)

    return part1, part2


if __name__ == "__main__":
    part1, part2 = solve("input.txt")
    print(f"part1: {part1}")
    print(f"part2: {part2}")
